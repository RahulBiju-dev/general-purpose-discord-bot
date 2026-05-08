import discord
import datetime

# ── Main Embeds ────────────────────────────────────────────────────────────

def ping_x0(latency_ms: int) -> discord.Embed:
    em = discord.Embed(description=f"🏓 Pong! **{latency_ms}ms**", colour=discord.Colour.green())
    return em


# ── Help Embeds ────────────────────────────────────────────────────────────

def help_home_x0(bot_name: str, bot_avatar_url: str | None, prefix: str, cog_list: list[str], total_commands: int) -> discord.Embed:
    home = discord.Embed(
        title=f"📖 {bot_name} — Help",
        description=(
            f"Use `{prefix}help <command>` for detailed info on a command.\n"
            f"Use the buttons below to navigate through categories.\n\n"
            f"**Prefix:** `{prefix}` or mention me"
        ),
        colour=discord.Colour.blurple()
    )
    if bot_avatar_url:
        home.set_thumbnail(url=bot_avatar_url)
    home.add_field(name="Categories", value="\n".join(cog_list) if cog_list else "No categories", inline=False)
    home.set_footer(text=f"Page 1 | {total_commands} total commands")
    return home

def help_category_x0(cog_name: str, command_fields: list[dict], page_num: int, prefix: str) -> discord.Embed:
    em = discord.Embed(
        title=cog_name,
        colour=discord.Colour.blurple()
    )
    for field in command_fields:
        em.add_field(name=field["name"], value=field["value"], inline=False)
    em.set_footer(text=f"Page {page_num} | Use {prefix}help <command> for details")
    return em

def help_command_x0(cmd_name: str, signature: str, aliases: list[str], help_desc: str | None, required_perms: bool, cog_name: str | None, prefix: str) -> discord.Embed:
    em = discord.Embed(
        title=f"Command: {cmd_name}",
        colour=discord.Colour.blurple()
    )
    em.add_field(name="Usage", value=f"`{prefix}{cmd_name} {signature}`", inline=False)
    if aliases:
        em.add_field(name="Aliases", value=", ".join(f"`{a}`" for a in aliases), inline=False)
    if help_desc:
        em.add_field(name="Description", value=help_desc, inline=False)
    if required_perms:
        em.add_field(name="Required Permissions", value="Check command decorators", inline=False)
    if cog_name:
        em.set_footer(text=f"Category: {cog_name}")
    return em


# ── Moderation Embeds ──────────────────────────────────────────────────────

def muted_x0(user: discord.Member | discord.User, duration: int) -> discord.Embed:
    em = discord.Embed(description=f"🔇 `{user.name}` was muted for **{duration} hours**.", color=discord.Colour.dark_orange())
    em.set_footer(text=f"User ID: {user.id}")
    return em

def unmuted_x0(user: discord.Member | discord.User) -> discord.Embed:
    em = discord.Embed(description=f"🔊 `{user.name}` was unmuted.", colour=discord.Colour.green())
    em.set_footer(text=f"User ID: {user.id}")
    return em

def muted_dm_x1(moderator: discord.User | discord.Member, duration: int, reason: str) -> discord.Embed:
    em = discord.Embed(title="🔇 You have been muted", description=f"Muted by {moderator.mention} for **{duration} hours**.\n**Reason:** {reason}",  color=discord.Colour.orange())
    return em

def kick_x0(user: discord.Member | discord.User, reason: str) -> discord.Embed:
    em = discord.Embed(description=f"👢 Kicked `{user.name}`\n**Reason:** {reason}", color=discord.Colour.dark_orange())
    em.set_footer(text=f"User ID: {user.id}")
    return em

def kick_dm_x1(moderator: discord.Member | discord.User, reason: str, guildName: str) -> discord.Embed:
    em = discord.Embed(title=f"👢 You have been kicked from {guildName}", description=f"**Reason:** {reason}", color=discord.Colour.yellow())
    em.set_footer(text=f"Kicked by {moderator.name}")
    return em

def ban_x0(user: discord.Member | discord.User) -> discord.Embed:
    em = discord.Embed(description=f"🔨 Banned `{user.name}`", color=discord.Colour.red())
    em.set_footer(text=f"User ID: {user.id}")
    return em

def unban_x0(user: discord.User) -> discord.Embed:
    em = discord.Embed(description=f"✅ Unbanned `{user.name}`", color=discord.Colour.green())
    em.set_footer(text=f"User ID: {user.id}")
    return em

def ban_dm_x1(moderator: discord.User | discord.Member, reason: str, guildName: str) -> discord.Embed:
    em = discord.Embed(title="🔨 You have been banned!", description=f"**Reason:** {reason}", colour=discord.Colour.red())
    em.set_footer(text=f"Banned from {guildName} by {moderator.name}")
    return em

def warn_x0(user: discord.Member | discord.User, warning_id: int, total: int) -> discord.Embed:
    em = discord.Embed(
        description=f"⚠️ {user.mention} has been warned. (Warning #{warning_id})\n**Total warnings:** {total}",
        color=discord.Colour.yellow()
    )
    em.set_footer(text=f"User ID: {user.id}")
    return em

def warn_dm_x1(moderator: discord.User | discord.Member, reason: str, guildName: str) -> discord.Embed:
    em = discord.Embed(title="⚠️ You have been warned!", description=f"**Reason:** {reason}", color=discord.Colour.yellow())
    em.set_footer(text=f"Sent from {guildName}")
    return em

def softban_x0(user: discord.Member | discord.User) -> discord.Embed:
    em = discord.Embed(description=f"🔨 `{user.name}` has been softbanned!", color=discord.Colour.red())
    em.set_footer(text=f"User ID: {user.id}")
    return em

