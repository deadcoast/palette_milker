---
title: "Textual - Grid-gutter"
source: "https://textual.textualize.io/styles/grid/grid_gutter/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Grid-gutter¶

The `grid-gutter` style sets the size of the gutter in the grid layout. That is, it sets the space between adjacent cells in the grid.

Gutter is only applied *between* the edges of cells. No spacing is added between the edges of the cells and the edges of the container.

Note

This style only affects widgets with `layout: grid`.

## Syntax¶

```
grid-gutter: <integer> [<integer>];
```

The `grid-gutter` style takes one or two [`<integer>`](https://textual.textualize.io/css_types/integer/) that set the length of the gutter along the vertical and horizontal axes. If only one [`<integer>`](https://textual.textualize.io/css_types/integer/) is supplied, it sets the vertical and horizontal gutters. If two are supplied, they set the vertical and horizontal gutters, respectively.

## Example¶

The example below employs a common trick to apply visually consistent spacing around all grid cells.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Grid
from textual.widgets import Label

class MyApp(App):
    CSS_PATH = "grid_gutter.tcss"

    def compose(self):
        yield Grid(
            Label("1"),
            Label("2"),
            Label("3"),
            Label("4"),
            Label("5"),
            Label("6"),
            Label("7"),
            Label("8"),
        )

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

```
Grid {
    grid-size: 2 4;
    grid-gutter: 1 2;  
}

Label {
    border: round white;
    content-align: center middle;
    width: 100%;
    height: 100%;
}
```

1. We set the horizontal gutter to be double the vertical gutter because terminal cells are typically two times taller than they are wide. Thus, the result shows visually consistent spacing around grid cells.

## CSS¶

```
/* Set vertical and horizontal gutters to be the same */
grid-gutter: 5;

/* Set vertical and horizontal gutters separately */
grid-gutter: 1 2;
```

## Python¶

Vertical and horizontal gutters correspond to different Python properties, so they must be set separately:

```
widget.styles.grid_gutter_vertical = "1"
widget.styles.grid_gutter_horizontal = "2"
```