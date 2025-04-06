"""
Base screen class for the Palette Milker application.

This module provides a base screen class with built-in error handling and logging
functionality that all screens should inherit from.
"""

import logging
from typing import Any
from typing import Callable
from typing import ClassVar
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Static

from ..utils.error_handler import ErrorDisplay
from ..utils.error_handler import ErrorInfo
from ..utils.error_handler import ErrorSeverity
from ..utils.error_handler import handle_error


# Create a logger for screens
logger = logging.getLogger("palette_milker.screens")


class BaseScreen(Screen):
    """
    Base screen class with built-in error handling.

    This class provides common functionality for screens including:
    - Centralized error handling
    - Consistent logging
    - UI error display
    - Standardized app-wide bindings
    """

    # Define app-wide bindings that all screens should inherit
    # Screens can override or extend these bindings as needed
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Application controls
        Binding("ctrl+q", "app.quit", "Quit", priority=True),
        Binding("f1", "app.toggle_help", "Help"),
        Binding("d", "app.toggle_dark", "Dark mode"),
        # Navigation
        Binding("tab", "focus_next", "Next field", show=False),
        Binding("shift+tab", "focus_previous", "Previous field", show=False),
        Binding("escape", "app.pop_screen", "Back", show=False, priority=True),
        # Screen navigation
        Binding("1", "app.view_palette", "Palette view"),
        Binding("2", "app.view_color_picker", "Color picker"),
        Binding("3", "app.view_export", "Export options"),
        # Palette Management
        Binding("ctrl+s", "app.save_palette", "Save palette"),
        Binding("ctrl+n", "app.new_palette", "New palette"),
        Binding("ctrl+o", "app.import_palette", "Import palette"),
        Binding("ctrl+e", "app.export_palette", "Export palette"),
    ]

    # Instance variables with proper typing
    error_display: Optional["ErrorDisplay"] = None
    _status_container: Optional["StatusContainer"] = None

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the base screen.

        Args:
            *args: Positional arguments to pass to the parent class
            **kwargs: Keyword arguments to pass to the parent class
        """
        super().__init__(*args, **kwargs)
        self.error_display = None
        self._status_container = None

    def compose(self) -> ComposeResult:
        """
        Compose the base screen.

        Note: Subclasses should override this method and yield their
        own widgets in addition to calling super().compose()
        """
        # Error display container
        self.error_display = ErrorDisplay(id="screen-error-display")
        yield self.error_display

        # Status container for operation feedback
        self._status_container = StatusContainer(id="screen-status-container")
        yield self._status_container

    def on_mount(self) -> None:
        """Handle screen mounting."""
        # Make sure error display is hidden by default
        if self.error_display:
            self.error_display.display = False

    def handle_error(
        self,
        message: str,
        severity: Union[str, ErrorSeverity] = ErrorSeverity.ERROR,
        exception: Optional[Exception] = None,
        context: Optional[Dict[str, Any]] = None,
        log: bool = True,
        notify: bool = True,
        display: bool = True,
    ) -> ErrorInfo:
        """
        Handle an error in the screen with consistent logging and notification.

        Args:
            message: The error message
            severity: The severity level
            exception: The original exception (if any)
            context: Additional context information
            log: Whether to log the error
            notify: Whether to notify the user
            display: Whether to display the error in the UI

        Returns:
            The error information object
        """
        # Create context if not provided
        if context is None:
            context = {}

        # Add screen info to context
        screen_context = {"screen": self.__class__.__name__, **context}

        # Handle the error using the central handler
        error_info = handle_error(
            message=message,
            severity=severity,
            exception=exception,
            context=screen_context,
            log=log,
            notify=notify,
            app=self.app,
        )

        # Display the error in the UI if requested
        if display and self.error_display:
            self.error_display.show_error(error_info)

        return error_info

    def try_operation(
        self,
        operation: Callable[[], Any],
        error_message: str = "Operation failed",
        success_message: Optional[str] = None,
        severity: Union[str, ErrorSeverity] = ErrorSeverity.ERROR,
        context: Optional[Dict[str, Any]] = None,
        log: bool = True,
        notify: bool = True,
        display: bool = True,
    ) -> Tuple[bool, Any, Optional[ErrorInfo]]:
        """
        Attempt an operation and handle any errors.

        Args:
            operation: The operation to attempt
            error_message: The base error message
            success_message: Optional message to show on success
            severity: The severity level for errors
            context: Additional context information
            log: Whether to log errors
            notify: Whether to notify the user of errors
            display: Whether to display errors in the UI

        Returns:
            Tuple of (success, result, error_info)
        """
        # Create context if not provided
        if context is None:
            context = {}

        # Add screen info to context
        screen_context = {"screen": self.__class__.__name__, **context}

        try:
            # Run the operation
            result = operation()

            # Show success message if provided
            if success_message:
                # Just use notify for success messages
                self.notify(success_message, severity="information")

                # Also show in status container if available
                if self._status_container:
                    self._status_container.show_status(success_message, "success")

            return True, result, None

        except Exception as e:
            # Create more specific error message if available
            specific_message = f"{error_message}: {e!s}" if str(e) else error_message

            # Handle the error
            error_info = self.handle_error(
                message=specific_message,
                severity=severity,
                exception=e,
                context=screen_context,
                log=log,
                notify=notify,
                display=display,
            )

            return False, None, error_info

    def show_status(self, message: str, status_type: str = "information", timeout: Optional[int] = None) -> None:
        """
        Show a status message in the status container.

        Args:
            message: The message to show
            status_type: The type of status (success, error, warning, information)
            timeout: Optional timeout in seconds to automatically hide the message
        """
        if self._status_container:
            self._status_container.show_status(message, status_type, timeout)


class StatusContainer(Container):
    """A container for displaying status messages."""

    DEFAULT_CSS = """
    StatusContainer {
        width: 100%;
        height: auto;
        margin: 1 0;
        padding: 1;
        background: $surface;
        border: solid $primary;
        display: none;
    }

    StatusContainer.visible {
        display: block;
    }

    StatusContainer.success {
        border: solid $success;
    }

    StatusContainer.error {
        border: solid $error;
    }

    StatusContainer.warning {
        border: solid $warning;
    }

    StatusContainer.information {
        border: solid $accent;
    }

    StatusContainer #status-message {
        width: 100%;
    }

    StatusContainer.success #status-message {
        color: $success;
    }

    StatusContainer.error #status-message {
        color: $error;
    }

    StatusContainer.warning #status-message {
        color: $warning;
    }

    StatusContainer.information #status-message {
        color: $accent;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the status container."""
        yield Static("", id="status-message")

    def on_mount(self) -> None:
        """Handle mounting of the container."""
        # Hide by default
        self.display = False

    def show_status(self, message: str, status_type: str = "information", timeout: Optional[int] = None) -> None:
        """
        Show a status message.

        Args:
            message: The message to show
            status_type: The type of status (success, error, warning, information)
            timeout: Optional timeout in seconds
        """
        # Update the message
        status_message = self.query_one("#status-message", Static)
        status_message.update(message)

        # Set the appropriate class
        self.remove_class("success")
        self.remove_class("error")
        self.remove_class("warning")
        self.remove_class("information")
        self.add_class(status_type)

        # Show the container
        self.display = True
        self.add_class("visible")

        # Set timeout if provided
        if timeout:
            # This is a simplified version - in a real implementation
            # we'd use a Timer or similar to hide after timeout
            # For now, just log that we would do this
            logger.debug(f"Would hide status after {timeout} seconds")

    def hide_status(self) -> None:
        """Hide the status message."""
        self.remove_class("visible")
        self.display = False
