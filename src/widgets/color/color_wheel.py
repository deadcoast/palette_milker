"""
ColorWheel widget for color selection.

This module provides a color wheel widget that allows users to select colors
visually or input hex values.
"""

from typing import Callable
from typing import ClassVar
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union
from typing import cast

from textual import events
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.containers import Horizontal
from textual.reactive import reactive
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
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ColorInput.

        Args:
            value: Initial color value
            on_change: Callback for when the color changes
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
        self.value = value
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

    def __init__(self, color: str = "#000000", widget_id: Optional[str] = None, classes: Optional[str] = None):
        """
        Initialize a color swatch.

        Args:
            color: The color to display (hex format)
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__("", id=widget_id, classes=classes)
        self.color = color

    def render(self) -> str:
        """Render a colored block."""
        return "███"

    def watch_color(self, color: str) -> None:
        """Update styles when color changes."""
        self.styles.background = color


class ColorWheel(Container):
    """A color wheel widget for selecting colors."""

    # Add key bindings for the color wheel
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        Binding("up", "move_selection_up", "Move up", show=False),
        Binding("down", "move_selection_down", "Move down", show=False),
        Binding("left", "move_selection_left", "Move left", show=False),
        Binding("right", "move_selection_right", "Move right", show=False),
        Binding("c", "copy_color", "Copy color"),
        Binding("r", "randomize_color", "Random color"),
        Binding("b", "brighten_color", "Brighten"),
        Binding("d", "darken_color", "Darken"),
    ]

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

    ColorWheel .selected {
        border: solid white;
    }
    """

    selected_color = reactive("#000000")
    selected_row = reactive(0)
    selected_col = reactive(0)

    def __init__(self, title: str = "COLOR WHEEL", widget_id: Optional[str] = None, classes: Optional[str] = None):
        """
        Initialize a color wheel widget.

        Args:
            title: Title for the color wheel
            widget_id: Widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
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
            yield HexInput(value=self.selected_color, on_change=self._on_hex_change, widget_id="hex-input")

    def watch_selected_row(self, old_row: int, new_row: int) -> None:
        """Update the UI when the selected row changes."""
        self._update_selected_swatch()

    def watch_selected_col(self, old_col: int, new_col: int) -> None:
        """Update the UI when the selected column changes."""
        self._update_selected_swatch()

    def _update_selected_swatch(self) -> None:
        """Update the visual selection in the color grid."""
        # Remove the 'selected' class from all swatches
        for swatch in self.query(".swatch"):
            swatch.remove_class("selected")

        # Calculate the index of the selected swatch
        index = self.selected_row * 16 + self.selected_col

        try:
            # Get all swatches
            swatches = list(self.query(".swatch"))
            if index < len(swatches):
                # Add the 'selected' class to the selected swatch
                swatch = swatches[index]
                swatch.add_class("selected")
                # Update the selected color - cast to ColorSwatch to access color property
                swatch_obj = cast(ColorSwatch, swatch)
                self.selected_color = swatch_obj.color
                # Update the hex input
                self.query_one("#hex-input", HexInput).value = self.selected_color
        except Exception as e:
            self.log(f"Error updating selected swatch: {e}")

    def _on_hex_change(self, value: str) -> None:
        """Handle hex input changes."""
        if value.startswith("#") and len(value) in [4, 7]:
            try:
                # Validate the hex color
                int(value[1:], 16)
                self.selected_color = value
            except ValueError:
                pass

    def on_click(self, event: events.Click) -> None:
        """Handle clicks on color swatches."""
        if isinstance(event.widget, ColorSwatch):
            # Get the color swatch
            swatch = event.widget

            # Update the selected color
            self.selected_color = swatch.color
            self.query_one("#hex-input", HexInput).value = self.selected_color

            # Find and update the row and column of the clicked swatch
            swatches = list(self.query(".swatch"))
            if swatch in swatches:
                index = swatches.index(swatch)
                self.selected_row, self.selected_col = divmod(index, 16)

    # Action methods for the bindings
    def action_move_selection_up(self) -> None:
        """Move the selection up."""
        self.selected_row = max(0, self.selected_row - 1)

    def action_move_selection_down(self) -> None:
        """Move the selection down."""
        self.selected_row = min(15, self.selected_row + 1)

    def action_move_selection_left(self) -> None:
        """Move the selection left."""
        self.selected_col = max(0, self.selected_col - 1)

    def action_move_selection_right(self) -> None:
        """Move the selection right."""
        self.selected_col = min(15, self.selected_col + 1)

    def action_copy_color(self) -> None:
        """Copy the selected color to clipboard."""
        # In a real app, this would copy to the clipboard
        self.notify(f"Color copied: {self.selected_color}")

    def action_randomize_color(self) -> None:
        """Set a random color."""
        import random

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        new_color = f"#{r:02x}{g:02x}{b:02x}"
        self.selected_color = new_color
        self.query_one("#hex-input", HexInput).value = new_color

    def action_brighten_color(self) -> None:
        """Brighten the current color."""
        # Simple brightening by adding 10% white
        try:
            color = self.selected_color.lstrip("#")
            r = min(255, int(color[:2], 16) + 25)
            g = min(255, int(color[2:4], 16) + 25)
            b = min(255, int(color[4:6], 16) + 25)
            new_color = f"#{r:02x}{g:02x}{b:02x}"
            self.selected_color = new_color
            self.query_one("#hex-input", HexInput).value = new_color
        except Exception as e:
            self.log(f"Error brightening color: {e}")

    def action_darken_color(self) -> None:
        """Darken the current color."""
        # Simple darkening by removing 10%
        try:
            color = self.selected_color.lstrip("#")
            r = max(0, int(color[:2], 16) - 25)
            g = max(0, int(color[2:4], 16) - 25)
            b = max(0, int(color[4:6], 16) - 25)
            new_color = f"#{r:02x}{g:02x}{b:02x}"
            self.selected_color = new_color
            self.query_one("#hex-input", HexInput).value = new_color
        except Exception as e:
            self.log(f"Error darkening color: {e}")
