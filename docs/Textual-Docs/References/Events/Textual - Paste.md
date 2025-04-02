---
title: "Textual - Paste"
source: "https://textual.textualize.io/events/paste/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
Bases: `[Event](https://textual.textualize.io/api/events/#textual.events.Event " Event (textual.events.Event)")`

Event containing text that was pasted into the Textual application. This event will only appear when running in a terminal emulator that supports bracketed paste mode. Textual will enable bracketed pastes when an app starts, and disable it when the app shuts down.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `text` [¶](https://textual.textualize.io/events/paste/#textual.events.Paste\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text that has been pasted. | *required* |

## text [¶](https://textual.textualize.io/events/paste/#textual.events.Paste.text "Permanent link")

```
text = text
```

The text that was pasted.