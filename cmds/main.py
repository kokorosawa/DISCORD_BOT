import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>Main is loaded<<")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} ms')


async def setup(bot):
    await bot.add_cog(Main(bot))