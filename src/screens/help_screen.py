"""
Enhanced help screen for the Palette Milker application.

This screen displays all available keyboard shortcuts and controls,
organized by category with improved visual layout and comprehensive coverage.
"""

from typing import Any
from typing import ClassVar
from typing import List
from typing import Tuple
from typing import Union

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.containers import Grid
from textual.containers import ScrollableContainer
from textual.screen import ModalScreen
from textual.widgets import Button
from textual.widgets import Rule
from textual.widgets import Static


class HelpScreen(ModalScreen):
    """
    Enhanced modal screen displaying all keyboard shortcuts and controls.

    This screen organizes shortcuts by category with improved visual
    hierarchy and navigation instructions.
    """

    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Keep these simple since this is a modal screen
        # that overlays other screens
        Binding("escape", "dismiss", "Close"),
        Binding("q", "dismiss", "Close", show=False),
        Binding("enter", "dismiss", "Close", show=False),
    ]

    DEFAULT_CSS = """
    HelpScreen {
        align: center middle;
    }

    #help-container {
        width: 90%;
        height: 90%;
        background: $surface;
        border: round $primary;
        padding: 1 2;
    }

    #help-title {
        text-align: center;
        text-style: bold;
        background: $primary;
        color: $text;
        padding: 1;
        margin-bottom: 1;
    }

    #help-content {
        height: 1fr;
        overflow: auto;
    }

    .shortcut-category {
        margin-top: 1;
        text-style: bold;
        color: $accent;
        background: $panel;
        width: 100%;
        text-align: center;
        padding: 0 1;
    }

    .shortcut-description {
        margin-top: 1;
        text-style: italic;
        color: $text-muted;
        padding-left: 2;
    }

    .shortcut-grid {
        width: 100%;
        grid-size: 2;
        grid-columns: 20 1fr;
        padding: 0 1;
        margin-bottom: 1;
    }

    .shortcut-grid-3col {
        width: 100%;
        grid-size: 3;
        grid-columns: 20 20 1fr;
        padding: 0 1;
        margin-bottom: 1;
    }

    .shortcut-key {
        width: 100%;
        padding-right: 1;
        color: $secondary;
    }

    .shortcut-alt-key {
        width: 100%;
        color: $secondary-darken-1;
    }

    .shortcut-label {
        color: $text;
    }

    .key-binding {
        background: $boost;
        color: $text;
        border: tall $primary;
        padding: 0 1;
        text-align: center;
    }

    #close-button {
        margin-top: 1;
        width: 20;
        align-horizontal: center;
    }

    .section-rule {
        margin: 1 0;
        color: $primary-darken-1;
    }

    .subsection-title {
        color: $secondary;
        text-style: bold;
        margin-top: 0;
        margin-left: 2;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the help screen with comprehensive keyboard shortcuts."""
        with Container(id="help-container"):
            yield Static("PALETTE MILKER - KEYBOARD SHORTCUTS & NAVIGATION", id="help-title")

            with ScrollableContainer(id="help-content"):
                # Introduction
                yield Static(
                    "Use the following keyboard shortcuts to navigate and control the application.",
                    classes="shortcut-description",
                )

                # Application Controls
                yield Static("Application Controls", classes="shortcut-category")
                with Grid(classes="shortcut-grid"):
                    yield Static("Ctrl+Q", classes="shortcut-key")
                    yield Static("Quit the application", classes="shortcut-label")

                    yield Static("F1", classes="shortcut-key")
                    yield Static("Show this help screen", classes="shortcut-label")

                    yield Static("D", classes="shortcut-key")
                    yield Static("Toggle dark/light mode", classes="shortcut-label")

                yield Rule(classes="section-rule")

                # Navigation Controls
                yield Static("Navigation", classes="shortcut-category")
                yield Static(
                    "Use these shortcuts to navigate between screens and UI elements.", classes="shortcut-description"
                )

                # Screen Navigation
                yield Static("Screen Navigation", classes="subsection-title")
                with Grid(classes="shortcut-grid"):
                    yield Static("1", classes="shortcut-key")
                    yield Static("Switch to palette view", classes="shortcut-label")

                    yield Static("2", classes="shortcut-key")
                    yield Static("Switch to color picker", classes="shortcut-label")

                    yield Static("3", classes="shortcut-key")
                    yield Static("Switch to export options", classes="shortcut-label")

                    yield Static("Escape", classes="shortcut-key")
                    yield Static("Go back/close dialog", classes="shortcut-label")

                # Tab Navigation
                yield Static("Tab Navigation", classes="subsection-title")
                with Grid(classes="shortcut-grid"):
                    yield Static("Tab", classes="shortcut-key")
                    yield Static("Move to next interactive element", classes="shortcut-label")

                    yield Static("Shift+Tab", classes="shortcut-key")
                    yield Static("Move to previous interactive element", classes="shortcut-label")

                    yield Static("Enter", classes="shortcut-key")
                    yield Static("Activate selected button/control", classes="shortcut-label")

                    yield Static("Space", classes="shortcut-key")
                    yield Static("Toggle selected checkbox/button", classes="shortcut-label")

                yield Rule(classes="section-rule")

                # Palette Management
                yield Static("Palette Management", classes="shortcut-category")
                with Grid(classes="shortcut-grid"):
                    yield Static("Ctrl+S", classes="shortcut-key")
                    yield Static("Save all palettes", classes="shortcut-label")

                    yield Static("Ctrl+N", classes="shortcut-key")
                    yield Static("Create new palette", classes="shortcut-label")

                    yield Static("Ctrl+O", classes="shortcut-key")
                    yield Static("Import palette", classes="shortcut-label")

                    yield Static("Ctrl+E", classes="shortcut-key")
                    yield Static("Export palette", classes="shortcut-label")

                    yield Static("R", classes="shortcut-key")
                    yield Static("Rename current palette", classes="shortcut-label")

                    yield Static("C", classes="shortcut-key")
                    yield Static("Copy/duplicate palette", classes="shortcut-label")

                yield Rule(classes="section-rule")

                # Color Manipulation
                yield Static("Color Manipulation", classes="shortcut-category")
                yield Static(
                    "Use these shortcuts to manage colors in the current palette.", classes="shortcut-description"
                )

                # Basic Color Operations
                with Grid(classes="shortcut-grid"):
                    yield Static("A", classes="shortcut-key")
                    yield Static("Add new color to palette", classes="shortcut-label")

                    yield Static("E", classes="shortcut-key")
                    yield Static("Edit selected color", classes="shortcut-label")

                    yield Static("D", classes="shortcut-key")
                    yield Static("Delete selected color", classes="shortcut-label")

                    yield Static("Ctrl+C", classes="shortcut-key")
                    yield Static("Copy color to clipboard", classes="shortcut-label")

                # Color Picker Shortcuts
                yield Static("Color Picker Controls", classes="subsection-title")
                with Grid(classes="shortcut-grid-3col"):
                    # Arrow Key Controls
                    yield Static("↑ (Up)", classes="shortcut-key")
                    yield Static("—", classes="shortcut-alt-key")
                    yield Static("Increase hue", classes="shortcut-label")

                    yield Static("↓ (Down)", classes="shortcut-key")
                    yield Static("—", classes="shortcut-alt-key")
                    yield Static("Decrease hue", classes="shortcut-label")

                    yield Static("← (Left)", classes="shortcut-key")
                    yield Static("—", classes="shortcut-alt-key")
                    yield Static("Decrease saturation", classes="shortcut-label")

                    yield Static("→ (Right)", classes="shortcut-key")
                    yield Static("—", classes="shortcut-alt-key")
                    yield Static("Increase saturation", classes="shortcut-label")

                    yield Static("Shift+↑", classes="shortcut-key")
                    yield Static("—", classes="shortcut-alt-key")
                    yield Static("Increase lightness", classes="shortcut-label")

                    yield Static("Shift+↓", classes="shortcut-key")
                    yield Static("—", classes="shortcut-alt-key")
                    yield Static("Decrease lightness", classes="shortcut-label")

                    # Format and Random
                    yield Static("F", classes="shortcut-key")
                    yield Static("H", classes="shortcut-alt-key")
                    yield Static("Toggle color format (HEX/RGB/HSL)", classes="shortcut-label")

                    yield Static("R", classes="shortcut-key")
                    yield Static("—", classes="shortcut-alt-key")
                    yield Static("Generate random color", classes="shortcut-label")

                yield Rule(classes="section-rule")

                # History
                yield Static("Edit History", classes="shortcut-category")
                with Grid(classes="shortcut-grid"):
                    yield Static("Ctrl+Z", classes="shortcut-key")
                    yield Static("Undo last action", classes="shortcut-label")

                    yield Static("Ctrl+Shift+Z", classes="shortcut-key")
                    yield Static("Redo last undone action", classes="shortcut-label")

                # Mouse Controls
                yield Static("Mouse Controls", classes="shortcut-category")
                with Grid(classes="shortcut-grid"):
                    yield Static("Left Click", classes="shortcut-key")
                    yield Static("Select item/activate control", classes="shortcut-label")

                    yield Static("Double Click", classes="shortcut-key")
                    yield Static("Edit item (palette name, color)", classes="shortcut-label")

                    yield Static("Right Click", classes="shortcut-key")
                    yield Static("Show context menu for item", classes="shortcut-label")

                # Display Options
                yield Static("Display Options", classes="shortcut-category")
                with Grid(classes="shortcut-grid"):
                    yield Static("H / F", classes="shortcut-key")
                    yield Static("Toggle color format display", classes="shortcut-label")

                    yield Static("Space", classes="shortcut-key")
                    yield Static("Toggle color details panel", classes="shortcut-label")

                yield Button("Close", id="close-button", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "close-button":
            self.dismiss()

    def action_dismiss(self, result: Any = None) -> None:
        """Dismiss the help screen."""
        self.dismiss(result)
