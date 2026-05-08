import discord
import time
from functions import database_functions as db


async def process_warning(guild_id: int, user_id: int, moderator_id: int, reason: str) -> tuple[int, int]:
    """Add a warning and return (warning_id, total_warnings_count)."""
    warning_id = await db.add_warning(guild_id, user_id, moderator_id, reason)
    await db.log_mod_action(guild_id, user_id, moderator_id, "warn", reason)
    warnings = await db.get_warnings(guild_id, user_id)
    return warning_id, len(warnings)


async def process_kick(guild_id: int, user_id: int, moderator_id: int, reason: str):
    """Log a kick action."""
    await db.log_mod_action(guild_id, user_id, moderator_id, "kick", reason)


async def process_ban(guild_id: int, user_id: int, moderator_id: int, reason: str, duration: str | None = None):
    """Log a ban action (permanent or temp)."""
    action = "tempban" if duration else "ban"
    await db.log_mod_action(guild_id, user_id, moderator_id, action, reason, duration)


async def process_unban(guild_id: int, user_id: int, moderator_id: int):
    """Log an unban action and remove temp ban entry if exists."""
    await db.log_mod_action(guild_id, user_id, moderator_id, "unban")
    await db.remove_temp_ban(guild_id, user_id)


async def process_mute(guild_id: int, user_id: int, moderator_id: int, reason: str, duration: str):
    """Log a mute action."""
    await db.log_mod_action(guild_id, user_id, moderator_id, "mute", reason, duration)


async def process_unmute(guild_id: int, user_id: int, moderator_id: int):
    """Log an unmute action."""
    await db.log_mod_action(guild_id, user_id, moderator_id, "unmute")


async def send_mod_log(guild: discord.Guild, embed: discord.Embed):
    """Send an embed to the guild's configured mod-log channel."""
    config = await db.get_guild_config(guild.id)
    if config and config.get("mod_log_channel_id"):
        channel = guild.get_channel(config["mod_log_channel_id"])
        if channel and isinstance(channel, discord.TextChannel):
            try:
                await channel.send(embed=embed)
            except discord.Forbidden:
                pass


def build_mod_log_embed(action: str, moderator: discord.Member | discord.User, target: discord.Member | discord.User, reason: str | None = None, duration: str | None = None, extra: str | None = None) -> discord.Embed:
    """Build a standard mod log embed."""
    from views import embeds
    return embeds.mod_log_x0(action, moderator, target, reason, duration, extra)


def format_warnings_list(warnings: list[dict], user: discord.Member | discord.User) -> discord.Embed:
    """Format a list of warnings into a nice embed."""
    from views import embeds
    return embeds.warnings_list_x0(warnings, user)


async def get_moderation_history_embed(guild_id: int, user: discord.Member | discord.User, limit: int = 10) -> discord.Embed:
    """Get a formatted embed of a user's mod history."""
    actions = await db.get_mod_actions(guild_id, user.id, limit)
    from views import embeds
    return embeds.moderation_history_x0(user, actions)
