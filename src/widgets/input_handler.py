from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from textual.app import App
from textual.app import ComposeResult
from textual.binding import Binding
from textual.events import Key
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Static


class InputHandler(Widget):
    """Widget for handling input events."""

    # Define key bindings for the input handler with proper type annotation
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        Binding("q", "quit", "Quit"),
        Binding("s", "save_palette", "Save palette"),
        Binding("n", "new_palette", "New palette"),
        Binding("o", "open_palette", "Load palette"),
        Binding("a", "add_color", "Add color"),
        Binding("d", "delete_color", "Delete color"),
        Binding("r", "rename_palette", "Rename"),
        Binding("h", "toggle_help", "Help"),
        Binding("1", "view_palette", "Palette view"),
        Binding("2", "view_color_picker", "Color picker"),
        Binding("3", "view_export", "Export options"),
    ]

    class InputRequested(Message):
        """Message sent when input is requested."""

        def __init__(
            self,
            input_type: str,
            prompt: str,
            default_value: str = "",
            validator: Optional[Callable[[str], bool]] = None,
            on_submit: Optional[Callable[[str], None]] = None,
            on_cancel: Optional[Callable[[], None]] = None,
            on_change: Optional[Callable[[str], None]] = None,
            on_validate: Optional[Callable[[str], Tuple[bool, str]]] = None,
        ) -> None:
            """Initialize input requested message.

            Args:
                input_type: Type of input requested
                prompt: Prompt text to display
                default_value: Default value for the input
                validator: Optional validation function
                on_submit: Optional callback for submission
                on_cancel: Optional callback for cancellation
                on_change: Optional callback for value changes
                on_validate: Optional callback for validation
            """
            # Always call super().__init__() with no arguments to follow Textual patterns
            super().__init__()
            # Store message attributes
            self.input_type = input_type
            self.prompt = prompt
            self.default_value = default_value
            self.validator = validator
            self.on_submit = on_submit
            self.on_cancel = on_cancel
            self.on_change = on_change
            self.on_validate = on_validate

    # For widget-specific functionality not covered by global bindings
    class PaletteActionRequested(Message):
        """Message sent for palette-specific actions that need parent handling."""

        def __init__(self, action: str, data: Optional[Dict[str, Any]] = None) -> None:
            """Initialize palette action request.

            Args:
                action: The action requested
                data: Optional data for the action
            """
            # Always call super().__init__() with no arguments to follow Textual patterns
            super().__init__()
            self.action = action
            self.data = data or {}

    class KeyActionRequested(Message):
        """Message sent when a key action is requested that's not handled by bindings."""

        def __init__(self, key: str) -> None:
            """Initialize key action request.

            Args:
                key: The key pressed
            """
            # Always call super().__init__() with no arguments to follow Textual patterns
            super().__init__()
            self.key = key

    def __init__(self, name: Optional[str] = None, widget_id: Optional[str] = None, classes: Optional[str] = None):
        """Initialize the input handler widget."""
        # Ensure a default ID if not provided
        if widget_id is None:
            widget_id = "input_handler"
        super().__init__(name=name, id=widget_id, classes=classes)

    # Define action methods that will be triggered by the bindings
    def action_quit(self) -> None:
        """Handle quit action."""
        self.post_message(self.PaletteActionRequested("quit"))

    def action_save_palette(self) -> None:
        """Handle save palette action."""
        self.post_message(self.PaletteActionRequested("save_palette"))

    def action_new_palette(self) -> None:
        """Handle new palette action."""
        self.post_message(self.PaletteActionRequested("new_palette"))

    def action_open_palette(self) -> None:
        """Handle open palette action."""
        self.post_message(self.PaletteActionRequested("open_palette"))

    def action_add_color(self) -> None:
        """Handle add color action."""
        self.post_message(self.PaletteActionRequested("add_color"))

    def action_delete_color(self) -> None:
        """Handle delete color action."""
        self.post_message(self.PaletteActionRequested("delete_color"))

    def action_rename_palette(self) -> None:
        """Handle rename palette action."""
        self.post_message(self.PaletteActionRequested("rename_palette"))

    def action_toggle_help(self) -> None:
        """Handle toggle help action."""
        self.post_message(self.PaletteActionRequested("toggle_help"))

    def action_view_palette(self) -> None:
        """Handle view palette action."""
        self.post_message(self.PaletteActionRequested("view_palette"))

    def action_view_color_picker(self) -> None:
        """Handle view color picker action."""
        self.post_message(self.PaletteActionRequested("view_color_picker"))

    def action_view_export(self) -> None:
        """Handle view export action."""
        self.post_message(self.PaletteActionRequested("view_export"))

    def on_key(self, event: Key) -> None:
        """Handle key events by using the binding system.

        Args:
            event: The key event
        """
        # Check if the key is handled by our bindings first
        key = event.key

        # Only post KeyActionRequested for keys not handled by BINDINGS
        # This makes direct key handling work as a fallback
        handled = False
        for binding in self.BINDINGS:
            if isinstance(binding, Binding) and binding.key == key:
                handled = True
                break
            elif isinstance(binding, tuple) and binding[0] == key:
                handled = True
                break

        if not handled:
            # Key not in bindings, let the app handle it directly
            self.post_message(self.KeyActionRequested(key))
            event.stop()  # Prevent further propagation


