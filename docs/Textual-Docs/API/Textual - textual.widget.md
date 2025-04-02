---
title: "Textual - textual.widget"
source: "https://textual.textualize.io/api/widget/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.widget

This module contains the `Widget` class, the base class for all widgets.

## AwaitMount [¶](https://textual.textualize.io/api/widget/#textual.widget.AwaitMount "Permanent link")

```
AwaitMount(parent, widgets)
```

An *optional* awaitable returned by and .

Example
```
await self.mount(Static("foo"))
```

## BadWidgetName [¶](https://textual.textualize.io/api/widget/#textual.widget.BadWidgetName "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when widget class names do not satisfy the required restrictions.

## MountError [¶](https://textual.textualize.io/api/widget/#textual.widget.MountError "Permanent link")

Bases:

Error raised when there was a problem with the mount request.

## PseudoClasses [¶](https://textual.textualize.io/api/widget/#textual.widget.PseudoClasses "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

Used for render/render\_line based widgets that use caching. This structure can be used as a cache-key.

### enabled [¶](https://textual.textualize.io/api/widget/#textual.widget.PseudoClasses.enabled "Permanent link")

```
enabled
```

Is 'enabled' applied?

### focus [¶](https://textual.textualize.io/api/widget/#textual.widget.PseudoClasses.focus "Permanent link")

```
focus
```

Is 'focus' applied?

### hover [¶](https://textual.textualize.io/api/widget/#textual.widget.PseudoClasses.hover "Permanent link")

```
hover
```

Is 'hover' applied?

## Widget [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget "Permanent link")

```
Widget(
    *,
    =None,
    =None,
    =None,
    =False,
    markup=True
)
```

Bases: `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")`

A Widget is the base class for Textual widgets.

