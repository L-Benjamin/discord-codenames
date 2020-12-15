from .state import State


_USAGE = (
    "`*guess xxx yyy zzz ...` where `xxx yyy zzz ...` are your guesses "
    "(words with no spaces), in order. They will be treated from leftmost to rightmost"
)

class Guessing(State):

    async def guess(self, channel, user, args):
        team = self.data.fmt_team_name()
        all, ours, theirs, gray, black = self.data.words_lists()

        if not self.data.in_game(user):
            await channel.send("You are not even playing!")
            return
        elif user != self.data.get_playing():
            await channel.send("It's not your turn yet!")
            return
        elif len(args) < 2:
            await channel.send("Invalid number of arguments to `*guess`, correct usage is {}".format(_USAGE))
            return
        elif len(args) > len(ours) + 1:
            await channel.send("You can't make that many guesses ! You only need {} more.".format(len(ours)))
            return

        for guess in args[1:]:
            if not guess in all:
                await channel.send("`{}` is not a valid guess, it's not in the list!".format(guess))
            elif guess in ours:
                ours.remove(guess)
                all.remove(guess)
                self.data.set_done_guess(True)
                await channel.send("`{}` was one of your words, +1 for {} team!".format(guess, team))
            elif guess in theirs:
                theirs.remove(guess)
                all.remove(guess)
                await channel.send("Unfortunately, `{}` was one of the other team's words, +1 for them! Your turn is over.".format(guess))
                self.data.set_done_guess(True)
                return await self.end(channel, user, None)
            elif guess in gray:
                gray.remove(guess)
                all.remove(guess)
                await channel.send("Unfortunately, `{}` was a gray word, your turn is over!".format(guess))
                self.data.set_done_guess(True)
                return await self.end(channel, user, None)
            elif guess == black:
                await channel.send((
                    "Bad luck! `{}` was the black word, {} team just lost the game. "
                    "Congratulations to {} and {} for winning the game :partying_face:!"
                ).format(
                    guess, 
                    team,
                    self.data.get_next_playing(1).display_name,
                    self.data.get_next_playing(2).display_name,
                ))

                self.data.reset()
                from .teaming import Teaming
                new_state = Teaming(self.data)
                await new_state.help(channel, None, None)
                return new_state

        if len(ours) == 0:
            await channel.send((
                "That was the last word you needed to guess! "
                "The {} team won! Congratulations to {} and {} for winning the game :partying_face:!"
            ).format(
                team,
                self.data.get_next_playing(3).display_name,
                self.data.get_playing().display_name,
            ))
            
            self.data.reset()
            from .teaming import Teaming
            new_state = Teaming(self.data)
            await new_state.help(channel, None, None)
            return new_state
        elif len(theirs) == 0:
            await channel.send((
                "That was the last of their words, {} team just lost the game"
                "Congratulations to {} and {} for winning the game :partying_face:!"
            ).format(
                team,
                self.data.get_next_playing(1).display_name,
                self.data.get_next_playing(2).display_name,
            ))

            self.data.reset()
            from .teaming import Teaming
            new_state = Teaming(self.data)
            await new_state.help(channel, None, None)
            return new_state
        
        await self.help(channel, None, None)

    async def end(self, channel, user, args):
        if not self.data.in_game(user):
            await channel.send("You are not even playing!")
            return
        elif user != self.data.get_playing():
            await channel.send("It's not your turn yet!")
            return

        if self.data.done_guess:
            await channel.send("Next turn!")
            self.data.next_turn()
            from .clueing import Clueing
            new_state = Clueing(self.data)
            await new_state.help(channel, None, None)
            return new_state
        else:
            await channel.send("You still haven't done a single guess!")

    async def help(self, channel, user, args):
        if self.data.has_done_guess():
            hint = "Do `*end` to end your turn if you want to"
        else:
            hint = "You still need to make at least one guess"

        await channel.send((
            "This is {} team's turn, we are currently waiting for "
            "{} to make a guess based off of {}'s clue, which was `{}` :thinking:. {}. "
            "Here is the available words list :book::\n{}"
            "To make a guess, do {}."
        ).format(
            self.data.fmt_team_name(),
            self.data.get_playing().mention,
            self.data.get_next_playing(3).display_name,
            self.data.get_clue(),
            hint,
            self.data.fmt_words(),
            _USAGE,
        ))