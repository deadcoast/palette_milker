---
title: "Textual - DataTable"
source: "https://textual.textualize.io/widgets/data_table/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## DataTable¶

A widget to display text in a table. This includes the ability to update data, use a cursor to navigate data, respond to mouse clicks, delete rows or columns, and individually render each cell as a Rich Text renderable. DataTable provides an efficiently displayed and updated table capable for most applications.

Applications may have custom rules for formatting, numbers, repopulating tables after searching or filtering, and responding to selections. The widget emits events to interface with custom logic.

- Focusable
- Container

## Guide¶

### Adding data¶

The following example shows how to fill a table with data. First, we use to include the `lane`, `swimmer`, `country`, and `time` columns in the table. After that, we use the method to insert the rows into the table.

<!-- SVG content removed by SVG Remover --> 

```
from textual.app import App, ComposeResult
from textual.widgets import DataTable

ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]

class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

app = TableApp()
if __name__ == "__main__":
    app.run()
```

To add a single row or column use and , respectively.

#### Styling and justifying cells¶

Cells can contain more than just plain strings - [Rich](https://rich.readthedocs.io/en/stable/introduction.html) renderables such as [`Text`](https://rich.readthedocs.io/en/stable/text.html?highlight=Text#rich-text) are also supported. `Text` objects provide an easy way to style and justify cell content:

<!-- SVG content removed by SVG Remover -->

```
from rich.text import Text

from textual.app import App, ComposeResult
from textual.widgets import DataTable

ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]

class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        for row in ROWS[1:]:
            # Adding styled and justified \`Text\` objects instead of plain strings.
            styled_row = [
                Text(str(cell), style="italic #03AC13", justify="right") for cell in row
            ]
            table.add_row(*styled_row)

app = TableApp()
if __name__ == "__main__":
    app.run()
```

### Keys¶

When adding a row to the table, you can supply a *key* to . A key is a unique identifier for that row. If you don't supply a key, Textual will generate one for you and return it from `add_row`. This key can later be used to reference the row, regardless of its current position in the table.

When working with data from a database, for example, you may wish to set the row `key` to the primary key of the data to ensure uniqueness. The method also accepts a `key` argument and works similarly.

Keys are important because cells in a data table can change location due to factors like row deletion and sorting. Thus, using keys instead of coordinates allows us to refer to data without worrying about its current location in the table.

If you want to change the table based solely on coordinates, you may need to convert that coordinate to a cell key first using the method.

### Cursors¶

A cursor allows navigating within a table with the keyboard or mouse. There are four cursor types: `"cell"` (the default), `"row"`, `"column"`, and `"none"`.

Change the cursor type by assigning to the reactive attribute.  
The coordinate of the cursor is exposed via the reactive attribute.

Using the keyboard, arrow keys, Page Up, Page Down, Home and End move the cursor highlight, emitting a message, then enter selects the cell, emitting a message. If the `cursor_type` is row, then and are emitted, similarly for and .

When moving the mouse over the table, a [`MouseMove`](https://textual.textualize.io/api/events/#textual.events.MouseMove " MouseMove") event is emitted, the cell hovered over is styled, and the reactive attribute is updated. Clicking the mouse then emits the and events.

<!-- SVG content removed by SVG Remover --> 

<!-- SVG content removed by SVG Remover --> 

<!-- SVG content removed by SVG Remover --> 

<!-- SVG content removed by SVG Remover --> 

```
from itertools import cycle

from textual.app import App, ComposeResult
from textual.widgets import DataTable

ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]

cursors = cycle(["column", "row", "cell", "none"])

class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = next(cursors)
        table.zebra_stripes = True
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

    def key_c(self):
        table = self.query_one(DataTable)
        table.cursor_type = next(cursors)

app = TableApp()
if __name__ == "__main__":
    app.run()
```

### Updating data¶

Cells can be updated using the and methods.

### Removing data¶

To remove all data in the table, use the method. To remove individual rows, use . The `remove_row` method accepts a `key` argument, which identifies the row to be removed.

If you wish to remove the row below the cursor in the `DataTable`, use `coordinate_to_cell_key` to get the row key of the row under the current `cursor_coordinate`, then supply this key to `remove_row`:

```
# Get the keys for the row and column under the cursor.
row_key, _ = table.coordinate_to_cell_key(table.cursor_coordinate)
# Supply the row key to \`remove_row\` to delete the row.
table.remove_row(row_key)
```

### Removing columns¶

To remove individual columns, use . The `remove_column` method accepts a `key` argument, which identifies the column to be removed.

You can remove the column below the cursor using the same `coordinate_to_cell_key` method described above:

```
# Get the keys for the row and column under the cursor.
_, column_key = table.coordinate_to_cell_key(table.cursor_coordinate)
# Supply the column key to \`column_row\` to delete the column.
table.remove_column(column_key)
```

You can fix a number of rows and columns in place, keeping them pinned to the top and left of the table respectively. To do this, assign an integer to the `fixed_rows` or `fixed_columns` reactive attributes of the `DataTable`.

<!-- SVG content removed by SVG Remover -->  

```
from textual.app import App, ComposeResult
from textual.widgets import DataTable

class TableApp(App):
    CSS = "DataTable {height: 1fr}"

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.focus()
        table.add_columns("A", "B", "C")
        for number in range(1, 100):
            table.add_row(str(number), str(number * 2), str(number * 3))
        table.fixed_rows = 2
        table.fixed_columns = 1
        table.cursor_type = "row"
        table.zebra_stripes = True

app = TableApp()
if __name__ == "__main__":
    app.run()
```

In the example above, we set `fixed_rows` to `2`, and `fixed_columns` to `1`, meaning the first two rows and the leftmost column do not scroll - they always remain visible as you scroll through the data table.

### Sorting¶

The DataTable rows can be sorted using the method.

There are three methods of using :

- By Column. Pass columns in as parameters to sort by the natural order of one or more columns. Specify a column using either a instance or the `key` you supplied to . For example, `sort("country", "region")` would sort by country, and, when the country values are equal, by region.
- By Key function. Pass a function as the `key` parameter to sort, similar to the [key function parameter](https://docs.python.org/3/howto/sorting.html#key-functions) of Python's [`sorted`](https://docs.python.org/3/library/functions.html#sorted) built-in. The function will be called once per row with a tuple of all row values.
- By both Column and Key function. You can specify which columns to include as parameters to your key function. For example, `sort("hours", "rate", key=lambda h, r: h*r)` passes two values to the key function for each row.

The `reverse` argument reverses the order of your sort. Note that correct sorting may require your key function to undo your formatting.

<!-- SVG content removed by SVG Remover -->

```
from rich.text import Text

from textual.app import App, ComposeResult
from textual.widgets import DataTable, Footer

ROWS = [
    ("lane", "swimmer", "country", "time 1", "time 2"),
    (4, "Joseph Schooling", Text("Singapore", style="italic"), 50.39, 51.84),
    (2, "Michael Phelps", Text("United States", style="italic"), 50.39, 51.84),
    (5, "Chad le Clos", Text("South Africa", style="italic"), 51.14, 51.73),
    (6, "László Cseh", Text("Hungary", style="italic"), 51.14, 51.58),
    (3, "Li Zhuhao", Text("China", style="italic"), 51.26, 51.26),
    (8, "Mehdy Metella", Text("France", style="italic"), 51.58, 52.15),
    (7, "Tom Shields", Text("United States", style="italic"), 51.73, 51.12),
    (1, "Aleksandr Sadovnikov", Text("Russia", style="italic"), 51.84, 50.85),
    (10, "Darren Burns", Text("Scotland", style="italic"), 51.84, 51.55),
]

class TableApp(App):
    BINDINGS = [
        ("a", "sort_by_average_time", "Sort By Average Time"),
        ("n", "sort_by_last_name", "Sort By Last Name"),
        ("c", "sort_by_country", "Sort By Country"),
        ("d", "sort_by_columns", "Sort By Columns (Only)"),
    ]

    current_sorts: set = set()

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        for col in ROWS[0]:
            table.add_column(col, key=col)
        table.add_rows(ROWS[1:])

    def sort_reverse(self, sort_type: str):
        """Determine if \`sort_type\` is ascending or descending."""
        reverse = sort_type in self.current_sorts
        if reverse:
            self.current_sorts.remove(sort_type)
        else:
            self.current_sorts.add(sort_type)
        return reverse

    def action_sort_by_average_time(self) -> None:
        """Sort DataTable by average of times (via a function) and
        passing of column data through positional arguments."""

        def sort_by_average_time_then_last_name(row_data):
            name, *scores = row_data
            return (sum(scores) / len(scores), name.split()[-1])

        table = self.query_one(DataTable)
        table.sort(
            "swimmer",
            "time 1",
            "time 2",
            key=sort_by_average_time_then_last_name,
            reverse=self.sort_reverse("time"),
        )

    def action_sort_by_last_name(self) -> None:
        """Sort DataTable by last name of swimmer (via a lambda)."""
        table = self.query_one(DataTable)
        table.sort(
            "swimmer",
            key=lambda swimmer: swimmer.split()[-1],
            reverse=self.sort_reverse("swimmer"),
        )

    def action_sort_by_country(self) -> None:
        """Sort DataTable by country which is a \`Rich.Text\` object."""
        table = self.query_one(DataTable)
        table.sort(
            "country",
            key=lambda country: country.plain,
            reverse=self.sort_reverse("country"),
        )

    def action_sort_by_columns(self) -> None:
        """Sort DataTable without a key."""
        table = self.query_one(DataTable)
        table.sort("swimmer", "lane", reverse=self.sort_reverse("columns"))

app = TableApp()
if __name__ == "__main__":
    app.run()
```

### Labeled rows¶

A "label" can be attached to a row using the method. This will add an extra column to the left of the table which the cursor cannot interact with. This column is similar to the leftmost column in a spreadsheet containing the row numbers. The example below shows how to attach simple numbered labels to rows.

<!-- SVG content removed by SVG Remover --> 

```
from rich.text import Text

from textual.app import App, ComposeResult
from textual.widgets import DataTable

ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]

class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        for number, row in enumerate(ROWS[1:], start=1):
            label = Text(str(number), style="#B0FC38 italic")
            table.add_row(*row, label=label)

app = TableApp()
if __name__ == "__main__":
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `show_header` | `bool` | `True` | Show the table header |
| `show_row_labels` | `bool` | `True` | Show the row labels (if applicable) |
| `fixed_rows` | `int` | `0` | Number of fixed rows (rows which do not scroll) |
| `fixed_columns` | `int` | `0` | Number of fixed columns (columns which do not scroll) |
| `zebra_stripes` | `bool` | `False` | Style with alternating colors on rows |
| `header_height` | `int` | `1` | Height of header row |
| `show_cursor` | `bool` | `True` | Show the cursor |
| `cursor_type` | `str` | `"cell"` | One of `"cell"`, `"row"`, `"column"`, or `"none"` |
| `cursor_coordinate` | [Coordinate](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate " Coordinate") | `Coordinate(0, 0)` | The current coordinate of the cursor |
| `hover_coordinate` | [Coordinate](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate " Coordinate") | `Coordinate(0, 0)` | The coordinate the *mouse* cursor is above |

## Messages¶

## Bindings¶

The data table widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| enter | Select cells under the cursor. |
| up | Move the cursor up. |
| down | Move the cursor down. |
| right | Move the cursor right. |
| left | Move the cursor left. |
| pageup | Move one page up. |
| pagedown | Move one page down. |
| ctrl+home | Move to the top. |
| ctrl+end | Move to the bottom. |
| home | Move to the home position (leftmost column). |
| end | Move to the end position (rightmost column). |

## Component Classes¶

The data table widget provides the following component classes:

| Class | Description |
| --- | --- |
| `datatable--cursor` | Target the cursor. |
| `datatable--hover` | Target the cells under the hover cursor. |
| `datatable--fixed` | Target fixed columns and fixed rows. |
| `datatable--fixed-cursor` | Target highlighted and fixed columns or header. |
| `datatable--header` | Target the header of the data table. |
| `datatable--header-cursor` | Target cells highlighted by the cursor. |
| `datatable--header-hover` | Target hovered header or row label cells. |
| `datatable--even-row` | Target even rows (row indices start at 0) if zebra\_stripes. |
| `datatable--odd-row` | Target odd rows (row indices start at 0) if zebra\_stripes. |

---

Bases: `[ScrollView](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView " ScrollView (textual.scroll_view.ScrollView)")`, `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`

A tabular widget that contains data.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `show_header` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(show_header\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the table header should be visible or not. | `True` |
| ## `show_row_labels` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(show_row_labels\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the row labels should be shown or not. | `True` |
|  | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of rows, counting from the top, that should be fixed and still visible when the user scrolls down. | `0` |
|  | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of columns, counting from the left, that should be fixed and still visible when the user scrolls right. | `0` |
| ## `zebra_stripes` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(zebra_stripes\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enables or disables a zebra effect applied to the background color of the rows of the table, where alternate colors are styled differently to improve the readability of the table. | `False` |
| ## `header_height` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(header_height\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The height, in number of cells, of the data table header. | `1` |
| ## `show_cursor` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(show_cursor\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the cursor should be visible when navigating the data table or not. | `True` |
| ## `cursor_foreground_priority` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(cursor_foreground_priority\) "Permanent link") | `Literal['renderable', 'css']` | If the data associated with a cell is an arbitrary renderable with a set foreground color, this determines whether that color is prioritized over the cursor component class or not. | `'css'` |
| ## `cursor_background_priority` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(cursor_background_priority\) "Permanent link") | `Literal['renderable', 'css']` | If the data associated with a cell is an arbitrary renderable with a set background color, this determines whether that color is prioritized over the cursor component class or not. | `'renderable'` |
| ## `cursor_type` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(cursor_type\) "Permanent link") |  | The type of cursor to be used when navigating the data table with the keyboard. | `'cell'` |
| ## `cell_padding` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(cell_padding\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of cells added on each side of each column. Setting this value to zero will likely make your table very hard to read. | `1` |
| ## `name` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

## BINDINGS [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding("enter", "select_cursor", "Select", show=False),
    Binding("up", "cursor_up", "Cursor up", show=False),
    Binding(
        "down", "cursor_down", "Cursor down", show=False
    ),
    Binding(
        "right", "cursor_right", "Cursor right", show=False
    ),
    Binding(
        "left", "cursor_left", "Cursor left", show=False
    ),
    Binding("pageup", "page_up", "Page up", show=False),
    Binding(
        "pagedown", "page_down", "Page down", show=False
    ),
    Binding("ctrl+home", "scroll_top", "Top", show=False),
    Binding(
        "ctrl+end", "scroll_bottom", "Bottom", show=False
    ),
    Binding("home", "scroll_home", "Home", show=False),
    Binding("end", "scroll_end", "End", show=False),
]
```

| Key(s) | Description |
| --- | --- |
| enter | Select cells under the cursor. |
| up | Move the cursor up. |
| down | Move the cursor down. |
| right | Move the cursor right. |
| left | Move the cursor left. |
| pageup | Move one page up. |
| pagedown | Move one page down. |
| ctrl+home | Move to the top. |
| ctrl+end | Move to the bottom. |
| home | Move to the home position (leftmost column). |
| end | Move to the end position (rightmost column). |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {
    "datatable--cursor",
    "datatable--hover",
    "datatable--fixed",
    "datatable--fixed-cursor",
    "datatable--header",
    "datatable--header-cursor",
    "datatable--header-hover",
    "datatable--odd-row",
    "datatable--even-row",
}
```

| Class | Description |
| --- | --- |
| `datatable--cursor` | Target the cursor. |
| `datatable--hover` | Target the cells under the hover cursor. |
| `datatable--fixed` | Target fixed columns and fixed rows. |
| `datatable--fixed-cursor` | Target highlighted and fixed columns or header. |
| `datatable--header` | Target the header of the data table. |
| `datatable--header-cursor` | Target cells highlighted by the cursor. |
| `datatable--header-hover` | Target hovered header or row label cells. |
| `datatable--even-row` | Target even rows (row indices start at 0) if zebra\_stripes. |
| `datatable--odd-row` | Target odd rows (row indices start at 0) if zebra\_stripes. |

## cell\_padding [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.cell_padding "Permanent link")

```
cell_padding =
```

Horizontal padding between cells, applied on each side of each cell.

## columns [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.columns "Permanent link")

```
columns = {}
```

Metadata about the columns of the table, indexed by their key.

## cursor\_background\_priority [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.cursor_background_priority "Permanent link")

```
cursor_background_priority =
```

Should we prioritize the cursor component class CSS background or the renderable background in the event where a cell contains a renderable with a background color.

## cursor\_column [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.cursor_column "Permanent link")

```
cursor_column
```

The index of the column that the DataTable cursor is currently on.

## cursor\_coordinate [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.cursor_coordinate "Permanent link")

```
cursor_coordinate = Reactive(
    Coordinate(0, 0), repaint=False, always_update=True
)
```

Current cursor [`Coordinate`](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate " Coordinate").

This can be set programmatically or changed via the method .

## cursor\_foreground\_priority [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.cursor_foreground_priority "Permanent link")

```
cursor_foreground_priority =
```

Should we prioritize the cursor component class CSS foreground or the renderable foreground in the event where a cell contains a renderable with a foreground color.

## cursor\_row [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.cursor_row "Permanent link")

```
cursor_row
```

The index of the row that the DataTable cursor is currently on.

## cursor\_type [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.cursor_type "Permanent link")

```
cursor_type =
```

The type of cursor of the `DataTable`.

```
fixed_columns =
```

The number of columns to fix (prevented from scrolling).

```
fixed_rows =
```

The number of rows to fix (prevented from scrolling).

## header\_height [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.header_height "Permanent link")

```
header_height =
```

The height of the header row (the row of column labels).

## hover\_column [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.hover_column "Permanent link")

```
hover_column
```

The index of the column that the mouse cursor is currently hovering above.

## hover\_coordinate [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.hover_coordinate "Permanent link")

```
hover_coordinate = Reactive(
    Coordinate(0, 0), repaint=False, always_update=True
)
```

The coordinate of the `DataTable` that is being hovered.

## hover\_row [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.hover_row "Permanent link")

```
hover_row
```

The index of the row that the mouse cursor is currently hovering above.

## ordered\_columns [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ordered_columns "Permanent link")

```
ordered_columns
```

The list of Columns in the DataTable, ordered as they appear on screen.

## ordered\_rows [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ordered_rows "Permanent link")

```
ordered_rows
```

The list of Rows in the DataTable, ordered as they appear on screen.

## row\_count [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.row_count "Permanent link")

```
row_count
```

The number of rows currently present in the DataTable.

## rows [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.rows "Permanent link")

```
rows = {}
```

Metadata about the rows of the table, indexed by their key.

## show\_cursor [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.show_cursor "Permanent link")

```
show_cursor =
```

Show/hide both the keyboard and hover cursor.

## show\_header [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.show_header "Permanent link")

```
show_header =
```

Show/hide the header row (the row of column labels).

## show\_row\_labels [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.show_row_labels "Permanent link")

```
show_row_labels =
```

Show/hide the column containing the labels of rows.

## zebra\_stripes [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.zebra_stripes "Permanent link")

```
zebra_stripes =
```

Apply alternating styles, datatable--even-row and datatable-odd-row, to create a zebra effect, e.g., alternating light and dark backgrounds.

## CellHighlighted [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellHighlighted "Permanent link")

```
CellHighlighted(data_table, value, coordinate, cell_key)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when the cursor moves to highlight a new cell.

This is only relevant when the `cursor_type` is `"cell"`. It's also posted when the cell cursor is re-enabled (by setting `show_cursor=True`), and when the cursor type is changed to `"cell"`. Can be handled using `on_data_table_cell_highlighted` in a subclass of `DataTable` or in a parent widget in the DOM.

### cell\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellHighlighted.cell_key "Permanent link")

```
cell_key = cell_key
```

The key for the highlighted cell.

### control [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellHighlighted.control "Permanent link")

```
control
```

Alias for the data table.

### coordinate [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellHighlighted.coordinate "Permanent link")

```
coordinate = coordinate
```

The coordinate of the highlighted cell.

### data\_table [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellHighlighted.data_table "Permanent link")

```
data_table = data_table
```

The data table.

### value [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellHighlighted.value "Permanent link")

```
value = value
```

The value in the highlighted cell.

## CellSelected [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellSelected "Permanent link")

```
CellSelected(data_table, value, coordinate, cell_key)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted by the `DataTable` widget when a cell is selected.

This is only relevant when the `cursor_type` is `"cell"`. Can be handled using `on_data_table_cell_selected` in a subclass of `DataTable` or in a parent widget in the DOM.

### cell\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellSelected.cell_key "Permanent link")

```
cell_key = cell_key
```

The key for the selected cell.

### control [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellSelected.control "Permanent link")

```
control
```

Alias for the data table.

### coordinate [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellSelected.coordinate "Permanent link")

```
coordinate = coordinate
```

The coordinate of the cell that was selected.

### data\_table [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellSelected.data_table "Permanent link")

```
data_table = data_table
```

The data table.

### value [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.CellSelected.value "Permanent link")

```
value = value
```

The value in the cell that was selected.

## ColumnHighlighted [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnHighlighted "Permanent link")

```
ColumnHighlighted(data_table, cursor_column, column_key)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when a column is highlighted.

This message is only posted when the `cursor_type` is set to `"column"`. Can be handled using `on_data_table_column_highlighted` in a subclass of `DataTable` or in a parent widget in the DOM.

### column\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnHighlighted.column_key "Permanent link")

```
column_key = column_key
```

The key of the column that was highlighted.

### control [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnHighlighted.control "Permanent link")

```
control
```

Alias for the data table.

### cursor\_column [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnHighlighted.cursor_column "Permanent link")

```
cursor_column = cursor_column
```

The x-coordinate of the column that was highlighted.

### data\_table [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnHighlighted.data_table "Permanent link")

```
data_table = data_table
```

The data table.

## ColumnSelected [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnSelected "Permanent link")

```
ColumnSelected(data_table, cursor_column, column_key)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when a column is selected.

This message is only posted when the `cursor_type` is set to `"column"`. Can be handled using `on_data_table_column_selected` in a subclass of `DataTable` or in a parent widget in the DOM.

### column\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnSelected.column_key "Permanent link")

```
column_key = column_key
```

The key of the column that was selected.

### control [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnSelected.control "Permanent link")

```
control
```

Alias for the data table.

### cursor\_column [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnSelected.cursor_column "Permanent link")

```
cursor_column = cursor_column
```

The x-coordinate of the column that was selected.

### data\_table [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.ColumnSelected.data_table "Permanent link")

```
data_table = data_table
```

The data table.

## HeaderSelected [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.HeaderSelected "Permanent link")

```
HeaderSelected(data_table, column_key, column_index, label)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when a column header/label is clicked.

### column\_index [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.HeaderSelected.column_index "Permanent link")

```
column_index = column_index
```

The index for the column.

### column\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.HeaderSelected.column_key "Permanent link")

```
column_key = column_key
```

The key for the column.

### control [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.HeaderSelected.control "Permanent link")

```
control
```

Alias for the data table.

### data\_table [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.HeaderSelected.data_table "Permanent link")

```
data_table = data_table
```

The data table.

### label [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.HeaderSelected.label "Permanent link")

```
label = label
```

The text of the label.

## RowHighlighted [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowHighlighted "Permanent link")

```
RowHighlighted(data_table, cursor_row, row_key)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when a row is highlighted.

This message is only posted when the `cursor_type` is set to `"row"`. Can be handled using `on_data_table_row_highlighted` in a subclass of `DataTable` or in a parent widget in the DOM.

### control [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowHighlighted.control "Permanent link")

```
control
```

Alias for the data table.

### cursor\_row [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowHighlighted.cursor_row "Permanent link")

```
cursor_row = cursor_row
```

The y-coordinate of the cursor that highlighted the row.

### data\_table [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowHighlighted.data_table "Permanent link")

```
data_table = data_table
```

The data table.

### row\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowHighlighted.row_key "Permanent link")

```
row_key = row_key
```

The key of the row that was highlighted.

## RowLabelSelected [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowLabelSelected "Permanent link")

```
RowLabelSelected(data_table, row_key, row_index, label)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when a row label is clicked.

### control [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowLabelSelected.control "Permanent link")

```
control
```

Alias for the data table.

### data\_table [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowLabelSelected.data_table "Permanent link")

```
data_table = data_table
```

The data table.

### label [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowLabelSelected.label "Permanent link")

```
label = label
```

The text of the label.

### row\_index [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowLabelSelected.row_index "Permanent link")

```
row_index = row_index
```

The index for the column.

### row\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowLabelSelected.row_key "Permanent link")

```
row_key = row_key
```

The key for the column.

## RowSelected [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowSelected "Permanent link")

```
RowSelected(data_table, cursor_row, row_key)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when a row is selected.

This message is only posted when the `cursor_type` is set to `"row"`. Can be handled using `on_data_table_row_selected` in a subclass of `DataTable` or in a parent widget in the DOM.

### control [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowSelected.control "Permanent link")

```
control
```

Alias for the data table.

### cursor\_row [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowSelected.cursor_row "Permanent link")

```
cursor_row = cursor_row
```

The y-coordinate of the cursor that made the selection.

### data\_table [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowSelected.data_table "Permanent link")

```
data_table = data_table
```

The data table.

### row\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.RowSelected.row_key "Permanent link")

```
row_key = row_key
```

The key of the row that was selected.

## action\_page\_down [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.action_page_down "Permanent link")

```
action_page_down()
```

Move the cursor one page down.

## action\_page\_left [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.action_page_left "Permanent link")

```
action_page_left()
```

Move the cursor one page left.

## action\_page\_right [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.action_page_right "Permanent link")

```
action_page_right()
```

Move the cursor one page right.

## action\_page\_up [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.action_page_up "Permanent link")

```
action_page_up()
```

Move the cursor one page up.

## action\_scroll\_bottom [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.action_scroll_bottom "Permanent link")

```
action_scroll_bottom()
```

Move the cursor and scroll to the bottom.

## action\_scroll\_end [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.action_scroll_end "Permanent link")

```
action_scroll_end()
```

Move the cursor and scroll to the rightmost column.

## action\_scroll\_home [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.action_scroll_home "Permanent link")

```
action_scroll_home()
```

Move the cursor and scroll to the leftmost column.

## action\_scroll\_top [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.action_scroll_top "Permanent link")

```
action_scroll_top()
```

Move the cursor and scroll to the top.

## add\_column [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_column "Permanent link")

```
add_column(, *, =None, =None, =None)
```

Add a column to the table.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `label` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_column\(label\) "Permanent link") | `TextType` | A str or Text object containing the label (shown top of column). | *required* |
| ### `width` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_column\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | Width of the column in cells or None to fit content. | `None` |
| ### `key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_column\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A key which uniquely identifies this column. If None, it will be generated for you. | `None` |
| ### `default` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_column\(default\) "Permanent link") | ` \| None` | The value to insert into pre-existing rows. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | Uniquely identifies this column. Can be used to retrieve this column regardless of its current location in the DataTable (it could have moved after being added due to sorting/insertion/deletion of other columns). |

## add\_columns [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_columns "Permanent link")

```
add_columns(*)
```

Add a number of columns.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `*labels` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_columns\(*labels\) "Permanent link") | `TextType` | Column headers. | `()` |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of the keys for the columns that were added. See the `add_column` method docstring for more information on how these keys are used. |

## add\_row [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_row "Permanent link")

```
add_row(*, =1, =None, =None)
```

Add a row at the bottom of the DataTable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `*cells` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_row\(*cells\) "Permanent link") |  | Positional arguments should contain cell data. | `()` |
| ### `height` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_row\(height\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The height of a row (in lines). Use `None` to auto-detect the optimal height. | `1` |
| ### `key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_row\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A key which uniquely identifies this row. If None, it will be generated for you and returned. | `None` |
| ### `label` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_row\(label\) "Permanent link") | `TextType \| None` | The label for the row. Will be displayed to the left if supplied. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | Unique identifier for this row. Can be used to retrieve this row regardless of its current location in the DataTable (it could have moved after being added due to sorting or insertion/deletion of other rows). |

## add\_rows [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_rows "Permanent link")

```
add_rows()
```

Add a number of rows at the bottom of the DataTable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `rows` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.add_rows\(rows\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]]` | Iterable of rows. A row is an iterable of cells. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of the keys for the rows that were added. See the `add_row` method docstring for more information on how these keys are used. |

## clear [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.clear "Permanent link")

```
clear(=False)
```

Clear the table.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `columns` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.clear\(columns\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Also clear the columns. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `DataTable` instance. |

## coordinate\_to\_cell\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.coordinate_to_cell_key "Permanent link")

```
coordinate_to_cell_key()
```

Return the key for the cell currently occupying this coordinate.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `coordinate` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.coordinate_to_cell_key\(coordinate\) "Permanent link") | `[Coordinate](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate " Coordinate (textual.coordinate.Coordinate)")` | The coordinate to exam the current cell key of. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The key of the cell currently occupying this coordinate. |

Raises:

| Type | Description |
| --- | --- |
|  | If the coordinate is not valid. |

## get\_cell [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_cell "Permanent link")

```
get_cell(, )
```

Given a row key and column key, return the value of the corresponding cell.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_cell\(row_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The row key of the cell. | *required* |
| ### `column_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_cell\(column_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The column key of the cell. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The value of the cell identified by the row and column keys. |

## get\_cell\_at [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_cell_at "Permanent link")

```
get_cell_at()
```

Get the value from the cell occupying the given coordinate.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `coordinate` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_cell_at\(coordinate\) "Permanent link") | `[Coordinate](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate " Coordinate (textual.coordinate.Coordinate)")` | The coordinate to retrieve the value from. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The value of the cell at the coordinate. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is no cell with the given coordinate. |

