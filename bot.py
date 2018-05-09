import discord
import asyncio
import time
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print('Connecté en tant que :')
    print(client.user.name)
    print(client.user.id)
    print('RSA.bot connecté')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!rsa'):
        tempsActuel = datetime.date.today()
        tempsNotification = datetime.date(2022, 11, 11)
        if tempsActuel > tempsNotification:
           await client.send_message(message.channel, "Bordel , enfin le Saint RSA :merci: ")
        else:
            await client.send_message(message.channel, datetime.date.today() - datetime.date(2022, 11, 11))
            
@client.event
async def on_game(Game):
     await discord.game(name ='être radié')




client.run('token')
