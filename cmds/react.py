import discord
from discord.ext import commands
import random
import  json



with open("setting.json",'r',encoding= 'utf8') as jfile:
    jdata = json.load(jfile)


def check_chinese(inp):
    china_word = ["視頻", "質量", "顯示屏", "代碼", "學霸", "老鐵", "程序員", "小姐姐", "抖音", "老鐵", "牛逼", "yyds", "nmsl", "中國", "YYDS", "NMSL"]
    for word in china_word:
        if word in inp: return True
    return False


class React(commands.Cog):
    def __init__(self, bot):
        self.bot = bot    
    @commands.command()
    async def eatap(self, ctx):
        res = random.choice(jdata['restaurant_apartment'])
        await ctx.send(res)

    @commands.command()
    async def eatsch(self, ctx):
        res = random.choice(jdata['restaurant_school'])
        await ctx.send(res)

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>React is loaded<<")
    async def on_message(self, message):
        if "機率"  in message.content:
            num=random.randint(1,100)
            await message.channel.send(str(num)+"%")
        
        if check_chinese(message.content):
            randm_num = random.randint(1, 100000)
            await message.channel.send(f"https://ect.incognitas.net/szh_police/szh_police{randm_num}.jpg")
        
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(React(bot))
