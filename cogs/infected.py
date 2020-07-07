import discord
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class InfectedCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def getInfectedData(self, ctx, level):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT title, description, replace(field, '\\n', '\n') as field, thumbnail, image, replace(footer, '\\n', '\n') as footer FROM realinfected WHERE level = level")
        result = cursor.fetchone()
        embedInf = discord.Embed(title=(result[0]), colour=discord.Colour(16333359), description=(result[1]))
        embedInf.add_field(name='​', value=f'{(result[2])}', inline=False)
        embedInf.set_thumbnail(url=(result[3]))
        embedInf.set_image(url=(result[4]))
        embedInf.set_footer(text=(result[5]))
        embedInf.timestamp = datetime.datetime.utcnow()

        embedInfLog = discord.Embed(title=str(result[0]), colour=discord.Colour(16333359), description=str(result[1]))
        embedInfLog.add_field(name='​', value=f'{(result[2])}', inline=False)
        embedInfLog.add_field(name='​', value=f'Execution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url=str(result[3]))
        embedInfLog.set_image(url=str(result[4]))
        embedInfLog.set_footer(text=str(result[5]), icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedInfLog.timestamp = datetime.datetime.utcnow()

        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

        return embedInf
        

    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl1(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, level=1)

        await ctx.send(embed=infectedData)


    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl2(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, level=2)

        await ctx.send(embed=infectedData)


    































def setup(client):
    client.add_cog(InfectedCog(client))