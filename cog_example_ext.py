from discord import app_commands
from discord.ext import commands


# all cogs inherit from this base class
class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # adding a bot attribute for easier access

    # adding a command to the cog
    @commands.command(name="ping")
    async def pingcmd(self, ctx):
        """the best command in existence"""
        await ctx.send(ctx.author.mention)

    # adding a slash command to the cog (make sure to sync this!)
    @app_commands.command(name="ping")
    async def slash_pingcmd(self, interaction):
        """the second best command in existence"""
        await interaction.response.send_message(interaction.user.mention)

    # adding an event listener to the cog
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild and message.guild.me.guild_permissions.ban_members:
            await message.author.ban(reason="no speek")  # very good reason

    # doing something when the cog gets loaded
    async def cog_load(self):
        print(f"{self.__class__.__name__} loaded!")

    # doing something when the cog gets unloaded
    async def cog_unload(self):
        print(f"{self.__class__.__name__} unloaded!")


# usually you’d use cogs in extensions
# you would then define a global async function named 'setup', and it would take 'bot' as its only parameter
async def setup(bot):
    # finally, adding the cog to the bot
    await bot.add_cog(ExampleCog(bot=bot))