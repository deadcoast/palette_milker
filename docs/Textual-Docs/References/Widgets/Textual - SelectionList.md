---
title: "Textual - SelectionList"
source: "https://textual.textualize.io/widgets/selection_list/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## SelectionList¶

Added in version 0.27.0

A widget for showing a vertical list of selectable options.

- Focusable
- Container

## Typing¶

The `SelectionList` control is a [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic), which allows you to set the type of the . For instance, if the data type for your values is an integer, you would type the widget as follows:

```
selections = [("First", 1), ("Second", 2)]
my_selection_list: SelectionList[int] =  SelectionList(*selections)
```

Note

Typing is entirely optional.

If you aren't familiar with typing or don't want to worry about it right now, feel free to ignore it.

## Examples¶

A selection list is designed to be built up of single-line prompts (which can be [Rich `Text`](https://rich.readthedocs.io/en/stable/text.html)) and an associated unique value.

### Selections as tuples¶

A selection list can be built with tuples, either of two or three values in length. Each tuple must contain a prompt and a value, and it can also optionally contain a flag for the initial selected state of the option.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, SelectionList

class SelectionListApp(App[None]):
    CSS_PATH = "selection_list.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield SelectionList[int](  
            ("Falken's Maze", 0, True),
            ("Black Jack", 1),
            ("Gin Rummy", 2),
            ("Hearts", 3),
            ("Bridge", 4),
            ("Checkers", 5),
            ("Chess", 6, True),
            ("Poker", 7),
            ("Fighter Combat", 8, True),
        )
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(SelectionList).border_title = "Shall we play some games?"

if __name__ == "__main__":
    SelectionListApp().run()
```

1. Note that the `SelectionList` is typed as `int`, for the type of the values.

```
Screen {
    align: center middle;
}

SelectionList {
    padding: 1;
    border: solid $accent;
    width: 80%;
    height: 80%;
}
```

### Selections as Selection objects¶

Alternatively, selections can be passed in as s:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, SelectionList
from textual.widgets.selection_list import Selection

class SelectionListApp(App[None]):
    CSS_PATH = "selection_list.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield SelectionList[int](  
            Selection("Falken's Maze", 0, True),
            Selection("Black Jack", 1),
            Selection("Gin Rummy", 2),
            Selection("Hearts", 3),
            Selection("Bridge", 4),
            Selection("Checkers", 5),
            Selection("Chess", 6, True),
            Selection("Poker", 7),
            Selection("Fighter Combat", 8, True),
        )
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(SelectionList).border_title = "Shall we play some games?"

if __name__ == "__main__":
    SelectionListApp().run()
```

1. Note that the `SelectionList` is typed as `int`, for the type of the values.

```
Screen {
    align: center middle;
}

SelectionList {
    padding: 1;
    border: solid $accent;
    width: 80%;
    height: 80%;
}
```

### Handling changes to the selections¶

Most of the time, when using the `SelectionList`, you will want to know when the collection of selected items has changed; this is ideally done using the message. Here is an example of using that message to update a `Pretty` with the collection of selected values:

<!-- SVG content removed by SVG Remover -->

```
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.events import Mount
from textual.widgets import Footer, Header, Pretty, SelectionList
from textual.widgets.selection_list import Selection

class SelectionListApp(App[None]):
    CSS_PATH = "selection_list_selected.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield SelectionList[str](  
                Selection("Falken's Maze", "secret_back_door", True),
                Selection("Black Jack", "black_jack"),
                Selection("Gin Rummy", "gin_rummy"),
                Selection("Hearts", "hearts"),
                Selection("Bridge", "bridge"),
                Selection("Checkers", "checkers"),
                Selection("Chess", "a_nice_game_of_chess", True),
                Selection("Poker", "poker"),
                Selection("Fighter Combat", "fighter_combat", True),
            )
            yield Pretty([])
        yield Footer()

    def on_mount(self) -> None:
        self.query_one(SelectionList).border_title = "Shall we play some games?"
        self.query_one(Pretty).border_title = "Selected games"

    @on(Mount)
    @on(SelectionList.SelectedChanged)
    def update_selected_view(self) -> None:
        self.query_one(Pretty).update(self.query_one(SelectionList).selected)

if __name__ == "__main__":
    SelectionListApp().run()
```

1. Note that the `SelectionList` is typed as `str`, for the type of the values.

```
Screen {
    align: center middle;
}

Horizontal {
    width: 80%;
    height: 80%;
}

SelectionList {
    padding: 1;
    border: solid $accent;
    width: 1fr;
}

Pretty {
    width: 1fr;
    border: solid $accent;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `highlighted` | `int` \| `None` | `None` | The index of the highlighted selection. `None` means nothing is highlighted. |

## Messages¶

## Bindings¶

The selection list widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| space | Toggle the state of the highlighted selection. |

It inherits from [`OptionList`](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList " OptionList") and so also inherits the following bindings:

| Key(s) | Description |
| --- | --- |
| down | Move the highlight down. |
| end | Move the highlight to the last option. |
| enter | Select the current option. |
| home | Move the highlight to the first option. |
| pagedown | Move the highlight down a page of options. |
| pageup | Move the highlight up a page of options. |
| up | Move the highlight up. |

## Component Classes¶

The selection list provides the following component classes:

| Class | Description |
| --- | --- |
| `selection-list--button` | Target the default button style. |
| `selection-list--button-selected` | Target a selected button style. |
| `selection-list--button-highlighted` | Target a highlighted button style. |
| `selection-list--button-selected-highlighted` | Target a highlighted selected button style. |

It inherits from [`OptionList`](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList " OptionList") and so also makes use of the following component classes:

| Class | Description |
| --- | --- |
| `option-list--option` | Target options that are not disabled, highlighted or have the mouse over them. |
| `option-list--option-disabled` | Target disabled options. |
| `option-list--option-highlighted` | Target the highlighted option. |
| `option-list--option-hover` | Target an option that has the mouse over it. |
| `option-list--separator` | Target the separators. |

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[OptionList](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList " OptionList (textual.widgets._option_list.OptionList)")`

A vertical selection list that allows making multiple selections.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `*selections` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList\(*selections\) "Permanent link") | `[] \| [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)"), ] \| [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)"), , [bool](https://docs.python.org/3/library/functions.html#bool)]` | The content for the selection list. | `()` |
| ## `name` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the selection list. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the selection list in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the selection list. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the selection list is disabled or not. | `False` |

