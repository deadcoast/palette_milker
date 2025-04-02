---
title: "Textual - Render and compose"
source: "https://textual.textualize.io/how-to/render-and-compose/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Render and compose¶

A common question that comes up on the [Textual Discord server](https://discord.gg/Enf6Z3qhVr) is what is the difference between [`render`](https://textual.textualize.io/api/widget/#textual.widget.Widget.render " render") and [`compose`](https://textual.textualize.io/api/widget/#textual.widget.Widget.compose " compose") methods on a widget? In this article we will clarify the differences, and use both these methods to build something fun.

![](https://www.youtube.com/watch?v=dYU7jHyabX8)

## Which method to use?¶

Render and compose are easy to confuse because they both ultimately define what a widget will look like, but they have quite different uses.

The `render` method on a widget returns a [Rich](https://rich.readthedocs.io/en/latest/) renderable, which is anything you could print with Rich. The simplest renderable is just text; so `render()` methods often return a string, but could equally return a [`Text`](https://rich.readthedocs.io/en/latest/text.html) instance, a [`Table`](https://rich.readthedocs.io/en/latest/tables.html), or anything else from Rich (or third party library). Whatever is returned from `render()` will be combined with any styles from CSS and displayed within the widget's borders.

The `compose` method is used to build [*compound* widgets](https://textual.textualize.io/guide/widgets/#compound-widgets) (widgets composed of other widgets).

A general rule of thumb, is that if you implement a `compose` method, there is no need for a `render` method because it is the widgets yielded from `compose` which define how the custom widget will look. However, you *can* mix these two methods. If you implement both, the `render` method will set the custom widget's *background* and `compose` will add widgets on top of that background.

## Combining render and compose¶

Let's look at an example that combines both these methods. We will create a custom widget with a [linear gradient](https://textual.textualize.io/api/renderables/#textual.renderables.gradient.LinearGradient " LinearGradient") as a background. The background will be animated (I did promise *fun*)!

```
from time import time

from textual.app import App, ComposeResult, RenderResult
from textual.containers import Container
from textual.renderables.gradient import LinearGradient
from textual.widgets import Static

COLORS = [
    "#881177",
    "#aa3355",
    "#cc6666",
    "#ee9944",
    "#eedd00",
    "#99dd55",
    "#44dd88",
    "#22ccbb",
    "#00bbcc",
    "#0099cc",
    "#3366bb",
    "#663399",
]
STOPS = [(i / (len(COLORS) - 1), color) for i, color in enumerate(COLORS)]

class Splash(Container):
    """Custom widget that extends Container."""

    DEFAULT_CSS = """
    Splash {
        align: center middle;
    }
    Static {
        width: 40;
        padding: 2 4;
    }
    """

    def on_mount(self) -> None:
        self.auto_refresh = 1 / 30  

    def compose(self) -> ComposeResult:
        yield Static("Making a splash with Textual!")  

    def render(self) -> RenderResult:
        return LinearGradient(time() * 90, STOPS)  

class SplashApp(App):
    """Simple app to show our custom widget."""

    def compose(self) -> ComposeResult:
        yield Splash()

if __name__ == "__main__":
    app = SplashApp()
    app.run()
```

<!-- SVG content removed by SVG Remover -->

The `Splash` custom widget has a `compose` method which adds a simple `Static` widget to display a message. Additionally there is a `render` method which returns a renderable to fill the background with a gradient.

Tip

As fun as this is, spinning animated gradients may be too distracting for most apps!

## Summary¶

Keep the following in mind when building [custom widgets](https://textual.textualize.io/guide/widgets/).

1. Use `render` to return simple text, or a Rich renderable.
2. Use `compose` to create a widget out of other widgets.
3. If you define both, then `render` will be used as a *background*.

---

We are here to [help](https://textual.textualize.io/help/)!