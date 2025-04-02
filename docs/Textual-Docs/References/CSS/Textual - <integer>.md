---
title: "Textual - <integer>"
source: "https://textual.textualize.io/css_types/integer/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <integer>¶

The `<integer>` CSS type represents an integer number.

## Syntax¶

An [`<integer>`](https://textual.textualize.io/css_types/integer/) is any valid integer number like `-10` or `42`.

Note

Some CSS rules may expect an `<integer>` within certain bounds. If that is the case, it will be noted in that rule.

## Examples¶

### CSS¶

```
.classname {
    offset: 10 -20
}
```

### Python¶

In Python, a rule that expects a CSS type `<integer>` will expect a value of the type `int`:

```
widget.styles.offset = (10, -20)
```