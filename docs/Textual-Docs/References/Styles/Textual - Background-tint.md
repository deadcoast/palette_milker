---
title: "Textual - Background-tint"
source: "https://textual.textualize.io/styles/background_tint/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Background-tint¶

The `background-tint` style modifies the background color by tinting (blending) it with a new color.

This style is typically used to subtly change the background of a widget for emphasis. For instance the following would make a focused widget have a slightly lighter background.

```
MyWidget:focus {
    background-tint: white 10%
}
```

The background tint color should typically have less than 100% alpha, in order to modify the background color. If the alpha component is 100% then the tint color will replace the background color entirely.

## Syntax¶

```
background-tint: <color> [<percentage>];
```

The `background-tint` style requires a [`<color>`](https://textual.textualize.io/css_types/color/) optionally followed by [`<percentage>`](https://textual.textualize.io/css_types/percentage/) to specify the color's opacity (clamped between `0%` and `100%`).

## Examples¶

### Basic usage¶

This example shows background tint applied with alpha from 0 to 100%.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Label

class BackgroundTintApp(App):
    CSS_PATH = "background_tint.tcss"

    def compose(self) -> ComposeResult:
        with Vertical(id="tint1"):
            yield Label("0%")
        with Vertical(id="tint2"):
            yield Label("25%")
        with Vertical(id="tint3"):
            yield Label("50%")
        with Vertical(id="tint4"):
            yield Label("75%")
        with Vertical(id="tint5"):
            yield Label("100%")

if __name__ == "__main__":
    app = BackgroundTintApp()
    app.run()
```

```
Vertical {
    background: $panel;
    color: auto 90%;
}
#tint1 { background-tint: $foreground 0%; }
#tint2 { background-tint: $foreground 25%; }
#tint3 { background-tint: $foreground 50%; }
#tint4 { background-tint: $foreground 75% }
#tint5 { background-tint: $foreground 100% }
```

## CSS¶

```
/* 10% backgrouhnd tint */
background-tint: blue 10%;

/* 20% RGB color */
background-tint: rgb(100, 120, 200, 0.2);
```

## Python¶

You can use the same syntax as CSS, or explicitly set a `Color` object for finer-grained control.

```
# Set 20% blue background tint
widget.styles.background_tint = "blue 20%"

from textual.color import Color
# Set with a color object
widget.styles.background_tint = Color(120, 60, 100, 0.5)
```

## See also¶

- [`background`](https://textual.textualize.io/styles/background/) to set the background color of a widget.
- [`color`](https://textual.textualize.io/styles/color/) to set the color of text in a widget.