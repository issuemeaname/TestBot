import random

import discord
from discord.ext import commands


token = ""
prefix = ";"
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)

# completely removes the idea of the "on_message" event and instead allows for
# dynamic command creation and easier argument implementation
@bot.event
async def on_ready():
    print("Test Bot\n")

# ;say
@bot.command()
async def say(ctx, message):
    await ctx.send(message)

# ;iq
@bot.command()
async def iq(ctx):
    iq = random.randint(-255, 255)
    append = ""

    if iq < -100:
        append = "**Big brain activated**"

    await ctx.send(f"{ctx.author.mention} {iq} {append}")


bot.run(token)
