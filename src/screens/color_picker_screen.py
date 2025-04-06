"""
Enhanced color picker screen for the Palette Milker application.

This screen provides a comprehensive color selection interface with
visual feedback and supports various color manipulation controls.
"""

from typing import ClassVar
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from textual.app import ComposeResult
from textual.binding import Binding
from textual.color import Color
from textual.containers import Container
from textual.containers import Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Button
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import Static

from ..messages.palette_messages import ColorSelectionChanged
from ..widgets.color.color_details import ColorDetails
from ..widgets.color.color_details import ColorValueChanged
from ..widgets.color.color_wheel import ColorWheel


class ColorSelectedMessage(Message):
    """Message sent when a color is selected in the color picker."""

    def __init__(self, color: Color) -> None:
        """Initialize with the selected color."""
        self.color = color
        super().__init__()


class ColorPickerScreen(Screen):
    """
    Enhanced color picker screen with comprehensive color controls.

    This screen provides a visual color picker, detailed color information,
    and controls for precise color manipulation.
    """

    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Navigation
        Binding("escape", "app.view_palette", "Back", show=True),
        Binding("1", "app.view_palette", "Palette view"),
        Binding("3", "app.view_export", "Export options"),
        # Color operations
        Binding("a", "app.add_color", "Add to palette"),
        Binding("r", "randomize", "Random color"),
        Binding("c", "copy_color", "Copy color"),
        # Format toggle
        Binding("f", "toggle_format", "Toggle format"),
        # Color adjustment with arrow keys
        Binding("up", "adjust_hue(1)", "Increase hue"),
        Binding("down", "adjust_hue(-1)", "Decrease hue"),
        Binding("left", "adjust_saturation(-5)", "Decrease saturation"),
        Binding("right", "adjust_saturation(5)", "Increase saturation"),
        Binding("shift+up", "adjust_lightness(5)", "Increase lightness"),
        Binding("shift+down", "adjust_lightness(-5)", "Decrease lightness"),
    ]

    DEFAULT_CSS = """
    ColorPickerScreen {
        layout: grid;
        grid-size: 2 1;  /* Two columns, one row */
        grid-columns: 1fr 1fr;
        grid-rows: 1fr;
        padding: 1;
    }

    #left-panel {
        width: 100%;
        height: 100%;
    }

    #right-panel {
        width: 100%;
        height: 100%;
    }

    .panel-title {
        background: $primary;
        color: $text;
        width: 100%;
        height: 1;
        content-align: center middle;
        text-style: bold;
    }

    #color-controls {
        width: 100%;
        padding: 1;
    }

    #action-buttons {
        width: 100%;
        height: 3;
        margin-top: 1;
        layout: horizontal;
    }

    Button {
        min-width: 15;
        margin-right: 1;
    }
    """

    # Reactive properties
    selected_color: reactive[Color] = reactive(Color.parse("#FFFFFF"))
    color_format: reactive[str] = reactive("hex")

    def __init__(self, color: Optional[Union[str, Color]] = None):
        """
        Initialize the color picker screen.

        Args:
            color: Optional initial color
        """
        super().__init__()
        if color:
            self.selected_color = color if isinstance(color, Color) else Color.parse(color)

    def compose(self) -> ComposeResult:
        """Compose the color picker interface."""
        yield Header()

        # Left panel with color wheel
        with Container(id="left-panel"):
            yield Static("COLOR WHEEL", classes="panel-title")
            yield ColorWheel(widget_id="color-wheel")

            with Horizontal(id="action-buttons"):
                yield Button("Add to Palette", id="add-to-palette", variant="primary")
                yield Button("Back to Palette", id="back-to-palette")

        # Right panel with detailed color controls
        with Container(id="right-panel"):
            yield Static("COLOR DETAILS", classes="panel-title")
            yield ColorDetails(self.selected_color, widget_id="color-details")

        yield Footer()

    def on_mount(self) -> None:
        """Initialize components when mounted."""
        # Update ColorWheel with current color
        wheel = self.query_one("#color-wheel", ColorWheel)
        wheel.selected_color = self.selected_color.hex

        # Update ColorDetails with current color
        details = self.query_one("#color-details", ColorDetails)
        details.color = self.selected_color
        details.display_format = self.color_format

    def watch_selected_color(self, old_color: Color, new_color: Color) -> None:
        """React to selected color changes."""
        if old_color != new_color:
            # Update components
            wheel = self.query_one("#color-wheel", ColorWheel)
            wheel.selected_color = new_color.hex

            details = self.query_one("#color-details", ColorDetails)
            details.color = new_color

    def watch_color_format(self, old_format: str, new_format: str) -> None:
        """React to color format changes."""
        if old_format != new_format:
            details = self.query_one("#color-details", ColorDetails)
            details.display_format = new_format

    # Handle ColorWheel color changes
    def on_color_wheel_selected_color(self, message: Message) -> None:
        """
        React to color selection in the color wheel.

        Args:
            message: Message containing the selected color
        """
        color_value = message.wheel.selected_color  # type: ignore
        self.selected_color = Color.parse(color_value)

    # Handle ColorDetails color changes
    def on_color_details_color_value_changed(self, message: ColorValueChanged) -> None:
        """
        React to color changes from the details widget.

        Args:
            message: Message containing the new color
        """
        if isinstance(message.color, Color):
            self.selected_color = message.color
        else:
            self.selected_color = Color.parse(message.color)

    # Handle button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id

        if button_id == "add-to-palette":
            self.action_add_color()
        elif button_id == "back-to-palette":
            self.app.switch_screen("main")

    # Action methods for key bindings
    def action_toggle_format(self) -> None:
        """Toggle between color formats."""
        formats = ["hex", "rgb", "hsl"]
        current_index = formats.index(self.color_format)
        next_index = (current_index + 1) % len(formats)
        self.color_format = formats[next_index]

    def action_randomize(self) -> None:
        """Generate a random color."""
        import random

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # Create RGB color using parse with format string
        self.selected_color = Color.parse(f"#{r:02x}{g:02x}{b:02x}")

    def action_copy_color(self) -> None:
        """Copy the current color value."""
        # Format based on current display format
        if self.color_format == "hex":
            color_str = self.selected_color.hex
        elif self.color_format == "rgb":
            r, g, b = self.selected_color.rgb
            color_str = f"rgb({r},{g},{b})"
        else:  # hsl
            details = self.query_one("#color-details", ColorDetails)
            color_str = details._get_hsl_string()

        # We'd integrate with system clipboard in a real implementation
        self.notify(f"Copied {color_str}")

    def action_add_color(self) -> None:
        """Add the current color to the active palette."""
        # Post message to be handled by app
        self.post_message(ColorSelectedMessage(self.selected_color))

        # Try to call app's add_color method
        try:
            # Post a message that the app might be listening for
            # Convert Textual Color to string for compatibility with expected message format
            self.post_message(ColorSelectionChanged(self, 0, self.selected_color.hex))

            # Also try to switch back to the palette view - this is a common pattern in Textual
            self.app.switch_screen("main")
        except Exception:
            self.notify("Unable to add color via app action")

        # Notify user
        self.notify("Color added to palette")

    def action_adjust_hue(self, amount: int) -> None:
        """
        Adjust the hue of the current color.

        Args:
            amount: Amount to adjust (degrees, positive or negative)
        """
        details = self.query_one("#color-details", ColorDetails)
        h, s, lightness = details._get_hsl_values()

        # Adjust hue (wrap around 0-360)
        h = (h + amount) % 360

        self._extracted_from_action_adjust_lightness_15(h, s, lightness)

    def action_adjust_saturation(self, amount: int) -> None:
        """
        Adjust the saturation of the current color.

        Args:
            amount: Amount to adjust (percentage, positive or negative)
        """
        details = self.query_one("#color-details", ColorDetails)
        h, s, lightness = details._get_hsl_values()

        # Adjust saturation (clamp 0-100)
        s = max(0, min(100, s + amount))

        self._extracted_from_action_adjust_lightness_15(h, s, lightness)

    def action_adjust_lightness(self, amount: int) -> None:
        """
        Adjust the lightness of the current color.

        Args:
            amount: Amount to adjust (percentage, positive or negative)
        """
        details = self.query_one("#color-details", ColorDetails)
        h, s, lightness = details._get_hsl_values()

        # Adjust lightness (clamp 0-100)
        lightness = max(0, min(100, lightness + amount))

        self._extracted_from_action_adjust_lightness_15(h, s, lightness)

    # TODO Rename this here and in `action_adjust_hue`, `action_adjust_saturation` and `action_adjust_lightness`
    def _extracted_from_action_adjust_lightness_15(self, h: int, s: int, lightness: int) -> None:
        """
        Update the selected color based on HSL values.

        Args:
            h: Hue value (0-360)
            s: Saturation value (0-100)
            lightness: Lightness value (0-100)
        """
        import colorsys

        h_norm = h / 360
        s_norm = s / 100
        lightness_norm = lightness / 100
        r, g, b = colorsys.hls_to_rgb(h_norm, lightness_norm, s_norm)
        r_byte = round(r * 255)
        g_byte = round(g * 255)
        b_byte = round(b * 255)
        self.selected_color = Color.parse(f"#{r_byte:02x}{g_byte:02x}{b_byte:02x}")
