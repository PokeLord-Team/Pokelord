import asyncio
import os
import traceback
from pathlib import Path
from random import randint
from secrets import TOKEN
import discord
from discord.ext import commands
from discord import Member, channel, message
from discord.ext.commands import has_permissions, MissingPermissions, Bot, has_guild_permissions
import json
intents = discord.Intents.default()
intents.members = True 
def get_prefix(bot, message):
    with open('cogs/prefixes/prefixes.json', 'r') as f:
        data = json.load(f)
    if not str(message.channel.id) in data:
        return commands.when_mentioned_or('e!', 'E!')(bot, message)
    return commands.when_mentioned_or(data[str(message.guild.id)])(bot, message)


bot2: Bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, owners_id=393480172638044160, intents=intents)
bot2.remove_command('help') 

ext = ['cogs.config', 'cogs.game', 'cogs.fun', 'cogs.other', 'cogs.help', 'cogs.mod'] # basic python
if __name__ == '__main__':
  bot2.color=0x808080
  for extension in ext:
    bot2.load_extension(extension) 

#https://www.youtube.com/watch?v=uXn-zOt68V8
 
bot2.run(TOKEN)
