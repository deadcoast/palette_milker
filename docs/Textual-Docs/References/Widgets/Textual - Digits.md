---
title: "Textual - Digits"
source: "https://textual.textualize.io/widgets/digits/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Digits¶

Added in version 0.33.0

A widget to display numerical values in tall multi-line characters.

The digits 0-9 and characters A-F are supported, in addition to `+`, `-`, `^`, `:`, and `×`. Other characters will be displayed in a regular size font.

You can set the text to be displayed in the constructor, or call to change the text after the widget has been mounted.

This widget will respect the [text-align](https://textual.textualize.io/styles/text_align/) rule.

- Focusable
- Container

## Example¶

The following example displays a few digits of Pi:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Digits

class DigitApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #pi {
        border: double green;
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Digits("3.141,592,653,5897", id="pi")

if __name__ == "__main__":
    app = DigitApp()
    app.run()
```

Here's another example which uses `Digits` to display the current time:

<!-- SVG content removed by SVG Remover -->

```
from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits

class ClockApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #clock {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Digits("", id="clock")

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")

if __name__ == "__main__":
    app = ClockApp()
    app.run(inline=True)
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

A widget to display numerical values using a 3x3 grid of unicode characters.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `value` [¶](https://textual.textualize.io/widgets/digits/#textual.widgets.Digits\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Value to display in widget. | `''` |
| ## `name` [¶](https://textual.textualize.io/widgets/digits/#textual.widgets.Digits\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/digits/#textual.widgets.Digits\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/digits/#textual.widgets.Digits\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/digits/#textual.widgets.Digits\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

## value [¶](https://textual.textualize.io/widgets/digits/#textual.widgets.Digits.value "Permanent link")

```
value
```

The current value displayed in the Digits.

## update [¶](https://textual.textualize.io/widgets/digits/#textual.widgets.Digits.update "Permanent link")

```
update()
```

Update the Digits with a new value.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `value` [¶](https://textual.textualize.io/widgets/digits/#textual.widgets.Digits.update\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | New value to display. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)` | If the value isn't a `str`. |