---
title: "Textual - Sparkline"
source: "https://textual.textualize.io/widgets/sparkline/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Sparkline¶

Added in version 0.27.0

A widget that is used to visually represent numerical data.

- Focusable
- Container

## Examples¶

### Basic example¶

The example below illustrates the relationship between the data, its length, the width of the sparkline, and the number of bars displayed.

Tip

The sparkline data is split into equally-sized chunks. Each chunk is represented by a bar and the width of the sparkline dictates how many bars there are.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Sparkline

data = [1, 2, 2, 1, 1, 4, 3, 1, 1, 8, 8, 2]  

class SparklineBasicApp(App[None]):
    CSS_PATH = "sparkline_basic.tcss"

    def compose(self) -> ComposeResult:
        yield Sparkline(  
            data,  
            summary_function=max,  
        )

app = SparklineBasicApp()
if __name__ == "__main__":
    app.run()
```

1. We have 12 data points.
2. This sparkline will have its width set to 3 via CSS.
3. The data (12 numbers) will be split across 3 bars, so 4 data points are associated with each bar.
4. Each bar will represent its largest value. The largest value of each chunk is 2, 4, and 8, respectively. That explains why the first bar is half the height of the second and the second bar is half the height of the third.

```
Screen {
    align: center middle;
}

Sparkline {
    width: 3;  
    margin: 2;
}
```

1. By setting the width to 3 we get three buckets.

### Different summary functions¶

The example below shows a sparkline widget with different summary functions. The summary function is what determines the height of each bar.

<!-- SVG content removed by SVG Remover -->

```
import random
from statistics import mean

from textual.app import App, ComposeResult
from textual.widgets import Sparkline

random.seed(73)
data = [random.expovariate(1 / 3) for _ in range(1000)]

class SparklineSummaryFunctionApp(App[None]):
    CSS_PATH = "sparkline.tcss"

    def compose(self) -> ComposeResult:
        yield Sparkline(data, summary_function=max)  
        yield Sparkline(data, summary_function=mean)  
        yield Sparkline(data, summary_function=min)  

app = SparklineSummaryFunctionApp()
if __name__ == "__main__":
    app.run()
```

1. Each bar will show the largest value of that bucket.
2. Each bar will show the mean value of that bucket.
3. Each bar will show the smaller value of that bucket.

```
Sparkline {
    width: 100%;
    margin: 2;
}
```

### Changing the colors¶

The example below shows how to use component classes to change the colors of the sparkline.

<!-- SVG content removed by SVG Remover -->

```
from math import sin

from textual.app import App, ComposeResult
from textual.widgets import Sparkline

class SparklineColorsApp(App[None]):
    CSS_PATH = "sparkline_colors.tcss"

    def compose(self) -> ComposeResult:
        nums = [abs(sin(x / 3.14)) for x in range(0, 360 * 6, 20)]
        yield Sparkline(nums, summary_function=max, id="fst")
        yield Sparkline(nums, summary_function=max, id="snd")
        yield Sparkline(nums, summary_function=max, id="trd")
        yield Sparkline(nums, summary_function=max, id="frt")
        yield Sparkline(nums, summary_function=max, id="fft")
        yield Sparkline(nums, summary_function=max, id="sxt")
        yield Sparkline(nums, summary_function=max, id="svt")
        yield Sparkline(nums, summary_function=max, id="egt")
        yield Sparkline(nums, summary_function=max, id="nnt")
        yield Sparkline(nums, summary_function=max, id="tnt")

app = SparklineColorsApp()
if __name__ == "__main__":
    app.run()
```

```
Sparkline {
    width: 100%;
    margin: 1;
}

#fst > .sparkline--max-color {
    color: $success;
}
#fst > .sparkline--min-color {
    color: $warning;
}

#snd > .sparkline--max-color {
    color: $warning;
}
#snd > .sparkline--min-color {
    color: $success;
}

#trd > .sparkline--max-color {
    color: $error;
}
#trd > .sparkline--min-color {
    color: $warning;
}

#frt > .sparkline--max-color {
    color: $warning;
}
#frt > .sparkline--min-color {
    color: $error;
}

#fft > .sparkline--max-color {
    color: $accent;
}
#fft > .sparkline--min-color {
    color: $accent 30%;
}

#sxt > .sparkline--max-color {
    color: $primary 30%;
}
#sxt > .sparkline--min-color {
    color: $primary;
}

#svt > .sparkline--max-color {
    color: $error;
}
#svt > .sparkline--min-color {
    color: $error 30%;
}

#egt > .sparkline--max-color {
    color: $error 30%;
}
#egt > .sparkline--min-color {
    color: $error;
}

#nnt > .sparkline--max-color {
    color: $success;
}
#nnt > .sparkline--min-color {
    color: $success 30%;
}

#tnt > .sparkline--max-color {
    color: $success 30%;
}
#tnt > .sparkline--min-color {
    color: $success;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `data` | `Sequence[float] \| None` | `None` | The data represented by the sparkline. |
| `summary_function` | `Callable[[Sequence[float]], float]` | `max` | The function that computes the height of each bar. |

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

The sparkline widget provides the following component classes:

Use these component classes to define the two colors that the sparkline interpolates to represent its numerical data.

Note

These two component classes are used exclusively for the *color* of the sparkline widget. Setting any style other than [`color`](https://textual.textualize.io/styles/color.md) will have no effect.

| Class | Description |
| --- | --- |
| `sparkline--max-color` | The color used for the larger values in the data. |
| `sparkline--min-color` | The color used for the smaller values in the data. |

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A sparkline widget to display numerical data.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `data` [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline\(data\) "Permanent link") | `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")[[float](https://docs.python.org/3/library/functions.html#float)] \| None` | The initial data to populate the sparkline with. | `None` |
| ## `min_color` [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline\(min_color\) "Permanent link") | `[Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The color of the minimum value, or `None` to take from CSS. | `None` |
| ## `max_color` [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline\(max_color\) "Permanent link") | `[Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)") \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | the color of the maximum value, or `None` to take from CSS. | `None` |
| ## `summary_function` [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline\(summary_function\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")[[float](https://docs.python.org/3/library/functions.html#float)]], [float](https://docs.python.org/3/library/functions.html#float)] \| None` | Summarizes bar values into a single value used to represent each bar. | `None` |
| ## `name` [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes for the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {
    "sparkline--max-color",
    "sparkline--min-color",
}
```

Use these component classes to define the two colors that the sparkline interpolates to represent its numerical data.

Note

These two component classes are used exclusively for the *color* of the sparkline widget. Setting any style other than [`color`](https://textual.textualize.io/styles/color.md) will have no effect.

| Class | Description |
| --- | --- |
| `sparkline--max-color` | The color used for the larger values in the data. |
| `sparkline--min-color` | The color used for the smaller values in the data. |

## data [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline.data "Permanent link")

```
data =
```

The data that populates the sparkline.

## summary\_function [¶](https://textual.textualize.io/widgets/sparkline/#textual.widgets.Sparkline.summary_function "Permanent link")

```
summary_function = reactive[
    Callable[[Sequence[float]], float]
](_max_factory)
```

The function that computes the value that represents each bar.