def softban_dm_x1(user: discord.Member | discord.User, guildName: str) -> discord.Embed:
    em = discord.Embed(title=f"🔨 You have been softbanned from {guildName}!", description="Please use a new invite if you wish to re-join.", colour=discord.Colour.red())
    return em

def tempban_x0(user: discord.Member | discord.User, duration: str) -> discord.Embed:
    em = discord.Embed(description=f"🔨 `{user.name}` has been temp-banned for **{duration}**.", color=discord.Colour.dark_red())
    em.set_footer(text=f"User ID: {user.id}")
    return em

def tempban_dm_x1(moderator: discord.User | discord.Member, reason: str, guildName: str, duration: str) -> discord.Embed:
    em = discord.Embed(title=f"🔨 You have been temporarily banned from {guildName}!", description=f"**Duration:** {duration}\n**Reason:** {reason}", colour=discord.Colour.dark_red())
    em.set_footer(text=f"Banned by {moderator.name}")
    return em

def lockchannel_x0() -> discord.Embed:
    em = discord.Embed(description="🔒 This channel has been **locked**.", color=discord.Colour.dark_orange())
    return em

def unlockchannel_x0() -> discord.Embed:
    em = discord.Embed(description="🔓 This channel has been **unlocked**.", color=discord.Colour.green())
    return em

def clearwarnings_x0(user: discord.Member | discord.User, count: int) -> discord.Embed:
    em = discord.Embed(description=f"🧹 Cleared **{count}** warning(s) for {user.mention}.", colour=discord.Colour.green())
    return em

def mod_log_x0(action: str, moderator: discord.Member | discord.User, target: discord.Member | discord.User, reason: str | None = None, duration: str | None = None, extra: str | None = None) -> discord.Embed:
    colours = {
        "warn": discord.Colour.yellow(),
        "mute": discord.Colour.orange(),
        "unmute": discord.Colour.green(),
        "kick": discord.Colour.dark_orange(),
        "ban": discord.Colour.red(),
        "tempban": discord.Colour.dark_red(),
        "unban": discord.Colour.green(),
        "softban": discord.Colour.dark_red(),
    }
    em = discord.Embed(
        title=f"Moderation Action: {action.upper()}",
        colour=colours.get(action, discord.Colour.greyple()),
        timestamp=discord.utils.utcnow()
    )
    em.add_field(name="Target", value=f"{target.mention} (`{target.id}`)", inline=True)
    em.add_field(name="Moderator", value=f"{moderator.mention}", inline=True)
    if reason:
        em.add_field(name="Reason", value=reason, inline=False)
    if duration:
        em.add_field(name="Duration", value=duration, inline=True)
    if extra:
        em.add_field(name="Details", value=extra, inline=False)
    em.set_thumbnail(url=target.display_avatar.url)
    em.set_footer(text=f"User ID: {target.id}")
    return em

def warnings_list_x0(warnings: list[dict], user: discord.Member | discord.User) -> discord.Embed:
    em = discord.Embed(
        title=f"Warnings for {user.display_name}",
        description=f"**Total warnings:** {len(warnings)}",
        colour=discord.Colour.yellow()
    )
    if not warnings:
        em.description = f"{user.display_name} has no warnings."
        em.colour = discord.Colour.green()
        return em

    for w in warnings[:25]:
        em.add_field(
            name=f"Warning #{w['id']}",
            value=f"**Reason:** {w['reason']}\n**By:** <@{w['moderator_id']}>\n**Date:** <t:{w['timestamp']}:R>",
            inline=False
        )
    if len(warnings) > 25:
        em.set_footer(text=f"Showing 25 of {len(warnings)} warnings")
    return em

def moderation_history_x0(user: discord.Member | discord.User, actions: list[dict]) -> discord.Embed:
    em = discord.Embed(
        title=f"Moderation History — {user.display_name}",
        colour=discord.Colour.blurple()
    )
    if not actions:
        em.description = "No moderation history found."
        return em

    for a in actions:
        value = f"**By:** <@{a['moderator_id']}>"
        if a.get("reason"):
            value += f"\n**Reason:** {a['reason']}"
        if a.get("duration"):
            value += f"\n**Duration:** {a['duration']}"
        value += f"\n**Date:** <t:{a['timestamp']}:R>"
        em.add_field(name=f"{a['action'].upper()} (#{a['id']})", value=value, inline=False)
    return em

def delwarn_x0(warning_id: int) -> discord.Embed:
    em = discord.Embed(description=f"🗑️ Deleted warning **#{warning_id}**.", colour=discord.Colour.green())
    return em


# ── Message Profile Embed ─────────────────────────────────────────────────

def mprofile_x0(userData: dict) -> discord.Embed:
    username = userData.get("username", "Unknown")
    em = discord.Embed(
        title=f"{username}'s Server Profile",
        color=discord.Colour.blurple()
    )
    created_at = userData.get("createdAt")
    joined_at = userData.get("joinDate")

    if created_at and isinstance(created_at, datetime.datetime):
        em.add_field(name="Created", value=f"<t:{int(created_at.timestamp())}:R>", inline=True)
    if joined_at and isinstance(joined_at, datetime.datetime):
        em.add_field(name="Joined", value=f"<t:{int(joined_at.timestamp())}:R>", inline=True)

    em.add_field(name="Messages", value=f"**{userData.get('nMessages', 0):,}** messages", inline=False)

    try:
        author_name = userData.get("authorname", "")
        author_avatar = userData.get("authorAvatar")
        if author_name and author_avatar:
            em.set_author(name=str(author_name), icon_url=author_avatar.url)
    except Exception:
        pass

    try:
        server_name = userData.get("servername", "")
        server_icon = userData.get("serverIcon")
        if server_icon:
            em.set_footer(text=str(server_name), icon_url=server_icon.url)
        else:
            em.set_footer(text=str(server_name))
    except Exception:
        pass

    return em


