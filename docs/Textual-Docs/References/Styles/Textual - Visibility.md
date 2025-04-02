---
title: "Textual - Visibility"
source: "https://textual.textualize.io/styles/visibility/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Visibility¶

The `visibility` style determines whether a widget is visible or not.

## Syntax¶

```
visibility: hidden | visible;
```

`visibility` takes one of two values to set the visibility of a widget.

### Values¶

| Value | Description |
| --- | --- |
| `hidden` | The widget will be invisible. |
| `visible` (default) | The widget will be displayed as normal. |

### Visibility inheritance¶

Note

Children of an invisible container *can* be visible.

By default, children inherit the visibility of their parents. So, if a container is set to be invisible, its children widgets will also be invisible by default. However, those widgets can be made visible if their visibility is explicitly set to `visibility: visible`. This is shown in the second example below.

## Examples¶

### Basic usage¶

Note that the second widget is hidden while leaving a space where it would have been rendered.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.widgets import Label

class VisibilityApp(App):
    CSS_PATH = "visibility.tcss"

    def compose(self):
        yield Label("Widget 1")
        yield Label("Widget 2", classes="invisible")
        yield Label("Widget 3")

if __name__ == "__main__":
    app = VisibilityApp()
    app.run()
```

```
Screen {
    background: green;
}

Label {
    height: 5;
    width: 100%;
    background: white;
    color: blue;
    border: heavy blue;
}

Label.invisible {
    visibility: hidden;
}
```

### Overriding container visibility¶

The next example shows the interaction of the `visibility` style with invisible containers that have visible children. The app below has three rows with a `Horizontal` container per row and three placeholders per row. The containers all have a white background, and then:

- the top container is visible by default (we can see the white background around the placeholders);
- the middle container is invisible and the children placeholders inherited that setting;
- the bottom container is invisible *but* the children placeholders are visible because they were set to be visible.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Placeholder

class VisibilityContainersApp(App):
    CSS_PATH = "visibility_containers.tcss"

    def compose(self):
        yield VerticalScroll(
            Horizontal(
                Placeholder(),
                Placeholder(),
                Placeholder(),
                id="top",
            ),
            Horizontal(
                Placeholder(),
                Placeholder(),
                Placeholder(),
                id="middle",
            ),
            Horizontal(
                Placeholder(),
                Placeholder(),
                Placeholder(),
                id="bot",
            ),
        )

if __name__ == "__main__":
    app = VisibilityContainersApp()
    app.run()
```

```
Horizontal {
    padding: 1 2;     
    background: white;
    height: 1fr;
}

#top {}               

#middle {             
    visibility: hidden;
}

#bot {                
    visibility: hidden;
}

#bot > Placeholder {  
    visibility: visible;
}

Placeholder {
    width: 1fr;
}
```

1. The padding and the white background let us know when the `Horizontal` is visible.
2. The top `Horizontal` is visible by default, and so are its children.
3. The middle `Horizontal` is made invisible and its children will inherit that setting.
4. The bottom `Horizontal` is made invisible...
5. ... but its children override that setting and become visible.

## CSS¶

```
/* Widget is invisible */
visibility: hidden;

/* Widget is visible */
visibility: visible;
```

## Python¶

```
# Widget is invisible
self.styles.visibility = "hidden"

# Widget is visible
self.styles.visibility = "visible"
```

There is also a shortcut to set a Widget's visibility. The `visible` property on `Widget` may be set to `True` or `False`.

```
# Make a widget invisible
widget.visible = False

# Make the widget visible again
widget.visible = True
```

## See also¶

- [`display`](https://textual.textualize.io/styles/display/) to specify whether a widget is displayed or not.