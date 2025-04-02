---
title: "Textual - RadioSet"
source: "https://textual.textualize.io/widgets/radioset/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## RadioSet¶

Added in version 0.13.0

A container widget that groups [`RadioButton`](https://textual.textualize.io/widgets/radiobutton/)s together.

- Focusable
- Container

## Example¶

### Simple example¶

The example below shows two radio sets, one built using a collection of [radio buttons](https://textual.textualize.io/widgets/radiobutton/), the other a collection of simple strings.

<!-- SVG content removed by SVG Remover -->

```
from rich.text import Text

from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import RadioButton, RadioSet

class RadioChoicesApp(App[None]):
    CSS_PATH = "radio_set.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal():
            # A RadioSet built up from RadioButtons.
            with RadioSet(id="focus_me"):
                yield RadioButton("Battlestar Galactica")
                yield RadioButton("Dune 1984")
                yield RadioButton("Dune 2021")
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
            # A RadioSet built up from a collection of strings.
            yield RadioSet(
                "Amanda",
                "Connor MacLeod",
                "Duncan MacLeod",
                "Heather MacLeod",
                "Joe Dawson",
                "Kurgan, [bold italic red]The[/]",
                "Methos",
                "Rachel Ellenstein",
                "Ramírez",
            )

    def on_mount(self) -> None:
        self.query_one("#focus_me").focus()

if __name__ == "__main__":
    RadioChoicesApp().run()
```

```
Screen {
    align: center middle;
}

Horizontal {
    align: center middle;
    height: auto;
}

RadioSet {
    width: 45%;
}
```

### Reacting to Changes in a Radio Set¶

Here is an example of using the message to react to changes in a `RadioSet`:

<!-- SVG content removed by SVG Remover -->

```
from rich.text import Text

from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Label, RadioButton, RadioSet

class RadioSetChangedApp(App[None]):
    CSS_PATH = "radio_set_changed.tcss"

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            with Horizontal():
                with RadioSet(id="focus_me"):
                    yield RadioButton("Battlestar Galactica")
                    yield RadioButton("Dune 1984")
                    yield RadioButton("Dune 2021")
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
            with Horizontal():
                yield Label(id="pressed")
            with Horizontal():
                yield Label(id="index")

    def on_mount(self) -> None:
        self.query_one(RadioSet).focus()

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        self.query_one("#pressed", Label).update(
            f"Pressed button label: {event.pressed.label}"
        )
        self.query_one("#index", Label).update(
            f"Pressed button index: {event.radio_set.pressed_index}"
        )

if __name__ == "__main__":
    RadioSetChangedApp().run()
```

```
VerticalScroll {
    align: center middle;
}

Horizontal {
    align: center middle;
    height: auto;
}

RadioSet {
    width: 45%;
}
```

## Messages¶

## Bindings¶

The `RadioSet` widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| enter, space | Toggle the currently-selected button. |
| left, up | Select the previous radio button in the set. |
| right, down | Select the next radio button in the set. |

## Component Classes¶

This widget has no component classes.

## See Also¶

- [RadioButton](https://textual.textualize.io/widgets/radiobutton/)

---

Bases: `[VerticalScroll](https://textual.textualize.io/api/containers/#textual.containers.VerticalScroll " VerticalScroll (textual.containers.VerticalScroll)")`

Widget for grouping a collection of radio buttons into a set.

When a collection of [`RadioButton`](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton " RadioButton")s are grouped with this widget, they will be treated as a mutually-exclusive grouping. If one button is turned on, the previously-on button will be turned off.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `buttons` [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet\(buttons\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [RadioButton](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton " RadioButton (textual.widgets._radio_button.RadioButton)")` | The labels or [`RadioButton`](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton " RadioButton")s to group together. | `()` |
| ## `name` [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the radio set. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the radio set in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the radio set. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the radio set is disabled or not. | `False` |
|  | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | Optional tooltip. | `None` |

Note

When a `str` label is provided, a [RadioButton](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton " RadioButton") will be created from it.

## BINDINGS [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding(
        "down,right",
        "next_button",
        "Next option",
        show=False,
    ),
    Binding(
        "enter,space", "toggle_button", "Toggle", show=False
    ),
    Binding(
        "up,left",
        "previous_button",
        "Previous option",
        show=False,
    ),
]
```

| Key(s) | Description |
| --- | --- |
| enter, space | Toggle the currently-selected button. |
| left, up | Select the previous radio button in the set. |
| right, down | Select the next radio button in the set. |

## pressed\_button [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.pressed_button "Permanent link")

```
pressed_button
```

The currently-pressed [`RadioButton`](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton " RadioButton"), or `None` if none are pressed.

## pressed\_index [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.pressed_index "Permanent link")

```
pressed_index
```

The index of the currently-pressed [`RadioButton`](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton " RadioButton"), or -1 if none are pressed.

## Changed [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.Changed "Permanent link")

```
Changed(radio_set, )
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when the pressed button in the set changes.

This message can be handled using an `on_radio_set_changed` method.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `pressed` [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.Changed\(pressed\) "Permanent link") | `[RadioButton](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton " RadioButton (textual.widgets._radio_button.RadioButton)")` | The radio button that was pressed. | *required* |

### ALLOW\_SELECTOR\_MATCH [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.Changed.ALLOW_SELECTOR_MATCH "Permanent link")

```
ALLOW_SELECTOR_MATCH = {'pressed'}
```

Additional message attributes that can be used with the [`on` decorator](https://textual.textualize.io/api/logger/#textual.on " on").

### control [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.Changed.control "Permanent link")

```
control
```

A reference to the that was changed.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### index [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.Changed.index "Permanent link")

```
index = pressed_index
```

The index of the [`RadioButton`](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton " RadioButton") that was pressed to make the change.

### pressed [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.Changed.pressed "Permanent link")

```
pressed =
```

The [`RadioButton`](https://textual.textualize.io/widgets/radiobutton/#textual.widgets.RadioButton " RadioButton") that was pressed to make the change.

### radio\_set [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.Changed.radio_set "Permanent link")

```
radio_set = radio_set
```

A reference to the that was changed.

## action\_next\_button [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.action_next_button "Permanent link")

```
action_next_button()
```

Navigate to the next button in the set.

Note that this will wrap around to the start if at the end.

## action\_previous\_button [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.action_previous_button "Permanent link")

```
action_previous_button()
```

Navigate to the previous button in the set.

Note that this will wrap around to the end if at the start.

## action\_toggle\_button [¶](https://textual.textualize.io/widgets/radioset/#textual.widgets.RadioSet.action_toggle_button "Permanent link")

```
action_toggle_button()
```

Toggle the state of the currently-selected button.