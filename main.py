import discord
import os
from discord.ext import commands

Client = discord.Client()
TOKEN = open("token.txt", "r").readline()
client = commands.Bot(command_prefix = 'y!')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready.')
    activity = discord.Activity(name='you', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

for filename in os.listdir('./extension'):
    if filename.endswith('.py'):
        client.load_extension(f'extension.{filename[:-3]}')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'extension.{extension}')
    await ctx.send("Extension loaded.")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'extension.{extension}')
    await ctx.send("Extension unloaded.")

client.run(TOKEN)
