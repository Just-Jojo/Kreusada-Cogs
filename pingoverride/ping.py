import contextlib
import functools
import logging
import random
from datetime import datetime

import discord
import yaml
from redbot.core import Config, commands
from redbot.core.utils.chat_formatting import box
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu

from .enums import PingOverrideVariables
from .objects import Member
from .utils import add_random_messages, curl

log = logging.getLogger("red.kreusada.pingoverride")


ping_com: commands.Command = None


async def embed_check(ctx: commands.Context) -> bool:
    return await ctx.cog.config.embed.toggled()


class PingOverride(commands.Cog):
    """Override the Core's ping command with your own response."""

    settings = {
        "response": "Pong.",
        "embed": {"toggled": False, "title": "Ping"},
        "reply_settings": {"toggled": False, "mention": False},
    }

    __author__ = ["Kreusada"]
    __version__ = "3.5.0"

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, 6465983465798475, True)
        self.config.register_global(**self.settings)

        if 719988449867989142 in self.bot.owner_ids:
            with contextlib.suppress(RuntimeError, ValueError):
                self.bot.add_dev_env_value(self.__class__.__name__.lower(), lambda x: self)

    def cog_unload(self):
        global ping_com
        if ping_com:
            try:
                self.bot.remove_command("ping")
            except Exception as e:
                log.info(e)
            self.bot.add_command(ping_com)
        with contextlib.suppress(KeyError):
            self.bot.add_dev_env_value(self.__class__.__name__.lower(), lambda x: self)

    def format_help_for_context(self, ctx: commands.Context) -> str:
        context = super().format_help_for_context(ctx)
        authors = ", ".join(self.__author__)
        return f"{context}\n\nAuthors: {authors}\nVersion: {self.__version__}"

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Pong."""
        settings = await self.config.all()
        fmt_kwargs = {"author": Member(ctx.author), "latency": round(self.bot.latency * 1000, 2)}

        content = settings["response"]
        if isinstance(content, list):
            content = random.choice(content)
        content = content.format(**fmt_kwargs)

        if settings["embed"]["toggled"] and await ctx.embed_requested():
            embed = discord.Embed(
                title=settings["embed"]["title"].format(**fmt_kwargs),
                description=content,
                colour=await ctx.embed_colour(),
                timestamp=datetime.utcnow(),
            )
            kwargs = {"embed": embed}
        else:
            kwargs = {"content": content}

        if settings["reply_settings"]["toggled"]:
            kwargs["mention_author"] = settings["reply_settings"]["mention"]
            sender = functools.partial(ctx.reply, **kwargs)
        else:
            sender = functools.partial(ctx.send, **kwargs)

        await sender()

    @commands.group()
    async def pingset(self, ctx: commands.Context):
        """Set your ping message."""

    @pingset.command(name="message", aliases=["response"])
    async def pingset_message(self, ctx: commands.Context, *, ping_message: str):
        """Set the ping message sent when a user runs the ping command.

        **Variables:**

        - `{author.name}`
        - `{author.mention}`
        - `{author.id}`
        - `{author.discriminator}`
        - `{author.name_and_discriminator}`
        - `{latency}`
        """
        try:
            ping_message.format(
                author=Member(ctx.author), latency=round(self.bot.latency * 1000, 2)
            )
        except KeyError as e:
            curled = curl(str(e).strip("'"))
            await ctx.send(
                box(f"{e.__class__.__name__}: {curled} is not a recognized variable", lang="yaml")
            )
            return
        except commands.BadArgument as e:
            curled = curl(f"author.{e}")
            await ctx.send(
                box(
                    f"{e.__class__.__name__}: {curled} is not valid, author has no attribute {e}",
                    lang="yaml",
                )
            )
            return

        setter = await add_random_messages(ctx, ping_message)

        await self.config.response.set(setter)
        if len(setter) != 1:
            message = "The ping responses have been set."
        else:
            message = "The ping response has been set."
        await ctx.send(message)

    @pingset.group(name="reply", invoke_without_command=True)
    async def pingset_reply(self, ctx: commands.Context, reply: bool):
        """Set whether the ping message uses replies."""
        await self.config.reply_settings.toggled.set(reply)
        verb = "enabled" if reply else "disabled"
        await ctx.send("Replies have been {}.".format(verb))

    @pingset_reply.command(name="mention")
    async def pingset_reply_mention(self, ctx: commands.Context, mention: bool):
        """Set whether the ping message uses replies."""
        await self.config.reply_settings.mention.set(mention)
        verb = "enabled" if mention else "disabled"
        await ctx.send("Reply mentions have been {}.".format(verb))

    @pingset.group(name="embed")
    @commands.bot_has_permissions(embed_links=True)
    async def pingset_embed(self, ctx: commands.Context):
        """Manage the embed settings for the ping command."""

    @pingset_embed.command(name="toggle")
    async def pingset_embed_toggle(self, ctx: commands.Context, toggle: bool):
        """Toggle whether embeds should be enabled for the ping command.

        Note, this will only affect the output if the bot has the permissions to embed.
        """
        await self.config.embed.toggled.set(toggle)
        verb = "enabled" if toggle else "disabled"
        await ctx.send("Embeds have been {} for the ping message.".format(verb))

    @pingset_embed.command(name="title")
    @commands.check(embed_check)
    async def pingset_embed_title(self, ctx: commands.Context, *, title: str):
        """Set the title for the embed.

        **Variables:**

        - `{author.name}`
        - `{author.id}`
        - `{author.discriminator}`
        - `{author.name_and_discriminator}`
        - `{latency}`
        """
        title = title.replace("{author.mention}", "{author.name}")
        try:
            title.format(author=Member(ctx.author), latency=round(self.bot.latency * 1000, 2))
        except KeyError as e:
            curled = curl(str(e).split("'"))
            await ctx.send(
                box(f"{e.__class__.__name__}: {curled} is not a recognized variable", lang="yaml")
            )
            return
        except commands.BadArgument as e:
            curled = curl(f"author.{e}")
            await ctx.send(
                box(
                    f"{e.__class__.__name__}: {curled} is not valid, author has no attribute {e}",
                    lang="yaml",
                )
            )
            return

        await self.config.embed.title.set(title)
        await ctx.send("The embed title has been set.")

    @pingset.command(name="variables", aliases=["vars"])
    async def pingset_variables(self, ctx: commands.Context):
        """List the available variables for the ping command."""
        data = []
        key = lambda x: x.name
        sorted_vars = sorted(PingOverrideVariables, key=key)
        var_length = len(sorted_vars)
        for c, v in enumerate(sorted_vars, 1):
            var = v.name.lower()
            if v.name.lower() != "latency":
                var = f"author.{var}"
            _dict = {var: {"description": v.value[1], "example": v.value[2]}}
            page_info = f"Page {c}/{var_length}"
            kwargs = {"text": yaml.dump(_dict) + page_info, "lang": "yaml"}
            data.append(box(**kwargs))
        if ctx.channel.permissions_for(ctx.me).add_reactions:
            await menu(ctx, data, DEFAULT_CONTROLS)
        else:
            await ctx.send_interactive(data)

    @pingset.command(name="settings")
    async def pingset_settings(self, ctx: commands.Context):
        """See the current settings for PingOverride."""
        settings = await self.config.all()

        message = f"Replies: {settings['reply_settings']['toggled']}\n"
        if settings["reply_settings"]["mention"]:
            message += "\t- These replies will mention\n"
        message += f"Embed:\n\tenabled: {settings['embed']['toggled']}\n\ttitle: {settings['embed']['title']}\n"

        response = settings["response"]
        if isinstance(response, list):
            message += "Responses:\n" + "\n".join(f"\t- {i}" for i in response)
        else:
            message += "Response: " + response
        await ctx.send(box(message, lang="yaml"))


def setup(bot):
    global ping_com
    cog = PingOverride(bot)
    ping_com = bot.remove_command("ping")
    bot.add_cog(cog)
