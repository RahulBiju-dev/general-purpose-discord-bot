# Contributing to General Purpose Discord Bot (GPDB)

Thank you for your interest in contributing to GPDB! We welcome contributions of all kinds, including bug fixes, new features, documentation improvements, and feedback.

To ensure a smooth collaboration process and maintain codebase quality, please follow the guidelines outlined below.

---

## 🛠️ Local Environment Setup

1. **Fork & Clone the Repository**
   Fork the repository on GitHub and clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/general-purpose-discord-bot.git
   cd general-purpose-discord-bot
   ```

2. **Set Up a Virtual Environment**
   We recommend using a Python virtual environment to manage dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**
   Copy/create your configuration file at `assets/config.json`:
   ```json
   {
       "prefix": ["-"],
       "token": "YOUR_DISCORD_BOT_TOKEN",
       "owners": [YOUR_DISCORD_USER_ID],
       "default_color": "#5865F2",
       "extensions": [
           "moderation",
           "help",
           "utility"
       ]
   }
   ```
   *Note: Never commit `config.json` containing actual secrets or tokens. It is gitignored by default.*

5. **Run the Bot**
   ```bash
   python main.py
   ```

---

## 🏗️ Codebase Architecture & Standards

We enforce a strict layered architecture to ensure code is modular, clean, and easily extensible. Before writing any code, **you must read and fully understand [architecture.md](architecture.md)**.

### Key Architectural Guidelines:
*   **Cogs (`cogs/`)**: All commands and event listeners must reside in a Cog class within the `cogs/` directory. No commands or complex listeners should be added directly to `main.py`.
*   **Views & Embeds (`views/`)**:
    *   **Embeds** must not be constructed inline inside cogs. Define all embed factories in [views/embeds.py](file:///home/rahulb/Projects/general-purpose-discord-bot/views/embeds.py).
    *   **UI Views** (buttons, dropdowns, etc.) must reside in [views/views.py](file:///home/rahulb/Projects/general-purpose-discord-bot/views/views.py).
*   **Database Access (`functions/database_functions.py`)**: All database interaction (SQL queries, insertions, table setup) must go through this single file. No other file should directly import `aiosqlite` or run database queries.
*   **Feature Logic (`functions/`)**: Complex or large processing logic must be extracted from the cog and placed in a dedicated `<feature>_functions.py` file within the `functions/` directory.

### Naming Conventions:
*   **Cogs**: Named in camelCase ending in `Commands` (e.g., `moderationCommands`). Cog docstrings must start with an emoji and a short description (e.g., `"""🛡️ Moderation commands."""`).
*   **Files**: All python files should use lowercase snake_case (e.g., `customcommands.py`, `database_functions.py`).
*   **Embeds**: Named in the format `<action>_x<tier>` where `x0` is for public channels, and `x1` is for DMs.
*   **Database Functions**: All operations must be asynchronous (`async def`).

---

## 📝 Coding Style

*   Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines.
*   Use explicit type annotations for function parameters and return types where possible.
*   Keep functions focused and modular.
*   Ensure all new commands are documented and provide user-friendly error handling or feedback.

---

## 🚀 Pull Request Lifecycle

1. **Create a Branch**
   Always work on a separate branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b bugfix/issue-description
   ```

2. **Commit Guidelines**
   Keep commit messages descriptive and structured:
   *   `feat: add new XP role rewards system`
   *   `fix: resolve database lock during concurrent giveaway entry`
   *   `docs: update installation instructions in README`

3. **Verify Your Changes**
   *   Ensure the code builds and runs locally without errors.
   *   Verify new commands in a test Discord guild.
   *   Verify database tables and indexes are updated properly if schema changes are introduced.

4. **Submit a Pull Request**
   *   Push your branch to GitHub and open a Pull Request (PR) against our `main` branch.
   *   Fill out the Pull Request template completely.
   *   Ensure that all checks pass and the architecture standards are met.
