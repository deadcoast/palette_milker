---
title: "Textual - Grid"
source: "https://textual.textualize.io/styles/grid/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Grid¶

There are a number of styles relating to the Textual `grid` layout.

For an in-depth look at the grid layout, visit the grid [guide](https://textual.textualize.io/guide/layout/#grid).

| Property | Description |
| --- | --- |
| [`column-span`](https://textual.textualize.io/styles/grid/column_span/) | Number of columns a cell spans. |
| [`grid-columns`](https://textual.textualize.io/styles/grid/grid_columns/) | Width of grid columns. |
| [`grid-gutter`](https://textual.textualize.io/styles/grid/grid_gutter/) | Spacing between grid cells. |
| [`grid-rows`](https://textual.textualize.io/styles/grid/grid_rows/) | Height of grid rows. |
| [`grid-size`](https://textual.textualize.io/styles/grid/grid_size/) | Number of columns and rows in the grid layout. |
| [`row-span`](https://textual.textualize.io/styles/grid/row_span/) | Number of rows a cell spans. |

## Syntax¶

```
column-span: <integer>;

grid-columns: <scalar>+;

grid-gutter: <scalar> [<scalar>];

grid-rows: <scalar>+;

grid-size: <integer> [<integer>];

row-span: <integer>;
```

Visit each style's reference page to learn more about how the values are used.

## Example¶

The example below shows all the styles above in action. The `grid-size: 3 4;` declaration sets the grid to 3 columns and 4 rows. The first cell of the grid, tinted magenta, shows a cell spanning multiple rows and columns. The spacing between grid cells is defined by the `grid-gutter` style.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Static

class GridApp(App):
    CSS_PATH = "grid.tcss"

    def compose(self):
        yield Static("Grid cell 1\n\nrow-span: 3;\ncolumn-span: 2;", id="static1")
        yield Static("Grid cell 2", id="static2")
        yield Static("Grid cell 3", id="static3")
        yield Static("Grid cell 4", id="static4")
        yield Static("Grid cell 5", id="static5")
        yield Static("Grid cell 6", id="static6")
        yield Static("Grid cell 7", id="static7")

if __name__ == "__main__":
    app = GridApp()
    app.run()
```

```
Screen {
    layout: grid;
    grid-size: 3 4;
    grid-rows: 1fr;
    grid-columns: 1fr;
    grid-gutter: 1;
}

Static {
    color: auto;
    background: lightblue;
    height: 100%;
    padding: 1 2;
}

#static1 {
    tint: magenta 40%;
    row-span: 3;
    column-span: 2;
}
```

Warning

The styles listed on this page will only work when the layout is `grid`.

## See also¶

- The [grid layout](https://textual.textualize.io/guide/layout/#grid) guide.