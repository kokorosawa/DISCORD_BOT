import asyncio
import discord
from discord.ext import commands
import os


intents=discord.Intents.all()
intents.members=True
bot = commands.Bot(command_prefix='!',intents=intents)


async def preload():
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')

@bot.command()
async def un(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'unloaded {extension} done')

@bot.command()
async def re(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'reloaded {extension} done')


@bot.command()
async def l(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'loaded {extension} done')


@bot.event
async def on_ready():
    game = discord.Game('Visual Studio Code')
    print(">>Bot is online<<")
    await bot.change_presence(status=discord.Status.idle, activity=game)


async def main():
    await preload()
    await bot.start("")


asyncio.run(main())