---
title: "Textual - Height"
source: "https://textual.textualize.io/styles/height/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Height¶

The `height` style sets a widget's height.

## Syntax¶

```
height: <scalar>;
```

The `height` style needs a [`<scalar>`](https://textual.textualize.io/css_types/scalar/) to determine the vertical length of the widget. By default, it sets the height of the content area, but if [`box-sizing`](https://textual.textualize.io/styles/box_sizing/) is set to `border-box` it sets the height of the border area.

## Examples¶

### Basic usage¶

This examples creates a widget with a height of 50% of the screen.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widget import Widget

class HeightApp(App):
    CSS_PATH = "height.tcss"

    def compose(self):
        yield Widget()

if __name__ == "__main__":
    app = HeightApp()
    app.run()
```

```
Screen > Widget {
    background: green;
    height: 50%;
    color: white;
}
```

### All height formats¶

The next example creates a series of wide widgets with heights set with different units. Open the CSS file tab to see the comments that explain how each height is computed. (The output includes a vertical ruler on the right to make it easier to check the height of each widget.)

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import VerticalScroll
from textual.widgets import Label, Placeholder, Static

class Ruler(Static):
    def compose(self):
        ruler_text = "·\n·\n·\n·\n•\n" * 100
        yield Label(ruler_text)

class HeightComparisonApp(App):
    CSS_PATH = "height_comparison.tcss"

    def compose(self):
        yield VerticalScroll(
            Placeholder(id="cells"),  
            Placeholder(id="percent"),
            Placeholder(id="w"),
            Placeholder(id="h"),
            Placeholder(id="vw"),
            Placeholder(id="vh"),
            Placeholder(id="auto"),
            Placeholder(id="fr1"),
            Placeholder(id="fr2"),
        )
        yield Ruler()

if __name__ == "__main__":
    app = HeightComparisonApp()
    app.run()
```

1. The id of the placeholder identifies which unit will be used to set the height of the widget.

```
#cells {
    height: 2;       
}
#percent {
    height: 12.5%;   
}
#w {
    height: 5w;      
}
#h {
    height: 12.5h;   
}
#vw {
    height: 6.25vw;  
}
#vh {
    height: 12.5vh;  
}
#auto {
    height: auto;    
}
#fr1 {
    height: 1fr;     
}
#fr2 {
    height: 2fr;     
}

Screen {
    layers: ruler;
    overflow: hidden;
}

Ruler {
    layer: ruler;
    dock: right;
    width: 1;
    background: $accent;
}
```

1. This sets the height to 2 lines.
2. This sets the height to 12.5% of the space made available by the container. The container is 24 lines tall, so 12.5% of 24 is 3.
3. This sets the height to 5% of the width of the direct container, which is the `VerticalScroll` container. Because it expands to fit all of the terminal, the width of the `VerticalScroll` is 80 and 5% of 80 is 4.
4. This sets the height to 12.5% of the height of the direct container, which is the `VerticalScroll` container. Because it expands to fit all of the terminal, the height of the `VerticalScroll` is 24 and 12.5% of 24 is 3.
5. This sets the height to 6.25% of the viewport width, which is 80. 6.25% of 80 is 5.
6. This sets the height to 12.5% of the viewport height, which is 24. 12.5% of 24 is 3.
7. This sets the height of the placeholder to be the optimal size that fits the content without scrolling. Because the content only spans one line, the placeholder has its height set to 1.
8. This sets the height to `1fr`, which means this placeholder will have half the height of a placeholder with `2fr`.
9. This sets the height to `2fr`, which means this placeholder will have twice the height of a placeholder with `1fr`.

## CSS¶

```
/* Explicit cell height */
height: 10;

/* Percentage height */
height: 50%;

/* Automatic height */
height: auto
```

## Python¶

```
self.styles.height = 10  # Explicit cell height can be an int
self.styles.height = "50%"
self.styles.height = "auto"
```

## See also¶

- [`max-height`](https://textual.textualize.io/styles/max_height/) and [`min-height`](https://textual.textualize.io/styles/min_height/) to limit the height of a widget.
- [`width`](https://textual.textualize.io/styles/width/) to set the width of a widget.