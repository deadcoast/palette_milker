---
title: "Textual - textual.await_remove"
source: "https://textual.textualize.io/api/await_remove/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.await\_remove

This module contains the `AwaitRemove` class. An `AwaitRemove` object is returned by [`Widget.remove()`](https://textual.textualize.io/api/widget/#textual.widget.Widget.remove " remove") and other methods which remove widgets. You can await the return value if you need to know exactly when the widget(s) have been removed. Or you can ignore it and Textual will wait for the widgets to be removed before handling the next message.

Note

You are unlikely to need to explicitly create these objects yourself.

An *optionally* awaitable object returned by methods that remove widgets.

## AwaitRemove [¶](https://textual.textualize.io/api/await_remove/#textual.await_remove.AwaitRemove "Permanent link")

```
AwaitRemove(tasks, post_remove=None)
```

An awaitable that waits for nodes to be removed.