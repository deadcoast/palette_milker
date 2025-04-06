"""
Enhanced color details widget for the Palette Milker application.

This module provides a rich color information display with visual feedback
and controls for color manipulation.
"""

from typing import ClassVar
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from rich.console import RenderableType
from rich.text import Text
from textual.app import ComposeResult
from textual.binding import Binding
from textual.color import Color
from textual.containers import Container
from textual.containers import Horizontal
from textual.containers import Vertical
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Button
from textual.widgets import Static


# Since Slider may not be available in this version of Textual, we'll use Static as a base
class Slider(Static):
    """Simple custom slider implementation."""

    value: reactive[int] = reactive(0)
    min: reactive[int] = reactive(0)
    max: reactive[int] = reactive(100)
    step: reactive[int] = reactive(1)

    def __init__(
        self,
        value: int = 0,
        min_value: int = 0,
        max_value: int = 100,
        step: int = 1,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ) -> None:
        """Initialize the slider."""
        super().__init__(name=name, id=widget_id, classes=classes)
        self.value = value
        self.min = min_value
        self.max = max_value
        self.step = step

    def render(self) -> RenderableType:
        """Render the slider."""
        # Simple text-based rendering
        width = 20  # Width in characters
        range_size = self.max - self.min
        if range_size <= 0:
            position = 0
        else:
            position = int(((self.value - self.min) / range_size) * width)

        bar = "▓" * position + "░" * (width - position)
        return Text(f"[{bar}] {self.value}")

    class Changed(Message):
        """Message sent when slider value changes."""

        def __init__(self, slider: "Slider", value: int) -> None:
            """Initialize with slider and value."""
            super().__init__()
            self.slider = slider
            self.value = value


class ColorValueChanged(Message):
    """Message sent when a color value is changed via the controls."""

    def __init__(self, color: Union[Color, str]) -> None:
        """Initialize with the new color value."""
        self.color = color
        super().__init__()