# ── Welcome / Leave Embeds ────────────────────────────────────────────────

def welcome_x0(member: discord.Member, message: str) -> discord.Embed:
    text = message.replace("{user}", member.mention).replace("{server}", member.guild.name).replace("{count}", str(member.guild.member_count))
    em = discord.Embed(
        title="Welcome!",
        description=text,
        colour=discord.Colour.green()
    )
    em.set_thumbnail(url=member.display_avatar.url)
    em.set_footer(text=f"Member #{member.guild.member_count}")
    return em

def leave_x0(member: discord.Member, message: str) -> discord.Embed:
    text = message.replace("{user}", str(member)).replace("{server}", member.guild.name)
    em = discord.Embed(
        title="Goodbye!",
        description=text,
        colour=discord.Colour.dark_grey()
    )
    em.set_thumbnail(url=member.display_avatar.url)
    return em


# ── Leveling Embeds ───────────────────────────────────────────────────────

def levelup_x0(member: discord.Member, level: int) -> discord.Embed:
    em = discord.Embed(
        description=f"🎉 Congratulations {member.mention}! You've reached **Level {level}**!",
        colour=discord.Colour.gold()
    )
    em.set_thumbnail(url=member.display_avatar.url)
    return em

def rank_x0(member: discord.Member, level: int, xp: int, current_xp: int, needed_xp: int, rank: int, progress_bar: str) -> discord.Embed:
    em = discord.Embed(
        title=f"📊 {member.display_name}'s Rank",
        colour=member.colour if member.colour != discord.Colour.default() else discord.Colour.blurple()
    )
    em.set_thumbnail(url=member.display_avatar.url)
    em.add_field(name="Rank", value=f"**#{rank}**", inline=True)
    em.add_field(name="Level", value=f"**{level}**", inline=True)
    em.add_field(name="Total XP", value=f"**{xp:,}**", inline=True)
    em.add_field(name="Progress", value=f"{progress_bar} `{current_xp}/{needed_xp} XP`", inline=False)
    return em

def leaderboard_x0(guild: discord.Guild, entries: list[dict], bot) -> discord.Embed:
    em = discord.Embed(
        title=f"🏆 {guild.name} — Leaderboard",
        colour=discord.Colour.gold()
    )
    if guild.icon:
        em.set_thumbnail(url=guild.icon.url)

    medals = ["🥇", "🥈", "🥉"]
    lines = []
    for i, entry in enumerate(entries):
        medal = medals[i] if i < 3 else f"**#{i+1}**"
        member = guild.get_member(entry["user_id"])
        name = member.display_name if member else f"User {entry['user_id']}"
        lines.append(f"{medal} {name} — Level **{entry['level']}** (`{entry['xp']:,} XP`)")

    em.description = "\n".join(lines) if lines else "No data yet!"
    return em

def level_roles_x0(guild: discord.Guild, roles: list[dict]) -> discord.Embed:
    em = discord.Embed(title="🏆 Level Role Rewards", colour=discord.Colour.gold())
    for lr in roles:
        role = guild.get_role(lr["role_id"])
        role_text = role.mention if role else f"Unknown ({lr['role_id']})"
        em.add_field(name=f"Level {lr['level']}", value=role_text, inline=True)
    return em


# ── Ticket Embeds ─────────────────────────────────────────────────────────

def ticket_commands_x0() -> discord.Embed:
    em = discord.Embed(
        title="🎫 Ticket Commands",
        description=(
            "`ticket setup` — Send the ticket panel\n"
            "`ticket setcategory <category>` — Set ticket category\n"
            "`ticket setlog <channel>` — Set ticket log channel\n"
            "`ticket close` — Close the current ticket\n"
            "`ticket add <user>` — Add a user to this ticket\n"
            "`ticket remove <user>` — Remove a user from this ticket\n"
        ),
        colour=discord.Colour.blurple()
    )
    return em

def ticket_panel_x0() -> discord.Embed:
    em = discord.Embed(
        title="🎫 Support Tickets",
        description="Click the button below to create a new support ticket.\nA private channel will be created for you.",
        colour=discord.Colour.blurple()
    )
    em.set_footer(text="Please describe your issue after the ticket is created.")
    return em

def ticket_created_x0(user: discord.Member) -> discord.Embed:
    em = discord.Embed(
        title="🎫 Ticket Created",
        description=f"Welcome {user.mention}!\n\nPlease describe your issue and a staff member will assist you shortly.\nUse the buttons below to manage this ticket.",
        colour=discord.Colour.green()
    )
    return em

def ticket_closed_x0(closer: discord.Member | discord.User) -> discord.Embed:
    em = discord.Embed(
        description=f"🔒 Ticket closed by {closer.mention}.",
        colour=discord.Colour.red()
    )
    return em


# ── Giveaway Embeds ───────────────────────────────────────────────────────

def giveaway_x0(prize: str, host: discord.Member | discord.User, end_time: int, winners: int) -> discord.Embed:
    em = discord.Embed(
        title="🎉 GIVEAWAY 🎉",
        description=f"**{prize}**\n\nReact with 🎉 to enter!\n\n**Winners:** {winners}\n**Ends:** <t:{end_time}:R> (<t:{end_time}:f>)",
        colour=discord.Colour.gold()
    )
    em.set_footer(text=f"Hosted by {host.display_name}")
    return em

