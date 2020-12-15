from .state import State


_USAGE = (
    "`*guess xxx yyy zzz ...` where `xxx yyy zzz ...` are your guesses "
    "(words with no spaces), in order. They will be treated from leftmost to rightmost"
)

class Guessing(State):

    async def guess(self, channel, user, args):
        team = self.data.team_str()
        ours, theirs = self.data.lists()

        if not user in self.data.players:
            await channel.send("You are not even playing !")
            return
        elif user != self.data.playing():
            await channel.send("It's not your turn yet !")
            return
        elif len(args) < 2:
            await channel.send("Invalid number of arguments to `*guess`, correct usage is {}".format(_USAGE))
            return
        elif len(args) > len(ours) + 1:
            await channel.send("You can't make that many guesses ! You only need {} more.".format(len(ours)))
            return

        for guess in args[1:]:
            if not guess in self.data.words:
                await channel.send("`{}` is not a valid guess, it's not in the list !".format(guess))
            elif guess in ours:
                ours.remove(guess)
                self.data.words.remove(guess)
                self.data.done_guess = True
                self.data.nguess -= 1
                await channel.send("`{}` was one of your words, +1 for {} team !".format(guess, team))
            elif guess in theirs:
                theirs.remove(guess)
                self.data.words.remove(guess)
                self.data.done_guess = True
                await channel.send("Unfortunately, `{}` was one of the other team's words, +1 for them ! Your turn is over.".format(guess))
                await self.stop(channel, user, None)
                break
            elif guess in self.data.gray_words:
                self.data.gray_words.remove(guess)
                self.data.words.remove(guess)
                self.data.done_guess = True
                await channel.send("Unfortunately, `{}` was a gray word, your turn is over !".format(guess))
                await self.stop(channel, user, None)
                break
            elif guess == self.data.black_word:
                await channel.send((
                    "Bad luck ! `{}` was the black word, {} team just lost the game."
                    "Congratulations to {} and {} for winning the game !"
                ).format(
                    guess, team,
                    self.data.players[(self.data.turn + 1) % 4].display_name,
                    self.data.players[(self.data.turn + 2) % 4].display_name,
                ))
                self.data.reset()
                from .teaming import Teaming
                new_state = Teaming(self.data)
                await new_state.help(channel, None, None)
                return new_state

        if len(ours) == 0:
            await channel.send((
                "That was the last word you needed to guess !"
                "The {} team won ! Congratulations to {} and {} for winning the game !"
            ).format(
                team,
                self.data.players[self.data.turn-1].display_name,
                self.data.players[self.data.turn].display_name,
            ))
            self.data.reset()
            from .teaming import Teaming
            new_state = Teaming(self.data)
            await new_state.help(channel, None, None)
            return new_state
        
        await self.help(channel, None, None)

    async def end(self, channel, user, args):
        if not user in self.data.players:
            await channel.send("You are not even playing !")
            return
        elif user != self.data.playing():
            await channel.send("It's not your turn yet !")
            return

        if self.data.done_guess:
            await channel.send("Next turn !")
            self.data.turn += 1
            self.data.turn %= 4
            from .clueing import Clueing
            new_state = Clueing(self.data)
            await new_state.help(channel, None, None)
            return new_state
        else:
            await channel.send("You still haven't done a single guess !")

    async def help(self, channel, user, args):
        team = self.data.team_str()

        await channel.send((
            "This is {} team's turn, we are currently waiting for "
            "{} to make a guess based off of {}'s clue, which was `{}`. "
            "He said you can still do {} guesses. {}\n"
            "Here is the available words list:\n{}\n"
            "To make a guess, do {}."
        ).format(
            team,
            self.data.players[self.data.turn].mention,
            self.data.players[self.data.turn - 1].display_name,
            self.data.clue,
            self.data.nguess,
            "Do `*end` to end your turn if you want to." if self.data.done_guess else "You still need to make at least one guess",
            self.data.words_str(),
            _USAGE,
        ))