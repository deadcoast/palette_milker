"""
Color harmony generator widget for the Palette Milker application.

This module provides a widget for generating color harmonies from a base color,
including complementary, analogous, triadic, tetradic, and monochromatic schemes.
"""

from enum import Enum
from typing import ClassVar
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from textual.app import ComposeResult
from textual.binding import Binding
from textual.color import Color as TextualColor
from textual.containers import Container
from textual.containers import Grid
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Select
from textual.widgets import Static

from ...models.color_model import Color
from ...utils.color_accessibility import analyze_color_pair


class HarmonyType(Enum):
    """Types of color harmonies."""

    COMPLEMENTARY = "Complementary"
    ANALOGOUS = "Analogous"
    TRIADIC = "Triadic"
    TETRADIC = "Tetradic"
    SPLIT_COMPLEMENTARY = "Split Complementary"
    MONOCHROMATIC = "Monochromatic"
    SHADES = "Shades"
    TINTS = "Tints"


class ColorSelected(Message):
    """Message sent when a color is selected from the harmonies."""

    def __init__(self, harmony_type: HarmonyType, color: Color) -> None:
        """
        Initialize with the harmony type and selected color.

        Args:
            harmony_type: The type of harmony the color came from
            color: The selected color
        """
        self.harmony_type = harmony_type
        self.color = color
        super().__init__()


