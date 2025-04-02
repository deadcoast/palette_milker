---
title: "Textual - Button"
source: "https://textual.textualize.io/widgets/button/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Button¶

A simple button widget which can be pressed using a mouse click or by pressing Enter when it has focus.

- Focusable
- Container

## Example¶

The example below shows each button variant, and its disabled equivalent. Clicking any of the non-disabled buttons in the example app below will result in the app exiting and the details of the selected button being printed to the console.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, Static

class ButtonsApp(App[str]):
    CSS_PATH = "button.tcss"

    def compose(self) -> ComposeResult:
        yield Horizontal(
            VerticalScroll(
                Static("Standard Buttons", classes="header"),
                Button("Default"),
                Button("Primary!", variant="primary"),
                Button.success("Success!"),
                Button.warning("Warning!"),
                Button.error("Error!"),
            ),
            VerticalScroll(
                Static("Disabled Buttons", classes="header"),
                Button("Default", disabled=True),
                Button("Primary!", variant="primary", disabled=True),
                Button.success("Success!", disabled=True),
                Button.warning("Warning!", disabled=True),
                Button.error("Error!", disabled=True),
            ),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(str(event.button))

if __name__ == "__main__":
    app = ButtonsApp()
    print(app.run())
```

```
Button {
    margin: 1 2;
}

Horizontal > VerticalScroll {
    width: 24;
}

.header {
    margin: 1 0 0 2;
    text-style: bold;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `label` | `str` | `""` | The text that appears inside the button. |
| `variant` | `ButtonVariant` | `"default"` | Semantic styling variant. One of `default`, `primary`, `success`, `warning`, `error`. |
| `disabled` | `bool` | `False` | Whether the button is disabled or not. Disabled buttons cannot be focused or clicked, and are styled in a way that suggests this. |

## Messages¶

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

## Additional Notes¶

- The spacing between the text and the edges of a button are *not* due to padding. The default styling for a `Button` includes borders and a `min-width` of 16 columns. To remove the spacing, set `border: none;` in your CSS and adjust the minimum width as needed.

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A simple clickable button.

Clicking the button will send a message, unless the `action` parameter is provided.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `label` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button\(label\) "Permanent link") | `[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)") \| None` | The text that appears within the button. | `None` |
| ## `variant` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button\(variant\) "Permanent link") |  | The variant of the button. | `'default'` |
| ## `name` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the button. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the button in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the button. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the button is disabled or not. | `False` |
|  | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | Optional tooltip. | `None` |
| ## `action` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button\(action\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional action to run when clicked. | `None` |

## active\_effect\_duration [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.active_effect_duration "Permanent link")

```
active_effect_duration = 0.2
```

Amount of time in seconds the button 'press' animation lasts.

## label [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.label "Permanent link")

```
label = from_text()
```

The text label that appears within the button.

## variant [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.variant "Permanent link")

```
variant =
```

The variant name for the button.

## Pressed [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.Pressed "Permanent link")

```
Pressed(button)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Event sent when a `Button` is pressed and there is no Button action.

Can be handled using `on_button_pressed` in a subclass of or in a parent widget in the DOM.

### button [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.Pressed.button "Permanent link")

```
button = button
```

The button that was pressed.

### control [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.Pressed.control "Permanent link")

```
control
```

An alias for .

This will be the same value as .

## action\_press [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.action_press "Permanent link")

```
action_press()
```

Activate a press of the button.

## error [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.error "Permanent link")

```
error(
    =None,
    *,
    =None,
    =None,
    =None,
    =False
)
```

Utility constructor for creating an error Button variant.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `label` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.error\(label\) "Permanent link") | `[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)") \| None` | The text that appears within the button. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.error\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the button is disabled or not. | `False` |
| ### `name` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.error\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the button. | `None` |
| ### `id` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.error\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the button in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.error\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the button. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.error\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the button is disabled or not. | `False` |

Returns:

| Type | Description |
| --- | --- |
|  | A widget of the 'error' . |

## press [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.press "Permanent link")

```
press()
```

Animate the button and send the message.

Can be used to simulate the button being pressed by a user.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The button instance. |

## success [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.success "Permanent link")

```
success(
    =None,
    *,
    =None,
    =None,
    =None,
    =False
)
```

Utility constructor for creating a success Button variant.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `label` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.success\(label\) "Permanent link") | `[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)") \| None` | The text that appears within the button. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.success\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the button is disabled or not. | `False` |
| ### `name` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.success\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the button. | `None` |
| ### `id` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.success\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the button in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.success\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the button. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.success\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the button is disabled or not. | `False` |

Returns:

| Type | Description |
| --- | --- |
|  | A widget of the 'success' . |

## validate\_label [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.validate_label "Permanent link")

```
validate_label(label)
```

Parse markup for self.label

## warning [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.warning "Permanent link")

```
warning(
    =None,
    *,
    =None,
    =None,
    =None,
    =False
)
```

Utility constructor for creating a warning Button variant.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `label` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.warning\(label\) "Permanent link") | `[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)") \| None` | The text that appears within the button. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.warning\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the button is disabled or not. | `False` |
| ### `name` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.warning\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the button. | `None` |
| ### `id` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.warning\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the button in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.warning\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the button. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/button/#textual.widgets.Button.warning\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the button is disabled or not. | `False` |

Returns:

| Type | Description |
| --- | --- |
|  | A widget of the 'warning' . |

## textual.widgets.button [¶](https://textual.textualize.io/widgets/button/#textual.widgets.button "Permanent link")

### ButtonVariant [¶](https://textual.textualize.io/widgets/button/#textual.widgets.button.ButtonVariant "Permanent link")

```
ButtonVariant = Literal[
    "default", "primary", "success", "warning", "error"
]
```

The names of the valid button variants.

These are the variants that can be used with a .