def giveaway_commands_x0() -> discord.Embed:
    em = discord.Embed(
        title="🎉 Giveaway Commands",
        description=(
            "`giveaway start <duration> <winners> <prize>` — Start a giveaway\n"
            "`giveaway end <message_id>` — End a giveaway early\n"
            "`giveaway reroll <message_id>` — Re-roll a giveaway winner\n"
        ),
        colour=discord.Colour.gold()
    )
    return em

def giveaway_ended_x0(prize: str, winners: list[discord.Member], host_id: int) -> discord.Embed:
    if winners:
        winner_text = ", ".join(w.mention for w in winners)
        em = discord.Embed(
            title="🎉 Giveaway Ended!",
            description=f"**Prize:** {prize}\n**Winner(s):** {winner_text}",
            colour=discord.Colour.gold(),
            timestamp=discord.utils.utcnow()
        )
    else:
        em = discord.Embed(
            title="🎉 Giveaway Ended!",
            description=f"**Prize:** {prize}\n**Winner(s):** No valid entries!",
            colour=discord.Colour.dark_grey(),
            timestamp=discord.utils.utcnow()
        )
    em.set_footer(text=f"Hosted by user ID {host_id}")
    return em


# ── Starboard Embed ───────────────────────────────────────────────────────

def starboard_x0(message: discord.Message, star_count: int, emoji: str) -> discord.Embed:
    em = discord.Embed(
        description=message.content or "*[No text content]*",
        colour=discord.Colour.gold(),
        timestamp=message.created_at
    )
    em.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    em.add_field(name="Source", value=f"[Jump to message]({message.jump_url})", inline=False)

    if message.attachments:
        em.set_image(url=message.attachments[0].url)

    em.set_footer(text=f"{emoji} {star_count}")
    return em

def starboard_settings_x0(channel: discord.abc.GuildChannel | None, threshold: int, emoji: str, is_setup: bool) -> discord.Embed:
    em = discord.Embed(title="⭐ Starboard Settings", colour=discord.Colour.gold())
    if is_setup:
        em.add_field(name="Channel", value=channel.mention if channel else "Not set", inline=True)
        em.add_field(name="Threshold", value=str(threshold), inline=True)
        em.add_field(name="Emoji", value=emoji, inline=True)
    else:
        em.description = "Starboard is not set up. Use `starboard setup <channel> [threshold]`."
    return em


# ── Fun Embeds ────────────────────────────────────────────────────────────

def poll_x0(question: str, author: discord.Member | discord.User) -> discord.Embed:
    em = discord.Embed(
        title="📊 Poll",
        description=question,
        colour=discord.Colour.blurple()
    )
    em.set_footer(text=f"Poll by {author.display_name}")
    return em

def eightball_x0(question: str, answer: str) -> discord.Embed:
    em = discord.Embed(colour=discord.Colour.purple())
    em.add_field(name="🎱 Question", value=question, inline=False)
    em.add_field(name="Answer", value=f"**{answer}**", inline=False)
    return em

def fun_coinflip_x0(emoji: str, result: str) -> discord.Embed:
    return discord.Embed(description=f"{emoji} **{result}!**", colour=discord.Colour.gold())

def fun_roll_x0(count: int, sides: int, result_text: str, total: int) -> discord.Embed:
    return discord.Embed(
        title=f"🎲 Rolling {count}d{sides}",
        description=f"Results: {result_text}\n**Total: {total}**",
        colour=discord.Colour.purple()
    )

def fun_rps_x0(choice: str, choice_emoji: str, bot_choice: str, bot_emoji: str, result_msg: str, colour: discord.Colour) -> discord.Embed:
    return discord.Embed(
        title="Rock Paper Scissors",
        description=f"You: {choice_emoji} **{choice.capitalize()}**\nBot: {bot_emoji} **{bot_choice.capitalize()}**\n\n{result_msg}",
        colour=colour
    )

def fun_meme_x0(title: str, url: str, image_url: str, ups: int, subreddit: str) -> discord.Embed:
    em = discord.Embed(
        title=title,
        colour=discord.Colour.random(),
        url=url
    )
    em.set_image(url=image_url)
    em.set_footer(text=f"👍 {ups} | r/{subreddit}")
    return em

def fun_joke_x0(setup: str, punchline: str) -> discord.Embed:
    return discord.Embed(
        title="😂 Joke",
        description=f"**{setup}**\n\n||{punchline}||",
        colour=discord.Colour.random()
    )

def fun_avatar_x0(target: discord.Member | discord.User, requester: discord.Member | discord.User) -> discord.Embed:
    em = discord.Embed(
        title=f"{target.display_name}'s Avatar",
        colour=discord.Colour.blurple()
    )
    em.set_image(url=target.display_avatar.url)
    em.set_footer(text=f"Requested by {requester.display_name}")
    return em

def fun_banner_x0(target: discord.User) -> discord.Embed:
    em = discord.Embed(
        title=f"{target.display_name}'s Banner",
        colour=discord.Colour.blurple()
    )
    if target.banner:
        em.set_image(url=target.banner.url)
    return em

def fun_choose_x0(choice: str) -> discord.Embed:
    return discord.Embed(
        title="🤔 I choose...",
        description=f"**{choice}**",
        colour=discord.Colour.purple()
    )

def fun_rate_x0(thing: str, rating: int, bar: str) -> discord.Embed:
    return discord.Embed(
        title="⭐ Rating",
        description=f"I rate **{thing}** a **{rating}/10**!\n{bar}",
        colour=discord.Colour.gold()
    )


