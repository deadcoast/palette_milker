---
title: "Textual - textual.map_geometry"
source: "https://textual.textualize.io/api/map_geometry/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.map\_geometry

A data structure returned by [screen.find\_widget](https://textual.textualize.io/api/screen/#textual.screen.Screen.find_widget " find_widget").

## MapGeometry [¶](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

Defines the absolute location of a Widget.

### clip [¶](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry.clip "Permanent link")

```
clip
```

A [region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region") to clip the widget by (if a Widget is within a container).

### container\_size [¶](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry.container_size "Permanent link")

```
container_size
```

The container [size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size") (area not occupied by scrollbars).

### dock\_gutter [¶](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry.dock_gutter "Permanent link")

```
dock_gutter
```

Space from the container reserved by docked widgets.

### order [¶](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry.order "Permanent link")

```
order
```

Tuple of tuples defining the painting order of the widget.

Each successive triple represents painting order information with regards to ancestors in the DOM hierarchy and the last triple provides painting order information for this specific widget.

### region [¶](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry.region "Permanent link")

```
region
```

The (screen) [region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region") occupied by the widget.

### virtual\_region [¶](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry.virtual_region "Permanent link")

```
virtual_region
```

The [region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region") relative to the container (but not necessarily visible).

### virtual\_size [¶](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry.virtual_size "Permanent link")

```
virtual_size
```

The virtual [size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size") (scrollable area) of a widget if it is a container.

### visible\_region [¶](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry.visible_region "Permanent link")

```
visible_region
```

The Widget region after clipping.