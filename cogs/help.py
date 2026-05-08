import discord, json
from discord.ext import commands
from views.views import HelpView
from views import embeds

with open('assets/config.json', 'rb') as f:
    config = json.load(f)


class helpCommands(commands.Cog):
    """❓ Paginated help command."""
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"Initialized: {self.__cog_name__}")
        super().__init__()

    def _build_pages(self, ctx: commands.Context) -> list[discord.Embed]:
        prefix = config["prefix"][0]
        pages = []

        bot_name = str(self.bot.user.display_name) if self.bot.user else "Bot"
        bot_avatar_url = self.bot.user.display_avatar.url if self.bot.user else None

        # List all cogs with their descriptions
        cog_list = []
        for cog_name, cog in sorted(self.bot.cogs.items()):
            if cog_name.startswith("_"):
                continue
            doc = cog.__doc__ or ""
            cmd_count = len([c for c in cog.get_commands() if not c.hidden])
            if cmd_count > 0:
                cog_list.append(f"**{doc.strip() or cog_name}** — `{cmd_count}` commands")

        home = embeds.help_home_x0(bot_name, bot_avatar_url, prefix, cog_list, len(self.bot.commands))
        pages.append(home)

        # Category pages
        for cog_name, cog in sorted(self.bot.cogs.items()):
            if cog_name.startswith("_"):
                continue
            cmds = [c for c in cog.get_commands() if not c.hidden]
            if not cmds:
                continue

            command_fields = []
            for cmd in sorted(cmds, key=lambda c: c.name):
                aliases = f" (aliases: {', '.join(cmd.aliases)})" if cmd.aliases else ""
                usage = f"`{prefix}{cmd.qualified_name}"
                if cmd.signature:
                    usage += f" {cmd.signature}"
                usage += "`"

                description = cmd.help or cmd.brief or "No description"
                command_fields.append({
                    "name": f"{usage}{aliases}",
                    "value": description[:100]
                })

            em = embeds.help_category_x0(f"{cog.__doc__ or cog_name}", command_fields, len(pages) + 1, prefix)
            pages.append(em)

        return pages

    @commands.command(name="help", aliases=["h", "commands"])
    async def help_command(self, ctx: commands.Context, *, command_name: str | None = None):
        """Show help for the bot or a specific command."""
        if command_name:
            cmd = self.bot.get_command(command_name)
            if not cmd:
                await ctx.send(embed=embeds.error_x0(f"Command `{command_name}` not found."))
                return

            prefix = config["prefix"][0]
            
            required_perms = False
            for check in cmd.checks:
                check_name = getattr(check, "__qualname__", "")
                if "has_permissions" in check_name:
                    required_perms = True
                    break
            
            cog_name = cmd.cog.__cog_name__ if cmd.cog else None
            em = embeds.help_command_x0(cmd.qualified_name, cmd.signature, cmd.aliases, cmd.help, required_perms, cog_name, prefix)

            await ctx.send(embed=em)
        else:
            pages = self._build_pages(ctx)
            view = HelpView(pages, ctx.author.id)
            await ctx.send(embed=pages[0], view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(helpCommands(bot))
