---
title: "Textual - textual.scroll_view"
source: "https://textual.textualize.io/api/scroll_view/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.scroll\_view

`ScrollView` is a base class for [Line API](https://textual.textualize.io/guide/widgets#line-api) widgets.

## ScrollView [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView "Permanent link")

```
ScrollView(
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

Bases: `[ScrollableContainer](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer " ScrollableContainer (textual.containers.ScrollableContainer)")`

A base class for a Widget that handles its own scrolling (i.e. doesn't rely on the compositor to render children).

### is\_scrollable [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.is_scrollable "Permanent link")

```
is_scrollable
```

Always scrollable.

### refresh\_line [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.refresh_line "Permanent link")

```
refresh_line()
```

Refresh a single line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `y` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.refresh_line\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Coordinate of line. | *required* |

### refresh\_lines [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.refresh_lines "Permanent link")

```
refresh_lines(, =1)
```

Refresh one or more lines.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `y_start` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.refresh_lines\(y_start\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | First line to refresh. | *required* |
| #### `line_count` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.refresh_lines\(line_count\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Total number of lines to refresh. | `1` |

### scroll\_to [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to "Permanent link")

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
| #### `x` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(x\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | X coordinate (column) to scroll to, or `None` for no change. | `None` |
| #### `y` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(y\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Y coordinate (row) to scroll to, or `None` for no change. | `None` |
| #### `animate` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate to new scroll position. | `True` |
| #### `speed` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Speed of scroll if `animate` is `True`; or `None` to use `duration`. | `None` |
| #### `duration` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Duration of animation, if `animate` is `True` and `speed` is `None`. | `None` |
| #### `easing` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An easing method for the scrolling animation. | `None` |
| #### `force` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(force\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Force scrolling even when prohibited by overflow styling. | `False` |
| #### `on_complete` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual._types.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'basic'` |
| #### `immediate` [¶](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView.scroll_to\(immediate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `False` the scroll will be deferred until after a screen refresh, set to `True` to scroll immediately. | `False` |