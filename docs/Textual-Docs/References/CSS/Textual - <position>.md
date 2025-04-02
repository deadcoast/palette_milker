---
title: "Textual - <position>"
source: "https://textual.textualize.io/css_types/position/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <position>¶

The `<position>` CSS type defines how the the `offset` rule is applied..

## Syntax¶

A [`<position>`](https://textual.textualize.io/css_types/position/) may be any of the following values:

| Value | Alignment type |
| --- | --- |
| `relative` | Offset is applied to widgets default position. |
| `absolute` | Offset is applied to the origin (top left) of its container. |

## Examples¶

### CSS¶

```
Label {
    position: absolute;
    offset: 10 5;
}
```

### Python¶

```
widget.styles.position = "absolute"
widget.styles.offset = (10, 5)
```