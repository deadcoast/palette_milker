---
title: "Textual - textual.renderables"
source: "https://textual.textualize.io/api/renderables/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.renderables

A collection of Rich renderables which may be returned from a widget's [`render()`](https://textual.textualize.io/api/widget/#textual.widget.Widget.render " render") method.

## Bar [¶](https://textual.textualize.io/api/renderables/#textual.renderables.bar.Bar "Permanent link")

```
Bar(
    =(0, 0),
    ="magenta",
    ="grey37",
    clickable_ranges=None,
    =None,
    =None,
)
```

Thin horizontal bar with a portion highlighted.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `highlight_range` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.bar.Bar\(highlight_range\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[float](https://docs.python.org/3/library/functions.html#float), [float](https://docs.python.org/3/library/functions.html#float)]` | The range to highlight. | `(0, 0)` |
| ### `highlight_style` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.bar.Bar\(highlight_style\) "Permanent link") | `StyleType` | The style of the highlighted range of the bar. | `'magenta'` |
| ### `background_style` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.bar.Bar\(background_style\) "Permanent link") | `StyleType` | The style of the non-highlighted range(s) of the bar. | `'grey37'` |
| ### `width` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.bar.Bar\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The width of the bar, or `None` to fill available width. | `None` |
| ### `gradient` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.bar.Bar\(gradient\) "Permanent link") | `[Gradient](https://textual.textualize.io/api/color/#textual.color.Gradient " Gradient (textual.color.Gradient)") \| None` | Optional gradient object. | `None` |

## Blank [¶](https://textual.textualize.io/api/renderables/#textual.renderables.blank.Blank "Permanent link")

```
Blank(color='transparent')
```

Draw solid background color.

## Digits [¶](https://textual.textualize.io/api/renderables/#textual.renderables.digits.Digits "Permanent link")

```
Digits(, ='')
```

Renders a 3X3 unicode 'font' for numerical values.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.digits.Digits\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Text to display. | *required* |
| ### `style` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.digits.Digits\(style\) "Permanent link") | `StyleType` | Style to apply to the digits. | `''` |

### get\_width [¶](https://textual.textualize.io/api/renderables/#textual.renderables.digits.Digits.get_width "Permanent link")

```
get_width()
```

Calculate the width without rendering.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `text` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.digits.Digits.get_width\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Text which may be displayed in the `Digits` widget. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | width of the text (in cells). |

## LinearGradient [¶](https://textual.textualize.io/api/renderables/#textual.renderables.gradient.LinearGradient "Permanent link")

```
LinearGradient(, )
```

Render a linear gradient with a rotation.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `angle` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.gradient.LinearGradient\(angle\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Angle of rotation in degrees. | *required* |
| ### `stops` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.gradient.LinearGradient\(stops\) "Permanent link") | `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[float](https://docs.python.org/3/library/functions.html#float), [Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)") \| [str](https://docs.python.org/3/library/stdtypes.html#str)]]` | List of stop consisting of pairs of offset (between 0 and 1) and color. | *required* |

## VerticalGradient [¶](https://textual.textualize.io/api/renderables/#textual.renderables.gradient.VerticalGradient "Permanent link")

```
VerticalGradient(color1, color2)
```

Draw a vertical gradient.

## Sparkline [¶](https://textual.textualize.io/api/renderables/#textual.renderables.sparkline.Sparkline "Permanent link")

```
Sparkline(
    ,
    *,
    ,
    =from_rgb(0, 255, 0),
    =from_rgb(255, 0, 0),
    =max
)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[T]`

A sparkline representing a series of data.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `data` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.sparkline.Sparkline\(data\) "Permanent link") | `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")[T]` | The sequence of data to render. | *required* |
| ### `width` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.sparkline.Sparkline\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The width of the sparkline/the number of buckets to partition the data into. | *required* |
| ### `min_color` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.sparkline.Sparkline\(min_color\) "Permanent link") | `[Color](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color "rich.color.Color")` | The color of values equal to the min value in data. | `[from_rgb](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color.from_rgb "rich.color.Color.from_rgb")(0, 255, 0)` |
| ### `max_color` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.sparkline.Sparkline\(max_color\) "Permanent link") | `[Color](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color "rich.color.Color")` | The color of values equal to the max value in data. | `[from_rgb](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color.from_rgb "rich.color.Color.from_rgb")(255, 0, 0)` |
| ### `summary_function` [¶](https://textual.textualize.io/api/renderables/#textual.renderables.sparkline.Sparkline\(summary_function\) "Permanent link") | `SummaryFunction[T]` | Function that will be applied to each bucket. | `[max](https://docs.python.org/3/library/functions.html#max)` |