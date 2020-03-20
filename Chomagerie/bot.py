import discord
from discord.ext import commands

import sys, traceback

TOKEN = open("TOKEN.txt", "r").read()

def get_prefix(bot, message):
    """Prefixe"""
    prefixes = ['!', 'fdp ', '?']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'
    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

# 'Events.py' in cogs >>>> cogs.Events
initial_extensions = ['cogs.Fun',
                      'cogs.Chomeur',
                      'cogs.nsfw',
                      'cogs.Events']

bot = commands.Bot(command_prefix=get_prefix, description='A fun bot')
#load extensions(cogs) listed in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
            
#-------------
@bot.event
async def on_ready():
    print(f'\n\n{bot.user.name} -\nVersion: {discord.__version__}\n')
    print("(C) Othiil 2019")
    print("{} serveurs".format(len(list(bot.guilds))))
    await bot.change_presence(activity=discord.Streaming(name='!help', url='https://twitch.tv/Faker'))
    print(f'\nSuccessfully logged in and booted! :)')

bot.run(TOKEN, bot=True, reconnect=True)
