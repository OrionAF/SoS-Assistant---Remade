import discord
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class _190Cog(commands.Cog, name='190Cog'):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role(703003853796409434)
    async def staterules(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = datetime.datetime.now()

        embed190 = discord.Embed(title='State Rules **Updated August 19th, amended by Governer**', colour=discord.Colour(29952), description=f"1.) No Tile hitting, unless within your alliance boundary or Kill Event.\n2.) No attacking of alliances during Trap, Horde and Fortress event.\n3.)  Facilities are free for all. Each alliance may hold only 1 Facility.\n**4.) Each alliance may hold up to 2 Bunkers. Only Bunker 10 will be for T9s and below. (NO level 30 players and above).**")
        embed190.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embed190.timestamp = datetime.datetime.utcnow()

        embed190Log = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embed190Log.set_author(name='State 190 rules.', icon_url=f'{ctx.author.avatar_url}')
        embed190Log.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embed190Log.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embed190)
        await channelInfoLogs.send(embed=embed190Log)
        await channelInfoLogs.send((f'◆↓◆↓◆↓◆↓◆↓◆↓◆'))

    @staterules.error
    async def staterules_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send(f'You are missing the required role to execute this command.')













def setup(client):
    client.add_cog(_190Cog(client))