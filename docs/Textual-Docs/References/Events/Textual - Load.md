---
title: "Textual - Load"
source: "https://textual.textualize.io/events/load/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Load

Bases: `[Event](https://textual.textualize.io/api/events/#textual.events.Event " Event (textual.events.Event)")`

Sent when the App is running but *before* the terminal is in application mode.

Use this event to run any setup that doesn't require any visuals such as loading configuration and binding keys.

- Bubbles
- Verbose

## See also¶

- [Mount](https://textual.textualize.io/events/mount/)