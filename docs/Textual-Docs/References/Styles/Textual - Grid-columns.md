---
title: "Textual - Grid-columns"
source: "https://textual.textualize.io/styles/grid/grid_columns/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Grid-columns¶

The `grid-columns` style allows to define the width of the columns of the grid.

Note

This style only affects widgets with `layout: grid`.

## Syntax¶

```
grid-columns: <scalar>+;
```

The `grid-columns` style takes one or more [`<scalar>`](https://textual.textualize.io/css_types/scalar/) that specify the length of the columns of the grid.

If there are more columns in the grid than scalars specified in `grid-columns`, they are reused cyclically. If the number of [`<scalar>`](https://textual.textualize.io/css_types/scalar/) is in excess, the excess is ignored.

## Example¶

The example below shows a grid with 10 labels laid out in a grid with 2 rows and 5 columns.

We set `grid-columns: 1fr 16 2fr`. Because there are more rows than scalars in the style definition, the scalars will be reused:

- columns 1 and 4 have width `1fr`;
- columns 2 and 5 have width `16`; and
- column 3 has width `2fr`.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Grid
from textual.widgets import Label

class MyApp(App):
    CSS_PATH = "grid_columns.tcss"

    def compose(self):
        yield Grid(
            Label("1fr"),
            Label("width = 16"),
            Label("2fr"),
            Label("1fr"),
            Label("width = 16"),
            Label("1fr"),
            Label("width = 16"),
            Label("2fr"),
            Label("1fr"),
            Label("width = 16"),
        )

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

```
Grid {
    grid-size: 5 2;
    grid-columns: 1fr 16 2fr;
}

Label {
    border: round white;
    content-align-horizontal: center;
    width: 100%;
    height: 100%;
}
```

## CSS¶

```
/* Set all columns to have 50% width */
grid-columns: 50%;

/* Every other column is twice as wide as the first one */
grid-columns: 1fr 2fr;
```

## Python¶

```
grid.styles.grid_columns = "50%"
grid.styles.grid_columns = "1fr 2fr"
```

## See also¶

- [`grid-rows`](https://textual.textualize.io/styles/grid/grid_rows/) to specify the height of the grid rows.