---
title: "Textual - TabbedContent"
source: "https://textual.textualize.io/widgets/tabbed_content/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## TabbedContent¶

Added in version 0.16.0

Switch between mutually exclusive content panes via a row of tabs.

- Focusable
- Container

This widget combines the [Tabs](https://textual.textualize.io/widgets/tabs/) and [ContentSwitcher](https://textual.textualize.io/widgets/content_switcher/) widgets to create a convenient way of navigating content.

Only a single child of TabbedContent is visible at once. Each child has an associated tab which will make it visible and hide the others.

## Composing¶

There are two ways to provide the titles for the tab. You can pass them as positional arguments to the constructor:

```
def compose(self) -> ComposeResult:
    with TabbedContent("Leto", "Jessica", "Paul"):
        yield Markdown(LETO)
        yield Markdown(JESSICA)
        yield Markdown(PAUL)
```

Alternatively you can wrap the content in a widget, which takes the tab title as the first parameter:

```
def compose(self) -> ComposeResult:
    with TabbedContent():
        with TabPane("Leto"):
            yield Markdown(LETO)
        with TabPane("Jessica"):
            yield Markdown(JESSICA)
        with TabPane("Paul"):
            yield Markdown(PAUL)
```

## Switching tabs¶

If you need to programmatically switch tabs, you should provide an `id` attribute to the `TabPane`s.

```
def compose(self) -> ComposeResult:
    with TabbedContent():
        with TabPane("Leto", id="leto"):
            yield Markdown(LETO)
        with TabPane("Jessica", id="jessica"):
            yield Markdown(JESSICA)
        with TabPane("Paul", id="paul"):
            yield Markdown(PAUL)
```

You can then switch tabs by setting the `active` reactive attribute:

```
# Switch to Jessica tab
self.query_one(TabbedContent).active = "jessica"
```

Note

If you don't provide `id` attributes to the tab panes, they will be assigned sequentially starting at `tab-1` (then `tab-2` etc).

## Initial tab¶

The first child of `TabbedContent` will be the initial active tab by default. You can pick a different initial tab by setting the `initial` argument to the `id` of the tab:

```
def compose(self) -> ComposeResult:
    with TabbedContent(initial="jessica"):
        with TabPane("Leto", id="leto"):
            yield Markdown(LETO)
        with TabPane("Jessica", id="jessica"):
            yield Markdown(JESSICA)
        with TabPane("Paul", id="paul"):
            yield Markdown(PAUL)
```

## Example¶

The following example contains a `TabbedContent` with three tabs.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, Markdown, TabbedContent, TabPane

LETO = """
# Duke Leto I Atreides

Head of House Atreides.
"""

JESSICA = """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""

PAUL = """
# Paul Atreides

Son of Leto and Jessica.
"""

class TabbedApp(App):
    """An example of tabbed content."""

    BINDINGS = [
        ("l", "show_tab('leto')", "Leto"),
        ("j", "show_tab('jessica')", "Jessica"),
        ("p", "show_tab('paul')", "Paul"),
    ]

    def compose(self) -> ComposeResult:
        """Compose app with tabbed content."""
        # Footer to show keys
        yield Footer()

        # Add the TabbedContent widget
        with TabbedContent(initial="jessica"):
            with TabPane("Leto", id="leto"):  # First tab
                yield Markdown(LETO)  # Tab content
            with TabPane("Jessica", id="jessica"):
                yield Markdown(JESSICA)
                with TabbedContent("Paul", "Alia"):
                    yield TabPane("Paul", Label("First child"))
                    yield TabPane("Alia", Label("Second child"))

            with TabPane("Paul", id="paul"):
                yield Markdown(PAUL)

    def action_show_tab(self, tab: str) -> None:
        """Switch to a new tab."""
        self.get_child_by_type(TabbedContent).active = tab

if __name__ == "__main__":
    app = TabbedApp()
    app.run()
```

## Styling¶

The `TabbedContent` widget is composed of two main sub-widgets: a [`Tabs`](https://textual.textualize.io/widgets/tabs/) and a [`ContentSwitcher`](https://textual.textualize.io/widgets/content_switcher/); you can style them accordingly.

The tabs within the `Tabs` widget will have prefixed IDs; each ID being the ID of the `TabPane` the `Tab` is for, prefixed with `--content-tab-`. If you wish to style individual tabs within the `TabbedContent` widget you will need to use that prefix for the `Tab` IDs.

For example, to create a `TabbedContent` that has red and green labels:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Label, TabbedContent, TabPane

class ColorTabsApp(App):
    CSS = """
    TabbedContent #--content-tab-green {
        color: green;
    }

    TabbedContent #--content-tab-red {
        color: red;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Red", id="red"):
                yield Label("Red!")
            with TabPane("Green", id="green"):
                yield Label("Green!")

