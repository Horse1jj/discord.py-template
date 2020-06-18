from discord.ext import commands
from modules import config
from os import getcwd, chdir, path, listdir
from pathlib import Path

bot = commands.Bot(command_prefix=config.Config().botPrefix)


if __name__ == '__main__':
    chdir(path.dirname(__file__))
    chdir('cogs')
    for dir in listdir(Path(getcwd())):
        if dir.endswith('.py'):
            bot.load_extension(f'cogs.{dir[:-3]}')

bot.run(config.Config().botToken)