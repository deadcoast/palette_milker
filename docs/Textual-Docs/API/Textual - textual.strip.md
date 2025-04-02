---
title: "Textual - textual.strip"
source: "https://textual.textualize.io/api/strip/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.strip

This module contains the `Strip` class and related objects.

A `Strip` contains the result of rendering a widget. See [Line API](https://textual.textualize.io/guide/widgets#line-api) for how to use Strips.

## Strip [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip "Permanent link")

```
Strip(, =None)
```

Represents a 'strip' (horizontal line) of a Textual Widget.

A Strip is like an immutable list of Segments. The immutability allows for effective caching.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `segments` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip\(segments\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | An iterable of segments. | *required* |
| ### `cell_length` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip\(cell_length\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The cell length if known, or None to calculate on demand. | `None` |

### cell\_length [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.cell_length "Permanent link")

```
cell_length
```

Get the number of cells required to render this object.

### link\_ids [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.link_ids "Permanent link")

```
link_ids
```

A set of the link ids in this Strip.

### text [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.text "Permanent link")

```
text
```

Segment text.

### adjust\_cell\_length [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.adjust_cell_length "Permanent link")

```
adjust_cell_length(, =None)
```

Adjust the cell length, possibly truncating or extending.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `cell_length` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.adjust_cell_length\(cell_length\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | New desired cell length. | *required* |
| #### `style` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.adjust_cell_length\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style") \| None` | Style when extending, or `None`. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | A new strip with the supplied cell length. |

### align [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.align "Permanent link")

```
align(, , , , , )
```

Align a list of strips on both axis.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `strips` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.align\(strips\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of strips, such as from a render. | *required* |
| #### `style` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.align\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | The Rich style of additional space. | *required* |
| #### `width` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.align\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Width of container. | *required* |
| #### `height` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.align\(height\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | Height of container. | *required* |
| #### `horizontal` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.align\(horizontal\) "Permanent link") | `AlignHorizontal` | Horizontal alignment method. | *required* |
| #### `vertical` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.align\(vertical\) "Permanent link") | `AlignVertical` | Vertical alignment method. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | An iterable of strips, with additional padding. |

### apply\_filter [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.apply_filter "Permanent link")

```
apply_filter(, background)
```

Apply a filter to all segments in the strip.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `filter` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.apply_filter\(filter\) "Permanent link") | `[LineFilter](https://textual.textualize.io/api/filter/#textual.filter.LineFilter " LineFilter (textual.filter.LineFilter)")` | A line filter object. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new Strip. |

### apply\_meta [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.apply_meta "Permanent link")

```
apply_meta()
```

Apply meta to all segments.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `meta` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.apply_meta\(meta\) "Permanent link") | `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]` | A dict of meta information. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new strip. |

### apply\_offsets [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.apply_offsets "Permanent link")

```
apply_offsets(, )
```

Apply offsets used in text selection.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.apply_offsets\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Offset on X axis (column). | *required* |
| #### `y` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.apply_offsets\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Offset on Y axis (row). | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New strip. |

### apply\_style [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.apply_style "Permanent link")

```
apply_style()
```

Apply a style to the Strip.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `style` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.apply_style\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | A Rich style. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new strip. |

### blank [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.blank "Permanent link")

```
blank(, =None)
```

Create a blank strip.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `cell_length` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.blank\(cell_length\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Desired cell length. | *required* |
| #### `style` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.blank\(style\) "Permanent link") | `StyleType \| None` | Style of blank. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | New strip. |

### crop [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop "Permanent link")

```
crop(, =None)
```

Crop a strip between two cell positions.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `start` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop\(start\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The start cell position (inclusive). | *required* |
| #### `end` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop\(end\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The end cell position (exclusive). | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | A new Strip. |

### crop\_extend [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop_extend "Permanent link")

```
crop_extend(, , )
```

Crop between two points, extending the length if required.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `start` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop_extend\(start\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Start offset of crop. | *required* |
| #### `end` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop_extend\(end\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | End offset of crop. | *required* |
| #### `style` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop_extend\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style") \| None` | Style of additional padding. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New cropped Strip. |

### crop\_pad [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop_pad "Permanent link")

```
crop_pad(, , , )
```

Crop the strip to `cell_length`, and add optional padding.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `cell_length` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop_pad\(cell_length\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Cell length of strip prior to padding. | *required* |
| #### `left` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop_pad\(left\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Additional padding on the left. | *required* |
| #### `right` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop_pad\(right\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Additional padding on the right. | *required* |
| #### `style` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.crop_pad\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | Style of any padding. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | Cropped and padded strip. |

### discard\_meta [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.discard_meta "Permanent link")

```
discard_meta()
```

Remove all meta from segments.

Returns:

| Type | Description |
| --- | --- |
|  | New strip. |

### divide [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.divide "Permanent link")

```
divide()
```

Divide the strip into multiple smaller strips by cutting at given (cell) indices.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `cuts` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.divide\(cuts\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[int](https://docs.python.org/3/library/functions.html#int)]` | An iterable of cell positions as ints. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")[]` | A new list of strips. |

### extend\_cell\_length [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.extend_cell_length "Permanent link")

```
extend_cell_length(, =None)
```

Extend the cell length if it is less than the given value.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `cell_length` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.extend_cell_length\(cell_length\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Required minimum cell length. | *required* |
| #### `style` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.extend_cell_length\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style") \| None` | Style for padding if the cell length is extended. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | A new Strip. |

### from\_lines [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.from_lines "Permanent link")

```
from_lines(, =None)
```

Convert lines (lists of segments) to a list of Strips.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `lines` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.from_lines\(lines\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]]` | List of lines, where a line is a list of segments. | *required* |
| #### `cell_length` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.from_lines\(cell_length\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | Cell length of lines (must be same) or None if not known. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | List of strips. |

### index\_to\_cell\_position [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.index_to_cell_position "Permanent link")

```
index_to_cell_position()
```

Given a character index, return the cell position of that character. This is the sum of the cell lengths of all the characters *before* the character at `index`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `index` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.index_to_cell_position\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index to convert. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The cell position of the character at `index`. |

### join [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.join "Permanent link")

```
join()
```

Join a number of strips into one.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `strips` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.join\(strips\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[ \| None]` | An iterable of Strips. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new combined strip. |

### simplify [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.simplify "Permanent link")

```
simplify()
```

Simplify the segments (join segments with same style)

Returns:

| Type | Description |
| --- | --- |
|  | New strip. |

### style\_links [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.style_links "Permanent link")

```
style_links(, )
```

Apply a style to Segments with the given link\_id.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `link_id` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.style_links\(link_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A link id. | *required* |
| #### `link_style` [¶](https://textual.textualize.io/api/strip/#textual.strip.Strip.style_links\(link_style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | Style to apply. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New strip (or same Strip if no changes). |

## StripRenderable [¶](https://textual.textualize.io/api/strip/#textual.strip.StripRenderable "Permanent link")

```
StripRenderable(strips, width=None)
```

A renderable which renders a list of strips into lines.

## get\_line\_length [¶](https://textual.textualize.io/api/strip/#textual.strip.get_line_length "Permanent link")

```
get_line_length()
```

Get the line length (total length of all segments).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `segments` [¶](https://textual.textualize.io/api/strip/#textual.strip.get_line_length\(segments\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | Iterable of segments. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | Length of line in cells. |