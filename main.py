import discord
from discord.ext import commands
from discord.flags import Intents

intents=discord.Intents.default()
intents.members=True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event

async def on_ready():
    print(">>Bot is online<<")

@bot.event

async def on_member_join(member):
    channel = bot.get_channel(920704186952335420)
    await channel.send(f'{member}join!')


async def on_member_remove(member):
    channel = bot.get_channel(920704221173674085)
    await channel.send(f'{member}leave!')

bot.run('OTIwMzM3NDgzMzgyNzg0MDcy.Ybi5Ew.AdKco1B5aV2ZrzQsQBgcZTxRtVQ')