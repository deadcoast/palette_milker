---
title: "Textual - OptionList"
source: "https://textual.textualize.io/widgets/option_list/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## OptionList¶

Added in version 0.17.0

A widget for showing a vertical list of Rich renderable options.

- Focusable
- Container

## Examples¶

### Options as simple strings¶

An `OptionList` can be constructed with a simple collection of string options:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, OptionList

class OptionListApp(App[None]):
    CSS_PATH = "option_list.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList(
            "Aerilon",
            "Aquaria",
            "Canceron",
            "Caprica",
            "Gemenon",
            "Leonis",
            "Libran",
            "Picon",
            "Sagittaron",
            "Scorpia",
            "Tauron",
            "Virgon",
        )
        yield Footer()

if __name__ == "__main__":
    OptionListApp().run()
```

```
Screen {
    align: center middle;
}

OptionList {
    width: 70%;
    height: 80%;
}
```

### Options as `Option` instances[¶](https://textual.textualize.io/widgets/option_list/#options-as-option-instances "Permanent link")

For finer control over the options, the `Option` class can be used; this allows for setting IDs, setting initial disabled state, etc. The `Separator` class can be used to add separator lines between options.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, OptionList
from textual.widgets.option_list import Option

class OptionListApp(App[None]):
    CSS_PATH = "option_list.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList(
            Option("Aerilon", id="aer"),
            Option("Aquaria", id="aqu"),
            None,
            Option("Canceron", id="can"),
            Option("Caprica", id="cap", disabled=True),
            None,
            Option("Gemenon", id="gem"),
            None,
            Option("Leonis", id="leo"),
            Option("Libran", id="lib"),
            None,
            Option("Picon", id="pic"),
            None,
            Option("Sagittaron", id="sag"),
            Option("Scorpia", id="sco"),
            None,
            Option("Tauron", id="tau"),
            None,
            Option("Virgon", id="vir"),
        )
        yield Footer()

if __name__ == "__main__":
    OptionListApp().run()
```

```
Screen {
    align: center middle;
}

OptionList {
    width: 70%;
    height: 80%;
}
```

### Options as Rich renderables¶

