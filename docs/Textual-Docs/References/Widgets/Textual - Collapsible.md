---
title: "Textual - Collapsible"
source: "https://textual.textualize.io/widgets/collapsible/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Collapsible¶

Added in version 0.37

A container with a title that can be used to show (expand) or hide (collapse) content, either by clicking or focusing and pressing Enter.

- Focusable
- Container

## Composing¶

You can add content to a Collapsible widget either by passing in children to the constructor, or with a context manager (`with` statement).

Here is an example of using the constructor to add content:

```
def compose(self) -> ComposeResult:
    yield Collapsible(Label("Hello, world."))
```

Here's how the to use it with the context manager:

```
def compose(self) -> ComposeResult:
    with Collapsible():
        yield Label("Hello, world.")
```

The second form is generally preferred, but the end result is the same.

The default title "Toggle" can be customized by setting the `title` parameter of the constructor:

```
def compose(self) -> ComposeResult:
    with Collapsible(title="An interesting story."):
        yield Label("Interesting but verbose story.")
```

## Initial State¶

The initial state of the `Collapsible` widget can be customized via the `collapsed` parameter of the constructor:

```
def compose(self) -> ComposeResult:
    with Collapsible(title="Contents 1", collapsed=False):
        yield Label("Hello, world.")

    with Collapsible(title="Contents 2", collapsed=True):  # Default.
        yield Label("Hello, world.")
```

## Collapse/Expand Symbols¶

The symbols used to show the collapsed / expanded state can be customized by setting the parameters `collapsed_symbol` and `expanded_symbol`:

```
def compose(self) -> ComposeResult:
    with Collapsible(collapsed_symbol=">>>", expanded_symbol="v"):
        yield Label("Hello, world.")
```

## Examples¶

The following example contains three `Collapsible`s in different states.

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Collapsible, Footer, Label, Markdown

LETO = """\
# Duke Leto I Atreides

Head of House Atreides."""

JESSICA = """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""

PAUL = """
# Paul Atreides

Son of Leto and Jessica.
"""

class CollapsibleApp(App[None]):
    """An example of collapsible container."""

    BINDINGS = [
        ("c", "collapse_or_expand(True)", "Collapse All"),
        ("e", "collapse_or_expand(False)", "Expand All"),
    ]

    def compose(self) -> ComposeResult:
        """Compose app with collapsible containers."""
        yield Footer()
        with Collapsible(collapsed=False, title="Leto"):
            yield Label(LETO)
        yield Collapsible(Markdown(JESSICA), collapsed=False, title="Jessica")
        with Collapsible(collapsed=True, title="Paul"):
            yield Markdown(PAUL)

    def action_collapse_or_expand(self, collapse: bool) -> None:
        for child in self.walk_children(Collapsible):
            child.collapsed = collapse

if __name__ == "__main__":
    app = CollapsibleApp()
    app.run()
```

### Setting Initial State¶

The example below shows nested `Collapsible` widgets and how to set their initial state.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Collapsible, Label

class CollapsibleApp(App[None]):
    def compose(self) -> ComposeResult:
        with Collapsible(collapsed=False):
            with Collapsible():
                yield Label("Hello, world.")

if __name__ == "__main__":
    app = CollapsibleApp()
    app.run()
```

### Custom Symbols¶

The following example shows `Collapsible` widgets with custom expand/collapse symbols.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Collapsible, Label

class CollapsibleApp(App[None]):
    def compose(self) -> ComposeResult:
        with Horizontal():
            with Collapsible(
                collapsed_symbol=">>>",
                expanded_symbol="v",
            ):
                yield Label("Hello, world.")

            with Collapsible(
                collapsed_symbol=">>>",
                expanded_symbol="v",
                collapsed=False,
            ):
                yield Label("Hello, world.")

if __name__ == "__main__":
    app = CollapsibleApp()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `collapsed` | `bool` | `True` | Controls the collapsed/expanded state of the widget. |
| `title` | `str` | `"Toggle"` | Title of the collapsed/expanded contents. |

## Messages¶

## Bindings¶

The collapsible widget defines the following binding on its title:

| Key(s) | Description |
| --- | --- |
| enter | Toggle the collapsible. |

## Component Classes¶

This widget has no component classes.

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A collapsible container.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `*children` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible\(*children\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | Contents that will be collapsed/expanded. | `()` |
| ## `title` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible\(title\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Title of the collapsed/expanded contents. | `'Toggle'` |
| ## `collapsed` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible\(collapsed\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Default status of the contents. | `True` |
| ## `collapsed_symbol` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible\(collapsed_symbol\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Collapsed symbol before the title. | `'▶'` |
| ## `expanded_symbol` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible\(expanded_symbol\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Expanded symbol before the title. | `'▼'` |
| ## `name` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the collapsible. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the collapsible in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the collapsible. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the collapsible is disabled or not. | `False` |

## Collapsed [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible.Collapsed "Permanent link")

```
Collapsed(collapsible)
```

Bases:

Event sent when the `Collapsible` widget is collapsed.

Can be handled using `on_collapsible_collapsed` in a subclass of or in a parent widget in the DOM.

## Expanded [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible.Expanded "Permanent link")

```
Expanded(collapsible)
```

Bases:

Event sent when the `Collapsible` widget is expanded.

Can be handled using `on_collapsible_expanded` in a subclass of or in a parent widget in the DOM.

## Toggled [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible.Toggled "Permanent link")

```
Toggled()
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Parent class subclassed by `Collapsible` messages.

Can be handled with `on(Collapsible.Toggled)` if you want to handle expansions and collapsed in the same way, or you can handle the specific events individually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `collapsible` [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible.Toggled\(collapsible\) "Permanent link") |  | The `Collapsible` widget that was toggled. | *required* |

### collapsible [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible.Toggled.collapsible "Permanent link")

```
collapsible =
```

The collapsible that was toggled.

### control [¶](https://textual.textualize.io/widgets/collapsible/#textual.widgets.Collapsible.Toggled.control "Permanent link")

```
control
```

An alias for .