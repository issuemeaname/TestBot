import discord
from discord.ext import commands

from bot.token import TOKEN


COMMAND_PREFIX = ";"


class TestBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f"{self.user.name} is now up!")


bot = TestBot(command_prefix=COMMAND_PREFIX)


@bot.command()
async def test(ctx):
    embed = discord.Embed(title="Status", description="Working!")

    await ctx.send(embed=embed)


@bot.command()
async def exit(ctx):
    embed = discord.Embed(title="Status", description="Shutting down...")

    await ctx.send(embed=embed)
    await bot.close()


if __name__ == "__main__":
    bot.run(TOKEN, reconnect=True)
