---
title: "Textual - Log"
source: "https://textual.textualize.io/widgets/log/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Log¶

Added in version 0.32.0

A Log widget displays lines of text which may be appended to in realtime.

Call to write a line at a time, or to write multiple lines at once. Call to clear the Log widget.

Tip

See also [RichLog](https://textual.textualize.io/widgets/rich_log/) which can write more than just text, and supports a number of advanced features.

- Focusable
- Container

## Example¶

The example below shows how to write text to a `Log` widget:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Log

TEXT = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain."""

class LogApp(App):
    """An app with a simple log."""

    def compose(self) -> ComposeResult:
        yield Log()

    def on_ready(self) -> None:
        log = self.query_one(Log)
        log.write_line("Hello, World!")
        for _ in range(10):
            log.write_line(TEXT)

if __name__ == "__main__":
    app = LogApp()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `max_lines` | `int` | `None` | Maximum number of lines in the log or `None` for no maximum. |
| `auto_scroll` | `bool` | `False` | Scroll to end of log when new lines are added. |

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[ScrollView](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView " ScrollView (textual.scroll_view.ScrollView)")`

A widget to log text.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `highlight` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log\(highlight\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable highlighting. | `False` |
| ## `max_lines` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log\(max_lines\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | Maximum number of lines to display. | `None` |
| ## `auto_scroll` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log\(auto_scroll\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Scroll to end on new lines. | `True` |
| ## `name` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the text log. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the text log in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the text log. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the text log is disabled or not. | `False` |

## auto\_scroll [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.auto_scroll "Permanent link")

```
auto_scroll =
```

Automatically scroll to new lines.

## highlight [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.highlight "Permanent link")

```
highlight =
```

Enable highlighting.

## highlighter [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.highlighter "Permanent link")

```
highlighter = ReprHighlighter()
```

The Rich Highlighter object to use, if `highlight=True`

## line\_count [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.line_count "Permanent link")

```
line_count
```

Number of lines of content.

## lines [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.lines "Permanent link")

```
lines
```

The raw lines in the Log.

Note that this attribute is read only. Changing the lines will not update the Log's contents.

## max\_lines [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.max_lines "Permanent link")

```
max_lines =
```

Maximum number of lines to show

## clear [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.clear "Permanent link")

```
clear()
```

Clear the Log.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Log` instance. |

## get\_selection [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.get_selection "Permanent link")

```
get_selection(selection)
```

Get the text under the selection.

```
Args:
        selection: Selection information.

    Returns:
        Tuple of extracted text and ending (typically "
```

" or " "), or `None` if no text could be extracted.

## notify\_style\_update [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.notify_style_update "Permanent link")

```
notify_style_update()
```

Called by Textual when styles update.

## refresh\_lines [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.refresh_lines "Permanent link")

```
refresh_lines(, =1)
```

Refresh one or more lines.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `y_start` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.refresh_lines\(y_start\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | First line to refresh. | *required* |
| ### `line_count` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.refresh_lines\(line_count\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Total number of lines to refresh. | `1` |

## write [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.write "Permanent link")

```
write(, =None)
```

Write to the log.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `data` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.write\(data\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Data to write. | *required* |
| ### `scroll_end` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.write\(scroll_end\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Scroll to the end after writing, or `None` to use `self.auto_scroll`. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Log` instance. |

## write\_line [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.write_line "Permanent link")

```
write_line(, =None)
```

Write content on a new line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `line` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.write_line\(line\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | String to write to the log. | *required* |
| ### `scroll_end` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.write_line\(scroll_end\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Scroll to the end after writing, or `None` to use `self.auto_scroll`. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Log` instance. |

## write\_lines [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.write_lines "Permanent link")

```
write_lines(, =None)
```

Write an iterable of lines.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `lines` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.write_lines\(lines\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[str](https://docs.python.org/3/library/stdtypes.html#str)]` | An iterable of strings to write. | *required* |
| ### `scroll_end` [¶](https://textual.textualize.io/widgets/log/#textual.widgets.Log.write_lines\(scroll_end\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Scroll to the end after writing, or `None` to use `self.auto_scroll`. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Log` instance. |