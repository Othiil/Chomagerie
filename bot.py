import discord
import asyncio
import time
import datetime
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready(): 
    #Console
    print('******************************')
    print('Connecté en tant que :       *')
    print(client.user.name, '                     *')
    print(client.user.id, '          *')
    print('RSA.bot connecté             *')
    print('******************************')

@client.command()
async def aide(ctx):
        await ctx.send("Viens par la")
        await ctx.send("https://github.com/Othiil/RSA.bot")

@client.command()    
async def rsa(ctx):
    tempsActuel = datetime.date.today()
    tempsNotification = datetime.date(2022, 11, 11)
    if tempsActuel > tempsNotification:
        await ctx.send("Bordel , enfin le Saint RSA :merci: ")
    else:
        await ctx.send(datetime.date.today() - datetime.date(2022, 11, 11))

@client.command()
async def risitas(ctx):
    await ctx.send("pas de commande risitas pour le moment clé")
    await ctx.send('http://image.noelshack.com/fichiers/2017/20/1495053127-paslebol.png00000000000000')
    """elif message.content.startswith('!risitas'):
        img = ['atome.png', '1.png', '2.png', '3.png',
               '4.png', '5.png', '6.png', '7.png', '8.png', 
               '9.png', '10.png', '11.png', '12.png', '13.png', 
               '14.png', '15.png','16.gif','17.png','18.png',
               '19.png', '20.png','21.png','22.png','23.png',
               '24.png', '25.png', '26.png','27.png','28.png',
               '29.png', '30.png', '31.png', '32.png', '33.png', '34.png', ]
        await client.send_file(message.channel, random.choice(img))"""

@client.command()
async def played(ctx):    
        await ctx.send("TEMPS DE JEU AU 1/1/18 :\n\nHpal > 1657h \nMonk > 235h\nDruid > 35h\nHunt > 464h\nRogue > 66h\n\nTOTAL > 2457h")
        await asyncio.sleep(0.5)
        await ctx.send("------------------")
        await asyncio.sleep(0.5)       
        await ctx.send("TEMPS DE JEU AU 12/08/18 :\n\nHpal > 2290h\nHpal 2 > 53h\nSham > 127h\nPriest > 103h\nWlock > 9h\nDrood > 67h\nDh > 29h\nWar > 59h\nDK > 29h\nMage > 79h\nHunt > 471h\nRogue > 70h\n\nTOTAL > 3799h\nbien joué le chomage FC est fier de toi clé")
       # await ctx.send_file(('rsa.png')  



client.run('NDQyMzAwNjI3NTk5NDkxMDcz.XLJLwg.VNtMR1RUpOdPz_CkKAq7u0XJuI0')
