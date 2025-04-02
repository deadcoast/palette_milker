---
title: "Textual - Header"
source: "https://textual.textualize.io/widgets/header/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
A simple header widget which docks itself to the top of the parent container.

Note

The application title which is shown in the header is taken from the [`title`](https://textual.textualize.io/api/app/#textual.app.App.title " title") and [`sub_title`](https://textual.textualize.io/api/app/#textual.app.App.sub_title " sub_title") of the application.

- Focusable
- Container

## Example¶

The example below shows an app with a `Header`.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Header

class HeaderApp(App):
    def compose(self) -> ComposeResult:
        yield Header()

if __name__ == "__main__":
    app = HeaderApp()
    app.run()
```

This example shows how to set the text in the `Header` using `App.title` and `App.sub_title`:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Header

class HeaderApp(App):
    def compose(self) -> ComposeResult:
        yield Header()

    def on_mount(self) -> None:
        self.title = "Header Application"
        self.sub_title = "With title and sub-title"

if __name__ == "__main__":
    app = HeaderApp()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `tall` | `bool` | `True` | Whether the `Header` widget is displayed as tall or not. The tall variant is 3 cells tall by default. The non-tall variant is a single cell tall. This can be toggled by clicking on the header. |

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A header widget with icon and clock.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `show_clock` [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header\(show_clock\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the clock should be shown on the right of the header. | `False` |
| ## `name` [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the header widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the header widget in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the header widget. | `None` |
| ## `icon` [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header\(icon\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Single character to use as an icon, or `None` for default. | `None` |
| ## `time_format` [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header\(time_format\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Time format (used by strftime) for clock, or `None` for default. | `None` |

## icon [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header.icon "Permanent link")

```
icon = Reactive('⭘')
```

A character for the icon at the top left.

## screen\_sub\_title [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header.screen_sub_title "Permanent link")

```
screen_sub_title
```

The sub-title that this header will display.

This depends on [`Screen.sub_title`](https://textual.textualize.io/api/screen/#textual.screen.Screen.sub_title " sub_title") and [`App.sub_title`](https://textual.textualize.io/api/app/#textual.app.App.sub_title " sub_title").

## screen\_title [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header.screen_title "Permanent link")

```
screen_title
```

The title that this header will display.

This depends on [`Screen.title`](https://textual.textualize.io/api/screen/#textual.screen.Screen.title " title") and [`App.title`](https://textual.textualize.io/api/app/#textual.app.App.title " title").

## tall [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header.tall "Permanent link")

```
tall = Reactive(False)
```

Set to `True` for a taller header or `False` for a single line header.

## time\_format [¶](https://textual.textualize.io/widgets/header/#textual.widgets.Header.time_format "Permanent link")

```
time_format = Reactive('%X')
```

Time format of the clock.