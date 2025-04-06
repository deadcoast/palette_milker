"""
Color manipulation widgets for the Milky Color Suite.

This module contains widgets related to color selection and manipulation,
providing the exact terminal-based UI design specified.
"""

import itertools
from typing import ClassVar
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from rich.console import RenderableType
from rich.text import Text
from textual import events
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.containers import Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button
from textual.widgets import Static

# Import Color class from our own models
from src.models.color_model import Color


# These imports require custom modules to be in the project's path
# from ascii.ascii_patterns import create_color_wheel
# from ascii.ascii_patterns import create_text_input
# from .ascii_widget import ASCIIWidget


# Temporary placeholder function until the actual imports are available
def create_text_input(label: str, value: str) -> str:
    """Placeholder for the actual create_text_input function."""
    return f"{label}> {value}"


class ColorWheel(Container):
    """
    A terminal-based color wheel widget.

    This widget displays a grid of colors for selection and includes
    controls for precise color input and selection.
    """

    DEFAULT_CSS = """
    ColorWheel {
        width: 60;
        height: 16;
        background: #FFFFFF;
    }

    ColorWheel #hex-input {
        dock: bottom;
        width: 100%;
        height: 1;
    }

    ColorWheel #color-grid {
        width: 100%;
        height: 12;
        background: #FFFFFF;
    }

    ColorWheel .controls {
        dock: top;
        width: 100%;
        height: 1;
    }
    """

    selected_color: reactive[Color] = reactive(Color("#FFFFFF"))
    width: reactive[int] = reactive(60)
    height: reactive[int] = reactive(16)

    def __init__(
        self,
        selected_color: str = "#FFFFFF",
        width: int = 60,
        height: int = 16,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ColorWheel widget.

        Args:
            selected_color: Initial selected color (hex string)
            width: Width of the color wheel
            height: Height of the color wheel
            name: The name of the widget
            widget_id: The ID of the widget (renamed from 'id')
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.selected_color = Color(selected_color)
        self.width = width
        self.height = height
        self.color_grid: Dict[Tuple[int, int], Color] = {}
        self._generate_color_grid()

    def _generate_color_grid(self) -> None:
        """Generate a grid of colors for the color wheel."""
        # Grid dimensions (excluding borders and header/footer)
        grid_width = self.width - 4
        grid_height = self.height - 7

        s = 1.0
        # Create a color grid mapped to coordinates
        for y, x in itertools.product(range(grid_height), range(grid_width)):
            # Normalize to 0-1 range
            h = x / grid_width
            v = 1.0 - (y / grid_height)

            # Create a color from HSV
            try:
                # Hue, Saturation, Value to RGB conversion
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

                # Create color object
                color = Color({"r": r * 255, "g": g * 255, "b": b * 255})
                self.color_grid[x, y] = color
            except ValueError:
                # Fallback if color creation fails
                self.color_grid[x, y] = Color("#000000")

    def compose(self) -> ComposeResult:
        """Compose the ColorWheel widget."""
        # ASCII frame using the pattern

        # Controls in the header
        with Horizontal(classes="controls"):
            yield Button("[⨀]", id="dropper-button", classes="dropper")
            yield Button("[save]", id="save-button", classes="save")

        yield Static(id="color-grid")
        # Hex input area
        yield ColorInput(current_color=self.selected_color.hex, widget_id="hex-input")

    def on_mount(self) -> None:
        """Handle the mount event."""
        self._render_color_grid()

    def _render_color_grid(self) -> None:
        """Render the color grid with the current colors."""
        # In a real implementation, this would render each color in the grid
        # in its correct position, allowing for selection
        pass

    def on_click(self, event: events.Click) -> None:
        """
        Handle click events on the color grid.

        Args:
            event: The click event
        """
        # Calculate click position relative to color grid
        try:
            # Since we can't directly check event.sender or event.target,
            # we'll just check if we have the offset attribute and use that
            if hasattr(event, "offset"):
                x, y = event.offset

                # Convert to grid coordinates
                grid_x = int(x)
                grid_y = int(y)

                # Check if valid coordinates
                if (grid_x, grid_y) in self.color_grid:
                    # Update selected color
                    self.selected_color = self.color_grid[grid_x, grid_y]

                    # Update hex input
                    hex_input = self.query_one("#hex-input", ColorInput)
                    hex_input.current_color = self.selected_color.hex

                    # Notify of color selection
                    self.post_message(self.ColorSelected(self.selected_color))
        except Exception:
            # Gracefully handle any errors in click handling
            pass

    def on_color_input_changed(self, message: "ColorInput.ColorChanged") -> None:
        """
        Handle color input changes.

        Args:
            message: The color changed message
        """
        try:
            self.selected_color = message.color
            self.post_message(self.ColorSelected(self.selected_color))
        except Exception:
            # Gracefully handle any errors in color input
            pass

    class ColorSelected(Message):
        """Message sent when a color is selected."""

        def __init__(self, color: Color) -> None:
            """
            Initialize the ColorSelected message.

            Args:
                color: The selected color
            """
            self.color = color
            super().__init__()


class ColorDropper(Widget):
    """
    A color dropper tool for selecting colors from the terminal.

    This provides a way to select colors from anywhere in the terminal
    by clicking on the desired color.
    """

    DEFAULT_CSS = """
    ColorDropper {
        background: #FFFFFF;
    }
    """

    active: reactive[bool] = reactive(False)

    def __init__(self, name: Optional[str] = None, widget_id: Optional[str] = None, classes: Optional[str] = None):
        """
        Initialize the ColorDropper widget.

        Args:
            name: The name of the widget
            widget_id: The ID of the widget (renamed from 'id')
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)

    def render(self) -> RenderableType:
        """Render the ColorDropper widget."""
        return Text("[⨀]", style="bold" if self.active else "")

    def on_click(self, event: events.Click) -> None:
        """
        Handle click events.

        Args:
            event: The click event
        """
        self.active = not self.active
        self.post_message(self.DropperToggled(self.active))
        self.refresh()

    class DropperToggled(Message):
        """Message sent when the dropper is toggled."""

        def __init__(self, active: bool) -> None:
            """
            Initialize the DropperToggled message.

            Args:
                active: Whether the dropper is active
            """
            self.active = active
            super().__init__()


class ColorInput(Widget):
    """
    A specialized input widget for entering color values.

    This widget validates and formats color inputs, and provides
    visual feedback for the current color.
    """

    DEFAULT_CSS = """
    ColorInput {
        height: 1;
        width: 100%;
    }
    """

    # Define key bindings
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        Binding("enter", "apply_color", "Apply"),
        Binding("escape", "reset_color", "Reset"),
        Binding("backspace", "backspace", "Delete"),
    ]

    current_color: reactive[str] = reactive("#FFFFFF")

    def __init__(
        self,
        current_color: str = "#FFFFFF",
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ColorInput widget.

        Args:
            current_color: Initial color (hex string)
            name: The name of the widget
            widget_id: The ID of the widget (renamed from 'id')
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.current_color = current_color
        self._input_text = current_color.lstrip("#")

    def render(self) -> RenderableType:
        """Render the ColorInput widget."""
        return Text(create_text_input("HEX", self._input_text))

    def action_apply_color(self) -> None:
        """Validate and apply the entered color."""
        self._validate_and_apply()

    def action_reset_color(self) -> None:
        """Reset to the current color."""
        self._input_text = self.current_color.lstrip("#")
        self.refresh()

    def action_backspace(self) -> None:
        """Remove the last character."""
        self._input_text = self._input_text[:-1]
        self.refresh()

    def on_key(self, event: events.Key) -> None:
        """
        Handle key events for hex characters input.

        Args:
            event: The key event
        """
        # Handle hex character input (not covered by bindings)
        if len(event.key) == 1 and event.key.lower() in "0123456789abcdef":
            self._input_text += event.key
            # Limit to 6 characters
            self._input_text = self._input_text[-6:]
            self.refresh()

            # Prevent default handling
            event.prevent_default()
            event.stop()

    def _validate_and_apply(self) -> None:
        """Validate and apply the entered color."""
        try:
            # Ensure correct hex format
            hex_value = self._input_text
            if len(hex_value) == 3:
                # Expand shorthand notation (e.g., #FFF to #FFFFFF)
                hex_value = "".join(c + c for c in hex_value)

            # Pad to 6 characters if needed
            hex_value = hex_value.ljust(6, "0")

            # Create color object to validate
            color = Color(f"#{hex_value}")

            # Update current color
            self.current_color = color.hex

            # Notify of color change
            self.post_message(self.ColorChanged(color))
        except ValueError:
            # Reset to current color on error
            self._input_text = self.current_color.lstrip("#")
            self.refresh()

    def watch_current_color(self, current_color: str) -> None:
        """
        Watch for changes to the current color.

        Args:
            current_color: The new current color
        """
        self._input_text = current_color.lstrip("#")
        self.refresh()

    class ColorChanged(Message):
        """Message sent when the color is changed."""

        def __init__(self, color: Color) -> None:
            """
            Initialize the ColorChanged message.

            Args:
                color: The new color
            """
            self.color = color
            super().__init__()
            super().__init__()
