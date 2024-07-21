import discord
from discord import app_commands
from discord.ext import commands
import random, json, urllib.request


# all cogs inherit from this base class
class others(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # adding a bot attribute for easier access

    @commands.command(name="relothers")
    async def relothers(self, ctx):
        await self.bot.reload_extension("others")
        await ctx.send("others reloaded")


    @commands.command(name="dice")
    async def dice(self, ctx, args):
        try:
            rolls, limit = map(int, args.split("d"))
        except Exception:
            await ctx.send("Format is NdN")
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command(name="insult")
    async def insult(self, ctx):
        if not ctx.message.mentions:
            target = ctx.message.author
        else:
            target = ctx.message.mentions[0]
        url = "https://insult.mattbas.org/api/insult.json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        print(target)
        result = target.mention + ", " + data["insult"]
        await ctx.send(result)

    # Magnum Opus, THROWING RANDOM SHIT
    @commands.command(name="throw")
    async def throw(self, ctx):
        f = open('ammo.json', )
        ammo = json.load(f)





async def setup(bot):
    # finally, adding the cog to the bot
    await bot.add_cog(others(bot=bot))