import discord
import config
import discord.ext
import string
import random
import secrets
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions


class AuthBot(commands.Cog):
    def __init__(self, client):
        print('AuthCOG  LOADED')
        self.client = client
        self.active_tokens = []
        self.current_clients = []

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author in self.current_clients:
            if isinstance(message.channel, discord.channel.DMChannel):
                if message.content in self.active_tokens:
                    guild = self.client.get_guild(config.GUILD_ID)
                    member = await guild.fetch_member(int(message.author.id))
                    role = get(guild.roles, name='Member')
                    await member.add_roles(role)
                    user = message.author
                    username = user.mention
                    audit_log = self.client.get_channel(config.AUDIT_LOG)
                    await audit_log.send(config.NEW_MEMBER(username))
                    await message.channel.send(config.AUTHORIZED)
                else:
                    await message.channel.send(config.ACCESS_DENIED)
                self.current_clients.remove(message.author)
                await message.author.send(config.SESSION_CLOSE)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await self.client.fetch_user(payload.user_id)
        bot_user = await self.client.fetch_user(config.CLIENT_ID)
        if user in self.current_clients:
            self.current_clients.remove(user)
            await user.send(config.SESSION_CLOSE)
        if user == bot_user:
            pass
        else:
            await message.clear_reactions()
            await message.add_reaction(config.REACTION)
            username = config.GET_USERNAME(user)
            audit_log = self.client.get_channel(config.AUDIT_LOG)
            await audit_log.send(config.NEW_REQUEST(username))
            await user.send(config.SESSION_START)
            await user.send(config.DM_ENTER_TOKEN)
            self.current_clients.append(user)

    @commands.command(name='new_token', pass_context=True)
    @has_permissions(administrator=True)
    async def _new_token(self, ctx):
        if ctx.channel == self.client.get_channel(config.BOT_COMMANDS):
            token = ''.join(
                ''.join(
                    secrets.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(256, 512))))
            self.active_tokens.append(token)
            print(token)
            await ctx.send(config.TOKEN_CREATION(token))
            user = ctx.message.author
            username = user.mention
            audit_log = self.client.get_channel(config.AUDIT_LOG)
            await audit_log.send(config.TOKEN_NOTIF(username))
        else:
            await ctx.send('This command cannot be used in this channel.')

    @commands.command(name='new_token', pass_context=True)
    @has_permissions(administrator=True)
    async def _clear_tokens(self, ctx):
        self.active_tokens = []
        await ctx.send('```Cleared active tokens.```')


def setup(bot):
    bot.add_cog(AuthBot(bot))
