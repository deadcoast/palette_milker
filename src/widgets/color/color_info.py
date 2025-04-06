# milky_color_suite/widgets/color/color_info.py
from typing import Any
from typing import cast

from textual.app import ComposeResult
from textual.color import Color
from textual.containers import Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Button
from textual.widgets import Static


class ActiveColorChanged(Message):
    """Message sent when the active color changes."""

    def __init__(self, color: Color) -> None:
        """Initialize with the new active color."""
        self.color = color
        super().__init__()


class ColorFormatChanged(Message):
    """Message sent when the color format changes."""

    def __init__(self, color_format: str) -> None:
        """Initialize with the new color format."""
        self.color_format = color_format
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
        yield Static(id="color-swatch")
        with Horizontal(id="format-buttons"):
            yield Button("HEX", id="btn-hex", variant="primary")  # Start with HEX active
            yield Button("RGB", id="btn-rgb")
            yield Button("HSL", id="btn-hsl")
        yield Static(id="color-value")

    def on_mount(self) -> None:
        """Set up the component when it's mounted and watch for relevant messages."""
        # Set initial state and update display
        self._set_initial_state()
        self._update_display()

    def on_active_color_changed(self, message: ActiveColorChanged) -> None:
        """Handle color change messages."""
        self._active_color = message.color
        self._update_display()

    def on_color_format_changed(self, message: ColorFormatChanged) -> None:
        """Handle format change messages."""
        self._color_format = message.color_format
        self._update_display()

    def _update_display(self) -> None:
        """Update the swatch and value based on current state."""
        color = self._active_color  # Use internal state or fetch from app
        color_format = self._color_format

        swatch = self.query_one("#color-swatch", Static)
        swatch.styles.background = color

        # Set text color for contrast - using RGB value for simple luminance check
        r, g, b = color.rgb
        is_dark = 0.299 * r + 0.587 * g + 0.114 * b < 127.5
        swatch.styles.color = "white" if is_dark else "black"

        # Update content
        swatch.renderable = f"Swatch: {color.hex}"  # Show hex on swatch for reference

        # Get the color string representation
        color_str = self._get_color_string(color, color_format)

        value_display = self.query_one("#color-value", Static)
        value_display.renderable = color_str

        # Update button variants
        hex_btn = self.query_one("#btn-hex", Button)
        rgb_btn = self.query_one("#btn-rgb", Button)
        hsl_btn = self.query_one("#btn-hsl", Button)

        hex_btn.variant = "primary" if color_format == "hex" else "default"
        rgb_btn.variant = "primary" if color_format == "rgb" else "default"
        hsl_btn.variant = "primary" if color_format == "hsl" else "default"

    def _set_initial_state(self) -> None:
        """Get initial state from the app if available."""
        app_instance = cast(Any, self.app)

        # Try to get values from app if they exist
        if hasattr(app_instance, "active_color"):
            self._active_color = app_instance.active_color

        if hasattr(app_instance, "color_format"):
            self._color_format = app_instance.color_format

    def _get_color_string(self, color: Color, color_format: str) -> str:
        """Get string representation of a color in the specified format."""
        app_instance = cast(Any, self.app)

        # Use app's method if available
        if hasattr(app_instance, "get_color_string"):
            # Explicitly cast the return value to ensure proper typing
            return cast(str, app_instance.get_color_string(color, color_format))

        # Fallback implementation
        if color_format == "hsl":
            return self._extracted_from__get_color_string_15(color)
        elif color_format == "rgb":
            r, g, b = color.rgb
            return f"rgb({r}, {g}, {b})"
        else:
            return color.hex

    # TODO Rename this here and in `_get_color_string`
    def _extracted_from__get_color_string_15(self, color: Color) -> str:
        # Simple HSL approximation
        import colorsys

        r, g, b = color.normalized
        h, lightness, s = colorsys.rgb_to_hls(r, g, b)  # Note: rgb_to_hls returns h,l,s
        h_deg = round(h * 360)
        s_pct = round(s * 100)
        l_pct = round(lightness * 100)
        return f"hsl({h_deg}, {s_pct}%, {l_pct}%)"

    # Handle button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle format button clicks."""
        app_instance = cast(Any, self.app)

        if event.button.id == "btn-hex":
            self._color_format = "hex"
            if hasattr(app_instance, "color_format"):
                app_instance.color_format = "hex"
            else:
                self.post_message(ColorFormatChanged("hex"))

        elif event.button.id == "btn-rgb":
            self._color_format = "rgb"
            if hasattr(app_instance, "color_format"):
                app_instance.color_format = "rgb"
            else:
                self.post_message(ColorFormatChanged("rgb"))

        elif event.button.id == "btn-hsl":
            self._color_format = "hsl"
            if hasattr(app_instance, "color_format"):
                app_instance.color_format = "hsl"
            else:
                self.post_message(ColorFormatChanged("hsl"))

        self._update_display()

    # Placeholder for Save to Palette button (add when Palette context exists)
    # yield Button("Save to Palette", id="btn-save-palette")
    # def on_button_pressed ... handle btn-save-palette