# ── Automod Embeds ────────────────────────────────────────────────────────

def automod_action_x0(member: discord.Member | discord.User, action: str, reason: str) -> discord.Embed:
    em = discord.Embed(
        title="🛡️ AutoMod Action",
        description=f"**User:** {member.mention} (`{member.id}`)\n**Action:** {action}\n**Reason:** {reason}",
        colour=discord.Colour.orange(),
        timestamp=discord.utils.utcnow()
    )
    em.set_thumbnail(url=member.display_avatar.url)
    return em

def automod_settings_x0(config: dict, badwords_count: int) -> discord.Embed:
    em = discord.Embed(title="🛡️ AutoMod Settings", colour=discord.Colour.blurple())
    em.add_field(name="Enabled", value="✅" if config["enabled"] else "❌", inline=True)
    em.add_field(name="Anti-Spam", value="✅" if config["anti_spam"] else "❌", inline=True)
    em.add_field(name="Anti-Invite", value="✅" if config["anti_invite"] else "❌", inline=True)
    em.add_field(name="Anti-Mass Mention", value="✅" if config["anti_massmention"] else "❌", inline=True)
    em.add_field(name="Mass Mention Threshold", value=str(config["massmention_threshold"]), inline=True)
    em.add_field(name="Blocked Words", value=str(badwords_count), inline=True)
    return em

def automod_wordlist_x0(words: list[str]) -> discord.Embed:
    if words:
        word_list = ", ".join(f"`{w}`" for w in words)
        em = discord.Embed(title="🚫 Blocked Words", description=word_list, colour=discord.Colour.red())
    else:
        em = discord.Embed(title="🚫 Blocked Words", description="No blocked words set.", colour=discord.Colour.green())
    return em


# ── Logging Embeds ────────────────────────────────────────────────────────

def message_delete_log(message: discord.Message) -> discord.Embed:
    em = discord.Embed(
        title="🗑️ Message Deleted",
        description=f"**Author:** {message.author.mention}\n**Channel:** {message.channel.mention}\n\n**Content:**\n{message.content[:1000] if message.content else '*[No text]*'}",  # type: ignore
        colour=discord.Colour.red(),
        timestamp=discord.utils.utcnow()
    )
    em.set_footer(text=f"Author ID: {message.author.id} | Message ID: {message.id}")
    return em

def message_edit_log(before: discord.Message, after: discord.Message) -> discord.Embed:
    em = discord.Embed(
        title="✏️ Message Edited",
        description=f"**Author:** {before.author.mention}\n**Channel:** {before.channel.mention}\n\n[Jump to message]({after.jump_url})",  # type: ignore
        colour=discord.Colour.yellow(),
        timestamp=discord.utils.utcnow()
    )
    em.add_field(name="Before", value=before.content[:1024] if before.content else "*[Empty]*", inline=False)
    em.add_field(name="After", value=after.content[:1024] if after.content else "*[Empty]*", inline=False)
    em.set_footer(text=f"Author ID: {before.author.id} | Message ID: {before.id}")
    return em

def member_join_log(member: discord.Member) -> discord.Embed:
    em = discord.Embed(
        title="📥 Member Joined",
        description=f"{member.mention} (`{member.name}`)\n**Account created:** <t:{int(member.created_at.timestamp())}:R>",
        colour=discord.Colour.green(),
        timestamp=discord.utils.utcnow()
    )
    em.set_thumbnail(url=member.display_avatar.url)
    em.set_footer(text=f"Member #{member.guild.member_count} | ID: {member.id}")
    return em

def member_leave_log(member: discord.Member) -> discord.Embed:
    roles = [r.mention for r in member.roles if r != member.guild.default_role]
    roles_text = ", ".join(roles[:15]) if roles else "None"
    em = discord.Embed(
        title="📤 Member Left",
        description=f"{member.mention} (`{member.name}`)\n**Roles:** {roles_text}",
        colour=discord.Colour.dark_grey(),
        timestamp=discord.utils.utcnow()
    )
    em.set_thumbnail(url=member.display_avatar.url)
    em.set_footer(text=f"ID: {member.id}")
    return em

def role_update_log(before: discord.Member, after: discord.Member) -> discord.Embed:
    added = set(after.roles) - set(before.roles)
    removed = set(before.roles) - set(after.roles)
    em = discord.Embed(
        title="🏷️ Role Update",
        description=f"**Member:** {after.mention}",
        colour=discord.Colour.blue(),
        timestamp=discord.utils.utcnow()
    )
    if added:
        em.add_field(name="Added", value=", ".join(r.mention for r in added), inline=False)
    if removed:
        em.add_field(name="Removed", value=", ".join(r.mention for r in removed), inline=False)
    em.set_footer(text=f"ID: {after.id}")
    return em

def voice_log(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState) -> discord.Embed:
    if before.channel is None and after.channel:
        desc = f"🔊 {member.mention} joined **{after.channel.name}**"
        colour = discord.Colour.green()
    elif before.channel and after.channel is None:
        desc = f"🔇 {member.mention} left **{before.channel.name}**"
        colour = discord.Colour.red()
    elif before.channel and after.channel and before.channel != after.channel:
        desc = f"🔀 {member.mention} moved from **{before.channel.name}** → **{after.channel.name}**"
        colour = discord.Colour.yellow()
    else:
        desc = f"🔊 {member.mention} voice state updated"
        colour = discord.Colour.greyple()

    em = discord.Embed(title="🎙️ Voice Update", description=desc, colour=colour, timestamp=discord.utils.utcnow())
    em.set_footer(text=f"ID: {member.id}")
    return em

