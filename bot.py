if __name__ == "__main__":
    
    from discord import Client, Game, Status
    from dotenv import load_dotenv
    from inspect import ismethod
    from os import getenv

    from data import Data
    from states.default import Default

    STATES = {}
    READY = False

    # Load discord token from .env file
    load_dotenv()
    token = getenv("DISCORD_TOKEN")

    # Create the bot
    client = Client()

    @client.event
    async def on_ready():
        status = Status.online
        activity = Game(name = "Code Names (*help)")

        global STATES
        for guild in client.guilds:
            # Initialize server's state
            STATES[guild] = Default(Data())
            # Set bot's status
            await client.change_presence(status=status, activity=activity)

        # Set bot ready to start operating
        global READY
        READY = True

        # Log
        print("bot ready")

    @client.event
    async def on_message(msg):
        channel = msg.channel
        content = msg.content
        user = msg.author

        # If msg comes from the bot or does not start with a *, do nothing
        if user == client.user or content[0] != "*":
            return

        # If bot is not ready yet, ask for more time
        global READY
        if not READY:
            await channel.send("I am not ready yet, wait a bit more please!")
            return

        # If message was sent from a private channel
        if not msg.guild:
            await channel.send("You can't use any commands in DMs.")
            return

        # Parse msg into a list, returning if the list is empty
        if len(args := content[1:].split(" ")) == 0:
            return

        # Get the state corresponding to that server
        global STATES
        state = STATES[msg.guild]

        # Search for a method that does not start with an underscore in the state object, if it
        # exist and is a method, invoke it with the channel the msg comes, it's sender and the
        # parsed arguments
        if args[0] != "" and args[0][0] != "_" and args[0] in dir(state) and ismethod(method := getattr(state, args[0])):
            if newstate := await method(channel, user, args):
                STATES[msg.guild] = newstate
        else:
            await channel.send("Command does not exist or is not available for now :slight_frown:, type `*help` if you feel lost.")

    # Launch the bot
    client.run(token)
