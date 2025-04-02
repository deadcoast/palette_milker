---
title: "Textual - Tint"
source: "https://textual.textualize.io/styles/tint/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Tint¶

The `tint` style blends a color with the whole widget.

## Syntax¶

```
tint: <color> [<percentage>];
```

The tint style blends a [`<color>`](https://textual.textualize.io/css_types/color/) with the widget. The color should likely have an *alpha* component (specified directly in the color used or by the optional [`<percentage>`](https://textual.textualize.io/css_types/percentage/)), otherwise the end result will obscure the widget content.

## Example¶

This examples shows a green tint with gradually increasing alpha.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.color import Color
from textual.widgets import Label

class TintApp(App):
    CSS_PATH = "tint.tcss"

    def compose(self):
        color = Color.parse("green")
        for tint_alpha in range(0, 101, 10):
            widget = Label(f"tint: green {tint_alpha}%;")
            widget.styles.tint = color.with_alpha(tint_alpha / 100)  
            yield widget

if __name__ == "__main__":
    app = TintApp()
    app.run()
```

1. We set the tint to a `Color` instance with varying levels of opacity, set through the method [with\_alpha](https://textual.textualize.io/api/color/#textual.color.Color.with_alpha " with_alpha").

```
Label {
    height: 3;
    width: 100%;
    text-style: bold;
    background: white;
    color: black;
    content-align: center middle;
}
```

## CSS¶

```
/* A red tint (could indicate an error) */
tint: red 20%;

/* A green tint */
tint: rgba(0, 200, 0, 0.3);
```

## Python¶

```
# A red tint
from textual.color import Color
widget.styles.tint = Color.parse("red").with_alpha(0.2);

# A green tint
widget.styles.tint = "rgba(0, 200, 0, 0.3)"
```