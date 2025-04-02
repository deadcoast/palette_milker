---
title: "Textual - textual.geometry"
source: "https://textual.textualize.io/api/geometry/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.geometry

Functions and classes to manage terminal geometry (anything involving coordinates or dimensions).

## NULL\_OFFSET [¶](https://textual.textualize.io/api/geometry/#textual.geometry.NULL_OFFSET "Permanent link")

```
NULL_OFFSET = (0, 0)
```

An constant for (0, 0).

## NULL\_REGION [¶](https://textual.textualize.io/api/geometry/#textual.geometry.NULL_REGION "Permanent link")

```
NULL_REGION = (0, 0, 0, 0)
```

A constant for a null region (at the origin, with both width and height set to zero).

## NULL\_SIZE [¶](https://textual.textualize.io/api/geometry/#textual.geometry.NULL_SIZE "Permanent link")

```
NULL_SIZE = (0, 0)
```

A constant for a null size (with zero area).

## NULL\_SPACING [¶](https://textual.textualize.io/api/geometry/#textual.geometry.NULL_SPACING "Permanent link")

```
NULL_SPACING = (0, 0, 0, 0)
```

A constant for no space.

## SpacingDimensions [¶](https://textual.textualize.io/api/geometry/#textual.geometry.SpacingDimensions "Permanent link")

```
SpacingDimensions = Union[
    int,
    Tuple[int],
    Tuple[int, int],
    Tuple[int, int, int, int],
]
```

The valid ways in which you can specify spacing.

## Offset [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

A cell offset defined by x and y coordinates.

Offsets are typically relative to the top left of the terminal or other container.

Textual prefers the names `x` and `y`, but you could consider `x` to be the *column* and `y` to be the *row*.

Offsets support addition, subtraction, multiplication, and negation.

Example
```
>>> from textual.geometry import Offset
>>> offset = Offset(3, 2)
>>> offset
Offset(x=3, y=2)
>>> offset += Offset(10, 0)
>>> offset
Offset(x=13, y=2)
>>> -offset
Offset(x=-13, y=-2)
```

### clamped [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.clamped "Permanent link")

```
clamped
```

This offset with `x` and `y` restricted to values above zero.

### is\_origin [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.is_origin "Permanent link")

```
is_origin
```

Is the offset at (0, 0)?

### transpose [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.transpose "Permanent link")

```
transpose
```

A tuple of x and y, in reverse order, i.e. (y, x).

### x [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.x "Permanent link")

```
x = 0
```

Offset in the x-axis (horizontal)

### y [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.y "Permanent link")

```
y = 0
```

Offset in the y-axis (vertical)

### blend [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.blend "Permanent link")

```
blend(, )
```

Calculate a new offset on a line between this offset and a destination offset.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `destination` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.blend\(destination\) "Permanent link") |  | Point where factor would be 1.0. | *required* |
| #### `factor` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.blend\(factor\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | A value between 0 and 1.0. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new point on a line between self and destination. |

### clamp [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.clamp "Permanent link")

```
clamp(, )
```

Clamp the offset to fit within a rectangle of width x height.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `width` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.clamp\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Width to clamp. | *required* |
| #### `height` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.clamp\(height\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Height to clamp. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new offset. |

### get\_distance\_to [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.get_distance_to "Permanent link")

```
get_distance_to()
```

