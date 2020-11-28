import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(Basic(bot))