
## Step 2: Color Extraction and Manipulation Tools

### Overview

This phase implements the core color functionality, including state management for the active color, visual color selection (adapted for TUI), and color information display. The browser-based eyedropper and canvas are replaced with TUI-appropriate alternatives.

### Prerequisites

* Completed Step 1: Project Setup and Core UI Framework (Python/Textual)
* Understanding of Textual's state management (reactive attributes, messages)
* Basic knowledge of Python color libraries (e.g., `rich.color`, `colorsys`)

### Implementation Tasks

#### 2.1 Color State Management (Textual Approach)

Instead of a React Context, manage color state using Textual's built-in mechanisms.

```python
# milky_color_suite/app.py (or main_screen.py)

from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.color import Color # Use Textual's Color class

# ... other imports

class MilkyColorSuiteApp(App): # Or within your MainScreen class
    """A Textual app to manage color palettes."""

    # Reactive attribute for the currently active color
    active_color = reactive(Color.parse("white"))

    # Reactive attribute for the display format
    color_format = reactive("hex") # Options: 'hex', 'rgb', 'hsl'

    # ... other app setup (CSS_PATH, SCREENS)

    def watch_active_color(self, old_color: Color, new_color: Color) -> None:
        """Called when active_color changes."""
        # Post a message to notify widgets or update UI directly
        self.post_message(self.ActiveColorChanged(new_color))
        # Example: Update a specific widget if needed
        # color_info_widget = self.query_one(ColorInfo)
        # color_info_widget.update_display()

    def watch_color_format(self, old_format: str, new_format: str) -> None:
        """Called when color_format changes."""
        self.post_message(self.ColorFormatChanged(new_format))
        # Example: Update ColorInfo display
        # color_info_widget = self.query_one(ColorInfo)
        # color_info_widget.update_display()

    # --- Utility methods ---
    def get_color_string(self, color: Color = None, format: str = None) -> str:
        """Convert a color to string in the specified format."""
        color = color or self.active_color
        format = format or self.color_format

        if format == "hex":
            return color.hex
        elif format == "rgb":
            r, g, b = color.rgb
            return f"rgb({r}, {g}, {b})"
        elif format == "hsl":
            # Textual Color doesn't directly expose HSL, use colorsys
            import colorsys
            r, g, b = color.normalized
            h, l, s = colorsys.rgb_to_hls(r, g, b) # HLS! Not HSL
            # Convert HLS to HSL for display consistency if needed, or just display HLS
            # HSL: H stays same, S_hsl = S_hls / (1 - abs(2*L-1)), L_hsl = L
            # Approximate HSL display based on HLS:
            h_deg = round(h * 360)
            s_pct = round(s * 100)
            l_pct = round(l * 100)
            return f"hsl({h_deg}, {s_pct}%, {l_pct}%)" # Displaying HLS values in HSL format string
        else:
            return color.hex

    def is_color_dark(self, color: Color = None) -> bool:
        """Check if a color is considered dark (for contrast)."""
        color = color or self.active_color
        # Use luminance - Textual Color has it!
        return color.luminance < 0.5

    # Define custom messages for communication (optional but good practice)
    class ActiveColorChanged(App.Message):
        def __init__(self, color: Color) -> None:
            self.color = color
            super().__init__()

    class ColorFormatChanged(App.Message):
        def __init__(self, format: str) -> None:
            self.format = format
            super().__init__()

    # ... rest of the App class (on_mount, etc.)
```

#### 2.2 Color Selection Widget (TUI Alternative)

Replace the HTML Canvas Color Wheel with TUI-friendly options:

* **Option 1: Simple Input Field:** Use a standard `Input` widget where the user types the color code (HEX, RGB).
* **Option 2: Predefined Swatches:** Use a `Container` with several `Button` or `Static` widgets showing predefined colors.
* **Option 3: Simple Sliders/Inputs:** Use `Input` widgets or potentially custom slider widgets for H, S, L or R, G, B values.