Get the distance to another offset.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `other` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Offset.get_distance_to\(other\) "Permanent link") |  | An offset. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[float](https://docs.python.org/3/library/functions.html#float)` | Distance to other offset. |

## Region [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

Defines a rectangular region.

A Region consists of a coordinate (x and y) and dimensions (width and height).

```
(x, y)
    ┌────────────────────┐ ▲
    │                    │ │
    │                    │ │
    │                    │ height
    │                    │ │
    │                    │ │
    └────────────────────┘ ▼
    ◀─────── width ──────▶
```
Example
```
>>> from textual.geometry import Region
>>> region = Region(4, 5, 20, 10)
>>> region
Region(x=4, y=5, width=20, height=10)
>>> region.area
200
>>> region.size
Size(width=20, height=10)
>>> region.offset
Offset(x=4, y=5)
>>> region.contains(1, 2)
False
>>> region.contains(10, 8)
True
```

### area [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.area "Permanent link")

```
area
```

The area under the region.

### bottom [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.bottom "Permanent link")

```
bottom
```

Maximum Y value (non inclusive).

### bottom\_left [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.bottom_left "Permanent link")

```
bottom_left
```

Bottom left offset of the region.

Returns:

| Type | Description |
| --- | --- |
|  | An offset. |

### bottom\_right [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.bottom_right "Permanent link")

```
bottom_right
```

Bottom right offset of the region.

Returns:

| Type | Description |
| --- | --- |
|  | An offset. |

### bottom\_right\_inclusive [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.bottom_right_inclusive "Permanent link")

```
bottom_right_inclusive
```

Bottom right corner of the region, within its boundaries.

### center [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.center "Permanent link")

```
center
```

The center of the region.

Note, that this does *not* return an `Offset`, because the center may not be an integer coordinate.

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[float](https://docs.python.org/3/library/functions.html#float), [float](https://docs.python.org/3/library/functions.html#float)]` | Tuple of floats. |

### column\_range [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.column_range "Permanent link")

```
column_range
```

A range object for X coordinates.

### column\_span [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.column_span "Permanent link")

```
column_span
```

A pair of integers for the start and end columns (x coordinates) in this region.

The end value is *exclusive*.

### corners [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.corners "Permanent link")

```
corners
```

The top left and bottom right coordinates as a tuple of four integers.

### height [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.height "Permanent link")

```
height = 0
```

The height of the region.

### line\_range [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.line_range "Permanent link")

```
line_range
```

A range object for Y coordinates.

### line\_span [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.line_span "Permanent link")

```
line_span
```

A pair of integers for the start and end lines (y coordinates) in this region.

The end value is *exclusive*.

### offset [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.offset "Permanent link")

```
offset
```

The top left corner of the region.

Returns:

| Type | Description |
| --- | --- |
|  | An offset. |

### reset\_offset [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.reset_offset "Permanent link")

```
reset_offset
```

An region of the same size at (0, 0).

Returns:

| Type | Description |
| --- | --- |
|  | A region at the origin. |

### right [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.right "Permanent link")

```
right
```

Maximum X value (non inclusive).

### size [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.size "Permanent link")

```
size
```

Get the size of the region.

### top\_right [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.top_right "Permanent link")

```
top_right
```

Top right offset of the region.

Returns:

| Type | Description |
| --- | --- |
|  | An offset. |

### width [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.width "Permanent link")

```
width = 0
```

The width of the region.

### x [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.x "Permanent link")

```
x = 0
```

Offset in the x-axis (horizontal).

### y [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.y "Permanent link")

```
y = 0
```

Offset in the y-axis (vertical).

### at\_offset [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.at_offset "Permanent link")

```
at_offset()
```

Get a new Region with the same size at a given offset.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `offset` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.at_offset\(offset\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | An offset. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New Region with adjusted offset. |

### clip [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.clip "Permanent link")

```
clip(, )
```

Clip this region to fit within width, height.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `width` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.clip\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Width of bounds. | *required* |
| #### `height` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.clip\(height\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Height of bounds. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | Clipped region. |

### constrain [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.constrain "Permanent link")

```
constrain(, , , )
```

Constrain a region to fit within a container, using different methods per axis.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `constrain_x` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.constrain\(constrain_x\) "Permanent link") | `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['none', 'inside', 'inflect']` | Constrain method for the X-axis. | *required* |
| #### `constrain_y` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.constrain\(constrain_y\) "Permanent link") | `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['none', 'inside', 'inflect']` | Constrain method for the Y-axis. | *required* |
| #### `margin` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.constrain\(margin\) "Permanent link") |  | Margin to maintain around region. | *required* |
| #### `container` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.constrain\(container\) "Permanent link") |  | Container to constrain to. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New widget, that fits inside the container (if possible). |

### contains [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.contains "Permanent link")

```
contains(, )
```

Check if a point is in the region.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.contains\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | X coordinate. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.contains\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y coordinate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the point is within the region. |

### contains\_point [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.contains_point "Permanent link")

```
contains_point()
```

Check if a point is in the region.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `point` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.contains_point\(point\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | A tuple of x and y coordinates. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the point is within the region. |

### contains\_region [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.contains_region "Permanent link")

```
contains_region()
```

Check if a region is entirely contained within this region.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `other` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.contains_region\(other\) "Permanent link") |  | A region. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the other region fits perfectly within this region. |

### crop\_size [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.crop_size "Permanent link")

```
crop_size()
```

Get a region with the same offset, with a size no larger than `size`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `size` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.crop_size\(size\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | Maximum width and height (WIDTH, HEIGHT). | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New region that could fit within `size`. |

### expand [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.expand "Permanent link")

```
expand()
```

Increase the size of the region by adding a border.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `size` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.expand\(size\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | Additional width and height. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new region. |

### from\_corners [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_corners "Permanent link")

```
from_corners(, , , )
```

Construct a Region form the top left and bottom right corners.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x1` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_corners\(x1\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Top left x. | *required* |
| #### `y1` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_corners\(y1\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Top left y. | *required* |
| #### `x2` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_corners\(x2\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Bottom right x. | *required* |
| #### `y2` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_corners\(y2\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Bottom right y. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new region. |

### from\_offset [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_offset "Permanent link")

```
from_offset(, )
```

Create a region from offset and size.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `offset` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_offset\(offset\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | Offset (top left point). | *required* |
| #### `size` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_offset\(size\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | Dimensions of region. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A region instance. |

### from\_union [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_union "Permanent link")

```
from_union()
```

Create a Region from the union of other regions.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `regions` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.from_union\(regions\) "Permanent link") | `[Collection](https://docs.python.org/3/library/typing.html#typing.Collection "typing.Collection")[]` | One or more regions. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A Region that encloses all other regions. |

### get\_scroll\_to\_visible [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.get_scroll_to_visible "Permanent link")

```
get_scroll_to_visible(, , *, =False)
```

Calculate the smallest offset required to translate a window so that it contains another region.

This method is used to calculate the required offset to scroll something into view.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `window_region` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.get_scroll_to_visible\(window_region\) "Permanent link") |  | The window region. | *required* |
| #### `region` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.get_scroll_to_visible\(region\) "Permanent link") |  | The region to move inside the window. | *required* |
| #### `top` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.get_scroll_to_visible\(top\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Get offset to top of window. | `False` |

Returns:

| Type | Description |
| --- | --- |
|  | An offset required to add to region to move it inside window\_region. |

### get\_spacing\_between [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.get_spacing_between "Permanent link")

```
get_spacing_between()
```

Get spacing between two regions.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `region` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.get_spacing_between\(region\) "Permanent link") |  | Another region. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | Spacing that if subtracted from `self` produces `region`. |

### grow [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.grow "Permanent link")

```
grow()
```

Grow a region by adding spacing.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `margin` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.grow\(margin\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | Grow space by `(<top>, <right>, <bottom>, <left>)`. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New region. |

### inflect [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.inflect "Permanent link")

```
inflect(=+1, =+1, =None)
```

Inflect a region around one or both axis.

The `x_axis` and `y_axis` parameters define which direction to move the region. A positive value will move the region right or down, a negative value will move the region left or up. A value of `0` will leave that axis unmodified.

If a margin is provided, it will add space between the resulting region.

Note that if margin is specified it *overlaps*, so the space will be the maximum of two edges, and not the total.

```
╔══════════╗    │
║          ║
║   Self   ║    │
║          ║
╚══════════╝    │

─ ─ ─ ─ ─ ─ ─ ─ ┌──────────┐
                │          │
                │  Result  │
                │          │
                └──────────┘
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x_axis` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.inflect\(x_axis\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | +1 to inflect in the positive direction, -1 to inflect in the negative direction. | `+1` |
| #### `y_axis` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.inflect\(y_axis\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | +1 to inflect in the positive direction, -1 to inflect in the negative direction. | `+1` |
| #### `margin` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.inflect\(margin\) "Permanent link") | ` \| None` | Additional margin. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | A new region. |

### intersection [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.intersection "Permanent link")

```
intersection()
```

Get the overlapping portion of the two regions.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `region` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.intersection\(region\) "Permanent link") |  | A region that overlaps this region. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new region that covers when the two regions overlap. |

### overlaps [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.overlaps "Permanent link")

```
overlaps()
```

Check if another region overlaps this region.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `other` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.overlaps\(other\) "Permanent link") |  | A Region. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if other region shares any cells with this region. |

### shrink [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.shrink "Permanent link")

```
shrink()
```

Shrink a region by subtracting spacing.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `margin` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.shrink\(margin\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | Shrink space by `(<top>, <right>, <bottom>, <left>)`. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The new, smaller region. |

### split [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.split "Permanent link")

```
split(, )
```

Split a region into 4 from given x and y offsets (cuts).

```
cut_x ↓
        ┌────────┐ ┌───┐
        │        │ │   │
        │    0   │ │ 1 │
        │        │ │   │
cut_y → └────────┘ └───┘
        ┌────────┐ ┌───┐
        │    2   │ │ 3 │
        └────────┘ └───┘
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `cut_x` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.split\(cut_x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Offset from self.x where the cut should be made. If negative, the cut is taken from the right edge. | *required* |
| #### `cut_y` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.split\(cut_y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Offset from self.y where the cut should be made. If negative, the cut is taken from the lower edge. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[, , , ]` | Four new regions which add up to the original (self). |

### split\_horizontal [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.split_horizontal "Permanent link")

```
split_horizontal()
```

Split a region into two, from a given y offset.

```
┌─────────┐
            │    0    │
            │         │
    cut →   └─────────┘
            ┌─────────┐
            │    1    │
            └─────────┘
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `cut` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.split_horizontal\(cut\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | An offset from self.y where the cut should be made. May be negative, for the offset to start from the lower edge. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[, ]` | Two regions, which add up to the original (self). |

### split\_vertical [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.split_vertical "Permanent link")

```
split_vertical()
```

Split a region into two, from a given x offset.

```
cut ↓
    ┌────────┐┌───┐
    │    0   ││ 1 │
    │        ││   │
    └────────┘└───┘
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `cut` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.split_vertical\(cut\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | An offset from self.x where the cut should be made. If cut is negative, it is taken from the right edge. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[, ]` | Two regions, which add up to the original (self). |

### translate [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.translate "Permanent link")

```
translate()
```

Move the offset of the Region.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `offset` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.translate\(offset\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | Offset to add to region. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new region shifted by (x, y). |

### translate\_inside [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.translate_inside "Permanent link")

```
translate_inside(, =True, =True)
```

Translate this region, so it fits within a container.

This will ensure that there is as little overlap as possible. The top left of the returned region is guaranteed to be within the container.

```
┌──────────────────┐         ┌──────────────────┐
│    container     │         │    container     │
│                  │         │    ┌─────────────┤
│                  │   ──▶   │    │    return   │
│       ┌──────────┴──┐      │    │             │
│       │    self     │      │    │             │
└───────┤             │      └────┴─────────────┘
        │             │
        └─────────────┘
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `container` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.translate_inside\(container\) "Permanent link") |  | A container region. | *required* |
| #### `x_axis` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.translate_inside\(x_axis\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow translation of X axis. | `True` |
| #### `y_axis` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.translate_inside\(y_axis\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow translation of Y axis. | `True` |

Returns:

| Type | Description |
| --- | --- |
|  | A new region with same dimensions that fits with inside container. |

### union [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.union "Permanent link")

```
union()
```

Get the smallest region that contains both regions.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `region` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Region.union\(region\) "Permanent link") |  | Another region. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | An optimally sized region to cover both regions. |

## Size [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

The dimensions (width and height) of a rectangular region.

Example
```
>>> from textual.geometry import Size
>>> size = Size(2, 3)
>>> size
Size(width=2, height=3)
>>> size.area
6
>>> size + Size(10, 20)
Size(width=12, height=23)
```

### area [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.area "Permanent link")

```
area
```

The area occupied by a region of this size.

### height [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.height "Permanent link")

```
height = 0
```

The height in cells.

### line\_range [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.line_range "Permanent link")

```
line_range
```

A range object that covers values between 0 and `height`.

### region [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.region "Permanent link")

```
region
```

A region of the same size, at the origin.

### width [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.width "Permanent link")

```
width = 0
```

The width in cells.

### clamp\_offset [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.clamp_offset "Permanent link")

```
clamp_offset()
```

Clamp an offset to fit within the width x height.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `offset` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.clamp_offset\(offset\) "Permanent link") |  | An offset. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new offset that will fit inside the dimensions defined in the Size. |

### contains [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.contains "Permanent link")

```
contains(, )
```

Check if a point is in area defined by the size.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.contains\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | X coordinate. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.contains\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y coordinate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the point is within the region. |

### contains\_point [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.contains_point "Permanent link")

```
contains_point()
```

Check if a point is in the area defined by the size.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `point` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.contains_point\(point\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | A tuple of x and y coordinates. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the point is within the region. |

### with\_height [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.with_height "Permanent link")

```
with_height()
```

Get a new Size with just the height changed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `height` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.with_height\(height\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | New height. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New Size instance. |

### with\_width [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.with_width "Permanent link")

```
with_width()
```

Get a new Size with just the width changed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `width` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Size.with_width\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | New width. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New Size instance. |

## Spacing [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

Stores spacing around a widget, such as padding and border.

Spacing is defined by four integers for the space at the top, right, bottom, and left of a region.

```
┌ ─ ─ ─ ─ ─ ─ ─▲─ ─ ─ ─ ─ ─ ─ ─ ┐
               │ top
│        ┏━━━━━▼━━━━━━┓         │
 ◀──────▶┃            ┃◀───────▶
│  left  ┃            ┃ right   │
         ┃            ┃
│        ┗━━━━━▲━━━━━━┛         │
               │ bottom
└ ─ ─ ─ ─ ─ ─ ─▼─ ─ ─ ─ ─ ─ ─ ─ ┘
```
Example
```
>>> from textual.geometry import Region, Spacing
>>> region = Region(2, 3, 20, 10)
>>> spacing = Spacing(1, 2, 3, 4)
>>> region.grow(spacing)
Region(x=-2, y=2, width=26, height=14)
>>> region.shrink(spacing)
Region(x=6, y=4, width=14, height=6)
>>> spacing.css
'1 2 3 4'
```

### bottom [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.bottom "Permanent link")

```
bottom = 0
```

Space from the bottom of a region.

### bottom\_right [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.bottom_right "Permanent link")

```
bottom_right
```

A pair of integers for the right, and bottom space.

### css [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.css "Permanent link")

```
css
```

A string containing the spacing in CSS format.

For example: "1" or "2 4" or "4 2 8 2".

### height [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.height "Permanent link")

```
height
```

Total space in the y axis.

### left [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.left "Permanent link")

```
left = 0
```

Space from the left of a region.

### max\_height [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.max_height "Permanent link")

```
max_height
```

The space between regions in the Y direction if margins overlap, i.e. `max(self.top, self.bottom)`.

### max\_width [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.max_width "Permanent link")

```
max_width
```

The space between regions in the X direction if margins overlap, i.e. `max(self.left, self.right)`.

### right [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.right "Permanent link")

```
right = 0
```

Space from the right of a region.

### top [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.top "Permanent link")

```
top = 0
```

Space from the top of a region.

### top\_left [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.top_left "Permanent link")

```
top_left
```

A pair of integers for the left, and top space.

### totals [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.totals "Permanent link")

```
totals
```

A pair of integers for the total horizontal and vertical space.

### width [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.width "Permanent link")

```
width
```

Total space in the x axis.

### all [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.all "Permanent link")

```
all()
```

Construct a Spacing with a given amount of spacing on all edges.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `amount` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.all\(amount\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The magnitude of spacing to apply to all edges. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | `Spacing(amount, amount, amount, amount)` |

### grow\_maximum [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.grow_maximum "Permanent link")

```
grow_maximum()
```

Grow spacing with a maximum.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `other` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.grow_maximum\(other\) "Permanent link") |  | Spacing object. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New spacing where the values are maximum of the two values. |

### horizontal [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.horizontal "Permanent link")

```
horizontal()
```

Construct a Spacing with a given amount of spacing on horizontal edges, and no vertical spacing.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `amount` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.horizontal\(amount\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The magnitude of spacing to apply to horizontal edges. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | `Spacing(0, amount, 0, amount)` |

### unpack [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.unpack "Permanent link")

```
unpack()
```

Unpack padding specified in CSS style.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `pad` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.unpack\(pad\) "Permanent link") |  | An integer, or tuple of 1, 2, or 4 integers. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` | If `pad` is an invalid value. |

Returns:

| Type | Description |
| --- | --- |
|  | New Spacing object. |

### vertical [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.vertical "Permanent link")

```
vertical()
```

Construct a Spacing with a given amount of spacing on vertical edges, and no horizontal spacing.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `amount` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing.vertical\(amount\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The magnitude of spacing to apply to vertical edges. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | `Spacing(amount, 0, amount, 0)` |

## clamp [¶](https://textual.textualize.io/api/geometry/#textual.geometry.clamp "Permanent link")

```
clamp(, , )
```

Restrict a value to a given range.

If `value` is less than the minimum, return the minimum. If `value` is greater than the maximum, return the maximum. Otherwise, return `value`.

The `minimum` and `maximum` arguments values may be given in reverse order.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `value` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.clamp\(value\) "Permanent link") | `T` | A value. | *required* |
| ### `minimum` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.clamp\(minimum\) "Permanent link") | `T` | Minimum value. | *required* |
| ### `maximum` [¶](https://textual.textualize.io/api/geometry/#textual.geometry.clamp\(maximum\) "Permanent link") | `T` | Maximum value. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `T` | New value that is not less than the minimum or greater than the maximum. |