import random

import discord


token = ""
prefix = ";"
bot = discord.Client()

@bot.event
async def on_message(msg):
    channel = msg.channel
    author = msg.author
    msg = msg.content
    command, args = msg.split(" ")[0:]

    # if message is command, process command
    if msg.startswith(prefix):
        # ;say
        if msg.startswith(prefix + "say"):
            msg = msg.replace(prefix + "say ", "")

            await channel.send(msg)
        # ;iq
        elif msg.startswith(prefix + "iq"):
            iq = random.randint(-255, 255)
            append = ""

            if iq < -300:
                append = "**Big brain activated**"

            await channel.send(f"{author.mention} {iq} {append}")

@bot.event
async def on_ready():
    print("Test Bot\n")


bot.run(token)
