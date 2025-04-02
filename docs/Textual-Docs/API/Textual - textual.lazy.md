---
title: "Textual - textual.lazy"
source: "https://textual.textualize.io/api/lazy/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.lazy

Tools for lazy loading widgets.

## Lazy [¶](https://textual.textualize.io/api/lazy/#textual.lazy.Lazy "Permanent link")

```
Lazy()
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

Wraps a widget so that it is mounted *lazily*.

Lazy widgets are mounted after the first refresh. This can be used to display some parts of the UI very quickly, followed by the lazy widgets. Technically, this won't make anything faster, but it reduces the time the user sees a blank screen and will make apps feel more responsive.

Making a widget lazy is beneficial for widgets which start out invisible, such as tab panes.

Note that since lazy widgets aren't mounted immediately (by definition), they will not appear in queries for a brief interval until they are mounted. Your code should take this into account.

Example
```
def compose(self) -> ComposeResult:
    yield Footer()
    with ColorTabs("Theme Colors", "Named Colors"):
        yield Content(ThemeColorButtons(), ThemeColorsView(), id="theme")
        yield Lazy(NamedColorsView())
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `widget` [¶](https://textual.textualize.io/api/lazy/#textual.lazy.Lazy\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A widget that should be mounted after a refresh. | *required* |

## Reveal [¶](https://textual.textualize.io/api/lazy/#textual.lazy.Reveal "Permanent link")

```
Reveal(widget)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

Similar to , but mounts children sequentially.

This is useful when you have so many child widgets that there is a noticeable delay before you see anything. By mounting the children over several frames, the user will feel that something is happening.

Example
```
def compose(self) -> ComposeResult:
    with lazy.Reveal(containers.VerticalScroll(can_focus=False)):
        yield Markdown(WIDGETS_MD, classes="column")
        yield Buttons()
        yield Checkboxes()
        yield Datatables()
        yield Inputs()
        yield ListViews()
        yield Logs()
        yield Sparklines()
    yield Footer()
```