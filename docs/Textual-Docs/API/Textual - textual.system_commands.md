---
title: "Textual - textual.system_commands"
source: "https://textual.textualize.io/api/system_commands_source/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.system\_commands

This module contains `SystemCommands`, a command palette command provider for Textual system commands.

This is a simple command provider that makes the most obvious application actions available via the [command palette](https://textual.textualize.io/api/command/#textual.command.CommandPalette " CommandPalette").

Note

The App base class installs this automatically.

## SystemCommandsProvider [¶](https://textual.textualize.io/api/system_commands_source/#textual.system_commands.SystemCommandsProvider "Permanent link")

```
SystemCommandsProvider(screen, match_style=None)
```

Bases: `[Provider](https://textual.textualize.io/api/command/#textual.command.Provider " Provider (textual.command.Provider)")`

A [source](https://textual.textualize.io/api/command/#textual.command.Provider " Provider") of command palette commands that run app-wide tasks.

Used by default in [`App.COMMANDS`](https://textual.textualize.io/api/app/#textual.app.App.COMMANDS " COMMANDS").

### discover [¶](https://textual.textualize.io/api/system_commands_source/#textual.system_commands.SystemCommandsProvider.discover "Permanent link")

```
discover()
```

Handle a request for the discovery commands for this provider.

Yields:

| Type | Description |
| --- | --- |
| `[Hits](https://textual.textualize.io/api/command/#textual.command.Hits " Hits (textual.command.Hits)")` | Commands that can be discovered. |

### search [¶](https://textual.textualize.io/api/system_commands_source/#textual.system_commands.SystemCommandsProvider.search "Permanent link")

```
search()
```

Handle a request to search for system commands that match the query.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `query` [¶](https://textual.textualize.io/api/system_commands_source/#textual.system_commands.SystemCommandsProvider.search\(query\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The user input to be matched. | *required* |

Yields:

| Type | Description |
| --- | --- |
| `[Hits](https://textual.textualize.io/api/command/#textual.command.Hits " Hits (textual.command.Hits)")` | Command hits for use in the command palette. |