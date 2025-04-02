---
title: "Textual - <keyline>"
source: "https://textual.textualize.io/css_types/keyline/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <keyline>¶

The `<keyline>` CSS type represents a line style used in the [keyline](https://textual.textualize.io/styles/keyline/) rule.

## Syntax¶

| Value | Description |
| --- | --- |
| `none` | No line (disable keyline). |
| `thin` | A thin line. |
| `heavy` | A heavy (thicker) line. |
| `double` | A double line. |

## Examples¶

### CSS¶

```
Vertical {
    keyline: thin green;
}
```

### Python¶

```
# A tuple of <keyline> and color
widget.styles.keyline = ("thin", "green")
```