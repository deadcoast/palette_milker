# milky_color_suite/main.py
from pathlib import Path
from typing import Any
from typing import ClassVar
from typing import List
from typing import Tuple
from typing import Union
from typing import cast

from textual.app import App
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import Static

from .models.application_state import ApplicationState
from .models.application_state import StateChanged
from .models.application_state import ThemeChanged
from .models.application_state import ViewMode
from .models.palette_model import Palette
from .models.palette_model import PaletteAdded
from .models.palette_model import PaletteColorUpdated
from .models.palette_model import PaletteRemoved
from .models.palette_model import PaletteUpdated
from .utils.error_handler import handle_error
from .utils.error_handler import logger
from .widgets.color.color_wheel import ColorWheel
from .widgets.input_handler import InputHandler
from .widgets.palette.palette_management import PaletteManagement


"""
Palette Milker - A Textual TUI Color Palette Manager

This application allows users to create, edit, and manage color palettes
with an ASCII-art styled interface.
"""


# Define data paths
DATA_DIR = Path(__file__).parent / "data"
PALETTES_FILE = DATA_DIR / "palettes.json"


class PaletteMilkerApp(App):
    """The main Palette Milker application."""

    TITLE = "Palette Milker"
    CSS_PATH = "app.tcss"

    # Define application-wide key bindings
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # === Application Controls ===
        Binding("ctrl+q", "quit", "Quit", priority=True),
        Binding("f1", "toggle_help", "Help"),
        Binding("d", "toggle_dark", "Dark mode"),
        # === Navigation ===
        # Focus control
        Binding("tab", "focus_next", "Next field", show=False),
        Binding("shift+tab", "focus_previous", "Previous field", show=False),
        # Screen navigation
        Binding("1", "view_palette", "Palette view"),
        Binding("2", "view_color_picker", "Color picker"),
        Binding("3", "view_export", "Export options"),
        Binding("escape", "pop_screen", "Back", show=False, priority=True),
        # === Palette Management ===
        Binding("ctrl+s", "save_palette", "Save palette"),
        Binding("ctrl+n", "new_palette", "New palette"),
        Binding("ctrl+o", "import_palette", "Import palette"),
        Binding("ctrl+e", "export_palette", "Export palette"),
        Binding("r", "rename_palette", "Rename"),
        Binding("c", "copy_palette", "Copy"),
        # === Color Operations ===
        Binding("a", "add_color", "Add color"),
        Binding("d", "delete_color", "Delete color"),
        Binding("e", "edit_color", "Edit color"),
        Binding("ctrl+c", "copy_color", "Copy color", show=False),
        # === Arrow Key Color Adjustment ===
        Binding("up", "color_adjust(hue, 1)", "Increase hue", show=False),
        Binding("down", "color_adjust(hue, -1)", "Decrease hue", show=False),
        Binding("left", "color_adjust(saturation, -1)", "Decrease saturation", show=False),
        Binding("right", "color_adjust(saturation, 1)", "Increase saturation", show=False),
        Binding("shift+up", "color_adjust(lightness, 1)", "Increase lightness", show=False),
        Binding("shift+down", "color_adjust(lightness, -1)", "Decrease lightness", show=False),
        # === History Controls ===
        Binding("ctrl+z", "undo", "Undo"),
        Binding("ctrl+shift+z", "redo", "Redo"),
        # === Display Options ===
        Binding("h", "toggle_hex_display", "Hex values"),
        Binding("space", "toggle_color_details", "Show details"),
    ]

    def __init__(self):
        """Initialize the application."""
        super().__init__()

        # Initialize the app logger
        self.app_logger = logger

        # Set up application-level error handling
        self._setup_error_handling()

        # Create application state manager
        self.app_state = ApplicationState(self)

    def _setup_error_handling(self):
        """Set up centralized error handling."""
        # App logger is already initialized in __init__
        pass

    def compose(self) -> ComposeResult:
        """Compose the main application UI."""
        # Header and Footer
        yield Header()
        yield Footer()

        # Main layout
        with Container(id="main-container"):
            # Left sidebar - Tree browser
            with Container(id="left-sidebar"):
                yield Static("╠───────────────╦", classes="sidebar-header-top")
                yield Static("│ (⊕) Browse    │", classes="sidebar-header")
                yield Static("╠───────────────╝", classes="sidebar-header-bottom")

                # Palettes section
                yield Static("│ ▼ Palettes    │", classes="browse-section-header")
                for palette in self.app_state.palette_collection.palettes:
                    yield Static(
                        f"│    {palette.name.ljust(11)}│", id=f"browse-{palette.palette_id}", classes="browse-item"
                    )
                yield Static("│               │", classes="browse-spacer")

                # Arrays section
                yield Static("│  ▼ Arrays     │", classes="browse-section-header")
                yield Static("│     UTTERS    │", classes="browse-item")
                yield Static("│     RGB       │", classes="browse-item")
                yield Static("│     HEX       │", classes="browse-item")
                yield Static("│               │", classes="browse-spacer")

            # Main content area
            with Container(id="main-content"):
                # Color wheel - use id as that's what ColorWheel expects
                yield ColorWheel(title="COLOR WHEEL", id="color-wheel")

                # Palette management
                active_palette = self.app_state.get_active_palette()
                if active_palette:
                    # Access attributes through the proper methods
                    active_color_index = 0
                    # Use type casting to access these attributes if needed
                    palette_model = cast(Any, self.app_state.palette_model)
                    if hasattr(palette_model, "active_color_index"):
                        active_color_index = palette_model.active_color_index

                    yield PaletteManagement(
                        palette_id=active_palette.palette_id,
                        palette_name=active_palette.name,
                        colors=active_palette.hex_colors,
                        active_color_index=active_color_index,
                        id="palette-management",
                    )
                else:
                    # Fallback if no active palette
                    yield PaletteManagement(id="palette-management")

    def on_mount(self) -> None:
        """Handle application mount event."""
        self.title = "Palette Milker - ASCII TUI Color Palette Manager"

        # Set initial theme based on app state
        self.dark = self.app_state.is_dark_mode

        # Make sure PaletteManagement has the current palette data
        self._update_palette_ui()

        # Capture initial state for history
        initial_state = self.app_state.capture_current_state()
        self.app_state.add_to_history(initial_state)

    # Handle state change messages
    def on_state_changed(self, message: StateChanged) -> None:
        """
        Handle state change messages from the app state manager.

        Args:
            message: The StateChanged message
        """
        # Handle different types of state changes
        key = message.key
        value = message.value

        # Update UI based on changed state
        if key == "is_dark_mode":
            self.dark = value
        elif key == "current_view":
            # Handle view changes
            if value == ViewMode.PALETTE:
                self.action_view_palette()
            elif value == ViewMode.COLOR_PICKER:
                self.action_view_color_picker()
            elif value == ViewMode.EXPORT:
                self.action_view_export()
            # Add other view modes as needed
        elif key in ["show_hex_values", "show_color_details"]:
            # These may require UI updates
            self._update_palette_ui()

    def on_theme_changed(self, message: ThemeChanged) -> None:
        """
        Handle theme change messages.

        Args:
            message: The ThemeChanged message
        """
        # Set the theme based on the message
        self.dark = message.is_dark

    def action_toggle_dark(self) -> None:
        """Toggle between light and dark mode."""
        self.app_state.toggle_dark_mode()

    def action_save_palette(self) -> None:
        """Save the current palette."""
        try:
            # Save the current palette collection using app state
            success = self.app_state.save_palettes()

            if success:
                self.notify("Palettes saved successfully!", severity="information")
            else:
                self.notify("Failed to save palettes", severity="error")

        except Exception as e:
            handle_error(
                message=f"Failed to save palettes: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "save_palette"},
            )

    def action_new_palette(self) -> None:
        """Create a new palette."""
        try:
            # Generate a new name
            new_name = f"New Palette {len(self.app_state.palette_collection)}"

            # Create a new palette with default colors
            # Create a list of hex color strings (standardized format)
            default_colors = ["#FFFFFF"] * 8

            self._extracted_from__extracted_from_action_copy_palette__13(
                new_name, default_colors, "Created new palette: "
            )
            # Save state for history
            state = self.app_state.capture_current_state()
            self.app_state.add_to_history(state)

        except Exception as e:
            handle_error(
                message=f"Failed to create new palette: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "new_palette"},
            )

    def action_import_palette(self) -> None:
        """Import a palette from a file."""
        from .screens.import_screen import ImportScreen

        self.push_screen(ImportScreen())

    def action_export_palette(self) -> None:
        """Export the palette in selected format."""
        from .screens.export_screen import ExportScreen

        # Create and switch to the export screen
        self.switch_screen(ExportScreen())

    def action_add_color(self) -> None:
        """Add a new color to the palette."""
        active_palette = self.app_state.get_active_palette()
        if not active_palette:
            self.notify("No active palette", severity="warning")
            return

        try:
            # Get the color from the color wheel
            color_wheel = self.query_one("#color-wheel", ColorWheel)
            current_color = color_wheel.selected_color

            # Add the color to the active palette
            active_palette.add_color(current_color)

            # Notify success
            self.notify(f"Added color {current_color}", severity="information")

            # Update the UI
            self._update_palette_ui()

        except Exception as e:
            handle_error(
                message=f"Failed to add color: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "add_color"},
            )

    def action_delete_color(self) -> None:
        """Delete the selected color."""
        active_palette = self.app_state.get_active_palette()
        if not active_palette:
            self.notify("No active palette", severity="warning")
            return

        try:
            # Check if there's at least 1 color left
            if len(active_palette) <= 1:
                self.notify("Cannot remove the last color", severity="warning")
                return

            # Use type casting to access active_color_index
            from typing import Any
            from typing import cast

            palette_model = cast(Any, self.app_state.palette_model)

            # Remove the active color
            index = palette_model.active_color_index
            removed_color = active_palette.remove_color(index)

            if removed_color:
                # Adjust the active color index if needed
                if index >= len(active_palette):
                    self.app_state.set_active_color_index(len(active_palette) - 1)

                # Notify success
                self.notify(f"Removed color {removed_color.hex}", severity="information")

                # Update the UI
                self._update_palette_ui()
            else:
                self.notify("Failed to remove color", severity="error")

        except Exception as e:
            handle_error(
                message=f"Failed to delete color: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "delete_color"},
            )

    def action_edit_color(self) -> None:
        """Edit the selected color."""
        if not self.app_state.get_active_palette():
            self.notify("No active palette", severity="warning")
            return

        try:
            # Get the color from the color wheel
            color_wheel = self.query_one("#color-wheel", ColorWheel)
            current_color = color_wheel.selected_color

            # Update the active color
            self.app_state.update_active_color(current_color)

            # Notify success
            self.notify(f"Updated color to {current_color}", severity="information")

            # Update the UI
            self._update_palette_ui()

        except Exception as e:
            handle_error(
                message=f"Failed to edit color: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "edit_color"},
            )

    def action_view_palette(self) -> None:
        """Switch to palette view."""
        self.switch_screen("main")

    def action_view_color_picker(self) -> None:
        """Switch to color picker view."""
        from .screens.color_picker import ColorPickerScreen

        # Create and switch to the color picker screen
        self.switch_screen(ColorPickerScreen())

    def action_view_export(self) -> None:
        """Switch to export options view."""
        from .screens.export_screen import ExportScreen

        # Create and switch to the export screen
        self.switch_screen(ExportScreen())

    def action_rename_palette(self) -> None:
        """Rename the current palette."""
        if not self.app_state.get_active_palette():
            self.notify("No active palette", severity="warning")
            return

        try:
            from .screens.rename_screen import RenameScreen

            # Create a rename screen with the current palette name
            rename_screen = RenameScreen(self.app_state.get_active_palette().name)
            self.push_screen(rename_screen)

        except Exception as e:
            handle_error(
                message=f"Failed to open rename dialog: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "rename_palette"},
            )

    def action_copy_palette(self) -> None:
        """Create a copy of the current palette."""
        active_palette = self.app_state.get_active_palette()
        if not active_palette:
            self.notify("No active palette", severity="warning")
            return

        try:
            self._extracted_from_action_copy_palette_(active_palette)
        except Exception as e:
            handle_error(
                message=f"Failed to copy palette: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "copy_palette"},
            )

    # TODO Rename this here and in `action_copy_palette`
    def _extracted_from_action_copy_palette_(self, active_palette):
        # Create a new name with "Copy" suffix
        palette_name = active_palette.name if hasattr(active_palette, "name") else "Palette"
        new_name = f"{palette_name} (Copy)"

        palette_colors = list(active_palette.colors)
        self._extracted_from__extracted_from_action_copy_palette__13(new_name, palette_colors, "Created copy: ")

    # TODO Rename this here and in `action_new_palette` and `_extracted_from_action_copy_palette_`
    def _extracted_from__extracted_from_action_copy_palette__13(self, new_name, arg1, arg2):
        from typing import Any
        from typing import cast

        palette = self.app_state.palette_model.add_palette(name=new_name, colors=cast(Any, arg1))
        self.app_state.set_active_palette(palette.palette_id)
        self.notify(f"{arg2}{new_name}", severity="information")
        self._update_palette_ui()

    def action_undo(self) -> None:
        """Undo the last action."""
        # This would be connected to an UndoManager in a future implementation
        self.notify("Undo not implemented yet", severity="warning")

    def action_redo(self) -> None:
        """Redo the last undone action."""
        # This would be connected to an UndoManager in a future implementation
        self.notify("Redo not implemented yet", severity="warning")

    def action_toggle_hex_display(self) -> None:
        """Toggle hex value display."""
        self.app_state.toggle_hex_display()

    def action_toggle_color_details(self) -> None:
        """Toggle color details display."""
        self.app_state.toggle_color_details()

    def action_toggle_help(self) -> None:
        """Toggle help screen."""
        self.app_state.toggle_help()

        # If help is now visible, show help screen
        if self.app_state.is_help_visible:
            from .screens.help_screen import HelpScreen

            self.push_screen(HelpScreen())

    def action_copy_color(self) -> None:
        """Copy the current color to clipboard."""
        try:
            # Get the current color from the color wheel
            color_wheel = self.query_one("#color-wheel", ColorWheel)
            color_hex = color_wheel.selected_color

            # In a real implementation, this would use the system clipboard
            # For now, just notify the user
            self.notify(f"Copied {color_hex} to clipboard", severity="information")
        except Exception as e:
            self.app_logger.error(f"Error copying color: {e}")
            self.notify("Failed to copy color", severity="error")

    def action_color_adjust(self, property_name: str, direction: int) -> None:
        """
        Adjust a color property by the specified direction.

        Args:
            property_name: The property to adjust (hue, saturation, lightness)
            direction: The direction to adjust (positive or negative)
        """
        try:
            # Get the current color from the color wheel
            from .widgets.color.color_wheel import ColorWheel

            color_wheel = self.query_one("#color-wheel", ColorWheel)

            # Get current color
            current_color = color_wheel.selected_color

            # Import adjustment utilities
            from .models.color_model import Color
            from .utils.color_adjustment import adjust_hue
            from .utils.color_adjustment import adjust_lightness
            from .utils.color_adjustment import adjust_saturation

            saturation_step = 5  # 5% change in saturation
            lightness_step = 5  # 5% change in lightness

            # Apply the adjustment based on property name
            if property_name == "hue":
                amount = direction * 10
                new_color = adjust_hue(Color(current_color), amount)
                color_wheel.selected_color = new_color.hex
            elif property_name == "lightness":
                amount = direction * lightness_step
                new_color = adjust_lightness(Color(current_color), amount)
                color_wheel.selected_color = new_color.hex
            elif property_name == "saturation":
                amount = direction * saturation_step
                new_color = adjust_saturation(Color(current_color), amount)
                color_wheel.selected_color = new_color.hex
            else:
                self.notify(f"Unknown color property: {property_name}", severity="error")

            # Update the active color in the palette if in edit mode
            self.action_edit_color()

        except Exception as e:
            self.app_logger.error(f"Error adjusting color: {e}")
            self.notify(f"Failed to adjust {property_name}", severity="error")

    def on_input_handler_key_action_requested(self, message: InputHandler.KeyActionRequested) -> None:
        """Handle key actions requested by the input handler.

        Args:
            message: The message containing the key action request
        """
        # Find the binding that matches this key
        for binding in self.BINDINGS:
            if isinstance(binding, Binding):
                # Check if this binding matches the key
                if binding.key == message.key:
                    # Extract action name and call it
                    action_name = binding.action
                    # Handle any parameters if action contains parentheses
                    if "(" in action_name:
                        # Extract action name and parameters from something like "change_color('red')"
                        base_action, params_str = action_name.split("(", 1)
                        params_str = params_str.rstrip(")")
                        # This is a simple approach - a more robust implementation would parse parameters properly
                        # For now, we'll handle simple string params
                        if "'" in params_str or '"' in params_str:
                            # It's a string parameter
                            param = params_str.strip("'\"")
                            method = getattr(self, f"action_{base_action}", None)
                            if method and callable(method):
                                method(param)
                    else:
                        # Simple action with no parameters
                        method = getattr(self, f"action_{action_name}", None)
                        if method and callable(method):
                            method()
                    return
            elif isinstance(binding, tuple) and len(binding) >= 2:
                # Handle tuple format bindings
                if binding[0] == message.key:
                    action_name = binding[1]
                    method = getattr(self, f"action_{action_name}", None)
                    if method and callable(method):
                        method()
                    return

        # If we get here, no binding was found - log for debugging
        self.app_logger.debug(f"No binding found for key: {message.key}")

    def on_input_handler_palette_action_requested(self, message: InputHandler.PaletteActionRequested) -> None:
        """Handle palette action requests from the input handler.

        Args:
            message: The message containing the palette action request
        """
        # Extract the action name
        action_name = message.action

        # Try to find the corresponding action method
        method_name = f"action_{action_name}"
        method = getattr(self, method_name, None)

        # If the method exists, call it with any provided data
        if method and callable(method):
            try:
                if message.data:
                    method(**message.data)
                else:
                    method()
            except Exception as e:
                # Log any errors that occur during execution
                self.app_logger.error(f"Error executing {method_name}: {e!s}")
                self.notify(f"Error: {e!s}", severity="error")
        else:
            # Log if the action doesn't exist
            self.app_logger.warning(f"No action method found for: {action_name}")

    def on_palette_imported_message(self, message):
        """Handle a palette imported message."""
        try:
            # Extract the palette data
            palette_data = message.palette

            # Create a new palette from the data
            palette = Palette(name=palette_data["name"], colors=palette_data["colors"])

            # Add to collection
            self.app_state.palette_collection.add_palette(palette)

            # Set as active
            self.app_state.set_active_palette(palette.palette_id)

            # Notify the user
            self.notify(f"Imported palette: {palette.name}", severity="information")

            # Update UI
            self._update_palette_ui()

        except Exception as e:
            handle_error(
                message=f"Failed to import palette: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "import_palette"},
            )

    def on_rename_submitted(self, message):
        """Handle rename submission."""
        active_palette = self.app_state.get_active_palette()
        if not active_palette:
            return

        try:
            # Rename the active palette
            new_name = message.name
            active_palette.name = new_name  # Direct attribute update

            # Notify success
            self.notify(f"Renamed palette to: {new_name}", severity="information")

            # Update the UI
            self._update_palette_ui()

        except Exception as e:
            handle_error(
                message=f"Failed to rename palette: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "rename_palette"},
            )

    def on_palette_management_color_selected(self, message):
        """Handle color selection from the palette management widget."""
        try:
            # Update the active color index in the model
            self.app_state.set_active_color_index(message.index)

            # Get the selected color
            active_palette = self.app_state.get_active_palette()
            if active_palette:
                selected_color = active_palette.get_color(message.index)
                if selected_color:
                    # Update the color wheel
                    color_wheel = self.query_one("#color-wheel", ColorWheel)
                    color_wheel.selected_color = selected_color.hex

        except Exception as e:
            self.app_logger.error(f"Error handling color selection: {e}")

    # Handle model message updates
    def on_palette_updated(self, message: PaletteUpdated) -> None:
        """Handle palette updated message.

        Args:
            message: The PaletteUpdated message
        """
        self._update_palette_ui()

    def on_palette_added(self, message: PaletteAdded) -> None:
        """Handle palette added message.

        Args:
            message: The PaletteAdded message
        """
        self._update_palette_ui()

    def on_palette_removed(self, message: PaletteRemoved) -> None:
        """Handle palette removed message.

        Args:
            message: The PaletteRemoved message
        """
        self._update_palette_ui()

    def on_palette_color_updated(self, message: PaletteColorUpdated) -> None:
        """Handle palette color updated message.

        Args:
            message: The PaletteColorUpdated message
        """
        self._update_palette_ui()

    def _update_palette_ui(self):
        """Update the palette management UI."""
        try:
            # Get the management widget
            management = self.query_one("#palette-management", PaletteManagement)

            # Check if we have an active palette
            active_palette = self.app_state.get_active_palette()
            if active_palette:
                # Get the active color index
                active_color_index = 0
                palette_model = cast(Any, self.app_state.palette_model)
                if hasattr(palette_model, "active_color_index"):
                    active_color_index = palette_model.active_color_index

                # Update management widget with current palette data
                management.update_palette(
                    palette_id=active_palette.palette_id,
                    palette_name=active_palette.name,
                    colors=active_palette.hex_colors,
                    active_color_index=active_color_index,
                )

            # Update display settings - check if these attributes exist first
            # Cast to Any to avoid type checking issues
            management_any = cast(Any, management)
            if hasattr(management_any, "show_hex"):
                management_any.show_hex = self.app_state.show_hex_values

            if hasattr(management_any, "show_details"):
                management_any.show_details = self.app_state.show_color_details

        except Exception as e:
            handle_error(
                message=f"Failed to update palette UI: {e!s}",
                severity="warning",
                exception=e,
                app=self,
                context={"action": "_update_palette_ui"},
            )

    def on_color_picker_screen_color_selected_message(self, message) -> None:
        """Handle color selection from the enhanced color picker screen.

        Args:
            message: The ColorSelectedMessage containing the selected color
        """
        try:
            # Convert the Textual Color to a string format our palette model can use
            color_hex = message.color.hex

            # Update the active color in the color wheel first
            try:
                color_wheel = self.query_one("#color-wheel", ColorWheel)
                color_wheel.selected_color = color_hex
            except Exception:
                # The color wheel might not be available on all screens
                pass

            # Now call the action to add this color to the palette
            self.action_add_color()

        except Exception as e:
            handle_error(
                message=f"Failed to process color selection: {e!s}",
                severity="error",
                exception=e,
                app=self,
                context={"action": "color_selected"},
            )


if __name__ == "__main__":
    app = PaletteMilkerApp()
    app.run()
