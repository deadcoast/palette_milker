---
title: "Textual - textual.await_complete"
source: "https://textual.textualize.io/api/await_complete/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.await\_complete

This module contains the `AwaitComplete` class. An `AwaitComplete` object is returned by methods that do work in the *background*. You can await this object if you need to know when that work has completed. Or you can ignore it, and Textual will automatically await the work before handling the next message.

Note

You are unlikely to need to explicitly create these objects yourself.

## AwaitComplete [¶](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete "Permanent link")

```
AwaitComplete(*awaitables, pre_await=None)
```

An 'optionally-awaitable' object which runs one or more coroutines (or other awaitables) concurrently.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `awaitables` [¶](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete\(awaitables\) "Permanent link") | `[Awaitable](https://docs.python.org/3/library/typing.html#typing.Awaitable "typing.Awaitable")` | One or more awaitables to run concurrently. | `()` |

### exception [¶](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete.exception "Permanent link")

```
exception
```

An exception if the awaitables failed.

### is\_done [¶](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete.is_done "Permanent link")

```
is_done
```

`True` if the task has completed.

### call\_next [¶](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete.call_next "Permanent link")

```
call_next()
```

Await after the next message.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `node` [¶](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete.call_next\(node\) "Permanent link") | `[MessagePump](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump " MessagePump (textual.message_pump.MessagePump)")` | The node which created the object. | *required* |

### nothing [¶](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete.nothing "Permanent link")

```
nothing()
```

Returns an already completed instance of AwaitComplete.

### set\_pre\_await\_callback [¶](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete.set_pre_await_callback "Permanent link")

```
set_pre_await_callback()
```

Set a callback to run prior to awaiting.

This is used by Textual, mainly to check for possible deadlocks. You are unlikely to need to call this method in an app.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `pre_await` [¶](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete.set_pre_await_callback\(pre_await\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.types.CallbackType)") \| None` | A callback. | *required* |