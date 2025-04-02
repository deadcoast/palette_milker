---
title: "Textual - ListView"
source: "https://textual.textualize.io/widgets/list_view/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## ListView¶

Added in version 0.6.0

Displays a vertical list of `ListItem`s which can be highlighted and selected. Supports keyboard navigation.

- Focusable
- Container

## Example¶

The example below shows an app with a simple `ListView`.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, ListItem, ListView

class ListViewExample(App):
    CSS_PATH = "list_view.tcss"

    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("One")),
            ListItem(Label("Two")),
            ListItem(Label("Three")),
        )
        yield Footer()

if __name__ == "__main__":
    app = ListViewExample()
    app.run()
```

```
Screen {
    align: center middle;
}

ListView {
    width: 30;
    height: auto;
    margin: 2 2;
}

Label {
    padding: 1 2;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `index` | `int` | `0` | The currently highlighted index. |

## Messages¶

## Bindings¶

The list view widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| enter | Select the current item. |
| up | Move the cursor up. |
| down | Move the cursor down. |

## Component Classes¶

This widget has no component classes.

---

Bases: `[VerticalScroll](https://textual.textualize.io/api/containers/#textual.containers.VerticalScroll " VerticalScroll (textual.containers.VerticalScroll)")`

A vertical list view widget.

Displays a vertical list of `ListItem`s which can be highlighted and selected using the mouse or keyboard.

Attributes:

| Name | Type | Description |
| --- | --- | --- |
|  |  | The index in the list that's currently highlighted. |

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `*children` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView\(*children\) "Permanent link") | `[ListItem](https://textual.textualize.io/widgets/list_item/#textual.widgets.ListItem " ListItem (textual.widgets._list_item.ListItem)")` | The ListItems to display in the list. | `()` |
| ## `initial_index` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView\(initial_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The index that should be highlighted when the list is first mounted. | `0` |
| ## `name` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The unique ID of the widget used in CSS/query selection. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the ListView is disabled or not. | `False` |

## BINDINGS [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding("enter", "select_cursor", "Select", show=False),
    Binding("up", "cursor_up", "Cursor up", show=False),
    Binding(
        "down", "cursor_down", "Cursor down", show=False
    ),
]
```

| Key(s) | Description |
| --- | --- |
| enter | Select the current item. |
| up | Move the cursor up. |
| down | Move the cursor down. |

## highlighted\_child [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.highlighted_child "Permanent link")

```
highlighted_child
```

The currently highlighted ListItem, or None if nothing is highlighted.

## index [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.index "Permanent link")

```
index = reactive[Optional[int]](None, init=False)
```

The index of the currently highlighted item.

## Highlighted [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Highlighted "Permanent link")

```
Highlighted(list_view, item)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when the highlighted item changes.

Highlighted item is controlled using up/down keys. Can be handled using `on_list_view_highlighted` in a subclass of `ListView` or in a parent widget in the DOM.

### ALLOW\_SELECTOR\_MATCH [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Highlighted.ALLOW_SELECTOR_MATCH "Permanent link")

```
ALLOW_SELECTOR_MATCH = {'item'}
```

