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

    @commands.command()
    async def travis(self, ctx):
        embedHero = discord.Embed(title=f'Travis', colour=discord.Colour(16333359), description="*One of Travis Cody's earliest memories is holding his grandfather's hunting rifle on the porch of the old house.  It went off by accident, blowing the lightbulp to pieces, and the young Travis was hooked.  He would accompany his grandfather and father on hunting expeditions from a young age and his hunting skills eventually helped him excel as a combat tracker in the military.  He enjoys a friendly rivalry with Jane, often having competitions to see who can hit a Lurcher between the eyes from the furthest distance.  He refers to all Infected as “varmint”, which confuses Nikola to no end.*")
        embedHero.set_author(name=f'Travis', icon_url='https://i.imgur.com/vwpD7pP.png')
        embedHero.add_field(name='​', value=f'​', inline=False)
        embedHero.add_field(name='', value=f'​', inline=False)
        embedHero.set_thumbnail(url='https://i.imgur.com/oVYh6KG.png')
        embedHero.set_image(url='https://i.imgur.com/xl37giI.png')
        embedHero.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedHero.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedHero)











def setup(client):
    client.add_cog(HeroesCog(client))