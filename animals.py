import discord
from discord import app_commands
from discord.ext import commands
import random, json, urllib.request


# all cogs inherit from this base class
class animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # adding a bot attribute for easier access

    @commands.command(name="relran")
    async def relan(self, ctx):
        await self.bot.reload_extension("animals")
        await ctx.send("animals reloaded")

    @commands.command(name="cat")
    async def cat(self, ctx):
        url = "https://api.thecatapi.com/v1/images/search"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        data2 = data[0]
        result = data2["url"]
        await ctx.send(result)

    @commands.command(name="rva")
    async def rva(self, ctx):
        f = open('strings.json', )
        strings = json.load(f)
        va = strings["va"]
        amount = len(va)-1
        await ctx.send("Viewapp in a Nutshell")
        sel = random.randint(0,amount)
        await ctx.send(va[sel])




async def setup(bot):
    # finally, adding the cog to the bot
    await bot.add_cog(animals(bot=bot))