class HarmonyGenerator(Container):
    """
    Widget for generating and displaying color harmonies.

    This widget takes a base color and generates various color harmonies,
    displaying them in swatches that can be selected and added to palettes.
    """

    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        Binding("c", "copy_color", "Copy color", show=False),
        Binding("a", "add_to_palette", "Add to palette", show=False),
    ]

    DEFAULT_CSS = """
    HarmonyGenerator {
        width: 100%;
        height: auto;
        border: solid $primary;
        padding: 1;
        background: $surface;
    }

    #harmony-title {
        width: 100%;
        height: 1;
        content-align: center middle;
        background: $primary;
        color: $text;
    }

    #harmony-controls {
        width: 100%;
        height: 3;
        margin: 1 0;
    }

    #harmony-type-selector {
        width: 100%;
    }

    #harmony-display {
        width: 100%;
        min-height: 6;
    }

    .harmony-grid {
        width: 100%;
        grid-size: 4 2;
        grid-columns: 1fr 1fr 1fr 1fr;
        grid-rows: 3 1;
        padding: 0;
    }

    .color-swatch {
        width: 100%;
        height: 3;
        content-align: center middle;
        border: solid $background;
    }

    .swatch-selected {
        border: tall $accent;
    }

    .color-info {
        width: 100%;
        height: 1;
        content-align: center middle;
        background: $surface;
    }

    .base-color {
        border: tall $accent;
    }

    #harmony-info {
        width: 100%;
        margin-top: 1;
        padding: 0 1;
    }

    #accessibility-info {
        margin-top: 1;
        background: $panel;
        padding: 0 1;
    }
    """

    # Reactive properties
    base_color: reactive[Color] = reactive(Color("#FFFFFF"))
    selected_harmony: reactive[HarmonyType] = reactive(HarmonyType.COMPLEMENTARY)
    harmony_colors: reactive[List[Color]] = reactive([])
    selected_color_index: reactive[int] = reactive(0)

    def __init__(
        self, base_color: Union[str, Color] = "#FFFFFF", widget_id: Optional[str] = None, classes: Optional[str] = None
    ):
        """
        Initialize the harmony generator.

        Args:
            base_color: Base color to generate harmonies from
            widget_id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
        self.base_color = base_color if isinstance(base_color, Color) else Color(base_color)

    def compose(self) -> ComposeResult:
        """Compose the harmony generator widget."""
        # Title
        yield Static("COLOR HARMONIES", id="harmony-title")

        # Controls for harmony type
        with Container(id="harmony-controls"):
            harmony_options = [(t.value, t.value) for t in HarmonyType]
            yield Select(harmony_options, value=HarmonyType.COMPLEMENTARY.value, id="harmony-type-selector")

        # Display area for the harmonies
        with Container(id="harmony-display"):
            # This will be populated in _update_display
            pass

        # Information about the selected harmony
        yield Static("", id="harmony-info")

        # Accessibility information
        yield Static("", id="accessibility-info")

    def on_mount(self) -> None:
        """Set up the widget when it's mounted."""
        # Generate initial harmonies
        self._generate_harmony_colors()
        self._update_display()

    def watch_base_color(self, old_value: Color, new_value: Color) -> None:
        """React to base color changes."""
        if old_value != new_value:
            self._generate_harmony_colors()
            self._update_display()

    def watch_selected_harmony(self, old_value: HarmonyType, new_value: HarmonyType) -> None:
        """React to selected harmony type changes."""
        if old_value != new_value:
            self._generate_harmony_colors()
            self._update_display()

    def watch_selected_color_index(self, old_value: int, new_value: int) -> None:
        """React to selected color index changes."""
        if old_value != new_value:
            self._update_selection()
            self._update_info()

    def _generate_harmony_colors(self) -> None:
        """Generate the harmony colors based on the selected harmony type."""
        harmony_type = self.selected_harmony
        base = self.base_color

        if harmony_type == HarmonyType.COMPLEMENTARY:
            # Base color + complementary
            comp = base.complementary()
            self.harmony_colors = [base, comp]

        elif harmony_type == HarmonyType.ANALOGOUS:
            # Base color + 2 analogous colors on each side
            analogous = base.analogous(5, 30)  # 5 colors, 30° apart
            self.harmony_colors = analogous

        elif harmony_type == HarmonyType.TRIADIC:
            # Base color + 2 colors 120° apart
            triadic = base.triadic()
            self.harmony_colors = triadic

        elif harmony_type == HarmonyType.TETRADIC:
            # Base color + 3 colors 90° apart (rectangle on color wheel)
            tetradic = base.tetradic()
            self.harmony_colors = tetradic

        elif harmony_type == HarmonyType.SPLIT_COMPLEMENTARY:
            self._extracted_from__generate_harmony_colors_28(base)
        elif harmony_type == HarmonyType.MONOCHROMATIC:
            # Base color + variations of saturation and lightness
            h, s, lightness = base.hsl
            colors = [base]

            # Add 3 variations with different saturation
            for s_mod in [-20, -10, 10]:
                new_s = max(0, min(100, s + s_mod))
                colors.append(Color({"h": h, "s": new_s, "l": lightness}))

            # Add 4 variations with different lightness
            for lightness_mod in [-20, -10, 10, 20]:
                new_lightness = max(0, min(100, lightness + lightness_mod))
                colors.append(Color({"h": h, "s": s, "l": new_lightness}))

            self.harmony_colors = colors[:8]  # Limit to 8 colors for display

        elif harmony_type == HarmonyType.SHADES:
            # Base color + progressively darker versions
            colors = [base]
            colors.extend(base.darken(amount) for amount in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
            self.harmony_colors = colors

        elif harmony_type == HarmonyType.TINTS:
            # Base color + progressively lighter versions
            colors = [base]
            colors.extend(base.lighten(amount) for amount in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
            self.harmony_colors = colors

    # TODO Rename this here and in `_generate_harmony_colors`
    def _extracted_from__generate_harmony_colors_28(self, base):
        # Base color + 2 colors on either side of complementary
        comp = base.complementary()
        h, s, lightness = comp.hsl
        h1 = (h - 30) % 360
        h2 = (h + 30) % 360
        split1 = Color({"h": h1, "s": s, "l": lightness})
        split2 = Color({"h": h2, "s": s, "l": lightness})
        self.harmony_colors = [base, split1, split2]

    def _update_display(self) -> None:
        """Update the color harmony display with current colors."""
        # Get the container for the display
        container = self.query_one("#harmony-display", Container)

        # Remove existing content
        container.remove_children()

        # Create a container for the harmony grid
        grid = Grid(classes="harmony-grid")
        container.mount(grid)

        # Add swatches for each color
        for i, color in enumerate(self.harmony_colors[:8]):  # Limit to 8 colors
            # Use TextualColor since we're setting the style directly
            textual_color = TextualColor.parse(color.hex)

            # Create swatch with base class
            classes = "color-swatch"
            if i == 0:
                classes += " base-color"  # Mark the base color
            if i == self.selected_color_index:
                classes += " swatch-selected"  # Mark selected color

            # Create and add the swatch
            swatch = Static(f"{color.hex}", id=f"swatch-{i}", classes=classes)
            swatch.styles.background = textual_color

            # Set text color for contrast
            text_color = TextualColor.parse("#FFFFFF") if self._is_dark(color) else TextualColor.parse("#000000")
            swatch.styles.color = text_color

            grid.mount(swatch)

            # Add color info
            h, s, lightness = color.hsl
            info = f"H:{h}° S:{s}% L:{lightness}%"
            info_label = Static(info, id=f"info-{i}", classes="color-info")
            grid.mount(info_label)

        # Update the information displays
        self._update_info()

    def _update_selection(self) -> None:
        """Update the selected color swatch."""
        # Remove selection from all swatches
        for swatch in self.query(".color-swatch"):
            swatch.remove_class("swatch-selected")

        # Add selection to the current swatch
        try:
            current_swatch = self.query_one(f"#swatch-{self.selected_color_index}", Static)
            current_swatch.add_class("swatch-selected")
        except Exception:
            # Ignore if the swatch doesn't exist
            pass

    def _update_info(self) -> None:
        """Update the harmony and accessibility information displays."""
        # Get the selected color
        if not self.harmony_colors or self.selected_color_index >= len(self.harmony_colors):
            return

        selected_color = self.harmony_colors[self.selected_color_index]

        # Update harmony info
        harmony_info = self.query_one("#harmony-info", Static)
        harmony_type_name = self.selected_harmony.value
        harmony_info.update(f"{harmony_type_name}: {selected_color.hex}")

        # Update accessibility info
        accessibility_info = self.query_one("#accessibility-info", Static)

        if self.selected_color_index > 0:  # Check against base color
            self._extracted_from__update_info_18(selected_color, accessibility_info)
        else:
            accessibility_info.update("")

    # TODO Rename this here and in `_update_info`
    def _extracted_from__update_info_18(self, selected_color, accessibility_info):
        base_color = self.harmony_colors[0]
        analysis = analyze_color_pair(selected_color, base_color)

        ratio = analysis["formatted_ratio"]
        passes_aa = "✓" if analysis["passes_aa_normal"] else "✗"
        passes_aaa = "✓" if analysis["passes_aaa_normal"] else "✗"

        accessibility_info.update(f"Contrast with base: {ratio} | AA: {passes_aa} | AAA: {passes_aaa}")

    def _is_dark(self, color: Color) -> bool:
        """Check if a color is dark (for contrast)."""
        r, g, b = color.rgb
        return r * 299 + g * 587 + b * 114 < 128000

    def on_select_changed(self, event: Select.Changed) -> None:
        """Handle selection changes for the harmony type."""
        # Get the new harmony type
        harmony_value = event.value

        # Find the corresponding HarmonyType enum value
        for harmony_type in HarmonyType:
            if harmony_type.value == harmony_value:
                self.selected_harmony = harmony_type
                break

    def on_static_click(self, event) -> None:
        """Handle clicks on color swatches."""
        # Check if this is a color swatch
        widget_id = event.widget.id
        if not widget_id or not widget_id.startswith("swatch-"):
            return

        # Extract the color index
        try:
            index = int(widget_id.split("-")[1])
            if 0 <= index < len(self.harmony_colors):
                self.selected_color_index = index
        except (ValueError, IndexError):
            pass

    def on_click(self, event) -> None:
        """Handle clicks on any widget."""
        # Only process if target is a Static
        if not isinstance(event.widget, Static):
            return

        # Forward to static click handler
        self.on_static_click(event)

    def on_mouse_down(self, event) -> None:
        """Handle mouse down events for double-click detection."""
        # Check if this is a color swatch (Static widget)
        if not isinstance(event.widget, Static):
            return

        widget_id = event.widget.id
        if not widget_id or not widget_id.startswith("swatch-"):
            return

        # For double clicks, we'll check if it's a double click in on_click
        # by tracking the time between clicks
        if event.button == 1 and event.count == 2:  # Left button, double click
            # Extract the color index
            try:
                index = int(widget_id.split("-")[1])
                if 0 <= index < len(self.harmony_colors):
                    self.selected_color_index = index
                    self.post_message(ColorSelected(self.selected_harmony, self.harmony_colors[index]))
            except (ValueError, IndexError):
                pass

    def action_copy_color(self) -> None:
        """Copy the selected color."""
        if not self.harmony_colors or self.selected_color_index >= len(self.harmony_colors):
            return

        color = self.harmony_colors[self.selected_color_index]
        # In a real implementation, this would copy to the clipboard
        self.notify(f"Copied {color.hex}")

    def action_add_to_palette(self) -> None:
        """Add the selected color to the active palette."""
        if not self.harmony_colors or self.selected_color_index >= len(self.harmony_colors):
            return

        color = self.harmony_colors[self.selected_color_index]
        self.post_message(ColorSelected(self.selected_harmony, color))
        self.notify(f"Added {color.hex} to palette")

    def update_base_color(self, color: Union[str, Color]) -> None:
        """
        Update the base color used for harmony generation.

        Args:
            color: New base color
        """
        self.base_color = color if isinstance(color, Color) else Color(color)