if __name__ == "__main__":
    ColorTabsApp().run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `active` | `str` | `""` | The `id` attribute of the active tab. Set this to switch tabs. |

## Messages¶

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

## See also¶

- [Tabs](https://textual.textualize.io/widgets/tabs/)
- [ContentSwitcher](https://textual.textualize.io/widgets/content_switcher/)

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A container with associated tabs to toggle content visibility.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `*titles` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent\(*titles\) "Permanent link") | `[ContentType](https://textual.textualize.io/api/content/#textual.content.ContentType " ContentType (textual.content.ContentType)")` | Positional argument will be used as title. | `()` |
| ## `initial` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent\(initial\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The id of the initial tab, or empty string to select the first tab. | `''` |
| ## `name` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the tabbed content. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the tabbed content in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the tabbed content. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the tabbed content is disabled or not. | `False` |

## active [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.active "Permanent link")

```
active = reactive('', init=False)
```

The ID of the active tab, or empty string if none are active.

## active\_pane [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.active_pane "Permanent link")

```
active_pane
```

The currently active pane, or `None` if no pane is active.

## tab\_count [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.tab_count "Permanent link")

```
tab_count
```

Total number of tabs.

## Cleared [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.Cleared "Permanent link")

```
Cleared()
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when no tab pane is active.

This can happen if all tab panes are removed or if the currently active tab pane is unset.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tabbed_content` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.Cleared\(tabbed_content\) "Permanent link") |  | The TabbedContent widget. | *required* |

### control [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.Cleared.control "Permanent link")

```
control
```

The `TabbedContent` widget that was cleared of all tab panes.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### tabbed\_content [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.Cleared.tabbed_content "Permanent link")

```
tabbed_content =
```

The `TabbedContent` widget that contains the tab activated.

## TabActivated [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.TabActivated "Permanent link")

```
TabActivated(, )
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when the active tab changes.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tabbed_content` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.TabActivated\(tabbed_content\) "Permanent link") |  | The TabbedContent widget. | *required* |
| ### `tab` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.TabActivated\(tab\) "Permanent link") | `ContentTab` | The Tab widget that was selected (contains the tab label). | *required* |

### ALLOW\_SELECTOR\_MATCH [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.TabActivated.ALLOW_SELECTOR_MATCH "Permanent link")

```
ALLOW_SELECTOR_MATCH = {'pane'}
```

Additional message attributes that can be used with the [`on` decorator](https://textual.textualize.io/api/logger/#textual.on " on").

### control [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.TabActivated.control "Permanent link")

```
control
```

The `TabbedContent` widget that contains the tab activated.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### pane [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.TabActivated.pane "Permanent link")

```
pane = get_pane()
```

The `TabPane` widget that was activated by selecting the tab.

### tab [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.TabActivated.tab "Permanent link")

```
tab =
```

The `Tab` widget that was selected (contains the tab label).

### tabbed\_content [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.TabActivated.tabbed_content "Permanent link")

```
tabbed_content =
```

The `TabbedContent` widget that contains the tab activated.

## add\_pane [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.add_pane "Permanent link")

```
add_pane(, *, =None, =None)
```

Add a new pane to the tabbed content.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `pane` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.add_pane\(pane\) "Permanent link") |  | The pane to add. | *required* |
| ### `before` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.add_pane\(before\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional pane or pane ID to add the pane before. | `None` |
| ### `after` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.add_pane\(after\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional pane or pane ID to add the pane after. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An optionally awaitable object that waits for the pane to be added. |

Raises:

| Type | Description |
| --- | --- |
| `[TabError](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabError " TabError (textual.widgets._tabs.Tabs.TabError)")` | If there is a problem with the addition request. |

