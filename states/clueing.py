from .state import State

class Clueing(State):

    async def clue(self, channel, user, args):
        pass
    
    async def help(self, channel, user, args):
        i = self.data.turn
        team = "red" if self.data.turn == 0 else "blue"

        await channel.send((
            "This is {} team's turn, we are currently waiting for "
            "{} to give a clue to {}, so he can make guesses.\n{}\n"
            "Here is the available words list:\n{}\n"
            "Do `*key` to get the list of words you need to make guess, or do "
            "`*clue xxx n` to give your clue, where `xxx` is your clue (a single "
            "word with no spaces) and `n` is the number of words your team-mate will have "
            "to guess."
        ).format(
            team,
            self.data.players[self.data.turn].mention,
            self.data.players[self.data.turn + 1].display_name,
            self.data.players_str(),
            self.data.words_str(),
        ))

    async def key(self, channel, user, args):
        if not user in self.data.players:
            await channel.send("You are not even playing !")
            return
        elif user != self.data.playing():
            await channel.send("It's not your turn !")
            return

        ours = self.data.red_words_str()
        theirs = self.data.blue_words_str()

        if self.data.turn == 2:
            ours, theirs = theirs, ours

        await user.send((
            "Here is the list of words you need to make your team-mate guess:\n{}\n "
            "Here is the list of words the other team need to guess:\n{}\n "
            "Here is the list of words that won't give anyone any points:\n{}\n "
            "Finally, here is the word that will make you lose of your team-mate guesses it:\n`{}`"
        ).format(
            self.data.words_str(),
            ours,
            theirs,
            self.data.gray_words_str(),
            self.data.black_word
        ))

        await channel.send("Sent the key to you, {}, go check your DMs.".format(user.display_name))


