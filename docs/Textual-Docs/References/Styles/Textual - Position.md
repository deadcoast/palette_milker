---
title: "Textual - Position"
source: "https://textual.textualize.io/styles/position/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Position¶

The `position` style modifies what [`offset`](https://textual.textualize.io/styles/offset/) is applied to. The default for `position` is `"relative"`, which means the offset is applied to the normal position of the widget. In other words, if `offset` is (1, 1), then the widget will be moved 1 cell and 1 line down from its usual position.

The alternative value of `position` is `"absolute"`. With absolute positioning, the offset is relative to the origin (i.e. the top left of the container). So a widget with offset (1, 1) and absolute positioning will be 1 cell and 1 line down from the top left corner.

Note

Absolute positioning takes precedence over the parent's alignment rule.

## Syntax¶

```
position: <position>;
```

## Examples¶

Two labels, the first is absolute positioned and is displayed relative to the top left of the screen. The second label is relative and is displayed offset from the center.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Label

class PositionApp(App):
    CSS_PATH = "position.tcss"

    def compose(self) -> ComposeResult:
        yield Label("Absolute", id="label1")
        yield Label("Relative", id="label2")

if __name__ == "__main__":
    app = PositionApp()
    app.run()
```

```
Screen {
    align: center middle;
}

Label {
    padding: 1;
    background: $panel;
    border: thick $border;
}

Label#label1 {
    position: absolute;
    offset: 2 1;
}

Label#label2 {
    position: relative;
    offset: 2 1;
}
```

## CSS¶

```
position: relative;
position: absolute;
```

## Python¶

```
widget.styles.position = "relative"
widget.styles.position = "absolute"
```