Note

Only one of `before` or `after` can be provided. If both are provided an exception is raised.

## clear\_panes [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.clear_panes "Permanent link")

```
clear_panes()
```

Remove all the panes in the tabbed content.

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An optionally awaitable object which waits for all panes to be removed and the Cleared message to be posted. |

## disable\_tab [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.disable_tab "Permanent link")

```
disable_tab()
```

Disables the tab with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab_id` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.disable_tab\(tab_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the to disable. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[TabError](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabError " TabError (textual.widgets._tabs.Tabs.TabError)")` | If there are any issues with the request. |

## enable\_tab [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.enable_tab "Permanent link")

```
enable_tab()
```

Enables the tab with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab_id` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.enable_tab\(tab_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the to enable. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[TabError](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabError " TabError (textual.widgets._tabs.Tabs.TabError)")` | If there are any issues with the request. |

## get\_pane [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.get_pane "Permanent link")

```
get_pane()
```

Get the `TabPane` associated with the given ID or tab.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `pane_id` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.get_pane\(pane_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| ContentTab` | The ID of the pane to get, or the Tab it is associated with. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The `TabPane` associated with the ID or the given tab. |

Raises:

| Type | Description |
| --- | --- |
| `[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` | Raised if no ID was available. |

## get\_tab [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.get_tab "Permanent link")

```
get_tab()
```

Get the `Tab` associated with the given ID or `TabPane`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `pane_id` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.get_tab\(pane_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| ` | The ID of the pane, or the pane itself. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Tab](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tab " Tab (textual.widgets._tabs.Tab)")` | The Tab associated with the ID. |

Raises:

| Type | Description |
| --- | --- |
| `[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` | Raised if no ID was available. |

## hide\_tab [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.hide_tab "Permanent link")

```
hide_tab()
```

Hides the tab with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab_id` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.hide_tab\(tab_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the to hide. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[TabError](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabError " TabError (textual.widgets._tabs.Tabs.TabError)")` | If there are any issues with the request. |

## remove\_pane [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.remove_pane "Permanent link")

```
remove_pane()
```

Remove a given pane from the tabbed content.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `pane_id` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.remove_pane\(pane_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the pane to remove. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An optionally awaitable object that waits for the pane to be removed and the Cleared message to be posted. |

## show\_tab [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.show_tab "Permanent link")

```
show_tab()
```

Shows the tab with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tab_id` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.show_tab\(tab_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the to show. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[TabError](https://textual.textualize.io/widgets/tabs/#textual.widgets.Tabs.TabError " TabError (textual.widgets._tabs.Tabs.TabError)")` | If there are any issues with the request. |

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A container for switchable content, with additional title.

This widget is intended to be used with .

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `title` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane\(title\) "Permanent link") | `[ContentType](https://textual.textualize.io/api/content/#textual.content.ContentType " ContentType (textual.content.ContentType)")` | Title of the TabPane (will be displayed in a tab label). | *required* |
| ## `*children` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane\(*children\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | Widget to go inside the TabPane. | `()` |
| ## `name` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional name for the TabPane. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional ID for the TabPane. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional initial classes for the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the TabPane is disabled or not. | `False` |

## Disabled [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane.Disabled "Permanent link")

```
Disabled(tab_pane)
```

Bases:

Sent when a tab pane is disabled via its reactive `disabled`.

## Enabled [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane.Enabled "Permanent link")

```
Enabled(tab_pane)
```

Bases:

Sent when a tab pane is enabled via its reactive `disabled`.

## Focused [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane.Focused "Permanent link")

```
Focused(tab_pane)
```

Bases:

Sent when a child widget is focused.

## TabPaneMessage [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane.TabPaneMessage "Permanent link")

```
TabPaneMessage(tab_pane)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Base class for `TabPane` messages.

### control [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane.TabPaneMessage.control "Permanent link")

```
control
```

The tab pane that is the object of this message.

This is an alias for the attribute `tab_pane` and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### tab\_pane [¶](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabPane.TabPaneMessage.tab_pane "Permanent link")

```
tab_pane
```

The `TabPane` that is he object of this message.