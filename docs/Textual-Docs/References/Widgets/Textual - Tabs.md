---
title: "Textual - Tabs"
source: "https://textual.textualize.io/widgets/tabs/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Tabs¶

Added in version 0.15.0

Displays a number of tab headers which may be activated with a click or navigated with cursor keys.

- Focusable
- Container

Construct a `Tabs` widget with strings or [Text](https://rich.readthedocs.io/en/stable/reference/text.html#rich.text.Text) objects as positional arguments, which will set the labels in the tabs. Here's an example with three tabs:

```
def compose(self) -> ComposeResult:
    yield Tabs("First tab", "Second tab", Text.from_markup("[u]Third[/u] tab"))
```

This will create widgets internally, with auto-incrementing `id` attributes (`"tab-1"`, `"tab-2"` etc). You can also supply `Tab` objects directly in the constructor, which will allow you to explicitly set an `id`. Here's an example:

```
def compose(self) -> ComposeResult:
    yield Tabs(
        Tab("First tab", id="one"),
        Tab("Second tab", id="two"),
    )
```

When the user switches to a tab by clicking or pressing keys, then `Tabs` will send a message which contains the `tab` that was activated. You can then use `event.tab.id` attribute to perform any related actions.

## Clearing tabs¶

Clear tabs by calling the method. Clearing the tabs will send a message with the `tab` attribute set to `None`.

## Adding tabs¶

Tabs may be added dynamically with the method, which accepts strings, [Text](https://rich.readthedocs.io/en/stable/reference/text.html#rich.text.Text), or objects.

## Example¶

The following example adds a `Tabs` widget above a text label. Press A to add a tab, C to clear the tabs.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, Tabs

NAMES = [
    "Paul Atreidies",
    "Duke Leto Atreides",
    "Lady Jessica",
    "Gurney Halleck",
    "Baron Vladimir Harkonnen",
    "Glossu Rabban",
    "Chani",
    "Silgar",
]

class TabsApp(App):
    """Demonstrates the Tabs widget."""

    CSS = """
    Tabs {
        dock: top;
    }
    Screen {
        align: center middle;
    }
    Label {
        margin:1 1;
        width: 100%;
        height: 100%;
        background: $panel;
        border: tall $primary;
        content-align: center middle;
    }
    """

    BINDINGS = [
        ("a", "add", "Add tab"),
        ("r", "remove", "Remove active tab"),
        ("c", "clear", "Clear tabs"),
    ]

    def compose(self) -> ComposeResult:
        yield Tabs(NAMES[0])
        yield Label()
        yield Footer()

    def on_mount(self) -> None:
        """Focus the tabs when the app starts."""
        self.query_one(Tabs).focus()

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        """Handle TabActivated message sent by Tabs."""
        label = self.query_one(Label)
        if event.tab is None:
            # When the tabs are cleared, event.tab will be None
            label.visible = False
        else:
            label.visible = True
            label.update(event.tab.label)

    def action_add(self) -> None:
        """Add a new tab."""
        tabs = self.query_one(Tabs)
        # Cycle the names
        NAMES[:] = [*NAMES[1:], NAMES[0]]
        tabs.add_tab(NAMES[0])

    def action_remove(self) -> None:
        """Remove active tab."""
        tabs = self.query_one(Tabs)
        active_tab = tabs.active_tab
        if active_tab is not None:
            tabs.remove_tab(active_tab.id)

    def action_clear(self) -> None:
        """Clear the tabs."""
        self.query_one(Tabs).clear()

if __name__ == "__main__":
    app = TabsApp()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `active` | `str` | `""` | The ID of the active tab. Set this attribute to a tab ID to change the active tab. |

## Messages¶

## Bindings¶

The Tabs widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| left | Move to the previous tab. |
| right | Move to the next tab. |

## Component Classes¶

This widget has no component classes.

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A row of tabs.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `*tabs` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs\(*tabs\) "Permanent link") | ` \| [ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)")` | Positional argument should be explicit Tab objects, or a str or Text. | `()` |
| ## `active` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs\(active\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | ID of the tab which should be active on start. | `None` |
| ## `name` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional name for the tabs widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional ID for the widget. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional initial classes for the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

## BINDINGS [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding(
        "left", "previous_tab", "Previous tab", show=False
    ),
    Binding("right", "next_tab", "Next tab", show=False),
]
```

| Key(s) | Description |
| --- | --- |
| left | Move to the previous tab. |
| right | Move to the next tab. |

## active [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.active "Permanent link")

```
active = reactive('', init=False)
```

The ID of the active tab, or empty string if none are active.

## active\_tab [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.active_tab "Permanent link")

```
active_tab
```

The currently active tab, or None if there are no active tabs.

## tab\_count [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.tab_count "Permanent link")

```
tab_count
```

Total number of tabs.

## Cleared [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.Cleared "Permanent link")

```
Cleared()
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Sent when there are no active tabs.

