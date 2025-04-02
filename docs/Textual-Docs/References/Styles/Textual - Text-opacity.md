---
title: "Textual - Text-opacity"
source: "https://textual.textualize.io/styles/text_opacity/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Text-opacity¶

The `text-opacity` style blends the foreground color (i.e. text) with the background color.

## Syntax¶

```
text-opacity: <number> | <percentage>;
```

The text opacity of a widget can be set as a [`<number>`](https://textual.textualize.io/css_types/number/) or a [`<percentage>`](https://textual.textualize.io/css_types/percentage/). If given as a number, then `text-opacity` should be a value between 0 and 1, where 0 makes the foreground color match the background (effectively making text invisible) and 1 will display text as normal. If given as a percentage, 0% will result in invisible text, and 100% will display fully opaque text.

Typically, if you set this value it would be somewhere between the two extremes. For instance, setting `text-opacity` to `70%` would result in slightly faded text. Setting it to `0.3` would result in very dim text.

Warning

Be careful not to set text opacity so low as to make it hard to read.

## Example¶

This example shows, from top to bottom, increasing `text-opacity` values.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Label

class TextOpacityApp(App):
    CSS_PATH = "text_opacity.tcss"

    def compose(self):
        yield Label("text-opacity: 0%", id="zero-opacity")
        yield Label("text-opacity: 25%", id="quarter-opacity")
        yield Label("text-opacity: 50%", id="half-opacity")
        yield Label("text-opacity: 75%", id="three-quarter-opacity")
        yield Label("text-opacity: 100%", id="full-opacity")

if __name__ == "__main__":
    app = TextOpacityApp()
    app.run()
```

```
#zero-opacity {
    text-opacity: 0%;
}

#quarter-opacity {
    text-opacity: 25%;
}

#half-opacity {
    text-opacity: 50%;
}

#three-quarter-opacity {
    text-opacity: 75%;
}

#full-opacity {
    text-opacity: 100%;
}

Label {
    height: 1fr;
    width: 100%;
    text-align: center;
    text-style: bold;
}
```

## CSS¶

```
/* Set the text to be "half-faded" against the background of the widget */
text-opacity: 50%;
```

## Python¶

```
# Set the text to be "half-faded" against the background of the widget
widget.styles.text_opacity = "50%"
```

## See also¶

- [`opacity`](https://textual.textualize.io/styles/opacity/) to specify the opacity of a whole widget.