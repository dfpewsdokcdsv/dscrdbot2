import discord
import random
import bot_logic
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

import discord
from discord.ext import commands
import bot_logic

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Бот готов')

@bot.command()
async def genpass(ctx, pass_length: int):
    password = bot_logic.generate_password(pass_length)
    await ctx.send(f'Сгенерированный пароль: {password}')


bot.run('token')
