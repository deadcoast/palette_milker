---
title: "Textual - Scrollbar-background-active"
source: "https://textual.textualize.io/styles/scrollbar_colors/scrollbar_background_active/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Scrollbar-background-active¶

The `scrollbar-background-active` style sets the background color of the scrollbar when the thumb is being dragged.

## Syntax¶

```
scrollbar-background-active: <color> [<percentage>];
```

`scrollbar-background-active` accepts a [`<color>`](https://textual.textualize.io/css_types/color/) (with an optional opacity level defined by a [`<percentage>`](https://textual.textualize.io/css_types/percentage/)) that is used to define the background color of a scrollbar when its thumb is being dragged.

## Example¶

![](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_colors_demo.gif)

Note

The GIF above has reduced quality to make it easier to load in the documentation. Try running the example yourself with `textual run docs/examples/styles/scrollbars2.py`.

```
from textual.app import App
from textual.widgets import Label

TEXT = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain.
"""

class Scrollbar2App(App):
    CSS_PATH = "scrollbars2.tcss"

    def compose(self):
        yield Label(TEXT * 10)

if __name__ == "__main__":
    app = Scrollbar2App()
    app.run()
```

```
Screen {
    scrollbar-background: blue;
    scrollbar-background-active: red;
    scrollbar-background-hover: purple;
    scrollbar-color: cyan;
    scrollbar-color-active: yellow;
    scrollbar-color-hover: pink;
}
```

## CSS¶

```
scrollbar-background-active: red;
```

## Python¶

```
widget.styles.scrollbar_background_active = "red"
```

## See also¶

- [`scrollbar-background`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_background/) to set the background color of scrollbars.
- [`scrollbar-background-hover`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_color_hover/) to set the scrollbar background color when the mouse pointer is over it.
- [`scrollbar-color-active`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_color_active/) to set the scrollbar color when the scrollbar is being dragged.