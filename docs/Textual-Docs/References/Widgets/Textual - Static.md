---
title: "Textual - Static"
source: "https://textual.textualize.io/widgets/static/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Static¶

A widget which displays static content. Can be used for Rich renderables and can also be the base for other types of widgets.

- Focusable
- Container

## Example¶

The example below shows how you can use a `Static` widget as a simple text label (but see [Label](https://textual.textualize.io/widgets/label/) as a way of displaying text).

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Static

class StaticApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Hello, world!")

if __name__ == "__main__":
    app = StaticApp()
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

## See Also¶

- [Label](https://textual.textualize.io/widgets/label/)
- [Pretty](https://textual.textualize.io/widgets/pretty/)

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A widget to display simple static content, or use as a base class for more complex widgets.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `content` [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static\(content\) "Permanent link") | `VisualType` | A Content object, Rich renderable, or string containing console markup. | `''` |
| ## `expand` [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static\(expand\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Expand content if required to fill container. | `False` |
| ## `shrink` [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static\(shrink\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Shrink content if required to fill container. | `False` |
| ## `markup` [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static\(markup\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if markup should be parsed and rendered. | `True` |
| ## `name` [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Name of widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | ID of Widget. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Space separated list of class names. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the static is disabled or not. | `False` |

## update [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static.update "Permanent link")

```
update(='')
```

Update the widget's content area with new text or Rich renderable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `content` [¶](https://textual.textualize.io/widgets/static/#textual.widgets.Static.update\(content\) "Permanent link") | `VisualType` | New content. | `''` |