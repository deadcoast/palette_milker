---
title: "Textual - ProgressBar"
source: "https://textual.textualize.io/widgets/progress_bar/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## ProgressBar¶

A widget that displays progress on a time-consuming task.

- Focusable
- Container

## Examples¶

### Progress Bar in Isolation¶

The example below shows a progress bar in isolation. It shows the progress bar in:

- its indeterminate state, when the `total` progress hasn't been set yet;
- the middle of the progress; and
- the completed state.

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Center, Middle
from textual.timer import Timer
from textual.widgets import Footer, ProgressBar

class IndeterminateProgressBar(App[None]):
    BINDINGS = [("s", "start", "Start")]

    progress_timer: Timer
    """Timer to simulate progress happening."""

    def compose(self) -> ComposeResult:
        with Center():
            with Middle():
                yield ProgressBar()
        yield Footer()

    def on_mount(self) -> None:
        """Set up a timer to simulate progess happening."""
        self.progress_timer = self.set_interval(1 / 10, self.make_progress, pause=True)

    def make_progress(self) -> None:
        """Called automatically to advance the progress bar."""
        self.query_one(ProgressBar).advance(1)

    def action_start(self) -> None:
        """Start the progress tracking."""
        self.query_one(ProgressBar).update(total=100)
        self.progress_timer.resume()

if __name__ == "__main__":
    IndeterminateProgressBar().run()
```

### Complete App Example¶

The example below shows a simple app with a progress bar that is keeping track of a fictitious funding level for an organisation.

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Center, VerticalScroll
from textual.widgets import Button, Header, Input, Label, ProgressBar

class FundingProgressApp(App[None]):
    CSS_PATH = "progress_bar.tcss"

    TITLE = "Funding tracking"

    def compose(self) -> ComposeResult:
        yield Header()
        with Center():
            yield Label("Funding: ")
            yield ProgressBar(total=100, show_eta=False)  
        with Center():
            yield Input(placeholder="$$$")
            yield Button("Donate")

        yield VerticalScroll(id="history")

    def on_button_pressed(self) -> None:
        self.add_donation()

    def on_input_submitted(self) -> None:
        self.add_donation()

    def add_donation(self) -> None:
        text_value = self.query_one(Input).value
        try:
            value = int(text_value)
        except ValueError:
            return
        self.query_one(ProgressBar).advance(value)
        self.query_one(VerticalScroll).mount(Label(f"Donation for ${value} received!"))
        self.query_one(Input).value = ""

if __name__ == "__main__":
    FundingProgressApp().run()
```

1. We create a progress bar with a total of `100` steps and we hide the ETA countdown because we are not keeping track of a continuous, uninterrupted task.

```
Container {
    overflow: hidden hidden;
    height: auto;
}

Center {
    margin-top: 1;
    margin-bottom: 1;
    layout: horizontal;
}

ProgressBar {
    padding-left: 3;
}

Input {
    width: 16;
}

VerticalScroll {
    height: auto;
}
```

### Gradient Bars¶

