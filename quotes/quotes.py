import aiohttp

from redbot.core import commands
from redbot.core.utils.chat_formatting import bold


class Quotes(commands.Cog):
    """Get a random quote."""

    __version__ = "1.0.0"
    __author__ = ["Kreusada"]

    def __init__(self, bot):
        self.bot = bot
        self.api = 'https://api.quotable.io/random'

    def format_help_for_context(self, ctx: commands.Context) -> str:
        context = super().format_help_for_context(ctx)
        authors = ", ".join(self.__author__)
        return f"{context}\n\nAuthor: {authors}\nVersion: {self.__version__}"

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    @commands.command()
    async def quote(self, ctx):
        """Get a random quote."""
        await ctx.trigger_typing()
        async with aiohttp.request("GET", self.api) as r:
            content = await r.json()
        formatter = lambda x, y: f"From {bold(x)}\n{y}"
        return await ctx.send(formatter(content["author"], content["content"]))