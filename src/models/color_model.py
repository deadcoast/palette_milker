"""
Color model for the Milky Color Suite.

This module defines the Color class and related types for handling
color data throughout the application.
"""

import re
from enum import Enum
from enum import auto
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from colour import Color as ColourColor


class ColorFormat(Enum):
    """Supported color formats."""

    HEX = auto()
    RGB = auto()
    HSL = auto()
    HSV = auto()
    CMYK = auto()

    def __str__(self) -> str:
        """Return string representation of the color format."""
        return self.name


class Color:
    """
    Represents a color in the Milky Color Suite.

    This class wraps the colour.Color class and provides additional
    functionality for handling different color formats and conversions.
    """

    def __init__(self, value: Union[str, Tuple, List, Dict, "Color"]) -> None:
        """
        Initialize a Color instance.

        Args:
            value: Color value, can be a hex string, RGB tuple, or another Color instance

        Raises:
            ValueError: If the color value is invalid
        """
        if isinstance(value, Color):
            self._color = value._color
        elif isinstance(value, str):
            self._color = self._from_string(value)
        elif isinstance(value, (tuple, list)) and len(value) in (3, 4):
            self._color = self._from_rgb_tuple(value)
        elif isinstance(value, dict):
            self._color = self._from_dict(value)
        else:
            raise ValueError(f"Unsupported color value: {value}")

    def _from_string(self, value: str) -> ColourColor:
        """
        Create a Color instance from a string.

        Args:
            value: Color string (e.g., "#FFFFFF", "rgb(255, 255, 255)")

        Returns:
            A ColourColor instance

        Raises:
            ValueError: If the color string is invalid
        """
        # Check if RGB format: rgb(255, 255, 255)
        rgb_match = re.match(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)", value)
        if rgb_match:
            r, g, b = map(int, rgb_match.groups())
            return ColourColor(rgb=(r / 255, g / 255, b / 255))

        # Check if HSL format: hsl(360, 100%, 100%)
        hsl_match = re.match(r"hsl\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)", value)
        if hsl_match:
            h, s, l = map(int, hsl_match.groups())
            return ColourColor(hsl=(h / 360, s / 100, l / 100))

        # Assume hex format or named color
        try:
            return ColourColor(value)
        except ValueError as e:
            raise ValueError(f"Invalid color string: {value}") from e

    def _from_rgb_tuple(self, value: Union[Tuple, List]) -> ColourColor:
        """
        Create a Color instance from an RGB tuple.

        Args:
            value: RGB tuple or list, either (r, g, b) or (r, g, b, a)
                  with values in range 0-255 or 0.0-1.0

        Returns:
            A ColourColor instance

        Raises:
            ValueError: If the RGB tuple is invalid
        """
        # Check if values are in 0-255 range
        if any(isinstance(v, int) and v > 1 for v in value):
            # Convert to 0.0-1.0 range
            rgb = tuple(v / 255 if isinstance(v, int) and v > 1 else v for v in value[:3])
        else:
            rgb = value[:3]

        try:
            return ColourColor(rgb=rgb)
        except ValueError as e:
            raise ValueError(f"Invalid RGB values: {value}") from e

    def _from_dict(self, value: Dict) -> ColourColor:
        """
        Create a Color instance from a dictionary.

        Args:
            value: Dictionary with color components (e.g., {"r": 255, "g": 255, "b": 255})

        Returns:
            A ColourColor instance

        Raises:
            ValueError: If the dictionary is invalid
        """
        if all(k in value for k in ("r", "g", "b")):
            # RGB format
            r = value["r"] / 255 if isinstance(value["r"], int) and value["r"] > 1 else value["r"]
            g = value["g"] / 255 if isinstance(value["g"], int) and value["g"] > 1 else value["g"]
            b = value["b"] / 255 if isinstance(value["b"], int) and value["b"] > 1 else value["b"]
            return ColourColor(rgb=(r, g, b))

        elif all(k in value for k in ("h", "s", "l")):
            # HSL format
            h = value["h"] / 360 if isinstance(value["h"], int) and value["h"] > 1 else value["h"]
            s = value["s"] / 100 if isinstance(value["s"], int) and value["s"] > 1 else value["s"]
            l = value["l"] / 100 if isinstance(value["l"], int) and value["l"] > 1 else value["l"]
            return ColourColor(hsl=(h, s, l))

        elif all(k in value for k in ("h", "s", "v")):
            return self._convert_to_rgb(value)
        else:
            raise ValueError(f"Invalid color dictionary: {value}")

    def _convert_to_rgb(self, value):
        # HSV format - convert to RGB first
        h = value["h"] / 360 if isinstance(value["h"], int) and value["h"] > 1 else value["h"]
        s = value["s"] / 100 if isinstance(value["s"], int) and value["s"] > 1 else value["s"]
        v = value["v"] / 100 if isinstance(value["v"], int) and value["v"] > 1 else value["v"]

        # HSV to RGB conversion
        h_i = int(h * 6)
        f = h * 6 - h_i
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)

        if h_i == 0:
            r, g, b = v, t, p
        elif h_i == 1:
            r, g, b = q, v, p
        elif h_i == 2:
            r, g, b = p, v, t
        elif h_i == 3:
            r, g, b = p, q, v
        elif h_i == 4:
            r, g, b = t, p, v
        else:
            r, g, b = v, p, q

        return ColourColor(rgb=(r, g, b))

    @property
    def hex(self) -> str:
        """
        Get the color as a hex string.

        Returns:
            Hex color string (e.g., "#FFFFFF")
        """
        return self._color.hex_l

    @property
    def rgb(self) -> Tuple[int, int, int]:
        """
        Get the color as RGB values.

        Returns:
            RGB tuple with values in range 0-255
        """
        r, g, b = self._color.rgb
        return (int(r * 255), int(g * 255), int(b * 255))

    @property
    def rgb_float(self) -> Tuple[float, float, float]:
        """
        Get the color as RGB values in 0.0-1.0 range.

        Returns:
            RGB tuple with values in range 0.0-1.0
        """
        return self._color.rgb

    @property
    def hsl(self) -> Tuple[int, int, int]:
        """
        Get the color as HSL values.

        Returns:
            HSL tuple with values in range 0-360, 0-100, 0-100
        """
        h, s, l = self._color.hsl
        return (int(h * 360), int(s * 100), int(l * 100))

    @property
    def hsl_float(self) -> Tuple[float, float, float]:
        """
        Get the color as HSL values in 0.0-1.0 range.

        Returns:
            HSL tuple with values in range 0.0-1.0
        """
        return self._color.hsl

    @property
    def hsv(self) -> Tuple[int, int, int]:
        """
        Get the color as HSV values.

        Returns:
            HSV tuple with values in range 0-360, 0-100, 0-100
        """
        # Convert RGB to HSV
        r, g, b = self.rgb_float
        max_val = max(r, g, b)
        min_val = min(r, g, b)
        diff = max_val - min_val

        # Hue calculation
        if diff == 0:
            h = 0
        elif max_val == r:
            h = 60 * ((g - b) / diff % 6)
        elif max_val == g:
            h = 60 * ((b - r) / diff + 2)
        else:  # max_val == b
            h = 60 * ((r - g) / diff + 4)

        # Saturation calculation
        s = 0 if max_val == 0 else diff / max_val

        # Value calculation
        v = max_val

        return (int(h), int(s * 100), int(v * 100))

    @property
    def cmyk(self) -> Tuple[int, int, int, int]:
        """
        Get the color as CMYK values.

        Returns:
            CMYK tuple with values in range 0-100
        """
        r, g, b = self.rgb_float

        # RGB to CMYK conversion
        k = 1 - max(r, g, b)
        if k == 1:
            return (0, 0, 0, 100)

        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)

        return (int(c * 100), int(m * 100), int(y * 100), int(k * 100))

    def get_format(self, format_type: ColorFormat) -> Union[str, Tuple]:
        """
        Get the color in the specified format.

        Args:
            format_type: The desired color format

        Returns:
            The color in the specified format
        """
        if format_type == ColorFormat.HEX:
            return self.hex
        elif format_type == ColorFormat.RGB:
            return self.rgb
        elif format_type == ColorFormat.HSL:
            return self.hsl
        elif format_type == ColorFormat.HSV:
            return self.hsv
        elif format_type == ColorFormat.CMYK:
            return self.cmyk
        else:
            raise ValueError(f"Unsupported color format: {format_type}")

    def with_alpha(self, alpha: float) -> str:
        """
        Get the color as a hex string with alpha.

        Args:
            alpha: Alpha value in range 0.0-1.0

        Returns:
            Hex color string with alpha (e.g., "#FFFFFFAA")
        """
        alpha_hex = hex(int(alpha * 255))[2:].zfill(2)
        return f"{self.hex}{alpha_hex}"

    def analogous(self, count: int = 3, angle: float = 30) -> List["Color"]:
        """
        Get analogous colors.

        Args:
            count: Number of colors to return
            angle: Angle between colors in degrees

        Returns:
            List of analogous colors
        """
        result = []
        h, s, l = self.hsl

        for i in range(count):
            # Calculate new hue
            new_hue = (h + (i - count // 2) * angle) % 360

            # Create new color
            new_color = Color({"h": new_hue, "s": s, "l": l})
            result.append(new_color)

        return result

    def complementary(self) -> "Color":
        """
        Get the complementary color.

        Returns:
            The complementary color
        """
        h, s, l = self.hsl
        h = (h + 180) % 360

        return Color({"h": h, "s": s, "l": l})

    def triadic(self) -> List["Color"]:
        """
        Get triadic colors.

        Returns:
            List of triadic colors
        """
        h, s, l = self.hsl

        h1 = (h + 120) % 360
        h2 = (h + 240) % 360

        return [self, Color({"h": h1, "s": s, "l": l}), Color({"h": h2, "s": s, "l": l})]

    def tetradic(self) -> List["Color"]:
        """
        Get tetradic colors.

        Returns:
            List of tetradic colors
        """
        h, s, l = self.hsl

        h1 = (h + 90) % 360
        h2 = (h + 180) % 360
        h3 = (h + 270) % 360

        return [
            self,
            Color({"h": h1, "s": s, "l": l}),
            Color({"h": h2, "s": s, "l": l}),
            Color({"h": h3, "s": s, "l": l}),
        ]

    def lighten(self, amount: float = 0.1) -> "Color":
        """
        Get a lighter version of the color.

        Args:
            amount: Amount to lighten by (0.0-1.0)

        Returns:
            Lightened color
        """
        new_color = ColourColor(self.hex)
        new_color.luminance += amount

        return Color(new_color.hex_l)

    def darken(self, amount: float = 0.1) -> "Color":
        """
        Get a darker version of the color.

        Args:
            amount: Amount to darken by (0.0-1.0)

        Returns:
            Darkened color
        """
        new_color = ColourColor(self.hex)
        new_color.luminance -= amount

        return Color(new_color.hex_l)

    def saturate(self, amount: float = 0.1) -> "Color":
        """
        Get a more saturated version of the color.

        Args:
            amount: Amount to saturate by (0.0-1.0)

        Returns:
            Saturated color
        """
        new_color = ColourColor(self.hex)
        new_color.saturation += amount

        return Color(new_color.hex_l)

    def desaturate(self, amount: float = 0.1) -> "Color":
        """
        Get a less saturated version of the color.

        Args:
            amount: Amount to desaturate by (0.0-1.0)

        Returns:
            Desaturated color
        """
        new_color = ColourColor(self.hex)
        new_color.saturation -= amount

        return Color(new_color.hex_l)

    def __str__(self) -> str:
        """String representation of the color."""
        return self.hex

    def __repr__(self) -> str:
        """Detailed string representation of the color."""
        return f"Color({self.hex})"

    def __eq__(self, other: object) -> bool:
        """Check if two colors are equal."""
        if not isinstance(other, Color):
            return NotImplemented

        return self.hex.lower() == other.hex.lower()