Progress bars support an optional `gradient` parameter, which renders a smooth gradient rather than a solid bar. To use a gradient, create and set a [Gradient](https://textual.textualize.io/api/color/#textual.color.Gradient " Gradient") object on the ProgressBar widget.

Note

Setting a gradient will override styles set in CSS.

Here's an example:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.color import Gradient
from textual.containers import Center, Middle
from textual.widgets import ProgressBar

class ProgressApp(App[None]):
    """Progress bar with a rainbow gradient."""

    def compose(self) -> ComposeResult:
        gradient = Gradient.from_colors(
            "#881177",
            "#aa3355",
            "#cc6666",
            "#ee9944",
            "#eedd00",
            "#99dd55",
            "#44dd88",
            "#22ccbb",
            "#00bbcc",
            "#0099cc",
            "#3366bb",
            "#663399",
        )
        with Center():
            with Middle():
                yield ProgressBar(total=100, gradient=gradient)

    def on_mount(self) -> None:
        self.query_one(ProgressBar).update(progress=70)

if __name__ == "__main__":
    ProgressApp().run()
```

### Custom Styling¶

This shows a progress bar with custom styling. Refer to the [section below](https://textual.textualize.io/widgets/progress_bar/#styling-the-progress-bar) for more information.

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Center, Middle
from textual.timer import Timer
from textual.widgets import Footer, ProgressBar

class StyledProgressBar(App[None]):
    BINDINGS = [("s", "start", "Start")]
    CSS_PATH = "progress_bar_styled.tcss"

    progress_timer: Timer
    """Timer to simulate progress happening."""

    def compose(self) -> ComposeResult:
        with Center():
            with Middle():
                yield ProgressBar()
        yield Footer()

    def on_mount(self) -> None:
        """Set up a timer to simulate progress happening."""
        self.progress_timer = self.set_interval(1 / 10, self.make_progress, pause=True)

    def make_progress(self) -> None:
        """Called automatically to advance the progress bar."""
        self.query_one(ProgressBar).advance(1)

    def action_start(self) -> None:
        """Start the progress tracking."""
        self.query_one(ProgressBar).update(total=100)
        self.progress_timer.resume()

if __name__ == "__main__":
    StyledProgressBar().run()
```

```
Bar > .bar--indeterminate {
    color: $primary;
    background: $secondary;
}

Bar > .bar--bar {
    color: $primary;
    background: $primary 30%;
}

Bar > .bar--complete {
    color: $error;
}

PercentageStatus {
    text-style: reverse;
    color: $secondary;
}

ETAStatus {
    text-style: underline;
}
```

## Styling the Progress Bar¶

The progress bar is composed of three sub-widgets that can be styled independently:

| Widget name | ID | Description |
| --- | --- | --- |
| `Bar` | `#bar` | The bar that visually represents the progress made. |
| `PercentageStatus` | `#percentage` | [Label](https://textual.textualize.io/widgets/label/) that shows the percentage of completion. |
| `ETAStatus` | `#eta` | [Label](https://textual.textualize.io/widgets/label/) that shows the estimated time to completion. |

### Bar Component Classes¶

The bar sub-widget provides the component classes that follow.

These component classes let you modify the foreground and background color of the bar in its different states.

| Class | Description |
| --- | --- |
| `bar--bar` | Style of the bar (may be used to change the color). |
| `bar--complete` | Style of the bar when it's complete. |
| `bar--indeterminate` | Style of the bar when it's in an indeterminate state. |

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `percentage` | `float  \| None` | The read-only percentage of progress that has been made. This is `None` if the `total` hasn't been set. |  |
| `progress` | `float` | `0` | The number of steps of progress already made. |
| `total` | `float  \| None` | The total number of steps that we are keeping track of. |  |

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A progress bar widget.

The progress bar uses "steps" as the measurement unit.

Example
```
class MyApp(App):
    def compose(self):
        yield ProgressBar(total=100)

    def key_space(self):
        self.query_one(ProgressBar).advance(5)
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `total` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(total\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The total number of steps in the progress if known. | `None` |
| ## `show_bar` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(show_bar\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to show the bar portion of the progress bar. | `True` |
| ## `show_percentage` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(show_percentage\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to show the percentage status of the bar. | `True` |
| ## `show_eta` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(show_eta\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to show the ETA countdown of the progress bar. | `True` |
| ## `name` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |
| ## `clock` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(clock\) "Permanent link") | `Clock \| None` | An optional clock object (leave as default unless testing). | `None` |
| ## `gradient` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar\(gradient\) "Permanent link") | `[Gradient](https://textual.textualize.io/api/color/#textual.color.Gradient " Gradient (textual.color.Gradient)") \| None` | An optional Gradient object (will replace CSS styles in the bar). | `None` |

## gradient [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.gradient "Permanent link")

```
gradient = reactive(None)
```

Optional gradient object (will replace CSS styling in bar).

## percentage [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.percentage "Permanent link")

```
percentage = reactive[Optional[float]](None)
```

The percentage of progress that has been completed.

The percentage is a value between 0 and 1 and the returned value is only `None` if the total progress of the bar hasn't been set yet.

Example
```
progress_bar = ProgressBar()
print(progress_bar.percentage)  # None
progress_bar.update(total=100)
progress_bar.advance(50)
print(progress_bar.percentage)  # 0.5
```

## progress [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.progress "Permanent link")

```
progress = reactive(0.0)
```

The progress so far, in number of steps.

## total [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.total "Permanent link")

```
total =
```

The total number of steps associated with this progress bar, when known.

The value `None` will render an indeterminate progress bar.

## advance [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.advance "Permanent link")

```
advance(=1)
```

Advance the progress of the progress bar by the given amount.

Example
```
progress_bar.advance(10)  # Advance 10 steps.
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `advance` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.advance\(advance\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Number of steps to advance progress by. | `1` |

## update [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.update "Permanent link")

```
update(*, =UNUSED, =UNUSED, =UNUSED)
```

Update the progress bar with the given options.

Example
```
progress_bar.update(
    total=200,  # Set new total to 200 steps.
    progress=50,  # Set the progress to 50 (out of 200).
)
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `total` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.update\(total\) "Permanent link") | `None \| [float](https://docs.python.org/3/library/functions.html#float) \| [UnusedParameter](https://textual.textualize.io/api/types/#textual.types.UnusedParameter " UnusedParameter (textual._types.UnusedParameter)")` | New total number of steps. | `UNUSED` |
| ### `progress` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.update\(progress\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| [UnusedParameter](https://textual.textualize.io/api/types/#textual.types.UnusedParameter " UnusedParameter (textual._types.UnusedParameter)")` | Set the progress to the given number of steps. | `UNUSED` |
| ### `advance` [¶](https://textual.textualize.io/widgets/progress_bar/#textual.widgets.ProgressBar.update\(advance\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| [UnusedParameter](https://textual.textualize.io/api/types/#textual.types.UnusedParameter " UnusedParameter (textual._types.UnusedParameter)")` | Advance the progress by this number of steps. | `UNUSED` |