def channel_create_log(channel: discord.abc.GuildChannel) -> discord.Embed:
    em = discord.Embed(
        title="📁 Channel Created",
        description=f"**Name:** {channel.mention}\n**Type:** {str(channel.type).replace('_', ' ').title()}",
        colour=discord.Colour.green(),
        timestamp=discord.utils.utcnow()
    )
    em.set_footer(text=f"Channel ID: {channel.id}")
    return em

def channel_delete_log(channel: discord.abc.GuildChannel) -> discord.Embed:
    em = discord.Embed(
        title="📁 Channel Deleted",
        description=f"**Name:** #{channel.name}\n**Type:** {str(channel.type).replace('_', ' ').title()}",
        colour=discord.Colour.red(),
        timestamp=discord.utils.utcnow()
    )
    em.set_footer(text=f"Channel ID: {channel.id}")
    return em


# ── Utility Embeds ────────────────────────────────────────────────────────

def afk_set_x0(user: discord.Member | discord.User, reason: str) -> discord.Embed:
    em = discord.Embed(description=f"💤 {user.mention} is now AFK: **{reason}**", colour=discord.Colour.dark_grey())
    return em

def afk_return_x0(user: discord.Member | discord.User) -> discord.Embed:
    em = discord.Embed(description=f"👋 Welcome back, {user.mention}! Your AFK has been removed.", colour=discord.Colour.green())
    return em

def afk_notify_x0(user: discord.Member | discord.User, reason: str, since: int) -> discord.Embed:
    em = discord.Embed(description=f"💤 {user.mention} is AFK: **{reason}** (since <t:{since}:R>)", colour=discord.Colour.dark_grey())
    return em

def reminder_set_x0(remind_at: int, message: str) -> discord.Embed:
    em = discord.Embed(
        description=f"⏰ Reminder set for <t:{remind_at}:R>\n**Reminder:** {message}",
        colour=discord.Colour.blurple()
    )
    return em

def reminder_fire_x0(user_id: int, message: str) -> discord.Embed:
    em = discord.Embed(
        title="⏰ Reminder!",
        description=f"<@{user_id}>, you asked to be reminded:\n\n**{message}**",
        colour=discord.Colour.gold()
    )
    return em

def calculator_x0(expression: str, result: str) -> discord.Embed:
    em = discord.Embed(title="🧮 Calculator", colour=discord.Colour.blurple())
    em.add_field(name="Expression", value=f"`{expression}`", inline=False)
    em.add_field(name="Result", value=f"**{result}**", inline=False)
    return em

def util_channelinfo_x0(target: discord.TextChannel, created_str: str) -> discord.Embed:
    em = discord.Embed(title=f"#{target.name}", colour=discord.Colour.blurple())
    em.add_field(name="ID", value=f"`{target.id}`", inline=True)
    em.add_field(name="Category", value=target.category.name if target.category else "None", inline=True)
    em.add_field(name="Created", value=created_str, inline=True)
    em.add_field(name="Topic", value=target.topic or "No topic set", inline=False)
    em.add_field(name="Slowmode", value=f"{target.slowmode_delay}s" if target.slowmode_delay else "Off", inline=True)
    em.add_field(name="NSFW", value="Yes" if target.is_nsfw() else "No", inline=True)
    em.add_field(name="Position", value=str(target.position), inline=True)
    return em

def util_reminders_x0(user_reminders: list[dict]) -> discord.Embed:
    em = discord.Embed(title="⏰ Your Reminders", colour=discord.Colour.blurple())
    for r in user_reminders[:10]:
        em.add_field(
            name=f"Reminder #{r['id']}",
            value=f"**Message:** {r['message'][:100]}\n**Fires:** <t:{r['remind_at']}:R>",
            inline=False
        )
    if len(user_reminders) > 10:
        em.set_footer(text=f"Showing 10 of {len(user_reminders)} reminders")
    return em

def util_custom_embed_x0(title: str, description: str, author: discord.Member | discord.User) -> discord.Embed:
    em = discord.Embed(title=title, description=description, colour=discord.Colour.blurple())
    em.set_footer(text=f"Sent by {author.display_name}")
    return em

def util_membercount_x0(guild: discord.Guild, total: int, humans: int, bots: int) -> discord.Embed:
    em = discord.Embed(
        title=f"👥 {guild.name} — Members",
        colour=discord.Colour.blurple()
    )
    em.add_field(name="Total", value=f"**{total:,}**", inline=True)
    em.add_field(name="Humans", value=f"**{humans:,}**", inline=True)
    em.add_field(name="Bots", value=f"**{bots:,}**", inline=True)
    return em

def util_invite_x0(bot_id: int) -> discord.Embed:
    em = discord.Embed(
        title="📨 Invite Me!",
        description=f"[Click here to invite me to your server!](https://discord.com/api/oauth2/authorize?client_id={bot_id}&permissions=8&scope=bot)",
        colour=discord.Colour.blurple()
    )
    return em

def util_botinfo_x0(bot) -> discord.Embed:
    em = discord.Embed(
        title=f"ℹ️ About {bot.user.display_name}",
        colour=discord.Colour.blurple()
    )
    em.set_thumbnail(url=bot.user.display_avatar.url)
    em.add_field(name="Servers", value=f"**{len(bot.guilds)}**", inline=True)
    em.add_field(name="Users", value=f"**{len(bot.users):,}**", inline=True)
    em.add_field(name="Latency", value=f"**{int(bot.latency * 1000)}ms**", inline=True)
    em.add_field(name="Commands", value=f"**{len(bot.commands)}**", inline=True)
    em.add_field(name="Library", value="discord.py", inline=True)
    return em

