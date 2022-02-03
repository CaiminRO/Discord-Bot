import os

import discord
from discord.ext import commands


"""
# logger (when hosted locally)
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
"""

# command prefix intialize
bot = commands.Bot(command_prefix=commands.when_mentioned_or('$'))


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))



@bot.command(name = "setprefix")
async def update_prefix(ctx, arg1: str):
    print('Command issued (setprefix) with argument: ' + arg1)

    bot = commands.Bot(command_prefix=commands.when_mentioned_or(arg1))
    await ctx.send("Changed command prefix to: " + arg1)

@bot.command(name = "echo", aliases=["repeat", "mimic"])
async def  copy_user(ctx, message: str):
    print('Command issued (echo / mimic / repeat) with argument: ' + arg1)
    
    await ctx.send(message)

@bot.command(name = "argcount", aliases=["argcheck"])
async def  num_args(ctx, *args):
    print('Command issued (argcheck / argcount) with {} arguments: {}'.format(len(args), ', '.join(args)))

    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


"""
# bot token (provided by hidden file when hosted locally)
f = open("token", 'r')
TOKEN = f.read()
"""

# discord bot login using token (provided when hosted through Heroku)
TOKEN = os.getenv("DISCORD_TOKEN")

if __name__ == "__main__":
    bot.run(TOKEN)