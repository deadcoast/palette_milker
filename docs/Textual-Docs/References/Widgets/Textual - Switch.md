---
title: "Textual - Switch"
source: "https://textual.textualize.io/widgets/switch/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Switch¶

A simple switch widget which stores a boolean value.

- Focusable
- Container

## Example¶

The example below shows switches in various states.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static, Switch

class SwitchApp(App):
    def compose(self) -> ComposeResult:
        yield Static("[b]Example switches\n", classes="label")
        yield Horizontal(
            Static("off:     ", classes="label"),
            Switch(animate=False),
            classes="container",
        )
        yield Horizontal(
            Static("on:      ", classes="label"),
            Switch(value=True),
            classes="container",
        )

        focused_switch = Switch()
        focused_switch.focus()
        yield Horizontal(
            Static("focused: ", classes="label"), focused_switch, classes="container"
        )

        yield Horizontal(
            Static("custom:  ", classes="label"),
            Switch(id="custom-design"),
            classes="container",
        )

app = SwitchApp(css_path="switch.tcss")
if __name__ == "__main__":
    app.run()
```

```
Screen {
    align: center middle;
}

.container {
    height: auto;
    width: auto;
}

Switch {
    height: auto;
    width: auto;
}

.label {
    height: 3;
    content-align: center middle;
    width: auto;
}

#custom-design {
    background: darkslategrey;
}

#custom-design > .switch--slider {
    color: dodgerblue;
    background: darkslateblue;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `value` | `bool` | `False` | The value of the switch. |

## Messages¶

## Bindings¶

The switch widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| enter,space | Toggle the switch state. |

## Component Classes¶

The switch widget provides the following component classes:

| Class | Description |
| --- | --- |
| `switch--slider` | Targets the slider of the switch. |

## Additional Notes¶

- To remove the spacing around a `Switch`, set `border: none;` and `padding: 0;`.

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A switch widget that represents a boolean value.

Can be toggled by clicking on it or through its .

The switch widget also contains that enable more customization.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `value` [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch\(value\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | The initial value of the switch. | `False` |
| ## `animate` [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the switch should animate when toggled. | `True` |
| ## `name` [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the switch. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the switch in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the switch. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the switch is disabled or not. | `False` |
|  | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | Optional tooltip. | `None` |

## BINDINGS [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding(
        "enter,space", "toggle_switch", "Toggle", show=False
    )
]
```

| Key(s) | Description |
| --- | --- |
| enter,space | Toggle the switch state. |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {'switch--slider'}
```

| Class | Description |
| --- | --- |
| `switch--slider` | Targets the slider of the switch. |

## value [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch.value "Permanent link")

```
value = reactive(False, init=False)
```

The value of the switch; `True` for on and `False` for off.

## Changed [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch.Changed "Permanent link")

```
Changed(switch, value)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when the status of the switch changes.

Can be handled using `on_switch_changed` in a subclass of `Switch` or in a parent widget in the DOM.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
| `value` | `[bool](https://docs.python.org/3/library/functions.html#bool)` | The value that the switch was changed to. |
| `switch` |  | The `Switch` widget that was changed. |

### control [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch.Changed.control "Permanent link")

```
control
```

Alias for self.switch.

## action\_toggle\_switch [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch.action_toggle_switch "Permanent link")

```
action_toggle_switch()
```

Toggle the state of the switch.

## toggle [¶](https://textual.textualize.io/widgets/switch/#textual.widgets.Switch.toggle "Permanent link")

```
toggle()
```

Toggle the switch value.

As a result of the value changing, a `Switch.Changed` message will be posted.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Switch` instance. |