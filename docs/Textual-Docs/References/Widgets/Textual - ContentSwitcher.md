---
title: "Textual - ContentSwitcher"
source: "https://textual.textualize.io/widgets/content_switcher/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## ContentSwitcher¶

Added in version 0.14.0

A widget for containing and switching display between multiple child widgets.

- Focusable
- Container

## Example¶

The example below uses a `ContentSwitcher` in combination with two `Button`s to create a simple tabbed view. Note how each `Button` has an ID set, and how each child of the `ContentSwitcher` has a corresponding ID; then a `Button.Clicked` handler is used to set `ContentSwitcher.current` to switch between the different views.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, ContentSwitcher, DataTable, Markdown

MARKDOWN_EXAMPLE = """# Three Flavours Cornetto

The Three Flavours Cornetto trilogy is an anthology series of British
comedic genre films directed by Edgar Wright.

## Shaun of the Dead

| Flavour | UK Release Date | Director |
| -- | -- | -- |
| Strawberry | 2004-04-09 | Edgar Wright |

## Hot Fuzz

| Flavour | UK Release Date | Director |
| -- | -- | -- |
| Classico | 2007-02-17 | Edgar Wright |

## The World's End

| Flavour | UK Release Date | Director |
| -- | -- | -- |
| Mint | 2013-07-19 | Edgar Wright |
"""

class ContentSwitcherApp(App[None]):
    CSS_PATH = "content_switcher.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal(id="buttons"):  
            yield Button("DataTable", id="data-table")  
            yield Button("Markdown", id="markdown")  

        with ContentSwitcher(initial="data-table"):  
            yield DataTable(id="data-table")
            with VerticalScroll(id="markdown"):
                yield Markdown(MARKDOWN_EXAMPLE)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one(ContentSwitcher).current = event.button.id  

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Book", "Year")
        table.add_rows(
            [
                (title.ljust(35), year)
                for title, year in (
                    ("Dune", 1965),
                    ("Dune Messiah", 1969),
                    ("Children of Dune", 1976),
                    ("God Emperor of Dune", 1981),
                    ("Heretics of Dune", 1984),
                    ("Chapterhouse: Dune", 1985),
                )
            ]
        )

if __name__ == "__main__":
    ContentSwitcherApp().run()
```

1. A `Horizontal` to hold the buttons, each with a unique ID.
2. This button will select the `DataTable` in the `ContentSwitcher`.
3. This button will select the `Markdown` in the `ContentSwitcher`.
4. Note that the initial visible content is set by its ID, see below.
5. When a button is pressed, its ID is used to switch to a different widget in the `ContentSwitcher`. Remember that IDs are unique within parent, so the buttons and the widgets in the `ContentSwitcher` can share IDs.

```
Screen {
    align: center middle;
    padding: 1;
}

#buttons {
    height: 3;
    width: auto;
}

ContentSwitcher {
    border: round $primary;
    width: 90%;
    height: 1fr;
}

MarkdownH2 {
    background: $panel;
    color: yellow;
    border: none;
    padding: 0 1;
}
```

When the user presses the "Markdown" button the view is switched:

<!-- SVG content removed by SVG Remover -->

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `current` | `str` \| `None` | `None` | The ID of the currently-visible child. `None` means nothing is visible. |

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[Container](https://textual.textualize.io/api/containers/#textual.containers.Container " Container (textual.containers.Container)")`

A widget for switching between different children.

Note

All child widgets that are to be switched between need a unique ID. Children that have no ID will be hidden and ignored.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `*children` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher\(*children\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | The widgets to switch between. | `()` |
| ## `name` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the content switcher. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the content switcher in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the content switcher. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the content switcher is disabled or not. | `False` |
| ## `initial` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher\(initial\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the initial widget to show, `None` or empty string for the first tab. | `None` |

Note

If `initial` is not supplied no children will be shown to start with.

## current [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher.current "Permanent link")

```
current = reactive[Optional[str]](None, init=False)
```

The ID of the currently-displayed widget.

If set to `None` then no widget is visible.

Note

If set to an unknown ID, this will result in [`NoMatches`](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches") being raised.

## visible\_content [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher.visible_content "Permanent link")

```
visible_content
```

A reference to the currently-visible widget.

`None` if nothing is visible.

## add\_content [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher.add_content "Permanent link")

```
add_content(, *, =None, =False)
```

Add new content to the `ContentSwitcher`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `widget` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher.add_content\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A Widget to add. | *required* |
| ### `id` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher.add_content\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | ID for the widget, or `None` if the widget already has an ID. | `None` |
| ### `set_current` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher.add_content\(set_current\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Set the new widget as current (which will cause it to display). | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An awaitable to wait for the new content to be mounted. |

## watch\_current [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher.watch_current "Permanent link")

```
watch_current(, )
```

React to the current visible child choice being changed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `old` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher.watch_current\(old\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The old widget ID (or `None` if there was no widget). | *required* |
| ### `new` [¶](https://textual.textualize.io/widgets/content_switcher/#textual.widgets.ContentSwitcher.watch_current\(new\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The new widget ID (or `None` if nothing should be shown). | *required* |