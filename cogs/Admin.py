from discord.ext import commands
from discord.ext.commands import has_permissions


class Admin(commands.Cog):
    def __init__(self, client):
        print('AdminCOG  LOADED')
        self.client = client

    @commands.command(name='reload', hidden=True, pass_context=True)
    @has_permissions(administrator=True)
    async def _reload(self, ctx, *, module: str):
        try:
            self.client.unload_extension(module)
            self.client.load_extension(module)
        except Exception as e:
            pass
        else:
            await ctx.send('\N{OK HAND SIGN}')


def setup(bot):
    bot.add_cog(Admin(bot))
