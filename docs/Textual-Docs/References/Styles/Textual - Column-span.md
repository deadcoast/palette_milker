---
title: "Textual - Column-span"
source: "https://textual.textualize.io/styles/grid/column_span/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Column-span¶

The `column-span` style specifies how many columns a widget will span in a grid layout.

Note

This style only affects widgets that are direct children of a widget with `layout: grid`.

## Syntax¶

```
column-span: <integer>;
```

The `column-span` style accepts a single non-negative [`<integer>`](https://textual.textualize.io/css_types/integer/) that quantifies how many columns the given widget spans.

## Example¶

The example below shows a 4 by 4 grid where many placeholders span over several columns.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Grid
from textual.widgets import Placeholder

class MyApp(App):
    CSS_PATH = "column_span.tcss"

    def compose(self):
        yield Grid(
            Placeholder(id="p1"),
            Placeholder(id="p2"),
            Placeholder(id="p3"),
            Placeholder(id="p4"),
            Placeholder(id="p5"),
            Placeholder(id="p6"),
            Placeholder(id="p7"),
        )

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

```
#p1 {
    column-span: 4;
}
#p2 {
    column-span: 3;
}
#p3 {
    column-span: 1;  /* Didn't need to be set explicitly. */
}
#p4 {
    column-span: 2;
}
#p5 {
    column-span: 2;
}
#p6 {
    /* Default value is 1. */
}
#p7 {
    column-span: 3;
}

Grid {
    grid-size: 4 4;
    grid-gutter: 1 2;
}

Placeholder {
    height: 100%;
}
```

## CSS¶

```
column-span: 3;
```

## Python¶

```
widget.styles.column_span = 3
```

## See also¶

- [`row-span`](https://textual.textualize.io/styles/grid/row_span/) to specify how many rows a widget spans.