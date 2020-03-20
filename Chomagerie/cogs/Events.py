import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        user = message.author.name
        msg = message.content
        print(f"{user} said {msg}")

    #await self.bot.process_commands(message)
  #  @commands.Cog.listener()
  #  async def on_message_delete(self, message):
   #     await message.channel.send("There was a message deleted here mdr")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("T'as pas la permission de faire ca")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("C'est pas une commance ca frero")

def setup(bot):
    bot.add_cog(Events(bot))