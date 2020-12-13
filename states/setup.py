from .state import State

class Setup(State):

    async def help(self, channel, user, args):
        await channel.send("hello")