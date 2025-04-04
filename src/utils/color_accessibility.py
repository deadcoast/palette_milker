"""
Color accessibility utilities for checking contrast and WCAG compliance.

This module provides functions for calculating contrast ratios,
checking WCAG compliance, and suggesting accessible alternatives
for color combinations.
"""

from typing import Dict
from typing import List
from typing import Union

from ..models.color_model import Color


def get_luminance(color: Union[str, Color]) -> float:
    """
    Calculate the relative luminance of a color according to WCAG 2.0.

    Args:
        color: Color to calculate luminance for (hex string or Color instance)

    Returns:
        Relative luminance value between 0 and 1
    """
    # Convert to Color instance if string
    color_obj = color if isinstance(color, Color) else Color(color)

    # Get RGB values
    r, g, b = [c / 255.0 for c in color_obj.rgb]

    # Convert RGB values to linear sRGB
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4

    # Calculate luminance
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def calculate_contrast_ratio(foreground: Union[str, Color], background: Union[str, Color]) -> float:
    """
    Calculate the contrast ratio between two colors according to WCAG 2.0.

    Args:
        foreground: Foreground color (text color)
        background: Background color

    Returns:
        Contrast ratio between 1 and 21
    """
    # Calculate luminance for both colors
    fg_lum = get_luminance(foreground)
    bg_lum = get_luminance(background)

    # Ensure lighter color is used as L1
    l1 = max(fg_lum, bg_lum)
    l2 = min(fg_lum, bg_lum)

    # Calculate contrast ratio
    return (l1 + 0.05) / (l2 + 0.05)


def get_wcag_compliance(contrast_ratio: float) -> Dict[str, bool]:
    """
    Check WCAG 2.0 compliance for a given contrast ratio.

    Args:
        contrast_ratio: Contrast ratio between 1 and 21

    Returns:
        Dictionary with compliance status for different WCAG levels
    """
    return {
        "AA_large": contrast_ratio >= 3.0,  # WCAG AA for large text (14pt bold or 18pt+)
        "AA_normal": contrast_ratio >= 4.5,  # WCAG AA for normal text
        "AAA_large": contrast_ratio >= 4.5,  # WCAG AAA for large text
        "AAA_normal": contrast_ratio >= 7.0,  # WCAG AAA for normal text
    }


def analyze_color_pair(foreground: Union[str, Color], background: Union[str, Color]) -> Dict:
    """
    Analyze the accessibility of a color pair.

    Args:
        foreground: Foreground color (text color)
        background: Background color

    Returns:
        Dictionary with contrast ratio and compliance status
    """
    # Calculate contrast ratio
    ratio = calculate_contrast_ratio(foreground, background)

    # Check compliance
    compliance = get_wcag_compliance(ratio)

    # Format ratio for display
    formatted_ratio = f"{ratio:.2f}:1"

    return {
        "foreground": str(foreground),
        "background": str(background),
        "contrast_ratio": ratio,
        "formatted_ratio": formatted_ratio,
        "compliance": compliance,
        "passes_aa_large": compliance["AA_large"],
        "passes_aa_normal": compliance["AA_normal"],
        "passes_aaa_large": compliance["AAA_large"],
        "passes_aaa_normal": compliance["AAA_normal"],
    }


