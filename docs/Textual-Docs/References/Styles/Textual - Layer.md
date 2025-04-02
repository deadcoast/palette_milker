---
title: "Textual - Layer"
source: "https://textual.textualize.io/styles/layer/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Layer¶

The `layer` style defines the layer a widget belongs to.

## Syntax¶

```
layer: <name>;
```

The `layer` style accepts a [`<name>`](https://textual.textualize.io/css_types/name/) that defines the layer this widget belongs to. This [`<name>`](https://textual.textualize.io/css_types/name/) must correspond to a [`<name>`](https://textual.textualize.io/css_types/name/) that has been defined in a [`layers`](https://textual.textualize.io/styles/layers/) style by an ancestor of this widget.

More information on layers can be found in the [guide](https://textual.textualize.io/guide/layout/#layers).

Warning

Using a `<name>` that hasn't been defined in a [`layers`](https://textual.textualize.io/styles/layers/) declaration of an ancestor of this widget has no effect.

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
/* Draw the widget on the layer called 'below' */
layer: below;
```

## Python¶

```
# Draw the widget on the layer called 'below'
widget.styles.layer = "below"
```

## See also¶

- The [layout guide](https://textual.textualize.io/guide/layout/#layers) section on layers.
- [`layers`](https://textual.textualize.io/styles/layers/) to define an ordered set of layers.