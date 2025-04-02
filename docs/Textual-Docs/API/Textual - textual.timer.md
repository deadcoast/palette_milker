---
title: "Textual - textual.timer"
source: "https://textual.textualize.io/api/timer/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.timer

Contains the `Timer` class. Timer objects are created by [set\_interval](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_interval " set_interval") or [set\_timer](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.set_timer " set_timer").

## TimerCallback [¶](https://textual.textualize.io/api/timer/#textual.timer.TimerCallback "Permanent link")

```
TimerCallback = Union[
    Callable[[], Awaitable[Any]], Callable[[], Any]
]
```

Type of valid callbacks to be used with timers.

## EventTargetGone [¶](https://textual.textualize.io/api/timer/#textual.timer.EventTargetGone "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised if the timer event target has been deleted prior to the timer event being sent.

## Timer [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer "Permanent link")

```
Timer(
    ,
    ,
    *,
    =None,
    =None,
    =None,
    =True,
    =False
)
```

A class to send timer-based events.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `event_target` [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer\(event_target\) "Permanent link") | `[MessageTarget](https://textual.textualize.io/api/types/#textual.types.MessageTarget " MessageTarget (textual._types.MessageTarget)")` | The object which will receive the timer events. | *required* |
| ### `interval` [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer\(interval\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | The time between timer events, in seconds. | *required* |
| ### `name` [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A name to assign the event (for debugging). | `None` |
| ### `callback` [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer\(callback\) "Permanent link") | ` \| None` | A optional callback to invoke when the event is handled. | `None` |
| ### `repeat` [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer\(repeat\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The number of times to repeat the timer, or None to repeat forever. | `None` |
| ### `skip` [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer\(skip\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable skipping of scheduled events that couldn't be sent in time. | `True` |
| ### `pause` [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer\(pause\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Start the timer paused. | `False` |

### pause [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer.pause "Permanent link")

```
pause()
```

Pause the timer.

A paused timer will not send events until it is resumed.

### reset [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer.reset "Permanent link")

```
reset()
```

Reset the timer, so it starts from the beginning.

### resume [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer.resume "Permanent link")

```
resume()
```

Resume a paused timer.

### stop [¶](https://textual.textualize.io/api/timer/#textual.timer.Timer.stop "Permanent link")

```
stop()
```

Stop the timer.