# milky_color_suite/main.py
from textual.app import App
from .screens.main_screen import MainScreen
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.color import Color  # Use Textual's Color class
import json
import uuid
from pathlib import Path
from textual.app import App, ComposeResult  # ... other imports
from textual.reactive import reactive
from textual.color import Color
"""
Palette Milker - A Textual TUI Color Palette Manager

This application allows users to create, edit, and manage color palettes
with an ASCII-art styled interface.
"""

from typing import Dict
from typing import List
from typing import Optional

from textual.app import App
from textual.app import ComposeResult
from textual.containers import Container
from textual.containers import Horizontal
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Footer
from textual.widgets import Header

from widgets.color_wheel import ColorWheel
from widgets.palette_management import ColorSlot
from widgets.palette_management import PaletteManagement


class PaletteMilkerApp(App):
    """The main Palette Milker application."""

    TITLE = "Palette Milker"
    CSS_PATH = "app.tcss"

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("n", "new_palette", "New Palette"),
        ("r", "rename_palette", "Rename Palette"),
        ("e", "export", "Export"),
        ("c", "copy_color", "Copy Color"),
    ]

    # Sample palettes for demonstration
    SAMPLE_PALETTES = {
        "Default": ["#FF5500", "#00AAFF", "#55FF00", "#AA00FF", "#FFAA00", "#00FFAA", "#FF0055", "#00FF55"],
        "Monochrome": ["#FFFFFF", "#DDDDDD", "#BBBBBB", "#999999", "#777777", "#555555", "#333333", "#000000"],
        "Sunset": ["#FF7700", "#FF5500", "#FF0000", "#DD0000", "#AA0000", "#880000", "#550000", "#220000"],
    }

    def __init__(self):
        """Initialize the application."""
        super().__init__()
        self.palettes = self.SAMPLE_PALETTES.copy()
        self.current_palette = "Default"
        self.current_color = self.palettes[self.current_palette][0]
        self._dark = True  # Initialize dark mode setting

    def compose(self) -> ComposeResult:
        """Compose the main application UI."""
        # Header and Footer
        yield Header()
        yield Footer()

        # Main layout
        with Container(id="main-container"):
            # Left sidebar - Tree browser
            with Container(id="left-sidebar"):
                yield Static("╠───────────────╦", classes="sidebar-header-top")
                yield Static("│ (⊕) Browse    │", classes="sidebar-header")
                yield Static("╠───────────────╝", classes="sidebar-header-bottom")

                # Palettes section
                yield Static("│ ▼ Palettes    │", classes="browse-section-header")
                for palette in self.palettes:
                    yield Static(f"│    {palette.ljust(11)}│", id=f"browse-{palette}", classes="browse-item")
                yield Static("│               │", classes="browse-spacer")

                # Arrays section
                yield Static("│  ▼ Arrays     │", classes="browse-section-header")
                yield Static("│     UTTERS    │", classes="browse-item")
                yield Static("│     RGB       │", classes="browse-item")
                yield Static("│     HEX       │", classes="browse-item")
                yield Static("│               │", classes="browse-spacer")

            # Main content area
            with Container(id="main-content"):
                # Color wheel
                yield ColorWheel(title="COLOR WHEEL", id="color-wheel")

                # Palette management
                yield PaletteManagement(palettes=self.palettes, id="palette-management")

    def on_mount(self) -> None:
        """Handle application mount event."""
        self.title = "Palette Milker - ASCII TUI Color Palette Manager"

        # Set initial theme
        self.dark = self._dark

        # Set initial palette and color
        palette_mgmt = self.query_one("#palette-management", PaletteManagement)
        palette_mgmt.current_palette = self.current_palette

        # Set the active color in the ColorWheel
        color_wheel = self.query_one("#color-wheel", ColorWheel)
        color_wheel.selected_color = self.current_color

    def action_toggle_dark(self) -> None:
        """Toggle between light and dark mode."""
        self.dark = not self.dark

    def action_new_palette(self) -> None:
        """Create a new palette."""
        # In a real implementation, this would show a dialog
        palette_name = f"Palette{len(self.palettes) + 1}"
        self.palettes[palette_name] = ["#000000"] * 8

        # Update the UI
        palette_mgmt = self.query_one("#palette-management", PaletteManagement)
        palette_mgmt.palettes = self.palettes
        palette_mgmt.current_palette = palette_name
        self.refresh()

    def action_rename_palette(self) -> None:
        """Rename the current palette."""
        # In a real implementation, this would show a dialog
        self.notify("Palette renamed")

    def action_export(self) -> None:
        """Export the current palette."""
        # In a real implementation, this would show export options
        self.notify(f"Exported palette: {self.current_palette}")

    def action_copy_color(self) -> None:
        """Copy the current color to clipboard."""
        # In a real implementation, this would copy to clipboard
        self.notify(f"Copied color: {self.current_color}")


class Static(Container):
    """A simple static text widget that can display ASCII art."""

    def __init__(self, text: str, id: Optional[str] = None, classes: Optional[str] = None):
        """
        Initialize a static text widget.

        Args:
            text: The text to display
            id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=id, classes=classes)
        self.text = text

    def render(self) -> str:
        """Render the text content."""
        return self.text


# Define data path
DATA_DIR = Path(__file__).parent / "data"
PALETTES_FILE = DATA_DIR / "palettes.json"
CSS_PATH = "app.tcss"  # Optional: Load main CSS
SCREENS = {"main": MainScreen()}


def create_empty_palette(name="Untitled Palette") -> dict:
    """Creates a new palette structure."""
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        # Store colors as hex strings for JSON serialization
        "colors": ["#ffffff"] * 8,
        "createdAt": datetime.now().isoformat(),  # Use datetime
    }

# --- Custom Messages ---
class PalettesChanged(App.Message):
    pass

class ActivePaletteChanged(App.Message):
    def __init__(self, palette_id: str | None) -> None:
        self.palette_id = palette_id
        super().__init__()

class ActiveSlotChanged(App.Message):
    def __init__(self, slot_index: int) -> None:
        self.slot_index = slot_index
        super().__init__()

def on_mount(self) -> None:
    """Called when the app is mounted."""
    self.push_screen("main")


if __name__ == "__main__":
    app = PaletteMilkerApp()
    app.run()
