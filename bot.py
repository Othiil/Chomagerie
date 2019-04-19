import discord
from discord.ext import commands
from discord.ext.commands import Bot

import asyncio
import time
import datetime
import random

from os import walk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

client = commands.Bot(command_prefix="!")


@client.command()
async def rsa(ctx):
    #Affiche le nombre de jours restant aavant l'éligibilité du khey sam pour son RSA.
    tempsActuel = datetime.date.today()
    tempsNotification = datetime.date(2022, 11, 11)
    if tempsActuel > tempsNotification:
        await ctx.send("Bordel , enfin le Saint RSA :merci: ")
    else:
        await ctx.send(datetime.date.today() - datetime.date(2022, 11, 11))


@client.command()
async def zebi(ctx):
    #Poste une image aléatoire depuis un fichier spécifié.
    img = [
        "0.jpg, 1.jpg",
        "2.jpg",
        "3.jpg",
        "4.jpg",
        "5.jpg",
        "6.jpg",
        "7.jpg",
        "8.jpg",
        "9.jpg",
        "10.jpg",
        "11.jpg",
        "12.jpg",
        "13.jpg",
        "14.jpg"
        "16.jpg"
        """,'17.jpg','18.jpg','19.jpg', '20.jpg','21.jpg','22.jpg','23.jpg','24.jpg', '25.jpg'""",
    ]
    await ctx.send(file=discord.File(random.choice(img)))


@client.command()
async def dragon(ctx):
    #Commande pas très utile mais qui fait référence à fianso.
    await ctx.send("ROULE UN DRAGON") 
    await asyncio.sleep(1.5)
    await ctx.send("FUME LE DRAGON")
    await asyncio.sleep(1.5)
    await ctx.send("CHARGE LE DRAGON ")
    await asyncio.sleep(1.5)
    await ctx.send("ET JE VISE LES TES-TÊ")
    await ctx.send(file=discord.File("fianso.png")) 


@client.command()
async def chomeur(ctx):
    #Temps de jeu du khey sam , meilleur hpal fr 
    await ctx.send(
        "TEMPS DE JEU AU 1/1/18 :\n\nHpal > 1657h \nMonk > 235h\nDruid > 35h\nHunt > 464h\nRogue > 66h\n\nTOTAL > 2457h"
    )
    await asyncio.sleep(0.5)
    await ctx.send("------------------")
    await asyncio.sleep(0.5)
    await ctx.send(
        "TEMPS DE JEU AU 12/08/18 :\n\nHpal > 2290h\nHpal 2 > 53h\nSham > 127h\nPriest > 103h\nWlock > 9h\nDrood > 67h\nDh > 29h\nWar > 59h\nDK > 29h\nMage > 79h\nHunt > 471h\nRogue > 70h\n\nTOTAL > 3799h\nbien joué le chomage FC est fier de toi clé"
    )
    await ctx.send(file=discord.File("rsa.png"))


@client.command(pass_context=True)
async def ping(ctx):
    #Commande ping , j'ai vraiment besoin de la décrire ? 
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await ctx.send(channel)
    t2 = time.perf_counter()
    embed = discord.Embed(
        title="Pong!",
        description="Ok {}ms.".format(round((t2 - t1) * 1000)),
        color=0xFFFFFF,
    )
    await ctx.send(embed=embed)


@client.command()
async def risibank(ctx):
    # Cette commande poste juste une image aléatoire de risibank
    url = "https://risibank.fr/stickers/hasard"
    headers = {"User-Agent": "Mozilla/5.0"}

    req = Request(url, headers=headers)
    soup = BeautifulSoup(urlopen(req).read(), "html.parser")
    link = soup.find("img", class_="img-preview-big")
    await ctx.send(link["src"])


@client.command()
async def img(ctx):
    #Même chose que plus haut , sauf que c'est pas le même dossier.
    f = []
    for (dirpath, dirnames, filenames) in walk("path"):
        f.extend(filenames)
        break
    sendfile = random.choice(f)
    await ctx.send(file = discord.File('path'+ sendfile))


client.run("token")
