if __name__ == "__main__":
    
    import discord
    from dotenv import load_dotenv
    from inspect import ismethod
    from os import getenv

    from states.setup import Setup

    STATES = {}
    READY = False

    load_dotenv()
    token = getenv("DISCORD_TOKEN")

    client = discord.Client()

    @client.event
    async def on_ready():
        status = discord.Status.online
        activity = discord.Game(name="Code Names")

        global STATES

        for guild in client.guilds:
            STATES[guild] = Setup()
            await client.change_presence(status=status, activity=activity)

        global READY
        READY = True

        print("--- bot is ready ---")

    @client.event
    async def on_message(msg):
        channel = msg.channel
        user = msg.author

        if msg.author == client.user:
            return

        if msg.content[0] != "*":
            return

        global READY
        if not READY:
            await msg.channel.send("I am not ready yet, wait a bit more please!")
            return

        if not msg.guild:
            await msg.channel.send("You can't use any commands in DMs")
            return

        if len(args := msg.content[1:].split(" ")) == 0:
            return

        global STATES
        state = STATES[msg.guild]

        if args[0] != "_" and ismethod(method := getattr(state, args[0])):
            if newstate := await method(channel, user, args):
                STATES[msg.guild] = newstate
        else:
            await channel.send("Command not found, type `*help` to get a list of commands")

    client.run(token)