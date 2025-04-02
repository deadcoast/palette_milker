---
title: "Textual - Link-style-hover"
source: "https://textual.textualize.io/styles/links/link_style_hover/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Link-style-hover¶

The `link-style-hover` style sets the text style for the link text when the mouse cursor is over the link.

Note

`link-style-hover` only applies to Textual action links as described in the [actions guide](https://textual.textualize.io/guide/actions/#links) and not to regular hyperlinks.

## Syntax¶

```
link-style-hover: <text-style>;
```

`link-style-hover` applies its [`<text-style>`](https://textual.textualize.io/css_types/text_style/) to the text of Textual action links when the mouse pointer is over them.

### Defaults¶

If not provided, a Textual action link will have `link-style-hover` set to `bold`.

## Example¶

The example below shows some links that have their color changed when the mouse moves over it. It also shows that `link-style-hover` does not affect hyperlinks.

![](https://textual.textualize.io/styles/links/demos/link_style_hover_demo.gif)

Note

The background color also changes when the mouse moves over the links because that is the default behavior. That can be customised by setting [`link-background-hover`](https://textual.textualize.io/styles/links/link_background_hover/) but we haven't done so in this example.

Note

The GIF has reduced quality to make it easier to load in the documentation. Try running the example yourself with `textual run docs/examples/styles/link_style_hover.py`.

```
from textual.app import App
from textual.widgets import Label

class LinkHoverStyleApp(App):
    CSS_PATH = "link_style_hover.tcss"

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
    app = LinkHoverStyleApp()
    app.run()
```

1. This label has a hyperlink so it won't be affected by the `link-style-hover` rule.
2. This label has an "action link" that can be styled with `link-style-hover`.
3. This label has an "action link" that can be styled with `link-style-hover`.
4. This label has an "action link" that can be styled with `link-style-hover`.

```
#lbl1, #lbl2 {
    link-style-hover: bold italic;  
}

#lbl3 {
    link-style-hover: reverse strike;
}

#lbl4 {
    link-style-hover: bold;
}
```

1. This will only affect one of the labels because action links are the only links that this rule affects.
2. The default behavior for links on hover is to change to a different text style, so we don't need to change anything if all we want is to add emphasis to the link under the mouse.

## CSS¶

```
link-style-hover: bold;
link-style-hover: bold italic reverse;
```

## Python¶

```
widget.styles.link_style_hover = "bold"
widget.styles.link_style_hover = "bold italic reverse"
```

## See also¶

- [`link-background-hover`](https://textual.textualize.io/styles/links/link_background_hover/) to set the background color of link text when the mouse pointer is over it.
- [`link-color-hover`](https://textual.textualize.io/styles/links/link_color_hover/) to set the color of link text when the mouse pointer is over it.
- [`link-style`](https://textual.textualize.io/styles/links/link_style/) to set the style of link text.
- [`text-style`](https://textual.textualize.io/styles/text_style/) to set the style of text in a widget.