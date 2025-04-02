---
title: "Textual - textual.pilot"
source: "https://textual.textualize.io/api/pilot/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.pilot

This module contains the `Pilot` class used by [App.run\_test](https://textual.textualize.io/api/app/#textual.app.App.run_test " run_test") to programmatically operate an app.

See the guide on how to [test Textual apps](https://textual.textualize.io/guide/testing).

## OutOfBounds [¶](https://textual.textualize.io/api/pilot/#textual.pilot.OutOfBounds "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when the pilot mouse target is outside of the (visible) screen.

## Pilot [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot "Permanent link")

```
Pilot(app)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[ReturnType]`

Pilot object to drive an app.

### app [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.app "Permanent link")

```
app
```

### click [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.click "Permanent link")

```
click(
    =None,
    =(0, 0),
    =False,
    =False,
    =False,
    =1,
)
```

Simulate clicking with the mouse at a specified position.

The final position to be clicked is computed based on the selector provided and the offset specified and it must be within the visible area of the screen.

Implementation note: This method bypasses the normal event processing in `App.on_event`.

Example

The code below runs an app and clicks its only button right in the middle:

```
async with SingleButtonApp().run_test() as pilot:
    await pilot.click(Button, offset=(8, 1))
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.click\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| [type](https://docs.python.org/3/library/functions.html#type)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")] \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A widget or selector used as an origin for the click offset. If this is not specified, the offset is interpreted relative to the screen. You can use this parameter to try to click on a specific widget. However, if the widget is currently hidden or obscured by another widget, the click may not land on the widget you specified. | `None` |
| #### `offset` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.click\(offset\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | The offset to click. The offset is relative to the widget / selector provided or to the screen, if no selector is provided. | `(0, 0)` |
| #### `shift` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.click\(shift\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Click with the shift key held down. | `False` |
| #### `meta` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.click\(meta\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Click with the meta key held down. | `False` |
| #### `control` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.click\(control\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Click with the control key held down. | `False` |
| #### `times` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.click\(times\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of times to click. 2 will double-click, 3 will triple-click, etc. | `1` |

Raises:

| Type | Description |
| --- | --- |
|  | If the position to be clicked is outside of the (visible) screen. |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if no selector was specified or if the click landed on the selected widget, False otherwise. |

### double\_click [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.double_click "Permanent link")

```
double_click(
    =None,
    =(0, 0),
    =False,
    =False,
    =False,
)
```

Simulate double clicking with the mouse at a specified position.

Alias for `pilot.click(..., times=2)`.

The final position to be clicked is computed based on the selector provided and the offset specified and it must be within the visible area of the screen.

Implementation note: This method bypasses the normal event processing in `App.on_event`.

Example

The code below runs an app and double-clicks its only button right in the middle:

```
async with SingleButtonApp().run_test() as pilot:
    await pilot.double_click(Button, offset=(8, 1))
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.double_click\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| [type](https://docs.python.org/3/library/functions.html#type)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")] \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A widget or selector used as an origin for the click offset. If this is not specified, the offset is interpreted relative to the screen. You can use this parameter to try to click on a specific widget. However, if the widget is currently hidden or obscured by another widget, the click may not land on the widget you specified. | `None` |
| #### `offset` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.double_click\(offset\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | The offset to click. The offset is relative to the widget / selector provided or to the screen, if no selector is provided. | `(0, 0)` |
| #### `shift` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.double_click\(shift\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Click with the shift key held down. | `False` |
| #### `meta` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.double_click\(meta\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Click with the meta key held down. | `False` |
| #### `control` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.double_click\(control\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Click with the control key held down. | `False` |

Raises:

| Type | Description |
| --- | --- |
|  | If the position to be clicked is outside of the (visible) screen. |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if no selector was specified or if the clicks landed on the selected widget, False otherwise. |

### exit [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.exit "Permanent link")

```
exit()
```

Exit the app with the given result.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `result` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.exit\(result\) "Permanent link") | `ReturnType` | The app result returned by `run` or `run_async`. | *required* |

### hover [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.hover "Permanent link")

```
hover(=None, =(0, 0))
```

Simulate hovering with the mouse cursor at a specified position.

The final position to be hovered is computed based on the selector provided and the offset specified and it must be within the visible area of the screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.hover\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| [type](https://docs.python.org/3/library/functions.html#type)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")] \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None \| None` | A widget or selector used as an origin for the hover offset. If this is not specified, the offset is interpreted relative to the screen. You can use this parameter to try to hover a specific widget. However, if the widget is currently hidden or obscured by another widget, the hover may not land on the widget you specified. | `None` |
| #### `offset` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.hover\(offset\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | The offset to hover. The offset is relative to the widget / selector provided or to the screen, if no selector is provided. | `(0, 0)` |

Raises:

| Type | Description |
| --- | --- |
|  | If the position to be hovered is outside of the (visible) screen. |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if no selector was specified or if the hover landed on the selected widget, False otherwise. |

### mouse\_down [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_down "Permanent link")

```
mouse_down(
    =None,
    =(0, 0),
    =False,
    =False,
    =False,
)
```

Simulate a [`MouseDown`](https://textual.textualize.io/api/events/#textual.events.MouseDown " MouseDown") event at a specified position.

The final position for the event is computed based on the selector provided and the offset specified and it must be within the visible area of the screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_down\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| [type](https://docs.python.org/3/library/functions.html#type)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")] \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A widget or selector used as an origin for the event offset. If this is not specified, the offset is interpreted relative to the screen. You can use this parameter to try to target a specific widget. However, if the widget is currently hidden or obscured by another widget, the event may not land on the widget you specified. | `None` |
| #### `offset` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_down\(offset\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | The offset for the event. The offset is relative to the selector / widget provided or to the screen, if no selector is provided. | `(0, 0)` |
| #### `shift` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_down\(shift\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Simulate the event with the shift key held down. | `False` |
| #### `meta` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_down\(meta\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Simulate the event with the meta key held down. | `False` |
| #### `control` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_down\(control\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Simulate the event with the control key held down. | `False` |

Raises:

| Type | Description |
| --- | --- |
|  | If the position for the event is outside of the (visible) screen. |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if no selector was specified or if the event landed on the selected widget, False otherwise. |

### mouse\_up [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_up "Permanent link")

```
mouse_up(
    =None,
    =(0, 0),
    =False,
    =False,
    =False,
)
```

Simulate a [`MouseUp`](https://textual.textualize.io/api/events/#textual.events.MouseUp " MouseUp") event at a specified position.

The final position for the event is computed based on the selector provided and the offset specified and it must be within the visible area of the screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_up\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| [type](https://docs.python.org/3/library/functions.html#type)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")] \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A widget or selector used as an origin for the event offset. If this is not specified, the offset is interpreted relative to the screen. You can use this parameter to try to target a specific widget. However, if the widget is currently hidden or obscured by another widget, the event may not land on the widget you specified. | `None` |
| #### `offset` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_up\(offset\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | The offset for the event. The offset is relative to the widget / selector provided or to the screen, if no selector is provided. | `(0, 0)` |
| #### `shift` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_up\(shift\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Simulate the event with the shift key held down. | `False` |
| #### `meta` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_up\(meta\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Simulate the event with the meta key held down. | `False` |
| #### `control` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.mouse_up\(control\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Simulate the event with the control key held down. | `False` |

Raises:

| Type | Description |
| --- | --- |
|  | If the position for the event is outside of the (visible) screen. |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if no selector was specified or if the event landed on the selected widget, False otherwise. |

### pause [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.pause "Permanent link")

```
pause(=None)
```

Insert a pause.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `delay` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.pause\(delay\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Seconds to pause, or None to wait for cpu idle. | `None` |

### press [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.press "Permanent link")

```
press(*)
```

Simulate key-presses.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*keys` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.press\(*keys\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Keys to press. | `()` |

### resize\_terminal [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.resize_terminal "Permanent link")

```
resize_terminal(, )
```

Resize the terminal to the given dimensions.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `width` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.resize_terminal\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The new width of the terminal. | *required* |
| #### `height` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.resize_terminal\(height\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The new height of the terminal. | *required* |

### triple\_click [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.triple_click "Permanent link")

```
triple_click(
    =None,
    =(0, 0),
    =False,
    =False,
    =False,
)
```

Simulate triple clicking with the mouse at a specified position.

Alias for `pilot.click(..., times=3)`.

The final position to be clicked is computed based on the selector provided and the offset specified and it must be within the visible area of the screen.

Implementation note: This method bypasses the normal event processing in `App.on_event`.

Example

The code below runs an app and triple-clicks its only button right in the middle:

```
async with SingleButtonApp().run_test() as pilot:
    await pilot.triple_click(Button, offset=(8, 1))
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.triple_click\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| [type](https://docs.python.org/3/library/functions.html#type)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")] \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A widget or selector used as an origin for the click offset. If this is not specified, the offset is interpreted relative to the screen. You can use this parameter to try to click on a specific widget. However, if the widget is currently hidden or obscured by another widget, the click may not land on the widget you specified. | `None` |
| #### `offset` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.triple_click\(offset\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | The offset to click. The offset is relative to the widget / selector provided or to the screen, if no selector is provided. | `(0, 0)` |
| #### `shift` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.triple_click\(shift\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Click with the shift key held down. | `False` |
| #### `meta` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.triple_click\(meta\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Click with the meta key held down. | `False` |
| #### `control` [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.triple_click\(control\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Click with the control key held down. | `False` |

Raises:

| Type | Description |
| --- | --- |
|  | If the position to be clicked is outside of the (visible) screen. |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if no selector was specified or if the clicks landed on the selected widget, False otherwise. |

### wait\_for\_animation [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.wait_for_animation "Permanent link")

```
wait_for_animation()
```

Wait for any current animation to complete.

### wait\_for\_scheduled\_animations [¶](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot.wait_for_scheduled_animations "Permanent link")

```
wait_for_scheduled_animations()
```

Wait for any current and scheduled animations to complete.

## WaitForScreenTimeout [¶](https://textual.textualize.io/api/pilot/#textual.pilot.WaitForScreenTimeout "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Exception raised if messages aren't being processed quickly enough.

If this occurs, the most likely explanation is some kind of deadlock in the app code.