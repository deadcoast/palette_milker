---
title: "Textual - Key"
source: "https://textual.textualize.io/events/key/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
Bases: `[InputEvent](https://textual.textualize.io/api/events/#textual.events.InputEvent " InputEvent (textual.events.InputEvent)")`

Sent when the user hits a key on the keyboard.

- Bubbles
- Verbose

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `key` [¶](https://textual.textualize.io/events/key/#textual.events.Key\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The key that was pressed. | *required* |
| ## `character` [¶](https://textual.textualize.io/events/key/#textual.events.Key\(character\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A printable character or `None` if it is not printable. | *required* |

## aliases [¶](https://textual.textualize.io/events/key/#textual.events.Key.aliases "Permanent link")

```
aliases = _get_key_aliases(key)
```

The aliases for the key, including the key itself.

## character [¶](https://textual.textualize.io/events/key/#textual.events.Key.character "Permanent link")

```
character = (
    key
    if len(key) == 1
    else None if character is None else character
)
```

A printable character or `None` if it is not printable.

## is\_printable [¶](https://textual.textualize.io/events/key/#textual.events.Key.is_printable "Permanent link")

```
is_printable
```

Check if the key is printable (produces a unicode character).

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the key is printable. |

## key [¶](https://textual.textualize.io/events/key/#textual.events.Key.key "Permanent link")

```
key = key
```

The key that was pressed.

## name [¶](https://textual.textualize.io/events/key/#textual.events.Key.name "Permanent link")

```
name
```

Name of a key suitable for use as a Python identifier.

## name\_aliases [¶](https://textual.textualize.io/events/key/#textual.events.Key.name_aliases "Permanent link")

```
name_aliases
```

The corresponding name for every alias in `aliases` list.