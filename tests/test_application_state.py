"""
Unit tests for the application_state module.

This module contains tests for the ApplicationState class.
"""

from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from src.models.application_state import ApplicationState
from src.models.application_state import StateChanged
from src.models.application_state import ThemeChanged
from src.models.application_state import ViewMode


class TestApplicationState:
    """Test suite for the ApplicationState class."""

    def test_initialization(self):
        """Test ApplicationState initialization."""
        # Mock app to avoid needing real app instance
        mock_app = MagicMock()

        # Patch the _create_default_palette_collection to avoid creating actual collections
        with patch.object(ApplicationState, '_create_default_palette_collection'):
            with patch.object(ApplicationState, '_initialize_palette_model'):
                state = ApplicationState(mock_app)

                # Check default state values
                assert state.is_dark_mode is True
                assert state.current_view == ViewMode.PALETTE
                assert state.show_hex_values is True
                assert state.show_color_details is False
                assert state.is_help_visible is False
                assert state.history == []
                assert state.history_index == -1
                assert state.app == mock_app

    def test_dark_mode_toggle(self):
        """Test toggling dark mode."""
        # Mock app
        mock_app = MagicMock()

        # Patch the initialization methods
        with patch.object(ApplicationState, '_create_default_palette_collection'):
            with patch.object(ApplicationState, '_initialize_palette_model'):
                state = ApplicationState(mock_app)

                # Initially dark mode is True
                assert state.is_dark_mode is True

                # Toggle to False
                new_value = state.toggle_dark_mode()
                assert new_value is False
                assert state.is_dark_mode is False

                # Should send ThemeChanged and StateChanged messages
                mock_app.post_message.assert_any_call(ThemeChanged(False))
                mock_app.post_message.assert_any_call(StateChanged("is_dark_mode", False))

                # Reset mock to check next toggle
                mock_app.reset_mock()

                # Toggle back to True
                new_value = state.toggle_dark_mode()
                assert new_value is True
                assert state.is_dark_mode is True

                # Should send ThemeChanged and StateChanged messages again
                mock_app.post_message.assert_any_call(ThemeChanged(True))
                mock_app.post_message.assert_any_call(StateChanged("is_dark_mode", True))

    def test_set_view(self):
        """Test setting the view mode."""
        # Mock app
        mock_app = MagicMock()

        # Patch the initialization methods
        with patch.object(ApplicationState, '_create_default_palette_collection'):
            with patch.object(ApplicationState, '_initialize_palette_model'):
                state = ApplicationState(mock_app)

                # Initially current_view is PALETTE
                assert state.current_view == ViewMode.PALETTE

                # Change to COLOR_PICKER
                state.set_view(ViewMode.COLOR_PICKER)
                assert state.current_view == ViewMode.COLOR_PICKER

                # Should send StateChanged message
                mock_app.post_message.assert_called_once_with(
                    StateChanged("current_view", ViewMode.COLOR_PICKER)
                )

                # Reset mock to check next change
                mock_app.reset_mock()

                # Setting to the same value should not trigger message
                state.set_view(ViewMode.COLOR_PICKER)
                mock_app.post_message.assert_not_called()

    def test_toggle_hex_display(self):
        """Test toggling hex display."""
        # Mock app
        mock_app = MagicMock()

        # Patch the initialization methods
        with patch.object(ApplicationState, '_create_default_palette_collection'):
            with patch.object(ApplicationState, '_initialize_palette_model'):
                state = ApplicationState(mock_app)

                # Initially show_hex_values is True
                assert state.show_hex_values is True

                # Toggle to False
                new_value = state.toggle_hex_display()
                assert new_value is False
                assert state.show_hex_values is False

                # Should send StateChanged message
                mock_app.post_message.assert_called_once_with(
                    StateChanged("show_hex_values", False)
                )

    def test_toggle_color_details(self):
        """Test toggling color details display."""
        # Mock app
        mock_app = MagicMock()

        # Patch the initialization methods
        with patch.object(ApplicationState, '_create_default_palette_collection'):
            with patch.object(ApplicationState, '_initialize_palette_model'):
                state = ApplicationState(mock_app)

                # Initially show_color_details is False
                assert state.show_color_details is False

                # Toggle to True
                new_value = state.toggle_color_details()
                assert new_value is True
                assert state.show_color_details is True

                # Should send StateChanged message
                mock_app.post_message.assert_called_once_with(
                    StateChanged("show_color_details", True)
                )

    def test_toggle_help(self):
        """Test toggling help visibility."""
        # Mock app
        mock_app = MagicMock()

        # Patch the initialization methods
        with patch.object(ApplicationState, '_create_default_palette_collection'):
            with patch.object(ApplicationState, '_initialize_palette_model'):
                state = ApplicationState(mock_app)

                # Initially is_help_visible is False
                assert state.is_help_visible is False

                # Toggle to True
                new_value = state.toggle_help()
                assert new_value is True
                assert state.is_help_visible is True

                # Should send StateChanged message
                mock_app.post_message.assert_called_once_with(
                    StateChanged("is_help_visible", True)
                )

    def test_history_management(self):
        """Test history management (add, undo, redo)."""
        # Mock app
        mock_app = MagicMock()

        # Patch the initialization methods
        with patch.object(ApplicationState, '_create_default_palette_collection'):
            with patch.object(ApplicationState, '_initialize_palette_model'):
                state = ApplicationState(mock_app)

                # Initially history is empty
                assert state.history == []
                assert state.history_index == -1

                # Add two states
                state1 = {"view_mode": ViewMode.PALETTE, "dark_mode": True}
                state2 = {"view_mode": ViewMode.COLOR_PICKER, "dark_mode": False}

                state.add_to_history(state1)
                assert state.history == [state1]
                assert state.history_index == 0

                state.add_to_history(state2)
                assert state.history == [state1, state2]
                assert state.history_index == 1

                # Cannot redo at the end of history
                assert state.can_redo() is False
                assert state.redo() is None

                # Undo once
                previous = state.undo()
                assert previous == state1
                assert state.history_index == 0

                # Cannot undo at the beginning of history
                assert state.can_undo() is False

                # Can redo once
                assert state.can_redo() is True
                next_state = state.redo()
                assert next_state == state2
                assert state.history_index == 1

                # Add a new state after undo/redo should truncate history
                state3 = {"view_mode": ViewMode.EXPORT, "dark_mode": True}
                state.history_index = 0  # Simulate undoing to state1
                state.add_to_history(state3)
                assert state.history == [state1, state3]
                assert state.history_index == 1

    def test_bind_to_app(self):
        """Test binding the state manager to an app."""
        # Mock app
        mock_app = MagicMock()

        # Patch the initialization methods
        with patch.object(ApplicationState, '_create_default_palette_collection'):
            with patch.object(ApplicationState, '_initialize_palette_model'):
                # Create with no app
                state = ApplicationState()
                assert state.app is None

                # Bind to app
                state.bind_to_app(mock_app)
                assert state.app == mock_app

    def test_capture_current_state(self):
        """Test capturing the current application state."""
        # Mock app
        mock_app = MagicMock()

        # Patch the initialization methods and get_active_palette
        with patch.object(ApplicationState, '_create_default_palette_collection'):
            with patch.object(ApplicationState, '_initialize_palette_model'):
                with patch.object(ApplicationState, 'get_active_palette', return_value=None):
                    state = ApplicationState(mock_app)

                    # Set some state
                    state.is_dark_mode = True
                    state.current_view = ViewMode.COLOR_PICKER
                    state.show_hex_values = False

                    # Capture state
                    current_state = state.capture_current_state()

                    # Verify the captured state
                    assert current_state["active_palette_id"] is None
                    assert current_state["active_color_index"] == 0
                    assert current_state["view_mode"] == ViewMode.COLOR_PICKER
                    assert current_state["dark_mode"] is True
                    assert current_state["show_hex"] is False


if __name__ == "__main__":
    pytest.main(["-v", "test_application_state.py"])
