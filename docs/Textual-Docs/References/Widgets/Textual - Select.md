---
title: "Textual - Select"
source: "https://textual.textualize.io/widgets/select/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Select¶

Added in version 0.24.0

A Select widget is a compact control to allow the user to select between a number of possible options.

- Focusable
- Container

The options in a select control may be passed into the constructor or set later with . Options should be given as a sequence of tuples consisting of two values: the first is the string (or [Rich Renderable](https://rich.readthedocs.io/en/latest/protocol.html)) to display in the control and list of options, the second is the value of option.

The value of the currently selected option is stored in the `value` attribute of the widget, and the `value` attribute of the message.

## Typing¶

The `Select` control is a typing Generic which allows you to set the type of the option values. For instance, if the data type for your values is an integer, you would type the widget as follows:

```
options = [("First", 1), ("Second", 2)]
my_select: Select[int] =  Select(options)
```

Note

Typing is entirely optional.

If you aren't familiar with typing or don't want to worry about it right now, feel free to ignore it.

## Examples¶

### Basic Example¶

The following example presents a `Select` with a number of options.

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

```
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Select

LINES = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.""".splitlines()

class SelectApp(App):
    CSS_PATH = "select.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Select((line, line) for line in LINES)

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.title = str(event.value)

if __name__ == "__main__":
    app = SelectApp()
    app.run()
```

```
Screen {
    align: center top;
}

Select {
    width: 60;
    margin: 2;
}
```

### Example using Class Method¶

The following example presents a `Select` created using the `from_values` class method.

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

```
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Select

LINES = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.""".splitlines()

class SelectApp(App):
    CSS_PATH = "select.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Select.from_values(LINES)

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.title = str(event.value)

if __name__ == "__main__":
    app = SelectApp()
    app.run()
```

```
Screen {
    align: center top;
}

Select {
    width: 60;
    margin: 2;
}
```

## Blank state¶

The `Select` widget has an option `allow_blank` for its constructor. If set to `True`, the widget may be in a state where there is no selection, in which case its value will be the special constant . The auxiliary methods and provide a convenient way to check if the widget is in this state and to set this state, respectively.

## Type to search¶

The `Select` widget has a `type_to_search` attribute which allows you to type to move the cursor to a matching option when the widget is expanded. To disable this behavior, set the attribute to `False`.

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `expanded` | `bool` | `False` | True to expand the options overlay. |
| `value` | `SelectType` \| `_NoSelection` |  | Current value of the Select. |

## Messages¶

## Bindings¶

The Select widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| enter,down,space,up | Activate the overlay |

## Component Classes¶

This widget has no component classes.

---

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[[SelectType](https://textual.textualize.io/api/types/#textual.types.SelectType " SelectType (textual.widgets._select.SelectType)")]`, `[Vertical](https://textual.textualize.io/api/containers/#textual.containers.Vertical " Vertical (textual.containers.Vertical)")`

Widget to select from a list of possible options.

A Select displays the current selection. When activated with Enter the widget displays an overlay with a list of all possible options.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `options` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select\(options\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType"), [SelectType](https://textual.textualize.io/api/types/#textual.types.SelectType " SelectType (textual.widgets._select.SelectType)")]]` | Options to select from. If no options are provided then `allow_blank` must be set to `True`. | *required* |
| ## `prompt` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select\(prompt\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Text to show in the control when no option is selected. | `'Select'` |
| ## `allow_blank` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select\(allow_blank\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enables or disables the ability to have the widget in a state with no selection made, in which case its value is set to the constant . | `True` |
| ## `value` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select\(value\) "Permanent link") | `[SelectType](https://textual.textualize.io/api/types/#textual.types.SelectType " SelectType (textual.widgets._select.SelectType)") \| [NoSelection](https://textual.textualize.io/api/types/#textual.types.NoSelection " NoSelection (textual.widgets._select.NoSelection)")` | Initial value selected. Should be one of the values in `options`. If no initial value is set and `allow_blank` is `False`, the widget will auto-select the first available option. |  |
| ## `type_to_search` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select\(type_to_search\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `True`, typing will search for options. | `True` |
| ## `name` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the select control. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the control in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the control. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the control is disabled or not. | `False` |
|  | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | Optional tooltip. | `None` |

Raises:

| Type | Description |
| --- | --- |
|  | If no options are provided and `allow_blank` is `False`. |

## BINDINGS [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding(
        "enter,down,space,up",
        "show_overlay",
        "Show menu",
        show=False,
    )
]
```

| Key(s) | Description |
| --- | --- |
| enter,down,space,up | Activate the overlay |

## BLANK [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.BLANK "Permanent link")

```
BLANK =
```

Constant to flag that the widget has no selection.

## expanded [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.expanded "Permanent link")

```
expanded = var(False, init=False)
```

True to show the overlay, otherwise False.

## prompt [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.prompt "Permanent link")

```
prompt =
```

The prompt to show when no value is selected.

## selection [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.selection "Permanent link")

```
selection
```

The currently selected item.

Unlike , this will not return Blanks. If nothing is selected, this will return `None`.

## value [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.value "Permanent link")

```
value = var[Union[SelectType, NoSelection]](
    , init=False
)
```

The value of the selection.

If the widget has no selection, its value will be . Setting this to an illegal value will raise a exception.

## Changed [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.Changed "Permanent link")

```
Changed(select, value)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when the select value was changed.

This message can be handled using a `on_select_changed` method.

### control [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.Changed.control "Permanent link")

```
control
```

The Select that sent the message.

### select [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.Changed.select "Permanent link")

```
select = select
```

The select widget.

### value [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.Changed.value "Permanent link")

```
value = value
```

The value of the Select when it changed.

```
action_show_overlay()
```

Show the overlay.

## clear [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.clear "Permanent link")

```
clear()
```

Clear the selection if `allow_blank` is `True`.

Raises:

| Type | Description |
| --- | --- |
|  | If `allow_blank` is set to `False`. |

## from\_values [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values "Permanent link")

```
from_values(
    ,
    *,
    ="Select",
    =True,
    =,
    =True,
    =None,
    =None,
    =None,
    =False
)
```

Initialize the Select control with values specified by an arbitrary iterable

The options shown in the control are computed by calling the built-in `str` on each value.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `values` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values\(values\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[SelectType](https://textual.textualize.io/api/types/#textual.types.SelectType " SelectType (textual.widgets._select.SelectType)")]` | Values used to generate options to select from. | *required* |
| ### `prompt` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values\(prompt\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Text to show in the control when no option is selected. | `'Select'` |
| ### `allow_blank` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values\(allow_blank\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enables or disables the ability to have the widget in a state with no selection made, in which case its value is set to the constant . | `True` |
| ### `value` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values\(value\) "Permanent link") | `[SelectType](https://textual.textualize.io/api/types/#textual.types.SelectType " SelectType (textual.widgets._select.SelectType)") \| [NoSelection](https://textual.textualize.io/api/types/#textual.types.NoSelection " NoSelection (textual.widgets._select.NoSelection)")` | Initial value selected. Should be one of the values in `values`. If no initial value is set and `allow_blank` is `False`, the widget will auto-select the first available value. |  |
| ### `type_to_search` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values\(type_to_search\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `True`, typing will search for options. | `True` |
| ### `name` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the select control. | `None` |
| ### `id` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the control in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the control. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.from_values\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the control is disabled or not. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[[SelectType](https://textual.textualize.io/api/types/#textual.types.SelectType " SelectType (textual.widgets._select.SelectType)")]` | A new Select widget with the provided values as options. |

## is\_blank [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.is_blank "Permanent link")

```
is_blank()
```

Indicates whether this `Select` is blank or not.

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the selection is blank, False otherwise. |

## set\_options [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.set_options "Permanent link")

```
set_options()
```

Set the options for the Select.

This will reset the selection. The selection will be empty, if allowed, otherwise the first valid option is picked.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `options` [¶](https://textual.textualize.io/widgets/select/#textual.widgets.Select.set_options\(options\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType"), [SelectType](https://textual.textualize.io/api/types/#textual.types.SelectType " SelectType (textual.widgets._select.SelectType)")]]` | An iterable of tuples containing the renderable to display for each option and the corresponding internal value. | *required* |

Raises:

| Type | Description |
| --- | --- |
|  | If the options iterable is empty and `allow_blank` is `False`. |

## EmptySelectError [¶](https://textual.textualize.io/widgets/select/#textual.widgets.select.EmptySelectError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when a has no options and `allow_blank=False`.

## InvalidSelectValueError [¶](https://textual.textualize.io/widgets/select/#textual.widgets.select.InvalidSelectValueError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when setting a to an unknown option.