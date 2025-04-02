---
title: "Textual - Layers"
source: "https://textual.textualize.io/styles/layers/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Layers¶

The `layers` style allows you to define an ordered set of layers.

## Syntax¶

```
layers: <name>+;
```

The `layers` style accepts one or more [`<name>`](https://textual.textualize.io/css_types/name/) that define the layers that the widget is aware of, and the order in which they will be painted on the screen.

The values used here can later be referenced using the [`layer`](https://textual.textualize.io/styles/layer/) property. The layers defined first in the list are drawn under the layers that are defined later in the list.

More information on layers can be found in the [guide](https://textual.textualize.io/guide/layout/#layers).

## Example¶

In the example below, `#box1` is yielded before `#box2`. However, since `#box1` is on the higher layer, it is drawn on top of `#box2`.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Static

class LayersExample(App):
    CSS_PATH = "layers.tcss"

    def compose(self) -> ComposeResult:
        yield Static("box1 (layer = above)", id="box1")
        yield Static("box2 (layer = below)", id="box2")

if __name__ == "__main__":
    app = LayersExample()
    app.run()
```

```
Screen {
    align: center middle;
    layers: below above;
}

Static {
    width: 28;
    height: 8;
    color: auto;
    content-align: center middle;
}

#box1 {
    layer: above;
    background: darkcyan;
}

#box2 {
    layer: below;
    background: orange;
    offset: 12 6;
}
```

## CSS¶

```
/* Bottom layer is called 'below', layer above it is called 'above' */
layers: below above;
```

## Python¶

```
# Bottom layer is called 'below', layer above it is called 'above'
widget.style.layers = ("below", "above")
```

## See also¶

- The [layout guide](https://textual.textualize.io/guide/layout/#layers) section on layers.
- [`layer`](https://textual.textualize.io/styles/layer/) to set the layer a widget belongs to.