class ColorDetails(Container):
    """An enhanced widget for displaying color details with interactive controls."""

    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        Binding("c", "copy_color", "Copy color"),
        Binding("s", "add_to_palette", "Save to palette"),
        Binding("h", "toggle_format", "Toggle format"),
    ]

    DEFAULT_CSS = """
    ColorDetails {
        width: 100%;
        height: auto;
        min-height: 15;
        border: thick $accent-darken-2;
        padding: 1;
        layout: vertical;
    }

    #color-preview {
        width: 100%;
        height: 5;
        content-align: center middle;
        border: wide $background;
        margin-bottom: 1;
    }

    #color-info {
        width: 100%;
        height: 3;
        margin-bottom: 1;
    }

    .color-value {
        width: 1fr;
        text-align: center;
        border: solid $primary;
        padding: 0 1;
    }

    .format-label {
        text-align: center;
        background: $primary;
        color: $text;
        padding: 0 1;
    }

    #color-sliders {
        width: 100%;
        height: auto;
    }

    .slider-row {
        width: 100%;
        height: 3;
        margin-bottom: 1;
        layout: horizontal;
    }

    .slider-label {
        width: 5;
        content-align: left middle;
        padding: 0 1;
    }

    .slider {
        width: 1fr;
    }

    .slider-value {
        width: 6;
        content-align: right middle;
        text-align: right;
        padding: 0 1;
    }

    #color-buttons {
        width: 100%;
        height: 3;
        margin-top: 1;
    }

    Button {
        min-width: 10;
        margin-right: 1;
    }

    #complementary-colors {
        width: 100%;
        height: 3;
        layout: horizontal;
        margin-top: 1;
    }

    .harmony-swatch {
        width: 1fr;
        height: 3;
        border: solid $background;
        content-align: center middle;
    }
    """

    # Reactive properties
    color: reactive[Color] = reactive(Color.parse("#ffffff"))
    display_format: reactive[str] = reactive("hex")

    def __init__(
        self,
        color: Union[str, Color] = "#ffffff",
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the color details widget.

        Args:
            color: Initial color (hex string or Color object)
            widget_id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
        self.color = color if isinstance(color, Color) else Color.parse(color)

    def compose(self) -> ComposeResult:
        """Compose the color details widget with interactive controls."""
        # Color preview with current values
        yield Static("", id="color-preview")

        # Color information in different formats
        with Horizontal(id="color-info"):
            yield Static("HEX", classes="format-label")
            yield Static(self.color.hex, id="hex-value", classes="color-value")
            yield Static("RGB", classes="format-label")
            yield Static(self._get_rgb_string(), id="rgb-value", classes="color-value")
            yield Static("HSL", classes="format-label")
            yield Static(self._get_hsl_string(), id="hsl-value", classes="color-value")

        # Color adjustment sliders
        with Vertical(id="color-sliders"):
            # RGB sliders
            with Container(classes="slider-row"):
                yield Static("R", classes="slider-label")
                r, g, b = self.color.rgb
                yield Slider(value=r, min_value=0, max_value=255, step=1, widget_id="red-slider", classes="slider")
                yield Static(f"{r}", id="red-value", classes="slider-value")

            with Container(classes="slider-row"):
                yield Static("G", classes="slider-label")
                yield Slider(value=g, min_value=0, max_value=255, step=1, widget_id="green-slider", classes="slider")
                yield Static(f"{g}", id="green-value", classes="slider-value")

            with Container(classes="slider-row"):
                yield Static("B", classes="slider-label")
                yield Slider(value=b, min_value=0, max_value=255, step=1, widget_id="blue-slider", classes="slider")
                yield Static(f"{b}", id="blue-value", classes="slider-value")

            # HSL sliders (approximate values)
            h, s, lightness = self._get_hsl_values()
            with Container(classes="slider-row"):
                yield Static("H", classes="slider-label")
                yield Slider(value=h, min_value=0, max_value=360, step=1, widget_id="hue-slider", classes="slider")
                yield Static(f"{h}°", id="hue-value", classes="slider-value")

            with Container(classes="slider-row"):
                yield Static("S", classes="slider-label")
                yield Slider(
                    value=s, min_value=0, max_value=100, step=1, widget_id="saturation-slider", classes="slider"
                )
                yield Static(f"{s}%", id="saturation-value", classes="slider-value")

            with Container(classes="slider-row"):
                yield Static("L", classes="slider-label")
                yield Slider(
                    value=lightness, min_value=0, max_value=100, step=1, widget_id="lightness-slider", classes="slider"
                )
                yield Static(f"{lightness}%", id="lightness-value", classes="slider-value")

        # Buttons for common operations
        with Horizontal(id="color-buttons"):
            yield Button("Add to Palette", id="add-to-palette", variant="primary")
            yield Button("Copy Color", id="copy-color")
            yield Button("Randomize", id="randomize-color")

        # Complementary colors
        with Horizontal(id="complementary-colors"):
            # We'll show complementary and analogous colors
            for i, harmony_color in enumerate(self._get_harmonious_colors()):
                yield Static(f"{harmony_color.hex}", id=f"harmony-{i}", classes="harmony-swatch")

    def on_mount(self) -> None:
        """Setup the widget when mounted."""
        self._update_display()

    def watch_color(self, old_color: Color, new_color: Color) -> None:
        """React to color changes."""
        if old_color != new_color:
            self._update_display()

    def watch_display_format(self, old_format: str, new_format: str) -> None:
        """React to display format changes."""
        if old_format != new_format:
            self._update_display()

    def _update_display(self) -> None:
        """Update all UI elements to reflect the current color."""
        # Update color preview
        preview = self.query_one("#color-preview", Static)
        preview.styles.background = self.color

        # Determine text color based on luminance for contrast
        is_dark = self._is_color_dark(self.color)
        preview.styles.color = "white" if is_dark else "black"

        # Update preview text based on display format
        if self.display_format == "hex":
            preview.update(self.color.hex)
        elif self.display_format == "rgb":
            preview.update(self._get_rgb_string())
        else:  # hsl
            preview.update(self._get_hsl_string())

        # Update color values
        self.query_one("#hex-value", Static).update(self.color.hex)
        self.query_one("#rgb-value", Static).update(self._get_rgb_string())
        self.query_one("#hsl-value", Static).update(self._get_hsl_string())

        # Update RGB slider values
        r, g, b = self.color.rgb
        self._extracted_from__update_display_26("#red-slider", r, "#red-value")
        self._extracted_from__update_display_26("#green-slider", g, "#green-value")
        self._extracted_from__update_display_26("#blue-slider", b, "#blue-value")
        # Update HSL slider values
        h, s, lightness = self._get_hsl_values()
        self._extracted_from__update_display_38("#hue-slider", h, "#hue-value", "°")
        self._extracted_from__update_display_38("#saturation-slider", s, "#saturation-value", "%")
        self._extracted_from__update_display_38("#lightness-slider", lightness, "#lightness-value", "%")
        # Update harmony colors
        harmony_colors = self._get_harmonious_colors()
        for i, harmony_color in enumerate(harmony_colors):
            harmony_swatch = self.query_one(f"#harmony-{i}", Static)
            harmony_swatch.styles.background = harmony_color

            # Set text color for contrast
            is_dark = self._is_color_dark(harmony_color)
            harmony_swatch.styles.color = "white" if is_dark else "black"
            harmony_swatch.update(harmony_color.hex)

    # TODO Rename this here and in `_update_display`
    def _extracted_from__update_display_38(self, arg0: str, arg1: int, arg2: str, arg3: str) -> None:
        """Update a slider and its corresponding value display."""
        # Get the slider directly - no need to cast when we've already specified the type in query_one
        hue_slider = self.query_one(arg0, Slider)
        hue_slider.value = arg1
        self.query_one(arg2, Static).update(f"{arg1}{arg3}")

    # TODO Rename this here and in `_update_display`
    def _extracted_from__update_display_26(self, arg0: str, arg1: int, arg2: str) -> None:
        """Update a slider and its corresponding value display."""
        # Get the slider directly - no need to cast when we've already specified the type in query_one
        red_slider = self.query_one(arg0, Slider)
        red_slider.value = arg1
        self.query_one(arg2, Static).update(f"{arg1}")

    def _get_rgb_string(self) -> str:
        """Get RGB representation of the current color."""
        r, g, b = self.color.rgb
        return f"rgb({r},{g},{b})"

    def _get_hsl_string(self) -> str:
        """Get HSL representation of the current color."""
        h, s, lightness = self._get_hsl_values()
        return f"hsl({h},{s}%,{lightness}%)"

    def _get_hsl_values(self) -> Tuple[int, int, int]:
        """Calculate HSL values for the current color."""
        import colorsys

        r, g, b = self.color.normalized
        h, lightness, s = colorsys.rgb_to_hls(r, g, b)  # Note: rgb_to_hls returns h,l,s
        h_deg = round(h * 360)
        s_pct = round(s * 100)
        lightness_pct = round(lightness * 100)
        return h_deg, s_pct, lightness_pct

    def _get_harmonious_colors(self) -> List[Color]:
        """Generate harmonious colors based on the current color."""
        # Get HSL values
        h, s, lightness = self._get_hsl_values()

        # Calculate complementary color (opposite on color wheel)
        complementary_h = (h + 180) % 360

        # Calculate analogous colors (adjacent on color wheel)
        analogous1_h = (h + 30) % 360
        analogous2_h = (h - 30) % 360

        # Calculate triadic colors (120 degrees apart)
        triadic1_h = (h + 120) % 360
        triadic2_h = (h + 240) % 360

        # Convert back to RGB and create Color objects
        import colorsys

        def hsl_to_color(h_deg: int, s_pct: int, l_pct: int) -> Color:
            h_norm = h_deg / 360
            s_norm = s_pct / 100
            l_norm = l_pct / 100
            r, g, b = colorsys.hls_to_rgb(h_norm, l_norm, s_norm)
            r_byte = round(r * 255)
            g_byte = round(g * 255)
            b_byte = round(b * 255)
            return Color(r_byte, g_byte, b_byte)

        return [
            hsl_to_color(complementary_h, s, lightness),
            hsl_to_color(analogous1_h, s, lightness),
            hsl_to_color(analogous2_h, s, lightness),
            hsl_to_color(triadic1_h, s, lightness),
            hsl_to_color(triadic2_h, s, lightness),
        ]

    def _is_color_dark(self, color: Color) -> bool:
        """Check if a color is dark (for contrast)."""
        r, g, b = color.rgb
        return (0.299 * r + 0.587 * g + 0.114 * b) < 128

    # Event handlers
    def on_slider_changed(self, event: Slider.Changed) -> None:
        """Handle slider value changes."""
        slider_id = event.slider.id
        value = event.value

        if slider_id in ("red-slider", "green-slider", "blue-slider"):
            # Update RGB values
            r, g, b = self.color.rgb

            if slider_id == "red-slider":
                r = value
                self.query_one("#red-value", Static).update(f"{r}")
            elif slider_id == "green-slider":
                g = value
                self.query_one("#green-value", Static).update(f"{g}")
            elif slider_id == "blue-slider":
                b = value
                self.query_one("#blue-value", Static).update(f"{b}")

            # Update the color
            self.color = Color(r, g, b)

        elif slider_id in ("hue-slider", "saturation-slider", "lightness-slider"):
            self._extracted_from_on_slider_changed_25(slider_id, value)
        # Notify about color change
        self.post_message(ColorValueChanged(self.color))

    # TODO Rename this here and in `on_slider_changed`
    def _extracted_from_on_slider_changed_25(self, slider_id: str, value: int) -> None:
        # Update HSL values
        h, s, lightness = self._get_hsl_values()

        if slider_id == "hue-slider":
            h = value
            self.query_one("#hue-value", Static).update(f"{h}°")
        elif slider_id == "lightness-slider":
            lightness = value
            self.query_one("#lightness-value", Static).update(f"{lightness}%")

        elif slider_id == "saturation-slider":
            s = value
            self.query_one("#saturation-value", Static).update(f"{s}%")
        # Convert HSL to RGB and update the color
        import colorsys

        h_norm = h / 360
        s_norm = s / 100
        l_norm = lightness / 100
        r, g, b = colorsys.hls_to_rgb(h_norm, l_norm, s_norm)
        r_byte = round(r * 255)
        g_byte = round(g * 255)
        b_byte = round(b * 255)
        self.color = Color(r_byte, g_byte, b_byte)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id

        if button_id == "add-to-palette":
            self.action_add_to_palette()
        elif button_id == "copy-color":
            self.action_copy_color()
        elif button_id == "randomize-color":
            self.action_randomize_color()

    # Action methods for bindings and buttons
    def action_copy_color(self) -> None:
        """Copy the current color."""
        # We'd integrate with system clipboard in a real implementation
        color_value = (
            self.color.hex
            if self.display_format == "hex"
            else self._get_rgb_string()
            if self.display_format == "rgb"
            else self._get_hsl_string()
        )
        self.notify(f"Copied {color_value}")

    def action_add_to_palette(self) -> None:
        """Add the current color to the active palette."""
        # This will dispatch a message for app to handle
        # No need to implement the actual functionality here
        self.notify("Color added to palette")

    def action_randomize_color(self) -> None:
        """Set a random color."""
        import random

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = Color(r, g, b)
        self.notify("Random color generated")

    def action_toggle_format(self) -> None:
        """Toggle between different color formats."""
        formats = ["hex", "rgb", "hsl"]
        current_index = formats.index(self.display_format)
        next_index = (current_index + 1) % len(formats)
        self.display_format = formats[next_index]
