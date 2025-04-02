---
title: "Textual - Scrollbar colors"
source: "https://textual.textualize.io/styles/scrollbar_colors/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Scrollbar colors¶

There are a number of styles to set the colors used in Textual scrollbars. You won't typically need to do this, as the default themes have carefully chosen colors, but you can if you want to.

| Style | Applies to |
| --- | --- |
| [`scrollbar-background`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_background/) | Scrollbar background. |
| [`scrollbar-background-active`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_background_active/) | Scrollbar background when the thumb is being dragged. |
| [`scrollbar-background-hover`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_background_hover/) | Scrollbar background when the mouse is hovering over it. |
| [`scrollbar-color`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_color/) | Scrollbar "thumb" (movable part). |
| [`scrollbar-color-active`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_color_active/) | Scrollbar thumb when it is active (being dragged). |
| [`scrollbar-color-hover`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_color_hover/) | Scrollbar thumb when the mouse is hovering over it. |
| [`scrollbar-corner-color`](https://textual.textualize.io/styles/scrollbar_colors/scrollbar_corner_color/) | The gap between the horizontal and vertical scrollbars. |

## Syntax¶

```
scrollbar-background: <color> [<percentage>];

scrollbar-background-active: <color> [<percentage>];

scrollbar-background-hover: <color> [<percentage>];

scrollbar-color: <color> [<percentage>];

scrollbar-color-active: <color> [<percentage>];

scrollbar-color-hover: <color> [<percentage>];

scrollbar-corner-color: <color> [<percentage>];
```

Visit each style's reference page to learn more about how the values are used.

## Example¶

This example shows two panels that contain oversized text. The right panel sets `scrollbar-background`, `scrollbar-color`, and `scrollbar-corner-color`, and the left panel shows the default colors for comparison.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Horizontal, ScrollableContainer
from textual.widgets import Label

TEXT = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain.
"""

class ScrollbarApp(App):
    CSS_PATH = "scrollbars.tcss"

    def compose(self):
        yield Horizontal(
            ScrollableContainer(Label(TEXT * 10)),
            ScrollableContainer(Label(TEXT * 10), classes="right"),
        )

if __name__ == "__main__":
    app = ScrollbarApp()
    app.run()
```

```
Label {
    width: 150%;
    height: 150%;
}

.right {
    scrollbar-background: red;
    scrollbar-color: green;
    scrollbar-corner-color: blue;
}

Horizontal > ScrollableContainer {
    width: 50%;
}
```