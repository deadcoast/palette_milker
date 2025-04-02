---
title: "Textual - Link-style"
source: "https://textual.textualize.io/styles/links/link_style/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Link-style¶

The `link-style` style sets the text style for the link text.

Note

`link-style` only applies to Textual action links as described in the [actions guide](https://textual.textualize.io/guide/actions/#links) and not to regular hyperlinks.

## Syntax¶

```
link-style: <text-style>;
```

`link-style` will take all the values specified and will apply that styling to text that is enclosed by a Textual action link.

### Defaults¶

If not provided, a Textual action link will have `link-style` set to `underline`.

## Example¶

The example below shows some links with different styles applied to their text. It also shows that `link-style` does not affect hyperlinks.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Label

class LinkStyleApp(App):
    CSS_PATH = "link_style.tcss"

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
    app = LinkStyleApp()
    app.run()
```

1. This label has a hyperlink so it won't be affected by the `link-style` rule.
2. This label has an "action link" that can be styled with `link-style`.
3. This label has an "action link" that can be styled with `link-style`.
4. This label has an "action link" that can be styled with `link-style`.

```
#lbl1, #lbl2 {
    link-style: bold italic;  
}

#lbl3 {
    link-style: reverse strike;
}

#lbl4 {
    link-style: bold;
}
```

1. This will only affect one of the labels because action links are the only links that this rule affects.

## CSS¶

```
link-style: bold;
link-style: bold italic reverse;
```

## Python¶

```
widget.styles.link_style = "bold"
widget.styles.link_style = "bold italic reverse"
```

## See also¶

- [`link-style-hover`](https://textual.textualize.io/styles/links/link_style_hover/) to set the style of link text when the mouse pointer is over it.
- [`text-style`](https://textual.textualize.io/styles/text_style/) to set the style of text in a widget.