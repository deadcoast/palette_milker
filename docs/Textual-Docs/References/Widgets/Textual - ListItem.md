---
title: "Textual - ListItem"
source: "https://textual.textualize.io/widgets/list_item/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## ListItem¶

Added in version 0.6.0

`ListItem` is the type of the elements in a `ListView`.

- Focusable
- Container

## Example¶

The example below shows an app with a simple `ListView`, consisting of multiple `ListItem`s. The arrow keys can be used to navigate the list.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, ListItem, ListView

class ListViewExample(App):
    CSS_PATH = "list_view.tcss"

    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("One")),
            ListItem(Label("Two")),
            ListItem(Label("Three")),
        )
        yield Footer()

if __name__ == "__main__":
    app = ListViewExample()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `highlighted` | `bool` | `False` | True if this ListItem is highlighted |

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A widget that is an item within a `ListView`.

A `ListItem` is designed for use within a [ListView](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView " ListView"), please see `ListView`'s documentation for more details on use.

## highlighted [¶](https://textual.textualize.io/widgets/list_item/#textual.widgets.ListItem.highlighted "Permanent link")

```
highlighted = reactive(False)
```

Is this item highlighted?