---
title: "Textual - textual.scrollbar"
source: "https://textual.textualize.io/api/scrollbar/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.scrollbar

Contains the widgets that manage Textual scrollbars.

Note

You will not typically need this for most apps.

## ScrollBar [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBar "Permanent link")

```
ScrollBar(vertical=True, name=None, *, thickness=1)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

### renderer [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBar.renderer "Permanent link")

```
renderer =
```

The class used for rendering scrollbars. This can be overridden and set to a ScrollBarRender-derived class in order to delegate all scrollbar rendering to that class. E.g.:

```
class MyScrollBarRender(ScrollBarRender): ...

app = MyApp()
ScrollBar.renderer = MyScrollBarRender
app.run()
```

Because this variable is accessed through specific instances (rather than through the class ScrollBar itself) it is also possible to set this on specific scrollbar instance to change only that instance:

```
my_widget.horizontal_scrollbar.renderer = MyScrollBarRender
```

### action\_grab [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBar.action_grab "Permanent link")

```
action_grab()
```

Begin capturing the mouse cursor.

### action\_scroll\_down [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBar.action_scroll_down "Permanent link")

```
action_scroll_down()
```

Scroll vertical scrollbars down, horizontal scrollbars right.

### action\_scroll\_up [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBar.action_scroll_up "Permanent link")

```
action_scroll_up()
```

Scroll vertical scrollbars up, horizontal scrollbars left.

## ScrollBarCorner [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBarCorner "Permanent link")

```
ScrollBarCorner(
    *children,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

Widget which fills the gap between horizontal and vertical scrollbars, should they both be present.

## ScrollBarRender [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBarRender "Permanent link")

```
ScrollBarRender(
    virtual_size=100,
    window_size=0,
    position=0,
    thickness=1,
    vertical=True,
    style="bright_magenta on #555555",
)
```

### BLANK\_GLYPH [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBarRender.BLANK_GLYPH "Permanent link")

```
BLANK_GLYPH = ' '
```

Glyph used for the main body of the scrollbar

### HORIZONTAL\_BARS [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBarRender.HORIZONTAL_BARS "Permanent link")

```
HORIZONTAL_BARS = ['▉', '▊', '▋', '▌', '▍', '▎', '▏', ' ']
```

Glyphs used for horizontal scrollbar ends, for smoother display.

### VERTICAL\_BARS [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollBarRender.VERTICAL_BARS "Permanent link")

```
VERTICAL_BARS = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', ' ']
```

Glyphs used for vertical scrollbar ends, for smoother display.

## ScrollDown [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollDown "Permanent link")

```
ScrollDown()
```

Bases:

Message sent when clicking below handle.

## ScrollLeft [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollLeft "Permanent link")

```
ScrollLeft()
```

Bases:

Message sent when clicking above handle.

## ScrollMessage [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollMessage "Permanent link")

```
ScrollMessage()
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Base class for all scrollbar messages.

## ScrollRight [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollRight "Permanent link")

```
ScrollRight()
```

Bases:

Message sent when clicking below handle.

## ScrollTo [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollTo "Permanent link")

```
ScrollTo(x=None, y=None, animate=True)
```

Bases:

Message sent when click and dragging handle.

## ScrollUp [¶](https://textual.textualize.io/api/scrollbar/#textual.scrollbar.ScrollUp "Permanent link")

```
ScrollUp()
```

Bases:

Message sent when clicking above handle.