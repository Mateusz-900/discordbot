import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_message_edit(before, after):
    await after.channel.send(f"wiadomość została edytowana z: {before.content}")
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
bot.run("MTU1MjczNTM0MzgwNjI1NTEwNA.GA2dCN.dT2cM1f2r7v1B_TQ0OvImVW6fW-2Os00oHonVQ")
