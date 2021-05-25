import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure
import os
import asyncio
import random
from web_server import web_server

client = commands.Bot(command_prefix='--') #Colocação de prefixo

web_server()
client.run(os.getenv('TOKEN'))