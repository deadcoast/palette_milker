"""
Export widgets for the Milky Color Suite.

This module contains widgets for exporting color palettes in different formats,
implementing the exact terminal-based UI design specified.
"""

import json
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

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

from ascii.ascii_patterns import create_button
from ascii.ascii_patterns import create_dropdown
from ascii.ascii_patterns import create_export_panel
from .ascii_widget import ASCIIWidget


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
    """

    FORMATS = ["CSS", "SCSS", "LESS", "JSON", "TXT", "ASE", "GPL"]

    selected_format: reactive[str] = reactive("CSS")
    expanded: reactive[bool] = reactive(False)

    def __init__(
        self,
        selected_format: str = "CSS",
        name: Optional[str] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the FormatSelector widget.

        Args:
            selected_format: The initially selected format
            name: The name of the widget
            id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=id, classes=classes)
        if selected_format in self.FORMATS:
            self.selected_format = selected_format
        else:
            self.selected_format = self.FORMATS[0]

    def render(self) -> RenderableType:
        """Render the FormatSelector widget."""
        pattern = create_dropdown(self.selected_format, self.expanded)
        return Text(pattern)

    def on_click(self, event: events.Click) -> None:
        """
        Handle click events.

        Args:
            event: The click event
        """
        self.expanded = not self.expanded
        self.refresh()

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
            self.refresh()
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
        # Get the active palette from our model
        active_palette = self.app.palette_model.get_active_palette()

        # Export using the UTTER format
        export_data = export_palette_to_utter(active_palette)

        # Display the exported content
        self.query_one("#export-content").update(export_data["content"])

        # Save to clipboard if requested
        if self.export_format == "utter":
            # ...handle clipboard logic
            pass


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
        id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the FormatOptions widget.

        Args:
            formats: The available formats
            name: The name of the widget
            id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=id, classes=classes)
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
        target = event.target
        if isinstance(target, Static) and "option" in target.classes:
            # Extract the format name from the ID
            format_name = target.id.split("-")[1]

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

    DEFAULT_CSS = """
    ExportPanel {
        width: 70;
        height: 20;
        background: ;
    }

    ExportPanel #export-preview {
        width: 60;
        height: 10;
        margin: 1 4;
        background: $background-lighten-1;
        color: $text;
    }

    ExportPanel #format-selector {
        width: 20;
        height: 3;
        margin: 1 1 1 4;
    }

    ExportPanel #format-options {
        width: 20;
        margin: 0 0 0 4;
    }

    ExportPanel #export-button {
        width: 15;
        height: 3;
        margin: 1 4 1 1;
    }
    """

    selected_format: reactive[str] = reactive("CSS")
    colors: reactive[List[str]] = reactive([])
    palette_name: reactive[str] = reactive("Default")

    def __init__(
        self,
        colors: Optional[List[str]] = None,
        palette_name: str = "Default",
        selected_format: str = "CSS",
        name: Optional[str] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ExportPanel widget.

        Args:
            colors: The colors to export
            palette_name: The name of the palette
            selected_format: The selected export format
            name: The name of the widget
            id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=id, classes=classes)
        self.colors = colors if colors is not None else ["#FFFFFF"] * 8
        self.palette_name = palette_name
        self.selected_format = selected_format

    def compose(self) -> ComposeResult:
        """Compose the ExportPanel widget."""
        # ASCII panel frame

        # Format selector
        yield FormatSelector(selected_format=self.selected_format, id="format-selector")

        # Format options (hidden by default)
        yield FormatOptions(id="format-options")

        # Export button
        yield Button("Export", id="export-button")

        # Export preview
        yield TextArea(self._generate_preview(), id="export-preview", readonly=True)

    def _generate_preview(self) -> str:
        """
        Generate a preview of the exported colors.

        Returns:
            A string preview of the exported colors
        """
        format_name = self.selected_format
        palette_name = self.palette_name
        colors = self.colors

        # Generate the preview based on the format
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
                preview += f"Color {i + 1}: {color}\n"

        elif format_name == "ASE":
            preview = f"# Adobe Swatch Exchange format\n# Palette: {palette_name}\n\n"
            preview += "Note: ASE is a binary format and cannot be previewed directly.\n"
            preview += "The actual export will create a proper ASE file."

        elif format_name == "GPL":
            preview = f"GIMP Palette\nName: {palette_name}\n"
            preview += "Columns: 8\n#\n"
            for color in colors:
                # Convert hex to RGB values
                try:
                    c = Color(color)
                    r, g, b = (int(v * 255) for v in c.rgb)
                    preview += f"{r} {g} {b} {color}\n"
                except Exception:
                    preview += f"255 255 255 {color}\n"

        else:
            preview = f"Format '{format_name}' not implemented yet."

        return preview

    def watch_selected_format(self, selected_format: str) -> None:
        """
        Watch for changes to the selected format.

        Args:
            selected_format: The new selected format
        """
        # Update the preview
        preview = self._generate_preview()
        self.query_one("#export-preview", TextArea).text = preview

    def watch_colors(self, colors: List[str]) -> None:
        """
        Watch for changes to the colors.

        Args:
            colors: The new colors
        """
        # Update the preview
        preview = self._generate_preview()
        self.query_one("#export-preview", TextArea).text = preview

    def watch_palette_name(self, palette_name: str) -> None:
        """
        Watch for changes to the palette name.

        Args:
            palette_name: The new palette name
        """
        # Update the preview
        preview = self._generate_preview()
        self.query_one("#export-preview", TextArea).text = preview

    def on_format_selector_show_options(self, message: FormatSelector.ShowOptions) -> None:
        """
        Handle format selector show options messages.

        Args:
            message: The show options message
        """
        # Show the format options
        self.query_one("#format-options", FormatOptions).show()

    def on_format_selector_hide_options(self, message: FormatSelector.HideOptions) -> None:
        """
        Handle format selector hide options messages.

        Args:
            message: The hide options message
        """
        # Hide the format options
        self.query_one("#format-options", FormatOptions).hide()

    def on_format_option_selected(self, message: FormatOptions.FormatOptionSelected) -> None:
        """
        Handle format option selected messages.

        Args:
            message: The format option selected message
        """
        # Update the format selector
        self.query_one("#format-selector", FormatSelector).select_format(message.format_name)

        # Update the selected format
        self.selected_format = message.format_name

        # Hide the format options
        self.query_one("#format-options", FormatOptions).hide()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events.

        Args:
            event: The button press event
        """
        if event.button.id == "export-button":
            # Notify of export request
            self.post_message(self.ExportRequested(self.selected_format, self.palette_name, self.colors))

    class ExportRequested(Message):
        """Message sent when export is requested."""

        def __init__(self, format_name: str, palette_name: str, colors: List[str]) -> None:
            """
            Initialize the ExportRequested message.

            Args:
                format_name: The selected format
                palette_name: The name of the palette
                colors: The colors to export
            """
            self.format_name = format_name
            self.palette_name = palette_name
            self.colors = colors
            super().__init__()
