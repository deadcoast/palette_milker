"""
ColorWheel widget for color selection.

This module provides a color wheel widget that allows users to select colors
visually or input hex values.
"""

from typing import Callable
from typing import List
from typing import Optional

from textual import events
from textual.app import ComposeResult
from textual.containers import Container
from textual.containers import Horizontal
from textual.containers import Vertical
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button
from textual.widgets import Input
from textual.widgets import Static


class HexInput(Input):
    """Input field for HEX color values with prompt."""

    DEFAULT_CSS = """
    HexInput {
        width: 100%;
        height: 1;
        content-align: left middle;
    }
    """

    def __init__(
        self,
        value: str = "",
        on_change: Optional[Callable[[str], None]] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None
    ):
        """
        Initialize a hex input field.

        Args:
            value: Initial hex value
            on_change: Optional callback for value changes
            id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(value, id=id, classes=classes)
        self.on_change_callback = on_change

    def compose(self) -> ComposeResult:
        """Compose the input with a HEX prompt."""
        yield Static("~HEX:\\>", classes="hex-prompt")

    def watch_value(self, value: str) -> None:
        """Watch for value changes and call the callback."""
        if self.on_change_callback:
            self.on_change_callback(value)


class ColorSwatch(Static):
    """A color swatch that displays a colored rectangle."""

    DEFAULT_CSS = """
    ColorSwatch {
        width: 3;
        height: 1;
    }
    """

    color = reactive("#000000")

    def __init__(
        self,
        color: str = "#000000",
        id: Optional[str] = None,
        classes: Optional[str] = None
    ):
        """
        Initialize a color swatch.

        Args:
            color: The color value (hex)
            id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__("", id=id, classes=classes)
        self.color = color

    def render(self) -> str:
        """Render a colored block."""
        return "███"

    def watch_color(self, color: str) -> None:
        """Update styles when color changes."""
        self.styles.background = color


class ColorWheel(Container):
    """A color wheel widget for selecting colors."""

    DEFAULT_CSS = """
    ColorWheel {
        width: 100%;
        height: auto;
        border: double $primary;
    }

    ColorWheel .header {
        height: 1;
        width: 100%;
        background: $primary;
        color: $text;
        text-align: center;
    }

    ColorWheel .color-grid {
        width: 100%;
        height: auto;
        min-height: 10;
    }

    ColorWheel .footer {
        height: 1;
        width: 100%;
    }

    ColorWheel .tools {
        width: 100%;
        height: 1;
    }
    """

    selected_color = reactive("#000000")

    def __init__(
        self,
        title: str = "COLOR WHEEL",
        id: Optional[str] = None,
        classes: Optional[str] = None
    ):
        """
        Initialize a color wheel widget.

        Args:
            title: Title for the color wheel
            id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=id, classes=classes)
        self.title = title

    def compose(self) -> ComposeResult:
        """Compose the color wheel widget."""
        # Header with controls and title
        with Horizontal(classes="header"):
            yield Button("[↕]", classes="resize")
            yield Button("[▼]", classes="dropdown")
            yield Static(self.title, classes="title")

        # Color grid
        with Container(classes="color-grid"):
            # This would be a dynamic grid of color samples in the real implementation
            for r in range(16):
                with Horizontal():
                    for g in range(16):
                        color = f"#{r:x}{g:x}8"
                        yield ColorSwatch(color, classes="swatch")

        # Footer with hex input
        with Container(classes="footer"):
            yield HexInput(
                value=self.selected_color,
                on_change=self._on_hex_change,
                id="hex-input"
            )

    def _on_hex_change(self, value: str) -> None:
        """Handle hex input changes."""
        if value.startswith("#") and (len(value) == 4 or len(value) == 7):
            try:
                # Validate the hex color
                int(value[1:], 16)
                self.selected_color = value
            except ValueError:
                pass

    def on_click(self, event: events.Click) -> None:
        """Handle clicks on color swatches."""
        if isinstance(event.widget, ColorSwatch):
            self.selected_color = event.widget.color
            self.query_one("#hex-input", HexInput).value = self.selected_color
