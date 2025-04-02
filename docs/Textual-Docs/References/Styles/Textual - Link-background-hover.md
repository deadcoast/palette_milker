---
title: "Textual - Link-background-hover"
source: "https://textual.textualize.io/styles/links/link_background_hover/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Link-background-hover¶

The `link-background-hover` style sets the background color of the link when the mouse cursor is over the link.

Note

`link-background-hover` only applies to Textual action links as described in the [actions guide](https://textual.textualize.io/guide/actions/#links) and not to regular hyperlinks.

## Syntax¶

```
link-background-hover: <color> [<percentage>];
```

`link-background-hover` accepts a [`<color>`](https://textual.textualize.io/css_types/color/) (with an optional opacity level defined by a [`<percentage>`](https://textual.textualize.io/css_types/percentage/)) that is used to define the background color of text enclosed in Textual action links when the mouse pointer is over it.

### Defaults¶

If not provided, a Textual action link will have `link-background-hover` set to `$accent`.

## Example¶

The example below shows some links that have their background color changed when the mouse moves over it and it shows that there is a default color for `link-background-hover`.

It also shows that `link-background-hover` does not affect hyperlinks.

![](https://textual.textualize.io/styles/links/demos/link_background_hover_demo.gif)

Note

The GIF has reduced quality to make it easier to load in the documentation. Try running the example yourself with `textual run docs/examples/styles/link_background_hover.py`.

```
from textual.app import App
from textual.widgets import Label

class LinkHoverBackgroundApp(App):
    CSS_PATH = "link_background_hover.tcss"

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
    app = LinkHoverBackgroundApp()
    app.run()
```

1. This label has a hyperlink so it won't be affected by the `link-background-hover` rule.
2. This label has an "action link" that can be styled with `link-background-hover`.
3. This label has an "action link" that can be styled with `link-background-hover`.
4. This label has an "action link" that can be styled with `link-background-hover`.

```
#lbl1, #lbl2 {
    link-background-hover: red;  
}

#lbl3 {
    link-background-hover: hsl(60,100%,50%) 50%;
}

#lbl4 {
    /* Empty to show the default hover background */ 
}
```

1. This will only affect one of the labels because action links are the only links that this rule affects.
2. The default behavior for links on hover is to change to a different background color, so we don't need to change anything if all we want is to add emphasis to the link under the mouse.

## CSS¶

```
link-background-hover: red 70%;
link-background-hover: $accent;
```

## Python¶

```
widget.styles.link_background_hover = "red 70%"
widget.styles.link_background_hover = "$accent"

# You can also use a \`Color\` object directly:
widget.styles.link_background_hover = Color(100, 30, 173)
```

## See also¶

- [`link-background`](https://textual.textualize.io/styles/links/link_background/) to set the background color of link text.
- [`link-color-hover`](https://textual.textualize.io/styles/links/link_color_hover/) to set the color of link text when the mouse pointer is over it.
- [`link-style-hover`](https://textual.textualize.io/styles/links/link_style_hover/) to set the style of link text when the mouse pointer is over it.