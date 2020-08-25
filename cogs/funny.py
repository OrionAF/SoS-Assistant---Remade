import discord
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class FunnyCog(commands.Cog):

    def __init__(self, client):
        self.client = client


#Posts an embeded image of the Infeceted Horde meme
    @commands.command()
    async def horde(self, ctx):
        channelMiscLogs = self.client.get_channel(732287672772460544)
        currentDT = datetime.datetime.now()

        embedHorde = discord.Embed(colour=discord.Colour(16302848))
        embedHorde.set_image(url="https://i.imgur.com/XqgTAlk.jpg")
        embedHorde.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedHorde.timestamp = datetime.datetime.utcnow()

        embedHordeLog = discord.Embed(colour=discord.Colour(16302848), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedHordeLog.set_image(url='https://i.imgur.com/XqgTAlk.jpg')
        embedHordeLog.set_author(name='Horde Meme', icon_url=f'{ctx.author.avatar_url}')
        embedHordeLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedHordeLog.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embedHorde)
        await channelMiscLogs.send(embed=embedHordeLog)
        await channelMiscLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    #Posts an embeded image of the no infantry meme
    @commands.command(aliases=['inf', 'noinf', 'noinfantry'])
    async def infantry(self, ctx):
        channelMiscLogs = self.client.get_channel(732287672772460544)
        currentDT = datetime.datetime.now()
        
        embedInfantry = discord.Embed(colour=discord.Colour(16302848))
        embedInfantry.set_image(url="https://i.imgur.com/NuCcLu6.png")
        embedInfantry.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedInfantry.timestamp = datetime.datetime.utcnow()

        embedInfantryLog = discord.Embed(colour=discord.Colour(16302848), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfantryLog.set_author(name='Infantry Meme', icon_url=f'{ctx.author.avatar_url}')
        embedInfantryLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedInfantryLog.timestamp = datetime.datetime.utcnow()
        
        await ctx.send(embed=embedInfantry)
        await channelMiscLogs.send(embed=embedInfantryLog)
        await channelMiscLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @commands.command()
    async def meme(self, ctx):
        meme = ['https://i.imgur.com/s5JT5xl.jpg',
                'https://i.imgur.com/n8ZS7lO.jpg',
                'https://i.imgur.com/o9efV0n.png',
                'https://i.imgur.com/uN2NcfU.jpg',
                'https://i.imgur.com/hmKSKsE.jpg',
                'https://i.imgur.com/oX5xRQb.jpg',
                'https://i.imgur.com/dL9dhEv.jpg',
                'https://i.imgur.com/KdsVHKy.jpg',
                'https://i.imgur.com/5J04UER.png',
                'https://i.imgur.com/8UAsyhZ.jpg',
                'https://i.imgur.com/bLsJl0T.jpg',
                'https://i.imgur.com/cDpvU5E.jpg',
                'https://i.imgur.com/9ynkRV3.jpg',
                'https://i.imgur.com/YCIhmjt.jpg',
                'https://i.imgur.com/ridKD6I.jpg',
                'https://i.imgur.com/6exkK9p.jpg',
                'https://i.imgur.com/Z8lO4RQ.jpg',
                'https://i.imgur.com/Ukw5GpP.jpg',
                'https://i.imgur.com/E7X3xDc.jpg']

        channelMiscLogs = self.client.get_channel(732287672772460544)
        currentDT = datetime.datetime.now()
        
        embedInfantry = discord.Embed(colour=discord.Colour(16302848))
        embedInfantry.set_image(url=f"{random.choice(meme)}")
        embedInfantry.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedInfantry.timestamp = datetime.datetime.utcnow()

        embedInfantryLog = discord.Embed(colour=discord.Colour(16302848), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfantryLog.set_author(name='Random Meme', icon_url=f'{ctx.author.avatar_url}')
        embedInfantryLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedInfantryLog.timestamp = datetime.datetime.utcnow()
        
        await ctx.send(embed=embedInfantry)
        await channelMiscLogs.send(embed=embedInfantryLog)
        await channelMiscLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


        





def setup(client):
    client.add_cog(FunnyCog(client))