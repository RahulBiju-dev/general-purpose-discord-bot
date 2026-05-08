import discord
import re
import datetime
import math


def parse_duration(duration_str: str) -> datetime.timedelta | None:
    """
    Parse a human-readable duration string into a timedelta.
    Supports: 30s, 5m, 2h, 1d, 1w, or combinations like 1d12h.
    """
    pattern = re.compile(r"(\d+)\s*([smhdw])", re.IGNORECASE)
    matches = pattern.findall(duration_str)
    if not matches:
        return None

    total = datetime.timedelta()
    units = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days", "w": "weeks"}

    for value, unit in matches:
        total += datetime.timedelta(**{units[unit.lower()]: int(value)})

    return total if total.total_seconds() > 0 else None


def format_duration(td: datetime.timedelta) -> str:
    """Format a timedelta into a human-readable string."""
    total_seconds = int(td.total_seconds())
    if total_seconds <= 0:
        return "0 seconds"

    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    parts = []
    if days > 0:
        parts.append(f"{days}d")
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if seconds > 0:
        parts.append(f"{seconds}s")

    return " ".join(parts)


def format_timestamp(dt: datetime.datetime) -> str:
    """Format a datetime to a Discord timestamp string."""
    return f"<t:{int(dt.timestamp())}:R>"


def truncate(text: str, max_length: int = 1024) -> str:
    """Truncate text to a maximum length, adding ellipsis if needed."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def format_permissions(permissions: discord.Permissions) -> str:
    """Format a Permissions object into a readable string of key permissions."""
    key_perms = [
        ("Administrator", permissions.administrator),
        ("Manage Server", permissions.manage_guild),
        ("Manage Roles", permissions.manage_roles),
        ("Manage Channels", permissions.manage_channels),
        ("Manage Messages", permissions.manage_messages),
        ("Kick Members", permissions.kick_members),
        ("Ban Members", permissions.ban_members),
        ("Moderate Members", permissions.moderate_members),
        ("Mention Everyone", permissions.mention_everyone),
        ("Manage Webhooks", permissions.manage_webhooks),
    ]
    enabled = [name for name, value in key_perms if value]
    return ", ".join(enabled) if enabled else "None"


def format_number(n: int) -> str:
    """Format a large number with commas."""
    return f"{n:,}"


def safe_div(a: int, b: int) -> float:
    """Safe division to avoid ZeroDivisionError."""
    return a / b if b != 0 else 0.0


def evaluate_math(expression: str) -> str:
    """
    Safely evaluate a basic math expression.
    Supports: +, -, *, /, **, %, sqrt, abs, round.
    """
    # Remove whitespace
    expr = expression.strip()

    # Only allow safe characters
    allowed = set("0123456789+-*/().% ")
    # Also allow some function names
    safe_funcs = {"sqrt": math.sqrt, "abs": abs, "round": round, "pow": pow}

    # Replace function names
    for fname in safe_funcs:
        expr = expr.replace(fname, f"__{fname}__")

    # Validate characters (after function replacement)
    clean = expr.replace("__", "")
    for fname in safe_funcs:
        clean = clean.replace(f"{fname}", "")
    for char in clean:
        if char not in allowed and not char.isalpha():
            return "Error: Invalid character in expression"

    try:
        # Build safe namespace
        namespace = {f"__{k}__": v for k, v in safe_funcs.items()}
        namespace["__builtins__"] = {}
        result = eval(expr, namespace)
        if isinstance(result, float) and result == int(result):
            return str(int(result))
        return str(round(result, 6)) if isinstance(result, float) else str(result)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Error: Invalid expression"



