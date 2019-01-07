import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import sys

f = open('token.txt', 'r')
token = f.read()
f.seek(0)
f.close()

p = ""
client = commands.Bot(command_prefix=p)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(game=discord.Game(name='with my son'))

@client.command
async def i'm(ctx, arg):
    client.say('Hi, ' + arg '. I'm Dad!)


client.run(token)
