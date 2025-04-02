---
title: "Textual - Checkbox"
source: "https://textual.textualize.io/widgets/checkbox/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Checkbox¶

Added in version 0.13.0

A simple checkbox widget which stores a boolean value.

- Focusable
- Container

## Example¶

The example below shows check boxes in various states.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Checkbox

class CheckboxApp(App[None]):
    CSS_PATH = "checkbox.tcss"

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            yield Checkbox("Arrakis :sweat:")
            yield Checkbox("Caladan")
            yield Checkbox("Chusuk")
            yield Checkbox("[b]Giedi Prime[/b]")
            yield Checkbox("[magenta]Ginaz[/]")
            yield Checkbox("Grumman", True)
            yield Checkbox("Kaitain", id="initial_focus")
            yield Checkbox("Novebruns", True)

    def on_mount(self):
        self.query_one("#initial_focus", Checkbox).focus()

if __name__ == "__main__":
    CheckboxApp().run()
```

```
Screen {
    align: center middle;
}

VerticalScroll {
    width: auto;
    height: auto;
    background: $boost;
    padding: 2;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `value` | `bool` | `False` | The value of the checkbox. |

## Messages¶

## Bindings¶

The checkbox widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| enter, space | Toggle the value. |

## Component Classes¶

The checkbox widget inherits the following component classes:

| Class | Description |
| --- | --- |
| `toggle--button` | Targets the toggle button itself. |
| `toggle--label` | Targets the text label of the toggle button. |

---

Bases: `ToggleButton`

A check box widget that represents a boolean value.

## Changed [¶](https://textual.textualize.io/widgets/checkbox/#textual.widgets.Checkbox.Changed "Permanent link")

```
Changed(toggle_button, value)
```

Bases: `Changed`

Posted when the value of the checkbox changes.

This message can be handled using an `on_checkbox_changed` method.

### checkbox [¶](https://textual.textualize.io/widgets/checkbox/#textual.widgets.Checkbox.Changed.checkbox "Permanent link")

```
checkbox
```

The checkbox that was changed.

### control [¶](https://textual.textualize.io/widgets/checkbox/#textual.widgets.Checkbox.Changed.control "Permanent link")

```
control
```

An alias for .