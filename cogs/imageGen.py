import discord
import asyncio
from src.imageCreate import create_image
from src import log
from discord import app_commands
from core.classes import Cog_Extension

logger = log.setup_logger(__name__)

class imageGen(Cog_Extension):
    @app_commands.command(name = "create_image", description = "generate image by bing image creator")
    async def create_image(self, interaction: discord.Interaction, *, prompt: str):
        await interaction.response.defer(ephemeral=False, thinking=True)
        logger.info(f"\x1b[31m{interaction.user}\x1b[0m : '{prompt}' ({interaction.channel}) [BingImageCreator]")
        task = asyncio.create_task(create_image(interaction, prompt))
        await asyncio.gather(task)

async def setup(bot):
    await bot.add_cog(imageGen(bot))