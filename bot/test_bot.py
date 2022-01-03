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


@bot.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

@bot.command()
async def argsin(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def changeCommandPrefix(ctx, arg1):
    bot = commands.Bot(command_prefix=commands.when_mentioned_or(arg1))
    await ctx.send("Change command prefix to: " + string(arg1))

@bot.command(name = "echo", aliases=["repeat"])
async def  copy_user(self, ctx:commands.Context, message: str):
    await ctx.send(message)

@bot.command(name = "argcheck", aliases=["argcount"])
async def  num_args(self, ctx:commands.Context, *args):
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