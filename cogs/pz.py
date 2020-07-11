import discord
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class PlagueZoneCog(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def pz(self, ctx):
        embedPZ1st = discord.Embed(colour=discord.Colour(16302848), description=f'**| Zone Matriarch | Challenge Stage |**\n\n<:Squad_Power:731035257876381697>Squad Power: **22,497**\n\n\n**Stats**\n\nHealth: **19,554**\nAttack: **42.4**\nDefense: **220**\n\n\n**Infected Skills**\n\n**Toxic Spit:** *Spits out a highly-toxic\nsubstance, dealing heavy initial\ndamage to target as well as lingering\ncontinuous damage over time.*\n\n\n**Rewards**\n\n<:Food:723743319389110312> x34,000\n<:Wood:723743319150297159> x34,000\nRare Hero Badge: 1\nRare Skill Book: 1\n<:CombatBookI:723744670076633168> x1')
        embedPZ = discord.Embed(colour=discord.Colour(16302848), description=f'**| Zone Matriarch | March Stage |**\n\n<:Squad_Power:731035257876381697>Squad Power: **6,480**\n\n\nPlague Zone Troop Power: **3,510**\nPlague Zone Troop Amount: **798**\n\n**Plague Zone Troop Breakdown**')
        embedPZ1st.set_author(name=f'Plague Zone Level 1', icon_url=f'https://i.imgur.com/Vf1Jax1.png')
        embedPZ.set_author(name='​', icon_url='https://i.imgur.com/dg7qbw0.png')
        embedPZ1st.set_thumbnail(url=f'https://i.imgur.com/wuoIs2y.png')
        embedPZ.set_thumbnail(url='https://i.imgur.com/dg7qbw0.png')
        embedPZ1st.set_image(url=f'https://i.imgur.com/UmrfghY.png')
        embedPZ.set_image(url='https://i.imgur.com/nQAmEom.png')        
        embedPZ.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedPZ.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedPZ1st)
        await ctx.send(embed=embedPZ)






























def setup(client):
    client.add_cog(PlagueZoneCog(client))