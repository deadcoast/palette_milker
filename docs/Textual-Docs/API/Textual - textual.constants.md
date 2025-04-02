---
title: "Textual - textual.constants"
source: "https://textual.textualize.io/api/constants/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.constants

This module contains constants, which may be set in environment variables.

## COLOR\_SYSTEM [¶](https://textual.textualize.io/api/constants/#textual.constants.COLOR_SYSTEM "Permanent link")

```
COLOR_SYSTEM = get_environ('TEXTUAL_COLOR_SYSTEM', 'auto')
```

Force color system override.

## DEBUG [¶](https://textual.textualize.io/api/constants/#textual.constants.DEBUG "Permanent link")

```
DEBUG = _get_environ_bool('TEXTUAL_DEBUG')
```

Enable debug mode.

## DEFAULT\_THEME [¶](https://textual.textualize.io/api/constants/#textual.constants.DEFAULT_THEME "Permanent link")

```
DEFAULT_THEME = get_environ("TEXTUAL_THEME", "textual-dark")
```

Textual theme to make default. More than one theme may be specified in a comma separated list. Textual will use the first theme that exists.

## DEVTOOLS\_HOST [¶](https://textual.textualize.io/api/constants/#textual.constants.DEVTOOLS_HOST "Permanent link")

```
DEVTOOLS_HOST = get_environ(
    "TEXTUAL_DEVTOOLS_HOST", "127.0.0.1"
)
```

The host where textual console is running.

## DEVTOOLS\_PORT [¶](https://textual.textualize.io/api/constants/#textual.constants.DEVTOOLS_PORT "Permanent link")

```
DEVTOOLS_PORT = _get_environ_port(
    "TEXTUAL_DEVTOOLS_PORT", 8081
)
```

Constant with the port that the devtools will connect to.

## DRIVER [¶](https://textual.textualize.io/api/constants/#textual.constants.DRIVER "Permanent link")

```
DRIVER = get_environ('TEXTUAL_DRIVER', None)
```

Import for replacement driver.

## ESCAPE\_DELAY [¶](https://textual.textualize.io/api/constants/#textual.constants.ESCAPE_DELAY "Permanent link")

```
ESCAPE_DELAY = (
    _get_environ_int("ESCDELAY", 100, minimum=1) / 1000.0
)
```

The delay (in seconds) before reporting an escape key (not used if the extend key protocol is available).

## FILTERS [¶](https://textual.textualize.io/api/constants/#textual.constants.FILTERS "Permanent link")

```
FILTERS = get_environ('TEXTUAL_FILTERS', '')
```

A list of filters to apply to renderables.

## LOG\_FILE [¶](https://textual.textualize.io/api/constants/#textual.constants.LOG_FILE "Permanent link")

```
LOG_FILE = get_environ('TEXTUAL_LOG', None)
```

A last resort log file that appends all logs, when devtools isn't working.

## MAX\_FPS [¶](https://textual.textualize.io/api/constants/#textual.constants.MAX_FPS "Permanent link")

```
MAX_FPS = _get_environ_int('TEXTUAL_FPS', 60, minimum=1)
```

Maximum frames per second for updates.

## PRESS [¶](https://textual.textualize.io/api/constants/#textual.constants.PRESS "Permanent link")

```
PRESS = get_environ('TEXTUAL_PRESS', '')
```

Keys to automatically press.

## SCREENSHOT\_DELAY [¶](https://textual.textualize.io/api/constants/#textual.constants.SCREENSHOT_DELAY "Permanent link")

```
SCREENSHOT_DELAY = _get_environ_int(
    "TEXTUAL_SCREENSHOT", -1, minimum=-1
)
```

Seconds delay before taking screenshot, -1 for no screenshot.

## SCREENSHOT\_FILENAME [¶](https://textual.textualize.io/api/constants/#textual.constants.SCREENSHOT_FILENAME "Permanent link")

```
SCREENSHOT_FILENAME = get_environ(
    "TEXTUAL_SCREENSHOT_FILENAME"
)
```

The filename to use for the screenshot.

## SCREENSHOT\_LOCATION [¶](https://textual.textualize.io/api/constants/#textual.constants.SCREENSHOT_LOCATION "Permanent link")

```
SCREENSHOT_LOCATION = get_environ(
    "TEXTUAL_SCREENSHOT_LOCATION"
)
```

The location where screenshots should be written.

## SHOW\_RETURN [¶](https://textual.textualize.io/api/constants/#textual.constants.SHOW_RETURN "Permanent link")

```
SHOW_RETURN = _get_environ_bool('TEXTUAL_SHOW_RETURN')
```

Write the return value on exit.

## SLOW\_THRESHOLD [¶](https://textual.textualize.io/api/constants/#textual.constants.SLOW_THRESHOLD "Permanent link")

```
SLOW_THRESHOLD = _get_environ_int(
    "TEXTUAL_SLOW_THRESHOLD", 500, minimum=100
)
```

The time threshold (in milliseconds) after which a warning is logged if message processing exceeds this duration.

## SMOOTH\_SCROLL [¶](https://textual.textualize.io/api/constants/#textual.constants.SMOOTH_SCROLL "Permanent link")

```
SMOOTH_SCROLL = (
    _get_environ_int("TEXTUAL_SMOOTH_SCROLL", 1) == 1
)
```

Should smooth scrolling be enabled? set `TEXTUAL_SMOOTH_SCROLL=0` to disable smooth

## TEXTUAL\_ANIMATIONS [¶](https://textual.textualize.io/api/constants/#textual.constants.TEXTUAL_ANIMATIONS "Permanent link")

```
TEXTUAL_ANIMATIONS = _get_textual_animations()
```

Determines whether animations run or not.