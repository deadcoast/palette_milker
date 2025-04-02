---
title: "Textual - textual.logging"
source: "https://textual.textualize.io/api/logging/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.logging

A Textual Logging handler.

If there is an active Textual app, then log messages will go via the app (and logged via textual console).

If there is *no* active app, then log messages will go to stderr or stdout, depending on configuration.

## TextualHandler [¶](https://textual.textualize.io/api/logging/#textual.logging.TextualHandler "Permanent link")

```
TextualHandler(=True, =False)
```

Bases: `[Handler](https://docs.python.org/3/library/logging.html#logging.Handler "logging.Handler")`

A Logging handler for Textual apps.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `stderr` [¶](https://textual.textualize.io/api/logging/#textual.logging.TextualHandler\(stderr\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Log to stderr when there is no active app. | `True` |
| ### `stdout` [¶](https://textual.textualize.io/api/logging/#textual.logging.TextualHandler\(stdout\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Log to stdout when there is no active app. | `False` |

### emit [¶](https://textual.textualize.io/api/logging/#textual.logging.TextualHandler.emit "Permanent link")

```
emit(record)
```

Invoked by logging.