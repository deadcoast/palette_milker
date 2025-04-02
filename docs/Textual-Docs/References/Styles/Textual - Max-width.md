---
title: "Textual - Max-width"
source: "https://textual.textualize.io/styles/max_width/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Max-width¶

The `max-width` style sets a maximum width for a widget.

## Syntax¶

```
max-width: <scalar>;
```

The `max-width` style accepts a [`<scalar>`](https://textual.textualize.io/css_types/scalar/) that defines an upper bound for the [`width`](https://textual.textualize.io/styles/width/) of a widget. That is, the width of a widget is never allowed to exceed `max-width`.

## Example¶

The example below shows some placeholders that were defined to span horizontally from the left edge of the terminal to the right edge. Then, we set `max-width` individually on each placeholder.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import VerticalScroll
from textual.widgets import Placeholder

class MaxWidthApp(App):
    CSS_PATH = "max_width.tcss"

    def compose(self):
        yield VerticalScroll(
            Placeholder("max-width: 50h", id="p1"),
            Placeholder("max-width: 999", id="p2"),
            Placeholder("max-width: 50%", id="p3"),
            Placeholder("max-width: 30", id="p4"),
        )

if __name__ == "__main__":
    app = MaxWidthApp()
    app.run()
```

```
Horizontal {
    height: 100%;
    width: 100%;
}

Placeholder {
    width: 100%;
    height: 1fr;
}

#p1 {
    max-width: 50h;
}

#p2 {
    max-width: 999;  
}

#p3 {
    max-width: 50%;
}

#p4 {
    max-width: 30;
}
```

1. This won't affect the placeholder because its width is less than the maximum width.

## CSS¶

```
/* Set the maximum width to 10 rows */
max-width: 10;

/* Set the maximum width to 25% of the viewport width */
max-width: 25vw;
```

## Python¶

```
# Set the maximum width to 10 rows
widget.styles.max_width = 10

# Set the maximum width to 25% of the viewport width
widget.styles.max_width = "25vw"
```

## See also¶

- [`min-width`](https://textual.textualize.io/styles/min_width/) to set a lower bound on the width of a widget.
- [`width`](https://textual.textualize.io/styles/width/) to set the width of a widget.