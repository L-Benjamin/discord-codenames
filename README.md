# discord-codenames

In this repository, you'll find the source code for a discord bot able to play the board game [Code Names](https://codenames.game) inside of your discord server.

## How to use

You will need `python3` and the two followng python libraries: `discord` and `python-dotenv`.

Create a file named `.env` in the root of the repository, and in it put `DISCORD_TOKEN=<your bot token>`. Of course, replace `<your bot token>` by a bot token, generated on [discord's developper portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications).

Invite your bot to your server via the portal, the bot needs to be able to read and send messages (including private ones).

Finally, do `python3 bot.py` to launch the bot. Start a new game with `*new`, in the discord chat.

## Implementation details

The code is entirely in Python for convenience reason, buit on top of the [discord.py](https://discordpy.readthedocs.io/en/latest/) api.

The global architecture is very simple, a bunch of states are declared in `states/`, and all define classes that acts as the different states of the program. They all posses a field `data` that they pass from one state to another upon changing. In `bot.py`, any command the user types is parsed and it's name is searched among the methods of the current state, and then called automatically.