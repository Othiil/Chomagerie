import discord 
from discord.ext import commands

import time
import datetime

class Chomeur(commands.Cog, name="Le khey sam"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chomeur(self, ctx):
        embed = discord.Embed(title="Chomeur", description="Temps de jeu du khey sam , meilleur hpal fr", colour=discord.Color.purple())
        embed.add_field(name="HPal = 3501 heures", value="Hpal 2 > 161 heures")
        embed.add_field(name="Monk = 694 heures ", value="Priest = 208 heures ")
        embed.add_field(name="Wlock = 16 heures", value="Druid = 70 heures")
        embed.add_field(name="Sham = 135 heures", value="Dh = 34 heures")
        embed.add_field(name="War = 64 heures", value="Dk = 33 heures")
        embed.add_field(name="Mage = 85 heures", value="Hunt = 475 heures")
        embed.add_field(name="Rogue (CE) = 74 heures", value="= 5710 heures")
        await ctx.send(embed=embed)
        await ctx.send(f"= 5710 heures soit 759 heures depuis le 1/1, soit 5h/jour jusqu'au 30/5 (date d'arrêt)")

    @commands.command()
    async def rsa(self, ctx):
        ''' Affiche le nombre de jours restant avant l'éligibilité du khey pour son RSA.'''
        tempsActuel = datetime.date.today()
        tempsNotification = datetime.date(2022, 11, 11)
        if tempsActuel > tempsNotification:
            await ctx.send("Bordel , enfin le Saint RSA :merci: ")
        else:
            await ctx.send(datetime.date.today() - datetime.date(2022, 11, 11))

def setup(bot):
    bot.add_cog(Chomeur(bot))