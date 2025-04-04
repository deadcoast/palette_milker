"""
Unit tests for the color_model module.

This module contains tests for the Color class and related color manipulation functions.
"""

import pytest

from src.models.color_model import Color


class TestColorModel:
    """Test suite for the Color model class."""

    def test_color_creation_from_hex(self):
        """Test creating a color from a hex string."""
        # Test with hash symbol
        color = Color("#FF5500")
        assert color.hex == "#FF5500"
        assert color.rgb == (255, 85, 0)

        # Test without hash symbol
        color = Color("00AAFF")
        assert color.hex == "#00AAFF"
        assert color.rgb == (0, 170, 255)

        # Test lowercase
        color = Color("#ff0000")
        assert color.hex == "#FF0000"
        assert color.rgb == (255, 0, 0)

    def test_color_creation_from_rgb(self):
        """Test creating a color from RGB values."""
        color = Color.from_rgb(255, 85, 0)
        assert color.hex == "#FF5500"
        assert color.rgb == (255, 85, 0)

        # Test boundary values
        color = Color.from_rgb(0, 0, 0)
        assert color.hex == "#000000"

        color = Color.from_rgb(255, 255, 255)
        assert color.hex == "#FFFFFF"

    def test_color_creation_from_hsl(self):
        """Test creating a color from HSL values."""
        # Red (0° hue)
        color = Color.from_hsl(0, 100, 50)
        assert color.hex == "#FF0000"

        # Green (120° hue)
        color = Color.from_hsl(120, 100, 50)
        assert color.hex == "#00FF00"

        # Blue (240° hue)
        color = Color.from_hsl(240, 100, 50)
        assert color.hex == "#0000FF"

        # White (any hue, 0% saturation, 100% lightness)
        color = Color.from_hsl(0, 0, 100)
        assert color.hex == "#FFFFFF"

        # Black (any hue, 0% saturation, 0% lightness)
        color = Color.from_hsl(0, 0, 0)
        assert color.hex == "#000000"

    def test_color_equality(self):
        """Test color equality comparison."""
        color1 = Color("#FF5500")
        color2 = Color("#FF5500")
        color3 = Color("#00AAFF")

        assert color1 == color2
        assert color1 != color3
        assert color1 != "not a color"

    def test_color_string_representation(self):
        """Test string representation of colors."""
        color = Color("#FF5500")
        assert str(color) == "#FF5500"
        assert repr(color) == "Color('#FF5500')"

    def test_color_properties(self):
        """Test computed color properties."""
        color = Color("#FF5500")

        # Test RGB components
        assert color.red == 255
        assert color.green == 85
        assert color.blue == 0

        # Test HSL components
        hsl = color.hsl
        assert 20 <= hsl[0] <= 30  # Hue around 25°
        assert 95 <= hsl[1] <= 100  # Saturation close to 100%
        assert 45 <= hsl[2] <= 55  # Lightness close to 50%

    def test_color_luminance(self):
        """Test luminance calculation."""
        # White has luminance 1.0
        white = Color("#FFFFFF")
        assert white.luminance == pytest.approx(1.0)

        # Black has luminance 0.0
        black = Color("#000000")
        assert black.luminance == pytest.approx(0.0)

        # Medium gray has luminance around 0.5
        gray = Color("#808080")
        assert 0.2 <= gray.luminance <= 0.3

    def test_color_contrast_ratio(self):
        """Test contrast ratio calculation."""
        # White and black have maximum contrast ratio (21:1)
        white = Color("#FFFFFF")
        black = Color("#000000")
        assert white.contrast_ratio(black) == pytest.approx(21.0, abs=0.5)

        # Same color has contrast ratio 1:1
        red = Color("#FF0000")
        assert red.contrast_ratio(red) == pytest.approx(1.0, abs=0.01)

        # Test symmetric property
        blue = Color("#0000FF")
        green = Color("#00FF00")
        assert blue.contrast_ratio(green) == pytest.approx(green.contrast_ratio(blue), abs=0.01)

    def test_invalid_color_creation(self):
        """Test creating colors with invalid inputs."""
        # Invalid hex format
        with pytest.raises(ValueError):
            Color("#XYZ")

        # Invalid RGB values (negative)
        with pytest.raises(ValueError):
            Color.from_rgb(-1, 0, 0)

        # Invalid RGB values (too large)
        with pytest.raises(ValueError):
            Color.from_rgb(256, 0, 0)

        # Invalid HSL values (negative hue)
        with pytest.raises(ValueError):
            Color.from_hsl(-1, 50, 50)

        # Invalid HSL values (hue > 360)
        with pytest.raises(ValueError):
            Color.from_hsl(361, 50, 50)

        # Invalid HSL values (saturation < 0)
        with pytest.raises(ValueError):
            Color.from_hsl(0, -1, 50)

        # Invalid HSL values (saturation > 100)
        with pytest.raises(ValueError):
            Color.from_hsl(0, 101, 50)

    def test_get_complementary_color(self):
        """Test generating complementary colors."""
        red = Color("#FF0000")
        complementary = red.get_complementary()

        # Complementary of red should be close to cyan
        assert complementary.hex == "#00FFFF"

        # Test symmetry (doing it twice should get back close to original)
        assert complementary.get_complementary().hex == "#FF0000"

    def test_lighten_darken(self):
        """Test lightening and darkening colors."""
        color = Color("#808080")  # Medium gray

        # Lighten by 20%
        lighter = color.lighten(20)
        assert lighter.hsl[2] > color.hsl[2]

        # Darken by 20%
        darker = color.darken(20)
        assert darker.hsl[2] < color.hsl[2]

        # Extreme lightening should approach white
        very_light = color.lighten(100)
        assert very_light.hsl[2] == 100

        # Extreme darkening should approach black
        very_dark = color.darken(100)
        assert very_dark.hsl[2] == 0

    def test_color_is_dark_light(self):
        """Test is_dark and is_light methods."""
        # Black is dark
        black = Color("#000000")
        assert black.is_dark() is True
        assert black.is_light() is False

        # White is light
        white = Color("#FFFFFF")
        assert white.is_dark() is False
        assert white.is_light() is True

        # Medium gray depends on threshold
        gray = Color("#808080")
        # Default threshold behavior
        assert (gray.is_dark() != gray.is_light())


if __name__ == "__main__":
    pytest.main(["-v", "test_color_model.py"])
