from discord import player
from states.teaming import Teaming
from .state import State

class Joining(State):
    
    async def help(self, channel, user, args):
        n = len(self.data.players)
        player_list = ""
        if n != 0:
            player_list = "```\n" + "".join((p.display_name + "\n" for p in self.data.players)) + "```\n"

        await channel.send((
            "We are now ({}/4) players, waiting for more players to join\n"
            "{}"
            "Type `*join` to join the game"
        ).format(n, player_list))

    async def join(self, channel, user, args):
        self.data.players += [user]
        if len(self.data.players) == 4:
            new_state = Teaming(self.data)
            await new_state.help(channel, user, args)
            return new_state
        else:
            await self.help(channel, user, args)
