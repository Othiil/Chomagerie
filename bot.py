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
from liste import liste,  liste2

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    game = discord.Game(
        name="{} serveurs | !help les pd".format(len(list(client.guilds)))
    )
    await client.change_presence(status=discord.Status.online, activity=game)
    print("--------------------------------------------")
    print("(C) Othiil 2019")
    print("ZbeulBot")
    print("{} serveurs".format(len(list(client.guilds))))
    print("--------------------------------------------")


@client.command()
async def rsa(ctx):
    """ Affiche le nombre de jours restant avant l'éligibilité du khey pour son RSA."""
    tempsActuel = datetime.date.today()
    tempsNotification = datetime.date(2022, 11, 11)
    if tempsActuel > tempsNotification:
        await ctx.send("Bordel , enfin le Saint RSA :merci: ")
    else:
        await ctx.send(datetime.date.today() - datetime.date(2022, 11, 11))


@client.command()
async def dragon(ctx):
    """fianso est un khey deter , et toi ? :) """
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
    """Temps de jeu du khey sam , meilleur hpal fr"""
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

@client.command()
async def risibank(ctx):
    """ça poste juste une image aléatoire de risibank"""
    url = "https://risibank.fr/stickers/hasard"
    headers = {"User-Agent": "Mozilla/5.0"}

    req = Request(url, headers=headers)
    soup = BeautifulSoup(urlopen(req).read(), "html.parser")
    link = soup.find("img", class_="img-preview-big")
    await ctx.send(link["src"])


@client.command()
async def sg(ctx):
    """Post une photo aléatoire.(NSFW)"""
   # path = "/run/media/antoine/127E02767E0252C1/RisiBot/satin/"
    """f = []
    for (dirpath, dirnames, filenames) in walk(path):
        f.extend(filenames)
        break
    sgfile = random.choice(f)
    await ctx.send(file=discord.File(path + sgfile))"""

    rdming = random.choice(liste)
    if ctx.channel.is_nsfw():
        await ctx.send(rdming)
    else:
        await ctx.send("Pas dans le bon chan gros fdp")

@client.command()
async def bd(ctx):
    rdming = random.choice(liste2)
    if ctx.channel.is_nsfw():
        await ctx.send(rdming)
    else:
        await ctx.send("Pas dans le bon chan gros fdp")

@client.command()
async def wiki(ctx):
    """C'est juste pour avoir un article random sur wikipedia, histoire que tu sois moins con fdp"""
    await ctx.send('Clique et instruit toi, sombre merde.')
    await ctx.send('https://fr.wikipedia.org/wiki/Spécial:Page_au_hasard')

@client.command()
async def jvc(ctx):
    """L'élite se doit de connaître ses classiques"""
    await ctx.send('https://wiki.jvflux.com/Sp%C3%A9cial:Page_au_hasard')

client.run("NDQyMzAwNjI3NTk5NDkxMDcz.XLnuzA.CUoOzgr19GLUWsCE9ydmTwnfCsE", bot=True, reconnect=True)
