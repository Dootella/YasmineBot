import discord
import time
from discord.ext import commands

class Giveaway(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def giveaway(self, ctx):
        embed = discord.Embed(title="Giveaway! #4", color=discord.Colour(0xff379b), description="It's time for another giveaway!")

        embed.set_image(url="https://www.youtube.com/watch?v=BcjoGIoErdE")
        embed.set_footer(icon_url="https://cdn.discordapp.com/embed/avatars/4.png")

        embed.add_field(name="__How does it work?__", value="The video down below contains the key.", inline=False)
        embed.add_field(name="__How can I claim it?__", value="A free Steam account is required to claim your prize. If you've found the hidden key but if you do not have an account, feel free to contact us for further assistance.", inline=False)
        
        embed.add_field(name="Good luck!", value="If you claimed **the game**, let us know!", inline=False)
        
        embed.add_field(name="Video", value="**WARNING** THIS VIDEO CONTAINS BRIGHT, FLASHING LIGHTS. VIEWER DESCRESTION IS ADVIDED. Click [here](https://youtu.be/UctwZU38yBc) if the video doesn't load. ")
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Giveaway(client))
