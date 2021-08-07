import asyncio
import contextlib
import logging
import re

import discord
import yaml

from redbot.core import Config, commands
from redbot.core.commands import BadArgument, Context, Converter
from redbot.core.utils.chat_formatting import box, humanize_list, inline
from redbot.core.utils.predicates import MessagePredicate
from yaml.error import MarkedYAMLError

log = logging.getLogger("red.kreusada.status")
YAML_CODE_BLOCK = re.compile(r"^((```y(a)ml?)(?=\s)|(```))")

_EMOJI_MAPPER = {
    "online": "\N{LARGE GREEN CIRCLE}",
    "idle": "\N{LARGE YELLOW CIRCLE}",
    "dnd": "\N{LARGE RED CIRCLE}",
    "invisible": "\N{MEDIUM WHITE CIRCLE}\N{VARIATION SELECTOR-16}"
}

ACTIVITY_ADDONS_MAPPER = {
    "listening": " to",
    "competing": " in",
}

class Code(Converter):
    async def convert(self, ctx: Context, code: str):
        if code.startswith("```") and code.endswith("```"):
            code = YAML_CODE_BLOCK.sub("", code)[:-3]
        else:
            code = code.strip("` \n")

        try:
            loader = yaml.full_load(code)
        except MarkedYAMLError:
            raise BadArgument("Please send valid YAML.")
        else:
            if not isinstance(loader, dict):
                raise BadArgument("Please provide valid YAML.")

        for key, val in loader.items():
            if isinstance(val, list):
                update = {}
                for _dict in val:
                    update.update(_dict)
                loader[key] = update

        return loader

def format_activity_name(activity):
    if activity in ACTIVITY_ADDONS_MAPPER.keys():
        return activity + ACTIVITY_ADDONS_MAPPER[activity].capitalize()
    return activity.capitalize()

default_settings = {
    "status": {
        "type": "online",
        "persist": True,
    },
    "activity": {
        "type": None,
        "content": None,
        "persist": False
    }
}

