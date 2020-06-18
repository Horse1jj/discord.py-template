import discord
from discord.ext import commands
from modules.config import Config
from modules.sql import connect, close


class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, name):
        self.bot.reload_extension(f'cogs.{name}')

    @commands.command()
    @commands.is_owner()
    async def get_all(self, ctx, *, name):
        conn, c = connect()
        await ctx.send('\n'.join([', '.join(i) for i in list(c.execute(f"SELECT * FROM {name}"))]))
        close(conn)

    @commands.command()
    @commands.is_owner()
    async def execute(self, ctx, *, sql):
        conn, c = connect()
        c.execute(sql)
        close(conn)

def setup(bot):
    bot.add_cog(Owner(bot))