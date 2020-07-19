import discord
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class FiendCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def getFiendData(self, ctx, lvl):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT title, description, replace(field, '\\n', '\n') as field, thumbnail, image, replace(footer, '\\n', '\n') as footer FROM fiends WHERE level = ?", (lvl,))
        result = cursor.fetchone()
        print(lvl)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        embedFiend = discord.Embed(title=(result[0]), colour=discord.Colour(16333359), description=(result[1]))
        embedFiend.add_field(name='​', value=f'{(result[2])}', inline=False)
        embedFiend.set_thumbnail(url=(result[3]))
        embedFiend.set_image(url=(result[4]))
        embedFiend.set_footer(text=(result[5]))
        embedFiend.timestamp = datetime.datetime.utcnow()

        embedFiendLog = discord.Embed(title=str(result[0]), colour=discord.Colour(16333359), description=str(result[1]))
        embedFiendLog.add_field(name='​', value=f'{(result[2])}', inline=False)
        embedFiendLog.add_field(name='​', value=f'Execution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedFiendLog.set_thumbnail(url=str(result[3]))
        embedFiendLog.set_image(url=str(result[4]))
        embedFiendLog.set_footer(text=str(result[5]), icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedFiendLog.timestamp = datetime.datetime.utcnow()

        await channelInfoLogs.send(embed=embedFiendLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


        return embedFiend


    @commands.command(aliases=('iflvl1', 'fiendlvl1', 'flv1', 'iflv1' 'fiendlv1'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def flvl1(self, ctx):
        infectedData = await FiendCog.getFiendData(self, ctx, 1)

        await ctx.send(embed=infectedData)


    @commands.command(aliases=('iflvl2', 'fiendlvl2', 'flv2', 'iflv2' 'fiendlv2'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def flvl2(self, ctx):
        infectedData = await FiendCog.getFiendData(self, ctx, 2)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=('iflvl3', 'fiendlvl3', 'flv3', 'iflv3' 'fiendlv3'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def flvl3(self, ctx):
        infectedData = await FiendCog.getFiendData(self, ctx, 3)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=('iflvl4', 'fiendlvl4', 'flv4', 'iflv4' 'fiendlv4'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def flvl4(self, ctx):
        infectedData = await FiendCog.getFiendData(self, ctx, 4)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=('iflvl5', 'fiendlvl5', 'flv5', 'iflv5' 'fiendlv5'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def flvl5(self, ctx):
        infectedData = await FiendCog.getFiendData(self, ctx, 5)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=('norm', 'hunter', 'normalhunter', 'normhunter'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def normal(self, ctx):
        infectedData = await FiendCog.getFiendData(self, ctx, 6)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=('elitehunter', 'elt', 'elthunter'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def elite(self, ctx):
        infectedData = await FiendCog.getFiendData(self, ctx, 7)

        await ctx.send(embed=infectedData)

def setup(client):
    client.add_cog(FiendCog(client))