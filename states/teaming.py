from .state import State


class Teaming(State):
    
    async def help(self, channel, user, args):        
        await channel.send((
            "Waiting for someone to start the game with `*start`. You can also change teams with "
            "the command `*team change` to change teams or `*team switch` to switch role with your team-mate.\n"
            "Here is the current composition of the teams:\nRed team:\n{}Blue team:\n{}"
        ).format(
            self.data.fmt_players([0, 1]),
            self.data.fmt_players([2, 3]),
        ))

    async def start(self, channel, user, args):
        if not self.data.in_game(user):
            await channel.send("You are not even playing !")
            return

        from .clueing import Clueing
        new_state = Clueing(self.data)
        await new_state.help(channel, None, None)
        return new_state

    async def team(self, channel, user, args):
        if not self.data.in_game(user):
            await channel.send("You are not even playing !")
            return

        _USAGE = "correct usage is `*team (change|switch)`."

        i = self.data.index_of_player(user)

        if len(args) < 2:
            await channel.send("Not enough arguments to `*team`, {}".format(_USAGE))
            return
        elif args[1] == "change":
            j = (i + 2) % 4
        elif args[1] == "switch":
            j = i + 1 if i % 2 == 0 else i - 1
        else:
            await channel.send("Invalid argument to `*team`, {}".format(_USAGE))
            return

        self.data.switch_players(i, j)

        await self.help(channel, None, None)

    async def quit(self, channel, user, args):
        if not self.data.is_in_game(user):
            await channel.send("You didn't even join !")
            return

        self.data.remove_player(user)
        
        if self.data.num_players() == 0:
            from .teaming import Teaming
            new_state = Teaming(self.data)
            await new_state.help(channel, None, None)
            return new_state

