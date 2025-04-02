---
title: "Textual - textual"
source: "https://textual.textualize.io/api/logger/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual

The root Textual module.

Exposes some commonly used symbols.

## log [¶](https://textual.textualize.io/api/logger/#textual.log "Permanent link")

```
log = (None)
```

Global logger that logs to the currently active app.

Example
```
from textual import log
log(locals())
```

## Logger [¶](https://textual.textualize.io/api/logger/#textual.Logger "Permanent link")

```
Logger(log_callable, group=INFO, verbosity=NORMAL)
```

A [logger class](https://textual.textualize.io/guide/devtools/#logging-handler) that logs to the Textual [console](https://textual.textualize.io/guide/devtools#console).

### debug [¶](https://textual.textualize.io/api/logger/#textual.Logger.debug "Permanent link")

```
debug
```

Logs debug messages.

### error [¶](https://textual.textualize.io/api/logger/#textual.Logger.error "Permanent link")

```
error
```

Logs errors.

### event [¶](https://textual.textualize.io/api/logger/#textual.Logger.event "Permanent link")

```
event
```

Logs events.

### info [¶](https://textual.textualize.io/api/logger/#textual.Logger.info "Permanent link")

```
info
```

Logs information.

### logging [¶](https://textual.textualize.io/api/logger/#textual.Logger.logging "Permanent link")

```
logging
```

Logs from stdlib logging module.

### system [¶](https://textual.textualize.io/api/logger/#textual.Logger.system "Permanent link")

```
system
```

Logs system information.

### verbose [¶](https://textual.textualize.io/api/logger/#textual.Logger.verbose "Permanent link")

```
verbose
```

A verbose logger.

### warning [¶](https://textual.textualize.io/api/logger/#textual.Logger.warning "Permanent link")

```
warning
```

Logs warnings.

### worker [¶](https://textual.textualize.io/api/logger/#textual.Logger.worker "Permanent link")

```
worker
```

Logs worker information.

### verbosity [¶](https://textual.textualize.io/api/logger/#textual.Logger.verbosity "Permanent link")

```
verbosity()
```

Get a new logger with selective verbosity.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `verbose` [¶](https://textual.textualize.io/api/logger/#textual.Logger.verbosity\(verbose\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True to use HIGH verbosity, otherwise NORMAL. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New logger. |

## LoggerError [¶](https://textual.textualize.io/api/logger/#textual.LoggerError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when the logger failed.

## on [¶](https://textual.textualize.io/api/logger/#textual.on "Permanent link")

```
on(, =None, **)
```

Decorator to declare that the method is a message handler.

The decorator accepts an optional CSS selector that will be matched against a widget exposed by a `control` property on the message.

Example
```
# Handle the press of buttons with ID "#quit".
@on(Button.Pressed, "#quit")
def quit_button(self) -> None:
    self.app.quit()
```

Keyword arguments can be used to match additional selectors for attributes listed in [`ALLOW_SELECTOR_MATCH`](https://textual.textualize.io/api/message/#textual.message.Message.ALLOW_SELECTOR_MATCH " ALLOW_SELECTOR_MATCH").

Example
```
# Handle the activation of the tab "#home" within the \`TabbedContent\` "#tabs".
@on(TabbedContent.TabActivated, "#tabs", pane="#home")
def switch_to_home(self) -> None:
    self.log("Switching back to the home tab.")
    ...
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `message_type` [¶](https://textual.textualize.io/api/logger/#textual.on\(message_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")]` | The message type (i.e. the class). | *required* |
| ### `selector` [¶](https://textual.textualize.io/api/logger/#textual.on\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An optional [selector](https://textual.textualize.io/guide/CSS#selectors). If supplied, the handler will only be called if `selector` matches the widget from the `control` attribute of the message. | `None` |
| ### `**kwargs` [¶](https://textual.textualize.io/api/logger/#textual.on\(**kwargs\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Additional selectors for other attributes of the message. | `{}` |

## work [¶](https://textual.textualize.io/api/logger/#textual.work "Permanent link")

```
work(
    : Callable[
        FactoryParamSpec, Coroutine[None, None, ReturnType]
    ],
    *,
    : str = "",
    : str = "default",
    : bool = True,
    : bool = False,
    : str | None = None,
    : bool = False
) -> Callable[FactoryParamSpec, "Worker[ReturnType]"]
```
```
work(
    : Callable[FactoryParamSpec, ReturnType],
    *,
    : str = "",
    : str = "default",
    : bool = True,
    : bool = False,
    : str | None = None,
    : bool = False
) -> Callable[FactoryParamSpec, "Worker[ReturnType]"]
```
```
work(
    *,
    : str = "",
    : str = "default",
    : bool = True,
    : bool = False,
    : str | None = None,
    : bool = False
) -> Decorator[..., ReturnType]
```

```
work(
    =None,
    *,
    ="",
    ="default",
    =True,
    =False,
    =None,
    =False
)
```

A decorator used to create [workers](https://textual.textualize.io/guide/workers).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `method` [¶](https://textual.textualize.io/api/logger/#textual.work\(method\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[FactoryParamSpec, ReturnType] \| [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[FactoryParamSpec, [Coroutine](https://docs.python.org/3/library/typing.html#typing.Coroutine "typing.Coroutine")[None, None, ReturnType]] \| None` | A function or coroutine. | `None` |
| ### `name` [¶](https://textual.textualize.io/api/logger/#textual.work\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A short string to identify the worker (in logs and debugging). | `''` |
| ### `group` [¶](https://textual.textualize.io/api/logger/#textual.work\(group\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A short string to identify a group of workers. | `'default'` |
| ### `exit_on_error` [¶](https://textual.textualize.io/api/logger/#textual.work\(exit_on_error\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Exit the app if the worker raises an error. Set to `False` to suppress exceptions. | `True` |
| ### `exclusive` [¶](https://textual.textualize.io/api/logger/#textual.work\(exclusive\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Cancel all workers in the same group. | `False` |
| ### `description` [¶](https://textual.textualize.io/api/logger/#textual.work\(description\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Readable description of the worker for debugging purposes. By default, it uses a string representation of the decorated method and its arguments. | `None` |
| ### `thread` [¶](https://textual.textualize.io/api/logger/#textual.work\(thread\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Mark the method as a thread worker. | `False` |