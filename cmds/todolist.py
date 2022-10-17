from asyncio import tasks
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

    # @commands.Cog.listener()
    # async def on_raw_reaction_add(self, payload):
    #     print(payload.emoji.name)
    #     if payload.emoji.name == '✅':
    #         print(payload.message_id)

    @tasks.loop(minutes = 1) 
    async def myLoop(self):
        #leetcode 呼叫器
        if "08:00:" in str(time.ctime()):
            channel = self.bot.get_channel(1031487148286816256)
            await channel.send("Leetcode https://leetcode.com")
            local = time.localtime(time.time())
            jsonFile = open('todolist.json','r', encoding= 'utf8')
            todo = json.load(jsonFile)
            tinylist = todo["todolist"]
            for i in tinylist:
                embed=discord.Embed(title=str('閒人'), description=str(local.tm_mon) + "." + str(local.tm_mday),color=0x10f500)
                embed.add_field(name=str(i), value="未完成", inline=False)
                await channel.send(embed = embed)
            time.sleep(60)

    @commands.command()
    async def todolist(self, ctx, thing):
        jsonFile = open('todolist.json','r', encoding= 'utf8')
        todo = json.load(jsonFile)
        jsonFile = open('todolist.json','w', encoding= 'utf8')
        tinylist = todo["todolist"]
        local = time.localtime(time.time())
        list = thing.split(",")
        for i in list:
            tinylist.append(i)
            embed=discord.Embed(title=str(ctx.author), description=str(local.tm_mon) + "." + str(local.tm_mday),color=0x10f500)
            embed.add_field(name=str(i), value="未完成", inline=False)
            await ctx.send(embed = embed)
        todo["todolist"] = tinylist    
        json.dump(todo, jsonFile, indent = 2,  ensure_ascii=False)

    @commands.command()
    async def todoshow(self, ctx):
        local = time.localtime(time.time())
        jsonFile = open('todolist.json','r', encoding= 'utf8')
        todo = json.load(jsonFile)
        tinylist = todo["todolist"]
        for i in tinylist:
            embed=discord.Embed(title=str(ctx.author), description=str(local.tm_mon) + "." + str(local.tm_mday),color=0x10f500)
            embed.add_field(name=str(i), value="未完成", inline=False)
            await ctx.send(embed = embed)

    @commands.command()
    async def todoadd(self, ctx, thing):
        jsonFile = open('todolist.json','r', encoding= 'utf8')
        todo = json.load(jsonFile)
        jsonFile = open('todolist.json','w', encoding= 'utf8')
        tinylist= todo["todolist"]
        tinylist.append(thing)
        todo["todolist"] = tinylist
        json.dump(todo, jsonFile, indent = 2,  ensure_ascii=False)
        await ctx.send(f"{thing} is added")

    @commands.command()
    async def todocls(self, ctx):
        jsonFile = open('todolist.json','w', encoding= 'utf8')
        data = {}
        data['todolist'] = []
        json.dump(data, jsonFile ,  indent = 2, ensure_ascii=False)
        await ctx.send(f"todolist is clear")


    
    
async def setup(bot):
    await bot.add_cog(Todolist(bot))