---
title: "Textual - textual.signal"
source: "https://textual.textualize.io/api/signal/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.signal

Signals are a simple pub-sub mechanism.

DOMNodes can subscribe to a signal, which will invoke a callback when the signal is published.

This is experimental for now, for internal use. It may be part of the public API in a future release.

## Signal [¶](https://textual.textualize.io/api/signal/#textual.signal.Signal "Permanent link")

```
Signal(, )
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[SignalT]`

A signal that a widget may subscribe to, in order to invoke callbacks when an associated event occurs.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `owner` [¶](https://textual.textualize.io/api/signal/#textual.signal.Signal\(owner\) "Permanent link") | `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")` | The owner of this signal. | *required* |
| ### `name` [¶](https://textual.textualize.io/api/signal/#textual.signal.Signal\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | An identifier for debugging purposes. | *required* |

### owner [¶](https://textual.textualize.io/api/signal/#textual.signal.Signal.owner "Permanent link")

```
owner
```

The owner of this Signal, or `None` if there is no owner.

### publish [¶](https://textual.textualize.io/api/signal/#textual.signal.Signal.publish "Permanent link")

```
publish()
```

Publish the signal (invoke subscribed callbacks).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `data` [¶](https://textual.textualize.io/api/signal/#textual.signal.Signal.publish\(data\) "Permanent link") | `SignalT` | An argument to pass to the callbacks. | *required* |

```
subscribe(, , =False)
```

Subscribe a node to this signal.

When the signal is published, the callback will be invoked.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  | `[MessagePump](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump " MessagePump (textual.message_pump.MessagePump)")` | Node to subscribe. | *required* |
|  | `SignalCallbackType` | A callback function which takes a single argument and returns anything (return type ignored). | *required* |
|  | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Invoke the callback immediately on publish if `True`, otherwise post it to the DOM node to be called once existing messages have been processed. | `False` |

Raises:

| Type | Description |
| --- | --- |
|  | Raised when subscribing a non-mounted widget. |

```
unsubscribe()
```

Unsubscribe a node from this signal.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  | `[MessagePump](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump " MessagePump (textual.message_pump.MessagePump)")` | Node to unsubscribe, | *required* |

## SignalError [¶](https://textual.textualize.io/api/signal/#textual.signal.SignalError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised for Signal errors.