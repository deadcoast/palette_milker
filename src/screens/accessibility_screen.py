"""
Color accessibility testing screen for the Palette Milker application.

This screen provides tools for checking color accessibility compliance
with WCAG standards and improving color combinations for better accessibility.
"""

from typing import ClassVar
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from textual import events
from textual.app import ComposeResult
from textual.binding import Binding
from textual.color import Color as TextualColor
from textual.containers import Container
from textual.containers import Grid
from textual.containers import ScrollableContainer
from textual.message import Message
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import Static

from ..models.color_model import Color
from ..models.palette_model import Palette
from ..utils.color_accessibility import calculate_contrast_ratio
from ..utils.color_accessibility import get_wcag_compliance
from ..utils.color_accessibility import is_color_blind_friendly
from ..utils.color_accessibility import optimize_text_color
from ..utils.color_accessibility import suggest_accessible_alternatives


class ColorPairSelected(Message):
    """Message sent when a color pair is selected for testing."""

    def __init__(self, foreground: Color, background: Color) -> None:
        """
        Initialize with foreground and background colors.

        Args:
            foreground: The foreground color
            background: The background color
        """
        self.foreground = foreground
        self.background = background
        super().__init__()


class AccessibilityScreen(Screen):
    """
    Screen for testing color accessibility.

    This screen provides tools for checking WCAG compliance for color pairs,
    visualizing color contrast, and suggesting accessible alternatives.
    """

    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Navigation
        Binding("escape", "app.view_palette", "Back to palettes"),
        # Color pair management
        Binding("r", "reverse_colors", "Swap fg/bg"),
        # Suggestions
        Binding("s", "suggest_improvements", "Suggest changes"),
        Binding("o", "optimize_text", "Optimize text"),
    ]

    DEFAULT_CSS = """
    AccessibilityScreen {
        background: $surface;
    }

    #accessibility-header {
        dock: top;
        height: 1;
        background: $primary;
        color: $text;
        text-align: center;
        padding: 0 1;
    }

    #palette-colors {
        width: 100%;
        height: 3;
        layout: horizontal;
        margin: 1 0;
    }

    .color-swatch {
        width: 1fr;
        height: 100%;
        border: solid $background;
        content-align: center middle;
    }

    .selected-swatch {
        border: tall $accent;
    }

    #test-area {
        width: 100%;
        margin: 1 0;
        padding: 1;
    }

    #preview-box {
        width: 100%;
        height: 10;
        border: wide $panel;
        margin-bottom: 1;
    }

    .preview-content {
        padding: 1;
    }

    .preview-title {
        text-style: bold;
    }

    .preview-text {
        margin-top: 1;
    }

    #contrast-info {
        width: 100%;
        background: $panel;
        padding: 1;
        margin-bottom: 1;
    }

    .info-grid {
        grid-size: 2;
        grid-columns: 1fr 1fr;
        width: 100%;
    }

    .info-item {
        height: 1;
        margin-bottom: 1;
    }

    .info-label {
        text-align: right;
        padding-right: 1;
    }

    .info-value {
        text-align: left;
    }

    .pass {
        color: $success;
    }

    .fail {
        color: $error;
    }

    #suggestions {
        width: 100%;
        height: 1fr;
        padding: 1;
        background: $panel-darken-1;
    }

    .suggestion-title {
        width: 100%;
        height: 1;
        margin-bottom: 1;
        text-style: bold;
    }

    .suggestion-item {
        width: 100%;
        height: 5;
        border: solid $primary;
        margin-bottom: 1;
        background: $panel;
    }

    .suggestion-header {
        width: 100%;
        height: 1;
        background: $primary;
        color: $text;
        padding: 0 1;
    }

    .suggestion-preview {
        width: 100%;
        height: 3;
        padding: 0 1;
    }

    .suggestion-info {
        width: 100%;
        height: 1;
        text-align: right;
        padding: 0 1;
    }

    #color-blind-info {
        width: 100%;
        background: $panel;
        padding: 1;
        margin-top: 1;
    }
    """

    # Reactive properties
    foreground_color: reactive[Color] = reactive(Color("#000000"))
    background_color: reactive[Color] = reactive(Color("#FFFFFF"))
    contrast_ratio: reactive[float] = reactive(21.0)
    wcag_compliance: reactive[Dict[str, bool]] = reactive({})
    color_blind_friendly: reactive[Dict[str, bool]] = reactive({})
    suggestions: reactive[List[Dict]] = reactive([])

    def __init__(self, palette: Optional[Palette] = None):
        """
        Initialize the accessibility screen.

        Args:
            palette: Optional palette to use for color selection
        """
        super().__init__()
        self.palette = palette

        # If a palette is provided, use its first two colors
        if palette and len(palette.colors) >= 2:
            self.foreground_color = palette.colors[0]
            self.background_color = palette.colors[1]

        # Initialize derived values
        self._update_accessibility_data()

    def compose(self) -> ComposeResult:
        """Compose the accessibility screen UI."""
        # Header and title
        yield Header()
        yield Static("COLOR ACCESSIBILITY CHECKER", id="accessibility-header")

        # Palette colors (if palette provided)
        with Container(id="palette-colors"):
            if self.palette:
                for i, color in enumerate(self.palette.colors):
                    # Create textual color for styling
                    textual_color = TextualColor.parse(color.hex)

                    # Determine if this is currently selected as foreground or background
                    classes = "color-swatch"
                    if color.hex == self.foreground_color.hex:
                        classes += " selected-swatch"

                    # Create the swatch
                    swatch = Static(color.hex, id=f"color-{i}", classes=classes)
                    swatch.styles.background = textual_color

                    # Set text color for contrast
                    text_color = (
                        TextualColor.parse("#FFFFFF") if self._is_dark(color) else TextualColor.parse("#000000")
                    )
                    swatch.styles.color = text_color

                    yield swatch

        # Main test area
        with Container(id="test-area"):
            # Preview box with sample text
            with Container(id="preview-box"):
                # Set background color
                preview_box = self.query_one("#preview-box")
                preview_box.styles.background = TextualColor.parse(self.background_color.hex)

                # Text content with foreground color
                with Container(classes="preview-content"):
                    title = Static("Sample Title Text (Large)", classes="preview-title")
                    title.styles.color = TextualColor.parse(self.foreground_color.hex)
                    yield title

                    text = Static(
                        "This is a sample paragraph of normal text to demonstrate the contrast "
                        "between the selected foreground and background colors. Good contrast is "
                        "essential for readability and accessibility.",
                        classes="preview-text",
                    )
                    text.styles.color = TextualColor.parse(self.foreground_color.hex)
                    yield text

            # Contrast and compliance information
            with Container(id="contrast-info"):
                yield Static("Contrast and Compliance", classes="info-label")

                with Grid(classes="info-grid"):
                    # Foreground color
                    yield Static("Foreground:", classes="info-label info-item")
                    yield Static(self.foreground_color.hex, classes="info-value info-item")

                    # Background color
                    yield Static("Background:", classes="info-label info-item")
                    yield Static(self.background_color.hex, classes="info-value info-item")

                    # Contrast ratio
                    yield Static("Contrast Ratio:", classes="info-label info-item")
                    ratio_text = f"{self.contrast_ratio:.2f}:1"
                    yield Static(ratio_text, classes="info-value info-item")

                    # WCAG AA (normal text)
                    yield Static("WCAG AA (Normal):", classes="info-label info-item")
                    aa_class = "pass" if self.wcag_compliance.get("AA_normal", False) else "fail"
                    aa_symbol = "✓" if self.wcag_compliance.get("AA_normal", False) else "✗"
                    yield Static(aa_symbol, classes=f"info-value info-item {aa_class}")

                    # WCAG AAA (normal text)
                    yield Static("WCAG AAA (Normal):", classes="info-label info-item")
                    aaa_class = "pass" if self.wcag_compliance.get("AAA_normal", False) else "fail"
                    aaa_symbol = "✓" if self.wcag_compliance.get("AAA_normal", False) else "✗"
                    yield Static(aaa_symbol, classes=f"info-value info-item {aaa_class}")

            # Colorblind information
            with Container(id="color-blind-info"):
                yield Static("Color Blindness Compatibility", classes="info-label")

                with Grid(classes="info-grid"):
                    for name, friendly in self.color_blind_friendly.items():
                        # Display each type of color blindness
                        label = name.capitalize() + ":"
                        yield Static(label, classes="info-label info-item")

                        friendly_class = "pass" if friendly else "fail"
                        friendly_symbol = "✓" if friendly else "✗"
                        yield Static(friendly_symbol, classes=f"info-value info-item {friendly_class}")

        # Suggestions section
        with ScrollableContainer(id="suggestions"):
            yield Static("Suggestions for Improvement", classes="suggestion-title")

        yield Footer()

    def on_mount(self) -> None:
        """Set up the screen when mounted."""
        self._update_preview()
        self._update_suggestions()

    def watch_foreground_color(self, old_color: Color, new_color: Color) -> None:
        """React to foreground color changes."""
        if old_color != new_color:
            self._extracted_from_watch_background_color_4()

    def watch_background_color(self, old_color: Color, new_color: Color) -> None:
        """React to background color changes."""
        if old_color != new_color:
            self._extracted_from_watch_background_color_4()

    # TODO Rename this here and in `watch_foreground_color` and `watch_background_color`
    def _extracted_from_watch_background_color_4(self) -> None:
        """Update data and UI after a color change."""
        self._update_accessibility_data()
        self._update_preview()
        self._update_suggestions()

    def _update_accessibility_data(self) -> None:
        """Update all accessibility data for the current color pair."""
        # Calculate contrast ratio
        self.contrast_ratio = calculate_contrast_ratio(self.foreground_color, self.background_color)

        # Check WCAG compliance
        self.wcag_compliance = get_wcag_compliance(self.contrast_ratio)

        # Check color blind friendliness
        self.color_blind_friendly = is_color_blind_friendly(self.foreground_color, self.background_color)

        # Generate suggestions
        self.suggestions = suggest_accessible_alternatives(self.foreground_color, self.background_color, 4.5)

    def _update_preview(self) -> None:
        """Update the preview box with current colors."""
        try:
            # Update preview box background
            preview_box = self.query_one("#preview-box", Container)
            preview_box.styles.background = TextualColor.parse(self.background_color.hex)

            # Update text color
            for text_element in self.query(".preview-title, .preview-text"):
                text_element.styles.color = TextualColor.parse(self.foreground_color.hex)

            # Update contrast and compliance info
            ratio_value = self.query_one(".info-grid .info-value", Static)
            if ratio_value:
                ratio_value.update(f"{self.contrast_ratio:.2f}:1")

            # Update WCAG compliance indicators
            info_values = list(self.query(".info-grid .info-value").results(Static))
            if len(info_values) >= 5:  # Ensure we have enough elements
                # Foreground and background
                info_values[0].update(self.foreground_color.hex)
                info_values[1].update(self.background_color.hex)

                # Contrast ratio
                info_values[2].update(f"{self.contrast_ratio:.2f}:1")

                self._extracted_from__update_preview_28("AA_normal", info_values, 3)
                self._extracted_from__update_preview_28("AAA_normal", info_values, 4)
        except Exception as e:
            # Just log the error without crashing
            self.app.log.error(f"Error updating preview: {e}")

    # TODO Rename this here and in `_update_preview`
    def _extracted_from__update_preview_28(self, arg0: str, info_values: List[Static], arg2: int) -> None:
        """
        Update a compliance indicator in the info grid.

        Args:
            arg0: The compliance key to check (e.g., "AA_normal")
            info_values: List of Static widgets containing the values
            arg2: Index of the widget to update
        """
        # WCAG AA
        aa_class = "pass" if self.wcag_compliance.get(arg0, False) else "fail"
        aa_symbol = "✓" if self.wcag_compliance.get(arg0, False) else "✗"
        info_values[arg2].update(aa_symbol)
        info_values[arg2].set_classes(f"info-value info-item {aa_class}")

    def _update_suggestions(self) -> None:
        """Update the suggestions section with current data."""
        try:
            # Get the suggestions container
            container = self.query_one("#suggestions", ScrollableContainer)

            # Keep the title but remove other children
            for child in list(container.children)[1:]:  # Skip the title
                child.remove()

            # If contrast is already compliant, show a message
            if not self.suggestions:
                if self.wcag_compliance.get("AA_normal", False):
                    container.mount(Static("✓ Current contrast meets WCAG AA standards", classes="pass"))
                else:
                    container.mount(Static("No suggestions available", classes="fail"))
                return

            # Add each suggestion
            for i, suggestion in enumerate(self.suggestions):
                fg = suggestion["foreground"]
                bg = suggestion["background"]
                ratio = suggestion["formatted_ratio"]
                adjustment = suggestion["adjustment"]

                # Create suggestion item
                item = Container(classes="suggestion-item", id=f"suggestion-{i}")

                # Header with adjustment info
                item.mount(Static(adjustment, classes="suggestion-header"))

                # Preview with the suggested colors
                preview = Container(classes="suggestion-preview")
                preview.styles.background = TextualColor.parse(bg)

                # Sample text
                text = Static("Sample Text", classes="preview-text")
                text.styles.color = TextualColor.parse(fg)
                preview.mount(text)

                item.mount(preview)

                # Info with contrast ratio
                item.mount(Static(f"Contrast: {ratio}", classes="suggestion-info"))

                # Mount the suggestion
                container.mount(item)
        except Exception as e:
            # Just log the error without crashing
            self.app.log.error(f"Error updating suggestions: {e}")

    def _is_dark(self, color: Color) -> bool:
        """Check if a color is dark (for contrast)."""
        r, g, b = color.rgb
        return r * 299 + g * 587 + b * 114 < 128000

    def _select_color(self, index: int) -> None:
        """
        Select a color from the palette as foreground or background.

        Args:
            index: Index of the color in the palette
        """
        if not self.palette or index >= len(self.palette.colors):
            return

        # Get the clicked color
        color = self.palette.colors[index]

        # Decide whether to set as foreground or background
        if color.hex == self.foreground_color.hex:
            # If already selected as foreground, do nothing
            pass
        elif color.hex == self.background_color.hex:
            # If already selected as background, switch fg/bg
            self.action_reverse_colors()
        else:
            # Otherwise, set as new foreground
            self.foreground_color = color

        # Update swatch selection
        self._update_swatch_selection()

    def _update_swatch_selection(self) -> None:
        """Update the selection status of color swatches."""
        # Remove selection from all swatches
        for swatch in self.query(".color-swatch"):
            swatch.remove_class("selected-swatch")

        # Mark foreground swatch as selected
        for i, color in enumerate(self.palette.colors if self.palette else []):
            if color.hex == self.foreground_color.hex:
                try:
                    swatch = self.query_one(f"#color-{i}", Static)
                    swatch.add_class("selected-swatch")
                except Exception:
                    pass

    def on_static_click(self, event: events.Click) -> None:
        """
        Handle clicks on color swatches.

        Args:
            event: The click event
        """
        # Check if this is a color swatch
        if event.widget is None or not hasattr(event.widget, "id"):
            return

        widget_id = event.widget.id
        if not widget_id or not widget_id.startswith("color-"):
            return

        # Extract the color index
        try:
            index = int(widget_id.split("-")[1])
            self._select_color(index)
        except (ValueError, IndexError):
            pass

    def on_container_click(self, event: events.Click) -> None:
        """
        Handle clicks on suggestion items.

        Args:
            event: The click event
        """
        # Check if this is a suggestion item
        if event.widget is None or not hasattr(event.widget, "id"):
            return

        container = event.widget
        container_id = container.id

        if not container_id or not container_id.startswith("suggestion-"):
            return

        # Extract the suggestion index
        try:
            index = int(container_id.split("-")[1])
            suggestion = self.suggestions[index]

            # Apply the suggestion
            self.foreground_color = Color(suggestion["foreground"])
            self.background_color = Color(suggestion["background"])

            self._extracted_from_action_optimize_text_20("Applied suggested colors")
        except (ValueError, IndexError):
            pass

    # Action methods
    def action_reverse_colors(self) -> None:
        """Swap foreground and background colors."""
        fg = self.foreground_color
        bg = self.background_color

        self.foreground_color = bg
        self.background_color = fg

        # Update swatch selection
        self._update_swatch_selection()

        # Notify user
        self.notify("Swapped foreground and background colors")

    def action_suggest_improvements(self) -> None:
        """Generate new suggestions for the current color pair."""
        self._update_accessibility_data()
        self._update_suggestions()

        # Focus on suggestions container
        suggestions = self.query_one("#suggestions", ScrollableContainer)
        suggestions.focus()

        # Notify user
        self.notify("Generated new suggestions")

    def action_optimize_text(self) -> None:
        """Optimize text color for the current background."""
        # Keep the current background but optimize the text color
        bg = self.background_color
        fg = optimize_text_color(bg)

        # Set as foreground
        self.foreground_color = fg

        self._extracted_from_action_optimize_text_20("Optimized text color for current background")

    # TODO Rename this here and in `on_container_click` and `action_optimize_text`
    def _extracted_from_action_optimize_text_20(self, arg0: str) -> None:
        """
        Update UI after applying color changes.

        Args:
            arg0: The notification message to display
        """
        self._update_preview()
        self._update_suggestions()
        self._update_swatch_selection()
        self.notify(arg0)
