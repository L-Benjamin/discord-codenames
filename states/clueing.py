from .guessing import Guessing
from .state import State

_USAGE = (
    "`*clue xxx n` where `xxx` is your clue (a single word with no spaces) "
    "and `n` is the number of words your team-mate will have to guess"
)

class Clueing(State):

    async def clue(self, channel, user, args):
        if not user in self.data.players:
            await channel.send("You are not even playing !")
            return
        elif user != self.data.playing():
            await channel.send("It's not your turn yet !")
            return
        elif len(args) != 3:
            await channel.send("Invalid number of arguments to clue, correct usage is {}".format(_USAGE))
            return
        
        try:
            n = int(args[2])
        except:
            await channel.send("Not a valid number: `{}`, correct usage is ".format(args[2], _USAGE))
            return

        ours, theirs = self.data.lists()

        if n > len(ours):
            await channel.send("That's too many guess ! You only need {} more words to win the game.".format(len(ours)))
            return
        elif n < 1:
            await channel.send("You need to ask for at least one guess !".format(len(ours)))
            return

        # Here verify the clue does not break any rules, if needed

        self.data.clue = args[1]
        self.data.nguess = n
        
        new_state = Guessing(self.data)
        await new_state.help(channel, None, None)
        return new_state
    
    async def help(self, channel, user, args):
        i = self.data.turn
        team = "red" if self.data.turn == 0 else "blue"

        await channel.send((
            "This is {} team's turn, we are currently waiting for "
            "{} to give a clue to {}, so he can make guesses.\n{}\n"
            "Here is the available words list:\n{}\n"
            "Do `*key` to get the list of words you need to make guess, or do {}"
        ).format(
            team,
            self.data.players[self.data.turn].mention,
            self.data.players[self.data.turn + 1].display_name,
            self.data.players_str(),
            self.data.words_str(),
            _USAGE,
        ))

    async def key(self, channel, user, args):
        if not user in self.data.players:
            await channel.send("You are not even playing !")
            return
        elif user != self.data.playing():
            await channel.send("It's not your turn yet !")
            return

        ours, theirs = self.data.lists_str()

        await user.send((
            "Here is the list of words you need to make your team-mate guess:\n{}\n "
            "Here is the list of words the other team needs to guess:\n{}\n "
            "Here is the list of words that won't give anyone any points:\n{}\n "
            "Finally, here is the word that will make you lose if your team-mate guesses it:\n`{}`"
        ).format(
            ours,
            theirs,
            self.data.gray_words_str(),
            self.data.black_word,
        ))

        await channel.send("Sent the key to you, {}, go check your DMs.".format(user.display_name))


