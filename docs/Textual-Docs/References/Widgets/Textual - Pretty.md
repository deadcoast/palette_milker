---
title: "Textual - Pretty"
source: "https://textual.textualize.io/widgets/pretty/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Pretty¶

Display a pretty-formatted object.

- Focusable
- Container

## Example¶

The example below shows a pretty-formatted `dict`, but `Pretty` can display any Python object.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Pretty

DATA = {
    "title": "Back to the Future",
    "releaseYear": 1985,
    "director": "Robert Zemeckis",
    "genre": "Adventure, Comedy, Sci-Fi",
    "cast": [
        {"actor": "Michael J. Fox", "character": "Marty McFly"},
        {"actor": "Christopher Lloyd", "character": "Dr. Emmett Brown"},
    ],
}

class PrettyExample(App):
    def compose(self) -> ComposeResult:
        yield Pretty(DATA)

app = PrettyExample()

if __name__ == "__main__":
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

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A pretty-printing widget.

Used to pretty-print any object.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `object` [¶](https://textual.textualize.io/widgets/pretty/#textual.widgets.Pretty\(object\) "Permanent link") | `[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | The object to pretty-print. | *required* |
| ## `name` [¶](https://textual.textualize.io/widgets/pretty/#textual.widgets.Pretty\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the pretty widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/pretty/#textual.widgets.Pretty\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the pretty in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/pretty/#textual.widgets.Pretty\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the pretty. | `None` |

## update [¶](https://textual.textualize.io/widgets/pretty/#textual.widgets.Pretty.update "Permanent link")

```
update()
```

Update the content of the pretty widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `object` [¶](https://textual.textualize.io/widgets/pretty/#textual.widgets.Pretty.update\(object\) "Permanent link") | `[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | The object to pretty-print. | *required* |