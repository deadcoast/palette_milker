---
title: "Textual - <vertical>"
source: "https://textual.textualize.io/css_types/vertical/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <vertical>¶

The `<vertical>` CSS type represents a position along the vertical axis.

## Syntax¶

The [`<vertical>`](https://textual.textualize.io/css_types/vertical/) type can take any of the following values:

| Value | Description |
| --- | --- |
| `bottom` | Aligns at the bottom of the vertical axis. |
| `middle` | Aligns in the middle of the vertical axis. |
| `top` (default) | Aligns at the top of the vertical axis. |

## Examples¶

### CSS¶

```
.container {
    align-vertical: top;
}
```

### Python¶

```
widget.styles.align_vertical = "top"
```