import discord
import time
from discord.ext import commands

class Core(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help and Documentation", description="Ah, it looks like you need some help. Here is a list with commands:", color=0xff379b)

        embed.add_field(name="y!greet", value="Gives a nice greet message", inline=False)
        embed.add_field(name="y!8ball", value="Reveal your destiny by asking questions", inline=False)
        embed.add_field(name="y!help", value="Gives this message", inline=False)
        embed.add_field(name="y!ping", value="Pong!", inline=False)


        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Piss off!')

def setup(client):
    client.add_cog(Core(client))
