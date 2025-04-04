"""
Application state manager for the Palette Milker application.

This module provides a central state management system for the application,
ensuring a clean separation between business logic and UI components.
"""

import logging
from enum import Enum
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from textual.message import Message

from .color_model import Color
from .palette_model import Palette
from .palette_model import PaletteCollection
from .palette_model import PaletteModel


# Define message types for state changes
class StateChanged(Message):
    """Base message for state changes."""

    def __init__(self, key: str, value: Any) -> None:
        """
        Initialize with the key and value that changed.

        Args:
            key: The name of the state property that changed
            value: The new value of the property
        """
        self.key = key
        self.value = value
        super().__init__()


class ThemeChanged(Message):
    """Message sent when the application theme changes."""

    def __init__(self, is_dark: bool) -> None:
        """
        Initialize with the new theme setting.

        Args:
            is_dark: Whether dark mode is enabled
        """
        self.is_dark = is_dark
        super().__init__()


class ViewMode(Enum):
    """Different view modes for the application."""

    PALETTE = "palette"
    COLOR_PICKER = "color_picker"
    EXPORT = "export"
    PALETTE_ORGANIZATION = "palette_organization"
    ACCESSIBILITY = "accessibility"


class ApplicationState:
    """
    Central state manager for the Palette Milker application.

    This class manages application-wide state, providing a clean
    separation between business logic and UI components.
    """

    def __init__(self, app: Any = None) -> None:
        """
        Initialize the application state.

        Args:
            app: Optional reference to the main application
        """
        self.app = app
        self.logger = logging.getLogger("palette_milker.app_state")

        # Initialize state properties
        self._is_dark_mode = True
        self._current_view = ViewMode.PALETTE
        self._show_hex_values = True
        self._show_color_details = False
        self._is_help_visible = False

        # History state for undo/redo
        self._history: List[Dict[str, Any]] = []
        self._history_index = -1

        # Initialize palette model
        self._initialize_palette_model()

    def _initialize_palette_model(self) -> None:
        """Initialize the palette model with default data."""
        # Create a default palette collection
        self.palette_collection = self._create_default_palette_collection()

        # Create palette model
        self.palette_model = PaletteModel(self.palette_collection)

        # Bind the model to this state manager for message handling
        if self.app:
            self.palette_model.bind_to_app(self.app)

    def _create_default_palette_collection(self) -> PaletteCollection:
        """Create a default palette collection with sample palettes."""
        # Define data paths
        data_dir = Path(__file__).parent.parent / "data"
        palettes_file = data_dir / "palettes.json"

        try:
            # Attempt to load palettes from file
            if palettes_file.exists():
                palette_collection = PaletteCollection.load_from_file(str(palettes_file))
                if palette_collection:
                    self.logger.info(f"Loaded palette collection from {palettes_file}")
                    return palette_collection
        except Exception as e:
            self.logger.error(f"Error loading palette collection: {e}")

        # Create sample palettes if loading fails
        default_palette = Palette(
            "Default", ["#FF5500", "#00AAFF", "#55FF00", "#AA00FF", "#FFAA00", "#00FFAA", "#FF0055", "#00FF55"]
        )

        monochrome_palette = Palette(
            "Monochrome", ["#FFFFFF", "#DDDDDD", "#BBBBBB", "#999999", "#777777", "#555555", "#333333", "#000000"]
        )

        sunset_palette = Palette(
            "Sunset", ["#FF7700", "#FF5500", "#FF0000", "#DD0000", "#AA0000", "#880000", "#550000", "#220000"]
        )

        # Create collection with the sample palettes
        self.logger.info("Created default palette collection")
        return PaletteCollection([default_palette, monochrome_palette, sunset_palette])

    # Properties for state values
    @property
    def is_dark_mode(self) -> bool:
        """Whether dark mode is enabled."""
        return self._is_dark_mode

    @is_dark_mode.setter
    def is_dark_mode(self, value: bool) -> None:
        """Set dark mode state."""
        if self._is_dark_mode != value:
            self._is_dark_mode = value
            if self.app:
                self.app.post_message(ThemeChanged(value))
                self.app.post_message(StateChanged("is_dark_mode", value))

    @property
    def current_view(self) -> ViewMode:
        """Current view mode."""
        return self._current_view

    @current_view.setter
    def current_view(self, value: ViewMode) -> None:
        """Set current view."""
        if self._current_view != value:
            self._current_view = value
            if self.app:
                self.app.post_message(StateChanged("current_view", value))

    @property
    def show_hex_values(self) -> bool:
        """Whether hex values are shown."""
        return self._show_hex_values

    @show_hex_values.setter
    def show_hex_values(self, value: bool) -> None:
        """Set hex value display."""
        if self._show_hex_values != value:
            self._show_hex_values = value
            if self.app:
                self.app.post_message(StateChanged("show_hex_values", value))

    @property
    def show_color_details(self) -> bool:
        """Whether color details are shown."""
        return self._show_color_details

    @show_color_details.setter
    def show_color_details(self, value: bool) -> None:
        """Set color details display."""
        if self._show_color_details != value:
            self._show_color_details = value
            if self.app:
                self.app.post_message(StateChanged("show_color_details", value))

    @property
    def is_help_visible(self) -> bool:
        """Whether help is visible."""
        return self._is_help_visible

    @is_help_visible.setter
    def is_help_visible(self, value: bool) -> None:
        """Set help visibility."""
        if self._is_help_visible != value:
            self._is_help_visible = value
            if self.app:
                self.app.post_message(StateChanged("is_help_visible", value))

    @property
    def history(self) -> List[Dict[str, Any]]:
        """History of state snapshots."""
        return self._history

    @history.setter
    def history(self, value: List[Dict[str, Any]]) -> None:
        """Set history."""
        self._history = value

    @property
    def history_index(self) -> int:
        """Current index in history."""
        return self._history_index

    @history_index.setter
    def history_index(self, value: int) -> None:
        """Set history index."""
        self._history_index = value

    def save_palettes(self) -> bool:
        """
        Save the current palette collection to file.

        Returns:
            Boolean indicating success or failure
        """
        try:
            # Save the current palette collection
            data_dir = Path(__file__).parent.parent / "data"
            palettes_file = data_dir / "palettes.json"

            # Create directory if it doesn't exist
            data_dir.mkdir(parents=True, exist_ok=True)

            # Save the palettes
            success = self.palette_collection.save_to_file(str(palettes_file))

            if success:
                self.logger.info(f"Saved palette collection to {palettes_file}")
            else:
                self.logger.error("Failed to save palette collection")

            return success
        except Exception as e:
            self.logger.error(f"Error saving palette collection: {e}")
            return False

    def set_dark_mode(self, enabled: bool) -> None:
        """
        Set the dark mode state.

        Args:
            enabled: Whether dark mode should be enabled
        """
        self.is_dark_mode = enabled

    def toggle_dark_mode(self) -> bool:
        """
        Toggle the dark mode state.

        Returns:
            The new dark mode state
        """
        new_state = not self.is_dark_mode
        self.set_dark_mode(new_state)
        return new_state

    def set_view(self, view: ViewMode) -> None:
        """
        Set the current view mode.

        Args:
            view: The view mode to set
        """
        self.current_view = view

    def toggle_hex_display(self) -> bool:
        """
        Toggle hex value display.

        Returns:
            The new hex display state
        """
        new_state = not self.show_hex_values
        self.show_hex_values = new_state
        return new_state

    def toggle_color_details(self) -> bool:
        """
        Toggle color details display.

        Returns:
            The new color details state
        """
        new_state = not self.show_color_details
        self.show_color_details = new_state
        return new_state

    def toggle_help(self) -> bool:
        """
        Toggle help visibility.

        Returns:
            The new help visibility state
        """
        new_state = not self.is_help_visible
        self.is_help_visible = new_state
        return new_state

    def add_to_history(self, state: Dict[str, Any]) -> None:
        """
        Add a state snapshot to the history for undo/redo.

        Args:
            state: The state snapshot to add
        """
        # If we're not at the end of the history, truncate it
        if self.history_index < len(self.history) - 1:
            self.history = self.history[: self.history_index + 1]

        # Add the new state
        new_history = list(self.history)
        new_history.append(state)
        self.history = new_history

        # Update the index
        self.history_index = len(self.history) - 1

    def can_undo(self) -> bool:
        """
        Check if undo is available.

        Returns:
            True if undo is available, False otherwise
        """
        return self.history_index > 0

    def can_redo(self) -> bool:
        """
        Check if redo is available.

        Returns:
            True if redo is available, False otherwise
        """
        return self.history_index < len(self.history) - 1

    def undo(self) -> Optional[Dict[str, Any]]:
        """
        Undo the last action by restoring a previous state.

        Returns:
            The restored state, or None if undo is not available
        """
        if not self.can_undo():
            return None

        # Move back in history
        self.history_index -= 1

        # Get the state at the new index
        return self.history[self.history_index]

    def redo(self) -> Optional[Dict[str, Any]]:
        """
        Redo a previously undone action.

        Returns:
            The restored state, or None if redo is not available
        """
        if not self.can_redo():
            return None

        # Move forward in history
        self.history_index += 1

        # Get the state at the new index
        return self.history[self.history_index]

    def capture_current_state(self) -> Dict[str, Any]:
        """
        Capture the current application state for history.

        Returns:
            Dictionary with the current state
        """
        # Capture relevant state properties
        active_palette_id = None
        active_color_index = 0

        # Access palette model data safely
        # We use the get methods instead of directly accessing reactive properties
        if self.get_active_palette() is not None:
            # Use type casting to safely access these attributes if needed
            from typing import cast

            palette_model = cast(Any, self.palette_model)
            active_palette_id = getattr(palette_model, "active_palette_id", None)
            active_color_index = getattr(palette_model, "active_color_index", 0)

        return {
            "active_palette_id": active_palette_id,
            "active_color_index": active_color_index,
            "view_mode": self.current_view,
            "dark_mode": self.is_dark_mode,
            "show_hex": self.show_hex_values,
            "show_details": self.show_color_details,
            # Include other relevant state...
        }

    def bind_to_app(self, app: Any) -> None:
        """
        Bind this state manager to an application.

        Args:
            app: The application to bind to
        """
        self.app = app

        # Also bind the palette model
        self.palette_model.bind_to_app(app)

    # Delegation methods to palette model for convenience
    def get_active_palette(self) -> Optional[Palette]:
        """
        Get the active palette.

        Returns:
            The active palette or None
        """
        return self.palette_model.active_palette

    def get_active_color(self) -> Optional[Color]:
        """
        Get the active color.

        Returns:
            The active color or None
        """
        return self.palette_model.active_color

    def set_active_palette(self, palette_id: str) -> None:
        """
        Set the active palette.

        Args:
            palette_id: ID of the palette to activate
        """
        self.palette_model.set_active_palette(palette_id)

    def set_active_color_index(self, index: int) -> None:
        """
        Set the active color index.

        Args:
            index: Index of the color to activate
        """
        self.palette_model.set_active_color_index(index)

    def update_active_color(self, color: Union[str, Color]) -> None:
        """
        Update the active color.

        Args:
            color: New color value
        """
        self.palette_model.update_active_color(color)
