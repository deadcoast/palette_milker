"""
Export widgets for the Milky Color Suite.

This module contains widgets for exporting color palettes in different formats,
implementing the exact terminal-based UI design specified.
"""

import json
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import cast

from colour import Color
from rich.console import RenderableType
from rich.text import Text
from textual import events
from textual.app import ComposeResult
from textual.containers import Container
from textual.containers import Horizontal
from textual.containers import Vertical
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button
from textual.widgets import Input
from textual.widgets import Select
from textual.widgets import Static
from textual.widgets import TextArea

from constants.builder import create_button
from constants.builder import create_dropdown
from constants.builder import create_export_panel
from src.utils.utter import UTTER
from widgets.ascii_widget import ASCIIWidget


def export_palette_to_utter(palette: Dict[str, Any]) -> Dict[str, Any]:
    """
    Export a palette to UTTER format.

    Creates a comprehensive color mapping using the palette data and generates
    CSS variables using the UTTER bottles system.

    Args:
        palette: The palette to export, should contain 'colors' and 'name'

    Returns:
        A dictionary with export data including content, raw data and UTTER instance

    Raises:
        ValueError: If palette data is invalid
    """
    if not isinstance(palette, dict) or 'colors' not in palette:
        raise ValueError("Invalid palette data - must contain colors list")

    # Create an UTTER instance from the palette colors
    colors = palette.get("colors", []) or ["#000000"] * 8

    # Create a dictionary mapping color names to hex values
    color_dict: Dict[str, str] = {}

    # Add standard color mappings based on position
    color_names = [
        "primary", "secondary", "tertiary", "accent",
        "light", "dark", "neutral", "highlight"
    ]

    # Map available colors to standard names
    for i, color in enumerate(colors):
        if i < len(color_names):
            color_dict[color_names[i]] = color
        # Also add numeric keys for all colors
        color_dict[f"color{i + 1}"] = color

    # Add darker/lighter variants for primary colors
    if "primary" in color_dict:
        # Simple simulation of darker/lighter variants
        primary = color_dict["primary"]
        if primary.startswith("#"):
            color_dict["primaryDarken"] = primary + "cc"  # Add alpha for darker
            color_dict["primaryLighten"] = primary + "66"  # Add alpha for lighter

    # Create the UTTER instance
    try:
        utter = UTTER.create_from_palette(color_dict)

        # Add a custom bottle for the specific palette
        palette_vars = {f"color-{i + 1}": color for i, color in enumerate(colors)}
        utter.create_custom_bottle("PaletteColors", palette_vars)

        # Convert to string representation
        content = utter.to_css()

        return {
            "format": "UTTER",
            "content": content,
            "palette": palette,
            "utter": utter,
            "raw": utter.to_dict(),
            "json": utter.to_json()
        }
    except Exception as e:
        # Fallback to simple CSS if UTTER creation fails
        content = "/* Error creating UTTER format, fallback to simple CSS */\n:root {\n"
        for i, color in enumerate(colors):
            content += f"  --color-{i + 1}: {color};\n"
        content += "}\n"

        return {
            "format": "CSS",
            "content": content,
            "palette": palette,
            "error": str(e)
        }


