---
title: "Textual - Link-color"
source: "https://textual.textualize.io/styles/links/link_color/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Link-color¶

The `link-color` style sets the color of the link text.

Note

`link-color` only applies to Textual action links as described in the [actions guide](https://textual.textualize.io/guide/actions/#links) and not to regular hyperlinks.

## Syntax¶

```
link-color: <color> [<percentage>];
```

`link-color` accepts a [`<color>`](https://textual.textualize.io/css_types/color/) (with an optional opacity level defined by a [`<percentage>`](https://textual.textualize.io/css_types/percentage/)) that is used to define the color of text enclosed in Textual action links.

## Example¶

The example below shows some links with their color changed. It also shows that `link-color` does not affect hyperlinks.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Label

class LinkColorApp(App):
    CSS_PATH = "link_color.tcss"

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
    app = LinkColorApp()
    app.run()
```

1. This label has a hyperlink so it won't be affected by the `link-color` rule.
2. This label has an "action link" that can be styled with `link-color`.
3. This label has an "action link" that can be styled with `link-color`.
4. This label has an "action link" that can be styled with `link-color`.

```
#lbl1, #lbl2 {
    link-color: red;  
}

#lbl3 {
    link-color: hsl(60,100%,50%) 50%;
}

#lbl4 {
    link-color: $accent;
}
```

1. This will only affect one of the labels because action links are the only links that this rule affects.

## CSS¶

```
link-color: red 70%;
link-color: $accent;
```

## Python¶

```
widget.styles.link_color = "red 70%"
widget.styles.link_color = "$accent"

# You can also use a \`Color\` object directly:
widget.styles.link_color = Color(100, 30, 173)
```

## See also¶

- [`link-background`](https://textual.textualize.io/styles/links/link_background/) to set the background color of link text.
- [`link-color-hover`](https://textual.textualize.io/styles/links/link_color_hover/) to set the color of link text when the mouse pointer is over it.