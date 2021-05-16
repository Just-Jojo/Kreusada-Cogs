import asyncio
import contextlib
import datetime
import pathlib
import random

import discord
import yaml

from redbot.core import commands, Config
from redbot.core.commands import BadArgument, Context
from redbot.core.utils import chat_formatting as cf

from yaml.parser import (
    ParserError as YAMLParserError,
    ScannerError as YAMLScannerError,
    MarkedYAMLError as YAMLMarkedError
)

with open(pathlib.Path(__file__).parent / "raffle.yaml") as f:
    asset = cf.box("".join(f.readlines()), lang="yaml")


class RaffleError(Exception):
    """Base exception for all raffle exceptions."""
    pass


class RequiredKeyError(RaffleError):
    """Raised when a raffle key is required."""

    def __init__(self, **kwargs):
        self.key = kwargs.get("key")

    def __str__(self):
        return f"The \"{self.key}\" key is required"


class UnknownRoleError(RaffleError):
    """Raised when an invalid role is provided to the parser."""

    def __init__(self, **kwargs):
        self.role = kwargs.get("role")

    def __str__(self):
        return f"\"{self.role}\" was not a valid role"

class UnknownUserError(RaffleError):
    """Raised when an invalid role is provided to the parser."""

    def __init__(self, **kwargs):
        self.user = kwargs.get("user")

    def __str__(self):
        return f"\"{self.user}\" was not a valid user"

class RaffleParser(object):
    """Parses the required and relevant yaml data to ensure
    that it matches the specified requirements."""

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.name = data.get("name", None)
        self.account_age = data.get("account_age", None)
        self.roles_needed_to_enter = (
            data.get("roles_needed_to_enter", None) 
            or data.get("role_needed_to_enter", None)
        )
        self.prevented_users = (
            data.get("prevented_users", None)
            or data.get("prvented_user", None)
        )

    def parser(self, ctx: Context):
        if self.account_age:
            if not isinstance(self.account_age, int):
                raise BadArgument("Days must be int, not {}".format(type(self.account_age).__name__))
            if self.account_age > (datetime.datetime.now() - datetime.datetime(2015, 5, 13)).days:
                raise BadArgument("Days must be less than Discord's creation date")
        if self.name:
            if not isinstance(self.name, str):
                raise BadArgument("Name must be str, not {}".format(type(self.name).__name__))
            if len(self.name) > 15:
                raise BadArgument("Name must be under 15 characters, your raffle name had {}".format(len(self.name)))
        else:
            raise RequiredKeyError(key="name")
        if self.roles_needed_to_enter:
            if not isinstance(self.roles_needed_to_enter, (int, list)):
                raise BadArgument("Roles must be int or list of ints, not {}".format(type(self.roles_needed_to_enter).__name__))
            if isinstance(self.roles_needed_to_enter, list):
                for r in self.roles_needed_to_enter:
                    if not ctx.guild.get_role(r):
                        raise UnknownRoleError(role=r)
            else:
                if not ctx.guild.get_role(self.roles_needed_to_enter):
                    raise UnknownRoleError(role=self.roles_needed_to_enter)
        if self.prevented_users:
            if not isinstance(self.prevented_users, (int, list)):
                raise BadArgument("Prevented users must be int or list of ints, not {}".format(type(self.prevented_users).__name__))
            if isinstance(self.prevented_users, list):
                for u in self.prevented_users:
                    if not ctx.bot.get_user(u):
                        raise UnknownRoleError(user=u)
            else:
                if not ctx.bot.get_user(self.prevented_users):
                    raise UnknownRoleError(user=self.prevented_users)
                    


