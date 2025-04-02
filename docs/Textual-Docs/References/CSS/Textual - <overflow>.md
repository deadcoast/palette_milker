---
title: "Textual - <overflow>"
source: "https://textual.textualize.io/css_types/overflow/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <overflow>¶

The `<overflow>` CSS type represents overflow modes.

## Syntax¶

The [`<overflow>`](https://textual.textualize.io/css_types/overflow/) type can take any of the following values:

| Value | Description |
| --- | --- |
| `auto` | Determine overflow mode automatically. |
| `hidden` | Don't overflow. |
| `scroll` | Allow overflowing. |

## Examples¶

### CSS¶

```
#container {
    overflow-y: hidden;  /* Don't overflow */
}
```

### Python¶

```
widget.styles.overflow_y = "hidden"  # Don't overflow
```