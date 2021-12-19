import discord
from discord.ext import commands
from discord.flags import Intents
import  json
import random

with open("setting.json",'r',encoding= 'utf8') as jfile:
    jdata = json.load(jfile)

intents=discord.Intents.default()
intents.members=True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event

async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['welcome_channel']))
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['leave_channel']))
    await channel.send(f'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')

@bot.command()
async def eatap(ctx):
    res= random.choice(jdata['restaurant_apartment'])
    await ctx.send(res)

@bot.command()
async def eatsch(ctx):
    res= random.choice(jdata['restaurant_school'])
    await ctx.send(res)

bot.run("OTIwMzM3NDgzMzgyNzg0MDcy.Ybi5Ew.t_qQDHqOVg0mnD0AJmfdsr3nqeE")