---
title: "Textual - Outline"
source: "https://textual.textualize.io/styles/outline/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Outline¶

The `outline` style enables the drawing of a box around the content of a widget, which means the outline is drawn *over* the content area.

Note

[`border`](https://textual.textualize.io/styles/border/) and [`outline`](https://textual.textualize.io/styles/outline/) cannot coexist in the same edge of a widget.

## Syntax¶

```
outline: [<border>] [<color>];

outline-top: [<border>] [<color>];
outline-right: [<border>] [<color>];
outline-bottom: [<border>] [<color>];
outline-left: [<border>] [<color>];
```

The style `outline` accepts an optional [`<border>`](https://textual.textualize.io/css_types/border/) that sets the visual style of the widget outline and an optional [`<color>`](https://textual.textualize.io/css_types/color/) to set the color of the outline.

Unlike the style [`border`](https://textual.textualize.io/styles/border/), the frame of the outline is drawn over the content area of the widget. This rule can be useful to add temporary emphasis on the content of a widget, if you want to draw the user's attention to it.

## Border command¶

The `textual` CLI has a subcommand which will let you explore the various border types interactively, when applied to the CSS rule [`border`](https://textual.textualize.io/styles/border/):

```
textual borders
```

## Examples¶

### Basic usage¶

This example shows a widget with an outline. Note how the outline occludes the text area.

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

class OutlineApp(App):
    CSS_PATH = "outline.tcss"

    def compose(self):
        yield Label(TEXT)

if __name__ == "__main__":
    app = OutlineApp()
    app.run()
```

```
Screen {
    background: white;
    color: black;
}

Label {
    margin: 4 8;
    background: green 20%;
    outline: wide green;
    width: 100%;
}
```

### All outline types¶

The next example shows a grid with all the available outline types.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Grid
from textual.widgets import Label

class AllOutlinesApp(App):
    CSS_PATH = "outline_all.tcss"

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
            Label("none", id="none"),
            Label("outer", id="outer"),
            Label("round", id="round"),
            Label("solid", id="solid"),
            Label("tall", id="tall"),
            Label("vkey", id="vkey"),
            Label("wide", id="wide"),
        )

if __name__ == "__main__":
    app = AllOutlinesApp()
    app.run()
```

```
#ascii {
    outline: ascii $accent;
}

#blank {
    outline: blank $accent;
}

#dashed {
    outline: dashed $accent;
}

#double {
    outline: double $accent;
}

#heavy {
    outline: heavy $accent;
}

#hidden {
    outline: hidden $accent;
}

#hkey {
    outline: hkey $accent;
}

#inner {
    outline: inner $accent;
}

#none {
    outline: none $accent;
}

#outer {
    outline: outer $accent;
}

#round {
    outline: round $accent;
}

#solid {
    outline: solid $accent;
}

#tall {
    outline: tall $accent;
}

#vkey {
    outline: vkey $accent;
}

#wide {
    outline: wide $accent;
}

Grid {
    grid-size: 3 5;
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
/* Set a heavy white outline */
outline:heavy white;

/* set a red outline on the left */
outline-left:outer red;
```

## Python¶

```
# Set a heavy white outline
widget.outline = ("heavy", "white")

# Set a red outline on the left
widget.outline_left = ("outer", "red")
```

## See also¶

- [`border`](https://textual.textualize.io/styles/border/) to add a border around a widget.