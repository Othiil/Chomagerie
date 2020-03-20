import discord 
from discord.ext import commands

import random
from liste import liste2

class nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bd(self, ctx):
        '''random belledelphine image'''
        rdming = random.choice(liste2)
        if ctx.channel.is_nsfw():
            await ctx.send(rdming)
        else:
            await ctx.send("Pas dans le bon chan")

def setup(bot):
    bot.add_cog(nsfw(bot))   