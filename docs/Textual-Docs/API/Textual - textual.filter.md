---
title: "Textual - textual.filter"
source: "https://textual.textualize.io/api/filter/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.filter

Filter classes.

Note

Filters are used internally, and not recommended for use by Textual app developers.

Filters are used internally to process terminal output after it has been rendered. Currently this is used internally to convert the application to monochrome, when the NO\_COLOR env var is set.

In the future, this system will be used to implement accessibility features.

## NO\_DIM [¶](https://textual.textualize.io/api/filter/#textual.filter.NO_DIM "Permanent link")

```
NO_DIM = Style(dim=False)
```

A Style to set dim to False.

## ANSIToTruecolor [¶](https://textual.textualize.io/api/filter/#textual.filter.ANSIToTruecolor "Permanent link")

```
ANSIToTruecolor(, enabled=True)
```

Bases:

Convert ANSI colors to their truecolor equivalents.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `terminal_theme` [¶](https://textual.textualize.io/api/filter/#textual.filter.ANSIToTruecolor\(terminal_theme\) "Permanent link") | `TerminalTheme` | A rich terminal theme. | *required* |

### apply [¶](https://textual.textualize.io/api/filter/#textual.filter.ANSIToTruecolor.apply "Permanent link")

```
apply(, )
```

Transform a list of segments.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `segments` [¶](https://textual.textualize.io/api/filter/#textual.filter.ANSIToTruecolor.apply\(segments\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A list of segments. | *required* |
| #### `background` [¶](https://textual.textualize.io/api/filter/#textual.filter.ANSIToTruecolor.apply\(background\) "Permanent link") | `[Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)")` | The background color. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A new list of segments. |

### truecolor\_style [¶](https://textual.textualize.io/api/filter/#textual.filter.ANSIToTruecolor.truecolor_style "Permanent link")

```
truecolor_style()
```

Replace system colors with truecolor equivalent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `style` [¶](https://textual.textualize.io/api/filter/#textual.filter.ANSIToTruecolor.truecolor_style\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | Style to apply truecolor filter to. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | New style. |

## DimFilter [¶](https://textual.textualize.io/api/filter/#textual.filter.DimFilter "Permanent link")

```
DimFilter(=0.5, enabled=True)
```

Bases:

Replace dim attributes with modified colors.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `dim_factor` [¶](https://textual.textualize.io/api/filter/#textual.filter.DimFilter\(dim_factor\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | The factor to dim by; 0 is 100% background (i.e. invisible), 1.0 is no change. | `0.5` |

### apply [¶](https://textual.textualize.io/api/filter/#textual.filter.DimFilter.apply "Permanent link")

```
apply(, )
```

Transform a list of segments.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `segments` [¶](https://textual.textualize.io/api/filter/#textual.filter.DimFilter.apply\(segments\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A list of segments. | *required* |
| #### `background` [¶](https://textual.textualize.io/api/filter/#textual.filter.DimFilter.apply\(background\) "Permanent link") | `[Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)")` | The background color. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A new list of segments. |

## LineFilter [¶](https://textual.textualize.io/api/filter/#textual.filter.LineFilter "Permanent link")

```
LineFilter(enabled=True)
```

Bases: `[ABC](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")`

Base class for a line filter.

### apply [¶](https://textual.textualize.io/api/filter/#textual.filter.LineFilter.apply "Permanent link")

```
apply(, )
```

Transform a list of segments.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `segments` [¶](https://textual.textualize.io/api/filter/#textual.filter.LineFilter.apply\(segments\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A list of segments. | *required* |
| #### `background` [¶](https://textual.textualize.io/api/filter/#textual.filter.LineFilter.apply\(background\) "Permanent link") | `[Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)")` | The background color. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A new list of segments. |

## Monochrome [¶](https://textual.textualize.io/api/filter/#textual.filter.Monochrome "Permanent link")

```
Monochrome(enabled=True)
```

Bases:

Convert all colors to monochrome.

### apply [¶](https://textual.textualize.io/api/filter/#textual.filter.Monochrome.apply "Permanent link")

```
apply(, )
```

Transform a list of segments.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `segments` [¶](https://textual.textualize.io/api/filter/#textual.filter.Monochrome.apply\(segments\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A list of segments. | *required* |
| #### `background` [¶](https://textual.textualize.io/api/filter/#textual.filter.Monochrome.apply\(background\) "Permanent link") | `[Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)")` | The background color. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A new list of segments. |

## NoColor [¶](https://textual.textualize.io/api/filter/#textual.filter.NoColor "Permanent link")

```
NoColor(enabled=True)
```

Bases:

Remove all color information from segments.

### apply [¶](https://textual.textualize.io/api/filter/#textual.filter.NoColor.apply "Permanent link")

```
apply(, )
```

Transform a list of segments.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `segments` [¶](https://textual.textualize.io/api/filter/#textual.filter.NoColor.apply\(segments\) "Permanent link") | `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A list of segments. | *required* |
| #### `background` [¶](https://textual.textualize.io/api/filter/#textual.filter.NoColor.apply\(background\) "Permanent link") | `[Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)")` | The background color. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Segment](https://rich.readthedocs.io/en/stable/reference/segment.html#rich.segment.Segment "rich.segment.Segment")]` | A new list of segments. |

## dim\_color [¶](https://textual.textualize.io/api/filter/#textual.filter.dim_color "Permanent link")

```
dim_color(, , )
```

Dim a color by blending towards the background

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `background` [¶](https://textual.textualize.io/api/filter/#textual.filter.dim_color\(background\) "Permanent link") | `[Color](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color "rich.color.Color")` | background color. | *required* |
| ### `color` [¶](https://textual.textualize.io/api/filter/#textual.filter.dim_color\(color\) "Permanent link") | `[Color](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color "rich.color.Color")` | Foreground color. | *required* |
| ### `factor` [¶](https://textual.textualize.io/api/filter/#textual.filter.dim_color\(factor\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Blend factor | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Color](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color "rich.color.Color")` | New dimmer color. |

## dim\_style [¶](https://textual.textualize.io/api/filter/#textual.filter.dim_style "Permanent link")

```
dim_style(, background, )
```

Replace dim attribute with a dim color.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `style` [¶](https://textual.textualize.io/api/filter/#textual.filter.dim_style\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | Style to dim. | *required* |
| ### `factor` [¶](https://textual.textualize.io/api/filter/#textual.filter.dim_style\(factor\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Blend factor. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | New dimmed style. |

## monochrome\_style [¶](https://textual.textualize.io/api/filter/#textual.filter.monochrome_style "Permanent link")

```
monochrome_style()
```

Convert colors in a style to monochrome.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `style` [¶](https://textual.textualize.io/api/filter/#textual.filter.monochrome_style\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | A Rich Style. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | A new Rich style. |