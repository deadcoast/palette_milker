---
title: "Textual - textual.errors"
source: "https://textual.textualize.io/api/errors/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.errors

General exception classes.

## DuplicateKeyHandlers [¶](https://textual.textualize.io/api/errors/#textual.errors.DuplicateKeyHandlers "Permanent link")

Bases:

More than one handler for a single key press.

For example, if the handlers `key_ctrl_i` and `key_tab` were defined on the same widget, then this error would be raised.

## NoWidget [¶](https://textual.textualize.io/api/errors/#textual.errors.NoWidget "Permanent link")

Bases:

Specified widget was not found.

## RenderError [¶](https://textual.textualize.io/api/errors/#textual.errors.RenderError "Permanent link")

Bases:

An object could not be rendered.

## TextualError [¶](https://textual.textualize.io/api/errors/#textual.errors.TextualError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Base class for Textual errors.