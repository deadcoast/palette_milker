---
title: "Textual - Border-title-background"
source: "https://textual.textualize.io/styles/border_title_background/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Border-title-background¶

The `border-title-background` style sets the *background* color of the [border\_title](https://textual.textualize.io/api/widget/#textual.widget.Widget.border_title " border_title").

## Syntax¶

```
border-title-background: (<color> | auto) [<percentage>];
```

## Example¶

The following examples demonstrates customization of the border color and text style rules.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Label

class BorderTitleApp(App):
    CSS_PATH = "border_title_colors.tcss"

    def compose(self) -> ComposeResult:
        yield Label("Hello, World!")

    def on_mount(self) -> None:
        label = self.query_one(Label)
        label.border_title = "Textual Rocks"
        label.border_subtitle = "Textual Rocks"

if __name__ == "__main__":
    app = BorderTitleApp()
    app.run()
```

```
Screen {
    align: center middle;
}

Label {
    padding: 4 8;
    border: heavy red;

    border-title-color: green;
    border-title-background: white;
    border-title-style: bold;

    border-subtitle-color: magenta;
    border-subtitle-background: yellow;
    border-subtitle-style: italic;
}
```

## CSS¶

```
border-title-background: blue;
```

## Python¶

```
widget.styles.border_title_background = "blue"
```

## See also¶

- [`border-title-align`](https://textual.textualize.io/styles/border_title_align/) to set the title's alignment.
- [`border-title-color`](https://textual.textualize.io/styles/border_subtitle_color/) to set the title's color.
- [`border-title-background`](https://textual.textualize.io/styles/border_subtitle_background/) to set the title's background color.
- [`border-title-style`](https://textual.textualize.io/styles/border_subtitle_style/) to set the title's text style.
- [`border-subtitle-align`](https://textual.textualize.io/styles/border_subtitle_align/) to set the sub-title's alignment.
- [`border-subtitle-color`](https://textual.textualize.io/styles/border_subtitle_color/) to set the sub-title's color.
- [`border-subtitle-background`](https://textual.textualize.io/styles/border_subtitle_background/) to set the sub-title's background color.
- [`border-subtitle-style`](https://textual.textualize.io/styles/border_subtitle_style/) to set the sub-title's text style.