See also [static](https://textual.textualize.io/widgets/static/#textual.widgets.Static " Static") for starting point for your own widgets.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `*children` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget\(*children\) "Permanent link") |  | Child widgets. | `()` |
| ### `name` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ### `id` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the widget. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

### ALLOW\_MAXIMIZE [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.ALLOW_MAXIMIZE "Permanent link")

```
ALLOW_MAXIMIZE = None
```

Defines default logic to allow the widget to be maximized.

- `None` Use default behavior (Focusable widgets may be maximized)
- `False` Do not allow widget to be maximized
- `True` Allow widget to be maximized

### ALLOW\_SELECT [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.ALLOW_SELECT "Permanent link")

```
ALLOW_SELECT = True
```

Does this widget support automatic text selection? May be further refined with

### BORDER\_SUBTITLE [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.BORDER_SUBTITLE "Permanent link")

```
BORDER_SUBTITLE = ''
```

Initial value for border\_subtitle attribute.

### BORDER\_TITLE [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.BORDER_TITLE "Permanent link")

```
BORDER_TITLE = ''
```

Initial value for border\_title attribute.

### absolute\_offset [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.absolute_offset "Permanent link")

```
absolute_offset = None
```

Force an absolute offset for the widget (used by tooltips).

### allow\_horizontal\_scroll [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.allow_horizontal_scroll "Permanent link")

```
allow_horizontal_scroll
```

Check if horizontal scroll is permitted.

May be overridden if you want different logic regarding allowing scrolling.

### allow\_maximize [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.allow_maximize "Permanent link")

```
allow_maximize
```

Check if the widget may be maximized.

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the widget may be maximized, or `False` if it should not be maximized. |

### allow\_select [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.allow_select "Permanent link")

```
allow_select
```

Check if this widget permits text selection.

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the widget supports text selection, otherwise `False`. |

### allow\_vertical\_scroll [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.allow_vertical_scroll "Permanent link")

```
allow_vertical_scroll
```

Check if vertical scroll is permitted.

May be overridden if you want different logic regarding allowing scrolling.

### auto\_links [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.auto_links "Permanent link")

```
auto_links = Reactive(True)
```

Widget will highlight links automatically.

### border\_subtitle [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.border_subtitle "Permanent link")

```
border_subtitle = _BorderTitle()
```

A title to show in the bottom border (if there is one).

### border\_title [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.border_title "Permanent link")

```
border_title = _BorderTitle()
```

A title to show in the top border (if there is one).

### can\_focus [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.can_focus "Permanent link")

```
can_focus = False
```

Widget may receive focus.

### can\_focus\_children [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.can_focus_children "Permanent link")

```
can_focus_children = True
```

Widget's children may receive focus.

### container\_size [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.container_size "Permanent link")

```
container_size
```

The size of the container (parent widget).

Returns:

| Type | Description |
| --- | --- |
| `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Container size. |

### container\_viewport [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.container_viewport "Permanent link")

```
container_viewport
```

The viewport region (parent window).

Returns:

| Type | Description |
| --- | --- |
| `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | The region that contains this widget. |

### content\_offset [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.content_offset "Permanent link")

```
content_offset
```

An offset from the Widget origin where the content begins.

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | Offset from widget's origin. |

### content\_region [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.content_region "Permanent link")

```
content_region
```

Gets an absolute region containing the content (minus padding and border).

Returns:

| Type | Description |
| --- | --- |
| `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | Screen region that contains a widget's content. |

### content\_size [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.content_size "Permanent link")

```
content_size
```

The size of the content area.

Returns:

| Type | Description |
| --- | --- |
| `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Content area size. |

### disabled [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.disabled "Permanent link")

```
disabled = Reactive(False)
```

Is the widget disabled? Disabled widgets can not be interacted with, and are typically styled to look dimmer.

### dock\_gutter [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.dock_gutter "Permanent link")

```
dock_gutter
```

Space allocated to docks in the parent.

Returns:

| Type | Description |
| --- | --- |
| `[Spacing](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing " Spacing (textual.geometry.Spacing)")` | Space to be subtracted from scrollable area. |

### expand [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.expand "Permanent link")

```
expand = Reactive(False)
```

Rich renderable may expand beyond optimal size.

### first\_of\_type [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.first_of_type "Permanent link")

```
first_of_type
```

Is this the first widget of its type in its siblings?

### focusable [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.focusable "Permanent link")

```
focusable
```

Can this widget currently be focused?

### gutter [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.gutter "Permanent link")

```
gutter
```

Spacing for padding / border / scrollbars.

Returns:

| Type | Description |
| --- | --- |
| `[Spacing](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing " Spacing (textual.geometry.Spacing)")` | Additional spacing around content area. |

### has\_focus [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.has_focus "Permanent link")

```
has_focus = Reactive(False, repaint=False)
```

Does this widget have focus? Read only.

### has\_focus\_within [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.has_focus_within "Permanent link")

```
has_focus_within
```

Are any descendants focused?

### highlight\_link\_id [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.highlight_link_id "Permanent link")

```
highlight_link_id = Reactive('')
```

The currently highlighted link id. Read only.

### horizontal\_scrollbar [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.horizontal_scrollbar "Permanent link")

```
horizontal_scrollbar
```

The horizontal scrollbar.

Note

This will *create* a scrollbar if one doesn't exist.

Returns:

| Type | Description |
| --- | --- |
| `[ScrollBar](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBar " ScrollBar (textual.scrollbar.ScrollBar)")` | ScrollBar Widget. |

### hover\_style [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.hover_style "Permanent link")

```
hover_style = Reactive(Style, repaint=False)
```

The current hover style (style under the mouse cursor). Read only.

### is\_anchored [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_anchored "Permanent link")

```
is_anchored
```

Is this widget anchored?

### is\_container [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_container "Permanent link")

```
is_container
```

Is this widget a container (contains other widgets)?

### is\_disabled [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_disabled "Permanent link")

```
is_disabled
```

Is the widget disabled either because `disabled=True` or an ancestor has `disabled=True`.

### is\_even [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_even "Permanent link")

```
is_even
```

Is this widget at an evenly numbered position within its siblings?

### is\_horizontal\_scroll\_end [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_horizontal_scroll_end "Permanent link")

```
is_horizontal_scroll_end
```

Is the horizontal scroll position at the maximum?

### is\_horizontal\_scrollbar\_grabbed [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_horizontal_scrollbar_grabbed "Permanent link")

```
is_horizontal_scrollbar_grabbed
```

Is the user dragging the vertical scrollbar?

### is\_in\_maximized\_view [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_in_maximized_view "Permanent link")

```
is_in_maximized_view
```

Is this widget, or a parent maximized?

### is\_maximized [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_maximized "Permanent link")

```
is_maximized
```

Is this widget maximized?

### is\_mounted [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_mounted "Permanent link")

```
is_mounted
```

Check if this widget is mounted.

### is\_mouse\_over [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_mouse_over "Permanent link")

```
is_mouse_over
```

Is the mouse currently over this widget?

Note this will be `True` if the mouse pointer is within the widget's region, even if the mouse pointer is not directly over the widget (there could be another widget between the mouse pointer and self).

### is\_odd [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_odd "Permanent link")

```
is_odd
```

Is this widget at an oddly numbered position within its siblings?

### is\_on\_screen [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_on_screen "Permanent link")

```
is_on_screen
```

Check if the node was displayed in the last screen update.

### is\_scrollable [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_scrollable "Permanent link")

```
is_scrollable
```

Can this widget be scrolled?

### is\_scrolling [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_scrolling "Permanent link")

```
is_scrolling
```

Is this widget currently scrolling?

### is\_vertical\_scroll\_end [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_vertical_scroll_end "Permanent link")

```
is_vertical_scroll_end
```

Is the vertical scroll position at the maximum?

### is\_vertical\_scrollbar\_grabbed [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.is_vertical_scrollbar_grabbed "Permanent link")

```
is_vertical_scrollbar_grabbed
```

Is the user dragging the vertical scrollbar?

### last\_of\_type [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.last_of_type "Permanent link")

```
last_of_type
```

Is this the last widget of its type in its siblings?

### layer [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.layer "Permanent link")

```
layer
```

Get the name of this widgets layer.

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of layer. |

### layers [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.layers "Permanent link")

```
layers
```

Layers of from parent.

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...]` | Tuple of layer names. |

### layout [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.layout "Permanent link")

```
layout
```

Get the layout object if set in styles, or a default layout.

Returns:

| Type | Description |
| --- | --- |
| `[Layout](https://textual.textualize.io/api/layout/#textual.layout.Layout " Layout (textual.layout.Layout)")` | A layout object. |

### link\_style [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.link_style "Permanent link")

```
link_style
```

Style of links.

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | Rich style. |

### link\_style\_hover [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.link_style_hover "Permanent link")

```
link_style_hover
```

Style of links underneath the mouse cursor.

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | Rich Style. |

```
loading = Reactive(False)
```

If set to `True` this widget will temporarily be replaced with a loading indicator.

### lock [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.lock "Permanent link")

```
lock = RLock()
```

`asyncio` lock to be used to synchronize the state of the widget.

Two different tasks might call methods on a widget at the same time, which might result in a race condition. This can be fixed by adding `async with widget.lock:` around the method calls.

### max\_scroll\_x [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.max_scroll_x "Permanent link")

```
max_scroll_x
```

The maximum value of `scroll_x`.

### max\_scroll\_y [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.max_scroll_y "Permanent link")

```
max_scroll_y
```

The maximum value of `scroll_y`.

### mouse\_hover [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mouse_hover "Permanent link")

```
mouse_hover = Reactive(False, repaint=False)
```

Is the mouse over this widget? Read only.

### offset [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.offset "Permanent link")

```
offset
```

Widget offset from origin.

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | Relative offset. |

### opacity [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.opacity "Permanent link")

```
opacity
```

Total opacity of widget.

### outer\_size [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.outer_size "Permanent link")

```
outer_size
```

The size of the widget (including padding and border).

Returns:

| Type | Description |
| --- | --- |
| `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Outer size. |

### region [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.region "Permanent link")

```
region
```

The region occupied by this widget, relative to the Screen.

Raises:

| Type | Description |
| --- | --- |
| `[NoScreen](https://textual.textualize.io/api/dom_node/#textual.dom.NoScreen " NoScreen (textual.dom.NoScreen)")` | If there is no screen. |
| `[NoWidget](https://textual.textualize.io/api/errors/#textual.errors.NoWidget " NoWidget (textual.errors.NoWidget)")` | If the widget is not on the screen. |

Returns:

| Type | Description |
| --- | --- |
| `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | Region within screen occupied by widget. |

### scroll\_offset [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_offset "Permanent link")

```
scroll_offset
```

Get the current scroll offset.

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | Offset a container has been scrolled by. |

### scroll\_target\_x [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_target_x "Permanent link")

```
scroll_target_x = Reactive(0.0, repaint=False)
```

Scroll target destination, X coord.

### scroll\_target\_y [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_target_y "Permanent link")

```
scroll_target_y = Reactive(0.0, repaint=False)
```

Scroll target destination, Y coord.

### scroll\_x [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_x "Permanent link")

```
scroll_x = Reactive(0.0, repaint=False, layout=False)
```

The scroll position on the X axis.

### scroll\_y [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_y "Permanent link")

```
scroll_y = Reactive(0.0, repaint=False, layout=False)
```

The scroll position on the Y axis.

### scrollable\_content\_region [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scrollable_content_region "Permanent link")

```
scrollable_content_region
```

Gets an absolute region containing the scrollable content (minus padding, border, and scrollbars).

Returns:

| Type | Description |
| --- | --- |
| `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | Screen region that contains a widget's content. |

### scrollable\_size [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scrollable_size "Permanent link")

```
scrollable_size
```

The size of the scrollable content.

Returns:

| Type | Description |
| --- | --- |
| `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Scrollable content size. |

### scrollbar\_corner [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scrollbar_corner "Permanent link")

```
scrollbar_corner
```

The scrollbar corner.

Note

This will *create* a scrollbar corner if one doesn't exist.

Returns:

| Type | Description |
| --- | --- |
| `[ScrollBarCorner](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBarCorner " ScrollBarCorner (textual.scrollbar.ScrollBarCorner)")` | ScrollBarCorner Widget. |

### scrollbar\_gutter [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scrollbar_gutter "Permanent link")

```
scrollbar_gutter
```

Spacing required to fit scrollbar(s).

Returns:

| Type | Description |
| --- | --- |
| `[Spacing](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing " Spacing (textual.geometry.Spacing)")` | Scrollbar gutter spacing. |

### scrollbar\_size\_horizontal [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scrollbar_size_horizontal "Permanent link")

```
scrollbar_size_horizontal
```

Get the height used by the *horizontal* scrollbar.

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | Number of rows in the horizontal scrollbar. |

### scrollbar\_size\_vertical [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scrollbar_size_vertical "Permanent link")

```
scrollbar_size_vertical
```

Get the width used by the *vertical* scrollbar.

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | Number of columns in the vertical scrollbar. |

### scrollbars\_enabled [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scrollbars_enabled "Permanent link")

```
scrollbars_enabled
```

A tuple of booleans that indicate if scrollbars are enabled.

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[bool](https://docs.python.org/3/library/functions.html#bool), [bool](https://docs.python.org/3/library/functions.html#bool)]` | A tuple of (, ) |

### scrollbars\_space [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scrollbars_space "Permanent link")

```
scrollbars_space
```

The number of cells occupied by scrollbars for width and height

### select\_container [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.select_container "Permanent link")

```
select_container
```

The widget's container used when selecting text..

Returns:

| Type | Description |
| --- | --- |
|  | A widget which contains this widget. |

### show\_horizontal\_scrollbar [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.show_horizontal_scrollbar "Permanent link")

```
show_horizontal_scrollbar = Reactive(False, layout=True)
```

Show a horizontal scrollbar?

### show\_vertical\_scrollbar [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.show_vertical_scrollbar "Permanent link")

```
show_vertical_scrollbar = Reactive(False, layout=True)
```

Show a vertical scrollbar?

### shrink [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.shrink "Permanent link")

```
shrink = Reactive(True)
```

Rich renderable may shrink below optimal size.

### siblings [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.siblings "Permanent link")

```
siblings
```

Get the widget's siblings (self is removed from the return list).

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of siblings. |

### size [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.size "Permanent link")

```
size
```

The size of the content area.

Returns:

| Type | Description |
| --- | --- |
| `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Content area size. |

### text\_selection [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.text_selection "Permanent link")

```
text_selection
```

Text selection information, or `None` if no text is selected in this widget.

```
tooltip
```

Tooltip for the widget, or `None` for no tooltip.

### vertical\_scrollbar [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.vertical_scrollbar "Permanent link")

```
vertical_scrollbar
```

The vertical scrollbar (create if necessary).

Note

This will *create* a scrollbar if one doesn't exist.

Returns:

| Type | Description |
| --- | --- |
| `[ScrollBar](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBar " ScrollBar (textual.scrollbar.ScrollBar)")` | ScrollBar Widget. |

### virtual\_region [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.virtual_region "Permanent link")

```
virtual_region
```

The widget region relative to its container (which may not be visible, depending on scroll offset).

Returns:

| Type | Description |
| --- | --- |
| `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | The virtual region. |

### virtual\_region\_with\_margin [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.virtual_region_with_margin "Permanent link")

```
virtual_region_with_margin
```

The widget region relative to its container (*including margin*), which may not be visible, depending on the scroll offset.

Returns:

| Type | Description |
| --- | --- |
| `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | The virtual region of the Widget, inclusive of its margin. |

### virtual\_size [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.virtual_size "Permanent link")

```
virtual_size = Reactive(Size(0, 0), layout=True)
```

The virtual (scrollable) [size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size") of the widget.

### visible\_siblings [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.visible_siblings "Permanent link")

```
visible_siblings
```

A list of siblings which will be shown.

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | List of siblings. |

### window\_region [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.window_region "Permanent link")

```
window_region
```

The region within the scrollable area that is currently visible.

Returns:

| Type | Description |
| --- | --- |
| `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | New region. |

### allow\_focus [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.allow_focus "Permanent link")

```
allow_focus()
```

Check if the widget is permitted to focus.

The base class returns . This method may be overridden if additional logic is required.

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the widget may be focused, or `False` if it may not be focused. |

### allow\_focus\_children [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.allow_focus_children "Permanent link")

```
allow_focus_children()
```

Check if a widget's children may be focused.

The base class returns . This method may be overridden if additional logic is required.

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the widget's children may be focused, or `False` if the widget's children may not be focused. |

### anchor [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.anchor "Permanent link")

```
anchor(*, =False)
```

Anchor the widget, which scrolls it into view (like ), but also keeps it in view if the widget's size changes, or the size of its container changes.

Note

Anchored widgets will be un-anchored if the users scrolls the container.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.anchor\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the scroll should animate, or `False` if it shouldn't. | `False` |

### animate [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate "Permanent link")

```
animate(
    ,
    ,
    *,
    =...,
    =None,
    =None,
    =0.0,
    =DEFAULT_EASING,
    =None,
    ="full"
)
```

Animate an attribute.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `attribute` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate\(attribute\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of the attribute to animate. | *required* |
| #### `value` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate\(value\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| [Animatable](https://textual.textualize.io/api/types/#textual.types.Animatable " Animatable (textual._animator.Animatable)")` | The value to animate to. | *required* |
| #### `final_value` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate\(final_value\) "Permanent link") | `[object](https://docs.python.org/3/library/functions.html#object)` | The final value of the animation. Defaults to `value` if not set. | `...` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The duration (in seconds) of the animation. | `None` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The speed of the animation. | `None` |
| #### `delay` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate\(delay\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | A delay (in seconds) before the animation starts. | `0.0` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | An easing method. | `DEFAULT_EASING` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.animate\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'full'` |

### batch [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.batch "Permanent link")

```
batch()
```

Async context manager that combines widget locking and update batching.

Use this async context manager whenever you want to acquire the widget lock and batch app updates at the same time.

Example
```
async with container.batch():
    await container.remove_children(Button)
    await container.mount(Label("All buttons are gone."))
```

### begin\_capture\_print [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.begin_capture_print "Permanent link")

```
begin_capture_print(=True, =True)
```

Capture text from print statements (or writes to stdout / stderr).

If printing is captured, the widget will be sent an [`events.Print`](https://textual.textualize.io/api/events/#textual.events.Print " Print") message.

Call to disable print capture.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `stdout` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.begin_capture_print\(stdout\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to capture stdout. | `True` |
| #### `stderr` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.begin_capture_print\(stderr\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to capture stderr. | `True` |

### blur [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.blur "Permanent link")

```
blur()
```

Blur (un-focus) the widget.

Focus will be moved to the next available widget in the focus chain.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Widget` instance. |

### can\_view\_entire [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.can_view_entire "Permanent link")

```
can_view_entire()
```

Check if a given widget is *fully* within the current view (scrollable area).

Note: This doesn't necessarily equate to a widget being visible. There are other reasons why a widget may not be visible.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.can_view_entire\(widget\) "Permanent link") |  | A widget that is a descendant of self. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the entire widget is in view, `False` if it is partially visible or not in view. |

### can\_view\_partial [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.can_view_partial "Permanent link")

```
can_view_partial()
```

Check if a given widget at least partially visible within the current view (scrollable area).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.can_view_partial\(widget\) "Permanent link") |  | A widget that is a descendant of self. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if any part of the widget is visible, `False` if it is outside of the viewable area. |

### capture\_mouse [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.capture_mouse "Permanent link")

```
capture_mouse(=True)
```

Capture (or release) the mouse.

When captured, mouse events will go to this widget even when the pointer is not directly over the widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `capture` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.capture_mouse\(capture\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True to capture or False to release. | `True` |

### check\_message\_enabled [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.check_message_enabled "Permanent link")

```
check_message_enabled()
```

Check if a given message is enabled (allowed to be sent).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `message` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.check_message_enabled\(message\) "Permanent link") | `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")` | A message object | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the message will be sent, or `False` if it is disabled. |

### clear\_anchor [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.clear_anchor "Permanent link")

```
clear_anchor()
```

Stop anchoring this widget (a no-op if this widget is not anchored).

### clear\_cached\_dimensions [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.clear_cached_dimensions "Permanent link")

```
clear_cached_dimensions()
```

Clear cached results of `get_content_width` and `get_content_height`.

Call if the widget's renderable changes size after the widget has been created.

Note

This is not required if you are extending [`Static`](https://textual.textualize.io/widgets/static/#textual.widgets.Static " Static").

### compose [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.compose "Permanent link")

```
compose()
```

Called by Textual to create child widgets.

This method is called when a widget is mounted or by setting `recompose=True` when calling .

Note that you don't typically need to explicitly call this method.

Example
```
def compose(self) -> ComposeResult:
    yield Header()
    yield Label("Press the button below:")
    yield Button()
    yield Footer()
```

### compose\_add\_child [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.compose_add_child "Permanent link")

```
compose_add_child()
```

Add a node to children.

This is used by the compose process when it adds children. There is no need to use it directly, but you may want to override it in a subclass if you want children to be attached to a different node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.compose_add_child\(widget\) "Permanent link") |  | A Widget to add. | *required* |

### end\_capture\_print [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.end_capture_print "Permanent link")

```
end_capture_print()
```

End print capture (set with ).

### focus [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.focus "Permanent link")

```
focus(=True)
```

Give focus to this widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `scroll_visible` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.focus\(scroll_visible\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Scroll parent to make this widget visible. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Widget` instance. |

### get\_child\_by\_id [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_child_by_id "Permanent link")

```
get_child_by_id(: str) ->
```
```
get_child_by_id(
    : str, : type[ExpectType]
) -> ExpectType
```

```
get_child_by_id(, =None)
```

Return the first child (immediate descendent) of this node with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `id` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_child_by_id\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the child. | *required* |
| #### `expect_type` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_child_by_id\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[ExpectType] \| None` | Require the object be of the supplied type, or None for any type. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `ExpectType \| ` | The first child of this node with the ID. |

Raises:

| Type | Description |
| --- | --- |
| `[NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches (textual.css.query.NoMatches)")` | if no children could be found for this ID |
| `[WrongType](https://textual.textualize.io/api/query/#textual.css.query.WrongType " WrongType (textual.css.query.WrongType)")` | if the wrong type was found. |

### get\_child\_by\_type [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_child_by_type "Permanent link")

```
get_child_by_type()
```

Get the first immediate child of a given type.

Only returns exact matches, and so will not match subclasses of the given type.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `expect_type` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_child_by_type\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[ExpectType]` | The type of the child to search for. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches (textual.css.query.NoMatches)")` | If no matching child is found. |

Returns:

| Type | Description |
| --- | --- |
| `ExpectType` | The first immediate child widget with the expected type. |

### get\_component\_rich\_style [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_component_rich_style "Permanent link")

```
get_component_rich_style(*names, =False)
```

Get a *Rich* style for a component.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `names` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_component_rich_style\(names\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Names of components. | `()` |
| #### `partial` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_component_rich_style\(partial\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Return a partial style (not combined with parent). | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | A Rich style object. |

### get\_content\_height [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_content_height "Permanent link")

```
get_content_height(, , )
```

Called by Textual to get the height of the content area. May be overridden in a subclass.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `container` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_content_height\(container\) "Permanent link") | `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Size of the container (immediate parent) widget. | *required* |
| #### `viewport` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_content_height\(viewport\) "Permanent link") | `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Size of the viewport. | *required* |
| #### `width` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_content_height\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Width of renderable. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The height of the content. |

### get\_content\_width [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_content_width "Permanent link")

```
get_content_width(, )
```

Called by textual to get the width of the content area. May be overridden in a subclass.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `container` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_content_width\(container\) "Permanent link") | `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Size of the container (immediate parent) widget. | *required* |
| #### `viewport` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_content_width\(viewport\) "Permanent link") | `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Size of the viewport. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The optimal width of the content. |

```
get_loading_widget()
```

Get a widget to display a loading indicator.

The default implementation will defer to App.get\_loading\_widget.

Returns:

| Type | Description |
| --- | --- |
|  | A widget in place of this widget to indicate a loading. |

### get\_pseudo\_class\_state [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_pseudo_class_state "Permanent link")

```
get_pseudo_class_state()
```

Get an object describing whether each pseudo class is present on this object or not.

Returns:

| Type | Description |
| --- | --- |
|  | A PseudoClasses object describing the pseudo classes that are present. |

### get\_selection [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_selection "Permanent link")

```
get_selection(selection)
```

Get the text under the selection.

```
Args:
        selection: Selection information.

    Returns:
        Tuple of extracted text and ending (typically "
```

" or " "), or `None` if no text could be extracted.

### get\_style\_at [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_style_at "Permanent link")

```
get_style_at(, )
```

Get the Rich style in a widget at a given relative offset.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_style_at\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | X coordinate relative to the widget. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_style_at\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y coordinate relative to the widget. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | A rich Style object. |

### get\_visual\_style [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_visual_style "Permanent link")

```
get_visual_style(*component_classes, =False)
```

Get the visual style for the widget, including any component styles.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `component_classes` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_visual_style\(component_classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Optional component styles. | `()` |
| #### `partial` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_visual_style\(partial\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Return a partial style (not combined with parent). | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://textual.textualize.io/api/style/#textual.style.Style " Style (textual.style.Style)")` | A Visual style instance. |

### get\_widget\_by\_id [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_widget_by_id "Permanent link")

```
get_widget_by_id(: str) ->
```
```
get_widget_by_id(
    : str, : type[ExpectType]
) -> ExpectType
```

```
get_widget_by_id(, =None)
```

Return the first descendant widget with the given ID.

Performs a depth-first search rooted at this widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `id` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_widget_by_id\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID to search for in the subtree. | *required* |
| #### `expect_type` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.get_widget_by_id\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[ExpectType] \| None` | Require the object be of the supplied type, or None for any type. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `ExpectType \| ` | The first descendant encountered with this ID. |

Raises:

| Type | Description |
| --- | --- |
| `[NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches (textual.css.query.NoMatches)")` | if no children could be found for this ID. |
| `[WrongType](https://textual.textualize.io/api/query/#textual.css.query.WrongType " WrongType (textual.css.query.WrongType)")` | if the wrong type was found. |

### mount [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount "Permanent link")

```
mount(*, =None, =None)
```

Mount widgets below this widget (making this widget a container).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*widgets` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount\(*widgets\) "Permanent link") |  | The widget(s) to mount. | `()` |
| #### `before` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount\(before\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [str](https://docs.python.org/3/library/stdtypes.html#str) \|  \| None` | Optional location to mount before. An `int` is the index of the child to mount before, a `str` is a `query_one` query to find the widget to mount before. | `None` |
| #### `after` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount\(after\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [str](https://docs.python.org/3/library/stdtypes.html#str) \|  \| None` | Optional location to mount after. An `int` is the index of the child to mount after, a `str` is a `query_one` query to find the widget to mount after. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | An awaitable object that waits for widgets to be mounted. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is a problem with the mount request. |

Note

Only one of `before` or `after` can be provided. If both are provided a `MountError` will be raised.

### mount\_all [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount_all "Permanent link")

```
mount_all(, *, =None, =None)
```

Mount widgets from an iterable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widgets` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount_all\(widgets\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | An iterable of widgets. | *required* |
| #### `before` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount_all\(before\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [str](https://docs.python.org/3/library/stdtypes.html#str) \|  \| None` | Optional location to mount before. An `int` is the index of the child to mount before, a `str` is a `query_one` query to find the widget to mount before. | `None` |
| #### `after` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount_all\(after\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [str](https://docs.python.org/3/library/stdtypes.html#str) \|  \| None` | Optional location to mount after. An `int` is the index of the child to mount after, a `str` is a `query_one` query to find the widget to mount after. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | An awaitable object that waits for widgets to be mounted. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is a problem with the mount request. |

Note

Only one of `before` or `after` can be provided. If both are provided a `MountError` will be raised.

### mount\_composed\_widgets [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount_composed_widgets "Permanent link")

```
mount_composed_widgets()
```

Called by Textual to mount widgets after compose.

There is generally no need to implement this method in your application. See [Lazy](https://textual.textualize.io/api/lazy/#textual.lazy.Lazy " Lazy") for a class which uses this method to implement *lazy* mounting.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widgets` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.mount_composed_widgets\(widgets\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of child widgets. | *required* |

### move\_child [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.move_child "Permanent link")

```
move_child(
    : int | ,
    *,
    : int | ,
    : None = None
) -> None
```
```
move_child(
    : int | ,
    *,
    : int | ,
    : None = None
) -> None
```

```
move_child(, *, =None, =None)
```

Move a child widget within its parent's list of children.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `child` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.move_child\(child\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| ` | The child widget to move. | *required* |
| #### `before` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.move_child\(before\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \|  \| None` | Child widget or location index to move before. | `None` |
| #### `after` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.move_child\(after\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \|  \| None` | Child widget or location index to move after. | `None` |

Raises:

| Type | Description |
| --- | --- |
|  | If there is a problem with the child or target. |

Note

Only one of `before` or `after` can be provided. If neither or both are provided a `WidgetError` will be raised.

### notify [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.notify "Permanent link")

```
notify(
    ,
    *,
    ="",
    ="information",
    =None
)
```

Create a notification.

Tip

This method is thread-safe.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `message` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.notify\(message\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The message for the notification. | *required* |
| #### `title` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.notify\(title\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The title for the notification. | `''` |
| #### `severity` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.notify\(severity\) "Permanent link") | `SeverityLevel` | The severity of the notification. | `'information'` |
| #### `timeout` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.notify\(timeout\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The timeout (in seconds) for the notification, or `None` for default. | `None` |

See [`App.notify`](https://textual.textualize.io/api/app/#textual.app.App.notify " notify") for the full documentation for this method.

### on\_prune [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.on_prune "Permanent link")

```
on_prune(event)
```

Close message loop when asked to prune.

### post\_message [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.post_message "Permanent link")

```
post_message()
```

Post a message to this widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `message` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.post_message\(message\) "Permanent link") | `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")` | Message to post. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the message was posted, False if this widget was closed / closing. |

### post\_render [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.post_render "Permanent link")

```
post_render(renderable, base_style)
```

Applies style attributes to the default renderable.

This method is called by Textual itself. It is unlikely you will need to call or implement this method.

Returns:

| Type | Description |
| --- | --- |
| `[ConsoleRenderable](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.ConsoleRenderable "rich.console.ConsoleRenderable")` | A new renderable. |

### pre\_layout [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.pre_layout "Permanent link")

```
pre_layout()
```

This method id called prior to a layout operation.

Implement this method if you want to make updates that should impact the layout.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `layout` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.pre_layout\(layout\) "Permanent link") | `[Layout](https://textual.textualize.io/api/layout/#textual.layout.Layout " Layout (textual.layout.Layout)")` | The [Layout](https://textual.textualize.io/api/layout/#textual.layout.Layout " Layout") instance that will be used to arrange this widget's children. | *required* |

### preflight\_checks [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.preflight_checks "Permanent link")

```
preflight_checks()
```

Called in debug mode to do preflight checks.

This is used by Textual to log some common errors, but you could implement this in custom widgets to perform additional checks.

### recompose [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.recompose "Permanent link")

```
recompose()
```

Recompose the widget.

Recomposing will remove children and call `self.compose` again to remount.

### refresh [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.refresh "Permanent link")

```
refresh(
    *, =True, =False, =False
)
```

Initiate a refresh of the widget.

This method sets an internal flag to perform a refresh, which will be done on the next idle event. Only one refresh will be done even if this method is called multiple times.

By default this method will cause the content of the widget to refresh, but not change its size. You can also set `layout=True` to perform a layout.

Warning

It is rarely necessary to call this method explicitly. Updating styles or reactive attributes will do this automatically.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*regions` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.refresh\(*regions\) "Permanent link") | `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | Additional screen regions to mark as dirty. | `()` |
| #### `repaint` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.refresh\(repaint\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Repaint the widget (will call render() again). | `True` |
| #### `layout` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.refresh\(layout\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Also layout widgets in the view. | `False` |
| #### `recompose` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.refresh\(recompose\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Re-compose the widget (will remove and re-mount children). | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Widget` instance. |

### release\_mouse [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.release_mouse "Permanent link")

```
release_mouse()
```

Release the mouse.

Mouse events will only be sent when the mouse is over the widget.

### remove [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.remove "Permanent link")

```
remove()
```

Remove the Widget from the DOM (effectively deleting it).

Returns:

| Type | Description |
| --- | --- |
| `[AwaitRemove](https://textual.textualize.io/api/await_remove/#textual.await_remove.AwaitRemove " AwaitRemove (textual.await_remove.AwaitRemove)")` | An awaitable object that waits for the widget to be removed. |

### remove\_children [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.remove_children "Permanent link")

```
remove_children(='*')
```

Remove the immediate children of this Widget from the DOM.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.remove_children\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")] \| [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | A CSS selector or iterable of widgets to remove. | `'*'` |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitRemove](https://textual.textualize.io/api/await_remove/#textual.await_remove.AwaitRemove " AwaitRemove (textual.await_remove.AwaitRemove)")` | An awaitable object that waits for the direct children to be removed. |

### render [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.render "Permanent link")

```
render()
```

Get [content](https://textual.textualize.io/guide/content) for the widget.

Implement this method in a subclass for custom widgets.

This method should return [markup](https://textual.textualize.io/guide/content#markup), a [Content](https://textual.textualize.io/api/content/#textual.content.Content " Content") object, or a [Rich](https://github.com/Textualize/rich) renderable.

Example
```
from textual.app import RenderResult
from textual.widget import Widget

class CustomWidget(Widget):
    def render(self) -> RenderResult:
        return "Welcome to [bold red]Textual[/]!"
```

Returns:

| Type | Description |
| --- | --- |
| `[RenderResult](https://textual.textualize.io/api/app/#textual.app.RenderResult " RenderResult (textual.app.RenderResult)")` | A string or object to render as the widget's content. |

### render\_line [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.render_line "Permanent link")

```
render_line()
```

Render a line of content.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `y` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.render_line\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y Coordinate of line. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Strip](https://textual.textualize.io/api/strip/#textual.strip.Strip " Strip (textual.strip.Strip)")` | A rendered line. |

### render\_lines [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.render_lines "Permanent link")

```
render_lines()
```

Render the widget into lines.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `crop` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.render_lines\(crop\) "Permanent link") | `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | Region within visible area to render. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Strip](https://textual.textualize.io/api/strip/#textual.strip.Strip " Strip (textual.strip.Strip)")]` | A list of list of segments. |

### render\_str [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.render_str "Permanent link")

```
render_str(: str) -> Content
```
```
render_str(: Content) -> Content
```

```
render_str()
```

Convert str into a [Content](https://textual.textualize.io/api/content/#textual.content.Content " Content") instance.

If you pass in an existing Content instance it will be returned unaltered.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `text_content` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.render_str\(text_content\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Content](https://textual.textualize.io/api/content/#textual.content.Content " Content (textual.content.Content)")` | Content or str. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Content](https://textual.textualize.io/api/content/#textual.content.Content " Content (textual.content.Content)")` | Content object. |

### run\_action [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.run_action "Permanent link")

```
run_action()
```

Perform a given action, with this widget as the default namespace.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `action` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.run_action\(action\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Action encoded as a string. | *required* |

### scroll\_down [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_down "Permanent link")

```
scroll_down(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic",
    =False
)
```

Scroll one line down.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_down\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_down\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if `animate` is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_down\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_down\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_down\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_down\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_down\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_down\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

### scroll\_end [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end "Permanent link")

```
scroll_end(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic",
    =False,
    =True,
    =True
)
```

Scroll to the end of the container.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if `animate` is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |
| #### `x_axis` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(x_axis\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow scrolling on X axis? | `True` |
| #### `y_axis` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_end\(y_axis\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow scrolling on Y axis? | `True` |

### scroll\_home [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home "Permanent link")

```
scroll_home(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic",
    =False,
    =True,
    =True
)
```

Scroll to home position.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if animate is `True`; or `None` to use duration. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |
| #### `x_axis` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(x_axis\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow scrolling on X axis? | `True` |
| #### `y_axis` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_home\(y_axis\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow scrolling on Y axis? | `True` |

### scroll\_left [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_left "Permanent link")

```
scroll_left(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic",
    =False
)
```

Scroll one cell left.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_left\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_left\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if `animate` is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_left\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_left\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_left\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_left\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_left\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_left\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

### scroll\_page\_down [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_down "Permanent link")

```
scroll_page_down(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic"
)
```

Scroll one page down.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_down\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_down\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if animate is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_down\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_down\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_down\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_down\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_down\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |

### scroll\_page\_left [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_left "Permanent link")

```
scroll_page_left(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic"
)
```

Scroll one page left.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_left\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_left\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if animate is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_left\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_left\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_left\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_left\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_left\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |

### scroll\_page\_right [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_right "Permanent link")

```
scroll_page_right(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic"
)
```

Scroll one page right.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_right\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_right\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if animate is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_right\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_right\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_right\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_right\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_right\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |

### scroll\_page\_up [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_up "Permanent link")

```
scroll_page_up(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic"
)
```

Scroll one page up.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_up\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_up\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if animate is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_up\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_up\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_up\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_up\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_page_up\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |

### scroll\_relative [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative "Permanent link")

```
scroll_relative(
    =None,
    =None,
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic",
    =False
)
```

Scroll relative to current position.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(x\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | X distance (columns) to scroll, or `None` for no change. | `None` |
| #### `y` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(y\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Y distance (rows) to scroll, or `None` for no change. | `None` |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate to new scroll position. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if `animate` is `True`. Or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if animate is `True` and speed is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_relative\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

### scroll\_right [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_right "Permanent link")

```
scroll_right(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic",
    =False
)
```

Scroll one cell right.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_right\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_right\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if animate is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_right\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_right\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_right\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_right\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_right\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_right\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

### scroll\_to [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to "Permanent link")

```
scroll_to(
    =None,
    =None,
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic",
    =False
)
```

Scroll to a given (absolute) coordinate, optionally animating.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(x\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | X coordinate (column) to scroll to, or `None` for no change. | `None` |
| #### `y` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(y\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Y coordinate (row) to scroll to, or `None` for no change. | `None` |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate to new scroll position. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if `animate` is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

Note

The call to scroll is made after the next refresh.

### scroll\_to\_center [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center "Permanent link")

```
scroll_to_center(
    ,
    =True,
    *,
    =None,
    =None,
    =None,
    =False,
    =True,
    =None,
    ="basic",
    =False
)
```

Scroll this widget to the center of self.

The center of the widget will be scrolled to the center of the container.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(widget\) "Permanent link") |  | The widget to scroll to the center of self. | *required* |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to animate the scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if animate is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `origin_visible` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(origin_visible\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Ensure that the top left corner of the widget remains visible after the scroll. | `True` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_center\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

### scroll\_to\_region [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region "Permanent link")

```
scroll_to_region(
    ,
    *,
    =None,
    =True,
    =None,
    =None,
    =None,
    center=False,
    =False,
    =True,
    =False,
    =None,
    ="basic",
    =True,
    =True,
    =False
)
```

Scrolls a given region into view, if required.

This method will scroll the least distance required to move `region` fully within the scrollable area.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `region` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(region\) "Permanent link") | `[Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")` | A region that should be visible. | *required* |
| #### `spacing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(spacing\) "Permanent link") | `[Spacing](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing " Spacing (textual.geometry.Spacing)") \| None` | Optional spacing around the region. | `None` |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` to animate, or `False` to jump. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if `animate` is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `top` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(top\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Scroll `region` to top of container. | `False` |
| #### `origin_visible` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(origin_visible\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Ensure that the top left of the widget is within the window. | `True` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `x_axis` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(x_axis\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow scrolling on X axis? | `True` |
| #### `y_axis` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(y_axis\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow scrolling on Y axis? | `True` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_region\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | The distance that was scrolled. |

### scroll\_to\_widget [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget "Permanent link")

```
scroll_to_widget(
    ,
    *,
    =True,
    =None,
    =None,
    =None,
    center=False,
    =False,
    =True,
    =False,
    =None,
    ="basic",
    =False
)
```

Scroll scrolling to bring a widget into view.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(widget\) "Permanent link") |  | A descendant widget. | *required* |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` to animate, or `False` to jump. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if `animate` is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `top` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(top\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Scroll widget to top of container. | `False` |
| #### `origin_visible` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(origin_visible\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Ensure that the top left of the widget is within the window. | `True` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_to_widget\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if any scrolling has occurred in any descendant, otherwise `False`. |

### scroll\_up [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_up "Permanent link")

```
scroll_up(
    *,
    =True,
    =None,
    =None,
    =None,
    =False,
    =None,
    ="basic",
    =False
)
```

Scroll one line up.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_up\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_up\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if `animate` is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_up\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and speed is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_up\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_up\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_up\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_up\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_up\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

### scroll\_visible [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible "Permanent link")

```
scroll_visible(
    =True,
    *,
    =None,
    =None,
    =False,
    =None,
    =False,
    =None,
    ="basic",
    =False
)
```

Scroll the container to make this widget visible.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scroll. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if animate is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `top` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible\(top\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Scroll to top of container. | `False` |
| #### `easing` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.scroll_visible\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |

### selection\_updated [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.selection_updated "Permanent link")

```
selection_updated()
```

Called when the selection is updated.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selection` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.selection_updated\(selection\) "Permanent link") | `Selection \| None` | Selection information or `None` if no selection. | *required* |

```
set_loading()
```

Set or reset the loading state of this widget.

A widget in a loading state will display a LoadingIndicator that obscures the widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  | `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` to put the widget into a loading state, or `False` to reset the loading state. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `None` | An optional awaitable. |

### set\_scroll [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.set_scroll "Permanent link")

```
set_scroll(, )
```

Set the scroll position without any validation.

This is a low-level method for when you want to see the scroll position in the next frame. For a more fully featured method, see .

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.set_scroll\(x\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Desired `X` coordinate. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.set_scroll\(y\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Desired `Y` coordinate. | *required* |

### stop\_animation [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.stop_animation "Permanent link")

```
stop_animation(, =True)
```

Stop an animation on an attribute.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `attribute` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.stop_animation\(attribute\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of the attribute whose animation should be stopped. | *required* |
| #### `complete` [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.stop_animation\(complete\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Should the animation be set to its final value? | `True` |

Note

If there is no animation scheduled or running, this is a no-op.

### suppress\_click [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.suppress_click "Permanent link")

```
suppress_click()
```

Suppress a click event.

This will prevent a [Click](https://textual.textualize.io/api/events/#textual.events.Click " Click") event being sent, if called after a mouse down event and before the click itself.

### text\_select\_all [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.text_select_all "Permanent link")

```
text_select_all()
```

Select the entire widget.

### watch\_disabled [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.watch_disabled "Permanent link")

```
watch_disabled(disabled)
```

Update the styles of the widget and its children when disabled is toggled.

### watch\_has\_focus [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.watch_has_focus "Permanent link")

```
watch_has_focus(value)
```

Update from CSS if has focus state changes.

### watch\_mouse\_hover [¶](https://textual.textualize.io/api/widget/#textual.widget.Widget.watch_mouse_hover "Permanent link")

```
watch_mouse_hover(value)
```

Update from CSS if mouse over state changes.

```
with_tooltip()
```

Chainable method to set a tooltip.

Example
```
def compose(self) -> ComposeResult:
    yield Label("Hello").with_tooltip("A greeting")
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | New tooltip, or `None` to clear the tooltip. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | Self. |

## WidgetError [¶](https://textual.textualize.io/api/widget/#textual.widget.WidgetError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Base widget error.