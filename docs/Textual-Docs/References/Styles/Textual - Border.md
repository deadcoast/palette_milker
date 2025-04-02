---
title: "Textual - Border"
source: "https://textual.textualize.io/styles/border/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Border¶

The `border` style enables the drawing of a box around a widget.

A border style may also be applied to individual edges with `border-top`, `border-right`, `border-bottom`, and `border-left`.

Note

[`border`](https://textual.textualize.io/styles/border/) and [`outline`](https://textual.textualize.io/styles/outline/) cannot coexist in the same edge of a widget.

## Syntax¶

```
border: [<border>] [<color>] [<percentage>];

border-top: [<border>] [<color>] [<percentage>];
border-right: [<border>] [<color> [<percentage>]];
border-bottom: [<border>] [<color> [<percentage>]];
border-left: [<border>] [<color> [<percentage>]];
```

In CSS, the border is set with a [border style](https://textual.textualize.io/styles/border/) and a color. Both are optional. An optional percentage may be added to blend the border with the background color.

In Python, the border is set with a tuple of [border style](https://textual.textualize.io/styles/border/) and a color.

## Border command¶

The `textual` CLI has a subcommand which will let you explore the various border types interactively:

```
textual borders
```

Alternatively, you can see the examples below.

## Examples¶

### Basic usage¶

This examples shows three widgets with different border styles.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Label

class BorderApp(App):
    CSS_PATH = "border.tcss"

    def compose(self):
        yield Label("My border is solid red", id="label1")
        yield Label("My border is dashed green", id="label2")
        yield Label("My border is tall blue", id="label3")

if __name__ == "__main__":
    app = BorderApp()
    app.run()
```

```
#label1 {
    background: red 20%;
    color: red;
    border: solid red;
}

#label2 {
    background: green 20%;
    color: green;
    border: dashed green;
}

#label3 {
    background: blue 20%;
    color: blue;
    border: tall blue;
}

Screen {
    background: white;
}

Screen > Label {
    width: 100%;
    height: 5;
    content-align: center middle;
    color: white;
    margin: 1;
    box-sizing: border-box;
}
```

### All border types¶

The next example shows a grid with all the available border types.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Grid
from textual.widgets import Label

class AllBordersApp(App):
    CSS_PATH = "border_all.tcss"

    def compose(self):
        yield Grid(
            Label("ascii", id="ascii"),
            Label("blank", id="blank"),
            Label("dashed", id="dashed"),
            Label("double", id="double"),
            Label("heavy", id="heavy"),
            Label("hidden/none", id="hidden"),
            Label("hkey", id="hkey"),
            Label("inner", id="inner"),
            Label("outer", id="outer"),
            Label("panel", id="panel"),
            Label("round", id="round"),
            Label("solid", id="solid"),
            Label("tall", id="tall"),
            Label("thick", id="thick"),
            Label("vkey", id="vkey"),
            Label("wide", id="wide"),
        )

if __name__ == "__main__":
    app = AllBordersApp()
    app.run()
```

```
#ascii {
    border: ascii $accent;
}

#blank {
    border: blank $accent;
}

#dashed {
    border: dashed $accent;
}

#double {
    border: double $accent;
}

#heavy {
    border: heavy $accent;
}

#hidden {
    border: hidden $accent;
}

#hkey {
    border: hkey $accent;
}

#inner {
    border: inner $accent;
}

#outer {
    border: outer $accent;
}

#panel {
    border: panel $accent;
}

#round {
    border: round $accent;
}

#solid {
    border: solid $accent;
}

#tall {
    border: tall $accent;
}

#thick {
    border: thick $accent;
}

#vkey {
    border: vkey $accent;
}

#wide {
    border: wide $accent;
}

Grid {
    grid-size: 4 4;
    align: center middle;
    grid-gutter: 1 2;
}

Label {
    width: 20;
    height: 3;
    content-align: center middle;
}
```

### Borders and outlines¶

The next example makes the difference between [`border`](https://textual.textualize.io/styles/border/) and [`outline`](https://textual.textualize.io/styles/outline/) clearer by having three labels side-by-side. They contain the same text, have the same width and height, and are styled exactly the same up to their [`border`](https://textual.textualize.io/styles/border/) and [`outline`](https://textual.textualize.io/styles/outline/) styles.

This example also shows that a widget cannot contain both a `border` and an `outline`:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Label

TEXT = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain."""

class OutlineBorderApp(App):
    CSS_PATH = "outline_vs_border.tcss"

    def compose(self):
        yield Label(TEXT, classes="outline")
        yield Label(TEXT, classes="border")
        yield Label(TEXT, classes="outline border")

if __name__ == "__main__":
    app = OutlineBorderApp()
    app.run()
```

```
Label {
    height: 8;
}

.outline {
    outline: $error round;
}

.border {
    border: $success heavy;
}
```

## CSS¶

```
/* Set a heavy white border */
border: heavy white;

/* Set a red border on the left */
border-left: outer red;

/* Set a rounded orange border, 50% opacity. */
border: round orange 50%;
```

## Python¶

```
# Set a heavy white border
widget.styles.border = ("heavy", "white")

# Set a red border on the left
widget.styles.border_left = ("outer", "red")
```

## See also¶

- [`box-sizing`](https://textual.textualize.io/styles/box_sizing/) to specify how to account for the border in a widget's dimensions.
- [`outline`](https://textual.textualize.io/styles/outline/) to add an outline around the content of a widget.
- [`border-title-align`](https://textual.textualize.io/styles/border_title_align/) to set the title's alignment.
- [`border-title-color`](https://textual.textualize.io/styles/border_subtitle_color/) to set the title's color.
- [`border-title-background`](https://textual.textualize.io/styles/border_subtitle_background/) to set the title's background color.
- [`border-title-style`](https://textual.textualize.io/styles/border_subtitle_style/) to set the title's text style.
- [`border-subtitle-align`](https://textual.textualize.io/styles/border_subtitle_align/) to set the sub-title's alignment.
- [`border-subtitle-color`](https://textual.textualize.io/styles/border_subtitle_color/) to set the sub-title's color.
- [`border-subtitle-background`](https://textual.textualize.io/styles/border_subtitle_background/) to set the sub-title's background color.
- [`border-subtitle-style`](https://textual.textualize.io/styles/border_subtitle_style/) to set the sub-title's text style.