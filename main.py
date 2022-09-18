import discord
from discord.ext import commands
from discord.flags import Intents
import  json
import random
from chatterbot import ChatBot
import time

with open("setting.json",'r',encoding= 'utf8') as jfile:
    jdata = json.load(jfile)

intents=discord.Intents.all()
intents.members=True

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    game = discord.Game('Visual Studio Code')
    print(">>Bot is online<<")
    await bot.change_presence(status=discord.Status.idle, activity=game)

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

@bot.command()
async def todolist(ctx,thing):
    local = time.localtime(time.time())
    list = thing.split(",")
    for i in list:
        embed=discord.Embed(title=str(ctx.author), description=str(local.tm_mon) + "." + str(local.tm_mday),color=0x10f500)
        embed.add_field(name=str(i), value="未完成", inline=False)
        await ctx.send(embed = embed)

def check_chinese(inp):
    china_word = ["視頻", "質量", "顯示屏", "代碼", "學霸", "老鐵", "程序員", "小姐姐", "抖音", "老鐵", "牛逼", "yyds", "nmsl", "中國", "YYDS", "NMSL"]
    for word in china_word:
        if word in inp: return True
    return False

@bot.event
#當有訊息時
async def on_message(message):
    if "機率"  in message.content:
        num=random.randint(1,100)
        await message.channel.send(str(num)+"%")
    
    if check_chinese(message.content):
        randm_num = random.randint(1, 100000)
        await message.channel.send(f"https://ect.incognitas.net/szh_police/szh_police{randm_num}.jpg")

bot.run("Token")