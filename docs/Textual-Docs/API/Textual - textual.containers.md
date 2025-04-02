---
title: "Textual - textual.containers"
source: "https://textual.textualize.io/api/containers/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.containers

Container widgets for quick styling.

With the exception of `Center` and `Middle` containers will fill all of the space in the parent widget.

## Center [¶](https://textual.textualize.io/api/containers/#textual.containers.Center "Permanent link")

```
Center(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A container which aligns children on the X axis.

## Container [¶](https://textual.textualize.io/api/containers/#textual.containers.Container "Permanent link")

```
Container(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

Simple container widget, with vertical layout.

## Grid [¶](https://textual.textualize.io/api/containers/#textual.containers.Grid "Permanent link")

```
Grid(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A container with grid layout.

## Horizontal [¶](https://textual.textualize.io/api/containers/#textual.containers.Horizontal "Permanent link")

```
Horizontal(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

An expanding container with horizontal layout and no scrollbars.

## HorizontalGroup [¶](https://textual.textualize.io/api/containers/#textual.containers.HorizontalGroup "Permanent link")

```
HorizontalGroup(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A non-expanding container with horizontal layout and no scrollbars.

## HorizontalScroll [¶](https://textual.textualize.io/api/containers/#textual.containers.HorizontalScroll "Permanent link")

```
HorizontalScroll(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    can_focus=None,
    can_focus_children=None,
    can_maximize=None
)
```

Bases:

A container with horizontal layout and an automatic scrollbar on the X axis.

## ItemGrid [¶](https://textual.textualize.io/api/containers/#textual.containers.ItemGrid "Permanent link")

```
ItemGrid(
    *,
    =None,
    =None,
    =None,
    =False,
    =None,
    =True,
    =False
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A container with grid layout and automatic columns.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `*children` [¶](https://textual.textualize.io/api/containers/#textual.containers.ItemGrid\(*children\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | Child widgets. | `()` |
| ### `name` [¶](https://textual.textualize.io/api/containers/#textual.containers.ItemGrid\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ### `id` [¶](https://textual.textualize.io/api/containers/#textual.containers.ItemGrid\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/api/containers/#textual.containers.ItemGrid\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the widget. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/api/containers/#textual.containers.ItemGrid\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |
| ### `stretch_height` [¶](https://textual.textualize.io/api/containers/#textual.containers.ItemGrid\(stretch_height\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Expand the height of widgets to the row height. | `True` |
| ### `min_column_width` [¶](https://textual.textualize.io/api/containers/#textual.containers.ItemGrid\(min_column_width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The smallest permitted column width. | `None` |
| ### `regular` [¶](https://textual.textualize.io/api/containers/#textual.containers.ItemGrid\(regular\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | All rows should have the same number of items. | `False` |

## Middle [¶](https://textual.textualize.io/api/containers/#textual.containers.Middle "Permanent link")

```
Middle(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A container which aligns children on the Y axis.

## Right [¶](https://textual.textualize.io/api/containers/#textual.containers.Right "Permanent link")

```
Right(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A container which aligns children on the X axis.

## ScrollableContainer [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer "Permanent link")

```
ScrollableContainer(
    *,
    =None,
    =None,
    =None,
    =False,
    =None,
    =None,
    can_maximize=None
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A scrollable container with vertical layout, and auto scrollbars on both axis.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `*children` [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer\(*children\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | Child widgets. | `()` |
| ### `name` [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ### `id` [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the widget. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |
| ### `can_focus` [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer\(can_focus\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Can this container be focused? | `None` |
| ### `can_focus_children` [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer\(can_focus_children\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Can this container's children be focused? | `None` |
| ### `can_maximized` [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer\(can_maximized\) "Permanent link") |  | Allow this container to maximize? `None` to use default logic., | *required* |

### BINDINGS [¶](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding("up", "scroll_up", "Scroll Up", show=False),
    Binding(
        "down", "scroll_down", "Scroll Down", show=False
    ),
    Binding(
        "left", "scroll_left", "Scroll Left", show=False
    ),
    Binding(
        "right", "scroll_right", "Scroll Right", show=False
    ),
    Binding(
        "home", "scroll_home", "Scroll Home", show=False
    ),
    Binding("end", "scroll_end", "Scroll End", show=False),
    Binding("pageup", "page_up", "Page Up", show=False),
    Binding(
        "pagedown", "page_down", "Page Down", show=False
    ),
    Binding(
        "ctrl+pageup", "page_left", "Page Left", show=False
    ),
    Binding(
        "ctrl+pagedown",
        "page_right",
        "Page Right",
        show=False,
    ),
]
```

Keyboard bindings for scrollable containers.

| Key(s) | Description |
| --- | --- |
| up | Scroll up, if vertical scrolling is available. |
| down | Scroll down, if vertical scrolling is available. |
| left | Scroll left, if horizontal scrolling is available. |
| right | Scroll right, if horizontal scrolling is available. |
| home | Scroll to the home position, if scrolling is available. |
| end | Scroll to the end position, if scrolling is available. |
| pageup | Scroll up one page, if vertical scrolling is available. |
| pagedown | Scroll down one page, if vertical scrolling is available. |
| ctrl+pageup | Scroll left one page, if horizontal scrolling is available. |
| ctrl+pagedown | Scroll right one page, if horizontal scrolling is available. |

## Vertical [¶](https://textual.textualize.io/api/containers/#textual.containers.Vertical "Permanent link")

```
Vertical(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

An expanding container with vertical layout and no scrollbars.

## VerticalGroup [¶](https://textual.textualize.io/api/containers/#textual.containers.VerticalGroup "Permanent link")

```
VerticalGroup(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A non-expanding container with vertical layout and no scrollbars.

## VerticalScroll [¶](https://textual.textualize.io/api/containers/#textual.containers.VerticalScroll "Permanent link")

```
VerticalScroll(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    can_focus=None,
    can_focus_children=None,
    can_maximize=None
)
```

Bases:

A container with vertical layout and an automatic scrollbar on the Y axis.