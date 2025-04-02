---
title: "Textual - <percentage>"
source: "https://textual.textualize.io/css_types/percentage/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <percentage>¶

The `<percentage>` CSS type represents a percentage value. It is often used to represent values that are relative to the parent's values.

Warning

Not to be confused with the [`<scalar>`](https://textual.textualize.io/css_types/scalar/) type.

## Syntax¶

A [`<percentage>`](https://textual.textualize.io/css_types/percentage/) is a [`<number>`](https://textual.textualize.io/css_types/number/) followed by the percent sign `%` (without spaces). Some rules may clamp the values between `0%` and `100%`.

## Examples¶

### CSS¶

```
#footer {
    /* Integer followed by % */
    color: red 70%;

    /* The number can be negative/decimal, although that may not make sense */
    offset: -30% 12.5%;
}
```

### Python¶

```
# Integer followed by %
widget.styles.color = "red 70%"

# The number can be negative/decimal, although that may not make sense
widget.styles.offset = ("-30%", "12.5%")
```