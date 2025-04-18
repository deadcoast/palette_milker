---
title: "Textual - <color>"
source: "https://textual.textualize.io/css_types/color/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## <color>¶

The `<color>` CSS type represents a color.

Warning

Not to be confused with the [`color`](https://textual.textualize.io/styles/color/) CSS rule to set text color.

## Syntax¶

A [`<color>`](https://textual.textualize.io/css_types/color/) should be in one of the formats explained in this section. A bullet point summary of the formats available follows:

- a recognised [named color](https://textual.textualize.io/css_types/color/#named-colors) (e.g., `red`);
- a 3 or 6 hexadecimal digit number representing the [RGB values](https://textual.textualize.io/css_types/color/#hex-rgb-value) of the color (e.g., `#F35573`);
- a 4 or 8 hexadecimal digit number representing the [RGBA values](https://textual.textualize.io/css_types/color/#hex-rgba-value) of the color (e.g., `#F35573A0`);
- a color description in the RGB system, [with](https://textual.textualize.io/css_types/color/#rgba-description) or [without](https://textual.textualize.io/css_types/color/#rgb-description) opacity (e.g., `rgb(23, 78, 200)`);
- a color description in the HSL system, [with](https://textual.textualize.io/css_types/color/#hsla-description) or [without](https://textual.textualize.io/css_types/color/#hsl-description) opacity (e.g., `hsl(290, 70%, 80%)`);

[Textual's default themes](https://textual.textualize.io/guide/design/) also provide many CSS variables with colors that can be used out of the box.

### Named colors¶

A named color is a [`<name>`](https://textual.textualize.io/css_types/name/) that Textual recognises. Below, you can find a (collapsed) list of all of the named colors that Textual recognises, along with their hexadecimal values, their RGB values, and a visual sample.

All named colors available. <!-- SVG content removed by SVG Remover -->

### Hex RGB value¶

The hexadecimal RGB format starts with an octothorpe `#` and is then followed by 3 or 6 hexadecimal digits: `0123456789ABCDEF`. Casing is ignored.

- If 6 digits are used, the format is `#RRGGBB`:
- `RR` represents the red channel;
- `GG` represents the green channel; and
- `BB` represents the blue channel.
- If 3 digits are used, the format is `#RGB`.

In a 3 digit color, each channel is represented by a single digit which is duplicated when converting to the 6 digit format. For example, the color `#A2F` is the same as `#AA22FF`.

### Hex RGBA value¶

This is the same as the [hex RGB value](https://textual.textualize.io/css_types/color/#hex-rgb-value), but with an extra channel for the alpha component (that sets opacity).

- If 8 digits are used, the format is `#RRGGBBAA`, equivalent to the format `#RRGGBB` with two extra digits for opacity.
- If 4 digits are used, the format is `#RGBA`, equivalent to the format `#RGB` with an extra digit for opacity.

### `rgb` description[¶](https://textual.textualize.io/css_types/color/#rgb-description "Permanent link")

The `rgb` format description is a functional description of a color in the RGB color space. This description follows the format `rgb(red, green, blue)`, where `red`, `green`, and `blue` are decimal integers between 0 and 255. They represent the value of the channel with the same name.

For example, `rgb(0, 255, 32)` is equivalent to `#00FF20`.

### `rgba` description[¶](https://textual.textualize.io/css_types/color/#rgba-description "Permanent link")

The `rgba` format description is the same as the `rgb` with an extra parameter for opacity, which should be a value between `0` and `1`.

For example, `rgba(0, 255, 32, 0.5)` is the color `rgb(0, 255, 32)` with 50% opacity.

### `hsl` description[¶](https://textual.textualize.io/css_types/color/#hsl-description "Permanent link")

The `hsl` format description is a functional description of a color in the HSL color space. This description follows the format `hsl(hue, saturation, lightness)`, where

- `hue` is a float between 0 and 360;
- `saturation` is a percentage between `0%` and `100%`; and
- `lightness` is a percentage between `0%` and `100%`.

For example, the color `#00FF20` would be represented as `hsl(128, 100%, 50%)` in the HSL color space.

### `hsla` description[¶](https://textual.textualize.io/css_types/color/#hsla-description "Permanent link")

The `hsla` format description is the same as the `hsl` with an extra parameter for opacity, which should be a value between `0` and `1`.

For example, `hsla(128, 100%, 50%, 0.5)` is the color `hsl(128, 100%, 50%)` with 50% opacity.

## Examples¶

### CSS¶

```
Header {
    background: red;           /* Color name */
}

.accent {
    color: $accent;            /* Textual variable */
}

#footer {
    tint: hsl(300, 20%, 70%);  /* HSL description */
}
```

### Python¶

In Python, rules that expect a `<color>` can also accept an instance of the type [`Color`](https://textual.textualize.io/api/color/#textual.color.Color " Color").

```
# Mimicking the CSS syntax
widget.styles.background = "red"           # Color name
widget.styles.color = "$accent"            # Textual variable
widget.styles.tint = "hsl(300, 20%, 70%)"  # HSL description

from textual.color import Color
# Using a Color object directly...
color = Color(16, 200, 45)
# ... which can also parse the CSS syntax
color = Color.parse("#A8F")
```