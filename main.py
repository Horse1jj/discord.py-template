from discord.ext import commands
from discord import Intents, app_commands
from modules import config
from os import getcwd, chdir, path, listdir
from pathlib import Path

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=config.Config().botPrefix,
            intents=Intents.all()
        )
        self.config = config.Config()

    async def setup_hook(self):
        chdir(path.dirname(__file__))
        chdir('cogs')
        for dir in listdir(Path(getcwd())):
            if dir.endswith('.py'):
                self.load_extension(f'cogs.{dir[:-3]}')


        guild = discord.Object(id=int(self.config.mainserverid))  
        await self.tree.sync(guild=guild)
        print(f"Synced commands to guild {guild.id}")

bot = MyBot()
bot.run(bot.config.botToken)
