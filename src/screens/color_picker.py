from typing import ClassVar
from typing import List
from typing import Tuple
from typing import Union

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.containers import Horizontal
from textual.containers import Vertical
from textual.reactive import reactive
from textual.widgets import Button
from textual.widgets import Input
from textual.widgets import Label
from textual.widgets import Static

from ..models.color_model import Color
from ..utils.color_adjustment import adjust_hue
from ..utils.color_adjustment import adjust_lightness
from ..utils.color_adjustment import adjust_saturation
from ..utils.color_adjustment import is_color_dark
from .base_screen import BaseScreen


class ColorPickerScreen(BaseScreen):
    """Screen for picking and adjusting colors."""

    # Load the CSS file for this screen
    CSS_PATH = "color_picker.tcss"

    # Reactive properties for color state
    selected_color: reactive[Color] = reactive(Color("#FF5500"))
    hue_value: reactive[int] = reactive(0)
    saturation_value: reactive[int] = reactive(100)
    lightness_value: reactive[int] = reactive(50)

    # Standard step sizes for adjustments
    HUE_STEP = 10  # 10 degrees on the color wheel
    SATURATION_STEP = 5  # 5% change in saturation
    LIGHTNESS_STEP = 5  # 5% change in lightness

    # Screen-specific bindings that extend BaseScreen bindings
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Color adjustment bindings
        Binding("up", "adjust_hue(1)", "Increase hue"),
        Binding("down", "adjust_hue(-1)", "Decrease hue"),
        Binding("left", "adjust_saturation(-1)", "Decrease saturation"),
        Binding("right", "adjust_saturation(1)", "Increase saturation"),
        Binding("shift+up", "adjust_lightness(1)", "Increase lightness"),
        Binding("shift+down", "adjust_lightness(-1)", "Decrease lightness"),
        # Screen-specific actions
        Binding("ctrl+c", "copy_color_hex", "Copy hex value"),
    ]

    def compose(self) -> ComposeResult:
        """Compose the color picker screen UI."""
        with Container(id="color-picker-container"):
            # Header section
            with Horizontal(id="picker-header"):
                yield Label("COLOR PICKER", id="picker-title")
                yield Button("Back to Palette", id="back-button")

            # Main content
            with Horizontal(id="picker-content"):
                # Color preview and hex input
                with Vertical(id="color-preview-section"):
                    yield Static("", id="color-preview-box")
                    yield Input(value=self.selected_color.hex, id="color-hex-input")
                    yield Label("Use arrow keys to adjust color:", id="instructions")
                    yield Label("↑/↓: Hue | ←/→: Saturation | Shift+↑/↓: Lightness", id="key-instructions")

                # HSL sliders and values
                with Vertical(id="color-sliders-section"):
                    # Hue control
                    with Horizontal(classes="slider-row"):
                        yield Label("Hue:", classes="slider-label")
                        yield Static(f"{self.hue_value}°", id="hue-value", classes="slider-value")

                    # Saturation control
                    with Horizontal(classes="slider-row"):
                        yield Label("Saturation:", classes="slider-label")
                        yield Static(f"{self.saturation_value}%", id="saturation-value", classes="slider-value")

                    # Lightness control
                    with Horizontal(classes="slider-row"):
                        yield Label("Lightness:", classes="slider-label")
                        yield Static(f"{self.lightness_value}%", id="lightness-value", classes="slider-value")

    def on_mount(self) -> None:
        """Handle screen mount event."""
        # Initialize color values from any existing color in the app
        self._update_from_app_color()
        # Update the UI with current color values
        self._update_ui()

    def _update_from_app_color(self) -> None:
        """Get the current color from the app if available."""
        try:
            # Try to get color from the app's color wheel
            from ..widgets.color.color_wheel import ColorWheel

            color_wheel = self.app.query_one("#color-wheel", ColorWheel)
            color_hex = color_wheel.selected_color

            # Convert to Color object
            self.selected_color = Color(color_hex)

            # Update HSL values
            h, s, lightness = self.selected_color.hsl
            self.hue_value = h
            self.saturation_value = s
            self.lightness_value = lightness
        except Exception:
            # If there's any issue, just use the default color
            pass

    def _update_ui(self) -> None:
        """Update UI elements based on current color values."""
        # Update color preview
        preview = self.query_one("#color-preview-box", Static)
        preview.styles.background = self.selected_color.hex

        # Use the is_color_dark utility function instead of a method
        preview.styles.color = "white" if is_color_dark(self.selected_color) else "black"

        # Update hex input
        hex_input = self.query_one("#color-hex-input", Input)
        hex_input.value = self.selected_color.hex

        # Update HSL value displays
        self.query_one("#hue-value", Static).update(f"{self.hue_value}°")
        self.query_one("#saturation-value", Static).update(f"{self.saturation_value}%")
        self.query_one("#lightness-value", Static).update(f"{self.lightness_value}%")

    def _update_from_hsl(self) -> None:
        """Update the selected color based on current HSL values."""
        self.selected_color = Color({"h": self.hue_value, "s": self.saturation_value, "l": self.lightness_value})
        self._update_ui()

    def _update_color_in_app(self) -> None:
        """Update the color in the main app."""
        try:
            # Try to update color in the app's color wheel
            from ..widgets.color.color_wheel import ColorWheel

            color_wheel = self.app.query_one("#color-wheel", ColorWheel)
            color_wheel.selected_color = self.selected_color.hex
        except Exception:
            # If there's any issue, just continue
            pass

    def action_adjust_hue(self, steps: int) -> None:
        """
        Adjust the hue value.

        Args:
            steps: Number of steps to adjust (positive or negative)
        """
        # Calculate the amount to adjust
        amount = steps * self.HUE_STEP

        # Apply the adjustment using the utility function
        self.selected_color = adjust_hue(self.selected_color, amount)

        # Update the HSL values from the new color
        h, s, lightness = self.selected_color.hsl
        self.hue_value = h
        self.saturation_value = s
        self.lightness_value = lightness

        # Update UI and propagate to app
        self._update_ui()
        self._update_color_in_app()

    def action_adjust_saturation(self, steps: int) -> None:
        """
        Adjust the saturation value.

        Args:
            steps: Number of steps to adjust (positive or negative)
        """
        # Calculate the amount to adjust
        amount = steps * self.SATURATION_STEP

        # Apply the adjustment using the utility function
        self.selected_color = adjust_saturation(self.selected_color, amount)

        # Update the HSL values from the new color
        h, s, lightness = self.selected_color.hsl
        self.hue_value = h
        self.saturation_value = s
        self.lightness_value = lightness

        # Update UI and propagate to app
        self._update_ui()
        self._update_color_in_app()

    def action_adjust_lightness(self, steps: int) -> None:
        """
        Adjust the lightness value.

        Args:
            steps: Number of steps to adjust (positive or negative)
        """
        # Calculate the amount to adjust
        amount = steps * self.LIGHTNESS_STEP

        # Apply the adjustment using the utility function
        self.selected_color = adjust_lightness(self.selected_color, amount)

        # Update the HSL values from the new color
        h, s, lightness = self.selected_color.hsl
        self.hue_value = h
        self.saturation_value = s
        self.lightness_value = lightness

        # Update UI and propagate to app
        self._update_ui()
        self._update_color_in_app()

    def action_copy_color_hex(self) -> None:
        """Copy the current color's hex value to clipboard."""
        # This would use the system clipboard in a real implementation
        self.notify(f"Copied {self.selected_color.hex} to clipboard", severity="information")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events.

        Args:
            event: The button press event
        """
        if event.button and hasattr(event.button, "id") and event.button.id == "back-button":
            self.app.switch_screen("main")

    def on_input_changed(self, event: Input.Changed) -> None:
        """
        Handle input change events.

        Args:
            event: The input change event
        """
        if (
            hasattr(event, "input")
            and event.input
            and hasattr(event.input, "id")
            and event.input.id == "color-hex-input"
        ):
            try:
                # Try to create a color from the input value
                color = Color(event.value)
                self.selected_color = color

                # Update HSL values
                h, s, lightness = color.hsl
                self.hue_value = h
                self.saturation_value = s
                self.lightness_value = lightness

                # Update UI and propagate to app
                self._update_ui()
                self._update_color_in_app()
            except Exception:
                # If input is invalid, don't update
                pass
