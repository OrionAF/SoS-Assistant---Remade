import discord
import os
from discord.ext import commands, tasks
import datetime
import asyncio
import random
import sqlite3


class ResourcesCog(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command(aliases=['f7', 'tomato7'])
    async def food7(self, ctx, arg: int=0):
        currentDT = datetime.datetime.now()
        gatherSpeed = (411840)
        resource = (5953250)
        gathertime = ((resource) / (gatherSpeed))
        minutes = ((gathertime) * 60)
        hours, minutes = divmod(minutes, 60)
        bonus = (gatherSpeed * (arg / 100.0))
        totaltime = (gatherSpeed + bonus)
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
                                    description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(hours, minutes)}**\n\nLevel `I` troops needed: **{t1:,}**\nLevel `II` troops needed: **{t2:,}**\nLevel `III` troops needed: **{t3:,}**\nLevel `IV` troops needed: **{t4:,}**\nLevel `V` troops needed: **{t5:,}**\nLevel `VI` troops needed: **{t6:,}**\n Level `VII` troops needed: **{t7:,}**\nLevel `VIII` troops needed: **{t8:,}**\nLevel `IX` troops needed: **{t9:,}**\nLevel `X` troops needed: **{t10:,}**', timestamp=currentDT)

        embedResource.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResource.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828814038925392/image5.png')
        embedResource.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')

        embedResourceArg = discord.Embed(title='Abandoned Farm, Level 7', 
                                        colour=discord.Colour(8596012), 
                                        description=f'Amount of food in tile: **{resource:,}**\nDefault gathering speed: **{gatherSpeed:,}/h**\nYour **{arg}%** bonus gathering speed: **{bonus:,}/h**\nYour total gathering speed: **{totaltime:,}/h**\nTime needed to deplete resource: **{"%02d hours and %02d minutes"%(bonushours, bonusminutes)}** hours\n\nLevel `I` troops needed: **{t1:,}**\nLevel `II` troops needed: **{t2:,}**\nLevel `III` troops needed: **{t3:,}**\nLevel `IV` troops needed: **{t4:,}**\nLevel `V` troops needed: **{t5:,}**\nLevel `VI` troops needed: **{t6:,}**\n Level `VII` troops needed: **{t7:,}**\nLevel `VIII` troops needed: **{t8:,}**\nLevel `IX` troops needed: **{t9:,}**\nLevel `X` troops needed: **{t10:,}**', timestamp=currentDT)

        embedResourceArg.set_thumbnail(url='https://cdn.discordapp.com/emojis/723743319389110312.png?v=1')
        embedResourceArg.set_image(url='https://cdn.discordapp.com/attachments/713050313791242322/724828814038925392/image5.png')
        embedResourceArg.set_footer(text='Missing or wrong information?  Suggestions or requests regarding the bot?\nMessage OrionAF#6982\n\n')
        if not arg:
            return await ctx.send(embed=embedResource)
        
        if arg != None:
            await ctx.send(embed=embedResourceArg)















def setup(client):
    client.add_cog(ResourcesCog(client))