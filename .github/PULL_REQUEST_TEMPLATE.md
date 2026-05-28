## Description

Please include a summary of the change and which issue is fixed. Also include relevant motivation and context.

Fixes # (issue)

## Type of Change

Please delete options that are not relevant:

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?

Please describe the tests that you ran to verify your changes. Provide instructions so we can reproduce.

- [ ] Local bot execution (run `python main.py` with custom `config.json`)
- [ ] Commands executed in test Discord guild (list commands tested):
- [ ] Verified database schema modifications and migrations (if applicable)

## Checklist

Before submitting this Pull Request, please verify:

- [ ] My code follows the guidelines and paradigms defined in [architecture.md](architecture.md).
- [ ] All database queries are asynchronous and located within [database_functions.py](file:///home/rahulb/Projects/general-purpose-discord-bot/functions/database_functions.py).
- [ ] No `discord.Embed` objects are constructed inline; all are imported from [views/embeds.py](file:///home/rahulb/Projects/general-purpose-discord-bot/views/embeds.py).
- [ ] All interactive UI components (Buttons, Dropdowns) are defined in [views/views.py](file:///home/rahulb/Projects/general-purpose-discord-bot/views/views.py).
- [ ] Complex business logic is separated from the Cog commands and placed in the `functions/` directory.
- [ ] My code is properly commented and uses type hints.
- [ ] I have performed a self-review of my own code.
- [ ] I have updated the documentation accordingly.
