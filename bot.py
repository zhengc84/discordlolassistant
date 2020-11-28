import discord
from discord.ext import commands, tasks
import os 

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print('ready to go')


for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')



bot.run('NzY0NTMyNjc3MjE0MzM5MDky.X4Hoig.57U4_ERLlbJbBjEyNI8Ae1e3C_4')