Because the prompts for the options can be [Rich renderables](https://rich.readthedocs.io/en/latest/protocol.html), this means they can be any height you wish. As an example, here is an option list comprised of [Rich tables](https://rich.readthedocs.io/en/latest/tables.html):

<!-- SVG content removed by SVG Remover -->

```
from __future__ import annotations

from rich.table import Table

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, OptionList

COLONIES: tuple[tuple[str, str, str, str], ...] = (
    ("Aerilon", "Demeter", "1.2 Billion", "Gaoth"),
    ("Aquaria", "Hermes", "75,000", "None"),
    ("Canceron", "Hephaestus", "6.7 Billion", "Hades"),
    ("Caprica", "Apollo", "4.9 Billion", "Caprica City"),
    ("Gemenon", "Hera", "2.8 Billion", "Oranu"),
    ("Leonis", "Artemis", "2.6 Billion", "Luminere"),
    ("Libran", "Athena", "2.1 Billion", "None"),
    ("Picon", "Poseidon", "1.4 Billion", "Queenstown"),
    ("Sagittaron", "Zeus", "1.7 Billion", "Tawa"),
    ("Scorpia", "Dionysus", "450 Million", "Celeste"),
    ("Tauron", "Ares", "2.5 Billion", "Hypatia"),
    ("Virgon", "Hestia", "4.3 Billion", "Boskirk"),
)

class OptionListApp(App[None]):
    CSS_PATH = "option_list.tcss"

    @staticmethod
    def colony(name: str, god: str, population: str, capital: str) -> Table:
        table = Table(title=f"Data for {name}", expand=True)
        table.add_column("Patron God")
        table.add_column("Population")
        table.add_column("Capital City")
        table.add_row(god, population, capital)
        return table

    def compose(self) -> ComposeResult:
        yield Header()
        yield OptionList(*[self.colony(*row) for row in COLONIES])
        yield Footer()

if __name__ == "__main__":
    OptionListApp().run()
```

```
Screen {
    align: center middle;
}

OptionList {
    width: 70%;
    height: 80%;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `highlighted` | `int` \| `None` | `None` | The index of the highlighted option. `None` means nothing is highlighted. |

## Messages¶

Both of the messages above inherit from the common base , so refer to its documentation to see what attributes are available.

## Bindings¶

The option list widget defines the following bindings:

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

The option list provides the following component classes:

| Class | Description |
| --- | --- |
| `option-list--option` | Target options that are not disabled, highlighted or have the mouse over them. |
| `option-list--option-disabled` | Target disabled options. |
| `option-list--option-highlighted` | Target the highlighted option. |
| `option-list--option-hover` | Target an option that has the mouse over it. |
| `option-list--separator` | Target the separators. |

Bases: `[ScrollView](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView " ScrollView (textual.scroll_view.ScrollView)")`

A navigable list of options.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `*content` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList\(*content\) "Permanent link") | `[OptionListContent](https://textual.textualize.io/api/types/#textual.types.OptionListContent " OptionListContent (textual.widgets._option_list.OptionListContent)")` | Positional arguments become the options. | `()` |
| ## `name` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Name of the OptionList. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the OptionList in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Initial CSS classes. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Disable the widget? | `False` |
| ## `markup` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList\(markup\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Strips should be rendered as Textual markup if `True`, or plain text if `False`. | `True` |

## BINDINGS [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding("down", "cursor_down", "Down", show=False),
    Binding("end", "last", "Last", show=False),
    Binding("enter", "select", "Select", show=False),
    Binding("home", "first", "First", show=False),
    Binding(
        "pagedown", "page_down", "Page Down", show=False
    ),
    Binding("pageup", "page_up", "Page Up", show=False),
    Binding("up", "cursor_up", "Up", show=False),
]
```

| Key(s) | Description |
| --- | --- |
| down | Move the highlight down. |
| end | Move the highlight to the last option. |
| enter | Select the current option. |
| home | Move the highlight to the first option. |
| pagedown | Move the highlight down a page of options. |
| pageup | Move the highlight up a page of options. |
| up | Move the highlight up. |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {
    "option-list--option",
    "option-list--option-disabled",
    "option-list--option-highlighted",
    "option-list--option-hover",
    "option-list--separator",
}
```

| Class | Description |
| --- | --- |
| `option-list--option` | Target options that are not disabled, highlighted or have the mouse over them. |
| `option-list--option-disabled` | Target disabled options. |
| `option-list--option-highlighted` | Target the highlighted option. |
| `option-list--option-hover` | Target an option that has the mouse over it. |
| `option-list--separator` | Target the separators. |

## highlighted [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.highlighted "Permanent link")

```
highlighted = reactive(None)
```

The index of the currently-highlighted option, or `None` if no option is highlighted.

## option\_count [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.option_count "Permanent link")

```
option_count
```

The number of options.

## options [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.options "Permanent link")

```
options
```

Sequence of options in the OptionList.

This is read-only

## OptionHighlighted [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionHighlighted "Permanent link")

```
OptionHighlighted(option_list, option, index)
```

Bases:

Message sent when an option is highlighted.

Can be handled using `on_option_list_option_highlighted` in a subclass of `OptionList` or in a parent node in the DOM.

## OptionMessage [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionMessage "Permanent link")

```
OptionMessage(, option, )
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Base class for all option messages.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `option_list` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionMessage\(option_list\) "Permanent link") |  | The option list that owns the option. | *required* |
| ### `index` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionMessage\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the option that the message relates to. | *required* |

### control [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionMessage.control "Permanent link")

```
control
```

The option list that sent the message.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### option [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionMessage.option "Permanent link")

```
option = option
```

The highlighted option.

### option\_id [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionMessage.option_id "Permanent link")

```
option_id = id
```

The ID of the option that the message relates to.

### option\_index [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionMessage.option_index "Permanent link")

```
option_index =
```

The index of the option that the message relates to.

### option\_list [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionMessage.option_list "Permanent link")

```
option_list =
```

The option list that sent the message.

## OptionSelected [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.OptionSelected "Permanent link")

```
OptionSelected(option_list, option, index)
```

Bases:

Message sent when an option is selected.

Can be handled using `on_option_list_option_selected` in a subclass of `OptionList` or in a parent node in the DOM.

## action\_cursor\_down [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.action_cursor_down "Permanent link")

```
action_cursor_down()
```

Move the highlight down to the next enabled option.

## action\_cursor\_up [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.action_cursor_up "Permanent link")

```
action_cursor_up()
```

Move the highlight up to the previous enabled option.

## action\_first [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.action_first "Permanent link")

```
action_first()
```

Move the highlight to the first enabled option.

## action\_last [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.action_last "Permanent link")

```
action_last()
```

Move the highlight to the last enabled option.

## action\_page\_down [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.action_page_down "Permanent link")

```
action_page_down()
```

Move the highlight down one page.

## action\_page\_up [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.action_page_up "Permanent link")

```
action_page_up()
```

Move the highlight up one page.

## action\_select [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.action_select "Permanent link")

```
action_select()
```

Select the currently highlighted option.

If an option is selected then a will be posted.

## add\_option [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.add_option "Permanent link")

```
add_option(=None)
```

Add a new option to the end of the option list.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `option` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.add_option\(option\) "Permanent link") | ` \| VisualType \| None` | New option to add, or `None` for a separator. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is an attempt to use a duplicate ID. |

## add\_options [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.add_options "Permanent link")

```
add_options()
```

Add new options.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `new_options` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.add_options\(new_options\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[OptionListContent](https://textual.textualize.io/api/types/#textual.types.OptionListContent " OptionListContent (textual.widgets._option_list.OptionListContent)")]` | Content of new options. | *required* |

## clear\_options [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.clear_options "Permanent link")

```
clear_options()
```

Clear the content of the option list.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

## disable\_option [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.disable_option "Permanent link")

```
disable_option()
```

Disable the option with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `option_id` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.disable_option\(option_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the option to disable. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

Raises:

| Type | Description |
| --- | --- |
|  | If no option has the given ID. |

## disable\_option\_at\_index [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.disable_option_at_index "Permanent link")

```
disable_option_at_index(index)
```

Disable the option at the given index.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is no option with the given index. |

## enable\_option [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.enable_option "Permanent link")

```
enable_option()
```

Enable the option with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `option_id` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.enable_option\(option_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the option to enable. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

Raises:

| Type | Description |
| --- | --- |
|  | If no option has the given ID. |

## enable\_option\_at\_index [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.enable_option_at_index "Permanent link")

```
enable_option_at_index(index)
```

Enable the option at the given index.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is no option with the given index. |

## get\_option [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.get_option "Permanent link")

```
get_option()
```

Get the option with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `option_id` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.get_option\(option_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the option to get. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The option with the ID. |

Raises:

| Type | Description |
| --- | --- |
|  | If no option has the given ID. |

## get\_option\_at\_index [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.get_option_at_index "Permanent link")

```
get_option_at_index()
```

Get the option at the given index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `index` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.get_option_at_index\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the option to get. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The option at that index. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is no option with the given index. |

## get\_option\_index [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.get_option_index "Permanent link")

```
get_option_index()
```

Get the index (offset in `self.options`) of the option with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `option_id` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.get_option_index\(option_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the option to get the index of. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the item with the given ID. |

Raises:

| Type | Description |
| --- | --- |
|  | If no option has the given ID. |

## remove\_option [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.remove_option "Permanent link")

```
remove_option()
```

Remove the option with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `option_id` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.remove_option\(option_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the option to remove. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

Raises:

| Type | Description |
| --- | --- |
|  | If no option has the given ID. |

## remove\_option\_at\_index [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.remove_option_at_index "Permanent link")

```
remove_option_at_index()
```

Remove the option at the given index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `index` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.remove_option_at_index\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the option to remove. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is no option with the given index. |

## replace\_option\_prompt [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.replace_option_prompt "Permanent link")

```
replace_option_prompt(, )
```

Replace the prompt of the option with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `option_id` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.replace_option_prompt\(option_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the option to replace the prompt of. | *required* |
| ### `prompt` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.replace_option_prompt\(prompt\) "Permanent link") | `VisualType` | The new prompt for the option. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

Raises:

| Type | Description |
| --- | --- |
|  | If no option has the given ID. |

## replace\_option\_prompt\_at\_index [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.replace_option_prompt_at_index "Permanent link")

```
replace_option_prompt_at_index(, )
```

Replace the prompt of the option at the given index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `index` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.replace_option_prompt_at_index\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the option to replace the prompt of. | *required* |
| ### `prompt` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.replace_option_prompt_at_index\(prompt\) "Permanent link") | `VisualType` | The new prompt for the option. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `OptionList` instance. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is no option with the given index. |

## scroll\_to\_highlight [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.scroll_to_highlight "Permanent link")

```
scroll_to_highlight(=False)
```

Scroll to the highlighted option.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `top` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.scroll_to_highlight\(top\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Ensure highlighted option is at the top of the widget. | `False` |

## validate\_highlighted [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.validate_highlighted "Permanent link")

```
validate_highlighted(highlighted)
```

Validate the `highlighted` property value on access.

## watch\_highlighted [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList.watch_highlighted "Permanent link")

```
watch_highlighted(highlighted)
```

React to the highlighted option having changed.

## DuplicateID [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.DuplicateID "Permanent link")

Bases: `OptionListError`

Raised if a duplicate ID is used when adding options to an option list.

## Option [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.Option "Permanent link")

```
Option(, =None, =False)
```

This class holds details of options in the list.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `prompt` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.Option\(prompt\) "Permanent link") | `VisualType` | The prompt (text displayed) for the option. | *required* |
| ### `id` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.Option\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An option ID for the option. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.Option\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Disable the option (will be shown grayed out, and will not be selectable). | `False` |

### id [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.Option.id "Permanent link")

```
id
```

Optional ID for the option.

### prompt [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.Option.prompt "Permanent link")

```
prompt
```

The original prompt.

## OptionDoesNotExist [¶](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.OptionDoesNotExist "Permanent link")

Bases: `OptionListError`

Raised when a request has been made for an option that doesn't exist.