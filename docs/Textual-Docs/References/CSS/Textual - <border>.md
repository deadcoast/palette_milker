---
title: "Textual - <border>"
source: "https://textual.textualize.io/css_types/border/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <border>¶

The `<border>` CSS type represents a border style.

## Syntax¶

The [`<border>`](https://textual.textualize.io/css_types/border/) type can take any of the following values:

| Border type | Description |
| --- | --- |
| `ascii` | A border with plus, hyphen, and vertical bar characters. |
| `blank` | A blank border (reserves space for a border). |
| `dashed` | Dashed line border. |
| `double` | Double lined border. |
| `heavy` | Heavy border. |
| `hidden` | Alias for "none". |
| `hkey` | Horizontal key-line border. |
| `inner` | Thick solid border. |
| `none` | Disabled border. |
| `outer` | Solid border with additional space around content. |
| `panel` | Solid border with thick top. |
| `round` | Rounded corners. |
| `solid` | Solid border. |
| `tall` | Solid border with additional space top and bottom. |
| `thick` | Border style that is consistently thick across edges. |
| `vkey` | Vertical key-line border. |
| `wide` | Solid border with additional space left and right. |

## Border command¶

The `textual` CLI has a subcommand which will let you explore the various border types interactively, when applied to the CSS rule [`border`](https://textual.textualize.io/styles/border/):

```
textual borders
```

## Examples¶

### CSS¶

```
#container {
    border: heavy red;
}

#heading {
    border-bottom: solid blue;
}
```

### Python¶

```
widget.styles.border = ("heavy", "red")
widget.styles.border_bottom = ("solid", "blue")
```