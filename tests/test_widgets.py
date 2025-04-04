"""
Integration tests for Textual widgets in the Palette Milker application.

This module contains tests for widget behaviors and interactions.
"""

from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
from textual.app import App
from textual.app import ComposeResult
from textual.widgets import Button
from textual.widgets import Static

from src.models.color_model import Color
from src.widgets.color.color_wheel import ColorWheel
from src.widgets.palette.palette_management import PaletteManagement


class TestAppBase(App):
    """Base test application for widget testing."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.received_messages = []
        self.is_mounted = False

    def on_mount(self) -> None:
        """Record when app is mounted."""
        self.is_mounted = True


class TestColorWheel:
    """Test suite for the ColorWheel widget."""

    class ColorWheelTestApp(TestAppBase):
        """Test app for ColorWheel."""

        def compose(self) -> ComposeResult:
            """Compose the test app UI."""
            yield ColorWheel(title="TEST COLOR WHEEL", id="color-wheel")

        def on_color_wheel_color_changed(self, message):
            """Capture color changed events."""
            self.received_messages.append(message)

    async def test_color_wheel_initialization(self, app_runner):
        """Test ColorWheel initialization."""
        async with app_runner(self.ColorWheelTestApp) as pilot:
            # Check that color wheel exists
            color_wheel = pilot.app.query_one("#color-wheel", ColorWheel)
            assert color_wheel is not None

            # Check default color
            assert isinstance(color_wheel.selected_color, str)
            assert color_wheel.selected_color.startswith("#")

    async def test_color_selection(self, app_runner):
        """Test selecting a color in the color wheel."""
        async with app_runner(self.ColorWheelTestApp) as pilot:
            color_wheel = pilot.app.query_one("#color-wheel", ColorWheel)

            # Set a specific color
            test_color = "#FF5500"
            color_wheel.selected_color = test_color

            # Should output the same color
            assert color_wheel.selected_color == test_color

            # App should have received a message
            assert len(pilot.app.received_messages) > 0
            assert any(msg.color == test_color for msg in pilot.app.received_messages)


class TestPaletteManagement:
    """Test suite for the PaletteManagement widget."""

    class PaletteManagementTestApp(TestAppBase):
        """Test app for PaletteManagement."""

        def compose(self) -> ComposeResult:
            """Compose the test app UI."""
            yield PaletteManagement(
                palette_id="test-palette",
                palette_name="Test Palette",
                colors=["#FF0000", "#00FF00", "#0000FF"],
                active_color_index=0,
                id="palette-management"
            )

        def on_palette_management_color_selected(self, message):
            """Capture color selection events."""
            self.received_messages.append(message)

    async def test_palette_management_initialization(self, app_runner):
        """Test PaletteManagement initialization."""
        async with app_runner(self.PaletteManagementTestApp) as pilot:
            # Check that palette management exists
            palette_mgmt = pilot.app.query_one("#palette-management", PaletteManagement)
            assert palette_mgmt is not None

            # Check initial state
            assert palette_mgmt.palette_id == "test-palette"
            assert palette_mgmt.palette_name == "Test Palette"
            assert len(palette_mgmt.colors) == 3

    async def test_update_palette(self, app_runner):
        """Test updating the palette data."""
        async with app_runner(self.PaletteManagementTestApp) as pilot:
            palette_mgmt = pilot.app.query_one("#palette-management", PaletteManagement)

            # Update palette with new data
            palette_mgmt.update_palette(
                palette_id="new-palette",
                palette_name="New Palette",
                colors=["#FFFF00", "#FF00FF"],
                active_color_index=1
            )

            # Check updated state
            assert palette_mgmt.palette_id == "new-palette"
            assert palette_mgmt.palette_name == "New Palette"
            assert len(palette_mgmt.colors) == 2
            assert palette_mgmt.active_color_index == 1

    async def test_color_selection(self, app_runner):
        """Test color selection in palette management."""
        async with app_runner(self.PaletteManagementTestApp) as pilot:
            palette_mgmt = pilot.app.query_one("#palette-management", PaletteManagement)

            # Initial active color index is 0
            assert palette_mgmt.active_color_index == 0

            # Find and click the second color slot
            # Note: For real tests, we would need to find the slot by ID and click it
            # For demonstration, we'll call the handler directly
            palette_mgmt._handle_color_slot_click(1)

            # Check that active color index changed
            assert palette_mgmt.active_color_index == 1

            # App should have received a message
            assert len(pilot.app.received_messages) > 0
            assert any(msg.index == 1 for msg in pilot.app.received_messages)


@pytest.fixture
def app_runner():
    """Provide a fixture for running textual apps in tests."""
    from textual.pilot import Pilot

    async def _app_runner(app_class):
        """Run a Textual app for testing."""
        app = app_class()
        async with Pilot(app) as pilot:
            return pilot

    return _app_runner


if __name__ == "__main__":
    pytest.main(["-v", "test_widgets.py"])
