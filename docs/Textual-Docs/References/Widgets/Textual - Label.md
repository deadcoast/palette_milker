---
title: "Textual - Label"
source: "https://textual.textualize.io/widgets/label/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Label¶

Added in version 0.5.0

A widget which displays static text, but which can also contain more complex Rich renderables.

- Focusable
- Container

## Example¶

The example below shows how you can use a `Label` widget to display some text.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Label

class LabelApp(App):
    def compose(self) -> ComposeResult:
        yield Label("Hello, world!")

if __name__ == "__main__":
    app = LabelApp()
    app.run()
```

## Reactive Attributes¶

This widget has no reactive attributes.

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[Static](https://textual.textualize.io/widgets/static/#textual.widgets.Static " Static (textual.widgets._static.Static)")`

A simple label widget for displaying text-oriented renderables.