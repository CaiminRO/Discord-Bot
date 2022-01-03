import logging

import discord
from discord.ext import commands


# logger
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



# discord bot start client
client = discord.Client()

# command prefix intialize
client = commands.when_mentioned_or(command_prefix='$')


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.command()
async def echo(ctx, *, message: str):
    await ctx.send(message)

@client.command()
async def argsin(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@client.command()
async def changeCommandPrefix(ctx, arg1):
    client = commands.Bot(command_prefix=arg1)
    await ctx.send("Change command prefix to: " + string(arg1))


@commands.command(name = "echo", aliases=["repeat"])
async def  echo(self, ctx:commands.Context, message: str):
    await ctx.send(message)

@commands.command(name = "argcheck", aliases=["aliase"])
async def  num_args(self, ctx:commands.Context, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))


# bot token
f = open("token", 'r')
token = f.read()

# discord bot login using token
client.run(token)