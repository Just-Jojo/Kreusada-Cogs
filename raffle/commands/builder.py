import asyncio
import contextlib
from typing import Optional

import discord
from redbot.core import commands
from redbot.core.commands import Context
from redbot.core.i18n import Translator
from redbot.core.utils.chat_formatting import box
from redbot.core.utils.predicates import MessagePredicate

from ..mixins.abc import RaffleMixin
from ..mixins.metaclass import MetaClass
from ..utils.enums import RaffleComponents
from ..utils.exceptions import RaffleError
from ..utils.formatting import cross, tick
from ..utils.helpers import (
    cleanup_code,
    format_traceback,
    format_underscored_text,
    getstrftime,
    number_suffix,
    validator,
)
from ..utils.parser import RaffleManager

_ = Translator("Raffle", __file__)


class BuilderCommands(RaffleMixin, metaclass=MetaClass):
    """Mixin for commands under ``[p]raffle edit``."""

    @commands.group()
    async def raffle(self, ctx: Context):
        pass

    @raffle.group()
    async def create(self, ctx: Context):
        """Create a raffle."""
        pass

    @create.command()
    async def reaction(self, ctx: Context):
        """Create a reaction-based raffle."""
        await ctx.trigger_typing()
        check = lambda x: x.author == ctx.author and x.channel == ctx.channel
        message = _(
            "You're about to create a new **reaction-based** raffle.\n"
            "Please consider reading the docs about the various "
            "conditional blocks if you haven't already.\n\n" + self.docs
        )

        message += _("\n\n**Conditions Blocks:**") + box(
            "\n".join(f"+ {e.name}" for e in RaffleComponents), lang="diff"
        )
        await ctx.send(message)

        try:
            content = await self.bot.wait_for("message", timeout=500, check=check)
        except asyncio.TimeoutError:
            with contextlib.suppress(discord.NotFound):
                await message.delete()

        valid = validator(cleanup_code(content.content))

        if not valid:
            return await ctx.send(
                cross(
                    _(
                        "Please provide valid YAML. You can validate your raffle YAML using `{}raffle parse`."
                    )
                ).format(ctx.clean_prefix)
            )

        try:
            parser = RaffleManager(valid, "reaction")
            parser.parser(ctx)
        except RaffleError as e:
            exc = cross(_("An exception occured whilst parsing your data."))
            return await ctx.send(exc + format_traceback(e))

        async with self.config.guild(ctx.guild).raffles() as raffle:

            rafflename = valid.get("name").lower()

            if rafflename in [x.lower() for x in raffle.keys()]:
                return await ctx.send(_("A raffle with this name already exists."))

            datetimeinfo = _(
                "{day} of {month}, {year} ({time})".format(
                    day=number_suffix(getstrftime("d")),
                    month=getstrftime("B"),
                    year=getstrftime("Y"),
                    time=getstrftime("X"),
                )
            )

            data = {
                "entries": [],
                "owner": ctx.author.id,
                "created_at": datetimeinfo,
            }

            conditions = {
                "end_message": valid.get("end_message", None),
                "join_message": valid.get("join_message", None),
                "account_age": valid.get("account_age", None),
                "server_join_age": valid.get("server_join_age", None),
                "roles_needed_to_enter": valid.get("roles_needed_to_enter", None),
                "badges_needed_to_enter": valid.get("badges_needed_to_enter", None),
                "prevented_users": valid.get("prevented_users", None),
                "allowed_users": valid.get("allowed_users", None),
                "description": valid.get("description", None),
                "maximum_entries": valid.get("maximum_entries", None),
                "on_end_action": valid.get("on_end_action", None),
                "suspense_timer": valid.get("suspense_timer", None),
                "reaction_emoji": valid.get("reaction_emoji", "\N{PARTY POPPER}"),
            }

            for k, v in conditions.items():
                if v:
                    data[k] = v

            try:
                await content.add_reaction(conditions["reaction_emoji"])
            except discord.HTTPException:
                await ctx.send(
                    _(
                        "Your reaction emoji {} appears to be invalid. "
                        "Make sure that if it is a custom emoji, I am in the "
                        "server that the emoji is in."
                    ).format(f"\"{conditions['reaction_emoji']}\"")
                )
                return

            await ctx.send(_("Which channel would you like to start the raffle in?"))
            check = MessagePredicate.valid_text_channel(ctx)
            try:
                await self.bot.wait_for("message", check=check, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send(_("You took too long to respond."))
                return

            channel = check.result

            if not await ctx.embed_requested():
                await ctx.send(
                    _("I need to be able to send messages to {}").format(channel.mention)
                )
                return
            if not channel.permissions_for(ctx.me).send_messages:
                await ctx.send(_("I am unable to send messages to this channel."))
                return
            if not channel.permissions_for(ctx.me).add_reactions:
                await ctx.send(_("I am unable to add reactions to this channel."))
                return

            embed = discord.Embed(
                title=f"{rafflename} raffle",
                description=conditions["description"]
                or "No description was provided for this raffle.",
                color=await ctx.embed_colour(),
            )

            filtered_conditions = []
            blocked_conditions = ("description", "reaction_emoji")
            for k, v in list(filter(lambda x: bool(x[1]), conditions.items())):
                if k in blocked_conditions:
                    continue
                if "user" in k:
                    users = "\n" + "\n".join(
                        f"- {v}" for v in [ctx.guild.get_member(u).name for u in v]
                    )
                    filtered_conditions.append((k, users))
                if "role" in k:
                    roles = "\n" + "\n".join(
                        f"- {v}" for v in [ctx.guild.get_role(r).name for r in v]
                    )
                    filtered_conditions.append((k, roles))
                elif isinstance(v, list):
                    filtered_conditions.append((k, "\n" + "\n".join(f"- {v}" for v in v)))
                else:
                    filtered_conditions.append((k, v))

            embed.add_field(
                name="Conditions",
                value=box(
                    "\n".join(
                        f"{format_underscored_text(k)}: {v}" for k, v in filtered_conditions
                    ),
                    lang="yaml",
                ),
            )

            msg = await channel.send(embed=embed)
            await msg.add_reaction(conditions["reaction_emoji"])

            data["external-settings"] = {"type": "reaction", "msgid": msg.id}

            raffle[rafflename] = data

            kwargs = {"content": tick(_("Raffle created with the name `{}`.".format(rafflename)))}
            if ctx.channel == check.result:
                kwargs["delete_after"] = 3

        await ctx.send(**kwargs)
        await self.clean_guild_raffles(ctx)

    @create.command(name="complex")
    async def _complex(self, ctx: Context):
        """Create a raffle with complex conditions."""
        await ctx.trigger_typing()
        check = lambda x: x.author == ctx.author and x.channel == ctx.channel
        message = _(
            "You're about to create a new raffle.\n"
            "Please consider reading the docs about the various "
            "conditional blocks if you haven't already.\n\n" + self.docs
        )

        message += _("\n\n**Conditions Blocks:**") + box(
            "\n".join(f"+ {e.name}" for e in RaffleComponents), lang="diff"
        )
        await ctx.send(message)

        try:
            content = await self.bot.wait_for("message", timeout=500, check=check)
        except asyncio.TimeoutError:
            with contextlib.suppress(discord.NotFound):
                await message.delete()

        valid = validator(cleanup_code(content.content))

        if not valid:
            return await ctx.send(
                cross(
                    _(
                        "Please provide valid YAML. You can validate your raffle YAML using `{}raffle parse`."
                    )
                ).format(ctx.clean_prefix)
            )

        try:
            parser = RaffleManager(valid, "command")
            parser.parser(ctx)
        except RaffleError as e:
            exc = cross(_("An exception occured whilst parsing your data."))
            return await ctx.send(exc + format_traceback(e))

        async with self.config.guild(ctx.guild).raffles() as raffle:

            rafflename = valid.get("name").lower()

            if rafflename in [x.lower() for x in raffle.keys()]:
                return await ctx.send(_("A raffle with this name already exists."))

            datetimeinfo = _(
                "{day} of {month}, {year} ({time})".format(
                    day=number_suffix(getstrftime("d")),
                    month=getstrftime("B"),
                    year=getstrftime("Y"),
                    time=getstrftime("X"),
                )
            )

            data = {
                "entries": [],
                "owner": ctx.author.id,
                "created_at": datetimeinfo,
                "external-settings": {"type": "command"},
            }

            conditions = {
                "end_message": valid.get("end_message", None),
                "join_message": valid.get("join_message", None),
                "account_age": valid.get("account_age", None),
                "server_join_age": valid.get("server_join_age", None),
                "roles_needed_to_enter": valid.get("roles_needed_to_enter", None),
                "badges_needed_to_enter": valid.get("badges_needed_to_enter", None),
                "prevented_users": valid.get("prevented_users", None),
                "allowed_users": valid.get("allowed_users", None),
                "description": valid.get("description", None),
                "maximum_entries": valid.get("maximum_entries", None),
                "on_end_action": valid.get("on_end_action", None),
                "suspense_timer": valid.get("suspense_timer", None),
            }

            for k, v in conditions.items():
                if v:
                    data[k] = v

            await ctx.send(tick(_("Raffle created with the name `{}`.".format(rafflename))))

            raffle[rafflename] = data
            await self.clean_guild_raffles(ctx)

    @create.command()
    async def simple(self, ctx, raffle_name: str, *, description: Optional[str] = None):
        """Create a simple arguments with just a name and description.

        **Arguments:**
            - `<name>` - The name for the raffle.
            - `[description]` - The description for the raffle.
        """
        raffle_name = raffle_name.lower()
        async with self.config.guild(ctx.guild).raffles() as raffle:

            if raffle_name in [x.lower() for x in raffle.keys()]:
                return await ctx.send(_("A raffle with this name already exists."))

            datetimeinfo = _(
                "{day} of {month}, {year} ({time})".format(
                    day=number_suffix(getstrftime("d")),
                    month=getstrftime("B"),
                    year=getstrftime("Y"),
                    time=getstrftime("X"),
                )
            )

            data = {
                "entries": [],
                "owner": ctx.author.id,
                "created_at": datetimeinfo,
            }

            if description:
                data["description"] = description

            raffle[raffle_name] = data
        await ctx.send(tick(_("Raffle created with the name `{}`.".format(raffle_name))))
        await self.clean_guild_raffles(ctx)
