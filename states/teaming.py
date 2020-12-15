from .state import State


class Teaming(State):
    
    async def help(self, channel, user, args):        
        await channel.send((
            "Waiting for someone to start the game with `*start`. You can also change teams with "
            "the command `*team change` to change or `*team switch` to switch role with your teammate.\n"
            "Here is the current composition of the teams:\nRed team:\n```\n{}\n{}\n```Blue team:\n```\n{}\n{}\n```"
        ).format(
            self.data.players[0].display_name,
            self.data.players[1].display_name,
            self.data.players[2].display_name,
            self.data.players[3].display_name,
        ))

    async def start(self, channel, user, args):
        if not user in self.data.players:
            await channel.send("You are not even playing !")
            return

        from .clueing import Clueing
        new_state = Clueing(self.data)
        await new_state.help(channel, None, None)
        return new_state

    async def team(self, channel, user, args):
        if not user in self.data.players:
            await channel.send("You are not even playing !")
            return

        _USAGE = "correct usage is `*team (change|switch)`."

        i = self.data.players.index(user)

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

        self.data.players[i], self.data.players[j] = self.data.players[j], self.data.players[i]

        await self.help(channel, None, None)

