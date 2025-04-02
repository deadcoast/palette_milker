---
title: "Textual - <text-align>"
source: "https://textual.textualize.io/css_types/text_align/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <text-align>¶

The `<text-align>` CSS type represents alignments that can be applied to text.

Warning

Not to be confused with the [`text-align`](https://textual.textualize.io/styles/text_align/) CSS rule that sets the alignment of text in a widget.

## Syntax¶

A [`<text-align>`](https://textual.textualize.io/css_types/text_align/) can be any of the following values:

| Value | Alignment type |
| --- | --- |
| `center` | Center alignment. |
| `end` | Alias for `right`. |
| `justify` | Text is justified inside the widget. |
| `left` | Left alignment. |
| `right` | Right alignment. |
| `start` | Alias for `left`. |

Tip

The meanings of `start` and `end` will likely change when RTL languages become supported by Textual.

## Examples¶

### CSS¶

```
Label {
    text-align: justify;
}
```

### Python¶

```
widget.styles.text_align = "justify"
```