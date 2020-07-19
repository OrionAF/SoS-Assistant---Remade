import discord
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class HeroesCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def getHeroData(self, ctx, lvl):
        db = sqlite3.connect('main.sqlite')
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()
        cursor = db.cursor()
        cursor.execute("SELECT color, replace(description, '\\n', '\n') as description, title, icon_url, main_skills, replace(max_lvl_military, '\\n', '\n') as max_lvl_military, replace(starting_lvl_military, '\\n', '\n') as starting_lvl_military, replace(max_lvl_explorer, '\\n', '\n') as max_lvl_explorer, replace(starting_lvl_explorer, '\\n', '\n') as starting_lvl_explorer, thumbnail, image, replace(footer, '\\n', '\n') as footer FROM heroes WHERE name = ?", (lvl,))
        result = cursor.fetchone()
        print(lvl)
        print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
        embedHeroStart = discord.Embed(colour=discord.Colour((result[0])), description=(result[1]))
        embedHeroStart.set_author(name=(result[2]), icon_url=(result[3]))
        embedHero = discord.Embed(colour=discord.Colour((result[0])), description=(result[4]))
        embedHero.add_field(name='​\n**Max Level Military**', value=(result[5]), inline=True)
        embedHero.add_field(name='​\n**Starting Level Military**', value=(result[6]), inline=True)
        embedHero.add_field(name='​', value='​', inline=True)
        embedHero.add_field(name='​\n**Max Level Explorer**', value=(result[7]), inline=True)
        embedHero.add_field(name='​\n**Starting Level Explorer**', value=(result[8]), inline=True)
        embedHero.add_field(name='​', value='​', inline=True)
        embedHeroStart.set_thumbnail(url=(result[9]))
        embedHero.set_image(url=(result[10]))
        embedHero.set_footer(text=(result[11]))
        embedHero.timestamp = datetime.datetime.utcnow()

        embedHeroStartLog = discord.Embed(colour=discord.Colour((result[0])), description=(result[1]))
        embedHeroStartLog.set_author(name=(result[2]), icon_url=(result[3]))
        embedHeroLog = discord.Embed(colour=discord.Colour((result[0])), description=(result[4]))
        embedHeroLog.add_field(name='​\n**Max Level Military**', value=(result[5]), inline=True)
        embedHeroLog.add_field(name='​\n**Starting Level Military**', value=(result[6]), inline=True)
        embedHeroLog.add_field(name='​', value='​', inline=True)
        embedHeroLog.add_field(name='​\n**Max Level Explorer**', value=(result[7]), inline=True)
        embedHeroLog.add_field(name='​\n**Starting Level Explorer**', value=(result[8]), inline=True)
        embedHeroLog.add_field(name='​', value='​', inline=True)
        embedHeroStartLog.set_thumbnail(url=(result[9]))
        embedHeroLog.set_image(url=(result[10]))
        embedHeroLog.set_footer(text=(result[11]), icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedHeroLog.timestamp = datetime.datetime.utcnow()
        embedHeroLog.add_field(name='​', value=f'Execution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')


        await ctx.send(embed=embedHeroStart)
        await channelInfoLogs.send(embed=embedHeroStartLog)
        await channelInfoLogs.send(embed=embedHeroLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


        return embedHero



    #Travis
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def travis(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 1)

        await ctx.send(embed=HeroData)

    #Maddie & Frank
    @commands.command(aliases=('frank', 'maddie&frank', 'maddieandfrank'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def maddie(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 2)

        await ctx.send(embed=HeroData)

    #Chef
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def chef(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 3)

        await ctx.send(embed=HeroData)

    #Ash
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ash(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 4)

        await ctx.send(embed=HeroData)

    #Ernie
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ernie(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 5)

        await ctx.send(embed=HeroData)

    #Eva
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def eva(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 6)

        await ctx.send(embed=HeroData)

    #Ghost
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ghost(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 7)

        await ctx.send(embed=HeroData)

    #Jane
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def jane(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 8)

        await ctx.send(embed=HeroData)

    #Jarret
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def jarret(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 9)

        await ctx.send(embed=HeroData)

    #Jeb
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def jeb(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 10)

        await ctx.send(embed=HeroData)

    #Lucky
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def lucky(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 11)

        await ctx.send(embed=HeroData)

    #Miho
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def miho(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 12)

        await ctx.send(embed=HeroData)

    #Mike
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def mike(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 13)

        await ctx.send(embed=HeroData)

    #Nikola
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def nikola(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 14)

        await ctx.send(embed=HeroData)

    #Ray & Rolex
    @commands.command(aliases=('rolex', 'ray&rolex', 'rayandrolex'))
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def ray(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 15)

        await ctx.send(embed=HeroData)

    #Rusty
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def rusty(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 16)

        await ctx.send(embed=HeroData)

    #Sarge
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def sarge(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 17)

        await ctx.send(embed=HeroData)

    #Tony
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def tony(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 18)

        await ctx.send(embed=HeroData)

    #Trish
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def trish(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 19)

        await ctx.send(embed=HeroData)

    #Wolfe
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def wolfe(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 20)

        await ctx.send(embed=HeroData)

    #Zach
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def zach(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 21)

        await ctx.send(embed=HeroData)

    #Zoe
    @commands.command()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def zoe(self, ctx):
        HeroData = await HeroesCog.getHeroData(self, ctx, 22)

        await ctx.send(embed=HeroData)











def setup(client):
    client.add_cog(HeroesCog(client))