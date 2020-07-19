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
        embedInfantry = discord.Embed(colour=discord.Colour(16302848))
        embedInfantryLog = discord.Embed(colour=discord.Colour(16302848), description=f'Executed by: {ctx.author.mention}')
        embedInfantry.set_image(url="https://i.imgur.com/XqgTAlk.jpg")
        embedInfantryLog.set_image(url='https://i.imgur.com/XqgTAlk.jpg')
        embedInfantryLog.add_field(name='​', value=f'Execution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfantryLog.timestamp = datetime.datetime.utcnow()
        embedInfantry.timestamp = datetime.datetime.utcnow()
        embedInfantry.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedInfantryLog.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        await ctx.send(embed=embedInfantry)
        await channelMiscLogs.send(embed=embedInfantryLog)
        await channelMiscLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    #https://i.imgur.com/NuCcLu6.png
    #Posts an embeded image of the no infantry meme
    @commands.command(aliases=['inf'])
    async def infantry(self, ctx):
        channelMiscLogs = self.client.get_channel(732287672772460544)
        currentDT = datetime.datetime.now()
        embedInfantry = discord.Embed(colour=discord.Colour(16302848))
        embedInfantryLog = discord.Embed(colour=discord.Colour(16302848), description=f'Executed by: {ctx.author.mention}')
        embedInfantry.set_image(url="https://i.imgur.com/NuCcLu6.png")
        embedInfantryLog.set_image(url='https://i.imgur.com/NuCcLu6.png')
        embedInfantryLog.add_field(name='​', value=f'Execution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfantryLog.timestamp = datetime.datetime.utcnow()
        embedInfantry.timestamp = datetime.datetime.utcnow()
        embedInfantry.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedInfantryLog.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        await ctx.send(embed=embedInfantry)
        await channelMiscLogs.send(embed=embedInfantryLog)
        await channelMiscLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


    @commands.command()
    async def addmeme(self, ctx, *, text):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        sql = ("INSERT INTO emoji(meme, guild.id) VALUES(?,?)")
        val = (ctx.guild.id, text)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        await ctx.send(f'Meme saved!\n{text}')




def setup(client):
    client.add_cog(FunnyCog(client))