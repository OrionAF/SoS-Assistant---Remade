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
        cursor = db.cursor()
        cursor.execute("SELECT color, description, title, icon_url, main_skills, replace(max_lvl_military, '\\n', '\n') as max_lvl_military, replace(starting_lvl_military, '\\n', '\n') as starting_lvl_military, replace(max_lvl_explorer, '\\n', '\n') as max_lvl_explorer, replace(starting_lvl_explorer, '\\n', '\n') as starting_lvl_explorer, thumbnail, image, replace(footer, '\\n', '\n') as footer FROM heroes WHERE name = ?", (lvl,))
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

        await ctx.send(embed=embedHeroStart)

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











def setup(client):
    client.add_cog(HeroesCog(client))