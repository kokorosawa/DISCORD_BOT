import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event

async def on_ready():
    print(">>Bot is online<<")

bot.run('OTIwMzM3NDgzMzgyNzg0MDcy.Ybi5Ew.DoyUo_kKxzXQ5AW6ZwWo1HKtlJk')