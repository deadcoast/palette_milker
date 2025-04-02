---
title: "Textual - MouseCapture"
source: "https://textual.textualize.io/events/mouse_capture/"
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

Sent when the mouse has been captured.

- Bubbles
- Verbose

When a mouse has been captured, all further mouse events will be sent to the capturing widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `mouse_position` [¶](https://textual.textualize.io/events/mouse_capture/#textual.events.MouseCapture\(mouse_position\) "Permanent link") | `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | The position of the mouse when captured. | *required* |

## mouse\_position [¶](https://textual.textualize.io/events/mouse_capture/#textual.events.MouseCapture.mouse_position "Permanent link")

```
mouse_position = mouse_position
```

The position of the mouse when captured.

## See also¶

- [capture\_mouse](https://textual.textualize.io/api/widget/#textual.widget.Widget.capture_mouse " capture_mouse")
- [release\_mouse](https://textual.textualize.io/api/widget/#textual.widget.Widget.release_mouse " release_mouse")
- [MouseRelease](https://textual.textualize.io/events/mouse_release/)