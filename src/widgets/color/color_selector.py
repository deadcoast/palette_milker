# milky_color_suite/widgets/color/color_selector.py
from typing import Any
from typing import Optional
from typing import Union
from typing import cast

from rich.console import RenderableType
from rich.text import Text
from textual.app import App
from textual.app import ComposeResult
from textual.color import Color
from textual.color import ColorParseError
from textual.containers import Container
from textual.containers import Vertical
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Button
from textual.widgets import Input
from textual.widgets import Static


# Option 1: Simple Input Field: Use a standard Input widget where the user types the color code (HEX, RGB).
# Option 2: Predefined Swatches: Use a Container with several Button or Static widgets showing predefined colors.
# Option 3: Simple Sliders/Inputs: Use Input widgets or potentially custom slider widgets for H, S, L or R, G, B values.


class ColorSelector(Static):
    """Widget for selecting or inputting a color."""

    DEFAULT_CSS = """
    ColorSelector {
        border: thick $accent;
        padding: 1;
    }
    ColorSelector Input {
        margin-top: 1;
    }
    #color-preview {
        height: 3;
        border: round white;
        margin-bottom: 1;
    }
    """

    # Reactive property to hold the current color value as a string
    color_input = reactive("#ffffff")
    _active_color = reactive(Color.parse("#ffffff"))

    def compose(self) -> ComposeResult:
        yield Static(id="color-preview")
        yield Input(placeholder="Enter color (e.g., #ff00ff, rgb(0,255,0))", id="color-input-field")
        # Add other selection methods here (swatches, sliders etc.) if desired

    def on_mount(self) -> None:
        """Initial setup."""
        self.query_one(Input).value = self.color_input
        self._update_preview(self.color_input)
        try:
            color_swatch = self.query_one(ColorSwatch)
            color_swatch.color = str(self._active_color)
            self._update_display()
        except Exception:
            # ColorSwatch might not be available in this context
            pass

    def _update_preview(self, value: str):
        """Update the preview box color."""
        preview = self.query_one("#color-preview", Static)
        try:
            color = Color.parse(value)
            preview.styles.background = color
            # Set foreground for contrast - calculate luminance from RGB values
            # Extract RGB values directly from the color
            # Convert hex string to RGB components
            hex_color = color.hex
            # Remove the # and parse the hex values
            r = int(hex_color[1:3], 16)
            g = int(hex_color[3:5], 16)
            b = int(hex_color[5:7], 16)
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            preview.styles.color = "black" if luminance > 0.5 else "white"
            preview.renderable = Text(f"Preview: {value}")
        except ColorParseError:
            preview.styles.background = "darkred"
            preview.styles.color = "white"
            preview.renderable = Text("Invalid Color")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle changes in the color input field."""
        self.color_input = event.value
        self._update_preview(event.value)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle submission of the color input field."""
        try:
            new_color = Color.parse(event.value)
            # Post a message to update the app's active color
            self.post_message(ActiveColorChanged(new_color))
            self.notify(f"Color set to {new_color.hex}")
        except ColorParseError:
            self.notify("Invalid color format.", severity="error")

    # Watch the reactive input value if needed for other logic
    def watch_color_input(self, old_value: str, new_value: str) -> None:
        # This might be redundant if on_input_changed handles everything
        pass

    def _update_display(self) -> None:
        """Update the display of the color info widget."""
        try:
            color_swatch = self.query_one(ColorSwatch)
            color_swatch.color = str(self._active_color)
        except Exception:
            pass

        try:
            color_value = self.query_one("#color-value", Static)
            # Get color format from app if available, otherwise default to hex
            color_format = "hex"
            app_instance = cast(Any, self.app)
            if hasattr(app_instance, "color_format"):
                color_format = cast(str, app_instance.color_format)
            color_value.renderable = Text(color_format)
        except Exception:
            pass

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle format button clicks."""
        app_instance = cast(Any, self.app)
        if not hasattr(app_instance, "color_format"):
            return

        if event.button.id == "btn-hex":
            self.post_message(ColorFormatChanged("hex"))
        elif event.button.id == "btn-rgb":
            self.post_message(ColorFormatChanged("rgb"))
        elif event.button.id == "btn-hsl":
            self.post_message(ColorFormatChanged("hsl"))


class ColorSwatch(Static):
    """A color swatch widget that displays a colored rectangle."""

    DEFAULT_CSS = """
    ColorSwatch {
        width: 3;
        height: 1;
    }
    """

    color = reactive("#000000")

    def __init__(self, color: str = "#000000", id: Optional[str] = None, classes: Optional[str] = None):
        super().__init__(id=id, classes=classes)
        self.color = color

    def render(self) -> RenderableType:
        return Text(f"[{self.color}]███[/]")

    def watch_color(self, color: str) -> None:
        self.color = color


class ActiveColorChanged(Message):
    """Message sent when the active color changes."""

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()


class ColorFormatChanged(Message):
    """Message sent when the color format changes."""

    def __init__(self, format: str) -> None:
        self.format = format
        super().__init__()


class ColorInfo(Static):
    """Displays information about the currently active color."""

    DEFAULT_CSS = """
    ColorInfo {
        border: thick $accent;
        padding: 1;
        margin-top: 1;
    }
    #color-swatch {
        height: 3;
        border: round white;
        margin-bottom: 1;
    }
    #format-buttons Button {
        min-width: 5; /* Adjust as needed */
        margin-right: 1;
    }
    #color-value {
        margin-top: 1;
        border: thin $primary;
        padding: 0 1;
        text-align: center; /* Requires Textual > 0.48 */
        min-height: 1;
    }
    """

    # Internal reactive state to trigger updates if needed, or rely on app messages
    _active_color: reactive[Color] = reactive(Color.parse("white"))
    _color_format: reactive[str] = reactive("hex")

    def compose(self) -> ComposeResult:
        yield ColorSwatch(id="color-swatch")
        yield Static(id="color-value")
        yield Button("Hex", id="btn-hex")
        yield Button("RGB", id="btn-rgb")
        yield Button("HSL", id="btn-hsl")

    def on_mount(self) -> None:
        """Set up initial state when the widget is mounted."""
        self.query_one(ColorSwatch).color = str(self._active_color)
        self._update_display()

    def _update_display(self) -> None:
        """Update the display of the color info widget."""
        color_swatch = self.query_one(ColorSwatch)
        color_value = self.query_one("#color-value", Static)
        color_swatch.color = str(self._active_color)

        # Use local color format if app doesn't have it
        color_format = self._color_format
        app_instance = cast(Any, self.app)
        if hasattr(app_instance, "color_format"):
            color_format = cast(str, app_instance.color_format)

        color_value.renderable = Text(color_format)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle format button clicks."""
        format_value = None
        if event.button.id == "btn-hex":
            format_value = "hex"
        elif event.button.id == "btn-rgb":
            format_value = "rgb"
        elif event.button.id == "btn-hsl":
            format_value = "hsl"

        if format_value:
            # Update local state
            self._color_format = format_value
            # Inform app if possible
            self.post_message(ColorFormatChanged(format_value))
            # Update display
            self._update_display()
