from textwrap import indent
import discord
from discord.ext import commands
import random
import  json
import time

with open("setting.json",'r',encoding= 'utf8') as jfile:
    jdata = json.load(jfile)

class Todolist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(">>Todolist is loaded<<")
    
    @commands.command()
    async def todolist(self, ctx, thing):
        local = time.localtime(time.time())
        list = thing.split(",")
        for i in list:
            embed=discord.Embed(title=str(ctx.author), description=str(local.tm_mon) + "." + str(local.tm_mday),color=0x10f500)
            embed.add_field(name=str(i), value="未完成", inline=False)
            await ctx.send(embed = embed)

    @commands.command()
    async def todoadd(self, ctx, thing):
        jsonFile = open('todolist.json','r')
        todo = json.load(jsonFile)
        jsonFile = open('todolist.json','w')
        tinylist= todo["todolist"]
        tinylist.append(thing)
        todo["todolist"] = tinylist
        json.dump(todo, jsonFile, indent=2)



    
    
async def setup(bot):
    await bot.add_cog(Todolist(bot))