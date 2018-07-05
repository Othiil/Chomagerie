import discord
import asyncio
import time
import datetime
import random
import os
import sys

#bot totalement inutile , mais qui rend service 

client = discord.Client()

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
        await client.send_message(message.channel, "Viens par la")
        await client.send_message(message.channel, "https://github.com/Othiil/RSA.bot")
    
    # !rsa , affiche juste le temps restant avant le RSA de sam
    elif message.content.startswith('!rsa'):
        tempsActuel = datetime.date.today()
        tempsNotification = datetime.date(2022, 11, 11)
        if tempsActuel > tempsNotification:
           await client.send_message(message.channel, "Bordel , enfin le Saint RSA :merci: ")
        else:
            await client.send_message(message.channel, datetime.date.today() - datetime.date(2022, 11, 11))

    elif message.author == client.user:
        return
#
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



client.run('token')
