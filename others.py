import discord
from discord import app_commands
from discord.ext import commands
import random, json, urllib.request, time


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
        result = target.mention + ", " + data["insult"]
        await ctx.send(result)

    # Magnum Opus, THROWING RANDOM SHIT
    @commands.command(name="throw")
    async def throw(self, ctx):
        f = open('ammo.json', )
        jammo = json.load(f)
        ammo = jammo["ammo"]
        steven = jammo["ammoSteven"]
        soft = jammo["ammoSoft"]
        hard = jammo["ammoHard"]
        corium = jammo["ammoCorium"]
        amountlimit = jammo["amount"]
        amount = random.randint(1, amountlimit)
        # print(len(ammo), len(steven), len(soft), len(hard), len(corium))
        output = ""
        r = 0
        for r in range(amount):
            sel = random.randint(1,100)
            if r <= 0:
                output = output
            elif r < amount-2:
                output = output + ", "
            else:
                output = output + " and "
            match sel:
                case sel if sel <=40:
                    sela = random.randint(0, len(ammo)-1)
                    output = output + ammo[sela]
                case sel if sel <=60:
                    sela = random.randint(0, len(steven)-1)
                    output = output + steven[sela]
                case sel if sel <=80:
                    sela = random.randint(0, len(soft)-1)
                    # print(sela)
                    output = output + soft[sela]
                case sel if sel <=95:
                    sela = random.randint(0, len(hard)-1)
                    output = output + hard[sela]
                case sel if sel >95:
                    sela = random.randint(0, len(corium)-1)
                    output = output + corium[sela]
                case _:
                    output = output + "Error"
            r += 1
        if not ctx.message.mentions:
            target = ctx.author.mention
        else:
            target = ctx.message.mentions[0].mention
        await ctx.send(output + " is thrown at " + target)


async def setup(bot):
    # finally, adding the cog to the bot
    await bot.add_cog(others(bot=bot))