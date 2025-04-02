---
title: "Textual - textual.coordinate"
source: "https://textual.textualize.io/api/coordinate/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.coordinate

A class to store a coordinate, used by the [DataTable](https://textual.textualize.io/widgets/data_table/#textual.widgets.DataTable " DataTable").

## Coordinate [¶](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

An object representing a row/column coordinate within a grid.

### column [¶](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate.column "Permanent link")

```
column
```

The column of the coordinate within a grid.

### row [¶](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate.row "Permanent link")

```
row
```

The row of the coordinate within a grid.

### down [¶](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate.down "Permanent link")

```
down()
```

Get the coordinate below.

Returns:

| Type | Description |
| --- | --- |
|  | The coordinate below. |

### left [¶](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate.left "Permanent link")

```
left()
```

Get the coordinate to the left.

Returns:

| Type | Description |
| --- | --- |
|  | The coordinate to the left. |

### right [¶](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate.right "Permanent link")

```
right()
```

Get the coordinate to the right.

Returns:

| Type | Description |
| --- | --- |
|  | The coordinate to the right. |

### up [¶](https://textual.textualize.io/api/coordinate/#textual.coordinate.Coordinate.up "Permanent link")

```
up()
```

Get the coordinate above.

Returns:

| Type | Description |
| --- | --- |
|  | The coordinate above. |