## BINDINGS [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding("space", "select", "Toggle option", show=False)
]
```

| Key(s) | Description |
| --- | --- |
| space | Toggle the state of the highlighted selection. |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {
    "selection-list--button",
    "selection-list--button-selected",
    "selection-list--button-highlighted",
    "selection-list--button-selected-highlighted",
}
```

| Class | Description |
| --- | --- |
| `selection-list--button` | Target the default button style. |
| `selection-list--button-selected` | Target a selected button style. |
| `selection-list--button-highlighted` | Target a highlighted button style. |
| `selection-list--button-selected-highlighted` | Target a highlighted selected button style. |

## selected [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.selected "Permanent link")

```
selected
```

The selected values.

This is a list of all of the associated with selections in the list that are currently in the selected state.

## SelectedChanged [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectedChanged "Permanent link")

```
SelectedChanged(selection_list)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.messages.Message)")`

Message sent when the collection of selected values changes.

This is sent regardless of whether the change occurred via user interaction or programmatically the the `SelectionList` API.

When a bulk change occurs, such as through `select_all` or `deselect_all`, only a single `SelectedChanged` message will be sent (rather than one per option).

Can be handled using `on_selection_list_selected_changed` in a subclass of or in a parent node in the DOM.

### control [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectedChanged.control "Permanent link")

```
control
```

An alias for `selection_list`.

### selection\_list [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectedChanged.selection_list "Permanent link")

```
selection_list
```

The `SelectionList` that sent the message.

## SelectionHighlighted [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectionHighlighted "Permanent link")

```
SelectionHighlighted(selection_list, index)
```

Bases: `[]`

Message sent when a selection is highlighted.

Can be handled using `on_selection_list_selection_highlighted` in a subclass of or in a parent node in the DOM.

## SelectionMessage [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectionMessage "Permanent link")

```
SelectionMessage(, )
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.messages.Message)")`

Base class for all selection messages.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `selection_list` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectionMessage\(selection_list\) "Permanent link") | `[]` | The selection list that owns the selection. | *required* |
| ### `index` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectionMessage\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the selection that the message relates to. | *required* |

### control [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectionMessage.control "Permanent link")

```
control
```

The selection list that sent the message.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### selection [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectionMessage.selection "Permanent link")

```
selection = get_option_at_index()
```

The highlighted selection.

### selection\_index [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectionMessage.selection_index "Permanent link")

```
selection_index =
```

The index of the selection that the message relates to.

### selection\_list [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectionMessage.selection_list "Permanent link")

```
selection_list =
```

The selection list that sent the message.

## SelectionToggled [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.SelectionToggled "Permanent link")

```
SelectionToggled(selection_list, index)
```

Bases: `[]`

Message sent when a selection is toggled.

This is only sent when the value is *explicitly* toggled e.g. via `toggle` or `toggle_all`, or via user interaction. If you programmatically set a value to be selected, this message will not be sent, even if it happens to be the opposite of what was originally selected (i.e. setting a True to a False or vice-versa).

Since this message indicates a toggle occurring at a per-option level, a message will be sent for each option that is toggled, even when a bulk action is performed (e.g. via `toggle_all`).

