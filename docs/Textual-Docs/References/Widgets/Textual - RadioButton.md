---
title: "Textual - RadioButton"
source: "https://textual.textualize.io/widgets/radiobutton/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## RadioButton¶

Added in version 0.13.0

A simple radio button which stores a boolean value.

- Focusable
- Container

A radio button is best used with others inside a [`RadioSet`](https://textual.textualize.io/widgets/radioset/).

## Example¶

The example below shows radio buttons, used within a [`RadioSet`](https://textual.textualize.io/widgets/radioset/).

<!-- SVG content removed by SVG Remover -->

```
from rich.text import Text

from textual.app import App, ComposeResult
from textual.widgets import RadioButton, RadioSet

class RadioChoicesApp(App[None]):
    CSS_PATH = "radio_button.tcss"

    def compose(self) -> ComposeResult:
        with RadioSet():
            yield RadioButton("Battlestar Galactica")
            yield RadioButton("Dune 1984")
            yield RadioButton("Dune 2021", id="focus_me")
            yield RadioButton("Serenity", value=True)
            yield RadioButton("Star Trek: The Motion Picture")
            yield RadioButton("Star Wars: A New Hope")
            yield RadioButton("The Last Starfighter")
            yield RadioButton(
                Text.from_markup(
                    "Total Recall :backhand_index_pointing_right: :red_circle:"
                )
            )
            yield RadioButton("Wing Commander")

    def on_mount(self) -> None:
        self.query_one(RadioSet).focus()

if __name__ == "__main__":
    RadioChoicesApp().run()
```

```
Screen {
    align: center middle;
}

RadioSet {
    width: 50%;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `value` | `bool` | `False` | The value of the radio button. |

## Messages¶

## Bindings¶

The radio button widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| enter, space | Toggle the value. |

## Component Classes¶

The checkbox widget inherits the following component classes:

| Class | Description |
| --- | --- |
| `toggle--button` | Targets the toggle button itself. |
| `toggle--label` | Targets the text label of the toggle button. |

## See Also¶

- [RadioSet](https://textual.textualize.io/widgets/radioset/)

---

Bases: `ToggleButton`

A radio button widget that represents a boolean value.

Note

A `RadioButton` is best used within a [RadioSet](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet " RadioSet").

## BUTTON\_INNER [¶](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton.BUTTON_INNER "Permanent link")

```
BUTTON_INNER = '●'
```

The character used for the inside of the button.

## Changed [¶](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton.Changed "Permanent link")

```
Changed(toggle_button, value)
```

Bases: `Changed`

Posted when the value of the radio button changes.

This message can be handled using an `on_radio_button_changed` method.

### control [¶](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton.Changed.control "Permanent link")

```
control
```

Alias for .

### radio\_button [¶](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton.Changed.radio_button "Permanent link")

```
radio_button
```

The radio button that was changed.