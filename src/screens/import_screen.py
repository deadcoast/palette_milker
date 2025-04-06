"""
Import screen for the Palette Milker application.

This screen provides options for importing palettes from various sources.
"""

import os
from typing import Any
from typing import ClassVar
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union
from typing import cast

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.containers import Horizontal
from textual.message import Message
from textual.widgets import Button
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import Label
from textual.widgets import Static

from ..utils.serialization import import_palette_from_file
from .base_screen import BaseScreen


class ImportFileMessage(Message):
    """Message to request a file import operation."""

    def __init__(self, file_filters: Optional[Dict[str, List[str]]] = None) -> None:
        """Initialize the file import message.

        Args:
            file_filters: Optional filters for file types
        """
        self.file_filters = file_filters or {}
        super().__init__()


class PaletteImportedMessage(Message):
    """Message sent when a palette has been successfully imported."""

    def __init__(self, palette: Dict[str, Any]) -> None:
        """Initialize the message with the imported palette.

        Args:
            palette: The imported palette data
        """
        self.palette = palette
        super().__init__()


class ImportScreen(BaseScreen):
    """
    Screen for importing palettes from various sources.

    This screen provides a user interface for selecting and importing
    palette files in different formats.
    """

    # Define bindings consistent with the app
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Application controls
        Binding("ctrl+q", "app.quit", "Quit", priority=True),
        Binding("f1", "app.toggle_help", "Help"),
        # Import actions
        Binding("ctrl+o", "import_file", "Import from file"),
        Binding("ctrl+v", "import_clipboard", "Import from clipboard"),
        # Navigation between sections
        Binding("1", "app.view_palette", "Palette view"),
        Binding("2", "app.view_color_picker", "Color picker"),
        Binding("3", "app.view_export", "Export options"),
        Binding("escape", "app.view_palette", "Back to palette"),
    ]

    CSS_PATH = "import_screen.tcss"  # Define styles in a separate file

    def __init__(self) -> None:
        """Initialize the import screen."""
        super().__init__()

        # Initialize variables
        self._imported_palette: Optional[Dict[str, Any]] = None  # Stores the currently imported palette

        # Default UI state
        self._import_status = "Awaiting import"

    def compose(self) -> ComposeResult:
        """Compose the import screen UI."""
        # Include base components (error display and status container)
        yield from super().compose()

        yield Header()

        with Container(id="import-container"):
            yield Static("Import Palette", id="import-title")

            with Container(id="import-options"):
                yield Label("Choose a method to import a palette:", id="import-instructions")

                with Horizontal(id="import-buttons"):
                    yield Button("Import from File", id="import-file-button", variant="primary")
                    yield Button("Import from Clipboard", id="import-clipboard-button", variant="default")

                # For drag-and-drop support
                with Container(id="drop-zone"):
                    yield Static("Drag & Drop a File Here", id="drop-label")

            # Preview area for imported palette
            with Container(id="preview-container"):
                yield Static("Preview", id="preview-title")

                with Container(id="palette-preview"):
                    yield Static("No palette imported yet", id="no-palette-message")

                # Import action buttons
                with Horizontal(id="action-buttons"):
                    yield Button("Add to My Palettes", id="add-palette-button", variant="primary")
                    yield Button("Back to Palette View", id="back-button", variant="default")

        yield Footer()

    def on_mount(self) -> None:
        """Handle screen mounting."""
        # Hide the palette preview initially
        preview = self.query_one("#palette-preview", Container)
        preview.display = False

        # Hide the add button initially
        add_button = self.query_one("#add-palette-button", Button)
        add_button.display = False

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id

        if button_id == "import-file-button":
            self.action_import_file()
        elif button_id == "import-clipboard-button":
            self.action_import_clipboard()
        elif button_id == "add-palette-button":
            self.action_add_to_palettes()
        elif button_id == "back-button":
            self.app.switch_screen("main")

    def action_import_file(self) -> None:
        """Import a palette from a file."""
        # Define file filters for the dialog
        file_filters = {
            "All Supported Formats": ["*.json", "*.css", "*.scss", "*.less", "*.gpl", "*.ase", "*.txt"],
            "JSON Files": ["*.json"],
            "CSS Files": ["*.css"],
            "SCSS Files": ["*.scss"],
            "LESS Files": ["*.less"],
            "GIMP Palette": ["*.gpl"],
            "Adobe Swatch Exchange": ["*.ase"],
            "Text Files": ["*.txt"],
            "All Files": ["*.*"],
        }

        # Post message to request file selection
        self.post_message(ImportFileMessage(file_filters))

        # In a real implementation, we'd wait for the dialog result
        # For now, simulate it with a fake file for demonstration
        demo_file = os.path.expanduser("~/Downloads/sample_palette.json")
        self._process_import_file(demo_file)

    def _process_import_file(self, file_path: str) -> None:
        """Process the imported file."""

        def import_operation() -> Dict[str, Any]:
            """
            Import a palette file.

            Returns:
                Dictionary containing the imported palette data

            Raises:
                ValueError: If the import fails
            """
            # Import the file and get result directly
            success, result = import_palette_from_file(file_path)

            if not success:
                # If the import failed, raise an exception to trigger error handling
                raise ValueError(str(result))

            # At this point, result must be a Dict because success is True
            assert isinstance(result, dict), "Expected dictionary result when success is True"
            return result  # This is the palette dictionary

        # Use the try_operation method from BaseScreen
        success, palette, _error_info = self.try_operation(
            operation=import_operation,
            error_message=f"Failed to import palette from {file_path}",
            success_message=f"Successfully imported palette from {file_path}",
            context={"file_path": file_path},
        )

        if success:
            # Display the palette preview
            self._display_palette_preview(cast(Dict[str, Any], palette))
            self.show_status(f"Imported palette: {palette.get('name', 'Unnamed')}", "success")

    def _process_clipboard_content(self, content: str) -> None:
        """Process clipboard content to extract colors."""

        def process_operation() -> Dict[str, Any]:
            """
            Process clipboard content to extract colors.

            Returns:
                Dictionary containing the extracted palette data
            """
            # Extract colors from the content
            import re

            # Look for hex colors
            hex_pattern = r"#[0-9A-Fa-f]{3,8}\b"
            colors = [match.group(0) for match in re.finditer(hex_pattern, content)]

            # If no colors found, raise exception
            if not colors:
                raise ValueError("No valid colors found in clipboard content")

            # Create a palette dictionary
            import uuid
            from datetime import datetime

            palette = {
                "id": str(uuid.uuid4()),
                "name": "Clipboard Import",
                "colors": colors,
                "createdAt": datetime.now().isoformat(),
            }

            return palette

        # Use the try_operation method from BaseScreen
        success, palette, _error_info = self.try_operation(
            operation=process_operation,
            error_message="Failed to process clipboard content",
            success_message="Colors extracted from clipboard",
            context={"content_preview": content[:50] + "..." if len(content) > 50 else content},
        )

        if success and palette:
            # Display the palette preview
            self._display_palette_preview(palette)

    def action_add_to_palettes(self) -> None:
        """Add the imported palette to the user's palettes."""

        def add_operation() -> Dict[str, Any]:
            """
            Add the imported palette to the user's palettes.

            Returns:
                Dictionary containing the added palette data
            """
            if self._imported_palette is None:
                raise ValueError("No palette to add")

            # Send a message to the app with the imported palette
            self.post_message(PaletteImportedMessage(self._imported_palette))
            return self._imported_palette

        # Use the try_operation method from BaseScreen
        success, _palette, _error_info = self.try_operation(
            operation=add_operation,
            error_message="Failed to add palette to collection",
            success_message="Palette added to your collection!",
            context={
                "palette_name": self._imported_palette.get("name", "Unknown") if self._imported_palette else "Unknown"
            },
        )

        if success:
            # Return to the main screen after a delay
            self.app.switch_screen("main")

    def _display_palette_preview(self, palette: Dict[str, Any]) -> None:
        """
        Display the palette preview.

        Args:
            palette: Dictionary containing palette data with 'name' and 'colors' keys
        """
        # Store the imported palette for later use
        self._imported_palette = palette

        # Update the palette name display
        palette_name = palette.get("name", "Unnamed Palette")
        palette_name_widget = self.query_one("#palette-name", Static)
        palette_name_widget.update(palette_name)

        # Find the palette preview container
        preview_container = self.query_one("#palette-preview", Container)

        # Clear existing swatches
        for child in list(preview_container.children):
            if isinstance(child, Static) and "color-swatch" in child.classes:
                child.remove()

        # Add swatches for each color in the palette
        colors = palette.get("colors", [])
        for color in colors:
            # Create a swatch for each color
            swatch = Static(color, classes="color-swatch")
            swatch.styles.background = color

            # Add to preview container
            preview_container.mount(swatch)

        # Show the palette information
        color_count = len(colors)
        info_widget = self.query_one("#palette-info", Static)
        info_widget.update(f"Contains {color_count} colors")

    def action_import_clipboard(self) -> None:
        """Import colors from the clipboard."""
        # In a real implementation, we'd access the system clipboard
        # For demonstration, use a sample content
        sample_content = "#FF5733 #33FF57 #5733FF #F3F3F3"
        self._process_clipboard_content(sample_content)
        self.show_status("Clipboard content processed", "info")
