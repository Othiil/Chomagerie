import discord
import asyncio
import time
import datetime
import random
import os
import sys

client = discord.Client()

# ascii art 8.6

@client.event
async def on_ready(): 
    #Console
    print('******************************')
    print('Connecté en tant que :       *')
    print(client.user.name, '                     *')
    print(client.user.id, '          *')
    print('RSA.bot connecté             *')
    print('******************************')

    #playing..
    while True:
        await client.change_presence(game=discord.Game(name="Prier l'atome"))
        await asyncio.sleep(10)
        await client.change_presence(game=discord.Game(name='!help'))
        await asyncio.sleep(10)
        await client.change_presence(game=discord.Game(name="Trouver un appart à issou"))
        await asyncio.sleep(10)

@client.event
async def on_message(message):
    #help command
    if message.content.startswith('!help'):
        await client.send_message(message.channel, "Viens par la enculé")
        await client.send_message(message.channel, "https://github.com/Othiil/RSA.bot")
    
    # !rsa , affiche juste le saint rsa de l'autre chomeur 
    elif message.content.startswith('!rsa'):
        tempsActuel = datetime.date.today()
        tempsNotification = datetime.date(2022, 11, 11)
        if tempsActuel > tempsNotification:
           await client.send_message(message.channel, "Bordel , enfin le Saint RSA :merci: ")
        else:
            await client.send_message(message.channel, datetime.date.today() - datetime.date(2022, 11, 11))

    elif message.author == client.user:
        return

    #Commande à modifier quand j'aurais pas la flemme
    elif message.content.startswith('!fdp'):
        msg = '{0.author.mention} est un gros fils de pute'.format(message)
        await client.send_message(message.channel, msg)

    #Commande pour faire apparaitre risitas , la liste peut augmenter
    elif message.content.startswith('!risitas'):
        img = ['atome.png', '1.png', '2.png', '3.png',
               '4.png', '5.png', '6.png', '7.png', '8.png', 
               '9.png', '10.png', '11.png', '12.png', '13.png', 
               '14.png', '15.png','16.gif','17.png','18.png',
               '19.png', '20.png','21.png','22.png','23.png',
               '24.png', '25.png', '26.png','27.png','28.png',
               '29.png', '30.png', '31.png', '32.png', '33.png', '34.png', ]
        await client.send_file(message.channel, random.choice(img))
    elif message.content.startswith('!test'):
        await client.send_message(message.channel, discord.Member + 'isse')

    #Commande intutile , suffit de lire la docstring en dessous :)
    elif message.content.startswith('!stop'): 
        #Je pose une docstring juste pour dire que la commande est éclaté et n'est même pas fonctionelle y'a juste a faire !oe pour l'éteindre
        await client.send_message(message.channel, 'T\'es  sur de vouloir éteindre le bot kolossal fdp ? (!oe / !nn)')
    
    #Permet d'arrêter le bot 
    elif message.content.startswith('!oe'):
        await client.send_message(message.channel, "El famoso bot va s'éteindre dans :")
        await client.send_message(message.channel, '3')
        await asyncio.sleep(1)
        await client.send_message(message.channel, '2')
        await asyncio.sleep(1)
        await client.send_message(message.channel, '1')
        await asyncio.sleep(1)
        await client.send_message(message.channel, 'VENGA VENGA')
        await client.send_file(message.channel, '16.gif')

        print("Le bot a été deconnecté via la commande d'arrêt")
        os.system('cls' if os.name == "nt" else 'clear')
        exit(0)

    #Sert à rien non plus 
    elif message.content.startswith('!nn'):
        await client.send_message(message.channel, "Bien vu")
        await client.send_file(message.channel, 'atome.png')


client.run('token')
