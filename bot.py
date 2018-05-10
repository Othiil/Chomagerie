import discord
import asyncio
import time
import datetime

client = discord.Client()

@client.event
async def on_ready(): #Console
    print('Connecté en tant que :')
    print(client.user.name)
    print(client.user.id)
    print('RSA.bot connecté')

    #playing..
    while True:
        await client.change_presence(game=discord.Game(name='Attendre les 25 ans'))
        await asyncio.sleep(15)
        await client.change_presence(game=discord.Game(name='Se faire radier'))
        await asyncio.sleep(15)
        await client.change_presence(game=discord.Game(name='Boire la sainte 8.6'))
        await asyncio.sleep(15)
        await client.change_presence(game=discord.Game(name='Trouver un squat pour la nuit'))
        await asyncio.sleep(15)


async def c_issou(self):
        """
        Sends a random cat picture

        {prefix}issou
        """
        issou = await self.req.get('https://risibank.fr/#')
        return Response(issou['file'])


@client.event
async def on_message(message):
    #help command
    if message.content.startswith('!help'):
        await client.send_message(message.channel, "clé si t'as besoin d'aide va voir la sainte page sponsorisé par pôle emploi")
        await client.send_message(message.channel, "https://github.com/Othiil/RSA.bot")
    # !rsa 
    elif message.content.startswith('!rsa'):
        tempsActuel = datetime.date.today()
        tempsNotification = datetime.date(2022, 11, 11)
        if tempsActuel > tempsNotification:
           await client.send_message(message.channel, "Bordel , enfin le Saint RSA :merci: ")
        else:
            await client.send_message(message.channel, datetime.date.today() - datetime.date(2022, 11, 11))
    elif message.author == client.user:
        return
    elif message.content.startswith('!fdp'):
        msg = '{0.author.mention} est un gros fils de pute'.format(message)
        await client.send_message(message.channel, msg)


client.run('token')
