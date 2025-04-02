---
title: "Textual - MarkdownViewer"
source: "https://textual.textualize.io/widgets/markdown_viewer/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## MarkdownViewer¶

Added in version 0.11.0

A Widget to display Markdown content with an optional Table of Contents.

- Focusable
- Container

Note

This Widget adds browser-like functionality on top of the [Markdown](https://textual.textualize.io/widgets/markdown/) widget.

## Example¶

The following example displays Markdown from a string and a Table of Contents.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import MarkdownViewer

EXAMPLE_MARKDOWN = """\
# Markdown Viewer

This is an example of Textual's \`MarkdownViewer\` widget.

## Features

Markdown syntax and extensions are supported.

- Typography *emphasis*, **strong**, \`inline code\` etc.
- Headers
- Lists (bullet and ordered)
- Syntax highlighted code blocks
- Tables!

## Tables

Tables are displayed in a DataTable widget.

| Name            | Type   | Default | Description                        |
| --------------- | ------ | ------- | ---------------------------------- |
| \`show_header\`   | \`bool\` | \`True\`  | Show the table header              |
| \`fixed_rows\`    | \`int\`  | \`0\`     | Number of fixed rows               |
| \`fixed_columns\` | \`int\`  | \`0\`     | Number of fixed columns            |
| \`zebra_stripes\` | \`bool\` | \`False\` | Display alternating colors on rows |
| \`header_height\` | \`int\`  | \`1\`     | Height of header row               |
| \`show_cursor\`   | \`bool\` | \`True\`  | Show a cell cursor                 |

## Code Blocks

Code blocks are syntax highlighted, with guidelines.

\`\`\`python
class ListViewExample(App):
    def compose(self) -> ComposeResult:
        yield ListView(
            ListItem(Label("One")),
            ListItem(Label("Two")),
            ListItem(Label("Three")),
        )
        yield Footer()
\`\`\`
"""

class MarkdownExampleApp(App):
    def compose(self) -> ComposeResult:
        yield MarkdownViewer(EXAMPLE_MARKDOWN, show_table_of_contents=True)

if __name__ == "__main__":
    app = MarkdownExampleApp()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `show_table_of_contents` | bool | True | Whether a Table of Contents should be displayed with the Markdown. |

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

## See Also¶

- [Markdown](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown " Markdown") code reference

---

Bases: `[VerticalScroll](https://textual.textualize.io/api/containers/#textual.containers.VerticalScroll " VerticalScroll (textual.containers.VerticalScroll)")`

A Markdown viewer widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `markdown` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer\(markdown\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | String containing Markdown, or None to leave blank. | `None` |
| ## `show_table_of_contents` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer\(show_table_of_contents\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Show a table of contents in a sidebar. | `True` |
| ## `name` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the widget. | `None` |
| ## `parser_factory` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer\(parser_factory\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[], MarkdownIt] \| None` | A factory function to return a configured MarkdownIt instance. If `None`, a "gfm-like" parser is used. | `None` |
| ## `open_links` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer\(open_links\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Open links automatically. If you set this to `False`, you can handle the events. | `True` |

## document [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer.document "Permanent link")

```
document
```

The [`Markdown`](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown " Markdown") document widget.

## table\_of\_contents [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer.table_of_contents "Permanent link")

```
table_of_contents
```

The widget.

## NavigatorUpdated [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer.NavigatorUpdated "Permanent link")

```
NavigatorUpdated()
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Navigator has been changed (clicked link etc).

## back [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer.back "Permanent link")

```
back()
```

Go back one level in the history.

## forward [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer.forward "Permanent link")

```
forward()
```

Go forward one level in the history.

## go [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer.go "Permanent link")

```
go(location)
```

Navigate to a new document path.

## textual.widgets.markdown [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown "Permanent link")

### TableOfContentsType [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.TableOfContentsType "Permanent link")

```
TableOfContentsType = 'list[tuple[int, str, str | None]]'
```

Information about the table of contents of a markdown document.

The triples encode the level, the label, and the optional block id of each heading.

### Markdown [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown "Permanent link")

```
Markdown(
    =None,
    *,
    =None,
    =None,
    =None,
    =None,
    =True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `markdown` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown\(markdown\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | String containing Markdown or None to leave blank for now. | `None` |
| #### `name` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| #### `id` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| #### `classes` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the widget. | `None` |
| #### `parser_factory` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown\(parser_factory\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[], MarkdownIt] \| None` | A factory function to return a configured MarkdownIt instance. If `None`, a "gfm-like" parser is used. | `None` |
| #### `open_links` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown\(open_links\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Open links automatically. If you set this to `False`, you can handle the events. | `True` |

#### COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {'em', 'strong', 's', 'code_inline'}
```

These component classes target standard inline markdown styles. Changing these will potentially break the standard markdown formatting.

| Class | Description |
| --- | --- |
| `code_inline` | Target text that is styled as inline code. |
| `em` | Target text that is emphasized inline. |
| `s` | Target text that is styled inline with strikethrough. |
| `strong` | Target text that is styled inline with strong. |

#### code\_dark\_theme [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.code_dark_theme "Permanent link")

```
code_dark_theme = reactive('material')
```

The theme to use for code blocks when the App theme is dark.

#### code\_light\_theme [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.code_light_theme "Permanent link")

```
code_light_theme = reactive('material-light')
```

The theme to use for code blocks when the App theme is light.

#### LinkClicked [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.LinkClicked "Permanent link")

```
LinkClicked(markdown, href)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

A link in the document was clicked.

##### control [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.LinkClicked.control "Permanent link")

```
control
```

The `Markdown` widget containing the link clicked.

This is an alias for [`LinkClicked.markdown`](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.LinkClicked.markdown " markdown") and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

##### href [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.LinkClicked.href "Permanent link")

```
href = unquote(href)
```

The link that was selected.

##### markdown [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.LinkClicked.markdown "Permanent link")

```
markdown = markdown
```

The `Markdown` widget containing the link clicked.

#### TableOfContentsSelected [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.TableOfContentsSelected "Permanent link")

```
TableOfContentsSelected(markdown, block_id)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

An item in the TOC was selected.

##### block\_id [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.TableOfContentsSelected.block_id "Permanent link")

```
block_id = block_id
```

ID of the block that was selected.

##### control [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.TableOfContentsSelected.control "Permanent link")

```
control
```

The `Markdown` widget where the selected item is.

This is an alias for [`TableOfContentsSelected.markdown`](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsSelected.markdown " markdown") and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

##### markdown [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.TableOfContentsSelected.markdown "Permanent link")

```
markdown = markdown
```

The `Markdown` widget where the selected item is.

#### TableOfContentsUpdated [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.TableOfContentsUpdated "Permanent link")

```
TableOfContentsUpdated(markdown, table_of_contents)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

The table of contents was updated.

##### control [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.TableOfContentsUpdated.control "Permanent link")

```
control
```

The `Markdown` widget associated with the table of contents.

This is an alias for [`TableOfContentsUpdated.markdown`](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsSelected.markdown " markdown") and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

##### markdown [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.TableOfContentsUpdated.markdown "Permanent link")

```
markdown = markdown
```

The `Markdown` widget associated with the table of contents.

##### table\_of\_contents [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.TableOfContentsUpdated.table_of_contents "Permanent link")

```
table_of_contents = table_of_contents
```

Table of contents.

#### goto\_anchor [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.goto_anchor "Permanent link")

```
goto_anchor()
```

Try and find the given anchor in the current document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `anchor` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.goto_anchor\(anchor\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The anchor to try and find. | *required* |

Note

The anchor is found by looking at all of the headings in the document and finding the first one whose slug matches the anchor.

Note that the slugging method used is similar to that found on GitHub.

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True when the anchor was found in the current document, False otherwise. |

#### load [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.load "Permanent link")

```
load()
```

Load a new Markdown document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `path` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.load\(path\) "Permanent link") | `[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")` | Path to the document. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[OSError](https://docs.python.org/3/library/exceptions.html#OSError)` | If there was some form of error loading the document. |

Note

The exceptions that can be raised by this method are all of those that can be raised by calling [`Path.read_text`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text).

#### sanitize\_location [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.sanitize_location "Permanent link")

```
sanitize_location()
```

Given a location, break out the path and any anchor.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `location` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.sanitize_location\(location\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The location to sanitize. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")` | A tuple of the path to the location cleaned of any anchor, plus |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | the anchor (or an empty string if none was found). |

#### unhandled\_token [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.unhandled_token "Permanent link")

```
unhandled_token()
```

Process an unhandled token.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `token` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.unhandled_token\(token\) "Permanent link") | `Token` | The MarkdownIt token to handle. | *required* |

Returns:

| Type | Description |
| --- | --- |
| ` \| None` | Either a widget to be added to the output, or `None`. |

#### update [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.update "Permanent link")

```
update()
```

Update the document with new Markdown.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `markdown` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.update\(markdown\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A string containing Markdown. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An optionally awaitable object. Await this to ensure that all children have been mounted. |

### MarkdownBlock [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownBlock "Permanent link")

```
MarkdownBlock(markdown, *args, **kwargs)
```

Bases: `[Static](https://textual.textualize.io/widgets/static/#textual.widgets.Static " Static (textual.widgets.Static)")`

The base class for a Markdown Element.

#### action\_link [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownBlock.action_link "Permanent link")

```
action_link(href)
```

Called on link click.

#### build\_from\_token [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownBlock.build_from_token "Permanent link")

```
build_from_token()
```

Build the block content from its source token.

This method allows the block to be rebuilt on demand, which is useful when the styles assigned to the [Markdown.COMPONENT\_CLASSES](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.COMPONENT_CLASSES " COMPONENT_CLASSES") change.

See https://github.com/Textualize/textual/issues/3464 for more information.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `token` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownBlock.build_from_token\(token\) "Permanent link") | `Token` | The token from which this block is built. | *required* |

#### notify\_style\_update [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownBlock.notify_style_update "Permanent link")

```
notify_style_update()
```

If CSS was reloaded, try to rebuild this block from its token.

#### rebuild [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownBlock.rebuild "Permanent link")

```
rebuild()
```

Rebuild the content of the block if we have a source token.

### MarkdownTableOfContents [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents "Permanent link")

```
MarkdownTableOfContents(
    ,
    =None,
    =None,
    =None,
    =False,
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

Displays a table of contents for a markdown document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `markdown` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents\(markdown\) "Permanent link") |  | The Markdown document associated with this table of contents. | *required* |
| #### `name` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| #### `id` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| #### `classes` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the widget. | `None` |
| #### `disabled` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

#### markdown [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents.markdown "Permanent link")

```
markdown =
```

The Markdown document associated with this table of contents.

#### table\_of\_contents [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents.table_of_contents "Permanent link")

```
table_of_contents = reactive[Optional[]](
    None, init=False
)
```

Underlying data to populate the table of contents widget.

#### rebuild\_table\_of\_contents [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents.rebuild_table_of_contents "Permanent link")

```
rebuild_table_of_contents()
```

Rebuilds the tree representation of the table of contents data.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ##### `table_of_contents` [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents.rebuild_table_of_contents\(table_of_contents\) "Permanent link") |  | Table of contents. | *required* |

#### watch\_table\_of\_contents [¶](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownTableOfContents.watch_table_of_contents "Permanent link")

```
watch_table_of_contents(table_of_contents)
```

Triggered when the table of contents changes.