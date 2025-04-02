---
title: "Textual - Link-color-hover"
source: "https://textual.textualize.io/styles/links/link_color_hover/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Link-color-hover¶

The `link-color-hover` style sets the color of the link text when the mouse cursor is over the link.

Note

`link-color-hover` only applies to Textual action links as described in the [actions guide](https://textual.textualize.io/guide/actions/#links) and not to regular hyperlinks.

## Syntax¶

```
link-color-hover: <color> [<percentage>];
```

`link-color-hover` accepts a [`<color>`](https://textual.textualize.io/css_types/color/) (with an optional opacity level defined by a [`<percentage>`](https://textual.textualize.io/css_types/percentage/)) that is used to define the color of text enclosed in Textual action links when the mouse pointer is over it.

### Defaults¶

If not provided, a Textual action link will have `link-color-hover` set to `white`.

## Example¶

The example below shows some links that have their color changed when the mouse moves over it. It also shows that `link-color-hover` does not affect hyperlinks.

![](https://textual.textualize.io/styles/links/demos/link_color_hover_demo.gif)

Note

The background color also changes when the mouse moves over the links because that is the default behavior. That can be customised by setting [`link-background-hover`](https://textual.textualize.io/styles/links/link_background_hover/) but we haven't done so in this example.

Note

The GIF has reduced quality to make it easier to load in the documentation. Try running the example yourself with `textual run docs/examples/styles/link_color_hover.py`.

```
from textual.app import App
from textual.widgets import Label

class LinkHoverColorApp(App):
    CSS_PATH = "link_color_hover.tcss"

    def compose(self):
        yield Label(
            "Visit the [link='https://textualize.io']Textualize[/link] website.",
            id="lbl1",  
        )
        yield Label(
            "Click [@click=app.bell]here[/] for the bell sound.",
            id="lbl2",  
        )
        yield Label(
            "You can also click [@click=app.bell]here[/] for the bell sound.",
            id="lbl3",  
        )
        yield Label(
            "[@click=app.quit]Exit this application.[/]",
            id="lbl4",  
        )

if __name__ == "__main__":
    app = LinkHoverColorApp()
    app.run()
```

1. This label has a hyperlink so it won't be affected by the `link-color-hover` rule.
2. This label has an "action link" that can be styled with `link-color-hover`.
3. This label has an "action link" that can be styled with `link-color-hover`.
4. This label has an "action link" that can be styled with `link-color-hover`.

```
#lbl1, #lbl2 {
    link-color-hover: red;  
}

#lbl3 {
    link-color-hover: hsl(60,100%,50%) 50%;
}

#lbl4 {
    link-color-hover: black;
}
```

1. This will only affect one of the labels because action links are the only links that this rule affects.

## CSS¶

```
link-color-hover: red 70%;
link-color-hover: black;
```

## Python¶

```
widget.styles.link_color_hover = "red 70%"
widget.styles.link_color_hover = "black"

# You can also use a \`Color\` object directly:
widget.styles.link_color_hover = Color(100, 30, 173)
```

## See also¶

- [`link-color`](https://textual.textualize.io/styles/links/link_color/) to set the color of link text.
- [`link-background-hover`](https://textual.textualize.io/styles/links/link_background_hover/) to set the background color of link text when the mouse pointer is over it.
- [`link-style-hover`](https://textual.textualize.io/styles/links/link_style_hover/) to set the style of link text when the mouse pointer is over it.