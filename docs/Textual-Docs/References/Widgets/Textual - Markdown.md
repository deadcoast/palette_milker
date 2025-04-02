---
title: "Textual - Markdown"
source: "https://textual.textualize.io/widgets/markdown/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Markdown¶

Added in version 0.11.0

A widget to display a Markdown document.

- Focusable
- Container

Tip

See [MarkdownViewer](https://textual.textualize.io/widgets/markdown_viewer/) for a widget that adds additional features such as a Table of Contents.

## Example¶

The following example displays Markdown from a string.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Markdown

EXAMPLE_MARKDOWN = """\
# Markdown Document

This is an example of Textual's \`Markdown\` widget.

## Features

Markdown syntax and extensions are supported.

- Typography *emphasis*, **strong**, \`inline code\` etc.
- Headers
- Lists (bullet and ordered)
- Syntax highlighted code blocks
- Tables!
"""

class MarkdownExampleApp(App):
    def compose(self) -> ComposeResult:
        yield Markdown(EXAMPLE_MARKDOWN)

if __name__ == "__main__":
    app = MarkdownExampleApp()
    app.run()
```

## Reactive Attributes¶

This widget has no reactive attributes.

## Messages¶

## Bindings¶

This widget has no bindings.

## Component Classes¶

The markdown widget provides the following component classes:

These component classes target standard inline markdown styles. Changing these will potentially break the standard markdown formatting.

| Class | Description |
| --- | --- |
| `code_inline` | Target text that is styled as inline code. |
| `em` | Target text that is emphasized inline. |
| `s` | Target text that is styled inline with strikethrough. |
| `strong` | Target text that is styled inline with strong. |

## See Also¶

- [MarkdownViewer](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.MarkdownViewer " MarkdownViewer") code reference

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `markdown` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown\(markdown\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | String containing Markdown or None to leave blank for now. | `None` |
| ## `name` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the widget. | `None` |
| ## `parser_factory` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown\(parser_factory\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[], MarkdownIt] \| None` | A factory function to return a configured MarkdownIt instance. If `None`, a "gfm-like" parser is used. | `None` |
| ## `open_links` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown\(open_links\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Open links automatically. If you set this to `False`, you can handle the [`LinkClicked`](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.Markdown.LinkClicked " LinkClicked") events. | `True` |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.COMPONENT_CLASSES "Permanent link")

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

## code\_dark\_theme [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.code_dark_theme "Permanent link")

```
code_dark_theme = reactive('material')
```

The theme to use for code blocks when the App theme is dark.

## code\_light\_theme [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.code_light_theme "Permanent link")

```
code_light_theme = reactive('material-light')
```

The theme to use for code blocks when the App theme is light.

## LinkClicked [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.LinkClicked "Permanent link")

```
LinkClicked(markdown, href)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

A link in the document was clicked.

### control [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.LinkClicked.control "Permanent link")

```
control
```

The `Markdown` widget containing the link clicked.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### href [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.LinkClicked.href "Permanent link")

```
href = unquote(href)
```

The link that was selected.

### markdown [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.LinkClicked.markdown "Permanent link")

```
markdown = markdown
```

The `Markdown` widget containing the link clicked.

## TableOfContentsSelected [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsSelected "Permanent link")

```
TableOfContentsSelected(markdown, block_id)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

An item in the TOC was selected.

### block\_id [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsSelected.block_id "Permanent link")

```
block_id = block_id
```

ID of the block that was selected.

### control [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsSelected.control "Permanent link")

```
control
```

The `Markdown` widget where the selected item is.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### markdown [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsSelected.markdown "Permanent link")

```
markdown = markdown
```

The `Markdown` widget where the selected item is.

## TableOfContentsUpdated [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsUpdated "Permanent link")

```
TableOfContentsUpdated(markdown, table_of_contents)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

The table of contents was updated.

### control [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsUpdated.control "Permanent link")

```
control
```

The `Markdown` widget associated with the table of contents.

This is an alias for and is used by the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator.

### markdown [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsUpdated.markdown "Permanent link")

```
markdown = markdown
```

The `Markdown` widget associated with the table of contents.

### table\_of\_contents [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.TableOfContentsUpdated.table_of_contents "Permanent link")

```
table_of_contents = table_of_contents
```

Table of contents.

## goto\_anchor [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.goto_anchor "Permanent link")

```
goto_anchor()
```

Try and find the given anchor in the current document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `anchor` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.goto_anchor\(anchor\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The anchor to try and find. | *required* |

Note

The anchor is found by looking at all of the headings in the document and finding the first one whose slug matches the anchor.

Note that the slugging method used is similar to that found on GitHub.

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True when the anchor was found in the current document, False otherwise. |

## load [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.load "Permanent link")

```
load()
```

Load a new Markdown document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `path` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.load\(path\) "Permanent link") | `[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")` | Path to the document. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[OSError](https://docs.python.org/3/library/exceptions.html#OSError)` | If there was some form of error loading the document. |

Note

The exceptions that can be raised by this method are all of those that can be raised by calling [`Path.read_text`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text).

## sanitize\_location [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.sanitize_location "Permanent link")

```
sanitize_location()
```

Given a location, break out the path and any anchor.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `location` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.sanitize_location\(location\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The location to sanitize. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")` | A tuple of the path to the location cleaned of any anchor, plus |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | the anchor (or an empty string if none was found). |

## unhandled\_token [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.unhandled_token "Permanent link")

```
unhandled_token()
```

Process an unhandled token.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `token` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.unhandled_token\(token\) "Permanent link") | `Token` | The MarkdownIt token to handle. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[MarkdownBlock](https://textual.textualize.io/widgets/markdown_viewer/#textual.widgets.markdown.MarkdownBlock " MarkdownBlock (textual.widgets._markdown.MarkdownBlock)") \| None` | Either a widget to be added to the output, or `None`. |

## update [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.update "Permanent link")

```
update()
```

Update the document with new Markdown.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `markdown` [¶](https://textual.textualize.io/widgets/markdown/#textual.widgets.Markdown.update\(markdown\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A string containing Markdown. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An optionally awaitable object. Await this to ensure that all children have been mounted. |