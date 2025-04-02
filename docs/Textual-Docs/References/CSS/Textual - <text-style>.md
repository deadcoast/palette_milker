---
title: "Textual - <text-style>"
source: "https://textual.textualize.io/css_types/text_style/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <text-style>¶

The `<text-style>` CSS type represents styles that can be applied to text.

Warning

Not to be confused with the [`text-style`](https://textual.textualize.io/styles/text_style/) CSS rule that sets the style of text in a widget.

## Syntax¶

A [`<text-style>`](https://textual.textualize.io/css_types/text_style/) can be the value `none` for plain text with no styling, or any *space-separated* combination of the following values:

| Value | Description |
| --- | --- |
| `bold` | **Bold text.** |
| `italic` | *Italic text.* |
| `reverse` | Reverse video text (foreground and background colors reversed). |
| `strike` | ~~Strikethrough text.~~ |
| `underline` | Underline text. |

## Examples¶

### CSS¶

```
#label1 {
    /* You can specify any value by itself. */
    rule: strike;
}

#label2 {
    /* You can also combine multiple values. */
    rule: strike bold italic reverse;
}
```

### Python¶

```
# You can specify any value by itself
widget.styles.text_style = "strike"

# You can also combine multiple values
widget.styles.text_style = "strike bold italic reverse
```