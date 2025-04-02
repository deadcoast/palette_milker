---
title: "Textual - Min-width"
source: "https://textual.textualize.io/styles/min_width/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Min-width¶

The `min-width` style sets a minimum width for a widget.

## Syntax¶

```
min-width: <scalar>;
```

The `min-width` style accepts a [`<scalar>`](https://textual.textualize.io/css_types/scalar/) that defines a lower bound for the [`width`](https://textual.textualize.io/styles/width/) of a widget. That is, the width of a widget is never allowed to be under `min-width`.

## Example¶

The example below shows some placeholders with their width set to `50%`. Then, we set `min-width` individually on each placeholder.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import VerticalScroll
from textual.widgets import Placeholder

class MinWidthApp(App):
    CSS_PATH = "min_width.tcss"

    def compose(self):
        yield VerticalScroll(
            Placeholder("min-width: 25%", id="p1"),
            Placeholder("min-width: 75%", id="p2"),
            Placeholder("min-width: 100", id="p3"),
            Placeholder("min-width: 400h", id="p4"),
        )

if __name__ == "__main__":
    app = MinWidthApp()
    app.run()
```

```
VerticalScroll {
    height: 100%;
    width: 100%;
    overflow-x: auto;
}

Placeholder {
    height: 1fr;
    width: 50%;
}

#p1 {
    min-width: 25%;
    
}

#p2 {
    min-width: 75%;
}

#p3 {
    min-width: 100;
}

#p4 {
    min-width: 400h;
}
```

1. This won't affect the placeholder because its width is larger than the minimum width.

## CSS¶

```
/* Set the minimum width to 10 rows */
min-width: 10;

/* Set the minimum width to 25% of the viewport width */
min-width: 25vw;
```

## Python¶

```
# Set the minimum width to 10 rows
widget.styles.min_width = 10

# Set the minimum width to 25% of the viewport width
widget.styles.min_width = "25vw"
```

## See also¶

- [`max-width`](https://textual.textualize.io/styles/max_width/) to set an upper bound on the width of a widget.
- [`width`](https://textual.textualize.io/styles/width/) to set the width of a widget.