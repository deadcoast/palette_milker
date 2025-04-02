---
title: "Textual - Content-align"
source: "https://textual.textualize.io/styles/content_align/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Content-align¶

The `content-align` style aligns content *inside* a widget.

## Syntax¶

```
content-align: <horizontal> <vertical>;

content-align-horizontal: <horizontal>;
content-align-vertical: <vertical>;
```

The `content-align` style takes a [`<horizontal>`](https://textual.textualize.io/css_types/horizontal/) followed by a [`<vertical>`](https://textual.textualize.io/css_types/vertical/).

You can specify the alignment of content on both the horizontal and vertical axes at the same time, or on each of the axis separately. To specify content alignment on a single axis, use the respective style and type:

- `content-align-horizontal` takes a [`<horizontal>`](https://textual.textualize.io/css_types/horizontal/) and does alignment along the horizontal axis; and
- `content-align-vertical` takes a [`<vertical>`](https://textual.textualize.io/css_types/vertical/) and does alignment along the vertical axis.

## Examples¶

### Basic usage¶

This first example shows three labels stacked vertically, each with different content alignments.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Label

class ContentAlignApp(App):
    CSS_PATH = "content_align.tcss"

    def compose(self):
        yield Label("With [i]content-align[/] you can...", id="box1")
        yield Label("...[b]Easily align content[/]...", id="box2")
        yield Label("...Horizontally [i]and[/] vertically!", id="box3")

if __name__ == "__main__":
    app = ContentAlignApp()
    app.run()
```

```
#box1 {
    content-align: left top;
    background: red;
}

#box2 {
    content-align-horizontal: center;
    content-align-vertical: middle;
    background: green;
}

#box3 {
    content-align: right bottom;
    background: blue;
}

Label {
    width: 100%;
    height: 1fr;
    padding: 1;
    color: white;
}
```

### All content alignments¶

The next example shows a 3 by 3 grid of labels. Each label has its text aligned differently.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Label

class AllContentAlignApp(App):
    CSS_PATH = "content_align_all.tcss"

    def compose(self):
        yield Label("left top", id="left-top")
        yield Label("center top", id="center-top")
        yield Label("right top", id="right-top")
        yield Label("left middle", id="left-middle")
        yield Label("center middle", id="center-middle")
        yield Label("right middle", id="right-middle")
        yield Label("left bottom", id="left-bottom")
        yield Label("center bottom", id="center-bottom")
        yield Label("right bottom", id="right-bottom")

if __name__ == "__main__":
    app = AllContentAlignApp()
    app.run()
```

```
#left-top {
    /* content-align: left top; this is the default implied value. */
}
#center-top {
    content-align: center top;
}
#right-top {
    content-align: right top;
}
#left-middle {
    content-align: left middle;
}
#center-middle {
    content-align: center middle;
}
#right-middle {
    content-align: right middle;
}
#left-bottom {
    content-align: left bottom;
}
#center-bottom {
    content-align: center bottom;
}
#right-bottom {
    content-align: right bottom;
}

Screen {
    layout: grid;
    grid-size: 3 3;
    grid-gutter: 1;
}

Label {
    width: 100%;
    height: 100%;
    background: $primary;
}
```

## CSS¶

```
/* Align content in the very center of a widget */
content-align: center middle;
/* Align content at the top right of a widget */
content-align: right top;

/* Change the horizontal alignment of the content of a widget */
content-align-horizontal: right;
/* Change the vertical alignment of the content of a widget */
content-align-vertical: middle;
```

## Python¶

```
# Align content in the very center of a widget
widget.styles.content_align = ("center", "middle")
# Align content at the top right of a widget
widget.styles.content_align = ("right", "top")

# Change the horizontal alignment of the content of a widget
widget.styles.content_align_horizontal = "right"
# Change the vertical alignment of the content of a widget
widget.styles.content_align_vertical = "middle"
```

## See also¶

- [`align`](https://textual.textualize.io/styles/align/) to set the alignment of children widgets inside a container.
- [`text-align`](https://textual.textualize.io/styles/text_align/) to set the alignment of text in a widget.