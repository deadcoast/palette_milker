---
title: "Textual - Scrollbar-corner-color"
source: "https://textual.textualize.io/styles/scrollbar_colors/scrollbar_corner_color/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Scrollbar-corner-color¶

The `scrollbar-corner-color` style sets the color of the gap between the horizontal and vertical scrollbars.

## Syntax¶

```
scrollbar-corner-color: <color> [<percentage>];
```

`scrollbar-corner-color` accepts a [`<color>`](https://textual.textualize.io/css_types/color/) (with an optional opacity level defined by a [`<percentage>`](https://textual.textualize.io/css_types/percentage/)) that is used to define the color of the gap between the horizontal and vertical scrollbars of a widget.

## Example¶

The example below sets the scrollbar corner (bottom-right corner of the screen) to white.

<!-- SVG content removed by SVG Remover -->

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

class ScrollbarCornerColorApp(App):
    CSS_PATH = "scrollbar_corner_color.tcss"

    def compose(self):
        yield Label(TEXT.replace("\n", " ") + "\n" + TEXT * 10)

if __name__ == "__main__":
    app = ScrollbarCornerColorApp()
    app.run()
```

```
Screen {
    overflow: auto auto;
    scrollbar-corner-color: white;
}
```

## CSS¶

```
scrollbar-corner-color: white;
```

## Python¶

```
widget.styles.scrollbar_corner_color = "white"
```

## See also¶

- [`scrollbar-background`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_background/) to set the background color of scrollbars.
- [`scrollbar-color`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_color/) to set the color of scrollbars.