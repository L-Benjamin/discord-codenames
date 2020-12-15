from .state import State


_USAGE = (
    "`*clue xxx n` where `xxx` is your clue (a single word with no spaces) "
    "and `n` is the number of words your team-mate should be able to guess (only informative)"
)

class Clueing(State):

    async def clue(self, channel, user, args):
        if not self.data.in_game(user):
            await channel.send("You are not even playing!")
            return
        elif user != self.data.get_playing():
            await channel.send("It's not your turn yet!")
            return
        elif len(args) != 3:
            await channel.send("Invalid number of arguments to `*clue`, correct usage is {}.".format(_USAGE))
            return

        try:
            n = int(args[2])
        except:
            await channel.send("Not a valid number: `{}`, correct usage is {}.".format(args[2], _USAGE))
            return

        _, ours, theirs, _, _ = self.data.words_lists()

        if n > len(ours):
            await channel.send("That's too many guess! You only need {} more words to win the game.".format(len(ours)))
            return
        elif n < 1:
            await channel.send("You need to ask for at least one guess!".format(len(ours)))
            return

        # Here verify the clue does not break any rules, if needed

        self.data.set_clue(args[1])
        self.data.set_done_guess(False)
        self.data.next_turn()
        
        from .guessing import Guessing
        new_state = Guessing(self.data)
        await new_state.help(channel, None, None)
        return new_state
    
    async def help(self, channel, user, args):
        await channel.send((
            "This is {} team's turn, we are currently waiting for "
            "{} to give a clue to {}, so he can make guesses.\n{}"
            "Here is the available words list :book::\n{}"
            "Do `*key` :key: to get the list of words you need to make your team-mate guess, "
            "or, if you are ready to give your clue, do {}."
        ).format(
            self.data.fmt_team_name(),
            self.data.get_playing().mention,
            self.data.get_next_playing(1).display_name,
            self.data.fmt_teams(),
            self.data.fmt_words(),
            _USAGE,
        ))

    async def key(self, channel, user, args):
        if not self.data.in_game(user):
            await channel.send("You are not even playing!")
            return
        elif not (idx := self.data.index_of_player(user)) in [0, 2]:
            await channel.send("It's not your turn yet!")
            return

        _, ours, theirs, gray, black = self.data.fmt_words_lists(idx == 2)

        await user.send((
            "Here is the list of words you need to make your team-mate guess :white_check_mark::\n{}"
            "Here is the list of words the other team needs to guess :x::\n{}"
            "Here is the list of words that won't give anyone any points :sleeping::\n{}"
            "Finally, here is the word that will make you lose if your team-mate guesses it :skull_crossbones::\n{}"
        ).format(
            ours,
            theirs,
            gray,
            black,
        ))


