import discord, time
from discord.ext import commands, tasks
from functions import database_functions as db
from functions import utility_functions as uf
from views import embeds


class utilityCommands(commands.Cog):
    """🔧 General utility commands."""
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.check_reminders.start()
        print(f"Initialized: {self.__cog_name__}")
        super().__init__()

    def cog_unload(self):
        self.check_reminders.cancel()

    # ── Reminder Loop ─────────────────────────────────────────────────────

    @tasks.loop(seconds=30)
    async def check_reminders(self):
        reminders = await db.get_due_reminders()
        for r in reminders:
            channel = self.bot.get_channel(r["channel_id"])
            if channel and isinstance(channel, discord.TextChannel):
                try:
                    await channel.send(embed=embeds.reminder_fire_x0(r["user_id"], r["message"]))
                except discord.Forbidden:
                    pass
            await db.delete_reminder(r["id"])

    @check_reminders.before_loop
    async def before_check_reminders(self):
        await self.bot.wait_until_ready()

    # ── AFK Handling ──────────────────────────────────────────────────────

    @commands.Cog.listener(name="on_message")
    async def afk_listener(self, message: discord.Message):
        if message.author.bot or not message.guild:
            return

        # Check if user is returning from AFK
        afk_data = await db.get_afk(message.guild.id, message.author.id)
        if afk_data:
            await db.remove_afk(message.guild.id, message.author.id)
            await message.reply(embed=embeds.afk_return_x0(message.author), delete_after=5)

        # Check if mentioned users are AFK
        for user in message.mentions:
            if user.bot:
                continue
            user_afk = await db.get_afk(message.guild.id, user.id)
            if user_afk:
                await message.reply(
                    embed=embeds.afk_notify_x0(user, user_afk["reason"], user_afk["timestamp"]),
                    delete_after=5
                )

    # ── Commands ──────────────────────────────────────────────────────────

    @commands.command(name="userinfo", aliases=["ui", "whois"])
    async def userinfo(self, ctx: commands.Context, user: discord.Member | None = None):
        """Display detailed information about a user."""
        target = user or (ctx.author if isinstance(ctx.author, discord.Member) else None)
        if target and isinstance(target, discord.Member):
            await ctx.send(embed=embeds.userinfo_x0(target))

    @commands.command(name="serverinfo", aliases=["si", "guildinfo"])
    async def serverinfo(self, ctx: commands.Context):
        """Display detailed information about the server."""
        if ctx.guild:
            await ctx.send(embed=embeds.serverinfo_x0(ctx.guild))


    @commands.command(name="channelinfo", aliases=["ci"])
    async def channelinfo(self, ctx: commands.Context, channel: discord.TextChannel | None = None):
        """Display information about a channel."""
        target = channel or (ctx.channel if isinstance(ctx.channel, discord.TextChannel) else None)
        if not target:
            return

        created_str = uf.format_timestamp(target.created_at)
        em = embeds.util_channelinfo_x0(target, created_str)
        await ctx.send(embed=em)

    @commands.command(name="afk")
    async def afk(self, ctx: commands.Context, *, reason: str = "AFK"):
        """Set your AFK status. Others will be notified when they mention you."""
        if ctx.guild:
            await db.set_afk(ctx.guild.id, ctx.author.id, reason)
            await ctx.send(embed=embeds.afk_set_x0(ctx.author, reason))

    @commands.command(name="remind", aliases=["remindme", "reminder"])
    async def remind(self, ctx: commands.Context, duration: str, *, message: str):
        """Set a reminder. Usage: remind 1h30m Take out the trash"""
        td = uf.parse_duration(duration)
        if not td:
            await ctx.send(embed=embeds.error_x0("Invalid duration! Use formats like `1h`, `30m`, `1d`."))
            return

        remind_at = int(time.time() + td.total_seconds())
        await db.add_reminder(ctx.author.id, ctx.channel.id, ctx.guild.id if ctx.guild else None, message, remind_at)
        await ctx.send(embed=embeds.reminder_set_x0(remind_at, message))

    @commands.command(name="reminders")
    async def reminders(self, ctx: commands.Context):
        """View your active reminders."""
        user_reminders = await db.get_user_reminders(ctx.author.id)
        if not user_reminders:
            await ctx.send(embed=embeds.info_x0("You have no active reminders."))
            return

        em = embeds.util_reminders_x0(user_reminders)
        await ctx.send(embed=em)

    @commands.command(name="calc", aliases=["calculator", "math"])
    async def calc(self, ctx: commands.Context, *, expression: str):
        """Evaluate a math expression. Supports: +, -, *, /, **, %"""
        result = uf.evaluate_math(expression)
        await ctx.send(embed=embeds.calculator_x0(expression, result))

    @commands.command(name="embed")
    @commands.has_permissions(manage_messages=True)
    async def create_embed(self, ctx: commands.Context, title: str, *, description: str):
        """Create a custom embed. Usage: embed "Title" Description text here"""
        em = embeds.util_custom_embed_x0(title, description, ctx.author)
        await ctx.send(embed=em)
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass

    @commands.command(name="membercount", aliases=["mc"])
    async def membercount(self, ctx: commands.Context):
        """Show the server's member count."""
        if ctx.guild:
            total = ctx.guild.member_count or 0
            bots = sum(1 for m in ctx.guild.members if m.bot)
            humans = total - bots
            em = embeds.util_membercount_x0(ctx.guild, total, humans, bots)
            await ctx.send(embed=em)

    @commands.command(name="invite")
    async def invite(self, ctx: commands.Context):
        """Get the bot's invite link."""
        em = embeds.util_invite_x0(self.bot.user.id) # type: ignore
        await ctx.send(embed=em)

    @commands.command(name="botinfo", aliases=["bi", "about"])
    async def botinfo(self, ctx: commands.Context):
        """Show information about the bot."""
        em = embeds.util_botinfo_x0(self.bot)
        await ctx.send(embed=em)


async def setup(bot: commands.Bot):
    await bot.add_cog(utilityCommands(bot))
