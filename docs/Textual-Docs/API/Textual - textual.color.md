---
title: "Textual - textual.color"
source: "https://textual.textualize.io/api/color/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.color

This module contains a powerful class which Textual uses to manipulate colors.

### Named colors¶

The following named colors are used by the method.

<!-- SVG content removed by SVG Remover -->

## BLACK [¶](https://textual.textualize.io/api/color/#textual.color.BLACK "Permanent link")

```
BLACK = (0, 0, 0)
```

A constant for pure black.

## TRANSPARENT [¶](https://textual.textualize.io/api/color/#textual.color.TRANSPARENT "Permanent link")

```
TRANSPARENT = ('transparent')
```

A constant for transparent.

## WHITE [¶](https://textual.textualize.io/api/color/#textual.color.WHITE "Permanent link")

```
WHITE = (255, 255, 255)
```

A constant for pure white.

## Color [¶](https://textual.textualize.io/api/color/#textual.color.Color "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

A class to represent a color.

Colors are stored as three values representing the degree of red, green, and blue in a color, and a fourth "alpha" value which defines where the color lies on a gradient of opaque to transparent.

Example
```
>>> from textual.color import Color
>>> color = Color.parse("red")
>>> color
Color(255, 0, 0)
>>> color.darken(0.5)
Color(98, 0, 0)
>>> color + Color.parse("green")
Color(0, 128, 0)
>>> color_with_alpha = Color(100, 50, 25, 0.5)
>>> color_with_alpha
Color(100, 50, 25, a=0.5)
>>> color + color_with_alpha
Color(177, 25, 12)
```

### a [¶](https://textual.textualize.io/api/color/#textual.color.Color.a "Permanent link")

```
a = 1.0
```

Alpha (opacity) component in range 0 to 1.

### ansi [¶](https://textual.textualize.io/api/color/#textual.color.Color.ansi "Permanent link")

```
ansi = None
```

ANSI color index. `-1` means default color. `None` if not an ANSI color.

### auto [¶](https://textual.textualize.io/api/color/#textual.color.Color.auto "Permanent link")

```
auto = False
```

Is the color automatic? (automatic colors may be white or black, to provide maximum contrast)

### b [¶](https://textual.textualize.io/api/color/#textual.color.Color.b "Permanent link")

```
b
```

Blue component in range 0 to 255.

### brightness [¶](https://textual.textualize.io/api/color/#textual.color.Color.brightness "Permanent link")

```
brightness
```

The human perceptual brightness.

A value of 1 is returned for pure white, and 0 for pure black. Other colors lie on a gradient between the two extremes.

### clamped [¶](https://textual.textualize.io/api/color/#textual.color.Color.clamped "Permanent link")

```
clamped
```

A clamped color (this color with all values in expected range).

### css [¶](https://textual.textualize.io/api/color/#textual.color.Color.css "Permanent link")

```
css
```

The color in CSS RGB or RGBA form.

For example, `"rgb(10,20,30)"` for an RGB color, or `"rgb(50,70,80,0.5)"` for an RGBA color.

### g [¶](https://textual.textualize.io/api/color/#textual.color.Color.g "Permanent link")

```
g
```

Green component in range 0 to 255.

### hex [¶](https://textual.textualize.io/api/color/#textual.color.Color.hex "Permanent link")

```
hex
```

The color in CSS hex form, with 6 digits for RGB, and 8 digits for RGBA.

For example, `"#46b3de"` for an RGB color, or `"#3342457f"` for a color with alpha.

### hex6 [¶](https://textual.textualize.io/api/color/#textual.color.Color.hex6 "Permanent link")

```
hex6
```

The color in CSS hex form, with 6 digits for RGB. Alpha is ignored.

For example, `"#46b3de"`.

### hsl [¶](https://textual.textualize.io/api/color/#textual.color.Color.hsl "Permanent link")

```
hsl
```

This color in HSL format.

HSL color is an alternative way of representing a color, which can be used in certain color calculations.

Returns:

| Type | Description |
| --- | --- |
|  | Color encoded in HSL format. |

### inverse [¶](https://textual.textualize.io/api/color/#textual.color.Color.inverse "Permanent link")

```
inverse
```

The inverse of this color.

Returns:

| Type | Description |
| --- | --- |
|  | Inverse color. |

### is\_transparent [¶](https://textual.textualize.io/api/color/#textual.color.Color.is_transparent "Permanent link")

```
is_transparent
```

Is the color transparent (i.e. has 0 alpha)?

### monochrome [¶](https://textual.textualize.io/api/color/#textual.color.Color.monochrome "Permanent link")

