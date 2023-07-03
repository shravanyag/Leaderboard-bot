import os
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix = ".")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

my_secret = os.environ['DISCORD_BOT_TOKEN']

keep_alive()
bot.run(my_secret)
