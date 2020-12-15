# discord-codenames

In this repository, you'll find the source code for a discord bot able to play the board game [Code Names](https://codenames.game) inside of your discord server.

# How to use

You will need `python3` and the two followng python libraries: `discord` and `python-dotenv`.

Create a file named `.env` in the root of the repository, and in it put `DISCORD_TOKEN=<your bot token>`. Of course, replace `<your bot token>` by a bot token, generated on [discord's developper portal](https://discord.com/login?redirect_to=%2Fdevelopers%2Fapplications).

Invite your bot to your server via the portal, the bot needs to be able to read and send messages (including private ones).

Finally, do `python3 bot.py` to launch the bot. Start a new game with `*new`, in the discord chat.