Additional message attributes that can be used with the [`on` decorator](https://textual.textualize.io/api/logger/#textual.on " on").

### control [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Highlighted.control "Permanent link")

```
control
```

The view that contains the item highlighted.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### item [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Highlighted.item "Permanent link")

```
item = item
```

The highlighted item, if there is one highlighted.

### list\_view [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Highlighted.list_view "Permanent link")

```
list_view = list_view
```

The view that contains the item highlighted.

## Selected [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Selected "Permanent link")

```
Selected(list_view, item)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when a list item is selected, e.g. when you press the enter key on it.

Can be handled using `on_list_view_selected` in a subclass of `ListView` or in a parent widget in the DOM.

### ALLOW\_SELECTOR\_MATCH [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Selected.ALLOW_SELECTOR_MATCH "Permanent link")

```
ALLOW_SELECTOR_MATCH = {'item'}
```

Additional message attributes that can be used with the [`on` decorator](https://textual.textualize.io/api/logger/#textual.on " on").

### control [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Selected.control "Permanent link")

```
control
```

The view that contains the item selected.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### item [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Selected.item "Permanent link")

```
item = item
```

The selected item.

### list\_view [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.Selected.list_view "Permanent link")

```
list_view = list_view
```

The view that contains the item selected.

## action\_cursor\_down [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.action_cursor_down "Permanent link")

```
action_cursor_down()
```

Highlight the next item in the list.

## action\_cursor\_up [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.action_cursor_up "Permanent link")

```
action_cursor_up()
```

Highlight the previous item in the list.

## action\_select\_cursor [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.action_select_cursor "Permanent link")

```
action_select_cursor()
```

Select the current item in the list.

## append [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.append "Permanent link")

```
append()
```

Append a new ListItem to the end of the ListView.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `item` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.append\(item\) "Permanent link") | `[ListItem](https://textual.textualize.io/widgets/list_item/#textual.widgets.ListItem " ListItem (textual.widgets._list_item.ListItem)")` | The ListItem to append. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitMount](https://textual.textualize.io/api/widget/#textual.widget.AwaitMount " AwaitMount (textual.widget.AwaitMount)")` | An awaitable that yields control to the event loop until the DOM has been updated with the new child item. |

## clear [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.clear "Permanent link")

```
clear()
```

Clear all items from the ListView.

Returns:

| Type | Description |
| --- | --- |
| `[AwaitRemove](https://textual.textualize.io/api/await_remove/#textual.await_remove.AwaitRemove " AwaitRemove (textual.await_remove.AwaitRemove)")` | An awaitable that yields control to the event loop until the DOM has been updated to reflect all children being removed. |

## extend [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.extend "Permanent link")

```
extend()
```

Append multiple new ListItems to the end of the ListView.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `items` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.extend\(items\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[ListItem](https://textual.textualize.io/widgets/list_item/#textual.widgets.ListItem " ListItem (textual.widgets._list_item.ListItem)")]` | The ListItems to append. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitMount](https://textual.textualize.io/api/widget/#textual.widget.AwaitMount " AwaitMount (textual.widget.AwaitMount)")` | An awaitable that yields control to the event loop until the DOM has been updated with the new child items. |

## insert [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.insert "Permanent link")

```
insert(, )
```

Insert new ListItem(s) to specified index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `index` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.insert\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | index to insert new ListItem. | *required* |
| ### `items` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.insert\(items\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[ListItem](https://textual.textualize.io/widgets/list_item/#textual.widgets.ListItem " ListItem (textual.widgets._list_item.ListItem)")]` | The ListItems to insert. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitMount](https://textual.textualize.io/api/widget/#textual.widget.AwaitMount " AwaitMount (textual.widget.AwaitMount)")` | An awaitable that yields control to the event loop until the DOM has been updated with the new child item. |

## pop [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.pop "Permanent link")

```
pop(=None)
```

Remove last ListItem from ListView or Remove ListItem from ListView by index

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `index` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.pop\(index\) "Permanent link") | `[Optional](https://docs.python.org/3/library/typing.html#typing.Optional "typing.Optional")[[int](https://docs.python.org/3/library/functions.html#int)]` | index of ListItem to remove from ListView | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An awaitable that yields control to the event loop until the DOM has been updated to reflect item being removed. |

## remove\_items [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.remove_items "Permanent link")

```
remove_items()
```

Remove ListItems from ListView by indices

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `indices` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.remove_items\(indices\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[int](https://docs.python.org/3/library/functions.html#int)]` | index(s) of ListItems to remove from ListView | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An awaitable object that waits for the direct children to be removed. |

## validate\_index [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.validate_index "Permanent link")

```
validate_index()
```

Clamp the index to the valid range, or set to None if there's nothing to highlight.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `index` [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.validate_index\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The index to clamp. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The clamped index. |

## watch\_index [¶](https://textual.textualize.io/widgets/list_view/#textual.widgets.ListView.watch_index "Permanent link")

```
watch_index(old_index, new_index)
```

Updates the highlighting when the index changes.