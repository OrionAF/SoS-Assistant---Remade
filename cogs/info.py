import discord
from discord import Embed, Emoji 
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class InfoCog(commands.Cog, name='InfoCog'):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def credits(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)
        
        embedCredits = discord.Embed(title='Credits', colour=discord.Colour(29952), description=f"The following people have helped in one way or another with the creation of this bot, the information or support.  Without them, this bot would never exist.\n\n**Dapo-190** | *dapo#7586*\n**ViciousImp-190** | *ViciousImp#7789*\n**Burn-190** | *Cal#2361*\n**I am Grööt!-190** | *Tomyumgoong#2340*\n**Argh-35** | *S.35-Argh#7578*\n**Cold Bodies-30** | *Cold Bodies#1181*\n\nAnd everyone else who send me screenshots of any kind of information.\n\n\n**These websites helped greatly as well, saving me time from doing the same work that they have allready done.**\n\n[SoS Facebook Page](https://www.facebook.com/TheSoSGame)\n[SOS-FR Sheet](https://docs.google.com/spreadsheets/d/1MuJqDEw-jiLuHFPlgoDbQxqUk4e2KIHKV4VU8MfPQXo/edit#gid=1421382497)\n[SoS Ultimate Guide EN](https://en.ultimate-guide.ovh/)\n[SoS Ultimate Guide FR](https://fr.ultimate-guide.ovh/accueil)\n[Teddy Plays - State of Survival Guide](http://www.savagery-gaming.com/)\n[ZE Gaming](https://zegaming.club/)\n[SoS-Companion](http://soscompanion.com/)\n\n\n**These Discord servers helped a lot in the creation of this bot.  Thank you for withstanding all my stupid questions.**\n\n[discord.py](https://discord.gg/dpy)\n[Python](https://discord.gg/python)\n[Code Ring](https://discord.gg/CyPd9rh)\n[Discord API](https://discord.gg/discord-api)\n\n\n**And at last I would like to thank the developers of this game for giving me permission to use theyr content, all from Facebook artwork to ingame screenshots and for putting in the hard work of developing this game.**\n\n\n*Special thanks to the members of **DLX** for theyr patience with me while I was working on the bot and for sticking with me through it all.  I'd also like to thank the mods in the [State of Survival](https://discord.gg/nycXFA7) Discord server for all of theyr hard work and patience, as well as the whole SoS community.*")
        embedCredits.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedCredits.timestamp = datetime.datetime.utcnow()

        embedCreditsLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedCreditsLog.set_author(name=f'Credits', icon_url=f'{ctx.author.avatar_url}')
        embedCreditsLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedCreditsLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedCredits)
        await channelInfoLogs.send(embed=embedCreditsLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    
    @commands.group(case_insensitive=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            currentDT = datetime.datetime.now()
            channelInfoLogs = self.client.get_channel(728238632175009863)

            embedHelp = discord.Embed(title='Help!', colour=discord.Colour(29952), description=f"Hello.  I am your **SoS Assistant**.  I have gathered some useful information for you, so you don't have to.  Here below you will find all command categories.  To access each help category for each command, just write out the category name after ``!help``.  For example: ``!help Infected``.")
            embedHelp.add_field(name='​', value='__**Heroes**__\nThe **Heroes** category will show you information about all heroes currently in the game right now.  I currently show you stats for heroes that are freshly unlocked, and completely maxed.\n\n__**Infected**__\nThe **Infected** category will show you all Infected levels exact troop power, troop amounts, rewards and more.\n\n__**Fiends**__\n**The Infected Fiends** category will show you all Fiends levels, including the Hunters, showing you exact troop numbers, troop amounts, rewards and more.\n\n__**Aliases**__\nMost commands have an alias command.  They were added incase a common typo was made, shorter command names, different preffered commands or just for the giggles.  In this catergory I will list all commands that have an alias.\n\n__**Misc**__\nSome random, fun commands.')
            embedHelp.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
            embedHelp.timestamp = datetime.datetime.utcnow()

            embedHelpLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
            embedHelpLog.set_author(name=f'Help!', icon_url=f'{ctx.author.avatar_url}')
            embedHelpLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
            embedHelpLog.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embedHelp)
            await channelInfoLogs.send(embed=embedHelpLog)
            await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


    @help.group()
    async def heroes(self, ctx):
        if ctx.invoked_subcommand is None:
            currentDT = datetime.datetime.now()
            channelInfoLogs = self.client.get_channel(728238632175009863)

            embedHeroes = discord.Embed(title='Help | Heroes Page 1/3 | ```!help heroes 1/2/3``` to switch pages.', colour=discord.Colour(29952), description=f'All commands here are **Hero** related.  The list is sorted alphabetically.\nEach hero command has a subcommand, but they can all be used without one.  Try it!\nYou can not pass all subcommands at a time, you can only do one subcommand at a time.')
            embedHeroes.add_field(name='​', value=f'```diff\n!Ash``` ```short - military - explorer```\n```diff\n!Basel``` ```short - military - explorer```\n```diff\n!Candy``` ```short - military - explorer```\n```diff\n!Chef``` ```short - military - explorer```\n```diff\n!Ernie``` ```short - military - explorer```\n```diff\n!Eva``` ```short - military - explorer```', inline=True)
            embedHeroes.add_field(name='​', value=f'```diff\n!Ghost``` ```short - military - explorer```\n```diff\n!Jane``` ```short - military - explorer```\n```diff\n!Jarrett``` ```short - military - explorer```\n```diff\n!Jeb``` ```short - military - explorer```\n```diff\n!Lucky``` ```short - military - explorer```\n```diff\n!Maddie``` ```short - military - explorer```', inline=True)
            embedHeroes.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
            embedHeroes.timestamp = datetime.datetime.utcnow()

            embedHeroesLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
            embedHeroesLog.set_author(name=f'Heroes Help 1/3', icon_url=f'{ctx.author.avatar_url}')
            embedHeroesLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
            embedHeroesLog.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embedHeroes)
            await channelInfoLogs.send(embed=embedHeroesLog)
            await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @heroes.command(name='2')
    async def heroes2(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedHeroes = discord.Embed(title='Help | Heroes Page 2/3 | ```!help heroes 1/2/3``` to switch pages.', colour=discord.Colour(29952), description=f'All commands here are **Hero** related.  The list is sorted alphabetically.\nEach hero command has a subcommand, but they can all be used without one.  Try it!\nYou can not pass all subcommands at a time, you can only do one subcommand at a time.')
        embedHeroes.add_field(name='​', value=f'```diff\n!Miho``` ```short - military - explorer```\n```diff\n!Mike``` ```short - military - explorer```\n```diff\n!Nikola``` ```short - military - explorer```\n```diff\n!Ray``` ```short - military - explorer```\n```diff\n!Rusty``` ```short - military - explorer```\n```diff\n!Sarge``` ```short - military - explorer```')
        embedHeroes.add_field(name='​', value=f'```diff\n!Tony``` ```short - military - explorer```\n```diff\n!Travis``` ```short - military - explorer```\n```diff\n!Trish``` ```short - military - explorer```\n```diff\n!Wolfe``` ```short - military - explorer```\n```diff\n!Zach``` ```short - military - explorer```\n```diff\n!Zoe``` ```short - military - explorer```')
        embedHeroes.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedHeroes.timestamp = datetime.datetime.utcnow()

        embedHeroesLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedHeroesLog.set_author(name=f'Heroes Help 2/3', icon_url=f'{ctx.author.avatar_url}')
        embedHeroesLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedHeroesLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedHeroes)
        await channelInfoLogs.send(embed=embedHeroesLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @heroes.command(name='3')
    async def heroes3(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedHeroes = discord.Embed(title='Help | Heroes Page 3/3 | ```!help heroes 1/2/3``` to switch pages.', colour=discord.Colour(29952), description=f'All commands here are **Hero** related.  These commands are hero specialization commands.  The main command is ``!spec`` followed by a specialization.  Try it!\nYou can not pass all subcommands at a time, you can only do one subcommand at a time.')
        embedHeroes.add_field(name='​', value=f'```diff\n!Spec``` ```Gathering - Infected - Patrol - Siege - Rally```')
        embedHeroes.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedHeroes.timestamp = datetime.datetime.utcnow()

        embedHeroesLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedHeroesLog.set_author(name=f'Heroes Help 3/3')
        embedHeroesLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedHeroesLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedHeroes)
        await channelInfoLogs.send(embed=embedHeroesLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @help.group()
    async def infected(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedInfected = discord.Embed(title='Help | Infected', colour=discord.Colour(29952), description=f'The Infected commands allow you to view detailed information about each level Infected, including, but not limited to: Infected recommended troop power, Infected actual troop power, troop amount, rewards and more.')
        embedInfected.add_field(name='​', value=f'```diff\n!ilvl1``` Shows information about Infected level 1.  You can replace ``1`` with any number between 1-30 and you will get their information.')
        embedInfected.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedInfected.timestamp = datetime.datetime.utcnow()

        embedInfectedLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedInfectedLog.set_author(name=f'Infected Help', icon_url=f'{ctx.author.avatar_url}')
        embedInfectedLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedInfectedLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedInfected)
        await channelInfoLogs.send(embed=embedInfectedLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @help.group(aliases=['fiend'])
    async def fiends(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedFiends = discord.Embed(title='Help | Infected Fiends/Infected Hunters', colour=discord.Colour(29952), description=f"The Fiend commands allow you to view detailed information about each Infected Fiend's level, including, but not limited to: Fiend recommended troop power, Fiend actual troop power, troop amount, rewards and more.")
        embedFiends.add_field(name='​', value=f'```diff\n!flvl1``` Shows information about Infected Fiend level 1.  You can replace ``1`` with any number between 1-5 and you will get their information.\n```diff\n!normal``` Shows information about Infected Hunter.\n```diff\n!elite``` Shows information about Elite Infected Hunter.')
        embedFiends.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedFiends.timestamp = datetime.datetime.utcnow()

        embedFiendsLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedFiendsLog.set_author(name=f'Infected Fiend Help')
        embedFiendsLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedFiendsLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedFiends)
        await channelInfoLogs.send(embed=embedFiendsLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @help.group(aliases=['alias'])
    async def aliases(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedAlias = discord.Embed(title='Help | Alias Commands', colour=discord.Colour(29952), description=f'Here below you will find all commands that have an alias, including all alias commands for that specific command.  The main command will be on the left side, bold and underlined, while the aliases will be in a codeblock, seperated with ``-`` if they have multiple aliases.')
        embedAlias.add_field(name='​', value=f'__**!help aliases**__ ``alias``\n\n**Hero Subcommands**\n__**military**__ ``army``\n__**explorer**__ ``explore`` - ``exploring``\n__**short**__ ``shorten`` - ``shorter``\n\n**Hero Aliases**\n__**!maddie**__ ``frank`` - ``maddie&frank`` - ``maddieandfrank``\n__**!ray**__ ``rolex`` - ``ray&rolex`` - ``rayandrolex``\n\n**Specialization**\n__**!spec**__ ``specialization`` - ``specs``\n\n**Infected**\n__**!ilvl1**__ ``i1``\n*P.S. Same for all the other levels*\n\n**Infected Fiends**\n__**!flvl1**__ ``iflvl1`` - ``if1`` - ``f1`` - ``fiendlvl1`` - ``flv1`` - ``iflv1`` - ``fiendlv1``\n*P.S. Same for all the other levels*\n\n**Miscellaneous**\n__**!infantry**__ ``inf`` - ``noinf`` - ``noinfantry``\n__**!version**__ ``v`` - ``ver``')
        embedAlias.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedAlias.timestamp = datetime.datetime.utcnow()

        embedAliasLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedAliasLog.set_author(name=f'Aliases Help', icon_url=f'{ctx.author.avatar_url}')
        embedAliasLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedAliasLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedAlias)
        await channelInfoLogs.send(embed=embedAliasLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @help.group()
    async def misc(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedMisc = discord.Embed(title='Help | Misc Commands', colour=discord.Colour(29952), description=f'Here below you will find all miscellaneous commands.  The "fun" commands.')
        embedMisc.add_field(name='​', value=f'```diff\n!horde```\n```diff\n!infantry```\n```diff\n!version```\n```diff\n!feedback```\n```diff\n!meme```')
        embedMisc.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedMisc.timestamp = datetime.datetime.utcnow()

        embedMiscLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedMiscLog.set_author(name=f'Miscellaneous Help', icon_url=f'{ctx.author.avatar_url}')
        embedMiscLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedMiscLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedMisc)
        await channelInfoLogs.send(embed=embedMiscLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @commands.command(aliases=['v', 'ver'])
    async def version(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedVersionLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedVersionLog.set_author(name=f'Version', icon_url=f'{ctx.author.avatar_url}')
        embedVersionLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedVersionLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(f'I am version number: Alpha 1.3.0')

        await channelInfoLogs.send(embed=embedVersionLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')



    @commands.group()
    async def sotf(self, ctx):
        if ctx.invoked_subcommand is None:
            currentDT = datetime.datetime.now()
            channelInfoLogs = self.client.get_channel(728238632175009863)

            embedSOTF = discord.Embed(colour=discord.Colour(29952), description=f'To view the different stages of Survival of the Fittest your state may have, you need to check ingame what hero is being represented for SOTF.\n\nCurrently there are;\n**Nikola** *Three different events*\n**Wolfe** *Two different events*\n**Zoe** *Three different events*\n**Jarret** *One event*\n\nTo view the different events for each hero, add a number after the hero name in the command.\n__**Example:**__ ``!sotf nikola 2``')
            embedSOTF.set_author(name=f'Survival of the Fittest')
            embedSOTF.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
            embedSOTF.set_footer(text=f'Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
            embedSOTF.timestamp = datetime.datetime.utcnow()

            embedSOTFLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
            embedSOTFLog.set_author(name=f'SOTF Blank', icon_url=f'{ctx.author.avatar_url}')
            embedSOTFLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
            embedSOTFLog.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embedSOTF)

            await channelInfoLogs.send(embed=embedSOTFLog)
            await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


    @sotf.group()
    async def nikola(self, ctx):
        if ctx.invoked_subcommand is None:
            currentDT = datetime.datetime.now()
            channelInfoLogs = self.client.get_channel(728238632175009863)

            embedNikola = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
            embedNikola.set_author(name=f'Survival of the Fittest - Nikola v1\nWeek 1-3')
            embedNikola.set_image(url='https://i.imgur.com/mnkcDon.png')
            embedNikola.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
            embedNikola.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
            embedNikola.timestamp = datetime.datetime.utcnow()

            embedNikolaLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
            embedNikolaLog.set_author(name='SOTF Nikola First Image', icon_url=f'{ctx.author.avatar_url}')
            embedNikolaLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
            embedNikolaLog.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embedNikola)

            await channelInfoLogs.send(embed=embedNikolaLog)
            await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @nikola.command(name='2')
    async def nikola2(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedNikola = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
        embedNikola.set_author(name=f'Survival of the Fittest - Nikola v2\nWeek 4-5')
        embedNikola.set_image(url='https://i.imgur.com/zPKNOib.png')
        embedNikola.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
        embedNikola.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedNikola.timestamp = datetime.datetime.utcnow()

        embedNikolaLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedNikolaLog.set_author(name='SOTF Nikola Second Image', icon_url=f'{ctx.author.avatar_url}')
        embedNikolaLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedNikolaLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedNikola)

        await channelInfoLogs.send(embed=embedNikolaLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @nikola.command(name='3')
    async def nikola3(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedNikola = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
        embedNikola.set_author(name=f'Survival of the Fittest - Nikola v3\nWeek 6-7')
        embedNikola.set_image(url='https://i.imgur.com/1EWeTfq.png')
        embedNikola.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
        embedNikola.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedNikola.timestamp = datetime.datetime.utcnow()

        embedNikolaLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedNikolaLog.set_author(name='SOTF Nikola Third Image', icon_url=f'{ctx.author.avatar_url}')
        embedNikolaLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedNikolaLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedNikola)

        await channelInfoLogs.send(embed=embedNikolaLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')


    @sotf.group()
    async def wolfe(self, ctx):
        if ctx.invoked_subcommand is None:
            currentDT = datetime.datetime.now()
            channelInfoLogs = self.client.get_channel(728238632175009863)

            embedWolfe = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
            embedWolfe.set_author(name=f'Survival of the Fittest - Wolfe v1\nWeek 8-11')
            embedWolfe.set_image(url='https://i.imgur.com/KAfWICU.png')
            embedWolfe.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
            embedWolfe.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
            embedWolfe.timestamp = datetime.datetime.utcnow()

            embedWolfeLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
            embedWolfeLog.set_author(name='SOTF Wolfe First Image', icon_url=f'{ctx.author.avatar_url}')
            embedWolfeLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
            embedWolfeLog.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embedWolfe)

            await channelInfoLogs.send(embed=embedWolfeLog)
            await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    
    @wolfe.command(name='2')
    async def wolfe2(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedWolfe = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
        embedWolfe.set_author(name=f'Survival of the Fittest - Wolfe v2\nWeek 12-13')
        embedWolfe.set_image(url='https://i.imgur.com/vqpC4F5.png')
        embedWolfe.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
        embedWolfe.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedWolfe.timestamp = datetime.datetime.utcnow()

        embedWolfeLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedWolfeLog.set_author(name='SOTF Wolfe Second Image', icon_url=f'{ctx.author.avatar_url}')
        embedWolfeLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedWolfeLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedWolfe)

        await channelInfoLogs.send(embed=embedWolfeLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @sotf.group()
    async def zoe(self, ctx):
        if ctx.invoked_subcommand is None:
            currentDT = datetime.datetime.now()
            channelInfoLogs = self.client.get_channel(728238632175009863)

            embedZoe = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
            embedZoe.set_author(name=f'Survival of the Fittest - Zoe v1\nWeek 14-15')
            embedZoe.set_image(url='https://i.imgur.com/KrqXw3p.png')
            embedZoe.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
            embedZoe.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
            embedZoe.timestamp = datetime.datetime.utcnow()

            embedZoeLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
            embedZoeLog.set_author(name='SOTF Zoe First Image', icon_url=f'{ctx.author.avatar_url}')
            embedZoeLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
            embedZoeLog.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embedZoe)

            await channelInfoLogs.send(embed=embedZoeLog)
            await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @zoe.command(name='2')
    async def zoe2(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedZoe = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
        embedZoe.set_author(name=f'Survival of the Fittest - Zoe v2\nWeek 16-19')
        embedZoe.set_image(url='https://i.imgur.com/fhu50nJ.png')
        embedZoe.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
        embedZoe.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedZoe.timestamp = datetime.datetime.utcnow()

        embedZoeLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedZoeLog.set_author(name='SOTF Zoe Second Image', icon_url=f'{ctx.author.avatar_url}')
        embedZoeLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedZoeLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedZoe)

        await channelInfoLogs.send(embed=embedZoeLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @zoe.command(name='3')
    async def zoe3(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedZoe = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
        embedZoe.set_author(name=f'Survival of the Fittest - Zoe v3\nWeek 20-23')
        embedZoe.set_image(url='https://i.imgur.com/IdqMBF7.png')
        embedZoe.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
        embedZoe.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedZoe.timestamp = datetime.datetime.utcnow()

        embedZoeLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedZoeLog.set_author(name='SOTF Zoe Third Image', icon_url=f'{ctx.author.avatar_url}')
        embedZoeLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedZoeLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedZoe)

        await channelInfoLogs.send(embed=embedZoeLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    
    @sotf.group()
    async def jarrett(self, ctx):
        if ctx.invoked_subcommand is None:
            currentDT = datetime.datetime.now()
            channelInfoLogs = self.client.get_channel(728238632175009863)

            embedJarrett = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
            embedJarrett.set_author(name=f'Survival of the Fittest - Jarrett v1\nWeek 24+')
            embedJarrett.set_image(url='https://i.imgur.com/84tw5ow.png')
            embedJarrett.set_thumbnail(url='https://i.imgur.com/jxrEh9l.png')
            embedJarrett.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
            embedJarrett.timestamp = datetime.datetime.utcnow()

            embedJarrettLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
            embedJarrettLog.set_author(name='SOTF Jarrett First Image', icon_url=f'{ctx.author.avatar_url}')
            embedJarrettLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
            embedJarrettLog.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embedJarrett)

            await channelInfoLogs.send(embed=embedJarrettLog)
            await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @commands.group()
    async def plasma(self, ctx):
        if ctx.invoked_subcommand is None:
            currentDT = datetime.datetime.now()
            channelInfoLogs = self.client.get_channel(728238632175009863)

            embedPlasma = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
            embedPlasma.set_author(name=f'Plasma cost for all buildings.  For detailed information per upgrade: !plasma detailed')
            embedPlasma.set_image(url='https://i.imgur.com/INfIPkV.pngg')
            embedPlasma.set_thumbnail(url='https://i.imgur.com/C6WHmHG.png')
            embedPlasma.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
            embedPlasma.timestamp = datetime.datetime.utcnow()

            embedPlasmaLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
            embedPlasmaLog.set_author(name='Plasma Simple', icon_url=f'{ctx.author.avatar_url}')
            embedPlasmaLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
            embedPlasmaLog.timestamp = datetime.datetime.utcnow()

            await ctx.send(embed=embedPlasma)

            await channelInfoLogs.send(embed=embedPlasmaLog)
            await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @plasma.command(aliases=['detail', 'details'])
    async def detailed(self, ctx):
        currentDT = datetime.datetime.now()
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedPlasma = discord.Embed(colour=discord.Colour(29952), description=f"Click/Tap on the image if it's to small.")
        embedPlasma.set_author(name=f'Detailed plasma information per upgrade')
        embedPlasma.set_image(url='https://i.imgur.com/Y5Whx33.png')
        embedPlasma.set_thumbnail(url='https://i.imgur.com/C6WHmHG.png')
        embedPlasma.set_footer(text='Missing or wrong information? \nMissing or wrong rewards? \nSuggestions or requests regarding the bot? \nMessage OrionAF#6982')
        embedPlasma.timestamp = datetime.datetime.utcnow()

        embedPlasmaLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedPlasmaLog.set_author(name='Plasma Detailed', icon_url=f'{ctx.author.avatar_url}')
        embedPlasmaLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')
        embedPlasmaLog.timestamp = datetime.datetime.utcnow()

        await ctx.send(embed=embedPlasma)

        await channelInfoLogs.send(embed=embedPlasmaLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

    @commands.command()
    async def feedback(self, ctx, *, feedback):
        currentDT = datetime.datetime.now()
        channelBotFeedback = self.client.get_channel(744966399092588664)
        channelInfoLogs = self.client.get_channel(728238632175009863)

        embedFeedback = discord.Embed(colour=discord.Colour(16302848), description=f'```Feedback Author: {ctx.author}\nTime & date: {currentDT}\nServer Name: {ctx.guild.name}\nMember Amount: {ctx.guild.member_count}```\n\nFeedback:\n{feedback}')
        embedFeedback.set_author(name=f"{ctx.author}'s feedback.", icon_url=f'{ctx.author.avatar_url}')
        embedFeedback.timestamp = datetime.datetime.utcnow()

        embedFeedbackLog = discord.Embed(colour=discord.Colour(29952), description=f'```Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
        embedFeedbackLog.set_author(name='Plasma Detailed', icon_url=f'{ctx.author.avatar_url}')
        embedFeedbackLog.set_footer(text=f'Info Logs', icon_url=f'{ctx.guild.icon_url_as(format=None)}')

        await channelBotFeedback.send(embed=embedFeedback)
        await channelBotFeedback.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')
        await channelInfoLogs.send(embed=embedFeedbackLog)
        await channelInfoLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')
        await ctx.send(f'Thank you for sharing your feedback {ctx.author}.  I have made my creator aware.')

    @feedback.error
    async def feedback_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            channelErrorLogs = self.client.get_channel(726006713618268250)
            currentDT = datetime.datetime.now()

            embedError = discord.Embed(colour=discord.Colour(13632027), description=f'To properly use this command, you need to provide some feedback after the command.  Example; ``!feedback I love this bot, and I use it all the time.``')
            embedError.set_author(name="Feedback Error!", icon_url="https://i.imgur.com/ty7SEua.png")

            embedErrorLog = discord.Embed(colour=discord.Colour(13632027), description=f'Execution information:\nTime & Date: {currentDT}\nName: {ctx.author}\nServer Name: {ctx.guild.name}\nGuild ID: {ctx.guild.id}\nServer Owner: {ctx.guild.owner}\nMember Amount: {ctx.guild.member_count}\nServer Icon:``` [Icon]({ctx.guild.icon_url_as(format=None, size=64)})')
            embedErrorLog.set_author(name="Feedback Error!", icon_url="https://i.imgur.com/ty7SEua.png")
        
            await ctx.send(embed=embedError)
            await channelErrorLogs.send(embed=embedErrorLog)
            await channelErrorLogs.send(f'◆↓◆↓◆↓◆↓◆↓◆↓◆')

        
    @commands.command(pass_context=True)
    async def debug(self, ctx, emoji: Emoji):
        embed = discord.Embed(title=f"{emoji}")
        embed.add_field(name="ID", value=repr(emoji.id))
        embed.add_field(name="Name", value=repr(emoji.name))
        await ctx.send(embed=embed)
    
    @commands.command()
    async def invite(self, ctx):
        await ctx.send(f'Here is an invite link if you would like to invite me to your server\nhttps://discord.com/api/oauth2/authorize?client_id=726002163368853583&permissions=452672&scope=bot')

    @commands.command()
    async def emojitest(self, ctx):
        emoji1 = self.client.get_emoji(745427268469391466)
        emoji2 = self.client.get_emoji(745427268519592012)
        emoji3 = self.client.get_emoji(745427269031297034)
        emoji4 = self.client.get_emoji(745427268645552160)
        emoji5 = self.client.get_emoji(745427268846747668)
        emoji6 = self.client.get_emoji(745427268825776260)
        emoji7 = self.client.get_emoji(745427268658135122)
        emoji8 = self.client.get_emoji(745427268725112975)
        emoji9 = self.client.get_emoji(745427268951605311)
        emoji10 = self.client.get_emoji(745427268633100373)
        emoji11 = self.client.get_emoji(745427268775444548)
        emoji12 = self.client.get_emoji(745427268913856613)
        emoji13 = self.client.get_emoji(745427269027102773)
        emoji14 = self.client.get_emoji(745427269115445368)
        emoji15 = self.client.get_emoji(745427268893147187)

        await ctx.send(f'{emoji1}{emoji2}{emoji3}{emoji4}{emoji5}\n{emoji6}{emoji7}{emoji8}{emoji9}{emoji10}\n{emoji11}{emoji12}{emoji13}{emoji14}{emoji15}')



    @commands.command()
    async def travistest(self, ctx):
        heroes = self.client.get_cog('HeroesCog')
        HeroData1 = await heroes.rally(self, ctx)

        await ctx.send(embed=HeroData1)



def setup(client):
    client.add_cog(InfoCog(client))