Can be handled using `on_selection_list_selection_toggled` in a subclass of or in a parent node in the DOM.

## add\_option [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.add_option "Permanent link")

```
add_option(=None)
```

Add a new selection option to the end of the list.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `item` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.add_option\(item\) "Permanent link") | `[OptionListContent](https://textual.textualize.io/api/types/#textual.types.OptionListContent " OptionListContent (textual.widgets._option_list.OptionListContent)") \|  \| [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)"), ] \| [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)"), , [bool](https://docs.python.org/3/library/functions.html#bool)]` | The new item to add. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The instance. |

Raises:

| Type | Description |
| --- | --- |
| `DuplicateID` | If there is an attempt to use a duplicate ID. |
|  | If the selection option is of the wrong form. |

## add\_options [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.add_options "Permanent link")

```
add_options()
```

Add new selection options to the end of the list.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `items` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.add_options\(items\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[OptionListContent](https://textual.textualize.io/api/types/#textual.types.OptionListContent " OptionListContent (textual.widgets._option_list.OptionListContent)") \| [] \| [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)"), ] \| [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)"), , [bool](https://docs.python.org/3/library/functions.html#bool)]]` | The new items to add. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The instance. |

Raises:

| Type | Description |
| --- | --- |
| `DuplicateID` | If there is an attempt to use a duplicate ID. |
|  | If one of the selection options is of the wrong form. |

## clear\_options [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.clear_options "Permanent link")

```
clear_options()
```

Clear the content of the selection list.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `SelectionList` instance. |

## deselect [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.deselect "Permanent link")

```
deselect()
```

Mark the given selection as not selected.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `selection` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.deselect\(selection\) "Permanent link") | `[] \| ` | The selection to mark as not selected. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The instance. |

## deselect\_all [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.deselect_all "Permanent link")

```
deselect_all()
```

Deselect all items.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The instance. |

## get\_option [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.get_option "Permanent link")

```
get_option()
```

Get the selection option with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `option_id` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.get_option\(option_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the selection option to get. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[]` | The selection option with the ID. |

Raises:

| Type | Description |
| --- | --- |
| `[OptionDoesNotExist](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.OptionDoesNotExist " OptionDoesNotExist (textual.widgets._option_list.OptionDoesNotExist)")` | If no selection option has the given ID. |

## get\_option\_at\_index [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.get_option_at_index "Permanent link")

```
get_option_at_index()
```

Get the selection option at the given index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `index` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.get_option_at_index\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the selection option to get. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[]` | The selection option at that index. |

Raises:

| Type | Description |
| --- | --- |
| `[OptionDoesNotExist](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.OptionDoesNotExist " OptionDoesNotExist (textual.widgets._option_list.OptionDoesNotExist)")` | If there is no selection option with the index. |

## select [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.select "Permanent link")

```
select()
```

Mark the given selection as selected.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `selection` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.select\(selection\) "Permanent link") | `[] \| ` | The selection to mark as selected. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The instance. |

## select\_all [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.select_all "Permanent link")

```
select_all()
```

Select all items.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The instance. |

## toggle [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.toggle "Permanent link")

```
toggle()
```

Toggle the selected state of the given selection.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `selection` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.toggle\(selection\) "Permanent link") | `[] \| ` | The selection to toggle. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The instance. |

## toggle\_all [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.SelectionList.toggle_all "Permanent link")

```
toggle_all()
```

Toggle all items.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The instance. |

## MessageSelectionType [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.MessageSelectionType "Permanent link")

```
MessageSelectionType = TypeVar('MessageSelectionType')
```

The type for the value of a in a message.

## SelectionType [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.SelectionType "Permanent link")

```
SelectionType = TypeVar('SelectionType')
```

The type for the value of a in a

## Selection [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.Selection "Permanent link")

```
Selection(
    ,
    ,
    =False,
    =None,
    =False,
)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[Option](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.Option " Option (textual.widgets._option_list.Option)")`

A selection for a .

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `prompt` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.Selection\(prompt\) "Permanent link") | `[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)")` | The prompt for the selection. | *required* |
| ### `value` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.Selection\(value\) "Permanent link") |  | The value for the selection. | *required* |
| ### `initial_state` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.Selection\(initial_state\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | The initial selected state of the selection. | `False` |
| ### `id` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.Selection\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The optional ID for the selection. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.Selection\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | The initial enabled/disabled state. Enabled by default. | `False` |

### initial\_state [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.Selection.initial_state "Permanent link")

```
initial_state
```

The initial selected state for the selection.

### value [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.Selection.value "Permanent link")

```
value
```

The value for this selection.

## SelectionError [¶](https://textual.textualize.io/widgets/selection_list/#textual.widgets.selection_list.SelectionError "Permanent link")

Bases: `[TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)`

Type of an error raised if a selection is badly-formed.