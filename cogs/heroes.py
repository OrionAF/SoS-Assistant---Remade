import discord
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class HeroesCog(commands.Cog, name='HeroesCog'):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def getHeroData(self, ctx, lvl):
        db = sqlite3.connect('main.sqlite')
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()
        cursor = db.cursor()
        cursor.execute("SELECT color, replace(description, '\\n', '\n') as description, title, icon_url, main_skills, replace(max_lvl_military, '\\n', '\n') as max_lvl_military, replace(starting_lvl_military, '\\n', '\n') as starting_lvl_military, replace(max_lvl_explorer, '\\n', '\n') as max_lvl_explorer, replace(starting_lvl_explorer, '\\n', '\n') as starting_lvl_explorer, thumbnail, image, replace(footer, '\\n', '\n') as footer, hero_power, replace(hero_gear, '\\n', '\n') as hero_gear FROM heroes WHERE name = ?", (lvl,))
        result = cursor.fetchone()
        author = f'{ctx.author}'
        print(repr(result[2]))
        print(author)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        embedHeroStart = discord.Embed(colour=discord.Colour((result[0])), description=(result[1]))
        embedHeroStart.set_author(name=(result[2]), icon_url=(result[3]))
        embedHero = discord.Embed(colour=discord.Colour((result[0])), description=(result[4]) + f'\n\n<:Power:731035257876381697>**Maximum Hero Power:** ' + (result[12]))
        embedHero.add_field(name='​\n<:General:736785291314069617>**Max Level Military**\n​', value=(result[5]), inline=True)
        embedHero.add_field(name='​\n<:Cadet:736786513945296949>**Starting Level Military**\n', value=(result[6]), inline=True)
        embedHero.add_field(name='​', value='​', inline=True)
        embedHero.add_field(name='​\n<:General:736785291314069617>**Max Level Explorer**\n', value=(result[7]), inline=True)
        embedHero.add_field(name='​\n<:Cadet:736786513945296949>**Starting Level Explorer**\n', value=(result[8]), inline=True)
        embedHero.add_field(name='​', value='​', inline=True)
        embedHero.add_field(name='​', value=f'<:EpicHeroParts:728344428078432386>' + (result[13]))
        embedHeroStart.set_thumbnail(url=(result[9]))
        embedHero.set_image(url=(result[10]))
        embedHero.set_footer(text=(result[11]))
        embedHero.timestamp = datetime.datetime.utcnow()

        embedHeroLog = discord.Embed(colour=discord.Colour((result[0])), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedHeroLog.set_author(name=(result[2]) + f'-Long Version', icon_url=f'{ctx.author.avatar_url}')
        embedHeroLog.set_thumbnail(url=(result[9]))
        embedHeroLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedHeroLog.timestamp = datetime.datetime.utcnow()


        await ctx.send(embed=embedHeroStart)
        await channelInfoLogs.send(embed=embedHeroLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


        return embedHero


    @commands.Cog.listener()
    async def getMilitaryHeroData(self, ctx, lvl):
        db = sqlite3.connect('main.sqlite')
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()
        cursor = db.cursor()
        cursor.execute("SELECT color, replace(description, '\\n', '\n') as description, title, icon_url, main_skills, replace(max_lvl_military, '\\n', '\n') as max_lvl_military, replace(starting_lvl_military, '\\n', '\n') as starting_lvl_military, replace(max_lvl_explorer, '\\n', '\n') as max_lvl_explorer, replace(starting_lvl_explorer, '\\n', '\n') as starting_lvl_explorer, thumbnail, image, replace(footer, '\\n', '\n') as footer, hero_power, replace(hero_gear, '\\n', '\n') as hero_gear FROM heroes WHERE name = ?", (lvl,))
        result = cursor.fetchone()
        author = f'{ctx.author}'
        print(repr(result[2]))
        print(author)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        embedHero = discord.Embed(colour=discord.Colour((result[0])), description=(result[4]) + f'\n\n<:Power:731035257876381697>**Maximum Hero Power:** ' + (result[12]))
        embedHero.set_author(name=(result[2]), icon_url=(result[3]))
        embedHero.add_field(name='​\n<:General:736785291314069617>**Max Level Military**\n​', value=(result[5]), inline=True)
        embedHero.add_field(name='​\n<:Cadet:736786513945296949>**Starting Level Military**\n', value=(result[6]), inline=True)
        embedHero.add_field(name='​', value='​', inline=True)
        embedHero.add_field(name='​', value=f'<:EpicHeroParts:728344428078432386>' + (result[13]))
        embedHero.set_thumbnail(url=(result[9]))
        embedHero.set_footer(text=(result[11]))
        embedHero.timestamp = datetime.datetime.utcnow()

        embedHeroLog = discord.Embed(colour=discord.Colour((result[0])), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedHeroLog.set_author(name=(result[2]) + f'-Military Version', icon_url=f'{ctx.author.avatar_url}')
        embedHeroLog.set_thumbnail(url=(result[9]))
        embedHeroLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedHeroLog.timestamp = datetime.datetime.utcnow()

        
        await channelInfoLogs.send(embed=embedHeroLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


        return embedHero


    @commands.Cog.listener()
    async def getExplorerHeroData(self, ctx, lvl):
        db = sqlite3.connect('main.sqlite')
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()
        cursor = db.cursor()
        cursor.execute("SELECT color, replace(description, '\\n', '\n') as description, title, icon_url, main_skills, replace(max_lvl_military, '\\n', '\n') as max_lvl_military, replace(starting_lvl_military, '\\n', '\n') as starting_lvl_military, replace(max_lvl_explorer, '\\n', '\n') as max_lvl_explorer, replace(starting_lvl_explorer, '\\n', '\n') as starting_lvl_explorer, thumbnail, image, replace(footer, '\\n', '\n') as footer, hero_power, replace(hero_gear, '\\n', '\n') as hero_gear FROM heroes WHERE name = ?", (lvl,))
        result = cursor.fetchone()
        author = f'{ctx.author}'
        print(repr(result[2]))
        print(author)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        embedHero = discord.Embed(colour=discord.Colour((result[0])), description=(result[4]) + f'\n\n<:Power:731035257876381697>**Maximum Hero Power:** ' + (result[12]))
        embedHero.set_author(name=(result[2]), icon_url=(result[3]))
        embedHero.add_field(name='​\n<:General:736785291314069617>**Max Level Explorer**\n', value=(result[7]), inline=True)
        embedHero.add_field(name='​\n<:Cadet:736786513945296949>**Starting Level Explorer**\n', value=(result[8]), inline=True)
        embedHero.set_thumbnail(url=(result[9]))
        embedHero.set_footer(text=(result[11]))
        embedHero.timestamp = datetime.datetime.utcnow()

        embedHeroLog = discord.Embed(colour=discord.Colour((result[0])), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedHeroLog.set_author(name=(result[2]) + f'-Explorer Version', icon_url=f'{ctx.author.avatar_url}')
        embedHeroLog.set_thumbnail(url=(result[9]))
        embedHeroLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedHeroLog.timestamp = datetime.datetime.utcnow()

        
        await channelInfoLogs.send(embed=embedHeroLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


        return embedHero


    @commands.Cog.listener()
    async def getShortHeroData(self, ctx, lvl):
        db = sqlite3.connect('main.sqlite')
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()
        cursor = db.cursor()
        cursor.execute("SELECT color, replace(description, '\\n', '\n') as description, title, icon_url, main_skills, replace(max_lvl_military, '\\n', '\n') as max_lvl_military, replace(starting_lvl_military, '\\n', '\n') as starting_lvl_military, replace(max_lvl_explorer, '\\n', '\n') as max_lvl_explorer, replace(starting_lvl_explorer, '\\n', '\n') as starting_lvl_explorer, thumbnail, image, replace(footer, '\\n', '\n') as footer, hero_power, replace(hero_gear, '\\n', '\n') as hero_gear FROM heroes WHERE name = ?", (lvl,))
        result = cursor.fetchone()
        author = f'{ctx.author}'
        print(repr(result[2]))
        print(author)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        embedHero = discord.Embed(colour=discord.Colour((result[0])), description=(result[4]) + f'\n\n<:Power:731035257876381697>**Maximum Hero Power:** ' + (result[12]))
        embedHero.set_author(name=(result[2]), icon_url=(result[3]))
        embedHero.add_field(name='​\n<:General:736785291314069617>**Max Level Military**\n​', value=(result[5]), inline=True)
        embedHero.add_field(name='​\n<:Cadet:736786513945296949>**Starting Level Military**\n', value=(result[6]), inline=True)
        embedHero.add_field(name='​', value='​', inline=True)
        embedHero.add_field(name='​\n<:General:736785291314069617>**Max Level Explorer**\n', value=(result[7]), inline=True)
        embedHero.add_field(name='​\n<:Cadet:736786513945296949>**Starting Level Explorer**\n', value=(result[8]), inline=True)
        embedHero.add_field(name='​', value='​', inline=True)
        embedHero.add_field(name='​', value=f'<:EpicHeroParts:728344428078432386>' + (result[13]))
        embedHero.set_thumbnail(url=(result[9]))
        embedHero.set_footer(text=(result[11]))
        embedHero.timestamp = datetime.datetime.utcnow()

        embedHeroLog = discord.Embed(colour=discord.Colour((result[0])), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedHeroLog.set_author(name=(result[2]) + f'-Short Version', icon_url=f'{ctx.author.avatar_url}')
        embedHeroLog.set_thumbnail(url=(result[9]))
        embedHeroLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedHeroLog.timestamp = datetime.datetime.utcnow()


        await channelInfoLogs.send(embed=embedHeroLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


        return embedHero


    #Travis
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def travis(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 1)

            await ctx.send(embed=HeroData)

    @travis.command(aliases=['army'])
    async def military(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 1)

        await ctx.send(embed=HeroData)

    @travis.command(aliases=['explore', 'exploring'])
    async def explorer(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 1)

        await ctx.send(embed=HeroData)

    @travis.command(aliases=['shorter', 'shorten'])
    async def short(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 1)

        await ctx.send(embed=HeroData)

    #Maddie & Frank
    @commands.group(aliases=('frank', 'maddie&frank', 'maddieandfrank'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def maddie(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 2)

            await ctx.send(embed=HeroData)

    @maddie.command(name='military', aliases=['army'])
    async def military1(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 2)

        await ctx.send(embed=HeroData)

    @maddie.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer1(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 2)

        await ctx.send(embed=HeroData)

    @maddie.command(name='short', aliases=['shorter', 'shorten'])
    async def short1(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 2)

        await ctx.send(embed=HeroData)

    #Chef
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def chef(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 3)

            await ctx.send(embed=HeroData)

    @chef.command(name='military', aliases=['army'])
    async def military2(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 3)

        await ctx.send(embed=HeroData)

    @chef.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer2(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 3)

        await ctx.send(embed=HeroData)

    @chef.command(aliases=['shorter', 'shorten'])
    async def short2(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 3)

        await ctx.send(embed=HeroData)

    #Ash
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ash(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 4)

            await ctx.send(embed=HeroData)

    @ash.command(name='military', aliases=['army'])
    async def military3(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 4)

        await ctx.send(embed=HeroData)

    @ash.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer3(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 4)

        await ctx.send(embed=HeroData)

    @ash.command(name='short', aliases=['shorter', 'shorten'])
    async def short3(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 4)

        await ctx.send(embed=HeroData)

    #Ernie
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ernie(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 5)

            await ctx.send(embed=HeroData)

    @ernie.command(name='military', aliases=['army'])
    async def military4(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 5)

        await ctx.send(embed=HeroData)

    @ernie.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer4(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 5)

        await ctx.send(embed=HeroData)

    @ernie.command(name='short', aliases=['shorter', 'shorten'])
    async def short4(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 5)

        await ctx.send(embed=HeroData)

    #Eva
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def eva(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 6)

            await ctx.send(embed=HeroData)

    @eva.command(name='military', aliases=['army'])
    async def military5(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 6)

        await ctx.send(embed=HeroData)

    @eva.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer5(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 6)

        await ctx.send(embed=HeroData)

    @eva.command(name='short', aliases=['shorter', 'shorten'])
    async def short5(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 4)

        await ctx.send(embed=HeroData)

    #Ghost
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ghost(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 7)

            await ctx.send(embed=HeroData)

    @ghost.command(name='military', aliases=['army'])
    async def military6(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 7)

        await ctx.send(embed=HeroData)

    @ghost.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer6(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 7)

        await ctx.send(embed=HeroData)

    @ghost.command(name='short', aliases=['shorter', 'shorten'])
    async def short6(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 7)

        await ctx.send(embed=HeroData)

    #Jane
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def jane(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 8)

            await ctx.send(embed=HeroData)

    @jane.command(name='military', aliases=['army'])
    async def military7(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 8)

        await ctx.send(embed=HeroData)

    @jane.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer7(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 8)

        await ctx.send(embed=HeroData)

    @jane.command(name='short', aliases=['shorter', 'shorten'])
    async def short7(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 8)

        await ctx.send(embed=HeroData)

    #Jarrett
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def jarrett(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 9)

            await ctx.send(embed=HeroData)

    @jarrett.command(name='military', aliases=['army'])
    async def military8(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 9)

        await ctx.send(embed=HeroData)

    @jarrett.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer8(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 9)

        await ctx.send(embed=HeroData)

    @jarrett.command(name='short', aliases=['shorter', 'shorten'])
    async def short8(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 9)

        await ctx.send(embed=HeroData)

    #Jeb
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def jeb(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 10)

            await ctx.send(embed=HeroData)

    @jeb.command(name='military', aliases=['army'])
    async def military9(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 10)

        await ctx.send(embed=HeroData)

    @jeb.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer9(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 10)

        await ctx.send(embed=HeroData)

    @jeb.command(name='short', aliases=['shorter', 'shorten'])
    async def short9(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 10)

        await ctx.send(embed=HeroData)

    #Lucky
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def lucky(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 11)

            await ctx.send(embed=HeroData)

    @lucky.command(name='military', aliases=['army'])
    async def military10(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 11)

        await ctx.send(embed=HeroData)

    @lucky.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer10(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 11)

        await ctx.send(embed=HeroData)

    @lucky.command(name='short', aliases=['shorter', 'shorten'])
    async def short10(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 11)

        await ctx.send(embed=HeroData)

    #Miho
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def miho(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 12)

            await ctx.send(embed=HeroData)

    @miho.command(name='military', aliases=['army'])
    async def military11(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 12)

        await ctx.send(embed=HeroData)

    @miho.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer11(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 12)

        await ctx.send(embed=HeroData)

    @miho.command(name='short', aliases=['shorter', 'shorten'])
    async def short11(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 12)

        await ctx.send(embed=HeroData)

    #Mike
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def mike(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 13)

            await ctx.send(embed=HeroData)

    @mike.command(name='military', aliases=['army'])
    async def military12(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 13)

        await ctx.send(embed=HeroData)

    @mike.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer12(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 13)

        await ctx.send(embed=HeroData)

    @mike.command(name='short', aliases=['shorter', 'shorten'])
    async def short12(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 13)

        await ctx.send(embed=HeroData)

    #Nikola
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def nikola(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 14)

            await ctx.send(embed=HeroData)

    @nikola.command(name='military', aliases=['army'])
    async def military13(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 14)

        await ctx.send(embed=HeroData)

    @nikola.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer13(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 14)

        await ctx.send(embed=HeroData)

    @nikola.command(name='short', aliases=['shorter', 'shorten'])
    async def short13(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 14)

        await ctx.send(embed=HeroData)

    #Ray & Rolex
    @commands.group(aliases=('rolex', 'ray&rolex', 'rayandrolex'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ray(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 15)

            await ctx.send(embed=HeroData)

    @ray.command(name='military', aliases=['army'])
    async def military14(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 15)

        await ctx.send(embed=HeroData)

    @ray.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer14(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 15)

        await ctx.send(embed=HeroData)

    @ray.command(name='short', aliases=['shorter', 'shorten'])
    async def short14(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 15)

        await ctx.send(embed=HeroData)

    #Rusty
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def rusty(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 16)

            await ctx.send(embed=HeroData)

    @rusty.command(name='military', aliases=['army'])
    async def military15(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 16)

        await ctx.send(embed=HeroData)

    @rusty.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer15(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 16)

        await ctx.send(embed=HeroData)

    @rusty.command(name='short', aliases=['shorter', 'shorten'])
    async def short15(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 16)

        await ctx.send(embed=HeroData)

    #Sarge
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def sarge(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 17)

            await ctx.send(embed=HeroData)

    @sarge.command(name='military', aliases=['army'])
    async def military16(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 17)

        await ctx.send(embed=HeroData)

    @sarge.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer16(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 17)

        await ctx.send(embed=HeroData)

    @sarge.command(name='short', aliases=['shorter', 'shorten'])
    async def short16(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 17)

        await ctx.send(embed=HeroData)

    #Tony
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def tony(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 18)

            await ctx.send(embed=HeroData)

    @tony.command(name='military', aliases=['army'])
    async def military17(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 18)

        await ctx.send(embed=HeroData)

    @tony.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer17(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 18)

        await ctx.send(embed=HeroData)

    @tony.command(name='short', aliases=['shorter', 'shorten'])
    async def short17(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 18)

        await ctx.send(embed=HeroData)

    #Trish
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def trish(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 19)

            await ctx.send(embed=HeroData)

    @trish.command(name='military', aliases=['army'])
    async def military18(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 19)

        await ctx.send(embed=HeroData)

    @trish.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer18(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 19)

        await ctx.send(embed=HeroData)

    @trish.command(name='short', aliases=['shorter', 'shorten'])
    async def short18(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 19)

        await ctx.send(embed=HeroData)

    #Wolfe
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def wolfe(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 20)

            await ctx.send(embed=HeroData)

    @wolfe.command(name='military', aliases=['army'])
    async def military19(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 20)

        await ctx.send(embed=HeroData)

    @wolfe.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer19(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 20)

        await ctx.send(embed=HeroData)

    @wolfe.command(name='short', aliases=['shorter', 'shorten'])
    async def short19(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 20)

        await ctx.send(embed=HeroData)

    #Zach
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def zach(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 21)

            await ctx.send(embed=HeroData)

    @zach.command(name='military', aliases=['army'])
    async def military20(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 21)

        await ctx.send(embed=HeroData)

    @zach.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer20(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 21)

        await ctx.send(embed=HeroData)

    @zach.command(name='short', aliases=['shorter', 'shorten'])
    async def short20(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 21)

        await ctx.send(embed=HeroData)

    #Zoe
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def zoe(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 22)

            await ctx.send(embed=HeroData)

    @zoe.command(name='military', aliases=['army'])
    async def military21(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 22)

        await ctx.send(embed=HeroData)

    @zoe.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer21(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 22)

        await ctx.send(embed=HeroData)

    @zoe.command(name='short', aliases=['shorter', 'shorten'])
    async def short21(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 22)

        await ctx.send(embed=HeroData)

    #Candy
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def candy(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 23)

            await ctx.send(embed=HeroData)

    @candy.command(name='military', aliases=['army'])
    async def military22(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 23)

        await ctx.send(embed=HeroData)

    @candy.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer22(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 23)

        await ctx.send(embed=HeroData)

    @candy.command(name='short', aliases=['shorter', 'shorten'])
    async def short22(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 23)

        await ctx.send(embed=HeroData)

    #Basel
    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def basel(self, ctx):
        if ctx.invoked_subcommand is None:
            HeroData = await HeroesCog.getHeroData(self, ctx, 24)

            await ctx.send(embed=HeroData)

    @basel.command(name='military', aliases=['army'])
    async def military23(self, ctx):
        HeroData = await HeroesCog.getMilitaryHeroData(self, ctx, 24)

        await ctx.send(embed=HeroData)

    @basel.command(name='explorer', aliases=['explore', 'exploring'])
    async def explorer23(self, ctx):
        HeroData = await HeroesCog.getExplorerHeroData(self, ctx, 24)

        await ctx.send(embed=HeroData)

    @basel.command(name='short', aliases=['shorter', 'shorten'])
    async def short23(self, ctx):
        HeroData = await HeroesCog.getShortHeroData(self, ctx, 24)

        await ctx.send(embed=HeroData)


    @commands.Cog.listener()
    async def getSpecData(self, ctx, lvl):
        db = sqlite3.connect('main.sqlite')
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()
        cursor = db.cursor()
        cursor.execute("Select image, description, replace(footer, '\\n', '\n') as footer, spec_icon FROM specs WHERE number = ?", (lvl,))
        result = cursor.fetchone()
        author = f'{ctx.author}'
        print(repr(result[1]))
        print(author)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        embedSpecs = discord.Embed(colour=discord.Colour(13400320))
        embedSpecs.set_author(name=(result[1]), icon_url=(result[3]))
        embedSpecs.set_image(url=(result[0]))
        embedSpecs.set_footer(text=(result[2]))
        embedSpecs.timestamp = datetime.datetime.utcnow()

        embedSpecsLog = discord.Embed(colour=discord.Colour(13400320), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedSpecsLog.set_author(name=(result[1]), icon_url=f'{ctx.author.avatar_url}')
        embedSpecsLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedSpecsLog.timestamp = datetime.datetime.utcnow()

        await channelInfoLogs.send(embed=embedSpecsLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

        return embedSpecs

    @commands.group(aliases=['spec', 'specs'], case_insensitive=True)
    async def specialization(self, ctx):
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title='Hero Specialization', colour=discord.Colour(13400320), description=f'You need to specify a category.  Categories are:\n**Gathering**\n**Infected**\n**Patrol**\n**Siege**\n**Rally**')
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    
    @specialization.command()
    async def gathering(self, ctx):
        SpecData = await HeroesCog.getSpecData(self, ctx, 1)

        await ctx.send(embed=SpecData)

    @specialization.command()
    async def infected(self, ctx):
        SpecData = await HeroesCog.getSpecData(self, ctx, 2)

        await ctx.send(embed=SpecData)

    @specialization.command()
    async def patrol(self, ctx):
        SpecData = await HeroesCog.getSpecData(self, ctx, 3)

        await ctx.send(embed=SpecData)

    @specialization.command()
    async def siege(self, ctx):
        SpecData = await HeroesCog.getSpecData(self, ctx, 4)

        await ctx.send(embed=SpecData)

    @specialization.command()
    async def rally(self, ctx):
        SpecData = await HeroesCog.getSpecData(self, ctx, 5)

        await ctx.send(embed=SpecData)


def setup(client):
    client.add_cog(HeroesCog(client))