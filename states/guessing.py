from .state import State

_USAGE = ""

class Guessing(State):

    async def guess(self, channel, user, args):
        if not user in self.data.players:
            await channel.send("You are not even playing !")
            return
        elif user != self.data.playing():
            await channel.send("It's not your turn yet !")
            return
        elif len(args) < 2:
            await channel.send("Invalid number of arguments to guess, correct usage is {}".format(_USAGE))
            return
    
    async def help(self, channel, user, args):
        pass
