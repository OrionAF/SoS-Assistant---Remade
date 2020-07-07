import discord
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class InfoCog(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def info(self, ctx):
        if ctx.invoked_subcommand is None:
            embedInfo = discord.Embed(title='Resource, Infected and Infected Fiend information.',colour=discord.Colour(8007567), description=f'**I**, <@&713050643526451262>, have gathered information for all the resource tiles, Infected, Infected Fiends,  Infected Hunters and the Plague Zones.\n\n**Infected Levels 1-30**\n\n**Infected Fiends Levels 1-5**\n\n**Infected Hunters, Elite and Normal**\n\n**Plague Zones Levels 1-30**\n\n**Resource Tiles**\nFood: Level 1-8\nWood: Level 1-8\nMetal: Level 1-8\nGas: Level 1-8')
            embedInfo.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embedInfo)

    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('This command has a **10** second cooldown.  Please retry in: **{:.2f}s**'.format(error.retry_after))


def setup(client):
    client.add_cog(InfoCog(client))