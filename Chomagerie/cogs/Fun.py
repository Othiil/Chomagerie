import discord 
from discord.ext import commands

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def wiki(self, ctx):
        '''C'est juste pour avoir un article random sur wikipedia'''
        await ctx.send('instruit toi')
        await ctx.send('https://fr.wikipedia.org/wiki/Spécial:Page_au_hasard')

    @commands.command()
    async def jvc(self, ctx):
        '''wiki jvc'''
        await ctx.send('https://wiki.jvflux.com/Sp%C3%A9cial:Page_au_hasard')

    @commands.command()
    async def risibank(self, ctx):
        '''ça poste juste une image aléatoire de risibank'''
        url = "https://risibank.fr/stickers/hasard"
        headers = {"User-Agent": "Mozilla/5.0"}

        req = Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), "html.parser")
        link = soup.find("img", class_="img-preview-big")
        await ctx.send(link["src"])

def setup(bot):
    bot.add_cog(Fun(bot))   