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

@client.command(pass_context=True, invoke_without_command=True)
async def im(ctx, arg):
    test = 'dad'
    if arg.lower() == test:
     await client.say('No, I\'m Dad!')
    else:
     await client.say('Hi, ' + arg + '. I\'m Dad!')

@client.command(pass_context=True, invoke_without_command=True)
async def i(ctx, arg1, arg2):
    am = 'am'
    test = 'dad'
    if arg1.lower() == am:
        if arg2.lower() == test:
            await client.say('No, I\'m Dad!')
        else:
            await client.say('Hi, ' + arg2 + '. I\'m Dad!')



client.run(token)
