import discord
from discord import app_commands
from discord.ext import commands
import urllib.request, json


# all cogs inherit from this base class
class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # adding a bot attribute for easier access

    @commands.command(name="relinfo")
    async def relinfo(self, ctx):
        await self.bot.reload_extension("info")
        await ctx.send("info reloaded")

    @commands.command(name="discord")
    async def discordcmd(self, ctx):
        url = "https://srhpyqt94yxb.statuspage.io/api/v2/summary.json"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        components = data["components"]
        api = components[0]    # API
        cf = components[1]     # Cloudflare
        mp = components[5]     # Media Proxy
        gw = components[10]    # Gateway
        pn = components[12]    # Push Notifications
        src = components[15]   # search

        embed = discord.Embed(title="Discord Status", color=0x5865F2)
        embed.add_field(name="API", value=api["status"])
        embed.add_field(name="Cloudflare", value=cf["status"])
        embed.add_field(name="Media Proxy", value=mp["status"])
        embed.add_field(name="Gateway", value=gw["status"])
        embed.add_field(name="Push Notifications", value=pn["status"])
        embed.add_field(name="Search", value=src["status"])
        await ctx.send(embed=embed)
    @commands.command(name="solmecke")
    async def solcmd(self, ctx, args1, args2):
        if args1.lower() == "gg":
            artikel = "artikel-" + args2
        else:
            artikel = args2

        solmeckeurl = "https://de.openlegaldata.io/law/" + args1.lower() + "/" + artikel.lower()
        await ctx.send(solmeckeurl)




async def setup(bot):
    # finally, adding the cog to the bot
    await bot.add_cog(info(bot=bot))