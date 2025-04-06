"""
Export screen for the Palette Milker application.

This screen provides options for exporting palettes in various formats.
"""

import os
from typing import Any
from typing import ClassVar
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.message import Message
from textual.widgets import Button
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import Static
from textual.widgets import TextArea

from ..models.color_model import Color
from ..utils.export_utils import export_palette
from ..widgets.export.export_widget import ExportPanel
from .base_screen import BaseScreen


class FileDialogMessage(Message):
    """Message to request a file dialog operation."""

    class DialogType:
        """Enumeration of dialog types."""

        SAVE = "save"
        OPEN = "open"

    def __init__(self, dialog_type: str, file_filters: Optional[Dict[str, List[str]]] = None) -> None:
        """Initialize the file dialog message.

        Args:
            dialog_type: Type of dialog (save/open)
            file_filters: Optional filters for file types
        """
        self.dialog_type = dialog_type
        self.file_filters = file_filters or {}
        super().__init__()


class ExportScreen(BaseScreen):
    """
    Screen for exporting palettes in various formats.

    This screen provides a user interface for selecting export formats
    and customizing export options.
    """

    # Define bindings consistent with the app
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Application controls
        Binding("ctrl+q", "app.quit", "Quit", priority=True),
        Binding("f1", "app.toggle_help", "Help"),
        # Export actions
        Binding("ctrl+e", "export", "Export palette"),
        Binding("ctrl+c", "copy_to_clipboard", "Copy to clipboard"),
        # Navigation between sections
        Binding("1", "app.view_palette", "Palette view"),
        Binding("2", "app.view_color_picker", "Color picker"),
        Binding("escape", "app.view_palette", "Back to palette"),
    ]

    DEFAULT_CSS = """
    ExportScreen {
        layout: vertical;
    }

    #export-title {
        content-align: center middle;
        text-style: bold;
        background: $primary;
        color: $text;
        height: 1;
    }

    #export-container {
        width: 100%;
        height: 100%;
        padding: 1;
    }

    #export-instructions {
        margin-bottom: 1;
    }

    #export-buttons {
        layout: horizontal;
        height: 3;
        margin-top: 1;
    }

    Button {
        margin-right: 2;
    }

    #export-status {
        background: $surface;
        color: $text;
        margin-top: 1;
        padding: 1;
        border: solid $primary;
        height: 3;
        display: none;
    }

    #export-status.visible {
        display: block;
    }

    #export-status.success {
        border: solid $success;
        color: $success;
    }

    #export-status.error {
        border: solid $error;
        color: $error;
    }
    """

    def __init__(self) -> None:
        """Initialize the export screen."""
        super().__init__()
        self.export_format = "CSS"
        self.palette_name = "Untitled Palette"
        self.palette_colors = ["#FFFFFF"] * 8

    def compose(self) -> ComposeResult:
        """Compose the export screen UI."""
        # Include base components
        yield from super().compose()

        yield Header()

        with Container(id="export-container"):
            yield Static("Export Palette", id="export-title")
            yield Static("Select a format and customize export options below.", id="export-instructions")

            # Main export panel
            yield ExportPanel(widget_id="export-panel")

            with Container(id="export-buttons"):
                yield Button("Export to File", id="export-file", variant="primary")
                yield Button("Copy to Clipboard", id="copy-clipboard", variant="default")
                yield Button("Back to Palette", id="back-button", variant="default")

        yield Footer()

    def on_mount(self) -> None:
        """Handle screen mounting."""
        # Try to get current palette information from the app
        try:
            # Access the app's palette information
            app = self.app
            if hasattr(app, "current_palette") and hasattr(app, "palettes"):
                self._extracted_from_on_mount_10(app)
        except Exception as e:
            self.log.error(f"Error getting palette information: {e}")

    # TODO Rename this here and in `on_mount`
    def _extracted_from_on_mount_10(self, app: Any) -> None:
        """
        Update export panel with palette information from app.

        Args:
            app: The application instance containing palette data
        """
        palette_name = app.current_palette
        palette_colors = app.palettes.get(palette_name, ["#FFFFFF"] * 8)

        # Update the export panel
        export_panel = self.query_one(ExportPanel)
        export_panel.palette_name = palette_name
        export_panel.palette_colors = palette_colors

        # Store locally
        self.palette_name = palette_name
        self.palette_colors = palette_colors

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "export-file":
            self.action_export()
        elif event.button.id == "copy-clipboard":
            self.action_copy_to_clipboard()
        elif event.button.id == "back-button":
            self.app.switch_screen("main")

    def on_export_panel_export_requested(self, message: ExportPanel.ExportRequested) -> None:
        """
        Handle export request from the ExportPanel.

        Args:
            message: Message containing export request details
        """
        # Update local variables
        self.export_format = message.format_name
        self.palette_name = message.palette_name
        self.palette_colors = message.palette_colors

        # Show status that export format is ready
        status = self.query_one("#export-status", Static)
        status.update(f"Format '{self.export_format}' ready to export. Click 'Export to File' to save.")
        status.remove_class("error")
        status.remove_class("success")
        status.add_class("visible")

    def action_export(self) -> None:
        """Export the palette to a file."""
        # Get the export panel
        export_panel = self.query_one(ExportPanel)

        # Get export information
        format_name = export_panel.selected_format
        palette_name = export_panel.palette_name
        colors = export_panel.palette_colors

        # Get appropriate file extension
        extension = self._get_file_extension(format_name)

        # Request file dialog via a message
        # This would be handled by the App, which has access to system dialogs
        file_filters = {
            "CSS Files": ["*.css"],
            "SCSS Files": ["*.scss"],
            "LESS Files": ["*.less"],
            "JSON Files": ["*.json"],
            "Text Files": ["*.txt"],
            "Adobe Swatch Exchange": ["*.ase"],
            "GIMP Palette": ["*.gpl"],
            "All Files": ["*.*"],
        }

        self.post_message(FileDialogMessage(FileDialogMessage.DialogType.SAVE, file_filters))

        # In a real implementation, we'd wait for the dialog result
        # For now, simulate it with a fake path for demonstration
        demo_path = os.path.expanduser(f"~/Downloads/{palette_name}{extension}")
        self._perform_export(colors, palette_name, format_name, demo_path)

    def _get_file_extension(self, format_name: str) -> str:
        """Get the appropriate file extension for the given format."""
        format_extensions = {
            "CSS": ".css",
            "SCSS": ".scss",
            "LESS": ".less",
            "JSON": ".json",
            "TXT": ".txt",
            "ASE": ".ase",
            "GPL": ".gpl",
            "UTTER": ".css",  # UTTER also exports as CSS
        }
        return format_extensions.get(format_name, ".txt")

    def _perform_export(self, colors: List[str], palette_name: str, format_name: str, file_path: str) -> None:
        """Perform the actual export operation."""

        def export_operation() -> str:
            """
            Export the palette to a file.

            Returns:
                Path to the exported file
            """
            # Convert color strings to Color objects
            color_objects = [Color(color) for color in colors]

            # Use export_palette from export_utils with appropriate casting
            from typing import cast

            # Cast the list to make the type checker happy
            result = export_palette(cast(List[Union[str, Color]], color_objects), palette_name, format_name, file_path)
            return result

        # Use the try_operation method from BaseScreen
        success, _result, _error_info = self.try_operation(
            operation=export_operation,
            error_message=f"Error exporting palette to {file_path}",
            success_message=f"Successfully exported palette to {file_path}",
            context={"format": format_name, "palette_name": palette_name, "file_path": file_path},
        )

        if success:
            # Show success in the status container
            self.show_status(f"Palette exported to {file_path}", "success")

    def action_copy_to_clipboard(self) -> None:
        """Copy the export content to clipboard."""

        def copy_operation() -> str:
            """
            Get the export content to copy to clipboard.

            Returns:
                Content to be copied to clipboard
            """
            # Get the export panel
            export_panel = self.query_one(ExportPanel)

            # Get the text from the preview area
            preview_widget = export_panel.query_one("#export-preview", TextArea)
            export_content = preview_widget.text

            # In a real implementation, we'd actually copy to system clipboard
            # For now, we just return the content
            return export_content

        # Use the try_operation method from BaseScreen
        success, _result, _error_info = self.try_operation(
            operation=copy_operation,
            error_message="Error copying to clipboard",
            success_message="Copied to clipboard!",
            severity="warning",  # Less severe than an error
        )

        if success:
            # Additional UI feedback if needed
            self.show_status("Content copied to clipboard", "success", timeout=3)