class StatusYamlParsingError(Exception):
    pass


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, 4054375435346, True)
        self.config.register_global(**default_settings)
        self.task = asyncio.create_task(self.start_up_change_presence())
        if 719988449867989142 in self.bot.owner_ids:
            with contextlib.suppress(RuntimeError, ValueError):
                self.bot.add_dev_env_value(self.__class__.__name__.lower(), lambda x: self)

    def cog_unload(self):
        self.task.cancel()

    async def start_up_change_presence(self):
        await self.bot.wait_until_red_ready()
        await self.change_presence()

    async def change_inpersistent_presence(self, settings):
        kwargs = {}
        activity = settings["activity"]
        status = settings["status"]
        if "status" in settings.keys():
            kwargs["status"] = getattr(discord.Status, status["type"])
        if "activity" in settings.keys():
            if activity["type"] == "streaming":
                kwds = {
                    "url": f"https://www.twitch.tv/{activity['content'].split('-')[0]}",
                    "name": activity['content'].split('-')[1],
                }
                activity_type = discord.Streaming(**kwds)
            else:
                activity_type = getattr(discord.ActivityType, activity["type"])
                activity = discord.Activity(name=activity["content"], type=activity_type)
                kwargs["activity"] = activity
        if kwargs:
            await self.bot.change_presence(**kwargs)


    async def change_presence(self):
        config = await self.config.all()
        kwargs = {}
        status = config["status"]
        activity = config["activity"]

        if not status["persist"]:
            await self.config.status.clear()
        else:
            kwargs["status"] = getattr(discord.Status, status["type"])

        if not activity["persist"]:
            await self.config.activity.clear()
        else:
            if activity["type"] == "streaming":
                kwds = {
                    "url": f"https://www.twitch.tv/{activity['content'].split('-')[0]}",
                    "name": activity['content'].split('-')[1],
                }
                activity_type = discord.Streaming(**kwds)
            else:
                activity_type = getattr(discord.ActivityType, activity["type"])
                activity = discord.Activity(name=activity["content"], type=activity_type)
                kwargs["activity"] = activity

        print(kwargs)
        if kwargs:
            await self.bot.change_presence(**kwargs)

    async def parse(ctx, loader):
        for key in loader.keys():
            if key not in ("status", "activity"):
                raise StatusYamlParsingError("Unrecognized key: {}".format(inline(key)))

        if "status" in loader.keys():
            
            status = loader["status"]

            for key in status.keys():
                if key not in ("persist", "type"):
                    raise StatusYamlParsingError("Unrecognized status key: {}".format(inline(key)))

            if not all([x in status.keys() for x in ["persist", "type"]]):
                raise StatusYamlParsingError("Persist and type status keys are required.")

            if not isinstance(status["persist"], bool):
                raise StatusYamlParsingError("Status persist key must be a boolean.")

            if not isinstance(status["type"], str):
                raise StatusYamlParsingError("Status type key must be a string.")

            statuses = ("online", "idle", "dnd", "invisible")
            
            if not status["type"] in statuses:
                raise StatusYamlParsingError("Status type unrecognized ({}). Must be one of {}.".format(inline(status["type"]), humanize_list(statuses, style="or")))

        if "activity" in loader.keys():

            activity = loader["activity"]

            for key in activity.keys():
                if key not in ("persist", "type", "content"):
                    raise StatusYamlParsingError("Unrecognized activity key: {}".format(inline(key)))

            if not all([x in activity.keys() for x in ["persist", "type", "content"]]):
                raise StatusYamlParsingError("Persist and type status keys are required.")

            if not isinstance(activity["persist"], bool):
                raise StatusYamlParsingError("Activity persist key must be a boolean.")

            if not isinstance(activity["type"], str):
                raise StatusYamlParsingError("Activity type key must be a string.")

            activities = ("playing", "watching", "listening", "competing", "streaming")
            
            if not activity["type"] in activities:
                raise StatusYamlParsingError("Activity type unrecognized ({}). Must be one of {}.".format(inline(activity["type"]), humanize_list(activities, style="or")))

            if activity["type"] == "streaming": 
                if not re.match(r".+-.+", activity["content"]):
                    raise StatusYamlParsingError("If the activity type is streaming, the content must be in the format `streamer-stream_title`.")
                if len(activity["content"].split("-")[0]) > 511:
                    raise StatusYamlParsingError("The maximum number of characters for the streamer is 511 characters.")
                if "twitch.tv/" not in activity["content"] and len(activity["content"].split("-")[1]) > (128 - len("https://www.twitch.tv/")):
                    raise StatusYamlParsingError("The maximum number of characters for the stream title is 128 characters.")

            if len(activity["content"]) > 128:
                raise StatusYamlParsingError("The maximum length for activity content is 128 characters.")

        return loader

    @commands.command(usage="<yaml>")
    async def statusset(self, ctx, *, _yaml: Code):
        """Set [botname]'s status using YAML.
        
        There are two keys: `status` and `activity`.
        
        **Status**
         - `type`: The status type, must be one of `online`, `idle`, `dnd`, or `invisible`.
         - `persist`: Whether the status persists through restarts, shutdowns, and cog reloads.
         
        **Activity**
         - `type`: The activity type, must be one of `playing`, `listening`, `watching`, `competing`, or `streaming`.
         - `content`: The content that comes after this activity type.
         - `persist`: Whether the activity persists through restarts, shutdowns, and cog reloads.

        **Example Usage**
        ```yaml
        status:
        - type: dnd
        - persist: false
        activity:
        - type: watching
        - content: you
        - persist: true
        ```

        Don't worry, the command will post meaningful error messages in case you get something wrong.
        """
        try:
            parser = await self.parse(_yaml)
        except StatusYamlParsingError as exc:
            return await ctx.send(exc)

        await ctx.send(box(parser, "json"))
        for category in parser.keys():
            await self.config.set_raw(category, value=parser[category])
        await self.change_inpersistent_presence(parser)
        return

    @commands.command()
    async def status(self, ctx: Context):
        """Shows the current status details for [botname]."""
        settings = await self.config.all()
        status = str(ctx.me.status)
        message = f"{_EMOJI_MAPPER[status]} {self.bot.user.name} is currently appearing in {status} state.\n"
        if not settings["status"]["persist"]:
            verb = "stay the same"
        elif status==settings["status"]["type"]:
            verb = "stay the same"
        else:
            new_status = settings["status"]["type"]
            verb = "change to " + new_status
        message += f"This status is destined to {verb} when the cog is reloaded, or when the bot is restarted.\n\n"
        
        if ctx.me.activity:
            message += f"Additionally, this bot also currently has a {ctx.me.activity.type.name} activity status. "
            message += f"(`{format_activity_name(ctx.me.activity.type.name)} {ctx.me.activity.name}`)\n"
            starting_verb = "This"
        else:
            message += f"\n"
            starting_verb = "In addition, their"

        if settings["activity"]["type"] == ctx.me.activity.type.name and settings["activity"]["persist"]:
            new_activity = inline(f"{format_activity_name(settings['activity']['type'])} {settings['activity']['content']}")
            verb = "change to " + new_activity
        else:
            verb = "stay the same"
        message += f"{starting_verb} activity is destined to {verb} when the cog is reloaded, or when the bot is restarted.\n"

        await ctx.send(message)
def setup(bot):
    cog = Status(bot)
    bot.add_cog(cog)