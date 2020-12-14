from .joining import Joining
from .state import State

class Default(State):
    
    async def help(self, channel, user, args):
        await channel.send("Waiting for someone to start a new game with the command `*new`")

    async def new(self, channel, user, args):
        new_state = Joining(self.data)
        await new_state.help(channel, None, None)
        return new_state
