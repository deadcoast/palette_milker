---
title: "Textual - Focus"
source: "https://textual.textualize.io/events/focus/"
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

Sent when a widget is focussed.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `from_app_focus` [¶](https://textual.textualize.io/events/focus/#textual.events.Focus\(from_app_focus\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if this focus event has been sent because the app itself has regained focus (via an AppFocus event). False if the focus came from within the Textual app (e.g. via the user pressing tab or a programmatic setting of the focused widget). | `False` |

## See also¶

- [AppBlur](https://textual.textualize.io/events/app_blur/)
- [AppFocus](https://textual.textualize.io/events/app_focus/)
- [Blur](https://textual.textualize.io/events/blur/)
- [DescendantBlur](https://textual.textualize.io/events/descendant_blur/)
- [DescendantFocus](https://textual.textualize.io/events/descendant_focus/)