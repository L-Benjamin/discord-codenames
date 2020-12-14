if __name__ == "__main__":
    
    from discord import Client, Game, Status
    from dotenv import load_dotenv
    from inspect import ismethod
    from os import getenv

    from states.default import Default

    STATES = {}
    READY = False

    load_dotenv()
    token = getenv("DISCORD_TOKEN")

    client = Client()

    @client.event
    async def on_ready():
        status = Status.online
        activity = Game(name = "Code Names")

        global STATES
        for guild in client.guilds:
            STATES[guild] = Default()
            await client.change_presence(status=status, activity=activity)

        global READY
        READY = True

        print("bot ready")

    @client.event
    async def on_message(msg):
        channel = msg.channel
        content = msg.content
        user = msg.author

        if user == client.user:
            return

        if len(content) < 2 or content[0] != "*":
            return

        global READY
        if not READY:
            await channel.send("I am not ready yet, wait a bit more please!")
            return

        if not msg.guild:
            await channel.send("You can't use any commands in DMs")
            return

        if len(args := content[1:].split(" ")) == 0:
            return

        global STATES
        state = STATES[msg.guild]

        if args[0][0] != "_" and ismethod(method := getattr(state, args[0])):
            if newstate := await method(channel, user, args):
                STATES[msg.guild] = newstate
        else:
            await channel.send("Command not found, type `*help` to get a list of commands")

    client.run(token)