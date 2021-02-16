import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "!")

# Load
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print('Cog Loaded.')

# Unload
@client.command()
async def unload(ctx, extension):
   client.unload_extension(f'cogs.{extension}')
   print('Cog Unloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        

client.run('key here')