---
title: "Textual - Enter"
source: "https://textual.textualize.io/events/enter/"
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

Sent when the mouse is moved over a widget.

Note that this event bubbles, so a widget may receive this event when the mouse moves over a child widget. Check the `node` attribute for the widget directly under the mouse.

- Bubbles
- Verbose

## control [¶](https://textual.textualize.io/events/enter/#textual.events.Enter.control "Permanent link")

```
control
```

Alias for the `node` under the mouse.

## node [¶](https://textual.textualize.io/events/enter/#textual.events.Enter.node "Permanent link")

```
node = node
```

The node directly under the mouse.

## See also¶

- [Click](https://textual.textualize.io/events/click/)
- [Leave](https://textual.textualize.io/events/leave/)
- [MouseDown](https://textual.textualize.io/events/mouse_down/)
- [MouseMove](https://textual.textualize.io/events/mouse_move/)
- [MouseScrollDown](https://textual.textualize.io/events/mouse_scroll_down/)
- [MouseScrollUp](https://textual.textualize.io/events/mouse_scroll_up/)
- [MouseUp](https://textual.textualize.io/events/mouse_up/)