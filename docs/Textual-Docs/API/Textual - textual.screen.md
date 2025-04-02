---
title: "Textual - textual.screen"
source: "https://textual.textualize.io/api/screen/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.screen

This module contains the `Screen` class and related objects.

The `Screen` class is a special widget which represents the content in the terminal. See [Screens](https://textual.textualize.io/guide/screens/) for details.

## ScreenResultCallbackType [¶](https://textual.textualize.io/api/screen/#textual.screen.ScreenResultCallbackType "Permanent link")

```
ScreenResultCallbackType = Union[
    Callable[[Optional[]], None],
    Callable[[Optional[]], Awaitable[None]],
]
```

Type of a screen result callback function.

## ScreenResultType [¶](https://textual.textualize.io/api/screen/#textual.screen.ScreenResultType "Permanent link")

```
ScreenResultType = TypeVar('ScreenResultType')
```

The result type of a screen.

## ModalScreen [¶](https://textual.textualize.io/api/screen/#textual.screen.ModalScreen "Permanent link")

```
ModalScreen(name=None, id=None, classes=None)
```

Bases: `[]`

A screen with bindings that take precedence over the App's key bindings.

The default styling of a modal screen will dim the screen underneath.

## ResultCallback [¶](https://textual.textualize.io/api/screen/#textual.screen.ResultCallback "Permanent link")

```
ResultCallback(, , =None)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`

Holds the details of a callback.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `requester` [¶](https://textual.textualize.io/api/screen/#textual.screen.ResultCallback\(requester\) "Permanent link") | `[MessagePump](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump " MessagePump (textual.message_pump.MessagePump)")` | The object making a request for the callback. | *required* |
| ### `callback` [¶](https://textual.textualize.io/api/screen/#textual.screen.ResultCallback\(callback\) "Permanent link") | `[] \| None` | The callback function. | *required* |
| ### `future` [¶](https://textual.textualize.io/api/screen/#textual.screen.ResultCallback\(future\) "Permanent link") | `[Future](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")[] \| None` | A Future to hold the result. | `None` |

### callback [¶](https://textual.textualize.io/api/screen/#textual.screen.ResultCallback.callback "Permanent link")

```
callback =
```

The callback function.

### future [¶](https://textual.textualize.io/api/screen/#textual.screen.ResultCallback.future "Permanent link")

```
future =
```

A future for the result

### requester [¶](https://textual.textualize.io/api/screen/#textual.screen.ResultCallback.requester "Permanent link")

```
requester =
```

The object in the DOM that requested the callback.

## Screen [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen "Permanent link")

```
Screen(=None, =None, =None)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

The base class for screens.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `name` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the screen. | `None` |
| ### `id` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the screen in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the screen. | `None` |

### ALLOW\_IN\_MAXIMIZED\_VIEW [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.ALLOW_IN_MAXIMIZED_VIEW "Permanent link")

```
ALLOW_IN_MAXIMIZED_VIEW = None
```

A selector for the widgets (direct children of Screen) that are allowed in the maximized view (in addition to maximized widget). Or `None` to default to [App.ALLOW\_IN\_MAXIMIZED\_VIEW](https://textual.textualize.io/api/app/#textual.app.App.ALLOW_IN_MAXIMIZED_VIEW " ALLOW_IN_MAXIMIZED_VIEW")

### AUTO\_FOCUS [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.AUTO_FOCUS "Permanent link")

```
AUTO_FOCUS = None
```

A selector to determine what to focus automatically when the screen is activated.

The widget focused is the first that matches the given [CSS selector](https://textual.textualize.io/guide/queries/#query-selectors). Set to `None` to inherit the value from the screen's app. Set to `""` to disable auto focus.

### COMMANDS [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.COMMANDS "Permanent link")

```
COMMANDS = set()
```

Command providers used by the [command palette](https://textual.textualize.io/guide/command_palette), associated with the screen.

Should be a set of [`command.Provider`](https://textual.textualize.io/api/command/#textual.command.Provider " Provider") classes.

### CSS [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.CSS "Permanent link")

```
CSS = ''
```

Inline CSS, useful for quick scripts. Rules here take priority over CSS\_PATH.

Note

This CSS applies to the whole app.

### CSS\_PATH [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.CSS_PATH "Permanent link")

```
CSS_PATH = None
```

File paths to load CSS from.

Note

This CSS applies to the whole app.

### ESCAPE\_TO\_MINIMIZE [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.ESCAPE_TO_MINIMIZE "Permanent link")

```
ESCAPE_TO_MINIMIZE = None
```

Use escape key to minimize (potentially overriding bindings) or `None` to defer to [`App.ESCAPE_TO_MINIMIZE`](https://textual.textualize.io/api/app/#textual.app.App.ESCAPE_TO_MINIMIZE " ESCAPE_TO_MINIMIZE").

### SUB\_TITLE [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.SUB_TITLE "Permanent link")

```
SUB_TITLE = None
```

A class variable to set the *default* sub-title for the screen.

This overrides the app sub-title. To update the sub-title while the screen is running, you can set the attribute.

### TITLE [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.TITLE "Permanent link")

```
TITLE = None
```

A class variable to set the *default* title for the screen.

This overrides the app title. To update the title while the screen is running, you can set the attribute.

### active\_bindings [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.active_bindings "Permanent link")

```
active_bindings
```

Get currently active bindings for this screen.

If no widget is focused, then app-level bindings are returned. If a widget is focused, then any bindings present in the screen and app are merged and returned.

This property may be used to inspect current bindings.

Returns:

| Type | Description |
| --- | --- |
| `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [ActiveBinding](https://textual.textualize.io/api/binding/#textual.binding.ActiveBinding " ActiveBinding (textual.binding.ActiveBinding)")]` | A map of keys to a tuple containing (NAMESPACE, BINDING, ENABLED). |

### allow\_select [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.allow_select "Permanent link")

```
allow_select
```

Check if this widget permits text selection.

### bindings\_updated\_signal [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.bindings_updated_signal "Permanent link")

```
bindings_updated_signal = Signal(self, 'bindings_updated')
```

A signal published when the bindings have been updated

### focus\_chain [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.focus_chain "Permanent link")

```
focus_chain
```

A list of widgets that may receive focus, in focus order.

### focused [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.focused "Permanent link")

```
focused = Reactive(None)
```

The focused [widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget") or `None` for no focus. To set focus, do not update this value directly. Use instead.

### is\_active [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.is_active "Permanent link")

```
is_active
```

Is the screen active (i.e. visible and top of the stack)?

### is\_current [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.is_current "Permanent link")

```
is_current
```

Is the screen current (i.e. visible to user)?

```
is_modal
```

Is the screen modal?

### layers [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.layers "Permanent link")

```
layers
```

Layers from parent.

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...]` | Tuple of layer names. |

### maximized [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.maximized "Permanent link")

```
maximized = Reactive(None, layout=True)
```

The currently maximized widget, or `None` for no maximized widget.

### screen\_layout\_refresh\_signal [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.screen_layout_refresh_signal "Permanent link")

```
screen_layout_refresh_signal = Signal(
    self, "layout-refresh"
)
```

The signal that is published when the screen's layout is refreshed.

### selections [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.selections "Permanent link")

```
selections = var(dict)
```

Map of widgets and selected ranges.

### stack\_updates [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.stack_updates "Permanent link")

```
stack_updates = Reactive(0, repaint=False)
```

An integer that updates when the screen is resumed.

### sub\_title [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.sub_title "Permanent link")

```
sub_title = SUB_TITLE
```

Screen sub-title to override [the app sub-title](https://textual.textualize.io/api/app/#textual.app.App.sub_title " sub_title").

### title [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.title "Permanent link")

```
title = TITLE
```

Screen title to override [the app title](https://textual.textualize.io/api/app/#textual.app.App.title " title").

### action\_blur [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.action_blur "Permanent link")

```
action_blur()
```

Action to remove focus (if set).

### action\_copy\_text [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.action_copy_text "Permanent link")

```
action_copy_text()
```

Copy selected text to clipboard.

### action\_dismiss [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.action_dismiss "Permanent link")

```
action_dismiss(=None)
```

A wrapper around that can be called as an action.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `result` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.action_dismiss\(result\) "Permanent link") | ` \| None` | The optional result to be passed to the result callback. | `None` |

### action\_maximize [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.action_maximize "Permanent link")

```
action_maximize()
```

Action to maximize the currently focused widget.

### action\_minimize [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.action_minimize "Permanent link")

```
action_minimize()
```

Action to minimize the currently maximized widget.

### can\_view\_entire [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.can_view_entire "Permanent link")

```
can_view_entire()
```

Check if a given widget is fully within the current screen.

Note: This doesn't necessarily equate to a widget being visible. There are other reasons why a widget may not be visible.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.can_view_entire\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A widget. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the entire widget is in view, `False` if it is partially visible or not in view. |

### can\_view\_partial [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.can_view_partial "Permanent link")

```
can_view_partial()
```

Check if a given widget is at least partially within the current view.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.can_view_partial\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A widget. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the any part of the widget is in view, `False` if it is completely outside of the screen. |

### clear\_selection [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.clear_selection "Permanent link")

```
clear_selection()
```

Clear any selected text.

### dismiss [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.dismiss "Permanent link")

```
dismiss(=None)
```

Dismiss the screen, optionally with a result.

Any callback provided in [push\_screen](https://textual.textualize.io/api/app/#textual.app.App.push_screen " push_screen") will be invoked with the supplied result.

Only the active screen may be dismissed. This method will produce a warning in the logs if called on an inactive screen (but otherwise have no effect).

Warning

Textual will raise a [`ScreenError`](https://textual.textualize.io/api/app/#textual.app.ScreenError " ScreenError") if you await the return value from a message handler on the Screen being dismissed. If you want to dismiss the current screen, you can call `self.dismiss()` *without* awaiting.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `result` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.dismiss\(result\) "Permanent link") | ` \| None` | The optional result to be passed to the result callback. | `None` |

### find\_widget [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.find_widget "Permanent link")

```
find_widget()
```

Get the screen region of a Widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.find_widget\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A Widget within the composition. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[MapGeometry](https://textual.textualize.io/api/map_geometry/#textual.map_geometry.MapGeometry " MapGeometry (textual._compositor.MapGeometry)")` | Region relative to screen. |

Raises:

| Type | Description |
| --- | --- |
| `[NoWidget](https://textual.textualize.io/api/errors/#textual.errors.NoWidget " NoWidget (textual.errors.NoWidget)")` | If the widget could not be found in this screen. |

### focus\_next [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.focus_next "Permanent link")

```
focus_next(='*')
```

Focus the next widget, optionally filtered by a CSS selector.

If no widget is currently focused, this will focus the first focusable widget. If no focusable widget matches the given CSS selector, focus is set to `None`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.focus_next\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")]` | CSS selector to filter what nodes can be focused. | `'*'` |

Returns:

| Type | Description |
| --- | --- |
| `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | Newly focused widget, or None for no focus. If the return is not `None`, then it is guaranteed that the widget returned matches the CSS selectors given in the argument. |

### focus\_previous [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.focus_previous "Permanent link")

```
focus_previous(='*')
```

Focus the previous widget, optionally filtered by a CSS selector.

If no widget is currently focused, this will focus the first focusable widget. If no focusable widget matches the given CSS selector, focus is set to `None`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.focus_previous\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")]` | CSS selector to filter what nodes can be focused. | `'*'` |

Returns:

| Type | Description |
| --- | --- |
| `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | Newly focused widget, or None for no focus. If the return is not `None`, then it is guaranteed that the widget returned matches the CSS selectors given in the argument. |

### get\_focusable\_widget\_at [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_focusable_widget_at "Permanent link")

```
get_focusable_widget_at(, )
```

Get the focusable widget under a given coordinate.

If the widget directly under the given coordinate is not focusable, then this method will check if any of the ancestors are focusable. If no ancestors are focusable, then `None` will be returned.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_focusable_widget_at\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | X coordinate. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_focusable_widget_at\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y coordinate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | A `Widget`, or `None` if there is no focusable widget underneath the coordinate. |

### get\_offset [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_offset "Permanent link")

```
get_offset()
```

Get the absolute offset of a given Widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_offset\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A widget | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | The widget's offset relative to the top left of the terminal. |

### get\_selected\_text [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_selected_text "Permanent link")

```
get_selected_text()
```

Get text under selection.

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Selected text, or `None` if no text was selected. |

### get\_style\_at [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_style_at "Permanent link")

```
get_style_at(, )
```

Get the style under a given coordinate.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_style_at\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | X Coordinate. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_style_at\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y Coordinate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | Rich Style object. |

### get\_widget\_and\_offset\_at [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_widget_and_offset_at "Permanent link")

```
get_widget_and_offset_at(, )
```

Get the widget under a given coordinate, and an offset within the original content.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_widget_and_offset_at\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | X Coordinate. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_widget_and_offset_at\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y Coordinate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None, [Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)") \| None]` | Tuple of Widget and Offset, both of which may be None. |

### get\_widget\_at [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_widget_at "Permanent link")

```
get_widget_at(, )
```

Get the widget at a given coordinate.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_widget_at\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | X Coordinate. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_widget_at\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y Coordinate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)"), [Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")]` | Widget and screen region. |

Raises:

| Type | Description |
| --- | --- |
| `[NoWidget](https://textual.textualize.io/api/errors/#textual.errors.NoWidget " NoWidget (textual.errors.NoWidget)")` | If there is no widget under the screen coordinate. |

### get\_widgets\_at [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_widgets_at "Permanent link")

```
get_widgets_at(, )
```

Get all widgets under a given coordinate.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_widgets_at\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | X coordinate. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.get_widgets_at\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y coordinate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)"), [Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")]]` | Sequence of (WIDGET, REGION) tuples. |

### maximize [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.maximize "Permanent link")

```
maximize(, =True)
```

Maximize a widget, so it fills the screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.maximize\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | Widget to maximize. | *required* |
| #### `container` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.maximize\(container\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If one of the widgets ancestors is a maximizeable widget, maximize that instead. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the widget was maximized, otherwise `False`. |

### minimize [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.minimize "Permanent link")

```
minimize()
```

Restore any maximized widget to normal state.

### pop\_until\_active [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.pop_until_active "Permanent link")

```
pop_until_active()
```

Pop any screens on top of this one, until this screen is active.

Raises:

| Type | Description |
| --- | --- |
| `ScreenError` | If this screen is not in the current mode. |

### refresh\_bindings [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.refresh_bindings "Permanent link")

```
refresh_bindings()
```

Call to request a refresh of bindings.

### set\_focus [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.set_focus "Permanent link")

```
set_focus(
    , =True, =False
)
```

Focus (or un-focus) a widget. A focused widget will receive key events first.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.set_focus\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | Widget to focus, or None to un-focus. | *required* |
| #### `scroll_visible` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.set_focus\(scroll_visible\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Scroll widget into view. | `True` |
| #### `from_app_focus` [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.set_focus\(from_app_focus\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if this focus is due to the app itself having regained focus. False if the focus is being set because a widget within the app regained focus. | `False` |

### validate\_sub\_title [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.validate_sub_title "Permanent link")

```
validate_sub_title(sub_title)
```

Ensure the sub-title is a string or `None`.

### validate\_title [¶](https://textual.textualize.io/api/screen/#textual.screen.Screen.validate_title "Permanent link")

```
validate_title(title)
```

Ensure the title is a string or `None`.

## SystemModalScreen [¶](https://textual.textualize.io/api/screen/#textual.screen.SystemModalScreen "Permanent link")

```
SystemModalScreen(name=None, id=None, classes=None)
```

Bases: `[]`

A variant of `ModalScreen` for internal use.

This version of `ModalScreen` allows us to build system-level screens; the type being used to indicate that the screen should be isolated from the main application.

Note

This screen is set to *not* inherit CSS.