```
monochrome
```

A monochrome version of this color.

Returns:

| Type | Description |
| --- | --- |
|  | The monochrome (black and white) version of this color. |

### normalized [¶](https://textual.textualize.io/api/color/#textual.color.Color.normalized "Permanent link")

```
normalized
```

A tuple of the color components normalized to between 0 and 1.

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[float](https://docs.python.org/3/library/functions.html#float), [float](https://docs.python.org/3/library/functions.html#float), [float](https://docs.python.org/3/library/functions.html#float)]` | Normalized components. |

### r [¶](https://textual.textualize.io/api/color/#textual.color.Color.r "Permanent link")

```
r
```

Red component in range 0 to 255.

### rgb [¶](https://textual.textualize.io/api/color/#textual.color.Color.rgb "Permanent link")

```
rgb
```

The red, green, and blue color components as a tuple of ints.

### rich\_color [¶](https://textual.textualize.io/api/color/#textual.color.Color.rich_color "Permanent link")

```
rich_color
```

This color encoded in Rich's Color class.

Returns:

| Type | Description |
| --- | --- |
| `[Color](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color "rich.color.Color")` | A color object as used by Rich. |

### automatic [¶](https://textual.textualize.io/api/color/#textual.color.Color.automatic "Permanent link")

```
automatic(alpha_percentage=100.0)
```

Create an automatic color.

### blend [¶](https://textual.textualize.io/api/color/#textual.color.Color.blend "Permanent link")

```
blend(, , =None)
```

Generate a new color between two colors.

This method calculates a new color on a gradient. The position on the gradient is given by `factor`, which is a float between 0 and 1, where 0 is the original color, and 1 is the `destination` color. A value of `gradient` between the two extremes produces a color somewhere between the two end points.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `destination` [¶](https://textual.textualize.io/api/color/#textual.color.Color.blend\(destination\) "Permanent link") |  | Another color. | *required* |
| #### `factor` [¶](https://textual.textualize.io/api/color/#textual.color.Color.blend\(factor\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | A blend factor, 0 -> 1. | *required* |
| #### `alpha` [¶](https://textual.textualize.io/api/color/#textual.color.Color.blend\(alpha\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | New alpha for result. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | A new color. |

### darken [¶](https://textual.textualize.io/api/color/#textual.color.Color.darken "Permanent link")

```
darken(, =None)
```

Darken the color by a given amount.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `amount` [¶](https://textual.textualize.io/api/color/#textual.color.Color.darken\(amount\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Value between 0-1 to reduce luminance by. | *required* |
| #### `alpha` [¶](https://textual.textualize.io/api/color/#textual.color.Color.darken\(alpha\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Alpha component for new color or None to copy alpha. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | New color. |

### from\_hsl [¶](https://textual.textualize.io/api/color/#textual.color.Color.from_hsl "Permanent link")

```
from_hsl(, , )
```

Create a color from HLS components.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `h` [¶](https://textual.textualize.io/api/color/#textual.color.Color.from_hsl\(h\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Hue. | *required* |
| #### `l` [¶](https://textual.textualize.io/api/color/#textual.color.Color.from_hsl\(l\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Lightness. | *required* |
| #### `s` [¶](https://textual.textualize.io/api/color/#textual.color.Color.from_hsl\(s\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Saturation. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new color. |

### from\_rich\_color [¶](https://textual.textualize.io/api/color/#textual.color.Color.from_rich_color "Permanent link")

```
from_rich_color(, =None)
```

Create a new color from Rich's Color class.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `rich_color` [¶](https://textual.textualize.io/api/color/#textual.color.Color.from_rich_color\(rich_color\) "Permanent link") | `[Color](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color "rich.color.Color") \| None` | An instance of [Rich color](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color). | *required* |
| #### `theme` [¶](https://textual.textualize.io/api/color/#textual.color.Color.from_rich_color\(theme\) "Permanent link") | `TerminalTheme \| None` | Optional Rich \[terminal theme\]\[rich.terminal\_theme.TerminalTheme\]. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | A new Color instance. |

### get\_contrast\_text [¶](https://textual.textualize.io/api/color/#textual.color.Color.get_contrast_text "Permanent link")

```
get_contrast_text(=0.95)
```

Get a light or dark color that best contrasts this color, for use with text.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `alpha` [¶](https://textual.textualize.io/api/color/#textual.color.Color.get_contrast_text\(alpha\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | An alpha value to apply to the result. | `0.95` |

Returns:

| Type | Description |
| --- | --- |
|  | A new color, either an off-white or off-black. |

### lighten [¶](https://textual.textualize.io/api/color/#textual.color.Color.lighten "Permanent link")

```
lighten(, =None)
```

Lighten the color by a given amount.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `amount` [¶](https://textual.textualize.io/api/color/#textual.color.Color.lighten\(amount\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | Value between 0-1 to increase luminance by. | *required* |
| #### `alpha` [¶](https://textual.textualize.io/api/color/#textual.color.Color.lighten\(alpha\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | Alpha component for new color or None to copy alpha. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | New color. |

### multiply\_alpha [¶](https://textual.textualize.io/api/color/#textual.color.Color.multiply_alpha "Permanent link")

```
multiply_alpha()
```

Create a new color, multiplying the alpha by a constant.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `alpha` [¶](https://textual.textualize.io/api/color/#textual.color.Color.multiply_alpha\(alpha\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | A value to multiple the alpha by (expected to be in the range 0 to 1). | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new color. |

### parse [¶](https://textual.textualize.io/api/color/#textual.color.Color.parse "Permanent link")

```
parse()
```

Parse a string containing a named color or CSS-style color.

Colors may be parsed from the following formats:

- Text beginning with a `#` is parsed as a hexadecimal color code, where R, G, B, and A must be hexadecimal digits (0-9A-F):

- `#RGB`
- `#RGBA`
- `#RRGGBB`
- `#RRGGBBAA`
- Alternatively, RGB colors can also be specified in the format that follows, where R, G, and B must be numbers between 0 and 255 and A must be a value between 0 and 1:

- `rgb(R,G,B)`
- `rgb(R,G,B,A)`
- The HSL model can also be used, with a syntax similar to the above, if H is a value between 0 and 360, S and L are percentages, and A is a value between 0 and 1:

- `hsl(H,S,L)`
- `hsla(H,S,L,A)`

Any other formats will raise a `ColorParseError`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `color_text` [¶](https://textual.textualize.io/api/color/#textual.color.Color.parse\(color_text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| ` | Text with a valid color format. Color objects will be returned unmodified. | *required* |

Raises:

| Type | Description |
| --- | --- |
|  | If the color is not encoded correctly. |

Returns:

| Type | Description |
| --- | --- |
|  | Instance encoding the color specified by the argument. |

### tint [¶](https://textual.textualize.io/api/color/#textual.color.Color.tint "Permanent link")

```
tint()
```

Apply a tint to a color.

Similar to blend, but combines color and alpha.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `color` [¶](https://textual.textualize.io/api/color/#textual.color.Color.tint\(color\) "Permanent link") |  | A color with alpha component. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New color |

### with\_alpha [¶](https://textual.textualize.io/api/color/#textual.color.Color.with_alpha "Permanent link")

```
with_alpha()
```

Create a new color with the given alpha.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `alpha` [¶](https://textual.textualize.io/api/color/#textual.color.Color.with_alpha\(alpha\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | New value for alpha. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A new color. |

## ColorParseError [¶](https://textual.textualize.io/api/color/#textual.color.ColorParseError "Permanent link")

```
ColorParseError(, =None)
```

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

A color failed to parse.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `message` [¶](https://textual.textualize.io/api/color/#textual.color.ColorParseError\(message\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The error message | *required* |
| ### `suggested_color` [¶](https://textual.textualize.io/api/color/#textual.color.ColorParseError\(suggested_color\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A close color we can suggest. | `None` |

## Gradient [¶](https://textual.textualize.io/api/color/#textual.color.Gradient "Permanent link")

```
Gradient(*stops, =50)
```

Defines a color gradient.

A gradient is defined by a sequence of "stops" consisting of a tuple containing a float and a color. The stop indicates the color at that point on a spectrum between 0 and 1. Colors may be given as a instance, or a string that can be parsed into a Color (with ).

The `quality` argument defines the number of *steps* in the gradient. Intermediate colors are interpolated from the two nearest colors. Increasing `quality` can generate a smoother looking gradient, at the expense of a little extra work to pre-calculate the colors.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `stops` [¶](https://textual.textualize.io/api/color/#textual.color.Gradient\(stops\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[float](https://docs.python.org/3/library/functions.html#float),  \| [str](https://docs.python.org/3/library/stdtypes.html#str)]` | Color stops. | `()` |
| ### `quality` [¶](https://textual.textualize.io/api/color/#textual.color.Gradient\(quality\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of steps in the gradient. | `50` |

Raises:

| Type | Description |
| --- | --- |
| `[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` | If any stops are missing (must be at least a stop for 0 and 1). |

### colors [¶](https://textual.textualize.io/api/color/#textual.color.Gradient.colors "Permanent link")

```
colors
```

A list of colors in the gradient.

### from\_colors [¶](https://textual.textualize.io/api/color/#textual.color.Gradient.from_colors "Permanent link")

```
from_colors(*, =50)
```

Construct a gradient form a sequence of colors, where the stops are evenly spaced.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*colors` [¶](https://textual.textualize.io/api/color/#textual.color.Gradient.from_colors\(*colors\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | Positional arguments may be Color instances or strings to parse into a color. | `()` |
| #### `quality` [¶](https://textual.textualize.io/api/color/#textual.color.Gradient.from_colors\(quality\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of steps in the gradient. | `50` |

Returns:

| Type | Description |
| --- | --- |
|  | A new Gradient instance. |

### get\_color [¶](https://textual.textualize.io/api/color/#textual.color.Gradient.get_color "Permanent link")

```
get_color()
```

Get a color from the gradient at a position between 0 and 1.

Positions that are between stops will return a blended color.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `position` [¶](https://textual.textualize.io/api/color/#textual.color.Gradient.get_color\(position\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | A number between 0 and 1, where 0 is the first stop, and 1 is the last. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A Textual color. |

### get\_rich\_color [¶](https://textual.textualize.io/api/color/#textual.color.Gradient.get_rich_color "Permanent link")

```
get_rich_color()
```

Get a (Rich) color from the gradient at a position between 0 and 1.

Positions that are between stops will return a blended color.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `position` [¶](https://textual.textualize.io/api/color/#textual.color.Gradient.get_rich_color\(position\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | A number between 0 and 1, where 0 is the first stop, and 1 is the last. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Color](https://rich.readthedocs.io/en/stable/reference/color.html#rich.color.Color "rich.color.Color")` | A (Rich) color. |

## HSL [¶](https://textual.textualize.io/api/color/#textual.color.HSL "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

A color in HLS (Hue, Saturation, Lightness) format.

### css [¶](https://textual.textualize.io/api/color/#textual.color.HSL.css "Permanent link")

```
css
```

HSL in css format.

### h [¶](https://textual.textualize.io/api/color/#textual.color.HSL.h "Permanent link")

```
h
```

Hue in range 0 to 1.

### l [¶](https://textual.textualize.io/api/color/#textual.color.HSL.l "Permanent link")

```
l
```

Lightness in range 0 to 1.

### s [¶](https://textual.textualize.io/api/color/#textual.color.HSL.s "Permanent link")

```
s
```

Saturation in range 0 to 1.

## HSV [¶](https://textual.textualize.io/api/color/#textual.color.HSV "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

A color in HSV (Hue, Saturation, Value) format.

### h [¶](https://textual.textualize.io/api/color/#textual.color.HSV.h "Permanent link")

```
h
```

Hue in range 0 to 1.

### s [¶](https://textual.textualize.io/api/color/#textual.color.HSV.s "Permanent link")

```
s
```

Saturation in range 0 to 1.

### v [¶](https://textual.textualize.io/api/color/#textual.color.HSV.v "Permanent link")

```
v
```

Value un range 0 to 1.

## Lab [¶](https://textual.textualize.io/api/color/#textual.color.Lab "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

A color in CIE-L\*ab format.

### L [¶](https://textual.textualize.io/api/color/#textual.color.Lab.L "Permanent link")

```
L
```

Lightness in range 0 to 100.

### a [¶](https://textual.textualize.io/api/color/#textual.color.Lab.a "Permanent link")

```
a
```

A axis in range -127 to 128.

### b [¶](https://textual.textualize.io/api/color/#textual.color.Lab.b "Permanent link")

```
b
```

B axis in range -127 to 128.

## lab\_to\_rgb [¶](https://textual.textualize.io/api/color/#textual.color.lab_to_rgb "Permanent link")

```
lab_to_rgb(lab, alpha=1.0)
```

Convert a CIE-L\*ab color to RGB.

Uses the standard RGB color space with a D65/2⁰ standard illuminant. Conversion passes through the XYZ color space. Cf. http://www.easyrgb.com/en/math.php.

## rgb\_to\_lab [¶](https://textual.textualize.io/api/color/#textual.color.rgb_to_lab "Permanent link")

```
rgb_to_lab(rgb)
```

Convert an RGB color to the CIE-L\*ab format.

Uses the standard RGB color space with a D65/2⁰ standard illuminant. Conversion passes through the XYZ color space. Cf. http://www.easyrgb.com/en/math.php.