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
    async def getInfectedData(self, ctx, lvl):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT title, description, replace(field, '\\n', '\n') as field, thumbnail, image, replace(footer, '\\n', '\n') as footer FROM realinfected WHERE level = ?", (lvl,))
        result = cursor.fetchone()
        print(lvl)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        embedInf = discord.Embed(title=(result[0]), colour=discord.Colour(16333359), description=(result[1]))
        embedInf.add_field(name='​', value=f'{(result[2])}', inline=False)
        embedInf.set_thumbnail(url=(result[3]))
        embedInf.set_image(url=(result[4]))
        embedInf.set_footer(text=(result[5]))
        embedInf.timestamp = datetime.datetime.utcnow()

        embedInfLog = discord.Embed(title=str(result[0]), colour=discord.Colour(16333359), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url=str(result[3]))
        embedInfLog.set_author(name='Infected', icon_url=f'{ctx.author.avatar_url}')
        embedInfLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedInfLog.timestamp = datetime.datetime.utcnow()

        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


        return embedInf
        

    @commands.command(aliases=['i1'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl1(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 1)

        await ctx.send(embed=infectedData)


    @commands.command(aliases=['i2'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl2(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 2)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i3'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl3(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 3)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i4'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl4(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 4)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i5'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl5(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 5)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i6'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl6(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 6)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i7'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl7(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 7)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i8'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl8(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 8)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i9'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl9(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 9)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i10'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl10(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 10)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i11'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl11(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 11)

        await ctx.send(embed=infectedData)
    
    @commands.command(aliases=['i12'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl12(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 12)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i13'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl13(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 13)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i14'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl14(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 14)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i15'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl15(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 15)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i16'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl16(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 16)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i17'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl17(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 17)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i18'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl18(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 18)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i19'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl19(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 19)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i20'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl20(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 20)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i21'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl21(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 21)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i22'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl22(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 22)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i23'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl23(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 23)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i24'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl24(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 24)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i25'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl25(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 25)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i26'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl26(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 26)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i27'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl27(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 27)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i28'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl28(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 28)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i29'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl29(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 29)

        await ctx.send(embed=infectedData)

    @commands.command(aliases=['i30'])
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ilvl30(self, ctx):
        infectedData = await InfectedCog.getInfectedData(self, ctx, 30)

        await ctx.send(embed=infectedData)


def setup(client):
    client.add_cog(InfectedCog(client))