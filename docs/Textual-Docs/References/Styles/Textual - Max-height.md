---
title: "Textual - Max-height"
source: "https://textual.textualize.io/styles/max_height/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Max-height¶

The `max-height` style sets a maximum height for a widget.

## Syntax¶

```
max-height: <scalar>;
```

The `max-height` style accepts a [`<scalar>`](https://textual.textualize.io/css_types/scalar/) that defines an upper bound for the [`height`](https://textual.textualize.io/styles/height/) of a widget. That is, the height of a widget is never allowed to exceed `max-height`.

## Example¶

The example below shows some placeholders that were defined to span vertically from the top edge of the terminal to the bottom edge. Then, we set `max-height` individually on each placeholder.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Placeholder

class MaxHeightApp(App):
    CSS_PATH = "max_height.tcss"

    def compose(self):
        yield Horizontal(
            Placeholder("max-height: 10w", id="p1"),
            Placeholder("max-height: 999", id="p2"),
            Placeholder("max-height: 50%", id="p3"),
            Placeholder("max-height: 10", id="p4"),
        )

if __name__ == "__main__":
    app = MaxHeightApp()
    app.run()
```

```
Horizontal {
    height: 100%;
    width: 100%;
}

Placeholder {
    height: 100%;
    width: 1fr;
}

#p1 {
    max-height: 10w;
}

#p2 {
    max-height: 999;  
}

#p3 {
    max-height: 50%;
}

#p4 {
    max-height: 10;
}
```

1. This won't affect the placeholder because its height is less than the maximum height.

## CSS¶

```
/* Set the maximum height to 10 rows */
max-height: 10;

/* Set the maximum height to 25% of the viewport height */
max-height: 25vh;
```

## Python¶

```
# Set the maximum height to 10 rows
widget.styles.max_height = 10

# Set the maximum height to 25% of the viewport height
widget.styles.max_height = "25vh"
```

## See also¶

- [`min-height`](https://textual.textualize.io/styles/min_height/) to set a lower bound on the height of a widget.
- [`height`](https://textual.textualize.io/styles/height/) to set the height of a widget.