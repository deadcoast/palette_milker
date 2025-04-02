---
title: "Textual - Link"
source: "https://textual.textualize.io/widgets/link/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Link¶

Added in version 0.84.0

A widget to display a piece of text that opens a URL when clicked, like a web browser link.

- Focusable
- Container

## Example¶

A trivial app with a link. Clicking the link open's a web-browser—as you might expect!

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Link

class LabelApp(App):
    AUTO_FOCUS = None
    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Link(
            "Go to textualize.io",
            url="https://textualize.io",
            tooltip="Click me",
        )

if __name__ == "__main__":
    app = LabelApp()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `text` | `str` | `""` | The text of the link. |
| `url` | `str` | `""` | The URL to open when the link is clicked. |

## Messages¶

This widget sends no messages.

## Bindings¶

The Link widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| enter | Open the link in the browser. |

## Component classes¶

This widget contains no component classes.

---

Bases: `[Static](https://textual.textualize.io/widgets/static/#textual.widgets.Static " Static (textual.widgets.Static)")`

A simple, clickable link that opens a URL.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `text` [¶](https://textual.textualize.io/widgets/link/#textual.widgets.Link\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Text of the link. | *required* |
| ## `url` [¶](https://textual.textualize.io/widgets/link/#textual.widgets.Link\(url\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A URL to open, when clicked. If `None`, the `text` parameter will also be used as the url. | `None` |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional tooltip. | `None` |
| ## `name` [¶](https://textual.textualize.io/widgets/link/#textual.widgets.Link\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Name of widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/link/#textual.widgets.Link\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | ID of Widget. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/link/#textual.widgets.Link\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Space separated list of class names. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/link/#textual.widgets.Link\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the static is disabled or not. | `False` |

## BINDINGS [¶](https://textual.textualize.io/widgets/link/#textual.widgets.Link.BINDINGS "Permanent link")

```
BINDINGS = [Binding('enter', 'open_link', 'Open link')]
```

| Key(s) | Description |
| --- | --- |
| enter | Open the link in the browser. |