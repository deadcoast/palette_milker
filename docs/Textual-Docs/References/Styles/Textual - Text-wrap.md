---
title: "Textual - Text-wrap"
source: "https://textual.textualize.io/styles/text_wrap/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Text-wrap¶

The `text-wrap` style set how Textual should wrap text. The default value is "wrap" which will word-wrap text. You can also set this style to "nowrap" which will disable wrapping entirely.

## Syntax¶

```
text-wrap: wrap | nowrap;
```

## Example¶

In the following example we have two pieces of text.

The first (top) text has the default value for `text-wrap` ("wrap") which will cause text to be word wrapped as normal. The second has `text-wrap` set to "nowrap" which disables text wrapping and results in a single line.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Static

TEXT = """I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear."""

class WrapApp(App):
    CSS_PATH = "text_wrap.tcss"

    def compose(self) -> ComposeResult:
        yield Static(TEXT, id="static1")
        yield Static(TEXT, id="static2")

if __name__ == "__main__":
    app = WrapApp()
    app.run()
```

```
Static {
    height: 1fr;
}

#static1 {
    text-wrap: wrap; /* this is the default */
    background: blue 20%;
}
#static2 {
    text-wrap: nowrap; /* disable wrapping */
    background: green 20%;
}
```

## CSS¶

```
text-wrap: wrap;
text-wrap: nowrap;
```

## Python¶

```
widget.styles.text_wrap = "wrap"
widget.styles.text_wrap = "nowrap"
```

## See also¶

- [`text-overflow`](https://textual.textualize.io/styles/text_overflow/) to set what happens to text that overflows the available width.