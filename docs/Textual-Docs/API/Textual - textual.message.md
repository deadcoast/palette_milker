---
title: "Textual - textual.message"
source: "https://textual.textualize.io/api/message/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.message

The base class for all messages (including events).

## Message [¶](https://textual.textualize.io/api/message/#textual.message.Message "Permanent link")

```
Message()
```

Base class for a message.

### ALLOW\_SELECTOR\_MATCH [¶](https://textual.textualize.io/api/message/#textual.message.Message.ALLOW_SELECTOR_MATCH "Permanent link")

```
ALLOW_SELECTOR_MATCH = set()
```

Additional attributes that can be used with the [`on` decorator](https://textual.textualize.io/api/logger/#textual.on " on").

These attributes must be widgets.

### control [¶](https://textual.textualize.io/api/message/#textual.message.Message.control "Permanent link")

```
control
```

The widget associated with this message, or None by default.

### handler\_name [¶](https://textual.textualize.io/api/message/#textual.message.Message.handler_name "Permanent link")

```
handler_name
```

Name of the default message handler.

### is\_forwarded [¶](https://textual.textualize.io/api/message/#textual.message.Message.is_forwarded "Permanent link")

```
is_forwarded
```

Has the message been forwarded?

### prevent\_default [¶](https://textual.textualize.io/api/message/#textual.message.Message.prevent_default "Permanent link")

```
prevent_default(=True)
```

Suppress the default action(s). This will prevent handlers in any base classes from being called.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `prevent` [¶](https://textual.textualize.io/api/message/#textual.message.Message.prevent_default\(prevent\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the default action should be suppressed, or False if the default actions should be performed. | `True` |

### set\_sender [¶](https://textual.textualize.io/api/message/#textual.message.Message.set_sender "Permanent link")

```
set_sender()
```

Set the sender of the message.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `sender` [¶](https://textual.textualize.io/api/message/#textual.message.Message.set_sender\(sender\) "Permanent link") | `[MessagePump](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump " MessagePump (textual.message_pump.MessagePump)")` | The sender. | *required* |

Note

When creating a message the sender is automatically set. Normally there will be no need for this method to be called. This method will be used when strict control is required over the sender of a message.

Returns:

| Type | Description |
| --- | --- |
| `Self` | Self. |

### stop [¶](https://textual.textualize.io/api/message/#textual.message.Message.stop "Permanent link")

```
stop(=True)
```

Stop propagation of the message to parent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `stop` [¶](https://textual.textualize.io/api/message/#textual.message.Message.stop\(stop\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | The stop flag. | `True` |