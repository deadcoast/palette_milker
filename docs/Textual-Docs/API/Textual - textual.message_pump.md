---
title: "Textual - textual.message_pump"
source: "https://textual.textualize.io/api/message_pump/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.message\_pump

A `MessagePump` is a base class for any object which processes messages, which includes Widget, Screen, and App.

Tip

Most of the method here are useful in general app development.

## MessagePump [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump "Permanent link")

```
MessagePump(parent=None)
```

Base class which supplies a message pump.

### app [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.app "Permanent link")

```
app
```

Get the current app.

Returns:

| Type | Description |
| --- | --- |
| `'App[object]'` | The current app. |

Raises:

| Type | Description |
| --- | --- |
| `[NoActiveAppError](https://textual.textualize.io/api/types/#textual.types.NoActiveAppError " NoActiveAppError (textual._context.NoActiveAppError)")` | if no active app could be found for the current asyncio context |

### has\_parent [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.has_parent "Permanent link")

```
has_parent
```

Does this object have a parent?

### is\_attached [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.is_attached "Permanent link")

```
is_attached
```

Is this node linked to the app through the DOM?

### is\_dom\_root [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.is_dom_root "Permanent link")

```
is_dom_root
```

Is this a root node (i.e. the App)?

### is\_parent\_active [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.is_parent_active "Permanent link")

```
is_parent_active
```

Is the parent active?

### is\_running [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.is_running "Permanent link")

```
is_running
```

Is the message pump running (potentially processing messages)?

### log [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.log "Permanent link")

```
log
```

Get a logger for this object.

Returns:

| Type | Description |
| --- | --- |
| `[Logger](https://textual.textualize.io/api/logger/#textual.Logger " Logger (textual.Logger)")` | A logger. |

### message\_queue\_size [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.message_queue_size "Permanent link")

```
message_queue_size
```

The current size of the message queue.

### message\_signal [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.message_signal "Permanent link")

```
message_signal = Signal(self, 'messages')
```

Subscribe to this signal to be notified of all messages sent to this widget.

This is a fairly low-level mechanism, and shouldn't replace regular message handling.

### call\_after\_refresh [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_after_refresh "Permanent link")

```
call_after_refresh(, *args, **kwargs)
```

Schedule a callback to run after all messages are processed and the screen has been refreshed. Positional and keyword arguments are passed to the callable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `callback` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_after_refresh\(callback\) "Permanent link") | `Callback` | A callable. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the callback was scheduled, or `False` if the callback could not be scheduled (may occur if the message pump was closed or closing). |

### call\_later [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_later "Permanent link")

```
call_later(, *, **)
```

Schedule a callback to run after all messages are processed in this object. Positional and keywords arguments are passed to the callable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `callback` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_later\(callback\) "Permanent link") | `Callback` | Callable to call next. | *required* |
| #### `*args` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_later\(*args\) "Permanent link") | `[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | Positional arguments to pass to the callable. | `()` |
| #### `**kwargs` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_later\(**kwargs\) "Permanent link") | `[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | Keyword arguments to pass to the callable. | `{}` |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the callback was scheduled, or `False` if the callback could not be scheduled (may occur if the message pump was closed or closing). |

### call\_next [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_next "Permanent link")

```
call_next(, *, **)
```

Schedule a callback to run immediately after processing the current message.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `callback` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_next\(callback\) "Permanent link") | `Callback` | Callable to run after current event. | *required* |
| #### `*args` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_next\(*args\) "Permanent link") | `[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | Positional arguments to pass to the callable. | `()` |
| #### `**kwargs` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.call_next\(**kwargs\) "Permanent link") | `[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | Keyword arguments to pass to the callable. | `{}` |

### check\_idle [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.check_idle "Permanent link")

```
check_idle()
```

Prompt the message pump to call idle if the queue is empty.

### check\_message\_enabled [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.check_message_enabled "Permanent link")

```
check_message_enabled()
```

Check if a given message is enabled (allowed to be sent).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `message` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.check_message_enabled\(message\) "Permanent link") | `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")` | A message object. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the message will be sent, or `False` if it is disabled. |

### disable\_messages [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.disable_messages "Permanent link")

```
disable_messages(*messages)
```

Disable message types from being processed.

### enable\_messages [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.enable_messages "Permanent link")

```
enable_messages(*messages)
```

Enable processing of messages types.

### on\_event [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.on_event "Permanent link")

```
on_event()
```

Called to process an event.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `event` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.on_event\(event\) "Permanent link") | `[Event](https://textual.textualize.io/api/events/#textual.events.Event " Event (textual.events.Event)")` | An Event object. | *required* |

### post\_message [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.post_message "Permanent link")

```
post_message()
```

Posts a message on to this widget's queue.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `message` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.post_message\(message\) "Permanent link") | `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")` | A message (including Event). | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the message was queued for processing, otherwise `False`. |

### prevent [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.prevent "Permanent link")

```
prevent(*message_types)
```

A context manager to *temporarily* prevent the given message types from being posted.

Example
```
input = self.query_one(Input)
with self.prevent(Input.Changed):
    input.value = "foo"
```

### set\_interval [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_interval "Permanent link")

```
set_interval(
    ,
    =None,
    *,
    =None,
    =0,
    =False
)
```

Call a function at periodic intervals.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `interval` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_interval\(interval\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Time (in seconds) between calls. | *required* |
| #### `callback` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_interval\(callback\) "Permanent link") | `[TimerCallback](https://textual.textualize.io/api/timer/#textual.timer.TimerCallback " TimerCallback (textual.timer.TimerCallback)") \| None` | Function to call. | `None` |
| #### `name` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_interval\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Name of the timer object. | `None` |
| #### `repeat` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_interval\(repeat\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Number of times to repeat the call or 0 for continuous. | `0` |
| #### `pause` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_interval\(pause\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Start the timer paused. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[Timer](https://textual.textualize.io/api/timer/#textual.timer.Timer " Timer (textual.timer.Timer)")` | A timer object. |

### set\_timer [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_timer "Permanent link")

```
set_timer(, =None, *, =None, =False)
```

Call a function after a delay.

Example
```
def ready():
    self.notify("Your soft boiled egg is ready!")
# Call ready() after 3 minutes
self.set_timer(3 * 60, ready)
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `delay` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_timer\(delay\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Time (in seconds) to wait before invoking callback. | *required* |
| #### `callback` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_timer\(callback\) "Permanent link") | `[TimerCallback](https://textual.textualize.io/api/timer/#textual.timer.TimerCallback " TimerCallback (textual.timer.TimerCallback)") \| None` | Callback to call after time has expired. | `None` |
| #### `name` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_timer\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Name of the timer (for debug). | `None` |
| #### `pause` [¶](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_timer\(pause\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Start timer paused. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[Timer](https://textual.textualize.io/api/timer/#textual.timer.Timer " Timer (textual.timer.Timer)")` | A timer object. |