This can occur when Tabs are cleared, if all tabs are hidden, or if the currently active tab is unset.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tabs` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.Cleared\(tabs\) "Permanent link") |  | The tabs widget. | *required* |

### control [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.Cleared.control "Permanent link")

```
control
```

The tabs widget which was cleared.

This is an alias for which is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### tabs [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.Cleared.tabs "Permanent link")

```
tabs =
```

The tabs widget which was cleared.

## TabActivated [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabActivated "Permanent link")

```
TabActivated(tabs, tab)
```

Bases:

Sent when a new tab is activated.

## TabDisabled [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabDisabled "Permanent link")

```
TabDisabled(tabs, tab)
```

Bases:

Sent when a tab is disabled.

## TabEnabled [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabEnabled "Permanent link")

```
TabEnabled(tabs, tab)
```

Bases:

Sent when a tab is enabled.

## TabError [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Exception raised when there is an error relating to tabs.

## TabHidden [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabHidden "Permanent link")

```
TabHidden(tabs, tab)
```

Bases:

Sent when a tab is hidden.

## TabMessage [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabMessage "Permanent link")

```
TabMessage(, )
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Parent class for all messages that have to do with a specific tab.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tabs` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabMessage\(tabs\) "Permanent link") |  | The Tabs widget. | *required* |
| ### `tab` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabMessage\(tab\) "Permanent link") |  | The tab that is the object of this message. | *required* |

### ALLOW\_SELECTOR\_MATCH [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabMessage.ALLOW_SELECTOR_MATCH "Permanent link")

```
ALLOW_SELECTOR_MATCH = {'tab'}
```

Additional message attributes that can be used with the [`on` decorator](https://textual.textualize.io/api/logger/#textual.on " on").

### control [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabMessage.control "Permanent link")

```
control
```

The tabs widget containing the tab that is the object of this message.

This is an alias for the attribute `tabs` and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### tab [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabMessage.tab "Permanent link")

```
tab =
```

The tab that is the object of this message.

### tabs [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabMessage.tabs "Permanent link")

```
tabs =
```

The tabs widget containing the tab.

## TabShown [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabShown "Permanent link")

```
TabShown(tabs, tab)
```

Bases:

Sent when a tab is shown.

## action\_next\_tab [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.action_next_tab "Permanent link")

```
action_next_tab()
```

Make the next tab active.

## action\_previous\_tab [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.action_previous_tab "Permanent link")

```
action_previous_tab()
```

Make the previous tab active.

## add\_tab [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.add_tab "Permanent link")

```
add_tab(, *, =None, =None)
```

Add a new tab to the end of the tab list.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.add_tab\(tab\) "Permanent link") | ` \| [ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)")` | A new tab object, or a label (str or Text). | *required* |
| ### `before` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.add_tab\(before\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional tab or tab ID to add the tab before. | `None` |
| ### `after` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.add_tab\(after\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional tab or tab ID to add the tab after. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An optionally awaitable object that waits for the tab to be mounted and internal state to be fully updated to reflect the new tab. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is a problem with the addition request. |

Note

Only one of `before` or `after` can be provided. If both are provided a `Tabs.TabError` will be raised.

## clear [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.clear "Permanent link")

```
clear()
```

Clear all the tabs.

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An awaitable object that waits for the tabs to be removed. |

## disable [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.disable "Permanent link")

```
disable()
```

Disable the indicated tab.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab_id` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.disable\(tab_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the to disable. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The that was targeted. |

Raises:

| Type | Description |
| --- | --- |
|  | If there are any issues with the request. |

## enable [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.enable "Permanent link")

```
enable()
```

Enable the indicated tab.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab_id` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.enable\(tab_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the to enable. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The that was targeted. |

Raises:

| Type | Description |
| --- | --- |
|  | If there are any issues with the request. |

## hide [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.hide "Permanent link")

```
hide()
```

Hide the indicated tab.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab_id` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.hide\(tab_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the to hide. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The that was targeted. |

Raises:

| Type | Description |
| --- | --- |
|  | If there are any issues with the request. |

## remove\_tab [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.remove_tab "Permanent link")

```
remove_tab()
```

Remove a tab.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab_or_id` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.remove_tab\(tab_or_id\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The Tab to remove or its id. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An optionally awaitable object that waits for the tab to be removed. |

## show [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.show "Permanent link")

```
show()
```

Show the indicated tab.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab_id` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.show\(tab_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the to show. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The that was targeted. |

Raises:

| Type | Description |
| --- | --- |
|  | If there are any issues with the request. |

## validate\_active [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.validate_active "Permanent link")

```
validate_active(active)
```

Check id assigned to active attribute is a valid tab.

## watch\_active [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.watch_active "Permanent link")

```
watch_active(previously_active, active)
```

Handle a change to the active tab.

---

Bases: `[Static](https://textual.textualize.io/widgets/static/#textual.widgets.Static " Static (textual.widgets.Static)")`

A Widget to manage a single tab within a Tabs widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `label` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab\(label\) "Permanent link") | `[ContentText](https://textual.textualize.io/api/content/#textual.content.ContentText " ContentText (textual.content.ContentText)")` | The label to use in the tab. | *required* |
| ## `id` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional ID for the widget. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Space separated list of class names. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the tab is disabled or not. | `False` |

## label [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab.label "Permanent link")

```
label
```

The label for the tab.

## label\_text [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab.label_text "Permanent link")

```
label_text
```

Undecorated text of the label.

## Clicked [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab.Clicked "Permanent link")

```
Clicked(tab)
```

Bases:

A tab was clicked.

## Disabled [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab.Disabled "Permanent link")

```
Disabled(tab)
```

Bases:

A tab was disabled.

## Enabled [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab.Enabled "Permanent link")

```
Enabled(tab)
```

Bases:

A tab was enabled.

## Relabelled [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab.Relabelled "Permanent link")

```
Relabelled(tab)
```

Bases:

A tab was relabelled.

## TabMessage [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab.TabMessage "Permanent link")

```
TabMessage(tab)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Tab-related messages.

These are mostly intended for internal use when interacting with `Tabs`.

### control [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab.TabMessage.control "Permanent link")

```
control
```

The tab that is the object of this message.

This is an alias for the attribute `tab` and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### tab [¶](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab.TabMessage.tab "Permanent link")

```
tab
```

The tab that is the object of this message.