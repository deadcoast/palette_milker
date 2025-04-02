---
title: "Textual - <hatch>"
source: "https://textual.textualize.io/css_types/hatch/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <hatch>¶

The `<hatch>` CSS type represents a character used in the [hatch](https://textual.textualize.io/styles/hatch/) rule.

## Syntax¶

| Value | Description |
| --- | --- |
| `cross` | A diagonal crossed line. |
| `horizontal` | A horizontal line. |
| `left` | A left leaning diagonal line. |
| `right` | A right leaning diagonal line. |
| `vertical` | A vertical line. |

## Examples¶

### CSS¶

```
.some-class {
    hatch: cross green;
}
```

### Python¶

```
widget.styles.hatch = ("cross", "red")
```