def userinfo_x0(member: discord.Member) -> discord.Embed:
    from functions import utility_functions as uf
    em = discord.Embed(
        title=f"{member.display_name}",
        colour=member.colour if member.colour != discord.Colour.default() else discord.Colour.blurple()
    )
    em.set_thumbnail(url=member.display_avatar.url)

    em.add_field(name="Username", value=f"`{member.name}`", inline=True)
    em.add_field(name="ID", value=f"`{member.id}`", inline=True)
    em.add_field(name="Bot", value="Yes" if member.bot else "No", inline=True)

    em.add_field(name="Created", value=uf.format_timestamp(member.created_at), inline=True)
    if member.joined_at:
        em.add_field(name="Joined", value=uf.format_timestamp(member.joined_at), inline=True)

    if member.premium_since:
        em.add_field(name="Boosting Since", value=uf.format_timestamp(member.premium_since), inline=True)

    roles = [r.mention for r in reversed(member.roles) if r != member.guild.default_role]
    roles_text = ", ".join(roles[:20]) if roles else "None"
    if len(roles) > 20:
        roles_text += f" (+{len(roles) - 20} more)"
    em.add_field(name=f"Roles [{len(roles)}]", value=roles_text, inline=False)

    key_perms = uf.format_permissions(member.guild_permissions)
    if key_perms != "None":
        em.add_field(name="Key Permissions", value=key_perms, inline=False)

    em.set_footer(text=f"User ID: {member.id}")
    return em

def serverinfo_x0(guild: discord.Guild) -> discord.Embed:
    from functions import utility_functions as uf
    em = discord.Embed(
        title=guild.name,
        description=guild.description or "",
        colour=discord.Colour.blurple()
    )

    if guild.icon:
        em.set_thumbnail(url=guild.icon.url)
    if guild.banner:
        em.set_image(url=guild.banner.url)

    em.add_field(name="Owner", value=f"{guild.owner.mention}" if guild.owner else "Unknown", inline=True)
    em.add_field(name="ID", value=f"`{guild.id}`", inline=True)
    em.add_field(name="Created", value=uf.format_timestamp(guild.created_at), inline=True)

    total = guild.member_count or 0
    bots = sum(1 for m in guild.members if m.bot)
    humans = total - bots
    em.add_field(name="Members", value=f"Total: **{uf.format_number(total)}**\nHumans: **{uf.format_number(humans)}**\nBots: **{uf.format_number(bots)}**", inline=True)

    text = len(guild.text_channels)
    voice = len(guild.voice_channels)
    categories = len(guild.categories)
    em.add_field(name="Channels", value=f"Text: **{text}**\nVoice: **{voice}**\nCategories: **{categories}**", inline=True)

    em.add_field(name="Roles", value=f"**{len(guild.roles) - 1}**", inline=True)
    em.add_field(name="Emojis", value=f"**{len(guild.emojis)}**/{guild.emoji_limit}", inline=True)
    em.add_field(name="Boost Level", value=f"Level **{guild.premium_tier}** ({guild.premium_subscription_count} boosts)", inline=True)

    if guild.verification_level:
        em.add_field(name="Verification", value=str(guild.verification_level).capitalize(), inline=True)

    em.set_footer(text=f"Server ID: {guild.id}")
    return em

def snipe_x0(message: discord.Message) -> discord.Embed:
    em = discord.Embed(
        description=message.content[:2000] if message.content else "*[No text content]*",
        colour=discord.Colour.dark_grey(),
        timestamp=message.created_at
    )
    em.set_author(name=message.author.display_name, icon_url=message.author.display_avatar.url)
    if message.attachments:
        em.set_image(url=message.attachments[0].url)
    em.set_footer(text=f"Deleted in #{message.channel}")  # type: ignore
    return em

def editsnipe_x0(before: discord.Message, after: discord.Message) -> discord.Embed:
    em = discord.Embed(
        colour=discord.Colour.yellow(),
        timestamp=after.edited_at or after.created_at
    )
    em.set_author(name=before.author.display_name, icon_url=before.author.display_avatar.url)
    em.add_field(name="Before", value=before.content[:1024] if before.content else "*[Empty]*", inline=False)
    em.add_field(name="After", value=after.content[:1024] if after.content else "*[Empty]*", inline=False)
    em.set_footer(text=f"In #{before.channel}")  # type: ignore
    return em


# ── Custom Commands Embeds ─────────────────────────────────────────────────

def customcmd_help_x0() -> discord.Embed:
    em = discord.Embed(
        title="📋 Custom Commands",
        description=(
            "`customcmd add <name> <response>` — Create a custom command\n"
            "`customcmd remove <name>` — Delete a custom command\n"
            "`customcmd list` — View all custom commands\n"
        ),
        colour=discord.Colour.blurple()
    )
    return em

def customcmd_added_x0(name: str) -> discord.Embed:
    em = discord.Embed(description=f"✅ Custom command `{name}` has been created!", colour=discord.Colour.green())
    return em

def customcmd_removed_x0(name: str) -> discord.Embed:
    em = discord.Embed(description=f"🗑️ Custom command `{name}` has been removed.", colour=discord.Colour.red())
    return em

def customcmd_list_x0(guild_name: str, commands: list[dict]) -> discord.Embed:
    em = discord.Embed(
        title=f"📋 Custom Commands — {guild_name}",
        colour=discord.Colour.blurple()
    )
    if not commands:
        em.description = "No custom commands set up yet."
        return em

    lines = [f"`{c['name']}` — by <@{c['creator_id']}>" for c in commands]
    em.description = "\n".join(lines)
    em.set_footer(text=f"{len(commands)} command(s)")
    return em


