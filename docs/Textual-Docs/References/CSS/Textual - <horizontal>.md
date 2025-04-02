---
title: "Textual - <horizontal>"
source: "https://textual.textualize.io/css_types/horizontal/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <horizontal>¶

The `<horizontal>` CSS type represents a position along the horizontal axis.

## Syntax¶

The [`<horizontal>`](https://textual.textualize.io/css_types/horizontal/) type can take any of the following values:

| Value | Description |
| --- | --- |
| `center` | Aligns in the center of the horizontal axis. |
| `left` (default) | Aligns on the left of the horizontal axis. |
| `right` | Aligns on the right of the horizontal axis. |

## Examples¶

### CSS¶

```
.container {
    align-horizontal: right;
}
```

### Python¶

```
widget.styles.align_horizontal = "right"
```