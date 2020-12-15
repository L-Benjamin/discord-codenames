from states.state import State


# Handle waiting when no one wants to play
class Default(State):
    
    # Display help 
    async def help(self, channel, user, args):
        await channel.send("Waiting for someone to start a new game with the command `*new`.")

    # Start a new game
    async def new(self, channel, user, args):
        from .joining import Joining
        new_state = Joining(self.data)
        await new_state.help(channel, None, None)
        return new_state
