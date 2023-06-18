import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def generate_password(ctx, pass_length: int):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for _ in range(pass_length):
        password += random.choice(elements)

    await ctx.send(f"Generated password: {password}")

bot.run(token)
