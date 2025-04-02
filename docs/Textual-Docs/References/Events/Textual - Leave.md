---
title: "Textual - Leave"
source: "https://textual.textualize.io/events/leave/"
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

Sent when the mouse is moved away from a widget, or if a widget is programmatically disabled while hovered.

Note that this widget bubbles, so a widget may receive Leave events for any child widgets. Check the `node` parameter for the original widget that was previously under the mouse.

- Bubbles
- Verbose

## control [¶](https://textual.textualize.io/events/leave/#textual.events.Leave.control "Permanent link")

```
control
```

Alias for the `node` that was previously under the mouse.

## node [¶](https://textual.textualize.io/events/leave/#textual.events.Leave.node "Permanent link")

```
node = node
```

The node that was previously directly under the mouse.

## See also¶

- [Click](https://textual.textualize.io/events/click/)
- [Enter](https://textual.textualize.io/events/enter/)
- [MouseDown](https://textual.textualize.io/events/mouse_down/)
- [MouseMove](https://textual.textualize.io/events/mouse_move/)
- [MouseScrollDown](https://textual.textualize.io/events/mouse_scroll_down/)
- [MouseScrollUp](https://textual.textualize.io/events/mouse_scroll_up/)
- [MouseUp](https://textual.textualize.io/events/mouse_up/)