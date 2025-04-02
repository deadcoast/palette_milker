---
title: "Textual - Footer"
source: "https://textual.textualize.io/widgets/footer/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
Added in version 0.63.0

A simple footer widget which is docked to the bottom of its parent container. Displays available keybindings for the currently focused widget.

- Focusable
- Container

## Example¶

The example below shows an app with a single keybinding that contains only a `Footer` widget. Notice how the `Footer` automatically displays the keybinding.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer

class FooterApp(App):
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        ),
        Binding(key="delete", action="delete", description="Delete the thing"),
        Binding(key="j", action="down", description="Scroll down", show=False),
    ]

    def compose(self) -> ComposeResult:
        yield Footer()

if __name__ == "__main__":
    app = FooterApp()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `compact` | `bool` | `False` | Display a more compact footer. |
| `show_command_palette` | `bool` | `True` | Display the key to invoke the command palette (show on the right hand side of the footer). |

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

## Additional Notes¶

- You can prevent keybindings from appearing in the footer by setting the `show` argument of the `Binding` to `False`.
- You can customize the text that appears for the key itself in the footer using the `key_display` argument of `Binding`.

---

Bases: `[ScrollableContainer](https://textual.textualize.io/api/containers/#textual.containers.ScrollableContainer " ScrollableContainer (textual.containers.ScrollableContainer)")`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | Child widgets. | `()` |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the widget. | `None` |
|  | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |
|  | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Show key binding to invoke the command palette, on the right of the footer. | `True` |

```
compact = reactive(False)
```

Display in compact style.

```
show_command_palette = reactive(True)
```

Show the key to invoke the command palette.