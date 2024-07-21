import discord
import json
from discord.ext import commands


f = open('settings.json',)
settings = json.load(f)

token = settings["token"]
class MyClient(commands.Bot):
    def __init__(self):
        #initialize our bot instance, make sure to pass your intents!
        #for this example, weil just have everything enabled
        super().__init__(
            command_prefix=settings["prefix"],
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
        await self.load_extension("info")
        await self.load_extension("others")


client = MyClient()
client.run(token)