def suggest_accessible_alternatives(
    foreground: Union[str, Color], background: Union[str, Color], target_ratio: float = 4.5
) -> List[Dict]:
    """
    Suggest accessible alternatives for a color pair.

    Args:
        foreground: Foreground color (text color)
        background: Background color
        target_ratio: Target contrast ratio (default: 4.5 for WCAG AA)

    Returns:
        List of alternative color pairs that meet the target ratio
    """
    # Convert to Color instances
    fg = foreground if isinstance(foreground, Color) else Color(foreground)
    bg = background if isinstance(background, Color) else Color(background)

    # Current contrast ratio
    current_ratio = calculate_contrast_ratio(fg, bg)

    # If already compliant, return empty list
    if current_ratio >= target_ratio:
        return []

    alternatives = []

    # Try lightening the foreground
    for amount in [0.1, 0.2, 0.3, 0.4]:
        lighter_fg = fg.lighten(amount)
        ratio = calculate_contrast_ratio(lighter_fg, bg)
        if ratio >= target_ratio:
            alternatives.append(
                {
                    "foreground": lighter_fg.hex,
                    "background": bg.hex,
                    "contrast_ratio": ratio,
                    "formatted_ratio": f"{ratio:.2f}:1",
                    "adjustment": f"Lightened foreground by {amount * 100:.0f}%",
                }
            )
            break

    # Try darkening the foreground
    for amount in [0.1, 0.2, 0.3, 0.4]:
        darker_fg = fg.darken(amount)
        ratio = calculate_contrast_ratio(darker_fg, bg)
        if ratio >= target_ratio:
            alternatives.append(
                {
                    "foreground": darker_fg.hex,
                    "background": bg.hex,
                    "contrast_ratio": ratio,
                    "formatted_ratio": f"{ratio:.2f}:1",
                    "adjustment": f"Darkened foreground by {amount * 100:.0f}%",
                }
            )
            break

    # Try lightening the background
    for amount in [0.1, 0.2, 0.3, 0.4]:
        lighter_bg = bg.lighten(amount)
        ratio = calculate_contrast_ratio(fg, lighter_bg)
        if ratio >= target_ratio:
            alternatives.append(
                {
                    "foreground": fg.hex,
                    "background": lighter_bg.hex,
                    "contrast_ratio": ratio,
                    "formatted_ratio": f"{ratio:.2f}:1",
                    "adjustment": f"Lightened background by {amount * 100:.0f}%",
                }
            )
            break

    # Try darkening the background
    for amount in [0.1, 0.2, 0.3, 0.4]:
        darker_bg = bg.darken(amount)
        ratio = calculate_contrast_ratio(fg, darker_bg)
        if ratio >= target_ratio:
            alternatives.append(
                {
                    "foreground": fg.hex,
                    "background": darker_bg.hex,
                    "contrast_ratio": ratio,
                    "formatted_ratio": f"{ratio:.2f}:1",
                    "adjustment": f"Darkened background by {amount * 100:.0f}%",
                }
            )
            break

    return alternatives


def is_color_blind_friendly(color1: Union[str, Color], color2: Union[str, Color]) -> Dict[str, bool]:
    """
    Check if a color pair is friendly for different types of color blindness.

    This is a simplified check based on color differences in different channels.

    Args:
        color1: First color
        color2: Second color

    Returns:
        Dictionary with friendliness status for different types of color blindness
    """
    # Convert to Color instances
    c1 = color1 if isinstance(color1, Color) else Color(color1)
    c2 = color2 if isinstance(color2, Color) else Color(color2)

    # Get RGB values
    r1, g1, b1 = c1.rgb
    r2, g2, b2 = c2.rgb

    # Calculate differences
    r_diff = abs(r1 - r2)
    g_diff = abs(g1 - g2)
    b_diff = abs(b1 - b2)

    # Thresholds for "significant difference"
    threshold = 100

    # Simplified checks for different types of color blindness
    return {
        # Protanopia (red-blind) - needs good blue-yellow differences
        "protanopia": b_diff > threshold or g_diff > threshold,
        # Deuteranopia (green-blind) - needs good blue-red differences
        "deuteranopia": b_diff > threshold or r_diff > threshold,
        # Tritanopia (blue-blind) - needs good red-green differences
        "tritanopia": r_diff > threshold or g_diff > threshold,
        # Achromatopsia (total color blindness) - needs good brightness difference
        "achromatopsia": calculate_contrast_ratio(c1, c2) > 3.0,
    }


def get_brightness(color: Union[str, Color]) -> int:
    """
    Calculate the perceived brightness of a color (0-255).

    Uses the formula: (R * 299 + G * 587 + B * 114) / 1000

    Args:
        color: Color to calculate brightness for

    Returns:
        Brightness value between 0 and 255
    """
    # Convert to Color instance
    color_obj = color if isinstance(color, Color) else Color(color)

    # Get RGB values
    r, g, b = color_obj.rgb

    # Calculate brightness
    return int((r * 299 + g * 587 + b * 114) / 1000)


def optimize_text_color(background: Union[str, Color]) -> Color:
    """
    Determine the optimal text color (black or white) for a given background.

    Args:
        background: Background color

    Returns:
        Black or white Color instance for optimal contrast
    """
    # Convert to Color instance
    bg = background if isinstance(background, Color) else Color(background)

    # Calculate brightness
    brightness = get_brightness(bg)

    # Use white text on dark backgrounds, black text on light backgrounds
    return Color("#FFFFFF") if brightness < 128 else Color("#000000")
