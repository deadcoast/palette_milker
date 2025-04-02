---
title: "Textual - Click"
source: "https://textual.textualize.io/events/click/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
Bases: `[MouseEvent](https://textual.textualize.io/api/events/#textual.events.MouseEvent " MouseEvent (textual.events.MouseEvent)")`

Sent when a widget is clicked.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `chain` [¶](https://textual.textualize.io/events/click/#textual.events.Click\(chain\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of clicks in the chain. 2 is a double click, 3 is a triple click, etc. | `1` |

## Double & triple clicks¶

The `chain` attribute on the `Click` event can be used to determine the number of clicks that occurred in quick succession. A value of `1` indicates a single click, `2` indicates a double click, and so on.

By default, clicks must occur within 500ms of each other for them to be considered a chain. You can change this value by setting the `CLICK_CHAIN_TIME_THRESHOLD` class variable on your `App` subclass.

See [MouseEvent](https://textual.textualize.io/api/events/#textual.events.MouseEvent " MouseEvent") for the list of properties and methods on the parent class.

## See also¶

- [Enter](https://textual.textualize.io/events/enter/)
- [Leave](https://textual.textualize.io/events/leave/)
- [MouseDown](https://textual.textualize.io/events/mouse_down/)
- [MouseEvent](https://textual.textualize.io/api/events/#textual.events.MouseEvent " MouseEvent")
- [MouseMove](https://textual.textualize.io/events/mouse_move/)
- [MouseScrollDown](https://textual.textualize.io/events/mouse_scroll_down/)
- [MouseScrollUp](https://textual.textualize.io/events/mouse_scroll_up/)
- [MouseUp](https://textual.textualize.io/events/mouse_up/)