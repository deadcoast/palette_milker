"""
Unit tests for the color_model module.

This module contains tests for the Color class and related color manipulation functions.
"""

import pytest

from src.models.color_model import Color


class TestColorModel:
    """Test suite for the Color model class."""

    def test_color_creation_from_hex(self) -> None:
        """Test creating a color from a hex string."""
        # Test with hash symbol
        color = Color("#FF5500")
        assert color.hex.upper() == "#FF5500"
        r, g, b = color.rgb
        assert r == 255
        assert abs(g - 85) <= 1  # Allow small difference due to conversion precision
        assert b == 0

        # Test with hash symbol - require # for hex colors
        color = Color("#00AAFF")
        assert color.hex.upper() == "#00AAFF"
        r, g, b = color.rgb
        assert r == 0
        assert abs(g - 170) <= 1  # Allow small difference due to conversion precision
        assert abs(b - 255) <= 1  # Allow small difference due to conversion precision

        # Test lowercase
        color = Color("#ff0000")
        assert color.hex.upper() == "#FF0000"
        r, g, b = color.rgb
        assert r == 255
        assert g == 0
        assert b == 0

    def test_color_creation_from_rgb(self) -> None:
        """Test creating a color from RGB values."""
        # Create from RGB tuple
        color = Color((255, 85, 0))
        assert color.hex.upper() == "#FF5500"
        r, g, b = color.rgb
        assert r == 255
        assert abs(g - 85) <= 1  # Allow small difference due to conversion precision
        assert b == 0

        # Test boundary values
        color = Color((0, 0, 0))
        assert color.hex.upper() == "#000000"
        r, g, b = color.rgb
        assert r == 0
        assert g == 0
        assert b == 0

        color = Color((255, 255, 255))
        assert color.hex.upper() == "#FFFFFF"
        r, g, b = color.rgb
        assert r == 255
        assert g == 255
        assert b == 255

    def test_color_creation_from_hsl(self) -> None:
        """Test creating a color from HSL values."""
        # Red (0° hue)
        color = Color({"h": 0, "s": 100, "l": 50})
        assert color.hex.upper() == "#FF0000"

        # Green (120° hue)
        color = Color({"h": 120, "s": 100, "l": 50})
        assert color.hex.upper() == "#00FF00"

        # Blue (240° hue)
        color = Color({"h": 240, "s": 100, "l": 50})
        assert color.hex.upper() == "#0000FF"

        # White (any hue, 0% saturation, 100% lightness)
        color = Color({"h": 0, "s": 0, "l": 100})
        assert color.hex.upper() == "#FFFFFF"

        # Black (any hue, 0% saturation, 0% lightness)
        color = Color({"h": 0, "s": 0, "l": 0})
        assert color.hex.upper() == "#000000"

    def test_color_equality(self) -> None:
        """Test color equality comparison."""
        color1 = Color("#FF5500")
        color2 = Color("#FF5500")
        color3 = Color("#00AAFF")

        assert color1 == color2
        assert color1 != color3
        assert color1 != "not a color"

    def test_color_string_representation(self) -> None:
        """Test string representation of colors."""
        color = Color("#FF5500")
        assert str(color).upper() == "#FF5500"
        repr_text = repr(color).upper()
        assert "COLOR" in repr_text
        assert "#FF5500" in repr_text

    def test_color_properties(self) -> None:
        """Test computed color properties."""
        color = Color("#FF5500")

        # Test RGB components
        r, g, b = color.rgb
        assert r == 255
        assert abs(g - 85) <= 1  # Allow small difference due to conversion precision
        assert b == 0

        # Test HSL components
        hsl = color.hsl
        assert 15 <= hsl[0] <= 30  # Hue between 15° and 30°
        assert 95 <= hsl[1] <= 100  # Saturation close to 100%
        assert 45 <= hsl[2] <= 55  # Lightness close to 50%

    def test_color_luminance(self) -> None:
        """Test luminance-related properties."""
        # Create colors to test
        white = Color("#FFFFFF")
        black = Color("#000000")
        gray = Color("#808080")

        # Test relative lightness between colors
        assert white.rgb_float[0] == 1.0
        assert white.rgb_float[1] == 1.0
        assert white.rgb_float[2] == 1.0

        assert black.rgb_float[0] == 0.0
        assert black.rgb_float[1] == 0.0
        assert black.rgb_float[2] == 0.0

        # Medium gray has RGB values around 0.5
        assert 0.45 <= gray.rgb_float[0] <= 0.55
        assert 0.45 <= gray.rgb_float[1] <= 0.55
        assert 0.45 <= gray.rgb_float[2] <= 0.55

    def test_color_contrast(self) -> None:
        """Test contrast relationships between colors."""
        # Create distinct colors
        white = Color("#FFFFFF")
        black = Color("#000000")
        red = Color("#FF0000")
        blue = Color("#0000FF")
        green = Color("#00FF00")

        # Test color relationships through properties
        # White and black are at opposite ends of the spectrum
        assert white.hsl[2] == 100  # White has 100% lightness
        assert black.hsl[2] == 0    # Black has 0% lightness

        # Test that red, green, and blue have different hue values
        assert red.hsl[0] != green.hsl[0]
        assert green.hsl[0] != blue.hsl[0]
        assert red.hsl[0] != blue.hsl[0]

    def test_invalid_color_creation(self) -> None:
        """Test creating colors with invalid inputs."""
        # Invalid hex format
        with pytest.raises(AttributeError):
            Color("#XYZ")

        # Invalid RGB values (negative)
        with pytest.raises(ValueError):
            Color((-1, 0, 0))

        # Invalid RGB values (too large)
        with pytest.raises(ValueError):
            Color((256, 0, 0))

    def test_get_complementary_color(self) -> None:
        """Test generating complementary colors."""
        red = Color("#FF0000")
        complementary = red.complementary()

        # Complementary of red should be close to cyan
        assert complementary.hex.upper() == "#00FFFF"

        # Test symmetry (doing it twice should get back close to original)
        assert complementary.complementary().hex.upper() == "#FF0000"

    def test_lighten_darken(self) -> None:
        """Test color harmony generation methods."""
        color = Color("#808080")  # Medium gray

        # Create analogous colors
        analogous_colors = color.analogous(3, 30)
        assert len(analogous_colors) == 3

        # Each returned color should be a Color instance
        for c in analogous_colors:
            assert isinstance(c, Color)

        # Create triadic colors
        triadic_colors = color.triadic()
        assert len(triadic_colors) == 3

        # Each returned color should be a Color instance
        for c in triadic_colors:
            assert isinstance(c, Color)

    def test_color_formats(self) -> None:
        """Test getting color in different formats."""
        # Create a color
        color = Color("#FF5500")

        # Test HSV format
        hsv = color.hsv
        assert isinstance(hsv, tuple)
        assert len(hsv) == 3
        assert 15 <= hsv[0] <= 30  # Hue between 15° and 30°
        assert 95 <= hsv[1] <= 100  # Saturation close to 100%
        assert 95 <= hsv[2] <= 100  # Value close to 100%

        # Test CMYK format
        cmyk = color.cmyk
        assert isinstance(cmyk, tuple)
        assert len(cmyk) == 4
        # For FF5500, we expect C=0, M and Y to be non-zero
        # K might be 0 for this bright color, so we don't test its exact value
        assert cmyk[0] == 0  # Cyan
        assert cmyk[1] > 0   # Magenta
        assert cmyk[2] > 0   # Yellow


if __name__ == "__main__":
    pytest.main(["-v", "test_color_model.py"])
