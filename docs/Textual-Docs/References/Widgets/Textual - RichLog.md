---
title: "Textual - RichLog"
source: "https://textual.textualize.io/widgets/rich_log/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## RichLog¶

A RichLog is a widget which displays scrollable content that may be appended to in realtime.

Call with a string or [Rich Renderable](https://rich.readthedocs.io/en/latest/protocol.html) to write content to the end of the RichLog. Call to clear the content.

Tip

See also [Log](https://textual.textualize.io/widgets/log/) which is an alternative to `RichLog` but specialized for simple text.

- Focusable
- Container

## Example¶

The example below shows an application showing a `RichLog` with different kinds of data logged.

<!-- SVG content removed by SVG Remover -->

```
import csv
import io

from rich.syntax import Syntax
from rich.table import Table

from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog

CSV = """lane,swimmer,country,time
4,Joseph Schooling,Singapore,50.39
2,Michael Phelps,United States,51.14
5,Chad le Clos,South Africa,51.14
6,László Cseh,Hungary,51.14
3,Li Zhuhao,China,51.26
8,Mehdy Metella,France,51.58
7,Tom Shields,United States,51.73
1,Aleksandr Sadovnikov,Russia,51.84"""

CODE = '''\
def loop_first_last(values: Iterable[T]) -> Iterable[tuple[bool, bool, T]]:
    """Iterate and generate a tuple with a flag for first and last value."""
    iter_values = iter(values)
    try:
        previous_value = next(iter_values)
    except StopIteration:
        return
    first = True
    for value in iter_values:
        yield first, False, previous_value
        first = False
        previous_value = value
    yield first, True, previous_value\
'''

class RichLogApp(App):
    def compose(self) -> ComposeResult:
        yield RichLog(highlight=True, markup=True)

    def on_ready(self) -> None:
        """Called  when the DOM is ready."""
        text_log = self.query_one(RichLog)

        text_log.write(Syntax(CODE, "python", indent_guides=True))

        rows = iter(csv.reader(io.StringIO(CSV)))
        table = Table(*next(rows))
        for row in rows:
            table.add_row(*row)

        text_log.write(table)
        text_log.write("[bold magenta]Write text or any Rich renderable!")

    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""
        text_log = self.query_one(RichLog)
        text_log.write(event)

if __name__ == "__main__":
    app = RichLogApp()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `highlight` | `bool` | `False` | Automatically highlight content. |
| `markup` | `bool` | `False` | Apply markup. |
| `max_lines` | `int` | `None` | Maximum number of lines in the log or `None` for no maximum. |
| `min_width` | `int` | 78 | Minimum width of renderables. |
| `wrap` | `bool` | `False` | Enable word wrapping. |

## Messages¶

This widget sends no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[ScrollView](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView " ScrollView (textual.scroll_view.ScrollView)")`

A widget for logging Rich renderables and text.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `max_lines` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(max_lines\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | Maximum number of lines in the log or `None` for no maximum. | `None` |
| ## `min_width` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(min_width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Width to use for calls to `write` with no specified `width`. | `78` |
| ## `wrap` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(wrap\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable word wrapping (default is off). | `False` |
| ## `highlight` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(highlight\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Automatically highlight content. By default, the `ReprHighlighter` is used. To customize highlighting, set `highlight=True` and then set the `highlighter` attribute to an instance of `Highlighter`. | `False` |
| ## `markup` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(markup\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Apply Rich console markup. | `False` |
| ## `auto_scroll` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(auto_scroll\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable automatic scrolling to end. | `True` |
| ## `name` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the text log. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the text log in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the text log. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the text log is disabled or not. | `False` |

## auto\_scroll [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.auto_scroll "Permanent link")

```
auto_scroll =
```

Automatically scroll to the end on write.

## highlight [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.highlight "Permanent link")

```
highlight =
```

Automatically highlight content.

## highlighter [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.highlighter "Permanent link")

```
highlighter = ReprHighlighter()
```

Rich Highlighter used to highlight content when highlight is True

## lines [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.lines "Permanent link")

```
lines = []
```

The lines currently visible in the log.

## markup [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.markup "Permanent link")

```
markup =
```

Apply Rich console markup.

## max\_lines [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.max_lines "Permanent link")

```
max_lines =
```

Maximum number of lines in the log or `None` for no maximum.

## min\_width [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.min_width "Permanent link")

```
min_width =
```

Minimum width of renderables.

## wrap [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.wrap "Permanent link")

```
wrap =
```

Enable word wrapping.

## clear [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.clear "Permanent link")

```
clear()
```

Clear the text log.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `RichLog` instance. |

## write [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.write "Permanent link")

```
write(
    ,
    =None,
    =False,
    =True,
    =None,
    =False,
)
```

Write a string or a Rich renderable to the bottom of the log.

Notes

The rendering of content will be deferred until the size of the `RichLog` is known. This means if you call `write` in `compose` or `on_mount`, the content will not be rendered immediately.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `content` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.write\(content\) "Permanent link") | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| [object](https://docs.python.org/3/library/functions.html#object)` | Rich renderable (or a string). | *required* |
| ### `width` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.write\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | Width to render, or `None` to use `RichLog.min_width`. If specified, `expand` and `shrink` will be ignored. | `None` |
| ### `expand` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.write\(expand\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Permit expanding of content to the width of the content region of the RichLog. If `width` is specified, then `expand` will be ignored. | `False` |
| ### `shrink` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.write\(shrink\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Permit shrinking of content to fit within the content region of the RichLog. If `width` is specified, then `shrink` will be ignored. | `True` |
| ### `scroll_end` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.write\(scroll_end\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Enable automatic scroll to end, or `None` to use `self.auto_scroll`. | `None` |
| ### `animate` [¶](https://textual.textualize.io/widgets/rich_log/#textual.widgets.RichLog.write\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable animation if the log will scroll. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `RichLog` instance. |