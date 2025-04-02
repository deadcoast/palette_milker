---
title: "Textual - textual.reactive"
source: "https://textual.textualize.io/api/reactive/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.reactive

This module contains the `Reactive` class which implements [reactivity](https://textual.textualize.io/guide/reactivity/).

## Reactive [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive "Permanent link")

```
Reactive(
    ,
    *,
    =False,
    =True,
    =False,
    =False,
    =True,
    =False,
    =False
)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[ReactiveType]`

Reactive descriptor.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `default` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive\(default\) "Permanent link") | `ReactiveType \| [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[], ReactiveType]` | A default value or callable that returns a default. | *required* |
| ### `layout` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive\(layout\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Perform a layout on change. | `False` |
| ### `repaint` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive\(repaint\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Perform a repaint on change. | `True` |
| ### `init` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive\(init\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Call watchers on initialize (post mount). | `False` |
| ### `always_update` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive\(always_update\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Call watchers even when the new value equals the old value. | `False` |
| ### `compute` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive\(compute\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Run compute methods when attribute is changed. | `True` |
| ### `recompose` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive\(recompose\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Compose the widget again when the attribute changes. | `False` |
| ### `bindings` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive\(bindings\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Refresh bindings when the reactive changes. | `False` |

### owner [¶](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive.owner "Permanent link")

```
owner
```

The owner (class) where the reactive was declared.

## ReactiveError [¶](https://textual.textualize.io/api/reactive/#textual.reactive.ReactiveError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Base class for reactive errors.

## TooManyComputesError [¶](https://textual.textualize.io/api/reactive/#textual.reactive.TooManyComputesError "Permanent link")

Bases:

Raised when an attribute has public and private compute methods.

## reactive [¶](https://textual.textualize.io/api/reactive/#textual.reactive.reactive "Permanent link")

```
reactive(
    ,
    *,
    =False,
    =True,
    =True,
    =False,
    recompose=False,
    =False
)
```

Bases: `[ReactiveType]`

Create a reactive attribute.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `default` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.reactive\(default\) "Permanent link") | `ReactiveType \| [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[], ReactiveType]` | A default value or callable that returns a default. | *required* |
| ### `layout` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.reactive\(layout\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Perform a layout on change. | `False` |
| ### `repaint` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.reactive\(repaint\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Perform a repaint on change. | `True` |
| ### `init` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.reactive\(init\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Call watchers on initialize (post mount). | `True` |
| ### `always_update` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.reactive\(always_update\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Call watchers even when the new value equals the old value. | `False` |
| ### `bindings` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.reactive\(bindings\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Refresh bindings when the reactive changes. | `False` |

## var [¶](https://textual.textualize.io/api/reactive/#textual.reactive.var "Permanent link")

```
var(
    , =True, =False, =False
)
```

Bases: `[ReactiveType]`

Create a reactive attribute (with no auto-refresh).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `default` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.var\(default\) "Permanent link") | `ReactiveType \| [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[], ReactiveType]` | A default value or callable that returns a default. | *required* |
| ### `init` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.var\(init\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Call watchers on initialize (post mount). | `True` |
| ### `always_update` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.var\(always_update\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Call watchers even when the new value equals the old value. | `False` |
| ### `bindings` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.var\(bindings\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Refresh bindings when the reactive changes. | `False` |

## await\_watcher [¶](https://textual.textualize.io/api/reactive/#textual.reactive.await_watcher "Permanent link")

```
await_watcher(obj, awaitable)
```

Coroutine to await an awaitable returned from a watcher

## invoke\_watcher [¶](https://textual.textualize.io/api/reactive/#textual.reactive.invoke_watcher "Permanent link")

```
invoke_watcher(
    , , , 
)
```

Invoke a watch function.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `watcher_object` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.invoke_watcher\(watcher_object\) "Permanent link") | `Reactable` | The object watching for the changes. | *required* |
| ### `watch_function` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.invoke_watcher\(watch_function\) "Permanent link") | `[WatchCallbackType](https://textual.textualize.io/api/types/#textual.types.WatchCallbackType " WatchCallbackType (textual._types.WatchCallbackType)")` | A watch function, which may be sync or async. | *required* |
| ### `old_value` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.invoke_watcher\(old_value\) "Permanent link") | `[object](https://docs.python.org/3/library/functions.html#object)` | The old value of the attribute. | *required* |
| ### `value` [¶](https://textual.textualize.io/api/reactive/#textual.reactive.invoke_watcher\(value\) "Permanent link") | `[object](https://docs.python.org/3/library/functions.html#object)` | The new value of the attribute. | *required* |