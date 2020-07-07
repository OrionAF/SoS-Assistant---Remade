import discord, datetime, time
import json
import os
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
from asyncio import sleep
import datetime as DT
from dotenv import load_dotenv
import logging

load_dotenv()
token = os.getenv('BOT_TOKEN')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

def owner(ctx):
    return ctx.author.id == 221070014252449792

client = commands.Bot(command_prefix = get_prefix, case_insensitive=True)
client.remove_command('help')
version = '0.0.1'

@client.event
async def on_ready():
    activity0 = discord.Activity(name='!help', type=discord.ActivityType.watching)
    currentDT = DT.datetime.now()
    print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
    print(currentDT)
    print('Created by #OrionAF#6983')
    print(f'Running on version: {version}')
    print('Bot is ready to RUMBLE!')
    print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
    await client.change_presence(activity=activity0)

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '*'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.check(owner)
async def load(ctx, extension):
    channelBotLogs = client.get_channel(726006745578733622)
    currentDT = DT.datetime.now()
    await ctx.channel.purge(limit=1)
    client.load_extension(f'cogs.{extension}')
    embedLoad = discord.Embed(colour=discord.Colour(39393), description=f'The extension ``{extension}`` has been loaded.\n\n*This message will self-delete in 10 seconds*')
    embedLoad.set_author(name='Extension Load', icon_url='https://i.imgur.com/89JvDkw.png')
    embedLoadNoDelete = discord.Embed(colour=discord.Colour(39393), description=f'The extension ``{extension}`` has been loaded.\n\nExecuted by {ctx.author.mention} at **{currentDT}**')
    embedLoadNoDelete.set_author(name='Extension Load', icon_url='https://i.imgur.com/89JvDkw.png')
    await ctx.send(embed=embedLoad, delete_after=10)
    await channelBotLogs.send(embed=embedLoadNoDelete)
    await channelBotLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

@client.command()
@commands.check(owner)
async def unload(ctx, extension):
    channelBotLogs = client.get_channel(726006745578733622)
    currentDT = DT.datetime.now()
    await ctx.channel.purge(limit=1)
    client.unload_extension(f'cogs.{extension}')
    embedUnload = discord.Embed(colour=discord.Colour(16302848), description=f'The extension ``{extension}`` has been unloaded.\n\n*This message will self-delete in 10 seconds*')
    embedUnload.set_author(name='Extension Unload', icon_url='https://i.imgur.com/89JvDkw.png')
    embedUnloadNoDelete = discord.Embed(colour=discord.Colour(16302848), description=f'The extension ``{extension}`` has been unloaded.\n\nExecuted by {ctx.author.mention} at **{currentDT}**')
    embedUnloadNoDelete.set_author(name='Extension Unload', icon_url='https://i.imgur.com/89JvDkw.png')
    await ctx.send(embed=embedUnload, delete_after=10)
    await channelBotLogs.send(embed=embedUnloadNoDelete)
    await channelBotLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

@client.command()
@commands.check(owner)
async def reload(ctx, extension):
    channelBotLogs = client.get_channel(726006745578733622)
    currentDT = DT.datetime.now()
    await ctx.channel.purge(limit=1)
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embedReload = discord.Embed(colour=discord.Colour(53606), description=f'The extension ``{extension}`` has been reloaded.\n\n*This message will self-delete in 10 seconds*')
    embedReload.set_author(name='Extension Reload', icon_url='https://i.imgur.com/89JvDkw.png')
    embedReloadNoDelete = discord.Embed(colour=discord.Colour(53606), description=f'The extension ``{extension}`` has been reloaded.\n\nExecuted by {ctx.author.mention} at **{currentDT}**')
    embedReloadNoDelete.set_author(name='Extension Reload', icon_url='https://i.imgur.com/89JvDkw.png')
    await ctx.send(embed=embedReload, delete_after=10)
    await channelBotLogs.send(embed=embedReloadNoDelete)
    await channelBotLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        channelErrorLogs = client.get_channel(726006713618268250)
        currentDT = DT.datetime.now()

        await ctx.channel.purge(limit=1)
        embedError = discord.Embed(colour=discord.Colour(13632027), description=f'That extension is allready loaded.  Maybe try reloading it?\n\n*This message will self-delete in 30 seconds.*')
        embedError.set_author(name="Extension allready loaded", icon_url="https://i.imgur.com/ty7SEua.png")

        embedErrorLog = discord.Embed(colour=discord.Colour(13632027), description=f'That extension is allready loaded.  Maybe try reloading it?\n\nExecution info:\nName: {ctx.author.mention}\nDate & time: **{currentDT}**')
        embedErrorLog.set_author(name="Extension allready loaded", icon_url="https://i.imgur.com/ty7SEua.png")

        await ctx.send(embed=embedError, delete_after=30)
        await channelErrorLogs.send(embed=embedErrorLog)
        await channelErrorLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

@client.command()
@commands.check(owner)
async def shutdown(ctx):
    channelBotLogs = client.get_channel(726006745578733622)
    currentDT = DT.datetime.now()
    embedShutdown = discord.Embed(colour=discord.Colour(10887193), description=f'{ctx.author.mention} told me to go to sleep.  **Apparently** bots need to sleep as well.\n Oh well, nap time.\n\n*This message will self-delete in 10 seconds*')
    embedShutdown.set_author(name='Bot Shutdown', icon_url='https://i.imgur.com/89JvDkw.png')
    embedShutdownNoDelete = discord.Embed(colour=discord.Colour(10887193), description=f'{ctx.author.mention} told me to go to sleep.  **Apparently** bots need to sleep as well.\n Oh well, nap time.\n\nExecuted by {ctx.author.mention} at **{currentDT}**')
    embedShutdownNoDelete.set_author(name='Bot Shutdown', icon_url='https://i.imgur.com/89JvDkw.png')
    await ctx.send(embed=embedShutdown, delete_after=10)
    await channelBotLogs.send(embed=embedShutdownNoDelete)
    await channelBotLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')
    activity11 = discord.Activity(name='Shutdown Imminent!', type=discord.ActivityType.watching)
    activity3 = discord.Activity(name='Shutdown in: 3', type=discord.ActivityType.watching)
    activity2 = discord.Activity(name='Shutdown in: 2', type=discord.ActivityType.watching)
    activity1 = discord.Activity(name='Shutdown in: 1', type=discord.ActivityType.watching)
    activity0 = discord.Activity(name='Goodbye! <3', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity11)
    await asyncio.sleep(15)
    await client.change_presence(activity=activity3)
    await asyncio.sleep(1)
    await client.change_presence(activity=activity2)
    await asyncio.sleep(1)
    await client.change_presence(activity=activity1)
    await asyncio.sleep(1)
    await client.change_presence(activity=activity0)
    await asyncio.sleep(2)
    await ctx.bot.close()

@client.command(aliases=['prefix', 'setprefix'])
@commands.check(owner)
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'My prefix has been changed to: ``{prefix}``')


client.run(token)