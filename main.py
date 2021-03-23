import discord
import config
from discord.ext import commands
from discord.ext.commands import has_permissions
from keepalive import keep_alive

client = commands.Bot(command_prefix='auth>')

extensions = ['cogs.AuthBot', 'cogs.Admin']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


keep_alive()
client.run(config.TOKEN)