class PaletteApp(App):
    """Example palette app using the proper Textual patterns."""

    # Global keyboard bindings
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Standard app actions
        Binding("q", "quit", "Quit"),
        Binding("ctrl+s", "save_palette", "Save palette"),
        Binding("ctrl+o", "load_palette", "Load palette"),
        # Palette editing actions
        Binding("n", "add_color", "Add color"),
        Binding("d", "delete_color", "Delete color"),
        Binding("r", "rename_palette", "Rename palette"),
        # View controls
        Binding("h", "toggle_help", "Toggle help"),
        Binding("tab", "next_section", "Next section"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Static("Palette App", id="title")
        # Use a consistent ID for the InputHandler
        yield InputHandler(widget_id="input_handler")
        # Add other widgets

    # Action handlers for key bindings
    def action_save_palette(self) -> None:
        """Save the current palette to a file."""
        self.notify("Saving palette...")
        # Implementation for saving the palette

    def action_load_palette(self) -> None:
        """Load a palette from a file."""
        self.notify("Loading palette...")
        # Implementation for loading a palette

    def action_add_color(self) -> None:
        """Add a new color to the palette."""
        self.notify("Adding color...")
        # Implementation for adding a color

    def action_delete_color(self) -> None:
        """Delete the selected color from the palette."""
        self.notify("Deleting color...")
        # Implementation for deleting a color

    def action_rename_palette(self) -> None:
        """Rename the current palette."""
        self.notify("Renaming palette...")
        # Implementation for renaming the palette

    def action_toggle_help(self) -> None:
        """Toggle the help overlay."""
        self.notify("Toggling help...")
        # Implementation for toggling help

    def action_next_section(self) -> None:
        """Move focus to the next section of the interface."""
        self.notify("Moving to next section...")
        # Implementation for moving to the next section

    # Handle messages from InputHandler using consistent naming
    def on_input_handler_palette_action_requested(self, message: InputHandler.PaletteActionRequested) -> None:
        """Handle palette actions requested by the input handler.

        Args:
            message: The PaletteActionRequested message
        """
        # Map palette actions to app actions
        action_map = {
            "save_palette": self.action_save_palette,
            "new_palette": self.action_add_color,  # Example mapping
            "open_palette": self.action_load_palette,
            "add_color": self.action_add_color,
            "delete_color": self.action_delete_color,
            "rename_palette": self.action_rename_palette,
            "toggle_help": self.action_toggle_help,
            "view_palette": self.action_next_section,  # Example mapping
            "view_color_picker": self.action_next_section,  # Example mapping
            "view_export": self.action_next_section,  # Example mapping
        }

        # Execute the mapped action if available
        action = action_map.get(message.action)
        if action:
            action()

    # Renamed from ActionRequested to KeyActionRequested for clarity
    def on_input_handler_key_action_requested(self, message: InputHandler.KeyActionRequested) -> None:
        """Handle key actions requested by the input handler.

        Args:
            message: The KeyActionRequested message
        """
        self.notify(f"Key pressed: {message.key}")
        # Handle the key action if needed


# Example usage:
if __name__ == "__main__":
    app = PaletteApp()
    app.run()
