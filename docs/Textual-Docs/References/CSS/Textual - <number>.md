---
title: "Textual - <number>"
source: "https://textual.textualize.io/css_types/number/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <number>¶

The `<number>` CSS type represents a real number, which can be an integer or a number with a decimal part (akin to a `float` in Python).

## Syntax¶

A [`<number>`](https://textual.textualize.io/css_types/number/) is an [`<integer>`](https://textual.textualize.io/css_types/integer/), optionally followed by the decimal point `.` and a decimal part composed of one or more digits.

## Examples¶

### CSS¶

```
Grid {
    grid-size: 3 6  /* Integers are numbers */
}

.translucid {
    opacity: 0.5    /* Numbers can have a decimal part */
}
```

### Python¶

In Python, a rule that expects a CSS type `<number>` will accept an `int` or a `float`:

```
widget.styles.grid_size = (3, 6)  # Integers are numbers
widget.styles.opacity = 0.5       # Numbers can have a decimal part
```