## get\_cell\_coordinate [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_cell_coordinate "Permanent link")

```
get_cell_coordinate(, )
```

Given a row key and column key, return the corresponding cell coordinate.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_cell_coordinate\(row_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The row key of the cell. | *required* |
| ### `column_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_cell_coordinate\(column_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The column key of the cell. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Coordinate](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate " Coordinate (textual.coordinate.Coordinate)")` | The current coordinate of the cell identified by the row and column keys. |

Raises:

| Type | Description |
| --- | --- |
|  | If the specified cell does not exist. |

## get\_column [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_column "Permanent link")

```
get_column()
```

Get the values from the column identified by the given column key.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `column_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_column\(column_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The key of the column. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | A generator which yields the cells in the column. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is no column corresponding to the key. |

## get\_column\_at [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_column_at "Permanent link")

```
get_column_at()
```

Get the values from the column at a given index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `column_index` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_column_at\(column_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the column. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | A generator which yields the cells in the column. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is no column with the given index. |

## get\_column\_index [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_column_index "Permanent link")

```
get_column_index()
```

Return the current index for the column identified by column\_key.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `column_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_column_index\(column_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The column key to find the current index of. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The current index of the specified column key. |

Raises:

| Type | Description |
| --- | --- |
|  | If the column key does not exist. |

## get\_row [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_row "Permanent link")

```
get_row()
```

Get the values from the row identified by the given row key.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_row\(row_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The key of the row. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of the values contained within the row. |

Raises:

| Type | Description |
| --- | --- |
|  | When there is no row corresponding to the key. |

## get\_row\_at [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_row_at "Permanent link")

```
get_row_at()
```

Get the values from the cells in a row at a given index. This will return the values from a row based on the rows *current position* in the table.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_index` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_row_at\(row_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the row. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of the values contained in the row. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is no row with the given index. |

## get\_row\_height [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_row_height "Permanent link")

```
get_row_height()
```

Given a row key, return the height of that row in terminal cells.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_row_height\(row_key\) "Permanent link") |  | The key of the row. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The height of the row, measured in terminal character cells. |

## get\_row\_index [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_row_index "Permanent link")

```
get_row_index()
```

Return the current index for the row identified by row\_key.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.get_row_index\(row_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The row key to find the current index of. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The current index of the specified row key. |

Raises:

| Type | Description |
| --- | --- |
|  | If the row key does not exist. |

## is\_valid\_column\_index [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.is_valid_column_index "Permanent link")

```
is_valid_column_index()
```

Return a boolean indicating whether the column\_index is within table bounds.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `column_index` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.is_valid_column_index\(column_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The column index to check. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the column index is within the bounds of the table. |

## is\_valid\_coordinate [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.is_valid_coordinate "Permanent link")

```
is_valid_coordinate()
```

Return a boolean indicating whether the given coordinate is valid.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `coordinate` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.is_valid_coordinate\(coordinate\) "Permanent link") | `[Coordinate](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate " Coordinate (textual.coordinate.Coordinate)")` | The coordinate to validate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the coordinate is within the bounds of the table. |

## is\_valid\_row\_index [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.is_valid_row_index "Permanent link")

```
is_valid_row_index()
```

Return a boolean indicating whether the row\_index is within table bounds.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_index` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.is_valid_row_index\(row_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The row index to check. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the row index is within the bounds of the table. |

## move\_cursor [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.move_cursor "Permanent link")

```
move_cursor(
    *, =None, =None, =False, =True
)
```

Move the cursor to the given position.

Example
```
datatable = app.query_one(DataTable)
datatable.move_cursor(row=4, column=6)
# datatable.cursor_coordinate == Coordinate(4, 6)
datatable.move_cursor(row=3)
# datatable.cursor_coordinate == Coordinate(3, 6)
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.move_cursor\(row\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The new row to move the cursor to. | `None` |
| ### `column` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.move_cursor\(column\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The new column to move the cursor to. | `None` |
| ### `animate` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.move_cursor\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to animate the change of coordinates. | `False` |
| ### `scroll` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.move_cursor\(scroll\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Scroll the cursor into view after moving. | `True` |

## refresh\_column [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.refresh_column "Permanent link")

```
refresh_column()
```

Refresh the column at the given index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `column_index` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.refresh_column\(column_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the column to refresh. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `DataTable` instance. |

## refresh\_coordinate [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.refresh_coordinate "Permanent link")

```
refresh_coordinate()
```

Refresh the cell at a coordinate.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `coordinate` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.refresh_coordinate\(coordinate\) "Permanent link") | `[Coordinate](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate " Coordinate (textual.coordinate.Coordinate)")` | The coordinate to refresh. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `DataTable` instance. |

## refresh\_row [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.refresh_row "Permanent link")

```
refresh_row()
```

Refresh the row at the given index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_index` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.refresh_row\(row_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the row to refresh. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `DataTable` instance. |

## remove\_column [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.remove_column "Permanent link")

```
remove_column()
```

Remove a column (identified by a key) from the DataTable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `column_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.remove_column\(column_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The key identifying the column to remove. | *required* |

Raises:

| Type | Description |
| --- | --- |
|  | If the column key does not exist. |

## remove\_row [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.remove_row "Permanent link")

```
remove_row()
```

Remove a row (identified by a key) from the DataTable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.remove_row\(row_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The key identifying the row to remove. | *required* |

Raises:

| Type | Description |
| --- | --- |
|  | If the row key does not exist. |

## sort [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.sort "Permanent link")

```
sort(*columns, =None, =False)
```

Sort the rows in the `DataTable` by one or more column keys or a key function (or other callable). If both columns and a key function are specified, only data from those columns will sent to the key function.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `columns` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.sort\(columns\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | One or more columns to sort by the values in. | `()` |
| ### `key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.sort\(key\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] \| None` | A function (or other callable) that returns a key to use for sorting purposes. | `None` |
| ### `reverse` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.sort\(reverse\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, the sort order will be reversed. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `DataTable` instance. |

## update\_cell [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.update_cell "Permanent link")

```
update_cell(
    , , , *, =False
)
```

Update the cell identified by the specified row key and column key.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.update_cell\(row_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The key identifying the row. | *required* |
| ### `column_key` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.update_cell\(column_key\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The key identifying the column. | *required* |
| ### `value` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.update_cell\(value\) "Permanent link") |  | The new value to put inside the cell. | *required* |
| ### `update_width` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.update_cell\(update_width\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to resize the column width to accommodate for the new cell content. | `False` |

Raises:

| Type | Description |
| --- | --- |
|  | When the supplied `row_key` and `column_key` cannot be found in the table. |

## update\_cell\_at [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.update_cell_at "Permanent link")

```
update_cell_at(, , *, =False)
```

Update the content inside the cell currently occupying the given coordinate.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `coordinate` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.update_cell_at\(coordinate\) "Permanent link") | `[Coordinate](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate " Coordinate (textual.coordinate.Coordinate)")` | The coordinate to update the cell at. | *required* |
| ### `value` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.update_cell_at\(value\) "Permanent link") |  | The new value to place inside the cell. | *required* |
| ### `update_width` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable.update_cell_at\(update_width\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to resize the column width to accommodate for the new cell content. | `False` |

## textual.widgets.data\_table [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table "Permanent link")

### CellType [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.CellType "Permanent link")

```
CellType = TypeVar('CellType')
```

Type used for cells in the DataTable.

### CursorType [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.CursorType "Permanent link")

```
CursorType = Literal['cell', 'row', 'column', 'none']
```

The valid types of cursors for .

### CellDoesNotExist [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.CellDoesNotExist "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

The cell key/index was invalid.

Raised when the coordinates or cell key provided does not exist in the DataTable (e.g. out of bounds index, invalid key)

### CellKey [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.CellKey "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

A unique identifier for a cell in the DataTable.

A cell key is a `(row_key, column_key)` tuple.

Even if the cell changes visual location (i.e. moves to a different coordinate in the table), this key can still be used to retrieve it, regardless of where it currently is.

#### column\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.CellKey.column_key "Permanent link")

```
column_key
```

The key of this cell's column.

#### row\_key [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.CellKey.row_key "Permanent link")

```
row_key
```

The key of this cell's row.

### Column [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.Column "Permanent link")

```
Column(
    key, label, width=0, content_width=0, auto_width=False
)
```

Metadata for a column in the DataTable.

#### get\_render\_width [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.Column.get_render_width "Permanent link")

```
get_render_width()
```

Width, in cells, required to render the column with padding included.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `data_table` [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.Column.get_render_width\(data_table\) "Permanent link") | `[[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]` | The data table where the column will be rendered. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The width, in cells, required to render the column with padding included. |

### ColumnDoesNotExist [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.ColumnDoesNotExist "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when the column index or column key provided does not exist in the DataTable (e.g. out of bounds index, invalid key)

### ColumnKey [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.ColumnKey "Permanent link")

```
ColumnKey(value=None)
```

Bases:

Uniquely identifies a column in the DataTable.

Even if the visual location of the column changes due to sorting or other modifications, a key will always refer to the same column.

### DuplicateKey [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.DuplicateKey "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

The key supplied already exists.

Raised when the RowKey or ColumnKey provided already refers to an existing row or column in the DataTable. Keys must be unique.

### Row [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.Row "Permanent link")

```
Row(key, height, label=None, auto_height=False)
```

Metadata for a row in the DataTable.

### RowDoesNotExist [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.RowDoesNotExist "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when the row index or row key provided does not exist in the DataTable (e.g. out of bounds index, invalid key)

### RowKey [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.RowKey "Permanent link")

```
RowKey(value=None)
```

Bases:

Uniquely identifies a row in the DataTable.

Even if the visual location of the row changes due to sorting or other modifications, a key will always refer to the same row.

### StringKey [¶](https://textual.textualize.io/widgets/data_table/#textual.widgets.data_table.StringKey "Permanent link")

```
StringKey(value=None)
```

An object used as a key in a mapping.

It can optionally wrap a string, and lookups into a map using the object behave the same as lookups using the string itself.