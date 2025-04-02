---
title: "Textual - Min-height"
source: "https://textual.textualize.io/styles/min_height/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Min-height¶

The `min-height` style sets a minimum height for a widget.

## Syntax¶

```
min-height: <scalar>;
```

The `min-height` style accepts a [`<scalar>`](https://textual.textualize.io/css_types/scalar/) that defines a lower bound for the [`height`](https://textual.textualize.io/styles/height/) of a widget. That is, the height of a widget is never allowed to be under `min-height`.

## Example¶

The example below shows some placeholders with their height set to `50%`. Then, we set `min-height` individually on each placeholder.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Placeholder

class MinHeightApp(App):
    CSS_PATH = "min_height.tcss"

    def compose(self):
        yield Horizontal(
            Placeholder("min-height: 25%", id="p1"),
            Placeholder("min-height: 75%", id="p2"),
            Placeholder("min-height: 30", id="p3"),
            Placeholder("min-height: 40w", id="p4"),
        )

if __name__ == "__main__":
    app = MinHeightApp()
    app.run()
```

```
Horizontal {
    height: 100%;
    width: 100%;
    overflow-y: auto;
}

Placeholder {
    width: 1fr;
    height: 50%;
}

#p1 {
    min-height: 25%;  
}

#p2 {
    min-height: 75%;
}

#p3 {
    min-height: 30;
}

#p4 {
    min-height: 40w;
}
```

1. This won't affect the placeholder because its height is larger than the minimum height.

## CSS¶

```
/* Set the minimum height to 10 rows */
min-height: 10;

/* Set the minimum height to 25% of the viewport height */
min-height: 25vh;
```

## Python¶

```
# Set the minimum height to 10 rows
widget.styles.min_height = 10

# Set the minimum height to 25% of the viewport height
widget.styles.min_height = "25vh"
```

## See also¶

- [`max-height`](https://textual.textualize.io/styles/max_height/) to set an upper bound on the height of a widget.
- [`height`](https://textual.textualize.io/styles/height/) to set the height of a widget.