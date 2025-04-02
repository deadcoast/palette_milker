---
title: "Textual - textual.work"
source: "https://textual.textualize.io/api/work/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.work

A decorator used to create [workers](https://textual.textualize.io/guide/workers).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `method` [¶](https://textual.textualize.io/api/work/#textual.work\(method\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[FactoryParamSpec, ReturnType] \| [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[FactoryParamSpec, [Coroutine](https://docs.python.org/3/library/typing.html#typing.Coroutine "typing.Coroutine")[None, None, ReturnType]] \| None` | A function or coroutine. | `None` |
| ## `name` [¶](https://textual.textualize.io/api/work/#textual.work\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A short string to identify the worker (in logs and debugging). | `''` |
| ## `group` [¶](https://textual.textualize.io/api/work/#textual.work\(group\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A short string to identify a group of workers. | `'default'` |
| ## `exit_on_error` [¶](https://textual.textualize.io/api/work/#textual.work\(exit_on_error\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Exit the app if the worker raises an error. Set to `False` to suppress exceptions. | `True` |
| ## `exclusive` [¶](https://textual.textualize.io/api/work/#textual.work\(exclusive\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Cancel all workers in the same group. | `False` |
| ## `description` [¶](https://textual.textualize.io/api/work/#textual.work\(description\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Readable description of the worker for debugging purposes. By default, it uses a string representation of the decorated method and its arguments. | `None` |
| ## `thread` [¶](https://textual.textualize.io/api/work/#textual.work\(thread\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Mark the method as a thread worker. | `False` |