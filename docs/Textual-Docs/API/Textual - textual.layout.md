---
title: "Textual - textual.layout"
source: "https://textual.textualize.io/api/layout/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.layout

## DockArrangeResult [¶](https://textual.textualize.io/api/layout/#textual.layout.DockArrangeResult "Permanent link")

```
DockArrangeResult(
    placements, widgets, scroll_spacing, _spatial_map=None
)
```

Result of .

### placements [¶](https://textual.textualize.io/api/layout/#textual.layout.DockArrangeResult.placements "Permanent link")

```
placements
```

A `WidgetPlacement` for every widget to describe its location on screen.

### scroll\_spacing [¶](https://textual.textualize.io/api/layout/#textual.layout.DockArrangeResult.scroll_spacing "Permanent link")

```
scroll_spacing
```

Spacing to reduce scrollable area.

### spatial\_map [¶](https://textual.textualize.io/api/layout/#textual.layout.DockArrangeResult.spatial_map "Permanent link")

```
spatial_map
```

A lazy-calculated spatial map.

### total\_region [¶](https://textual.textualize.io/api/layout/#textual.layout.DockArrangeResult.total_region "Permanent link")

```
total_region
```

The total area occupied by the arrangement.

Returns:

| Type | Description |
| --- | --- |
| `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | A Region. |

### widgets [¶](https://textual.textualize.io/api/layout/#textual.layout.DockArrangeResult.widgets "Permanent link")

```
widgets
```

A set of widgets in the arrangement.

### get\_visible\_placements [¶](https://textual.textualize.io/api/layout/#textual.layout.DockArrangeResult.get_visible_placements "Permanent link")

```
get_visible_placements()
```

Get the placements visible within the given region.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `region` [¶](https://textual.textualize.io/api/layout/#textual.layout.DockArrangeResult.get_visible_placements\(region\) "Permanent link") | `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | A region. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | Set of placements. |

## Layout [¶](https://textual.textualize.io/api/layout/#textual.layout.Layout "Permanent link")

Bases: `[ABC](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")`

Base class of the object responsible for arranging Widgets within a container.

### arrange [¶](https://textual.textualize.io/api/layout/#textual.layout.Layout.arrange "Permanent link")

```
arrange(, children, )
```

Generate a layout map that defines where on the screen the widgets will be drawn.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `parent` [¶](https://textual.textualize.io/api/layout/#textual.layout.Layout.arrange\(parent\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | Parent widget. | *required* |
| #### `size` [¶](https://textual.textualize.io/api/layout/#textual.layout.Layout.arrange\(size\) "Permanent link") | `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Size of container. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `ArrangeResult` | An iterable of widget location |

### render\_keyline [¶](https://textual.textualize.io/api/layout/#textual.layout.Layout.render_keyline "Permanent link")

```
render_keyline()
```

Render keylines around all widgets.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `container` [¶](https://textual.textualize.io/api/layout/#textual.layout.Layout.render_keyline\(container\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | The container widget. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[StripRenderable](https://textual.textualize.io/api/strip/#textual.strip.StripRenderable " StripRenderable (textual.strip.StripRenderable)")` | A renderable to draw the keylines. |

## WidgetPlacement [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

The position, size, and relative order of a widget within its parent.

### reset\_origin [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.reset_origin "Permanent link")

```
reset_origin
```

Reset the origin in the placement (moves it to (0, 0)).

### apply\_absolute [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.apply_absolute "Permanent link")

```
apply_absolute()
```

Applies absolute offsets (in place).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `placements` [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.apply_absolute\(placements\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of placements. | *required* |

### get\_bounds [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.get_bounds "Permanent link")

```
get_bounds()
```

Get a bounding region around all placements.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `placements` [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.get_bounds\(placements\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | A number of placements. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | An optimal binding box around all placements. |

### process\_offset [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.process_offset "Permanent link")

```
process_offset(, )
```

Apply any absolute offset or constrain rules to the placement.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `constrain_region` [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.process_offset\(constrain_region\) "Permanent link") | `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | The container region when applying constrain rules. | *required* |
| #### `absolute_offset` [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.process_offset\(absolute_offset\) "Permanent link") | `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | Default absolute offset that moves widget into screen coordinates. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | Processes placement, may be the same instance. |

### translate [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.translate "Permanent link")

```
translate(, translate_offset)
```

Move all non-absolute placements by a given offset.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `placements` [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.translate\(placements\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | List of placements. | *required* |
| #### `offset` [¶](https://textual.textualize.io/api/layout/#textual.layout.WidgetPlacement.translate\(offset\) "Permanent link") |  | Offset to add to placements. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | Placements with adjusted region, or same instance if offset is null. |