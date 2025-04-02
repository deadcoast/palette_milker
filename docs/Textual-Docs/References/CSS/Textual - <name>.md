---
title: "Textual - <name>"
source: "https://textual.textualize.io/css_types/name/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <name>¶

The `<name>` type represents a sequence of characters that identifies something.

## Syntax¶

A [`<name>`](https://textual.textualize.io/css_types/name/) is any non-empty sequence of characters:

- starting with a letter `a-z`, `A-Z`, or underscore `_`; and
- followed by zero or more letters `a-zA-Z`, digits `0-9`, underscores `_`, and hiphens `-`.

## Examples¶

### CSS¶

```
Screen {
    layers: onlyLetters Letters-and-hiphens _lead-under letters-1-digit;
}
```

### Python¶

```
widget.styles.layers = "onlyLetters Letters-and-hiphens _lead-under letters-1-digit"
```