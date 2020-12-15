# Methods of State that don't start with an underscore must 
# be async and take 4 arguments:
# - self
# - channel: a discord channel
# - user: a discord user
# - args: a list of strings
# Those methods will be automatically called when a user uses a command
# with the same name as one of those methods.

from data import Data


# Mother class of all other states
class State:

    # Create a new state with the given data
    def __init__(self, data):
        self.data = data

    # Reset the game when called. Need confirmation for safety
    async def reset(self, channel, user, args):
        if len(args) < 2 or args[1] != "confirm":
            await channel.send((
                "Are you sure you want to reset the game ? All progress will be lost. "
                "Type `*reset confirm` to confirm resetting."
            ))
        else:
            await channel.send("Game reset.")
            from .default import Default
            new_state = Default(Data())
            await new_state.help(channel, None, None)
            return new_state