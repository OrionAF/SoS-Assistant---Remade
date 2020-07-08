import discord
import os
from discord.ext import commands, tasks
import datetime as DT
import asyncio
import random


class Information(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.group()
    #@commands.has_role(703013734045712424)
    #@commands.cooldown(1, 10, commands.BucketType.user)
    async def info(self, ctx):
        if ctx.invoked_subcommand is None:
            currentDT = DT.datetime.now()
            embedInfo = discord.Embed(title='Resource, Infected and Infected Fiend information.',colour=discord.Colour(8007567), description=f'**I**, <@&713050643526451262>, have gathered information for all the resource tiles, Infected, Infected Fiends,  Infected Hunters and the Plague Zones.\n\n**Infected Levels 1-30**\n\n**Infected Fiends Levels 1-5**\n\n**Infected Hunters, Elite and Normal**\n\n**Plague Zones Levels 1-30**\n\n**Resource Tiles**\nFood: Level 1-8\nWood: Level 1-8\nMetal: Level 1-8\nGas: Level 1-8', timestamp=currentDT)
            await ctx.send(embed=embedInfo)

    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('This command has a **10** second cooldown.  Please retry in: **{:.2f}s**'.format(error.retry_after))


##################################################################################################
#                                                                                                #
#             Everthing here below is information on the Infected.                               #
#                                                                                                #
##################################################################################################



    @info.command(aliases=['Ilvl1', 'infectedlvl1', 'Infectedlvl1', 'ilv1', 'Ilv1', 'inflvl1', 'Inflvl1', 'inflv1', 'Inflv1', 'i1', 'I1'])
    async def ilvl1(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.1 Lurcher', colour=discord.Colour(16333359), description=f'*Slow, but unrelenting, in the pursuit of your brains.*\n\nRecommended Troop Power **189**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **120**\nInfected Troop amount: **40**\n\n**Infected Troop breakdown**', timestamp=currentDT)
        embedInf.set_thumbnail(url='https://i.imgur.com/aNaHPVP.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723701261148487710/image0.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.1 Lurcher', colour=discord.Colour(16333359), description=f'*Slow, but unrelenting, in the pursuit of your brains.*\n\nRecommended Troop Power **189**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **120**\nInfected Troop amount: **40**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})', timestamp=currentDT)
        embedInfLog.set_thumbnail(url='https://i.imgur.com/aNaHPVP.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723701261148487710/image0.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl2', 'infectedlvl2', 'Infectedlvl2', 'ilv2', 'Ilv2', 'inflvl2', 'Inflvl2', 'inflv2', 'Inflv2', 'i2', 'I2'])
    async def ilvl2(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.2 Lurcher', colour=discord.Colour(16333359), description=f'*Slow, but unrelenting, in the pursuit of your brains.*\n\nRecommended Troop Power **344**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **222**\nInfected Troop amount: **74**\n\n**Infected Troop breakdown**', timestamp=currentDT)
        embedInf.set_thumbnail(url='https://i.imgur.com/aNaHPVP.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723703075508060200/image0.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.2 Lurcher', colour=discord.Colour(16333359), description=f'*Slow, but unrelenting, in the pursuit of your brains.*\n\nRecommended Troop Power **344**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **222**\nInfected Troop amount: **74**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})', timestamp=currentDT)
        embedInfLog.set_thumbnail(url='https://i.imgur.com/aNaHPVP.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723703075508060200/image0.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl3', 'infectedlvl3', 'Infectedlvl3', 'ilv3', 'Ilv3', 'inflvl3', 'Inflvl3', 'inflv3', 'Inflv3', 'i3', 'I3'])
    async def ilvl3(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.3 Lurcher', colour=discord.Colour(16333359), description=f'*Slow, but unrelenting, in the pursuit of your brains.*\n\nRecommended Troop Power **525**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **345**\nInfected Troop amount: **115**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/aNaHPVP.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723704627232637068/image0.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.3 Lurcher', colour=discord.Colour(16333359), description=f'*Slow, but unrelenting, in the pursuit of your brains.*\n\nRecommended Troop Power **525**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **345**\nInfected Troop amount: **115**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/aNaHPVP.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723704627232637068/image0.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl4', 'infectedlvl4', 'Infectedlvl4', 'ilv4', 'Ilv4', 'inflvl4', 'Inflvl4', 'inflv4', 'Inflv4', 'i4', 'I4'])
    async def ilvl4(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.4 Runner', colour=discord.Colour(16333359), description=f'*Recently turned.  Much quicker than later-stage Infected.*\n\nRecommended Troop Power **781**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **511**\nInfected Troop amount: **160**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/NShnXS1.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723729177790119986/image0.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.4 Runner', colour=discord.Colour(16333359), description=f'*Recently turned.  Much quicker than later-stage Infected.*\n\nRecommended Troop Power **781**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **511**\nInfected Troop amount: **160**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/NShnXS1.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723729177790119986/image0.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl5', 'infectedlvl5', 'Infectedlvl5', 'ilv5', 'Ilv5', 'inflvl5', 'Inflvl5', 'inflv5', 'Inflv5', 'i5', 'I5'])
    async def ilvl5(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.5 Runner', colour=discord.Colour(16333359), description=f'*Recently turned.  Much quicker than later-stage Infected.*\n\nRecommended Troop Power **1,098**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **724**\nInfected Troop amount: **213**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/NShnXS1.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723732731632156713/4.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.5 Runner', colour=discord.Colour(16333359), description=f'*Recently turned.  Much quicker than later-stage Infected.*\n\nRecommended Troop Power **1,098**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **724**\nInfected Troop amount: **213**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/NShnXS1.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723732731632156713/4.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl6', 'infectedlvl6', 'Infectedlvl6', 'ilv6', 'Ilv6', 'inflvl6', 'Inflvl6', 'inflv6', 'Inflv6', 'i6', 'I6'])
    async def ilvl6(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.6 Runner', colour=discord.Colour(16333359), description=f'*Recently turned.  Much quicker than later-stage Infected.*\n\nRecommended Troop Power **2,000**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **1,328**\nInfected Troop amount: **332**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/NShnXS1.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723733389227851806/image0.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.6 Runner', colour=discord.Colour(16333359), description=f'*Recently turned.  Much quicker than later-stage Infected.*\n\nRecommended Troop Power **2,000**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **1,328**\nInfected Troop amount: **332**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/NShnXS1.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723733389227851806/image0.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')
    
    @info.command(aliases=['Ilvl7', 'infectedlvl7', 'Infectedlvl7', 'ilv7', 'Ilv7', 'inflvl7', 'Inflvl7', 'inflv7', 'Inflv7', 'i7', 'I7'])
    async def ilvl7(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.7 Spitter', colour=discord.Colour(16333359), description=f'*Talk about a reflux problem.*\n\nRecommended Troop Power **3,135**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **2,084**\nInfected Troop amount: **474**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/48Y0op5.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723736023259021413/image0_1.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.7 Spitter', colour=discord.Colour(16333359), description=f'*Talk about a reflux problem.*\n\nRecommended Troop Power **3,135**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **2,084**\nInfected Troop amount: **474**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/48Y0op5.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723736023259021413/image0_1.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl8', 'infectedlvl8', 'Infectedlvl8', 'ilv8', 'Ilv8', 'inflvl8', 'Inflvl8', 'inflv8', 'Inflv8', 'i8', 'I8'])
    async def ilvl8(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.8 Spitter', colour=discord.Colour(16333359), description=f'*Talk about a reflux problem.*\n\nRecommended Troop Power **4,621**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **3,062**\nInfected Troop amount: **638**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/48Y0op5.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723738648591204392/image0_2.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.8 Spitter', colour=discord.Colour(16333359), description=f'*Talk about a reflux problem.*\n\nRecommended Troop Power **4,621**\n\n**Chance to get:**\n<:Food:723743319389110312> 25,000\n<:Wood:723743319150297159> 25,000\n<:CombatBookI:723744670076633168> 1x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **3,062**\nInfected Troop amount: **638**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/48Y0op5.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723738648591204392/image0_2.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl9', 'infectedlvl9', 'Infectedlvl9', 'ilv9', 'Ilv9', 'inflvl9', 'Inflvl9', 'inflv9', 'Inflv9', 'i9', 'I9'])
    async def ilvl9(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.9 Spitter', colour=discord.Colour(16333359), description=f'*Talk about a reflux problem.*\n\nRecommended Troop Power **7,521**\n\n**Chance to get:**\n<:Food:723743319389110312> 33,000\n<:Wood:723743319150297159> 33,000\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **5,004**\nInfected Troop amount: **834**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/48Y0op5.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723739969192984616/image0.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.9 Spitter', colour=discord.Colour(16333359), description=f'*Talk about a reflux problem.*\n\nRecommended Troop Power **7,521**\n\n**Chance to get:**\n<:Food:723743319389110312> 33,000\n<:Wood:723743319150297159> 33,000\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **5,004**\nInfected Troop amount: **834**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/48Y0op5.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723739969192984616/image0.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl10', 'infectedlvl10', 'Infectedlvl10', 'ilv10', 'Ilv10', 'inflvl10', 'Inflvl10', 'inflv10', 'Inflv10', 'i10', 'I10'])
    async def ilvl10(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.10 Spitter', colour=discord.Colour(16333359), description=f'*Talk about a reflux problem.*\n\nRecommended Troop Power **10,480**\n\n**Chance to get:**\n<:Food:723743319389110312> 33,000\n<:Wood:723743319150297159> 33,000\n<:Metal:723743319221469184> 6,600\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **6,975**\nInfected Troop amount: **1,057**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/48Y0op5.gif')
        embedInf.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723740560032137286/image0_3.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.10 Spitter', colour=discord.Colour(16333359), description=f'*Talk about a reflux problem.*\n\nRecommended Troop Power **10,480**\n\n**Chance to get:**\n<:Food:723743319389110312> 33,000\n<:Wood:723743319150297159> 33,000\n<:Metal:723743319221469184> 6,600\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **6,975**\nInfected Troop amount: **1,057**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/48Y0op5.gif')
        embedInfLog.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/723740560032137286/image0_3.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl11', 'infectedlvl11', 'Infectedlvl11', 'ilv11', 'Ilv11', 'inflvl11', 'Inflvl11', 'inflv11', 'Inflv11', 'i11', 'I11'])
    async def ilvl11(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.11 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **15,795**\n\n**Chance to get:**\n<:Food:723743319389110312> 41,500\n<:Wood:723743319150297159> 41,500\n<:Metal:723743319221469184> 8,300\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **10,509**\nInfected Troop amount: **1,460**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInf.set_image(url='https://i.imgur.com/zz18CJR.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.11 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **15,795**\n\n**Chance to get:**\n<:Food:723743319389110312> 41,500\n<:Wood:723743319150297159> 41,500\n<:Metal:723743319221469184> 8,300\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **10,509**\nInfected Troop amount: **1,460**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInfLog.set_image(url='https://i.imgur.com/zz18CJR.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl12', 'infectedlvl12', 'Infectedlvl12', 'ilv12', 'Ilv12', 'inflvl12', 'Inflvl12', 'inflv12', 'Inflv12', 'i12', 'I12'])
    async def ilvl12(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.12 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **27,766**\n\n**Chance to get:**\n<:Food:723743319389110312> 41,500\n<:Wood:723743319150297159> 41,500\n<:Metal:723743319221469184> 8,300\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **17,334**\nInfected Troop amount: **1,926**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInf.set_image(url='https://i.imgur.com/hWbEMso.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.12 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **27,766**\n\n**Chance to get:**\n<:Food:723743319389110312> 41,500\n<:Wood:723743319150297159> 41,500\n<:Metal:723743319221469184> 8,300\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **17,334**\nInfected Troop amount: **1,926**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInfLog.set_image(url='https://i.imgur.com/hWbEMso.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl13', 'infectedlvl13', 'Infectedlvl13', 'ilv13', 'Ilv13', 'inflvl13', 'Inflvl13', 'inflv13', 'Inflv13', 'i13', 'I13'])
    async def ilvl13(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.13 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **43,404**\n\n**Chance to get:**\n<:Food:723743319389110312> 45,000\n<:Wood:723743319150297159> 45,000\n<:Metal:723743319221469184> 9,000\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **24,077**\nInfected Troop amount: **2,457**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInf.set_image(url='https://i.imgur.com/HQ3hv7m.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.13 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **43,404**\n\n**Chance to get:**\n<:Food:723743319389110312> 45,000\n<:Wood:723743319150297159> 45,000\n<:Metal:723743319221469184> 9,000\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **24,077**\nInfected Troop amount: **2,457**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInfLog.set_image(url='https://i.imgur.com/HQ3hv7m.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl14', 'infectedlvl14', 'Infectedlvl14', 'ilv14', 'Ilv14', 'inflvl14', 'Inflvl14', 'inflv14', 'Inflv14', 'i14', 'I14'])
    async def ilvl14(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.14 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **64,975**\n\n**Chance to get:**\n<:Food:723743319389110312> 48,500\n<:Wood:723743319150297159> 48,500\n<:Metal:723743319221469184> 9,700\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **32,458**\nInfected Troop amount: **3,062**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInf.set_image(url='https://i.imgur.com/7br55Cg.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.14 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **64,975**\n\n**Chance to get:**\n<:Food:723743319389110312> 48,500\n<:Wood:723743319150297159> 48,500\n<:Metal:723743319221469184> 9,700\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **32,458**\nInfected Troop amount: **3,062**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInfLog.set_image(url='https://i.imgur.com/7br55Cg.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl15', 'infectedlvl15', 'Infectedlvl15', 'ilv15', 'Ilv15', 'inflvl15', 'Inflvl15', 'inflv15', 'Inflv15', 'i15', 'I15'])
    async def ilvl15(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.15 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **107,171**\n\n**Chance to get:**\n<:Food:723743319389110312> 56,000\n<:Wood:723743319150297159> 56,000\n<:Metal:723743319221469184> 11,200\n<:Gas:723743319187914884> 2,800\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **48,698**\nInfected Troop amount: **3,746**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInf.set_image(url='https://i.imgur.com/qvP5lUh.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.15 Swiper', colour=discord.Colour(16333359), description=f'*Keep your distance or lose your looks*\n\nRecommended Troop Power **107,171**\n\n**Chance to get:**\n<:Food:723743319389110312> 56,000\n<:Wood:723743319150297159> 56,000\n<:Metal:723743319221469184> 11,200\n<:Gas:723743319187914884> 2,800\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **48,698**\nInfected Troop amount: **3,746**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfLog.set_thumbnail(url='https://i.imgur.com/UPcYY2S.gif')
        embedInfLog.set_image(url='https://i.imgur.com/qvP5lUh.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl16', 'infectedlvl16', 'Infectedlvl16', 'ilv16', 'Ilv16', 'inflvl16', 'Inflvl16', 'inflv16', 'Inflv16', 'i16', 'I16'])
    async def ilvl16(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.16 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **176,108**\n\n**Chance to get:**\n<:Food:723743319389110312> 56,000\n<:Wood:723743319150297159> 56,000\n<:Metal:723743319221469184> 11,200\n<:Gas:723743319187914884> 2,800\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **73,302**\nInfected Troop amount: **5,091**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInf.set_image(url='https://i.imgur.com/qSsXXI9.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.16 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **176,108**\n\n**Chance to get:**\n<:Food:723743319389110312> 56,000\n<:Wood:723743319150297159> 56,000\n<:Metal:723743319221469184> 11,200\n<:Gas:723743319187914884> 2,800\n<:CombatBookI:723744670076633168> 2x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **73,302**\nInfected Troop amount: **5,091**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInfLog.set_image(url='https://i.imgur.com/qSsXXI9.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl17', 'infectedlvl17', 'Infectedlvl17', 'ilv17', 'Ilv17', 'inflvl17', 'Inflvl17', 'inflv17', 'Inflv17', 'i17', 'I17'])
    async def ilvl17(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.17 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **273,786**\n\n**Chance to get:**\n<:Food:723743319389110312> 62,500\n<:Wood:723743319150297159> 62,500\n<:Metal:723743319221469184> 12,500\n<:Gas:723743319187914884> 3,100\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **105,261**\nInfected Troop amount: **6,662**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInf.set_image(url='https://i.imgur.com/q4VH8Sh.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.17 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **273,786**\n\n**Chance to get:**\n<:Food:723743319389110312> 62,500\n<:Wood:723743319150297159> 62,500\n<:Metal:723743319221469184> 12,500\n<:Gas:723743319187914884> 3,100\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **105,261**\nInfected Troop amount: **6,662**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInfLog.set_image(url='https://i.imgur.com/q4VH8Sh.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl18', 'infectedlvl18', 'Infectedlvl18', 'ilv18', 'Ilv18', 'inflvl18', 'Inflvl18', 'inflv18', 'Inflv18', 'i18', 'I18'])
    async def ilvl18(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.18 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **484,655**\n\n**Chance to get:**\n<:Food:723743319389110312> 66,500\n<:Wood:723743319150297159> 66,500\n<:Metal:723743319221469184> 13,300\n<:Gas:723743319187914884> 3,350\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **173,080**\nInfected Troop amount: **8,654**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInf.set_image(url='https://i.imgur.com/9qaMBr3.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.18 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **484,655**\n\n**Chance to get:**\n<:Food:723743319389110312> 66,500\n<:Wood:723743319150297159> 66,500\n<:Metal:723743319221469184> 13,300\n<:Gas:723743319187914884> 3,350\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **173,080**\nInfected Troop amount: **8,654**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInfLog.set_image(url='https://i.imgur.com/9qaMBr3.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl19', 'infectedlvl19', 'Infectedlvl19', 'ilv19', 'Ilv19', 'inflvl19', 'Inflvl19', 'inflv19', 'Inflv19', 'i19', 'I19'])
    async def ilvl19(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.19 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **724,444**\n\n**Chance to get:**\n<:Food:723743319389110312> 70,500\n<:Wood:723743319150297159> 70,500\n<:Metal:723743319221469184> 14,100\n<:Gas:723743319187914884> 3,500\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **241,412**\nInfected Troop amount: **11,177**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInf.set_image(url='https://i.imgur.com/eLhoEvZ.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.19 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **724,444**\n\n**Chance to get:**\n<:Food:723743319389110312> 70,500\n<:Wood:723743319150297159> 70,500\n<:Metal:723743319221469184> 14,100\n<:Gas:723743319187914884> 3,500\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **241,412**\nInfected Troop amount: **11,177**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInfLog.set_image(url='https://i.imgur.com/eLhoEvZ.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl20', 'infectedlvl20', 'Infectedlvl20', 'ilv20', 'Ilv20', 'inflvl20', 'Inflvl20', 'inflv20', 'Inflv20', 'i20', 'I20'])
    async def ilvl20(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.20 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **983,156**\n\n**Chance to get:**\n<:Food:723743319389110312> 74,500\n<:Wood:723743319150297159> 74,500\n<:Metal:723743319221469184> 14,900\n<:Gas:723743319187914884> 3,700\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **327,652**\nInfected Troop amount: **14,123**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInf.set_image(url='https://i.imgur.com/ToFq4Ho.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.20 Regenerator', colour=discord.Colour(16333359), description=f"*Headshot.  Don't mess around.*\n\nRecommended Troop Power **983,156**\n\n**Chance to get:**\n<:Food:723743319389110312> 74,500\n<:Wood:723743319150297159> 74,500\n<:Metal:723743319221469184> 14,900\n<:Gas:723743319187914884> 3,700\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **327,652**\nInfected Troop amount: **14,123**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/DNN0LcM.gif')
        embedInfLog.set_image(url='https://i.imgur.com/ToFq4Ho.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')
    
    @info.command(aliases=['Ilvl21', 'infectedlvl21', 'Infectedlvl21', 'ilv21', 'Ilv21', 'inflvl21', 'Inflvl21', 'inflv21', 'Inflv21', 'i21', 'I21'])
    async def ilvl21(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.21 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **1,614,060**\n\n**Chance to get:**\n<:Food:723743319389110312> 78,500\n<:Wood:723743319150297159> 78,500\n<:Metal:723743319221469184> 15,700\n<:Gas:723743319187914884> 3,950\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **537,992**\nInfected Troop amount: **19,214**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/562chXp.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.21 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **1,614,060**\n\n**Chance to get:**\n<:Food:723743319389110312> 78,500\n<:Wood:723743319150297159> 78,500\n<:Metal:723743319221469184> 15,700\n<:Gas:723743319187914884> 3,950\n<:CombatBookI:723744670076633168> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **537,992**\nInfected Troop amount: **19,214**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/562chXp.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl22', 'infectedlvl22', 'Infectedlvl22', 'ilv22', 'Ilv22', 'inflvl22', 'Inflvl22', 'inflv22', 'Inflv22', 'i22', 'I22'])
    async def ilvl22(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.22 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **2,268,621**\n\n**Chance to get:**\n<:Food:723743319389110312> 82,500\n<:Wood:723743319150297159> 82,500\n<:Metal:723743319221469184> 16,500\n<:Gas:723743319187914884> 4,150\n<:CombatBookI:723744670076633168> 3x\n<:AdvancedAlloy:724115815649247293> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **756,084**\nInfected Troop amount: **25,203**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/8zkwXrp.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.22 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **2,268,621**\n\n**Chance to get:**\n<:Food:723743319389110312> 82,500\n<:Wood:723743319150297159> 82,500\n<:Metal:723743319221469184> 16,500\n<:Gas:723743319187914884> 4,150\n<:CombatBookI:723744670076633168> 3x\n<:AdvancedAlloy:724115815649247293> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **756,084**\nInfected Troop amount: **25,203**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/8zkwXrp.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl23', 'infectedlvl23', 'Infectedlvl23', 'ilv23', 'Ilv23', 'inflvl23', 'Inflvl23', 'inflv23', 'Inflv23', 'i23', 'I23'])
    async def ilvl23(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.23 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **3,091,029**\n\n**Chance to get:**\n<:Food:723743319389110312> 90,000\n<:Wood:723743319150297159> 90,000\n<:Metal:723743319221469184> 18,000\n<:Gas:723743319187914884> 4,500\n<:CombatBookI:723744670076633168> 4x\n<:AdvancedAlloy:724115815649247293> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **1,030,202**\nInfected Troop amount: **32,194**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/UStQWk5.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.23 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **3,091,029**\n\n**Chance to get:**\n<:Food:723743319389110312> 90,000\n<:Wood:723743319150297159> 90,000\n<:Metal:723743319221469184> 18,000\n<:Gas:723743319187914884> 4,500\n<:CombatBookI:723744670076633168> 4x\n<:AdvancedAlloy:724115815649247293> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **1,030,202**\nInfected Troop amount: **32,194**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/UStQWk5.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl24', 'infectedlvl24', 'Infectedlvl24', 'ilv24', 'Ilv24', 'inflvl24', 'Inflvl24', 'inflv24', 'Inflv24', 'i24', 'I24'])
    async def ilvl24(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.24 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **4,594,200**\n\n**Chance to get:**\n<:Food:723743319389110312> 94,500\n<:Wood:723743319150297159> 94,500\n<:Metal:723743319221469184> 18,900\n<:Gas:723743319187914884> 4,750\n<:CombatBookI:723744670076633168> 4x\n<:AdvancedAlloy:724115815649247293> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **1,531,400**\nInfected Troop amount: **40,300**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/1nTnYcR.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.24 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **4,594,200**\n\n**Chance to get:**\n<:Food:723743319389110312> 94,500\n<:Wood:723743319150297159> 94,500\n<:Metal:723743319221469184> 18,900\n<:Gas:723743319187914884> 4,750\n<:CombatBookI:723744670076633168> 4x\n<:AdvancedAlloy:724115815649247293> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **1,531,400**\nInfected Troop amount: **40,300**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/1nTnYcR.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl25', 'infectedlvl25', 'Infectedlvl25', 'ilv25', 'Ilv25', 'inflvl25', 'Inflvl25', 'inflv25', 'Inflv25', 'i25', 'I25'])
    async def ilvl25(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.25 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **5,659,004**\n\n**Chance to get:**\n<:Food:723743319389110312> 106,000\n<:Wood:723743319150297159> 106,000\n<:Metal:723743319221469184> 21,000\n<:Gas:723743319187914884> 5,300\n<:CombatBookI:723744670076633168> 4x\n<:AdvancedAlloy:724115815649247293> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **1,886,320**\nInfected Troop amount: **49,640**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/rUjfhjr.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.25 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **5,659,004**\n\n**Chance to get:**\n<:Food:723743319389110312> 106,000\n<:Wood:723743319150297159> 106,000\n<:Metal:723743319221469184> 21,000\n<:Gas:723743319187914884> 5,300\n<:CombatBookI:723744670076633168> 4x\n<:AdvancedAlloy:724115815649247293> 3x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **1,886,320**\nInfected Troop amount: **49,640**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/rUjfhjr.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl26', 'infectedlvl26', 'Infectedlvl26', 'ilv26', 'Ilv26', 'inflvl26', 'Inflvl26', 'inflv26', 'Inflv26', 'i26', 'I26'])
    async def ilvl26(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.26 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **7,061,403**\n\n**Chance to get:**\n<:Food:723743319389110312> 119,000\n<:Wood:723743319150297159> 119,000\n<:Metal:723743319221469184> 23,800\n<:Gas:723743319187914884> 5,950\n<:CombatBookI:723744670076633168> 5x\n<:AdvancedAlloy:724115815649247293> 4x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **2,353,654**\nInfected Troop amount: **58,259**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/wWJWW54.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.26 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **7,061,403**\n\n**Chance to get:**\n<:Food:723743319389110312> 119,000\n<:Wood:723743319150297159> 119,000\n<:Metal:723743319221469184> 23,800\n<:Gas:723743319187914884> 5,950\n<:CombatBookI:723744670076633168> 5x\n<:AdvancedAlloy:724115815649247293> 4x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **2,353,654**\nInfected Troop amount: **58,259**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/wWJWW54.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl27', 'infectedlvl27', 'Infectedlvl27', 'ilv27', 'Ilv27', 'inflvl27', 'Inflvl27', 'inflv27', 'Inflv27', 'i27', 'I27'])
    async def ilvl27(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.27 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **8,692,520**\n\n**Chance to get:**\n<:Food:723743319389110312> 133,500\n<:Wood:723743319150297159> 133,500\n<:Metal:723743319221469184> 26,700\n<:Gas:723743319187914884> 6,650\n<:CombatBookI:723744670076633168> 5x\n<:AdvancedAlloy:724115815649247293> 4x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **2,897,296**\nInfected Troop amount: **67,694**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/CVg70NU.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.27 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **8,692,520**\n\n**Chance to get:**\n<:Food:723743319389110312> 133,500\n<:Wood:723743319150297159> 133,500\n<:Metal:723743319221469184> 26,700\n<:Gas:723743319187914884> 6,650\n<:CombatBookI:723744670076633168> 5x\n<:AdvancedAlloy:724115815649247293> 4x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **2,897,296**\nInfected Troop amount: **67,694**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/CVg70NU.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl28', 'infectedlvl28', 'Infectedlvl28', 'ilv28', 'Ilv28', 'inflvl28', 'Inflvl28', 'inflv28', 'Inflv28', 'i28', 'I28'])
    async def ilvl28(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.28 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **11,822,087**\n\n**Chance to get:**\n<:Food:723743319389110312> 149,000\n<:Wood:723743319150297159> 149,000\n<:Metal:723743319221469184> 29,800\n<:Gas:723743319187914884> 7,450\n<:CombatBookI:723744670076633168> 6x\n<:AdvancedAlloy:724115815649247293> 5x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **3,940,600**\nInfected Troop amount: **78,812**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/PEqmLax.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.28 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **11,822,087**\n\n**Chance to get:**\n<:Food:723743319389110312> 149,000\n<:Wood:723743319150297159> 149,000\n<:Metal:723743319221469184> 29,800\n<:Gas:723743319187914884> 7,450\n<:CombatBookI:723744670076633168> 6x\n<:AdvancedAlloy:724115815649247293> 5x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **3,940,600**\nInfected Troop amount: **78,812**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/PEqmLax.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl29', 'infectedlvl29', 'Infectedlvl29', 'ilv29', 'Ilv29', 'inflvl29', 'Inflvl29', 'inflv29', 'Inflv29', 'i29', 'I29'])
    async def ilvl29(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.29 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **13,792,705**\n\n**Chance to get:**\n<:Food:723743319389110312> 169,500\n<:Wood:723743319150297159> 169,500\n<:Metal:723743319221469184> 33,900\n<:Gas:723743319187914884> 8,500\n<:CombatBookI:723744670076633168> 7x\n<:AdvancedAlloy:724115815649247293> 6x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **4,597,450**\nInfected Troop amount: **91,949**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/ZmKcwax.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.29 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **13,792,705**\n\n**Chance to get:**\n<:Food:723743319389110312> 169,500\n<:Wood:723743319150297159> 169,500\n<:Metal:723743319221469184> 33,900\n<:Gas:723743319187914884> 8,500\n<:CombatBookI:723744670076633168> 7x\n<:AdvancedAlloy:724115815649247293> 6x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **4,597,450**\nInfected Troop amount: **91,949**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/ZmKcwax.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @info.command(aliases=['Ilvl30', 'infectedlvl30', 'Infectedlvl30', 'ilv30', 'Ilv30', 'inflvl30', 'Inflvl30', 'inflv30', 'Inflv30', 'i30', 'I30'])
    async def ilvl30(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.30 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **17,161,788**\n\n**Chance to get:**\n<:Food:723743319389110312> 187,500\n<:Wood:723743319150297159> 187,500\n<:Metal:723743319221469184> 37,500\n<:Gas:723743319187914884> 9,400\n<:CombatBookI:723744670076633168> 8x\n<:AdvancedAlloy:724115815649247293> 6x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **5,720,480**\nInfected Troop amount: **107,528**\n\n**Infected Troop breakdown**")
        embedInf.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInf.set_image(url='https://i.imgur.com/5gtLA1c.png')
        embedInf.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.30 Summoner', colour=discord.Colour(16333359), description=f"*Be prepared to have company.*\n\nRecommended Troop Power **17,161,788**\n\n**Chance to get:**\n<:Food:723743319389110312> 187,500\n<:Wood:723743319150297159> 187,500\n<:Metal:723743319221469184> 37,500\n<:Gas:723743319187914884> 9,400\n<:CombatBookI:723744670076633168> 8x\n<:AdvancedAlloy:724115815649247293> 6x\n\nStamina Cost: **10**\nTravis Stamina Cost: **8**\n\nInfected Battle Power: **5,720,480**\nInfected Troop amount: **107,528**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})")
        embedInfLog.set_thumbnail(url='https://i.imgur.com/kp3iQWp.gif')
        embedInfLog.set_image(url='https://i.imgur.com/5gtLA1c.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')



##################################################################################################
#                                                                                                #
#             Everthing here below is information on the Infected Fiends.                        #
#                                                                                                #
##################################################################################################


    @info.command(aliases=['Iflvl1', 'IFlvl1', 'iFlvl1', 'iflv1', 'Iflv1', 'IFlv1', 'iFlv1', 'if1', 'If1', 'IF1', 'iF1', 'fiendlvl1', 'Fiendlvl1', 'fiendlv1', 'Fiendlv1'])
    async def iflvl1(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.1 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **369,256**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KWood:728344428170707064> x24\n<:5minhealingspeedup:728344428175163402> x1\n\n**Possible Rewards:**\n<:SargeFragment:728344427944214600> x1-2\n<:EpicHeroParts:728344428078432386> x1-2\n<:Biocaps:728344427617321001> x10-14\n<:10KFood:728344428095209533> x10-20\n<:10KWood:728344428087083018> x10-20\n<:1KMetal:728344427982094368> x20-40\n<:1KGas:728344428040683632> x5-10\n<:1minTroopSpeedup:728345986761490433> x4-8\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **138,801**\nInfected Troop amount: **10,677**\n\n**Infected Troop breakdown**')
        embedInf.set_thumbnail(url='https://i.imgur.com/1fem4o3.gif')
        embedInf.set_image(url='https://i.imgur.com/Bj4f91X.png')
        embedInf.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.1 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **369,256**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KWood:728344428170707064> x24\n<:5minhealingspeedup:728344428175163402> x1\n\n**Possible Rewards:**\n<:SargeFragment:728344427944214600> x1-2\n<:EpicHeroParts:728344428078432386> x1-2\n<:Biocaps:728344427617321001> x10-14\n<:10KFood:728344428095209533> x10-20\n<:10KWood:728344428087083018> x10-20\n<:1KMetal:728344427982094368> x20-40\n<:1KGas:728344428040683632> x5-10\n<:1minTroopSpeedup:728345986761490433> x4-8\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **138,801**\nInfected Troop amount: **10,677**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})', timestamp=currentDT)
        embedInfLog.set_thumbnail(url='https://i.imgur.com/1fem4o3.gif')
        embedInfLog.set_image(url='https://i.imgur.com/Bj4f91X.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


    @info.command(aliases=['Iflvl2', 'IFlvl2', 'iFlvl2', 'iflv2', 'Iflv2', 'IFlv2', 'iFlv2', 'if2', 'If2', 'IF2', 'iF2', 'fiendlvl2', 'Fiendlvl2', 'fiendlv2', 'Fiendlv2'])
    async def iflvl2(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.2 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **1,380,002**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KFood:728344428292341770> x28\n<:5minhealingspeedup:728344428175163402> x1\n\n**Possible Rewards:**\n<:SargeFragment:728344427944214600> x2\n<:EpicHeroParts:728344428078432386> x1-2\n<:Biocaps:728344427617321001> x20\n<:10KFood:728344428095209533> x25\n<:10KWood:728344428087083018> x25\n<:1KMetal:728344427982094368> x50\n<:1KGas:728344428040683632> x13\n<:1minTroopSpeedup:728345986761490433> x11\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **496,140**\nInfected Troop amount: **24,807**\n\n**Infected Troop breakdown**', timestamp=currentDT)
        embedInf.set_thumbnail(url='https://i.imgur.com/CVzlZ8C.gif')
        embedInf.set_image(url='https://i.imgur.com/sw5cpoG.png')
        embedInf.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.2 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **1,380,002**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KFood:728344428292341770> x28\n<:5minhealingspeedup:728344428175163402> x1\n\n**Possible Rewards:**\n<:SargeFragment:728344427944214600> x2\n<:EpicHeroParts:728344428078432386> x1-2\n<:Biocaps:728344427617321001> x20\n<:10KFood:728344428095209533> x25\n<:10KWood:728344428087083018> x25\n<:1KMetal:728344427982094368> x50\n<:1KGas:728344428040683632> x13\n<:1minTroopSpeedup:728345986761490433> x11\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **496,140**\nInfected Troop amount: **24,807**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})', timestamp=currentDT)
        embedInfLog.set_thumbnail(url='https://i.imgur.com/CVzlZ8C.gif')
        embedInfLog.set_image(url='https://i.imgur.com/sw5cpoG.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


    @info.command(aliases=['Iflvl3', 'IFlvl3', 'iFlvl3', 'iflv3', 'Iflv3', 'IFlv3', 'iFlv3', 'if3', 'If3', 'IF3', 'iF3', 'fiendlvl3', 'Fiendlvl3', 'fiendlv3', 'Fiendlv3'])
    async def iflvl3(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.3 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **3,395,280**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KWood:728344428170707064> x32\n<:5minhealingspeedup:728344428175163402> x2\n\n**Possible Rewards:**\n<:SargeFragment:728344427944214600> x1-3\n<:EpicHeroParts:728344428078432386> x1-3\n<:Biocaps:728344427617321001> x26\n<:10KFood:728344428095209533> x25-33\n<:10KWood:728344428087083018> x25-33\n<:1KMetal:728344427982094368> x50-66\n<:1KGas:728344428040683632> x13-17\n<:1minTroopSpeedup:728345986761490433> x11-14\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **1,111,588**\nInfected Troop amount: **49,639**\n\n**Infected Troop breakdown**', timestamp=currentDT)
        embedInf.set_thumbnail(url='https://i.imgur.com/naqNQ2F.gif')
        embedInf.set_image(url='https://i.imgur.com/VPZIOzK.png')
        embedInf.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.3 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **3,395,280**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KWood:728344428170707064> x32\n<:5minhealingspeedup:728344428175163402> x2\n\n**Possible Rewards:**\n<:SargeFragment:728344427944214600> x1-3\n<:EpicHeroParts:728344428078432386> x1-3\n<:Biocaps:728344427617321001> x26\n<:10KFood:728344428095209533> x25-33\n<:10KWood:728344428087083018> x25-33\n<:1KMetal:728344427982094368> x50-66\n<:1KGas:728344428040683632> x13-17\n<:1minTroopSpeedup:728345986761490433> x11-14\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **1,111,588**\nInfected Troop amount: **49,639**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})', timestamp=currentDT)
        embedInfLog.set_thumbnail(url='https://i.imgur.com/naqNQ2F.gif')
        embedInfLog.set_image(url='https://i.imgur.com/VPZIOzK.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


    @info.command(aliases=['Iflvl4', 'IFlvl4', 'iFlvl4', 'iflv4', 'Iflv4', 'IFlv4', 'iFlv4', 'if4', 'If4', 'IF4', 'iF4', 'fiendlvl4', 'Fiendlvl4', 'fiendlv4', 'Fiendlv4'])
    async def iflvl4(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.4 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **12,043,682**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KFood:728344428292341770> x36\n<:5minhealingspeedup:728344428175163402> x2\n\n**Possible Rewards:**\n<:EpicHeroFragment:728344428116181022> x1-3\n<:EpicHeroParts:728344428078432386> x1\n<:Biocaps:728344427617321001> x24-26\n<:10KFood:728344428095209533> x33-40\n<:10KWood:728344428087083018> x33-40\n<:1KMetal:728344427982094368> x66-80\n<:1KGas:728344428040683632> x17-20\n<:1minTroopSpeedup:728345986761490433> x14-17\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **4,034,110**\nInfected Troop amount: **129,995**\n\n**Infected Troop breakdown**', timestamp=currentDT)
        embedInf.set_thumbnail(url='https://i.imgur.com/5YSZuz7.gif')
        embedInf.set_image(url='https://i.imgur.com/llpoZuc.png')
        embedInf.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.4 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **12,043,682**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KFood:728344428292341770> x36\n<:5minhealingspeedup:728344428175163402> x2\n\n**Possible Rewards:**\n<:EpicHeroFragment:728344428116181022> x1-3\n<:EpicHeroParts:728344428078432386> x1\n<:Biocaps:728344427617321001> x24-26\n<:10KFood:728344428095209533> x33-40\n<:10KWood:728344428087083018> x33-40\n<:1KMetal:728344427982094368> x66-80\n<:1KGas:728344428040683632> x17-20\n<:1minTroopSpeedup:728345986761490433> x14-17\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **4,034,110**\nInfected Troop amount: **129,995**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})', timestamp=currentDT)
        embedInfLog.set_thumbnail(url='https://i.imgur.com/5YSZuz7.gif')
        embedInfLog.set_image(url='https://i.imgur.com/llpoZuc.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


    @info.command(aliases=['Iflvl5', 'IFlvl5', 'iFlvl5', 'iflv5', 'Iflv5', 'IFlv5', 'iFlv5', 'if5', 'If5', 'IF5', 'iF5', 'fiendlvl5', 'Fiendlvl5', 'fiendlv5', 'Fiendlv5'])
    async def iflvl5(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Lv.5 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **30,802,716**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KWood:728344428170707064> x40\n<:5minhealingspeedup:728344428175163402> x3\n\n**Possible Rewards:**\n<:EpicHeroFragment:728344428116181022> x1\n<:EpicHeroParts:728344428078432386> x1\n<:Biocaps:728344427617321001> x30-32\n<:10KFood:728344428095209533> x40-50\n<:10KWood:728344428087083018> x40-50\n<:1KMetal:728344427982094368> x80-100\n<:1KGas:728344428040683632> x20-25\n<:1minTroopSpeedup:728345986761490433> x17-21\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **9,938,824**\nInfected Troop amount: **261,824**\n\n**Infected Troop breakdown**', timestamp=currentDT)
        embedInf.set_thumbnail(url='https://i.imgur.com/iMBesk8.gif')
        embedInf.set_image(url='https://i.imgur.com/gZMFkbB.png')
        embedInf.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Lv.5 Infected Fiend', colour=discord.Colour(13400320), description=f'*Fiends are more powerful than regular\nInfected.  Chiefs must join forces in a\nrally.*\n\nRecommended Troop Power **30,802,716**\n\n**Rally Launch Rewards:**\n<:EpicHeroBadge:728344428099666030> x1\n<:1KWood:728344428170707064> x40\n<:5minhealingspeedup:728344428175163402> x3\n\n**Possible Rewards:**\n<:EpicHeroFragment:728344428116181022> x1\n<:EpicHeroParts:728344428078432386> x1\n<:Biocaps:728344427617321001> x30-32\n<:10KFood:728344428095209533> x40-50\n<:10KWood:728344428087083018> x40-50\n<:1KMetal:728344427982094368> x80-100\n<:1KGas:728344428040683632> x20-25\n<:1minTroopSpeedup:728345986761490433> x17-21\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **9,938,824**\nInfected Troop amount: **261,824**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})', timestamp=currentDT)
        embedInfLog.set_thumbnail(url='https://i.imgur.com/iMBesk8.gif')
        embedInfLog.set_image(url='https://i.imgur.com/gZMFkbB.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


    @info.command(aliases=['norm', 'Normal', 'Norm', 'hunter', 'Hunter', 'normhunter', 'Normhunter', 'normHunter', 'NormHunter', 'normalhunter', 'Normalhunter', 'normalHunter', 'NormalHunter'])
    async def normal(self, ctx):
        channelInfoLogs = self.client.get_channel(728238632175009863)
        currentDT = DT.datetime.now()
        embedInf = discord.Embed(title='Infected Hunter', colour=discord.Colour(13400320), description=f"*From the diary we know this is a skilled\nhunter who used to hunt with Travis,\nbut now he's turned....*\n\nRecommended Troop Power **5,000**\n\n**Rewards:**\n<:TravisFragment:728344427977769021> 2-3\n<:1minGeneralSpeedup:728731148120752240> 10-20\n<:EpicHeroBadge:728344428099666030> 0-1\n<:Food:723743319389110312> 150,000\n<:Wood:723743319150297159> 150,000\n<:Metal:723743319221469184> 30,000\n<:Gas:723743319187914884> 7,500\n<:CombatBookI:723744670076633168> 8\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **2,700**\nInfected Troop amount: **750**\n\n**Infected Troop breakdown**", timestamp=currentDT)
        embedInf.set_thumbnail(url='https://i.imgur.com/0SMQ3Ap.gif')
        embedInf.set_image(url='https://i.imgur.com/mFGOg38.png')
        embedInf.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedInfLog = discord.Embed(title='Infected Hunter', colour=discord.Colour(13400320), description=f"*From the diary we know this is a skilled\nhunter who used to hunt with Travis,\nbut now he's turned....*\n\nRecommended Troop Power **5,000**\n\n**Rewards:**\n<:TravisFragment:728344427977769021> 2-3\n<:1minGeneralSpeedup:728731148120752240> 10-20\n<:EpicHeroBadge:728344428099666030> 0-1\n<:Food:723743319389110312> 150,000\n<:Wood:723743319150297159> 150,000\n<:Metal:723743319221469184> 30,000\n<:Gas:723743319187914884> 7,500\n<:CombatBookI:723744670076633168> 8\n\nStamina Cost: **25**\nTravis Stamina Cost: **20**\n\nInfected Battle Power: **2,700**\nInfected Troop amount: **750**\n\n**Infected Troop breakdown**\n\nExecution information:\nTime & Date: **{currentDT}**\nName: **{ctx.author}**\nServer Name: **{ctx.guild.name}**\nGuild ID: **{ctx.guild.id}**\nServer Owner: **{ctx.guild.owner}**\nMember Amount: **{ctx.guild.member_count}**\nServer Icon: [Icon]({ctx.guild.icon_url_as(format=None, size=64)})", timestamp=currentDT)
        embedInfLog.set_thumbnail(url='https://i.imgur.com/0SMQ3Ap.gif')
        embedInfLog.set_image(url='https://i.imgur.com/mFGOg38.png')
        embedInfLog.set_footer(text='Missing or wrong information?\nMissing or wrong rewards?\nSuggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await ctx.send(embed=embedInf)
        await channelInfoLogs.send(embed=embedInfLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')



##################################################################################################
#                                                                                                #
#             Everthing here below is information on the Resource Tiles.                         #
#                                                                                                #
##################################################################################################


    @info.command(aliases=['Food1', 'f1', 'F1', 'tomato1', 'Tomato1'])
    async def food1(self, ctx, arg: int=0):
        currentDT = DT.datetime.now()
        gatherSpeed = (316000)
        resource = (64300)
        gathertime = round((resource) / (gatherSpeed), 2)
        minutes = ((gathertime) * 60)
        hours, minutes = divmod(minutes, 60)
        t1 = round((resource) / 108)
        t1 = round((resource) / 108)
        t2 = round((resource) / 124)
        t3 = round((resource) / 142)
        t4 = round((resource) / 164)
        t5 = round((resource) / 188)
        t6 = round((resource) / 217)
        t7 = round((resource) / 249)
        t8 = round((resource) / 287)
        t9 = round((resource) / 330)
        t10 = round((resource) / 379)
        embedResource = discord.Embed(title='Abandoned Farm, Level 1', 
                                    colour=discord.Colour(8596012), 
                                    description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(hours,minutes)}** hours\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResource.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResource.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724817714467569695/image0.png')
        embedResource.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedResourceArg = discord.Embed(title='Abandoned Farm, Level 1', 
                                        colour=discord.Colour(8596012), 
                                        description=f'Amount of food in tile: **{resource:,}**\nYour gathering speed: **{gatherSpeed + arg:,}/h**\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResourceArg.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResourceArg.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724817714467569695/image0.png')
        embedResourceArg.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')
        if not arg:
            return await ctx.send(embed=embedResource)
               
        if arg != None:
            await ctx.send(embed=embedResourceArg)





    @info.command(aliases=['Food2', 'f2', 'F2', 'tomato2', 'Tomato2'])
    async def food2(self, ctx, arg: int=0):
        currentDT = DT.datetime.now()
        gatherSpeed = (332640)
        resource = (128750)
        gathertime = round((resource) / (gatherSpeed), 2)
        minutes = ((gathertime) * 60)
        hours, minutes = divmod(minutes, 60)
        t1 = round((resource) / 108)
        t2 = round((resource) / 124)
        t3 = round((resource) / 142)
        t4 = round((resource) / 164)
        t5 = round((resource) / 188)
        t6 = round((resource) / 217)
        t7 = round((resource) / 249)
        t8 = round((resource) / 287)
        t9 = round((resource) / 330)
        t10 = round((resource) / 379)
        embedResource = discord.Embed(title='Abandoned Farm, Level 2', 
                                    colour=discord.Colour(8596012), 
                                    description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(hours,minutes)}** hours\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResource.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResource.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828812658999347/image0.png')
        embedResource.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedResourceArg = discord.Embed(title='Abandoned Farm, Level 2', 
                                        colour=discord.Colour(8596012), 
                                        description=f'Amount of food in tile: **{resource:,}**\nYour gathering speed: **{gatherSpeed + arg:,}/h**\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResourceArg.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResourceArg.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828812658999347/image0.png')
        embedResourceArg.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')
        if not arg:
            return await ctx.send(embed=embedResource)
                
        if arg != None:
            await ctx.send(embed=embedResourceArg)



    @info.command(aliases=['Food3', 'f3', 'F3', 'tomato3', 'Tomato3'])
    async def food3(self, ctx, arg: int=0):
        currentDT = DT.datetime.now()
        gatherSpeed = (348480)
        resource = (269850)
        gathertime = round((resource) / (gatherSpeed), 2)
        minutes = ((gathertime) * 60)
        hours, minutes = divmod(minutes, 60)
        t1 = round((resource) / 108)
        t1 = round((resource) / 108)
        t2 = round((resource) / 124)
        t3 = round((resource) / 142)
        t4 = round((resource) / 164)
        t5 = round((resource) / 188)
        t6 = round((resource) / 217)
        t7 = round((resource) / 249)
        t8 = round((resource) / 287)
        t9 = round((resource) / 330)
        t10 = round((resource) / 379)
        embedResource = discord.Embed(title='Abandoned Farm, Level 3', 
                                    colour=discord.Colour(8596012), 
                                    description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(hours,minutes)}** hours\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResource.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResource.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828812906594404/image1.png')
        embedResource.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedResourceArg = discord.Embed(title='Abandoned Farm, Level 3', 
                                        colour=discord.Colour(8596012), 
                                        description=f'Amount of food in tile: **{resource:,}**\nYour gathering speed: **{gatherSpeed + arg:,}/h**\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResourceArg.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResourceArg.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828812906594404/image1.png')
        embedResourceArg.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')
        if not arg:
            return await ctx.send(embed=embedResource)
          
        if arg != None:
            await ctx.send(embed=embedResourceArg)



    @info.command(aliases=['Food4', 'f4', 'F4', 'tomato4', 'Tomato4'])
    async def food4(self, ctx, arg: int=0):
        currentDT = DT.datetime.now()
        gatherSpeed = (364320)
        resource = (577900)
        gathertime = round((resource) / (gatherSpeed), 2)
        minutes = ((gathertime) * 60)
        hours, minutes = divmod(minutes, 60)
        t1 = round((resource) / 108)
        t1 = round((resource) / 108)
        t2 = round((resource) / 124)
        t3 = round((resource) / 142)
        t4 = round((resource) / 164)
        t5 = round((resource) / 188)
        t6 = round((resource) / 217)
        t7 = round((resource) / 249)
        t8 = round((resource) / 287)
        t9 = round((resource) / 330)
        t10 = round((resource) / 379)
        embedResource = discord.Embed(title='Abandoned Farm, Level 4', 
                                    colour=discord.Colour(8596012), 
                                    description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(hours,minutes)}** hours\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResource.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResource.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828813262979152/image2.png')
        embedResource.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedResourceArg = discord.Embed(title='Abandoned Farm, Level 4', 
                                        colour=discord.Colour(8596012), 
                                        description=f'Amount of food in tile: **{resource:,}**\nYour gathering speed: **{gatherSpeed + arg:,}/h**\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResourceArg.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResourceArg.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828813262979152/image2.png')
        embedResourceArg.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')
        if not arg:
            return await ctx.send(embed=embedResource)
               
        if arg != None:
            await ctx.send(embed=embedResourceArg)



    @info.command(aliases=['Food5', 'f5', 'F5', 'tomato5', 'Tomato5'])
    async def food5(self, ctx, arg: int=0):
        currentDT = DT.datetime.now()
        gatherSpeed = (380160)
        resource = (1253100)
        gathertime = round((resource) / (gatherSpeed), 2)
        minutes = ((gathertime) * 60)
        hours, minutes = divmod(minutes, 60)
        t1 = round((resource) / 108)
        t1 = round((resource) / 108)
        t2 = round((resource) / 124)
        t3 = round((resource) / 142)
        t4 = round((resource) / 164)
        t5 = round((resource) / 188)
        t6 = round((resource) / 217)
        t7 = round((resource) / 249)
        t8 = round((resource) / 287)
        t9 = round((resource) / 330)
        t10 = round((resource) / 379)
        embedResource = discord.Embed(title='Abandoned Farm, Level 5', 
                                    colour=discord.Colour(8596012), 
                                    description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(hours,minutes)}** hours\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResource.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResource.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828813543997520/image3.png')
        embedResource.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedResourceArg = discord.Embed(title='Abandoned Farm, Level 5', 
                                        colour=discord.Colour(8596012), 
                                        description=f'Amount of food in tile: **{resource:,}**\nYour gathering speed: **{gatherSpeed + arg:,}/h**\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResourceArg.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResourceArg.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828813543997520/image3.png')
        embedResourceArg.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')
        if not arg:
            return await ctx.send(embed=embedResource)
               
        if arg != None:
            await ctx.send(embed=embedResourceArg)



    @info.command(aliases=['Food6', 'f6', 'F6', 'tomato6', 'Tomato6'])
    async def food6(self, ctx, arg: int=0):
        currentDT = DT.datetime.now()
        gatherSpeed = (396000)
        resource = (2731200)
        gathertime = round((resource) / (gatherSpeed), 2)
        minutes = ((gathertime) * 60)
        hours, minutes = divmod(minutes, 60)
        t1 = round((resource) / 108)
        t1 = round((resource) / 108)
        t2 = round((resource) / 124)
        t3 = round((resource) / 142)
        t4 = round((resource) / 164)
        t5 = round((resource) / 188)
        t6 = round((resource) / 217)
        t7 = round((resource) / 249)
        t8 = round((resource) / 287)
        t9 = round((resource) / 330)
        t10 = round((resource) / 379)
        embedResource = discord.Embed(title='Abandoned Farm, Level 6', 
                                    colour=discord.Colour(8596012), 
                                    description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(hours,minutes)}** hours\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResource.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResource.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828813829210156/image4.png')
        embedResource.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedResourceArg = discord.Embed(title='Abandoned Farm, Level 6', 
                                        colour=discord.Colour(8596012), 
                                        description=f'Amount of food in tile: **{resource:,}**\nYour gathering speed: **{gatherSpeed + arg:,}/h**\n\nLevel I troops needed: **{t1:,}**\nLevel II troops needed: **{t2:,}**\nLevel III troops needed: **{t3:,}**\nLevel IV troops needed: **{t4:,}**\nLevel V troops needed: **{t5:,}**\nLevel VI troops needed: **{t6:,}**\n Level VII troops needed: **{t7:,}**\nLevel VIII troops needed: **{t8:,}**\nLevel IX troops needed: **{t9:,}**\nLevel X troops needed: **{t10:,}**', timestamp=currentDT)

        embedResourceArg.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResourceArg.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828813829210156/image4.png')
        embedResourceArg.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')
        if not arg:
            return await ctx.send(embed=embedResource)
               
        if arg != None:
            await ctx.send(embed=embedResourceArg)



    @info.command(aliases=['Food7', 'f7', 'F7', 'tomato7', 'Tomato7'])
    async def food7(self, ctx, arg: int=0):
        currentDT = DT.datetime.now()
        gatherSpeed = (411840)
        resource = (5953250)
        gathertime = ((resource) / (gatherSpeed))
        minutes = ((gathertime) * 60)
        hours, minutes = divmod(minutes, 60)
        bonus = (gatherSpeed * (arg / 100.0))
        totaltime = (gatherSpeed * ((arg / 100.0) + 1.0))
        bonusgathertime = ((resource) / (totaltime))
        bonusminutes = ((bonusgathertime) * 60)
        bonushours, bonusminutes = divmod(bonusminutes, 60)
        t1 = round((resource) / 108)
        t1 = round((resource) / 108)
        t2 = round((resource) / 124)
        t3 = round((resource) / 142)
        t4 = round((resource) / 164)
        t5 = round((resource) / 188)
        t6 = round((resource) / 217)
        t7 = round((resource) / 249)
        t8 = round((resource) / 287)
        t9 = round((resource) / 330)
        t10 = round((resource) / 379)
        embedResource = discord.Embed(title='Abandoned Farm, Level 7', 
                                    colour=discord.Colour(8596012), 
                                    description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(hours, minutes)}** hours\n\nLevel `I` troops needed: **{t1:,}**\nLevel `II` troops needed: **{t2:,}**\nLevel `III` troops needed: **{t3:,}**\nLevel `IV` troops needed: **{t4:,}**\nLevel `V` troops needed: **{t5:,}**\nLevel `VI` troops needed: **{t6:,}**\n Level `VII` troops needed: **{t7:,}**\nLevel `VIII` troops needed: **{t8:,}**\nLevel `IX` troops needed: **{t9:,}**\nLevel `X` troops needed: **{t10:,}**', timestamp=currentDT)

        embedResource.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResource.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828814038925392/image5.png')
        embedResource.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedResourceArg = discord.Embed(title='Abandoned Farm, Level 7', 
                                        colour=discord.Colour(8596012), 
                                        description=f'Amount of food in tile: **{resource:,}**\nYour **{arg}%** bonus gathering speed: **{bonus:,}/h**\nYour total gathering speed: **{totaltime:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(bonushours, bonusminutes)}** hours\n\nLevel `I` troops needed: **{t1:,}**\nLevel `II` troops needed: **{t2:,}**\nLevel `III` troops needed: **{t3:,}**\nLevel `IV` troops needed: **{t4:,}**\nLevel `V` troops needed: **{t5:,}**\nLevel `VI` troops needed: **{t6:,}**\n Level `VII` troops needed: **{t7:,}**\nLevel `VIII` troops needed: **{t8:,}**\nLevel `IX` troops needed: **{t9:,}**\nLevel `X` troops needed: **{t10:,}**', timestamp=currentDT)

        embedResourceArg.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResourceArg.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828814038925392/image5.png')
        embedResourceArg.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')
        if not arg:
            return await ctx.send(embed=embedResource)
               
        if arg != None:
            await ctx.send(embed=embedResourceArg)



    @info.command(aliases=['Food8', 'f8', 'F8', 'tomato8', 'Tomato8'])
    async def food8(self, ctx, arg: int=0):
        currentDT = DT.datetime.now()
        gatherSpeed = (427680)
        resource = (13484450)
        gathertime = round((resource) / (gatherSpeed), 2)
        minutes = ((gathertime) * 60)
        hours, minutes = divmod(minutes, 60)

        t1 = round((resource) / 108)
        t1 = round((resource) / 108)
        t2 = round((resource) / 124)
        t3 = round((resource) / 142)
        t4 = round((resource) / 164)
        t5 = round((resource) / 188)
        t6 = round((resource) / 217)
        t7 = round((resource) / 249)
        t8 = round((resource) / 287)
        t9 = round((resource) / 330)
        t10 = round((resource) / 379)
        embedResource = discord.Embed(title='Abandoned Farm, Level 8', 
                                    colour=discord.Colour(8596012), 
                                    description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(hours,minutes)}**\n\nLevel `I` troops needed: **{t1:,}**\nLevel `II` troops needed: **{t2:,}**\nLevel `III` troops needed: **{t3:,}**\nLevel `IV` troops needed: **{t4:,}**\nLevel `V` troops needed: **{t5:,}**\nLevel `VI` troops needed: **{t6:,}**\n Level `VII` troops needed: **{t7:,}**\nLevel `VIII` troops needed: **{t8:,}**\nLevel `IX` troops needed: **{t9:,}**\nLevel `X` troops needed: **{t10:,}**', timestamp=currentDT)

        embedResource.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResource.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828814252965899/image6.png')
        embedResource.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedResourceArg = discord.Embed(title='Abandoned Farm, Level 8', 
                                        colour=discord.Colour(8596012), 
                                        description=f'Amount of food in tile: **{resource:,}**\nYour gathering speed: **{gatherSpeed * ((arg / 100.0) + 1.0):,}/h**\n\nLevel `I` troops needed: **{t1:,}**\nLevel `II` troops needed: **{t2:,}**\nLevel `III` troops needed: **{t3:,}**\nLevel `IV` troops needed: **{t4:,}**\nLevel `V` troops needed: **{t5:,}**\nLevel `VI` troops needed: **{t6:,}**\n Level `VII` troops needed: **{t7:,}**\nLevel `VIII` troops needed: **{t8:,}**\nLevel `IX` troops needed: **{t9:,}**\nLevel `X` troops needed: **{t10:,}**', timestamp=currentDT)

        embedResourceArg.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResourceArg.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828814252965899/image6.png')
        embedResourceArg.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')
        if not arg:
            return await ctx.send(embed=embedResource)
               
        if arg != None:
            await ctx.send(embed=embedResourceArg)














def setup(client):
    client.add_cog(Information(client))