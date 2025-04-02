---
title: "Textual - Box-sizing"
source: "https://textual.textualize.io/styles/box_sizing/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Box-sizing¶

The `box-sizing` style determines how the width and height of a widget are calculated.

## Syntax¶

```
box-sizing: border-box | content-box;
```

### Values¶

| Value | Description |
| --- | --- |
| `border-box` (default) | Padding and border are included in the width and height. If you add padding and/or border the widget will not change in size, but you will have less space for content. |
| `content-box` | Padding and border will increase the size of the widget, leaving the content area unaffected. |

## Example¶

Both widgets in this example have the same height (5). The top widget has `box-sizing: border-box` which means that padding and border reduce the space for content. The bottom widget has `box-sizing: content-box` which increases the size of the widget to compensate for padding and border.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Static

class BoxSizingApp(App):
    CSS_PATH = "box_sizing.tcss"

    def compose(self):
        yield Static("I'm using border-box!", id="static1")
        yield Static("I'm using content-box!", id="static2")

if __name__ == "__main__":
    app = BoxSizingApp()
    app.run()
```

```
#static1 {
    box-sizing: border-box;
}

#static2 {
    box-sizing: content-box;
}

Screen {
    background: white;
    color: black;
}

App Static {
    background: blue 20%;
    height: 5;
    margin: 2;
    padding: 1;
    border: wide black;
}
```

## CSS¶

```
/* Set box sizing to border-box (default) */
box-sizing: border-box;

/* Set box sizing to content-box */
box-sizing: content-box;
```

## Python¶

```
# Set box sizing to border-box (default)
widget.box_sizing = "border-box"

# Set box sizing to content-box
widget.box_sizing = "content-box"
```

## See also¶

- [`border`](https://textual.textualize.io/styles/border/) to add a border around a widget.
- [`padding`](https://textual.textualize.io/styles/padding/) to add spacing around the content of a widget.