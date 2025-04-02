---
title: "Textual - Style Inline Apps"
source: "https://textual.textualize.io/how-to/style-inline-apps/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Style Inline Apps¶

Version 0.55.0 of Textual added support for running apps *inline* (below the prompt). Running an inline app is as simple as adding `inline=True` to [`run()`](https://textual.textualize.io/api/app/#textual.app.App.run " run").

![](https://www.youtube.com/watch?v=dxAf3vDr4aQ)

Your apps will typically run inline without modification, but you may want to make some tweaks for inline mode, which you can do with a little CSS. This How-To will explain how.

Let's look at an inline app. The following app displays the the current time (and keeps it up to date).

```
from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits

class ClockApp(App):
    CSS = """
    Screen {
        align: center middle;
    }
    #clock {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Digits("", id="clock")

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")

if __name__ == "__main__":
    app = ClockApp()
    app.run(inline=True)
```

With Textual's default settings, this clock will be displayed in 5 lines; 3 for the digits and 2 for a top and bottom border.

You can change the height or the border with CSS and the `:inline` pseudo-selector, which only matches rules in inline mode. Let's update this app to remove the default border, and increase the height:

```
from datetime import datetime

from textual.app import App, ComposeResult
from textual.widgets import Digits

class ClockApp(App):
    CSS = """
    Screen {
        align: center middle;
        &:inline {
            border: none;
            height: 50vh;
            Digits {
                color: $success;
            }
        }
    }
    #clock {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Digits("", id="clock")

    def on_ready(self) -> None:
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        clock = datetime.now().time()
        self.query_one(Digits).update(f"{clock:%T}")

if __name__ == "__main__":
    app = ClockApp()
    app.run(inline=True)
```

The highlighted CSS targets online inline mode. By setting the `height` rule on Screen we can define how many lines the app should consume when it runs. Setting `border: none` removes the default border when running in inline mode.

We've also added a rule to change the color of the clock when running inline.

## Summary¶

Most apps will not require modification to run inline, but if you want to tweak the height and border you can write CSS that targets inline mode with the `:inline` pseudo-selector.