class Raffle(commands.Cog):
    """Create raffles for your server."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, 583475034985340, force_registration=True)
        self.config.register_guild(raffles={})

    @staticmethod
    def format_traceback(exc) -> str:
        boxit = lambda x, y: cf.box(f"{x}: {y}", lang="yaml")
        return boxit(exc.__class__.__name__, exc)

    @staticmethod
    def cleanup_code(content) -> str:
        # From redbot.core.dev_commands, thanks will :P
        if content.startswith("```") and content.endswith("```"):
            return "\n".join(content.split("\n")[1:-1])
        return content.strip("` \n")

    @staticmethod
    def validator(data) -> dict:
        try:
            loader = yaml.full_load(data)
        except (YAMLParserError, YAMLScannerError, YAMLMarkedError):
            return False
        if not isinstance(loader, dict):
            return False
        return loader

    async def replenish_cache(self, ctx: Context) -> None:
        async with self.config.guild(ctx.guild).raffles() as r:
            for v in list(r.values()):
                getter = v[0].get("entries")
                for userid in getter:
                    if not self.bot.get_user(userid):
                        getter.remove(userid)

    @commands.group()
    async def raffle(self, ctx: Context):
        """Manage raffles for your server."""

    @raffle.command()
    async def create(self, ctx: Context):
        """Create a raffle."""
        check = lambda x: x.author == ctx.author and x.channel == ctx.channel
        await ctx.send("Now you need to compose your YAML. For reference, see below:" + asset)
        try:
            content = await self.bot.wait_for("message", timeout=250, check=check)
        except asyncio.TimeoutError:
            return await ctx.send("You took too long to respond.")
        content = content.content
        valid = self.validator(self.cleanup_code(content))
        if not valid:
            return await ctx.send("Please provide valid YAML.")
        try:
            parser = RaffleParser(valid)
            parser.parser(ctx)
        except Exception as e:
            return await ctx.send(self.format_traceback(e))
        async with self.config.guild(ctx.guild).raffles() as raffle:
            data = {
                "account_age": valid.get("account_age", None),
                "roles_needed_to_enter": valid.get("roles_needed_to_enter", []),
                "prevented_users": valid.get("prevented_users", []),
                "entries": [],
                "owner": ctx.author.id,
            }
            rafflename = valid.get("name").lower()
            raffle[rafflename] = [data]
            await ctx.send(
                "Raffle created with the name \"{0}\". Type `{1}raffle join {0}` to join the raffle.".format(
                    rafflename,
                    ctx.clean_prefix
                )
            )
        await self.replenish_cache(ctx)

    @raffle.command()
    async def join(self, ctx: Context, raffle: str):
        """Join a raffle."""
        async with self.config.guild(ctx.guild).raffles() as r:
            raffle_data = r.get(raffle, None)
            if not raffle_data:
                return await ctx.send("There is not an ongoing raffle with the name `{}`.".format(raffle))
            raffle_entries = raffle_data[0].get("entries")
            if ctx.author.id in raffle_entries:
                return await ctx.send("You are already in this raffle.")
            raffle_entries.append(ctx.author.id)
            await ctx.send(f"{ctx.author.mention} you have been added to the raffle!")

    @raffle.command()
    async def leave(self, ctx: Context, raffle: str):
        """Leave a raffle."""
        async with self.config.guild(ctx.guild).raffles() as r:
            raffle_data = r.get(raffle, None)
            if not raffle_data:
                return await ctx.send("There is not an ongoing raffle with the name `{}`.".format(raffle))
            raffle_entries = raffle_data[0].get("entries")
            if not ctx.author.id in raffle_entries:
                return await ctx.send("You are not entered into this raffle.")
            raffle_entries.remove(ctx.author.id)
            await ctx.send(f"{ctx.author.mention} you have been removed from the raffle.")

    @raffle.command()
    async def mention(self, ctx: Context, raffle: str):
        """Mention all the users entered into a raffle."""
        await self.replenish_cache(ctx)
        async with self.config.guild(ctx.guild).raffles() as r:
            raffle_data = r.get(raffle, None)
            if not raffle_data:
                return await ctx.send("There is not an ongoing raffle with the name `{}`.".format(raffle))
            raffle_entities = lambda x: raffle_data[0].get(x)
            if not ctx.author.id == raffle_entities("owner"):
                return await ctx.send("You are not the owner of this raffle.")
            if not raffle_entities("entries"):
                return await ctx.send("There are no entries yet for this raffle.")
            for page in cf.pagify(cf.humanize_list([self.bot.get_user(u).mention for u in raffle_entities("entries")])):
                await ctx.send(page)

    @raffle.command()
    async def end(self, ctx: Context, raffle: str):
        """End a raffle."""
        async with self.config.guild(ctx.guild).raffles() as r:
            raffle_data = r.get(raffle, None)
            if not raffle_data:
                return await ctx.send("There is not an ongoing raffle with the name `{}`.".format(raffle))
            raffle_entities = lambda x: raffle_data[0].get(x)
            if not ctx.author.id == raffle_entities("owner"):
                return await ctx.send("You are not the owner of this raffle.")
            del raffle_data
            await ctx.send("Raffle ended.")
        
    @raffle.command(name="list")
    async def _list(self, ctx: Context):
        """List the currently ongoing raffles."""
        async with self.config.guild(ctx.guild).raffles() as r:
            if not r:
                return await ctx.send("There are no ongoing raffles.")
            await ctx.send("\n".join(f"`{r}`" for r in list(r.keys())))

    @raffle.command()
    async def teardown(self, ctx: Context):
        """End ALL ongoing raffles."""
        async with self.config.guild(ctx.guild).raffles() as r:
            r.clear()
            await ctx.send("Raffles cleared.")

    @raffle.command()
    async def raw(self, ctx: Context, raffle: str):
        """View the raw dict for a raffle."""
        async with self.config.guild(ctx.guild).raffles() as r:
            raffle_data = r.get(raffle, None)
            if not raffle_data:
                return await ctx.send("There is not an ongoing raffle with the name `{}`.".format(raffle))
            data = {raffle: raffle_data}
            for page in cf.pagify(str(data)):
                await ctx.send(cf.box(page, lang="json"))
        await self.replenish_cache(ctx)

    @raffle.command()
    async def members(self, ctx: Context, raffle: str):
        """Get all the members of a raffle."""
        async with self.config.guild(ctx.guild).raffles() as r:
            raffle_data = r.get(raffle, None)
            if not raffle_data:
                return await ctx.send("There is not an ongoing raffle with the name `{}`.".format(raffle))
            raffle_entities = lambda x: raffle_data[0].get(x)
            if not raffle_entities("entries"):
                return await ctx.send("There are no entries yet for this raffle.")
            for page in cf.pagify(cf.humanize_list([self.bot.get_user(u).display_name for u in raffle_entities("entries")])):
                await ctx.send(page)

    @raffle.command()
    async def draw(self, ctx: Context, raffle: str):
        """Draw a raffle and select a winner."""
        async with self.config.guild(ctx.guild).raffles() as r:
            raffle_data = r.get(raffle, None)
            if not raffle_data:
                return await ctx.send("There is not an ongoing raffle with the name `{}`.".format(raffle))
            raffle_entities = lambda x: raffle_data[0].get(x)
            if not raffle_entities("entries"):
                return await ctx.send("There are no participants yet for this raffle.")
            winner = random.choice(raffle_entities("entries"))
            await ctx.send(
                "Congratulations {}, you have won the {} raffle! {}".format(
                    self.bot.get_user(winner).mention,
                    raffle,
                    ":tada:"
                )
            )
            del raffle_data



            