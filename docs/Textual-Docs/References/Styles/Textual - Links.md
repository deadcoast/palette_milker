---
title: "Textual - Links"
source: "https://textual.textualize.io/styles/links/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Links¶

Textual supports the concept of inline "links" embedded in text which trigger an action when pressed. There are a number of styles which influence the appearance of these links within a widget.

Note

These CSS rules only target Textual action links. Internet hyperlinks are not affected by these styles.

| Property | Description |
| --- | --- |
| [`link-background`](https://textual.textualize.io/styles/links/link_background/) | The background color of the link text. |
| [`link-background-hover`](https://textual.textualize.io/styles/links/link_background_hover/) | The background color of the link text when the cursor is over it. |
| [`link-color`](https://textual.textualize.io/styles/links/link_color/) | The color of the link text. |
| [`link-color-hover`](https://textual.textualize.io/styles/links/link_color_hover/) | The color of the link text when the cursor is over it. |
| [`link-style`](https://textual.textualize.io/styles/links/link_style/) | The style of the link text (e.g. underline). |
| [`link-style-hover`](https://textual.textualize.io/styles/links/link_style_hover/) | The style of the link text when the cursor is over it. |

## Syntax¶

```
link-background: <color> [<percentage>];

link-color: <color> [<percentage>];

link-style: <text-style>;

link-background-hover: <color> [<percentage>];

link-color-hover: <color> [<percentage>];

link-style-hover: <text-style>;
```

Visit each style's reference page to learn more about how the values are used.

## Example¶

In the example below, the first label illustrates default link styling. The second label uses CSS to customize the link color, background, and style.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Static

TEXT = """\
Here is a [@click='app.bell']link[/] which you can click!
"""

class LinksApp(App):
    CSS_PATH = "links.tcss"

    def compose(self) -> ComposeResult:
        yield Static(TEXT)
        yield Static(TEXT, id="custom")

if __name__ == "__main__":
    app = LinksApp()
    app.run()
```

```
#custom {
    link-color: black 90%;
    link-background: dodgerblue;
    link-style: bold italic underline;
}
```

## Additional Notes¶

- Inline links are not widgets, and thus cannot be focused.

## See Also¶

- An [introduction to links](https://textual.textualize.io/guide/actions/#links) in the Actions guide.