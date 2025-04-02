---
title: "Textual - textual.events"
source: "https://textual.textualize.io/api/events/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.events

Builtin events sent by Textual.

Events may be marked as "Bubbles" and "Verbose". See the [events guide](https://textual.textualize.io/guide/events/#bubbling) for an explanation of bubbling. Verbose events are excluded from the textual console, unless you explicitly request them with the `-v` switch as follows:

```
textual console -v
```

## AppBlur [¶](https://textual.textualize.io/api/events/#textual.events.AppBlur "Permanent link")

```
AppBlur()
```

Bases:

Sent when the app loses focus.

- Bubbles
- Verbose

Note

Only available when running within a terminal that supports `FocusOut`, or when running via textual-web.

## AppFocus [¶](https://textual.textualize.io/api/events/#textual.events.AppFocus "Permanent link")

```
AppFocus()
```

Bases:

Sent when the app has focus.

- Bubbles
- Verbose

Note

Only available when running within a terminal that supports `FocusIn`, or when running via textual-web.

## Blur [¶](https://textual.textualize.io/api/events/#textual.events.Blur "Permanent link")

```
Blur()
```

Bases:

Sent when a widget is blurred (un-focussed).

- Bubbles
- Verbose

## Callback [¶](https://textual.textualize.io/api/events/#textual.events.Callback "Permanent link")

```
Callback(callback)
```

Bases:

Sent by Textual to invoke a callback (see [call\_next](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_next " call_next") and [call\_later](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_later " call_later")).

## Click [¶](https://textual.textualize.io/api/events/#textual.events.Click "Permanent link")

```
Click(
    widget,
    x,
    y,
    delta_x,
    delta_y,
    button,
    shift,
    meta,
    ctrl,
    screen_x=None,
    screen_y=None,
    style=None,
    =1,
)
```

Bases:

Sent when a widget is clicked.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `chain` [¶](https://textual.textualize.io/api/events/#textual.events.Click\(chain\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of clicks in the chain. 2 is a double click, 3 is a triple click, etc. | `1` |

## Compose [¶](https://textual.textualize.io/api/events/#textual.events.Compose "Permanent link")

```
Compose()
```

Bases:

Sent to a widget to request it to compose and mount children.

This event is used internally by Textual. You won't typically need to explicitly handle it,

- Bubbles
- Verbose

## CursorPosition [¶](https://textual.textualize.io/api/events/#textual.events.CursorPosition "Permanent link")

```
CursorPosition(x, y)
```

Bases:

Internal event used to retrieve the terminal's cursor position.

## DeliveryComplete [¶](https://textual.textualize.io/api/events/#textual.events.DeliveryComplete "Permanent link")

```
DeliveryComplete(key, path=None, name=None)
```

Bases:

Sent to App when a file has been delivered.

### key [¶](https://textual.textualize.io/api/events/#textual.events.DeliveryComplete.key "Permanent link")

```
key
```

The delivery key associated with the delivery.

This is the same key that was returned by `App.deliver_text`/`App.deliver_binary`.

### name [¶](https://textual.textualize.io/api/events/#textual.events.DeliveryComplete.name "Permanent link")

```
name = None
```

Optional name returned to the app to identify the download.

### path [¶](https://textual.textualize.io/api/events/#textual.events.DeliveryComplete.path "Permanent link")

```
path = None
```

The path where the file was saved, or `None` if the path is not available, for example if the file was delivered via web browser.

## DeliveryFailed [¶](https://textual.textualize.io/api/events/#textual.events.DeliveryFailed "Permanent link")

```
DeliveryFailed(key, exception, name=None)
```

Bases:

Sent to App when a file delivery fails.

### exception [¶](https://textual.textualize.io/api/events/#textual.events.DeliveryFailed.exception "Permanent link")

```
exception
```

The exception that was raised during the delivery.

### key [¶](https://textual.textualize.io/api/events/#textual.events.DeliveryFailed.key "Permanent link")

```
key
```

The delivery key associated with the delivery.

### name [¶](https://textual.textualize.io/api/events/#textual.events.DeliveryFailed.name "Permanent link")

```
name = None
```

Optional name returned to the app to identify the download.

## DescendantBlur [¶](https://textual.textualize.io/api/events/#textual.events.DescendantBlur "Permanent link")

```
DescendantBlur(widget)
```

Bases:

Sent when a child widget is blurred.

- Bubbles
- Verbose

### control [¶](https://textual.textualize.io/api/events/#textual.events.DescendantBlur.control "Permanent link")

```
control
```

The widget that was blurred (alias of `widget`).

### widget [¶](https://textual.textualize.io/api/events/#textual.events.DescendantBlur.widget "Permanent link")

```
widget
```

The widget that was blurred.

## DescendantFocus [¶](https://textual.textualize.io/api/events/#textual.events.DescendantFocus "Permanent link")

```
DescendantFocus(widget)
```

Bases:

Sent when a child widget is focussed.

- Bubbles
- Verbose

### control [¶](https://textual.textualize.io/api/events/#textual.events.DescendantFocus.control "Permanent link")

```
control
```

The widget that was focused (alias of `widget`).

### widget [¶](https://textual.textualize.io/api/events/#textual.events.DescendantFocus.widget "Permanent link")

```
widget
```

The widget that was focused.

## Enter [¶](https://textual.textualize.io/api/events/#textual.events.Enter "Permanent link")

```
Enter(node)
```

Bases:

Sent when the mouse is moved over a widget.

Note that this event bubbles, so a widget may receive this event when the mouse moves over a child widget. Check the `node` attribute for the widget directly under the mouse.

- Bubbles
- Verbose

### control [¶](https://textual.textualize.io/api/events/#textual.events.Enter.control "Permanent link")

```
control
```

Alias for the `node` under the mouse.

### node [¶](https://textual.textualize.io/api/events/#textual.events.Enter.node "Permanent link")

```
node = node
```

The node directly under the mouse.

## Event [¶](https://textual.textualize.io/api/events/#textual.events.Event "Permanent link")

```
Event()
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

The base class for all events.

## Focus [¶](https://textual.textualize.io/api/events/#textual.events.Focus "Permanent link")

```
Focus(=False)
```

Bases:

Sent when a widget is focussed.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `from_app_focus` [¶](https://textual.textualize.io/api/events/#textual.events.Focus\(from_app_focus\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if this focus event has been sent because the app itself has regained focus (via an AppFocus event). False if the focus came from within the Textual app (e.g. via the user pressing tab or a programmatic setting of the focused widget). | `False` |

## Hide [¶](https://textual.textualize.io/api/events/#textual.events.Hide "Permanent link")

```
Hide()
```

Bases:

Sent when a widget has been hidden.

- Bubbles
- Verbose

Sent when any of the following conditions apply:

- The widget is removed from the DOM.
- The widget is no longer displayed because it has been scrolled or clipped from the terminal or its container.
- The widget has its `display` attribute set to `False`.
- The widget's `display` style is set to `"none"`.

## Idle [¶](https://textual.textualize.io/api/events/#textual.events.Idle "Permanent link")

```
Idle()
```

Bases:

Sent when there are no more items in the message queue.

This is a pseudo-event in that it is created by the Textual system and doesn't go through the usual message queue.

- Bubbles
- Verbose

## InputEvent [¶](https://textual.textualize.io/api/events/#textual.events.InputEvent "Permanent link")

```
InputEvent()
```

Bases:

Base class for input events.

## Key [¶](https://textual.textualize.io/api/events/#textual.events.Key "Permanent link")

```
Key(, )
```

Bases:

Sent when the user hits a key on the keyboard.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `key` [¶](https://textual.textualize.io/api/events/#textual.events.Key\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The key that was pressed. | *required* |
| ### `character` [¶](https://textual.textualize.io/api/events/#textual.events.Key\(character\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A printable character or `None` if it is not printable. | *required* |

### aliases [¶](https://textual.textualize.io/api/events/#textual.events.Key.aliases "Permanent link")

```
aliases = _get_key_aliases()
```

The aliases for the key, including the key itself.

### character [¶](https://textual.textualize.io/api/events/#textual.events.Key.character "Permanent link")

```
character = (
    
    if len() == 1
    else None if  is None else 
)
```

A printable character or `None` if it is not printable.

### is\_printable [¶](https://textual.textualize.io/api/events/#textual.events.Key.is_printable "Permanent link")

```
is_printable
```

Check if the key is printable (produces a unicode character).

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the key is printable. |

### key [¶](https://textual.textualize.io/api/events/#textual.events.Key.key "Permanent link")

```
key =
```

The key that was pressed.

### name [¶](https://textual.textualize.io/api/events/#textual.events.Key.name "Permanent link")

```
name
```

Name of a key suitable for use as a Python identifier.

### name\_aliases [¶](https://textual.textualize.io/api/events/#textual.events.Key.name_aliases "Permanent link")

```
name_aliases
```

The corresponding name for every alias in `aliases` list.

## Leave [¶](https://textual.textualize.io/api/events/#textual.events.Leave "Permanent link")

```
Leave(node)
```

Bases:

Sent when the mouse is moved away from a widget, or if a widget is programmatically disabled while hovered.

Note that this widget bubbles, so a widget may receive Leave events for any child widgets. Check the `node` parameter for the original widget that was previously under the mouse.

- Bubbles
- Verbose

### control [¶](https://textual.textualize.io/api/events/#textual.events.Leave.control "Permanent link")

```
control
```

Alias for the `node` that was previously under the mouse.

### node [¶](https://textual.textualize.io/api/events/#textual.events.Leave.node "Permanent link")

```
node = node
```

The node that was previously directly under the mouse.

## Load [¶](https://textual.textualize.io/api/events/#textual.events.Load "Permanent link")

```
Load()
```

Bases:

Sent when the App is running but *before* the terminal is in application mode.

Use this event to run any setup that doesn't require any visuals such as loading configuration and binding keys.

- Bubbles
- Verbose

## Mount [¶](https://textual.textualize.io/api/events/#textual.events.Mount "Permanent link")

```
Mount()
```

Bases:

Sent when a widget is *mounted* and may receive messages.

- Bubbles
- Verbose

## MouseCapture [¶](https://textual.textualize.io/api/events/#textual.events.MouseCapture "Permanent link")

```
MouseCapture()
```

Bases:

Sent when the mouse has been captured.

- Bubbles
- Verbose

When a mouse has been captured, all further mouse events will be sent to the capturing widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `mouse_position` [¶](https://textual.textualize.io/api/events/#textual.events.MouseCapture\(mouse_position\) "Permanent link") | `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | The position of the mouse when captured. | *required* |

### mouse\_position [¶](https://textual.textualize.io/api/events/#textual.events.MouseCapture.mouse_position "Permanent link")

```
mouse_position =
```

The position of the mouse when captured.

## MouseDown [¶](https://textual.textualize.io/api/events/#textual.events.MouseDown "Permanent link")

```
MouseDown(
    widget,
    x,
    y,
    delta_x,
    delta_y,
    button,
    shift,
    meta,
    ctrl,
    screen_x=None,
    screen_y=None,
    style=None,
)
```

Bases:

Sent when a mouse button is pressed.

- Bubbles
- Verbose

## MouseEvent [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent "Permanent link")

```
MouseEvent(
    ,
    ,
    ,
    ,
    ,
    ,
    ,
    ,
    ,
    =None,
    =None,
    =None,
)
```

Bases:

Sent in response to a mouse event.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `widget` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | The widget under the mouse. | *required* |
| ### `x` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(x\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | The relative x coordinate. | *required* |
| ### `y` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(y\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | The relative y coordinate. | *required* |
| ### `delta_x` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(delta_x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Change in x since the last message. | *required* |
| ### `delta_y` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(delta_y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Change in y since the last message. | *required* |
| ### `button` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(button\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Indexed of the pressed button. | *required* |
| ### `shift` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(shift\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the shift key is pressed. | *required* |
| ### `meta` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(meta\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the meta key is pressed. | *required* |
| ### `ctrl` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(ctrl\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the ctrl key is pressed. | *required* |
| ### `screen_x` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(screen_x\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The absolute x coordinate. | `None` |
| ### `screen_y` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(screen_y\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The absolute y coordinate. | `None` |
| ### `style` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style") \| None` | The Rich Style under the mouse cursor. | `None` |

### button [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.button "Permanent link")

```
button =
```

Indexed of the pressed button.

### ctrl [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.ctrl "Permanent link")

```
ctrl =
```

`True` if the ctrl key is pressed.

### delta [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.delta "Permanent link")

```
delta
```

Mouse coordinate delta (change since last event).

### delta\_x [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.delta_x "Permanent link")

```
delta_x
```

Change in `x` since last message.

### delta\_y [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.delta_y "Permanent link")

```
delta_y
```

Change in `y` since the last message.

### meta [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.meta "Permanent link")

```
meta =
```

`True` if the meta key is pressed.

### offset [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.offset "Permanent link")

```
offset
```

The mouse coordinate as an offset.

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | Mouse coordinate. |

### pointer\_screen\_x [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.pointer_screen_x "Permanent link")

```
pointer_screen_x
```

The X coordinate of the pointer relative to the screen.

### pointer\_screen\_y [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.pointer_screen_y "Permanent link")

```
pointer_screen_y
```

The Y coordinate of the pointer relative to the screen.

### pointer\_x [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.pointer_x "Permanent link")

```
pointer_x
```

The relative X coordinate of the pointer.

### pointer\_y [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.pointer_y "Permanent link")

```
pointer_y
```

The relative Y coordinate of the pointer.

### screen\_offset [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.screen_offset "Permanent link")

```
screen_offset
```

Mouse coordinate relative to the screen.

### screen\_x [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.screen_x "Permanent link")

```
screen_x
```

X coordinate of the cell relative to top left of screen.

### screen\_y [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.screen_y "Permanent link")

```
screen_y
```

Y coordinate of the cell relative to top left of screen.

### shift [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.shift "Permanent link")

```
shift =
```

`True` if the shift key is pressed.

### style [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.style "Permanent link")

```
style
```

The (Rich) Style under the cursor.

### widget [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.widget "Permanent link")

```
widget =
```

The widget under the mouse at the time of a click.

### x [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.x "Permanent link")

```
x
```

The relative X coordinate of the cell under the mouse.

### y [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.y "Permanent link")

```
y
```

The relative Y coordinate of the cell under the mouse.

### get\_content\_offset [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.get_content_offset "Permanent link")

```
get_content_offset()
```

Get offset within a widget's content area, or None if offset is not in content (i.e. padding or border).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.get_content_offset\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | Widget receiving the event. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)") \| None` | An offset where the origin is at the top left of the content area. |

### get\_content\_offset\_capture [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.get_content_offset_capture "Permanent link")

```
get_content_offset_capture()
```

Get offset from a widget's content area.

This method works even if the offset is outside the widget content region.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/events/#textual.events.MouseEvent.get_content_offset_capture\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | Widget receiving the event. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | An offset where the origin is at the top left of the content area. |

## MouseMove [¶](https://textual.textualize.io/api/events/#textual.events.MouseMove "Permanent link")

```
MouseMove(
    widget,
    x,
    y,
    delta_x,
    delta_y,
    button,
    shift,
    meta,
    ctrl,
    screen_x=None,
    screen_y=None,
    style=None,
)
```

Bases:

Sent when the mouse cursor moves.

- Bubbles
- Verbose

## MouseRelease [¶](https://textual.textualize.io/api/events/#textual.events.MouseRelease "Permanent link")

```
MouseRelease()
```

Bases:

Mouse has been released.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `mouse_position` [¶](https://textual.textualize.io/api/events/#textual.events.MouseRelease\(mouse_position\) "Permanent link") | `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | The position of the mouse when released. | *required* |

### mouse\_position [¶](https://textual.textualize.io/api/events/#textual.events.MouseRelease.mouse_position "Permanent link")

```
mouse_position =
```

The position of the mouse when released.

## MouseScrollDown [¶](https://textual.textualize.io/api/events/#textual.events.MouseScrollDown "Permanent link")

```
MouseScrollDown(
    widget,
    x,
    y,
    delta_x,
    delta_y,
    button,
    shift,
    meta,
    ctrl,
    screen_x=None,
    screen_y=None,
    style=None,
)
```

Bases:

Sent when the mouse wheel is scrolled *down*.

- Bubbles
- Verbose

## MouseScrollUp [¶](https://textual.textualize.io/api/events/#textual.events.MouseScrollUp "Permanent link")

```
MouseScrollUp(
    widget,
    x,
    y,
    delta_x,
    delta_y,
    button,
    shift,
    meta,
    ctrl,
    screen_x=None,
    screen_y=None,
    style=None,
)
```

Bases:

Sent when the mouse wheel is scrolled *up*.

- Bubbles
- Verbose

## MouseUp [¶](https://textual.textualize.io/api/events/#textual.events.MouseUp "Permanent link")

```
MouseUp(
    widget,
    x,
    y,
    delta_x,
    delta_y,
    button,
    shift,
    meta,
    ctrl,
    screen_x=None,
    screen_y=None,
    style=None,
)
```

Bases:

Sent when a mouse button is released.

- Bubbles
- Verbose

## Paste [¶](https://textual.textualize.io/api/events/#textual.events.Paste "Permanent link")

```
Paste()
```

Bases:

Event containing text that was pasted into the Textual application. This event will only appear when running in a terminal emulator that supports bracketed paste mode. Textual will enable bracketed pastes when an app starts, and disable it when the app shuts down.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/api/events/#textual.events.Paste\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text that has been pasted. | *required* |

### text [¶](https://textual.textualize.io/api/events/#textual.events.Paste.text "Permanent link")

```
text =
```

The text that was pasted.

## Print [¶](https://textual.textualize.io/api/events/#textual.events.Print "Permanent link")

```
Print(, =False)
```

Bases:

Sent to a widget that is capturing [`print`](https://docs.python.org/3/library/functions.html#print).

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/api/events/#textual.events.Print\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Text that was printed. | *required* |
| ### `stderr` [¶](https://textual.textualize.io/api/events/#textual.events.Print\(stderr\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the print was to stderr, or `False` for stdout. | `False` |

Note

Python's [`print`](https://docs.python.org/3/library/functions.html#print) output can be captured with [`App.begin_capture_print`](https://textual.textualize.io/api/app/#textual.app.App.begin_capture_print " begin_capture_print").

### stderr [¶](https://textual.textualize.io/api/events/#textual.events.Print.stderr "Permanent link")

```
stderr =
```

`True` if the print was to stderr, or `False` for stdout.

### text [¶](https://textual.textualize.io/api/events/#textual.events.Print.text "Permanent link")

```
text =
```

The text that was printed.

## Ready [¶](https://textual.textualize.io/api/events/#textual.events.Ready "Permanent link")

```
Ready()
```

Bases:

Sent to the `App` when the DOM is ready and the first frame has been displayed.

- Bubbles
- Verbose

## Resize [¶](https://textual.textualize.io/api/events/#textual.events.Resize "Permanent link")

```
Resize(
    , , =None, pixel_size=None
)
```

Bases:

Sent when the app or widget has been resized.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `size` [¶](https://textual.textualize.io/api/events/#textual.events.Resize\(size\) "Permanent link") | `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | The new size of the Widget. | *required* |
| ### `virtual_size` [¶](https://textual.textualize.io/api/events/#textual.events.Resize\(virtual_size\) "Permanent link") | `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | The virtual size (scrollable size) of the Widget. | *required* |
| ### `container_size` [¶](https://textual.textualize.io/api/events/#textual.events.Resize\(container_size\) "Permanent link") | `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)") \| None` | The size of the Widget's container widget. | `None` |

### container\_size [¶](https://textual.textualize.io/api/events/#textual.events.Resize.container_size "Permanent link")

```
container_size = (
     if  is None else 
)
```

The size of the Widget's container widget.

### pixel\_size [¶](https://textual.textualize.io/api/events/#textual.events.Resize.pixel_size "Permanent link")

```
pixel_size = pixel_size
```

Size of terminal window in pixels if known, or `None` if not known.

### size [¶](https://textual.textualize.io/api/events/#textual.events.Resize.size "Permanent link")

```
size =
```

The new size of the Widget.

### virtual\_size [¶](https://textual.textualize.io/api/events/#textual.events.Resize.virtual_size "Permanent link")

```
virtual_size =
```

The virtual size (scrollable size) of the Widget.

### from\_dimensions [¶](https://textual.textualize.io/api/events/#textual.events.Resize.from_dimensions "Permanent link")

```
from_dimensions(, )
```

Construct from basic dimensions.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `cells` [¶](https://textual.textualize.io/api/events/#textual.events.Resize.from_dimensions\(cells\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)]` | tuple of (, ) in cells. | *required* |
| #### `pixels` [¶](https://textual.textualize.io/api/events/#textual.events.Resize.from_dimensions\(pixels\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)] \| None` | tuple of (, ) in pixels if known, or `None` if not known. | *required* |

## ScreenResume [¶](https://textual.textualize.io/api/events/#textual.events.ScreenResume "Permanent link")

```
ScreenResume()
```

Bases:

Sent to screen that has been made active.

- Bubbles
- Verbose

## ScreenSuspend [¶](https://textual.textualize.io/api/events/#textual.events.ScreenSuspend "Permanent link")

```
ScreenSuspend()
```

Bases:

Sent to screen when it is no longer active.

- Bubbles
- Verbose

## Show [¶](https://textual.textualize.io/api/events/#textual.events.Show "Permanent link")

```
Show()
```

Bases:

Sent when a widget is first displayed.

- Bubbles
- Verbose

## Timer [¶](https://textual.textualize.io/api/events/#textual.events.Timer "Permanent link")

```
Timer(timer, time, count=0, callback=None)
```

Bases:

Sent in response to a timer.

- Bubbles
- Verbose

## Unmount [¶](https://textual.textualize.io/api/events/#textual.events.Unmount "Permanent link")

```
Unmount()
```

Bases:

Sent when a widget is unmounted and may no longer receive messages.

- Bubbles
- Verbose