from .state import State


class Joining(State):
    
    async def help(self, channel, user, args):
        await channel.send((
            "We are now ({}/4) players, waiting for more players to join :hugging:.\n{}"
            "Type `*join` to join the game. "
            "Alternatively, do `*quit` if you want to quit the lobby."   
        ).format(
            self.data.num_players(), 
            self.data.fmt_players(range(self.data.num_players())),
        ))

    async def join(self, channel, user, args):
        if self.data.add_player(user):
            from .teaming import Teaming
            new_state = Teaming(self.data)
            await new_state.help(channel, user, args)
            return new_state
        else:
            await self.help(channel, None, None)

    async def quit(self, channel, user, args):
        if not self.data.in_game(user):
            await channel.send("You didn't even join!")
            return

        self.data.remove_player(user)
        
        if self.data.num_players() == 0:
            from .default import Default
            new_state = Default()
            await new_state.help(channel, None, None)
            return new_state
        else:
            await self.help(channel, None, None)