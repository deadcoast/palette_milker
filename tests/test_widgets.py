"""
Unit tests for Textual widgets in the Palette Milker application.

This module contains tests for widget behaviors and basic functionality.

Note: These are simplified tests that verify basic widget instantiation and property
manipulation. Full interactive testing of Textual widgets normally requires mounting them
in a test application and using the Textual pilot/testing tools. Those tests have been
simplified here to focus on the non-UI aspects of the widgets that can be tested without
mounting them in a Textual application context.
"""

import pytest

from src.widgets.color.color_wheel import ColorWheel
from src.widgets.palette.palette_management import PaletteManagement


def test_color_wheel_instantiation() -> None:
    """Test that ColorWheel can be instantiated with proper parameters."""
    # Create a color wheel with default parameters
    color_wheel = ColorWheel()
    assert isinstance(color_wheel, ColorWheel)
    assert color_wheel.selected_color.startswith("#")

    # Create with custom parameters
    custom_wheel = ColorWheel(title="Custom Title", widget_id="custom-wheel")
    assert custom_wheel.title == "Custom Title"
    assert custom_wheel.id == "custom-wheel"


def test_color_wheel_selection() -> None:
    """Test color selection functionality in the ColorWheel."""
    color_wheel = ColorWheel()

    # Set a specific color
    test_color = "#FF5500"
    color_wheel.selected_color = test_color

    # Check the color was set
    assert color_wheel.selected_color == test_color


def test_simple_widget_creation() -> None:
    """Test that widgets can be created with basic parameters."""
    # Just validate that we can instantiate widgets without errors
    color_wheel = ColorWheel(title="Color Wheel")
    assert isinstance(color_wheel, ColorWheel)

    # Create simple PaletteManagement without complex initialization
    # Note: Full widget initialization would require mounting in a real app
    palette_mgmt = PaletteManagement()
    assert isinstance(palette_mgmt, PaletteManagement)


if __name__ == "__main__":
    pytest.main(["-v", "test_widgets.py"])
