---
title: "Textual - Grid-size"
source: "https://textual.textualize.io/styles/grid/grid_size/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Grid-size¶

The `grid-size` style sets the number of columns and rows in a grid layout.

The number of rows can be left unspecified and it will be computed automatically.

Note

This style only affects widgets with `layout: grid`.

## Syntax¶

```
grid-size: <integer> [<integer>];
```

The `grid-size` style takes one or two non-negative [`<integer>`](https://textual.textualize.io/css_types/integer/). The first defines how many columns there are in the grid. If present, the second one sets the number of rows – regardless of the number of children of the grid –, otherwise the number of rows is computed automatically.

## Examples¶

### Columns and rows¶

In the first example, we create a grid with 2 columns and 5 rows, although we do not have enough labels to fill in the whole grid:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Grid
from textual.widgets import Label

class MyApp(App):
    CSS_PATH = "grid_size_both.tcss"

    def compose(self):
        yield Grid(
            Label("1"),
            Label("2"),
            Label("3"),
            Label("4"),
            Label("5"),
        )

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

```
Grid {
    grid-size: 2 4;  
}

Label {
    border: round white;
    content-align: center middle;
    width: 100%;
    height: 100%;
}
```

1. Create a grid with 2 columns and 4 rows.

### Columns only¶

In the second example, we create a grid with 2 columns and however many rows are needed to display all of the grid children:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Grid
from textual.widgets import Label

class MyApp(App):
    CSS_PATH = "grid_size_columns.tcss"

    def compose(self):
        yield Grid(
            Label("1"),
            Label("2"),
            Label("3"),
            Label("4"),
            Label("5"),
        )

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

```
Grid {
    grid-size: 2;  
}

Label {
    border: round white;
    content-align: center middle;
    width: 100%;
    height: 100%;
}
```

1. Create a grid with 2 columns and however many rows.

## CSS¶

```
/* Grid with 3 columns and 5 rows */
grid-size: 3 5;

/* Grid with 4 columns and as many rows as needed */
grid-size: 4;
```

## Python¶

To programmatically change the grid size, the number of rows and columns must be specified separately:

```
widget.styles.grid_size_rows = 3
widget.styles.grid_size_columns = 6
```