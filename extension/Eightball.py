import discord
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def greet(self, ctx, *, question):
        responses = [
                ":smiley: :wave: Hello, there!",
                ":kissing_heart: Hey cutie!",
                ":blush: Hi",
                ":smiling_face_with_3_hearts: Helloo!",
                ":flushed: Hey Teddy bear",
                ":woman_tipping_hand:",
                "Huh... what..?",
                "Hellon't",
                "Oi mate",
                "Piss off!"]
        await ctx.send(f'\n{random.choice(responses)}')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
    client.add_cog(Fun(client))

