import discord
import os.path
import youtube_dl
import aiohttp
from discord.voice_client import VoiceClient
from discord.ext import commands


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, brief="Makes the bot join your channel", aliases=['j', 'jo'])
    async def join(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined :speaker: **{channel}**")

    @commands.command(pass_context=True, brief="Makes the bot leave your channel", aliases=['l', 'le', 'lea'])
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        await server.disconnect()
        await ctx.send(f"Left :speaker: **{channel}**")

def setup(client):
    client.add_cog(Music(client))