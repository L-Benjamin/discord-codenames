from .state import State


class Teaming(State):
    
    async def help(self, channel, user, args):        
        await channel.send((
            "Waiting for someone to start :checkered_flag: the game with `*start`. You can also change teams with "
            "the command `*team change` to change teams or `*team switch` to switch role with your team-mate. "
            "Alternatively, do `*quit` if you want to quit the game.\n"
            "Here is the current composition of the teams:\n:red_circle: Red team:\n{}:blue_circle: Blue team:\n{}"
            "*You can always do* `*reset` *to reset the bot*"
        ).format(
            self.data.fmt_players([0, 1]),
            self.data.fmt_players([2, 3]),
        ))

    async def quit(self, channel, user, args):
        if not self.data.in_game(user):
            await channel.send("You didn't even join!")
            return

        self.data.remove_player(user)

        from .joining import Joining
        new_state = Joining(self.data)
        await new_state.help(channel, None, None)
        return new_state

    async def start(self, channel, user, args):
        if not self.data.in_game(user):
            await channel.send("You are not even playing!")
            return

        from .clueing import Clueing
        new_state = Clueing(self.data)
        await new_state.help(channel, None, None)
        return new_state

    async def team(self, channel, user, args):
        if not self.data.in_game(user):
            await channel.send("You are not even playing!")
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
