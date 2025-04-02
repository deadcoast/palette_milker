# milky_color_suite/widgets/color/color_info.py
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import Static, Button, Label
from textual.color import Color


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
        """Subscribe to app messages or set initial state."""
        # Could listen for App messages instead of using internal reactive vars
        # self.watch(self.app, "active_color", self._app_color_changed)
        # self.watch(self.app, "color_format", self._app_format_changed)
        self._update_display()  # Initial display

    def _update_display(self) -> None:
        """Update the swatch and value based on current state."""
        color = self._active_color  # Use internal state or fetch from app
        format = self._color_format

        swatch = self.query_one("#color-swatch")
        swatch.styles.background = color
        # Set text color for contrast
        swatch.styles.color = "black" if color.luminance > 0.5 else "white"
        swatch.update(f"Swatch: {color.hex}")  # Show hex on swatch for reference

        value_display = self.query_one("#color-value")
        value_display.update(self.app.get_color_string(color, format))  # Use app's helper

        # Update button variants
        self.query_one("#btn-hex").variant = "primary" if format == "hex" else "default"
        self.query_one("#btn-rgb").variant = "primary" if format == "rgb" else "default"
        self.query_one("#btn-hsl").variant = "primary" if format == "hsl" else "default"

    # Example message handlers if using App messages
    def on_mount(self) -> None:
        # Assuming the App class defines these messages
        self.app.subscribe(self.app.ActiveColorChanged, self._handle_color_change)
        self.app.subscribe(self.app.ColorFormatChanged, self._handle_format_change)
        self._set_initial_state()
        self._update_display()

    def _set_initial_state(self):
        """Get initial state from the app."""
        self._active_color = self.app.active_color
        self._color_format = self.app.color_format

    def _handle_color_change(self, message: "MilkyColorSuiteApp.ActiveColorChanged") -> None:
        self._active_color = message.color
        self._update_display()

    def _handle_format_change(self, message: "MilkyColorSuiteApp.ColorFormatChanged") -> None:
        self._color_format = message.format
        self._update_display()

    # Handle button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle format button clicks."""
        if event.button.id == "btn-hex":
            self.app.color_format = "hex"
        elif event.button.id == "btn-rgb":
            self.app.color_format = "rgb"
        elif event.button.id == "btn-hsl":
            self.app.color_format = "hsl"
        # The watch_color_format in the App will trigger the update via message

    # Placeholder for Save to Palette button (add when Palette context exists)
    # yield Button("Save to Palette", id="btn-save-palette")
    # def on_button_pressed ... handle btn-save-palette
