---
title: "Textual - Link-background"
source: "https://textual.textualize.io/styles/links/link_background/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Link-background¶

The `link-background` style sets the background color of the link.

Note

`link-background` only applies to Textual action links as described in the [actions guide](https://textual.textualize.io/guide/actions/#links) and not to regular hyperlinks.

## Syntax¶

```
link-background: <color> [<percentage>];
```

`link-background` accepts a [`<color>`](https://textual.textualize.io/css_types/color/) (with an optional opacity level defined by a [`<percentage>`](https://textual.textualize.io/css_types/percentage/)) that is used to define the background color of text enclosed in Textual action links.

## Example¶

The example below shows some links with their background color changed. It also shows that `link-background` does not affect hyperlinks.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Label

class LinkBackgroundApp(App):
    CSS_PATH = "link_background.tcss"

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
    app = LinkBackgroundApp()
    app.run()
```

1. This label has a hyperlink so it won't be affected by the `link-background` rule.
2. This label has an "action link" that can be styled with `link-background`.
3. This label has an "action link" that can be styled with `link-background`.
4. This label has an "action link" that can be styled with `link-background`.

```
#lbl1, #lbl2 {
    link-background: red;  
}

#lbl3 {
    link-background: hsl(60,100%,50%) 50%;
}

#lbl4 {
    link-background: $accent;
}
```

1. This will only affect one of the labels because action links are the only links that this rule affects.

## CSS¶

```
link-background: red 70%;
link-background: $accent;
```

## Python¶

```
widget.styles.link_background = "red 70%"
widget.styles.link_background = "$accent"

# You can also use a \`Color\` object directly:
widget.styles.link_background = Color(100, 30, 173)
```

## See also¶

- [`link-color`](https://textual.textualize.io/styles/links/link_color/) to set the color of link text.
- [`link-background-hover`](https://textual.textualize.io/styles/links/link_background_hover/) to set the background color of link text when the mouse pointer is over it.