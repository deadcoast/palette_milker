---
title: "Textual - Placeholder"
source: "https://textual.textualize.io/widgets/placeholder/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Placeholder¶

Added in version 0.6.0

A widget that is meant to have no complex functionality. Use the placeholder widget when studying the layout of your app before having to develop your custom widgets.

The placeholder widget has variants that display different bits of useful information. Clicking a placeholder will cycle through its variants.

- Focusable
- Container

## Example¶

The example below shows each placeholder variant.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Placeholder

class PlaceholderApp(App):
    CSS_PATH = "placeholder.tcss"

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            Container(
                Placeholder("This is a custom label for p1.", id="p1"),
                Placeholder("Placeholder p2 here!", id="p2"),
                Placeholder(id="p3"),
                Placeholder(id="p4"),
                Placeholder(id="p5"),
                Placeholder(),
                Horizontal(
                    Placeholder(variant="size", id="col1"),
                    Placeholder(variant="text", id="col2"),
                    Placeholder(variant="size", id="col3"),
                    id="c1",
                ),
                id="bot",
            ),
            Container(
                Placeholder(variant="text", id="left"),
                Placeholder(variant="size", id="topright"),
                Placeholder(variant="text", id="botright"),
                id="top",
            ),
            id="content",
        )

if __name__ == "__main__":
    app = PlaceholderApp()
    app.run()
```

```
Placeholder {
    height: 100%;
}

#top {
    height: 50%;
    width: 100%;
    layout: grid;
    grid-size: 2 2;
}

#left {
    row-span: 2;
}

#bot {
    height: 50%;
    width: 100%;
    layout: grid;
    grid-size: 8 8;
}

#c1 {
    row-span: 4;
    column-span: 8;
    height: 100%;
}

#col1, #col2, #col3 {
    width: 1fr;
}

#p1 {
    row-span: 4;
    column-span: 4;
}

#p2 {
    row-span: 2;
    column-span: 4;
}

#p3 {
    row-span: 2;
    column-span: 2;
}

#p4 {
    row-span: 1;
    column-span: 2;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `variant` | `str` | `"default"` | Styling variant. One of `default`, `size`, `text`. |

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A simple placeholder widget to use before you build your custom widgets.

This placeholder has a couple of variants that show different data. Clicking the placeholder cycles through the available variants, but a placeholder can also be initialised in a specific variant.

The variants available are:

| Variant | Placeholder shows |
| --- | --- |
| default | Identifier label or the ID of the placeholder. |
| size | Size of the placeholder. |
| text | Lorem Ipsum text. |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `label` [¶](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder\(label\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The label to identify the placeholder. If no label is present, uses the placeholder ID instead. | `None` |
| ## `variant` [¶](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder\(variant\) "Permanent link") | `[PlaceholderVariant](https://textual.textualize.io/api/types/#textual.types.PlaceholderVariant " PlaceholderVariant (textual.widgets._placeholder.PlaceholderVariant)")` | The variant of the placeholder. | `'default'` |
| ## `name` [¶](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the placeholder. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the placeholder in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A space separated string with the CSS classes of the placeholder, if any. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the placeholder is disabled or not. | `False` |

## variant [¶](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder.variant "Permanent link")

```
variant = validate_variant()
```

The current variant of the placeholder.

## cycle\_variant [¶](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder.cycle_variant "Permanent link")

```
cycle_variant()
```

Get the next variant in the cycle.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Placeholder` instance. |

## validate\_variant [¶](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder.validate_variant "Permanent link")

```
validate_variant(variant)
```

Validate the variant to which the placeholder was set.