```python
# milky_color_suite/widgets/color/color_selector.py
from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.reactive import reactive
from textual.widgets import Static, Input, Button
from textual.color import Color, ColorParseError

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

    def compose(self) -> ComposeResult:
        yield Static(id="color-preview")
        yield Input(placeholder="Enter color (e.g., #ff00ff, rgb(0,255,0))", id="color-input-field")
        # Add other selection methods here (swatches, sliders etc.) if desired

    def on_mount(self) -> None:
        """Initial setup."""
        self.query_one(Input).value = self.color_input
        self._update_preview(self.color_input)

    def _update_preview(self, value: str):
         """Update the preview box color."""
         preview = self.query_one("#color-preview")
         try:
             color = Color.parse(value)
             preview.styles.background = color
             # Set foreground for contrast
             preview.styles.color = "black" if color.luminance > 0.5 else "white"
             preview.update(f"Preview: {value}")
         except ColorParseError:
             preview.styles.background = "darkred"
             preview.styles.color = "white"
             preview.update("Invalid Color")


    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle changes in the color input field."""
        self.color_input = event.value
        self._update_preview(event.value)

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle submission of the color input field."""
        try:
            new_color = Color.parse(event.value)
            # Update the app's active color
            self.app.active_color = new_color # Assuming 'app' property is available
            self.notify(f"Color set to {new_color.hex}")
        except ColorParseError:
            self.notify("Invalid color format.", severity="error")

    # Watch the reactive input value if needed for other logic
    def watch_color_input(self, old_value: str, new_value: str) -> None:
        # This might be redundant if on_input_changed handles everything
        pass

    # Optional: Add methods to handle swatch clicks or slider changes if implemented
```

#### 2.3 Color Dropper Tool (Not Applicable in TUI)

* The `EyeDropper` API is browser-specific and cannot be used in a terminal application.
* The `ImageColorPicker` fallback requires GUI interaction or complex setup:
    * It *could* be implemented as a separate script that opens an image (using Pillow, OpenCV), lets the user click (requires a GUI window library like Tkinter, PyQt, or even a simple graphical interaction via the terminal if supported), gets the color, and passes it back to the Textual app. This is **significantly outside** the scope of a standard TUI and adds external dependencies.
    * **Recommendation:** Remove this feature for the Textual version or replace it with manual color input/selection methods within the TUI. The ASCII button `[⨀]` should be removed or repurposed.

#### 2.4 Color Info Display Component

```python
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
            yield Button("HEX", id="btn-hex", variant="primary") # Start with HEX active
            yield Button("RGB", id="btn-rgb")
            yield Button("HSL", id="btn-hsl")
        yield Static(id="color-value")

    def on_mount(self) -> None:
        """Subscribe to app messages or set initial state."""
        # Could listen for App messages instead of using internal reactive vars
        # self.watch(self.app, "active_color", self._app_color_changed)
        # self.watch(self.app, "color_format", self._app_format_changed)
        self._update_display() # Initial display

    def _update_display(self) -> None:
        """Update the swatch and value based on current state."""
        color = self._active_color # Use internal state or fetch from app
        format = self._color_format

        swatch = self.query_one("#color-swatch")
        swatch.styles.background = color
        # Set text color for contrast
        swatch.styles.color = "black" if color.luminance > 0.5 else "white"
        swatch.update(f"Swatch: {color.hex}") # Show hex on swatch for reference

        value_display = self.query_one("#color-value")
        value_display.update(self.app.get_color_string(color, format)) # Use app's helper

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

    def _handle_color_change(self, message: 'MilkyColorSuiteApp.ActiveColorChanged') -> None:
        self._active_color = message.color
        self._update_display()

    def _handle_format_change(self, message: 'MilkyColorSuiteApp.ColorFormatChanged') -> None:
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
```

#### 2.5 Integration with App/Screen

Update the main screen (`main_screen.py`) to include these widgets:

```python
# milky_color_suite/screens/main_screen.py
# ... other imports
from ..widgets.color.color_selector import ColorSelector
from ..widgets.color.color_info import ColorInfo

class MainScreen(Screen):
    # ... BINDINGS, CSS_PATH ...

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
             with VerticalScroll(id="sidebar-container"):
                 yield Static("Sidebar Area")
                 # Add PaletteList (Step 3), ImageColorPicker (removed/replaced) here
             with Container(id="main-and-palette"):
                 with VerticalScroll(id="main-container"):
                     yield Label("Color Tools") # Add a label/title
                     yield ColorSelector() # Add the selector
                     yield ColorInfo()     # Add the info display
                     # Add PaletteName (Step 3), ExportPanel (Step 4) here
                 with Container(id="palette-container"):
                     yield Static("Palette Area (Step 3)", id="palette-content")
                     # Add PalettePanel (Step 3) here
        yield Footer()

    # ... actions ...
```