# ── Role Embeds ────────────────────────────────────────────────────────────

def role_added_x0(member: discord.Member, role: discord.Role) -> discord.Embed:
    em = discord.Embed(description=f"✅ Added {role.mention} to {member.mention}.", colour=discord.Colour.green())
    return em

def role_removed_x0(member: discord.Member, role: discord.Role) -> discord.Embed:
    em = discord.Embed(description=f"❌ Removed {role.mention} from {member.mention}.", colour=discord.Colour.red())
    return em

def role_created_x0(role: discord.Role) -> discord.Embed:
    em = discord.Embed(
        title="✨ Role Created",
        description=f"{role.mention} (`{role.name}`)",
        colour=role.colour if role.colour != discord.Colour.default() else discord.Colour.blurple()
    )
    em.add_field(name="Color", value=str(role.colour), inline=True)
    em.add_field(name="Hoisted", value="Yes" if role.hoist else "No", inline=True)
    em.add_field(name="Mentionable", value="Yes" if role.mentionable else "No", inline=True)
    em.set_footer(text=f"Role ID: {role.id}")
    return em

def role_deleted_x0(name: str, role_id: int) -> discord.Embed:
    em = discord.Embed(description=f"🗑️ Role **{name}** has been deleted.", colour=discord.Colour.red())
    em.set_footer(text=f"Role ID: {role_id}")
    return em

def role_info_x0(role: discord.Role) -> discord.Embed:
    em = discord.Embed(
        title=f"🏷️ Role Info — {role.name}",
        colour=role.colour if role.colour != discord.Colour.default() else discord.Colour.blurple()
    )
    em.add_field(name="ID", value=f"`{role.id}`", inline=True)
    em.add_field(name="Color", value=str(role.colour), inline=True)
    em.add_field(name="Position", value=str(role.position), inline=True)
    em.add_field(name="Hoisted", value="Yes" if role.hoist else "No", inline=True)
    em.add_field(name="Mentionable", value="Yes" if role.mentionable else "No", inline=True)
    em.add_field(name="Members", value=str(len(role.members)), inline=True)
    em.add_field(name="Created", value=f"<t:{int(role.created_at.timestamp())}:R>", inline=False)
    if role.permissions.value:
        key_perms = [
            name.replace("_", " ").title()
            for name, value in iter(role.permissions)
            if value and name in (
                "administrator", "manage_guild", "manage_channels", "manage_roles",
                "manage_messages", "ban_members", "kick_members", "moderate_members",
                "mention_everyone", "manage_webhooks", "manage_nicknames"
            )
        ]
        if key_perms:
            em.add_field(name="Key Permissions", value=", ".join(key_perms), inline=False)
    return em

def role_members_x0(role: discord.Role) -> discord.Embed:
    members = role.members
    em = discord.Embed(
        title=f"👥 Members with {role.name}",
        colour=role.colour if role.colour != discord.Colour.default() else discord.Colour.blurple()
    )
    if not members:
        em.description = "No members currently have this role."
    else:
        shown = members[:30]
        em.description = " ".join(m.mention for m in shown)
        if len(members) > 30:
            em.set_footer(text=f"Showing 30 of {len(members)} members")
        else:
            em.set_footer(text=f"{len(members)} member(s)")
    return em

def rrole_panel_x0(title: str, description: str, roles: list[discord.Role]) -> discord.Embed:
    em = discord.Embed(title=title, description=description, colour=discord.Colour.blurple())
    role_list = "\n".join(f"• {r.mention}" for r in roles)
    em.add_field(name="Available Roles", value=role_list or "No roles configured.", inline=False)
    em.set_footer(text="Click a button to toggle your role.")
    return em

def roles_list_x0(guild_name: str, total_roles: int, lines: list[str]) -> discord.Embed:
    em = discord.Embed(
        title=f"🏷️ {guild_name} — Roles ({total_roles} total)",
        description="\n".join(lines) if lines else "No roles found.",
        colour=discord.Colour.blurple(),
    )
    if total_roles > 25:
        em.set_footer(text=f"Showing top 25 of {total_roles} roles.")
    return em

def sar_menu_x0(roles: list[discord.Role]) -> discord.Embed:
    em = discord.Embed(
        title="🎭 Self-Assignable Roles",
        colour=discord.Colour.blurple(),
    )
    if roles:
        em.description = "\n".join(f"• {r.mention}" for r in roles)
        em.set_footer(text="Use -sar get <role> to assign a role to yourself.")
    else:
        em.description = "No self-assignable roles are configured yet.\nAdmins can add them with `-sar add <role>`."
    return em


# ── Config Embeds ──────────────────────────────────────────────────────────

def config_set_x0(setting: str, value: str) -> discord.Embed:
    em = discord.Embed(description=f"✅ **{setting}** has been set to {value}.", colour=discord.Colour.green())
    return em

def config_error_x0(message: str) -> discord.Embed:
    em = discord.Embed(description=f"❌ {message}", colour=discord.Colour.red())
    return em

def success_x0(message: str) -> discord.Embed:
    em = discord.Embed(description=f"✅ {message}", colour=discord.Colour.green())
    return em

def error_x0(message: str) -> discord.Embed:
    em = discord.Embed(description=f"❌ {message}", colour=discord.Colour.red())
    return em

def info_x0(message: str) -> discord.Embed:
    em = discord.Embed(description=f"ℹ️ {message}", colour=discord.Colour.blurple())
    return em