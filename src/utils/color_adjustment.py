"""
Color adjustment utilities for the Palette Milker application.

This module provides functions for manipulating colors in HSL space,
allowing for intuitive adjustments like changing hue, saturation or lightness.
"""

from typing import Dict
from typing import Tuple
from typing import Union

from ..models.color_model import Color


def adjust_hue(color: Union[str, Color], amount: int) -> Color:
    """
    Adjust the hue of a color.

    Args:
        color: Color to adjust, either as a hex string or Color object
        amount: Amount to adjust the hue by (positive or negative degrees)

    Returns:
        A new Color object with the adjusted hue
    """
    # Convert to Color object if it's a string
    if isinstance(color, str):
        color = Color(color)

    # Get current HSL values
    h, s, lightness = color.hsl

    # Adjust hue (keep it in 0-360 range)
    new_h = (h + amount) % 360

    # Create a new color with the adjusted hue
    return Color({"h": new_h, "s": s, "l": lightness})


def adjust_saturation(color: Union[str, Color], amount: int) -> Color:
    """
    Adjust the saturation of a color.

    Args:
        color: Color to adjust, either as a hex string or Color object
        amount: Amount to adjust the saturation by (positive or negative percentage)

    Returns:
        A new Color object with the adjusted saturation
    """
    # Convert to Color object if it's a string
    if isinstance(color, str):
        color = Color(color)

    # Get current HSL values
    h, s, lightness = color.hsl

    # Adjust saturation (clamp between 0-100)
    new_s = max(0, min(100, s + amount))

    # Create a new color with the adjusted saturation
    return Color({"h": h, "s": new_s, "l": lightness})


def adjust_lightness(color: Union[str, Color], amount: int) -> Color:
    """
    Adjust the lightness of a color.

    Args:
        color: Color to adjust, either as a hex string or Color object
        amount: Amount to adjust the lightness by (positive or negative percentage)

    Returns:
        A new Color object with the adjusted lightness
    """
    # Convert to Color object if it's a string
    if isinstance(color, str):
        color = Color(color)

    # Get current HSL values
    h, s, lightness = color.hsl

    # Adjust lightness (clamp between 0-100)
    new_l = max(0, min(100, lightness + amount))

    # Create a new color with the adjusted lightness
    return Color({"h": h, "s": s, "l": new_l})


def adjust_color(color: Union[str, Color], hue: int = 0, saturation: int = 0, lightness: int = 0) -> Color:
    """
    Adjust multiple aspects of a color at once.

    Args:
        color: Color to adjust, either as a hex string or Color object
        hue: Amount to adjust the hue by (default: 0)
        saturation: Amount to adjust the saturation by (default: 0)
        lightness: Amount to adjust the lightness by (default: 0)

    Returns:
        A new Color object with the adjusted properties
    """
    # Convert to Color object if it's a string
    if isinstance(color, str):
        color = Color(color)

    # Get current HSL values
    h, s, lightness_value = color.hsl

    # Adjust all properties (with appropriate constraints)
    new_h = (h + hue) % 360
    new_s = max(0, min(100, s + saturation))
    new_l = max(0, min(100, lightness_value + lightness))

    # Create a new color with the adjusted values
    return Color({"h": new_h, "s": new_s, "l": new_l})


def get_color_info(color: Union[str, Color]) -> Dict[str, Union[str, Tuple[int, ...], bool]]:
    """
    Get comprehensive information about a color.

    Args:
        color: Color to analyze, either as a hex string or Color object

    Returns:
        Dictionary with color information in various formats
    """
    # Convert to Color object if it's a string
    if isinstance(color, str):
        color = Color(color)

    # Extract color information in various formats
    return {
        "hex": color.hex,
        "rgb": color.rgb,
        "hsl": color.hsl,
        "hsv": color.hsv,
        "cmyk": color.cmyk,
        "is_dark": is_color_dark(color),
    }


def is_color_dark(color: Union[str, Color]) -> bool:
    """
    Determine if a color is dark (for contrast purposes).

    Args:
        color: Color to check, either as a hex string or Color object

    Returns:
        True if the color is considered dark, False otherwise
    """
    # Convert to Color object if it's a string
    if isinstance(color, str):
        color = Color(color)

    # Calculate relative luminance using standard formula
    r, g, b = color.rgb_float
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b

    # Color is dark if luminance is below threshold (typical threshold is 0.5)
    return luminance < 0.5
