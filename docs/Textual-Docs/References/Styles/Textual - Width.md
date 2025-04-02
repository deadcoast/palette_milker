---
title: "Textual - Width"
source: "https://textual.textualize.io/styles/width/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Width¶

The `width` style sets a widget's width.

## Syntax¶

```
width: <scalar>;
```

The style `width` needs a [`<scalar>`](https://textual.textualize.io/css_types/scalar/) to determine the horizontal length of the width. By default, it sets the width of the content area, but if [`box-sizing`](https://textual.textualize.io/styles/box_sizing/) is set to `border-box` it sets the width of the border area.

## Examples¶

### Basic usage¶

This example adds a widget with 50% width of the screen.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widget import Widget

class WidthApp(App):
    CSS_PATH = "width.tcss"

    def compose(self):
        yield Widget()

if __name__ == "__main__":
    app = WidthApp()
    app.run()
```

```
Screen > Widget {
    background: green;
    width: 50%;
    color: white;
}
```

### All width formats¶

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Label, Placeholder, Static

class Ruler(Static):
    def compose(self):
        ruler_text = "····•" * 100
        yield Label(ruler_text)

class WidthComparisonApp(App):
    CSS_PATH = "width_comparison.tcss"

    def compose(self):
        yield Horizontal(
            Placeholder(id="cells"),  
            Placeholder(id="percent"),
            Placeholder(id="w"),
            Placeholder(id="h"),
            Placeholder(id="vw"),
            Placeholder(id="vh"),
            Placeholder(id="auto"),
            Placeholder(id="fr1"),
            Placeholder(id="fr3"),
        )
        yield Ruler()

if __name__ == "__main__":
    app = WidthComparisonApp()
    app.run()
```

1. The id of the placeholder identifies which unit will be used to set the width of the widget.

```
#cells {
    width: 9;      
}
#percent {
    width: 12.5%;  
}
#w {
    width: 10w;    
}
#h {
    width: 25h;    
}
#vw {
    width: 15vw;   
}
#vh {
    width: 25vh;   
}
#auto {
    width: auto;   
}
#fr1 {
    width: 1fr;    
}
#fr3 {
    width: 3fr;    
}

Screen {
    layers: ruler;
}

Ruler {
    layer: ruler;
    dock: bottom;
    overflow: hidden;
    height: 1;
    background: $accent;
}
```

1. This sets the width to 9 columns.
2. This sets the width to 12.5% of the space made available by the container. The container is 80 columns wide, so 12.5% of 80 is 10.
3. This sets the width to 10% of the width of the direct container, which is the `Horizontal` container. Because it expands to fit all of the terminal, the width of the `Horizontal` is 80 and 10% of 80 is 8.
4. This sets the width to 25% of the height of the direct container, which is the `Horizontal` container. Because it expands to fit all of the terminal, the height of the `Horizontal` is 24 and 25% of 24 is 6.
5. This sets the width to 15% of the viewport width, which is 80. 15% of 80 is 12.
6. This sets the width to 25% of the viewport height, which is 24. 25% of 24 is 6.
7. This sets the width of the placeholder to be the optimal size that fits the content without scrolling. Because the content is the string `"#auto"`, the placeholder has its width set to 5.
8. This sets the width to `1fr`, which means this placeholder will have a third of the width of a placeholder with `3fr`.
9. This sets the width to `3fr`, which means this placeholder will have triple the width of a placeholder with `1fr`.

## CSS¶

```
/* Explicit cell width */
width: 10;

/* Percentage width */
width: 50%;

/* Automatic width */
width: auto;
```

## Python¶

```
widget.styles.width = 10
widget.styles.width = "50%
widget.styles.width = "auto"
```

## See also¶

- [`max-width`](https://textual.textualize.io/styles/max_width/) and [`min-width`](https://textual.textualize.io/styles/min_width/) to limit the width of a widget.
- [`height`](https://textual.textualize.io/styles/height/) to set the height of a widget.