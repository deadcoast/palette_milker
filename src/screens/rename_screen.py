"""
Palette Rename Screen module.

This module provides a screen for renaming palettes.
"""

from typing import ClassVar
from typing import List
from typing import Tuple
from typing import Union

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.containers import Horizontal
from textual.message import Message
from textual.screen import ModalScreen
from textual.widgets import Button
from textual.widgets import Input
from textual.widgets import Static


class RenameScreen(ModalScreen):
    """A modal screen for renaming palettes."""

    # Define screen-specific key bindings
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        Binding("escape", "pop_screen", "Cancel"),
        Binding("enter", "submit", "Submit"),
    ]

    # CSS styles for the dialog
    DEFAULT_CSS = """
    RenameScreen {
        align: center middle;
    }

    #rename-dialog {
        width: 50%;
        height: auto;
        border: thick $accent;
        background: $surface;
        padding: 1 2;
    }

    #rename-title {
        text-align: center;
        width: 100%;
        height: 1;
        margin-bottom: 1;
    }

    #rename-buttons {
        width: 100%;
        height: 3;
        margin-top: 1;
        content-align: center middle;
    }

    Button {
        margin-right: 1;
    }
    """

    class RenameSubmitted(Message):
        """Message sent when a rename is submitted."""

        def __init__(self, name: str) -> None:
            """Initialize the message with the new name.

            Args:
                name: The new name for the palette
            """
            super().__init__()
            self.name = name

    def __init__(self, current_name: str) -> None:
        """Initialize the rename screen.

        Args:
            current_name: The current name of the palette
        """
        super().__init__()
        self.current_name = current_name

    def compose(self) -> ComposeResult:
        """Compose the rename dialog.

        Returns:
            A ComposeResult containing child widgets
        """
        with Container(id="rename-dialog"):
            yield Static("Rename Palette", id="rename-title")

            # Input field with current name
            yield Input(value=self.current_name, placeholder="Enter new palette name", id="rename-input")

            # Button row
            with Horizontal(id="rename-buttons"):
                yield Button("Cancel", variant="error", id="cancel-button")
                yield Button("Rename", variant="primary", id="submit-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events.

        Args:
            event: The button pressed event
        """
        button_id = event.button.id

        if button_id == "cancel-button":
            self.dismiss()  # Close the dialog without submitting
        elif button_id == "submit-button":
            self.action_submit()

    def action_submit(self) -> None:
        """Submit the rename."""
        # Get the input value
        input_widget = self.query_one("#rename-input", Input)
        new_name = input_widget.value

        # Only proceed if we have a name
        if new_name.strip():
            # Send a message with the new name
            self.post_message(self.RenameSubmitted(new_name))
            # Close the dialog
            self.app.pop_screen()
        else:
            # Show an error if the name is empty
            input_widget.add_class("error")
            input_widget.placeholder = "Name cannot be empty"
