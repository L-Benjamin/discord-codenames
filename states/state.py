# Methods of State that don't start with an underscore must 
# be async and take 4 arguments:
# - self
# - channel: a discord channel
# - user: a discord user
# - args: a list of strings
# Those methods will be automatically called when a user uses a command
# with the same name as one of those methods.

from .data import Data


class State:

    def __init__(self, data = Data()):
        self.data = data

    async def exit(self, channel, user, args):
        if len(args) < 2 or args[1] != "confirm":
            await channel.send((
                "Are you sure you want to exit the game ? All progress will be lost. "
                "Type `*exit confirm` to confirm exiting."
            ))
        else:
            await channel.send("Game terminated.")
            from .default import Default
            new_state = Default()
            await new_state.help(channel, None, None)
            return new_state