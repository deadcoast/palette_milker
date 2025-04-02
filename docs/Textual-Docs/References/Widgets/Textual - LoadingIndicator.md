---
title: "Textual - LoadingIndicator"
source: "https://textual.textualize.io/widgets/loading_indicator/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
Added in version 0.15.0

Displays pulsating dots to indicate when data is being loaded.

- Focusable
- Container

Tip

Widgets have a [`loading`](https://textual.textualize.io/api/widget/#textual.widget.Widget.loading " loading") reactive which you can use to temporarily replace your widget with a `LoadingIndicator`. See the [Loading Indicator](https://textual.textualize.io/guide/widgets/#loading-indicator) section in the Widgets guide for details.

## Example¶

Simple usage example:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import LoadingIndicator

class LoadingApp(App):
    def compose(self) -> ComposeResult:
        yield LoadingIndicator()

if __name__ == "__main__":
    app = LoadingApp()
    app.run()
```

## Changing Indicator Color¶

You can set the color of the loading indicator by setting its `color` style.

Here's how you would do that with CSS:

```
LoadingIndicator {
    color: red;
}
```

## Reactive Attributes¶

This widget has no reactive attributes.

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

Display an animated loading indicator.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the widget. | `None` |
|  | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

```
on_input(event)
```

Prevent all input events from bubbling, thus disabling widgets in a loading state.