class FormatSelector(Widget):
    """
    A widget for selecting an export format.

    This widget displays a dropdown of available export formats.
    """

    DEFAULT_CSS = """
    FormatSelector {
        width: 20;
        height: 3;
    }

    FormatSelector #dropdown-display {
        width: 100%;
        height: 1;
        border: solid $primary;
        padding: 0 1;
    }

    FormatSelector #dropdown-arrow {
        width: 1;
        height: 1;
        content-align: center middle;
    }
    """

    FORMATS: ClassVar[List[str]] = ["CSS", "SCSS", "LESS", "JSON", "TXT", "ASE", "GPL"]

    selected_format: reactive[str] = reactive("CSS")
    expanded: reactive[bool] = reactive(False)

    def __init__(
        self,
        selected_format: str = "CSS",
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the FormatSelector widget.

        Args:
            selected_format: The initially selected format
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        if selected_format in self.FORMATS:
            self.selected_format = selected_format
        else:
            self.selected_format = self.FORMATS[0]

    def compose(self) -> ComposeResult:
        """Compose the FormatSelector widget with proper child widgets."""
        with Horizontal():
            yield Static(self.selected_format, id="dropdown-display")
            yield Static("▼", id="dropdown-arrow")

    def watch_selected_format(self, old_format: str, new_format: str) -> None:
        """Watch for changes to the selected format.

        Args:
            old_format: The previous format
            new_format: The new format
        """
        # Update the display text
        display = self.query_one("#dropdown-display", Static)
        display.update(new_format)

    def on_click(self, event: events.Click) -> None:
        """
        Handle click events.

        Args:
            event: The click event
        """
        self.expanded = not self.expanded

        if self.expanded:
            # Show the dropdown options
            self.post_message(self.ShowOptions())
        else:
            # Hide the dropdown options
            self.post_message(self.HideOptions())

    def select_format(self, format_name: str) -> None:
        """
        Select a format.

        Args:
            format_name: The format to select
        """
        if format_name in self.FORMATS:
            self.selected_format = format_name
            self.expanded = False
            self.post_message(self.FormatSelected(format_name))

    class ShowOptions(Message):
        """Message sent when the dropdown is expanded."""

        pass

    class HideOptions(Message):
        """Message sent when the dropdown is collapsed."""

        pass

    class FormatSelected(Message):
        """Message sent when a format is selected."""

        def __init__(self, format_name: str) -> None:
            """
            Initialize the FormatSelected message.

            Args:
                format_name: The selected format
            """
            self.format_name = format_name
            super().__init__()

    def on_export_button_pressed(self):
        """Handle export button press."""
        # Get the active palette from app (using cast for type safety)
        app = cast(Any, self.app)

        # Get the active palette - safely check if palette_model exists
        active_palette = {}
        if hasattr(app, "palette_model"):
            active_palette = app.palette_model.get_active_palette()

        # Export using the UTTER format
        export_data = export_palette_to_utter(active_palette)

        # Display the exported content
        preview_widget = self.query_one("#export-content", Static)
        preview_widget.update(export_data["content"])


class FormatOptions(Container):
    """
    A container of format options.

    This widget displays a list of format options that can be selected.
    """

    DEFAULT_CSS = """
    FormatOptions {
        width: 20;
        background: $surface;
        border: solid $primary;
        display: none;
    }

    FormatOptions.visible {
        display: block;
    }

    FormatOptions .option {
        width: 100%;
        height: 1;
        padding: 0 1;
    }

    FormatOptions .option:hover {
        background: $accent;
    }
    """

    formats: reactive[List[str]] = reactive([])

    def __init__(
        self,
        formats: Optional[List[str]] = None,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the FormatOptions widget.

        Args:
            formats: The available formats
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        if formats is not None:
            self.formats = formats
        else:
            self.formats = ["CSS", "SCSS", "LESS", "JSON", "TXT", "ASE", "GPL"]

    def compose(self) -> ComposeResult:
        """Compose the FormatOptions widget."""
        for format_name in self.formats:
            yield Static(format_name, classes="option", id=f"option-{format_name}")

    def on_click(self, event: events.Click) -> None:
        """
        Handle click events.

        Args:
            event: The click event
        """
        # Check if the target widget is a Static widget with the 'option' class
        widget = event.widget
        if isinstance(widget, Static) and "option" in widget.classes:
            # Extract the format name from the ID, handling None case
            widget_id = widget.id
            if widget_id is not None and "-" in widget_id:
                format_name = widget_id.split("-")[1]
                # Notify of format selection
                self.post_message(self.FormatOptionSelected(format_name))

    def show(self) -> None:
        """Show the format options."""
        self.add_class("visible")

    def hide(self) -> None:
        """Hide the format options."""
        self.remove_class("visible")

    class FormatOptionSelected(Message):
        """Message sent when a format option is selected."""

        def __init__(self, format_name: str) -> None:
            """
            Initialize the FormatOptionSelected message.

            Args:
                format_name: The selected format
            """
            self.format_name = format_name
            super().__init__()


class ExportPanel(Container):
    """
    A panel for exporting color palettes.

    This widget displays a panel with options for exporting a color palette,
    including format selection and preview.
    """

    # Available export formats
    FORMATS: ClassVar[List[str]] = ["CSS", "SCSS", "LESS", "JSON", "TXT", "ASE", "GPL", "UTTER"]

    DEFAULT_CSS = """
    ExportPanel {
        width: 100%;
        height: 100%;
        background: $panel;
        border: solid $primary;
        padding: 1;
    }

    ExportPanel #format-selector {
        width: 20;
        height: 3;
        margin: 1;
    }

    ExportPanel #export-preview {
        width: 100%;
        height: 100%;
        background: $surface;
        border: solid $primary;
        margin: 1;
    }

    ExportPanel #export-button {
        width: 15;
        height: 3;
        margin: 1 4 1 1;
    }

    ExportPanel .format-option {
        background: $panel;
        width: 100%;
    }

    ExportPanel .format-option:hover {
        background: $accent;
    }
    """

    # Define reactive properties properly
    selected_format: reactive[str] = reactive("CSS")
    palette_name: reactive[str] = reactive("Default")
    palette_colors: reactive[List[str]] = reactive(["#FFFFFF"] * 8)

    def __init__(
        self,
        colors: Optional[List[str]] = None,
        palette_name: str = "Default",
        selected_format: str = "CSS",
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ExportPanel widget.

        Args:
            colors: The colors to export
            palette_name: The name of the palette
            selected_format: The selected export format
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        # Initialize reactive properties
        if colors is not None:
            self.palette_colors = colors.copy()  # Create a copy to avoid reference issues
        self.palette_name = palette_name

        # Validate selected format
        if selected_format in self.FORMATS:
            self.selected_format = selected_format
        else:
            self.selected_format = "CSS"  # Default to CSS

    # Define watchers for reactive properties
    def watch_selected_format(self, old_format: str, new_format: str) -> None:
        """Watch for changes to the selected format.

        Args:
            old_format: The previous format
            new_format: The new format
        """
        self._update_preview()

        # Also update the Select widget if it exists
        try:
            format_selector = self.query_one("#format-selector", Select)
            if format_selector.value != new_format:
                format_selector.value = new_format
        except Exception:
            # The widget might not be mounted yet
            pass

    def watch_palette_colors(self, old_colors: List[str], new_colors: List[str]) -> None:
        """Watch for changes to the palette colors.

        Args:
            old_colors: The previous colors
            new_colors: The new colors
        """
        self._update_preview()

    def watch_palette_name(self, old_name: str, new_name: str) -> None:
        """Watch for changes to the palette name.

        Args:
            old_name: The previous name
            new_name: The new name
        """
        self._update_preview()

    def _update_preview(self) -> None:
        """Update the preview text area."""
        try:
            # Generate the preview content
            preview_content = self._generate_preview()

            # Find the preview widget
            preview_widget = self.query_one("#export-preview", TextArea)

            # Update the preview content
            if preview_widget:
                preview_widget.text = preview_content
        except Exception as e:
            # Handle any errors that might occur during preview generation
            error_message = f"Error updating preview: {str(e)}"
            try:
                # Try to update the preview widget with the error message
                preview_widget = self.query_one("#export-preview", TextArea)
                if preview_widget:
                    preview_widget.text = error_message
            except Exception:
                # If we can't even update the error message, log it
                print(f"Failed to update preview: {error_message}")

    def compose(self) -> ComposeResult:
        """Compose the ExportPanel widget."""
        # Format selector using standard Textual Select widget
        yield Select(
            [(format_name, format_name) for format_name in self.FORMATS],
            value=self.selected_format,
            id="format-selector"
        )

        # Export button
        yield Button("Export", id="export-button", variant="primary")

        # Export preview
        yield TextArea(id="export-preview", read_only=True)

    def on_mount(self) -> None:
        """Initialize the widget when mounted."""
        # Generate initial preview content
        preview_content = self._generate_preview()

        # Update the preview widget
        preview_widget = self.query_one("#export-preview", TextArea)
        preview_widget.text = preview_content

    def _generate_preview(self) -> str:
        """
        Generate a preview of the exported colors.

        Returns:
            A string preview of the exported colors
        """
        format_name = self.selected_format
        palette_name = self.palette_name
        colors = self.palette_colors or ["#FFFFFF"] * 8

        # Sanitize color values outside of the loop to avoid try-except performance hit
        sanitized_colors = []

        # Process each color once before entering any loops
        for color in colors:
            # Default to white for safety
            safe_color = "#FFFFFF"

            # Only try to parse valid-looking hex colors
            if isinstance(color, str) and color.startswith("#"):
                hex_part = color.lstrip("#")

                # Check for valid hex format (3, 4, 6, or 8 digits)
                if len(hex_part) in (3, 4, 6, 8):
                    # Check if it's a valid hex string
                    if all(c in "0123456789ABCDEFabcdef" for c in hex_part):
                        # At this point, we have a valid hex color, but let's still
                        # standardize it via the Color class in a single try-except
                        try:
                            c = Color(color)
                            safe_color = c.hex_l
                        except Exception:
                            # Keep the default white
                            pass

            sanitized_colors.append(safe_color)

        # Use sanitized colors for all format generation
        colors = sanitized_colors

        # Generate the preview based on the format
        try:
            if format_name == "CSS":
                preview = "/* Palette: {} */\n:root {{\n".format(palette_name)
                for i, color in enumerate(colors):
                    preview += f"  --color-{i + 1}: {color};\n"
                preview += "}\n"

            elif format_name == "SCSS":
                preview = "// Palette: {}\n".format(palette_name)
                for i, color in enumerate(colors):
                    preview += f"$color-{i + 1}: {color};\n"

            elif format_name == "LESS":
                preview = "// Palette: {}\n".format(palette_name)
                for i, color in enumerate(colors):
                    preview += f"@color-{i + 1}: {color};\n"

            elif format_name == "JSON":
                colors_dict = {"name": palette_name, "colors": colors}
                preview = json.dumps(colors_dict, indent=2)

            elif format_name == "TXT":
                preview = f"Palette: {palette_name}\n\n"
                for i, color in enumerate(colors):
                    # Extract RGB values for display
                    c = Color(color)
                    r, g, b = (int(v * 255) for v in c.rgb)
                    preview += f"Color {i + 1}: {color} (RGB: {r}, {g}, {b})\n"

            elif format_name == "ASE":
                preview = f"# Adobe Swatch Exchange format\n# Palette: {palette_name}\n\n"
                preview += "Note: ASE is a binary format and cannot be previewed directly.\n"
                preview += "The actual export will create a proper ASE file."

            elif format_name == "GPL":
                preview = f"GIMP Palette\nName: {palette_name}\n"
                preview += "Columns: 8\n#\n"
                for color in colors:
                    # Convert hex to RGB values
                    c = Color(color)
                    r, g, b = (int(v * 255) for v in c.rgb)
                    preview += f"{r} {g} {b} {color}\n"

            elif format_name == "UTTER":
                # Create a palette dictionary for UTTER
                palette_dict = {
                    "name": palette_name,
                    "colors": colors
                }

                # Export using the UTTER format
                export_data = export_palette_to_utter(palette_dict)
                preview = export_data["content"]

            else:
                preview = f"Format '{format_name}' not implemented yet."

            return preview

        except Exception as e:
            # Provide a helpful error message if any format-specific processing fails
            error_message = f"/* Error generating preview for {format_name} format: {e!s} */\n\n"
            error_message += "/* Fallback to basic format */\n\n"
            error_message += f"Palette: {palette_name}\n\n"

            for i, color in enumerate(colors):
                error_message += f"Color {i + 1}: {color}\n"

            return error_message

    def on_select_changed(self, event: Select.Changed) -> None:
        """Handle format selection changes.

        Args:
            event: The select changed event
        """
        if event.select.id == "format-selector" and event.value is not None:
            # Make sure we're assigning a string, not None
            self.selected_format = str(event.value)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events.

        Args:
            event: The button press event
        """
        if event.button.id == "export-button":
            # Notify of export request
            self.post_message(self.ExportRequested(self.selected_format, self.palette_name, self.palette_colors))

    class ExportRequested(Message):
        """Message sent when export is requested."""

        def __init__(self, format_name: str, palette_name: str, palette_colors: List[str]) -> None:
            """
            Initialize the ExportRequested message.

            Args:
                format_name: The selected format
                palette_name: The name of the palette
                palette_colors: The colors to export
            """
            super().__init__()
            self.format_name = format_name
            self.palette_name = palette_name
            self.palette_colors = palette_colors.copy()  # Create a copy to avoid reference issues
