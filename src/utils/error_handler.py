"""
Error handling and notification utilities for the Palette Milker application.

This module provides centralized error handling, logging, and notification
functionality to ensure consistent error management throughout the application.
"""

import logging
import traceback
from enum import Enum
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple
from typing import Union
from typing import cast

from textual.app import App
from textual.containers import Container
from textual.message import Message


# Configure the logger
logger = logging.getLogger("palette_milker")
logger.setLevel(logging.INFO)

# Create console handler if none exists
if not logger.handlers:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


class ErrorSeverity(Enum):
    """Enumeration of error severity levels."""

    DEBUG = "debug"
    INFO = "information"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "error"  # Map critical to error for UI purposes


class ErrorInfo:
    """Class to encapsulate error information."""

    def __init__(
        self,
        message: str,
        severity: Union[str, ErrorSeverity] = ErrorSeverity.ERROR,
        exception: Optional[Exception] = None,
        context: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize the error information.

        Args:
            message: The error message
            severity: The severity level
            exception: The original exception (if any)
            context: Additional context information
        """
        self.message = message

        # Convert string severity to enum if needed
        if isinstance(severity, str):
            try:
                self.severity = ErrorSeverity(severity)
            except ValueError:
                self.severity = ErrorSeverity.ERROR
        else:
            self.severity = severity

        self.exception = exception
        self.context = context or {}
        self.traceback = traceback.format_exc() if exception else None

    def __str__(self) -> str:
        """Return a string representation of the error."""
        return self.message

    @property
    def log_level(self) -> int:
        """Get the corresponding log level for this error severity."""
        severity_map = {
            ErrorSeverity.DEBUG: logging.DEBUG,
            ErrorSeverity.INFO: logging.INFO,
            ErrorSeverity.WARNING: logging.WARNING,
            ErrorSeverity.ERROR: logging.ERROR,
            ErrorSeverity.CRITICAL: logging.CRITICAL,
        }
        return severity_map.get(self.severity, logging.ERROR)

    @property
    def ui_severity(self) -> str:
        """Get the UI severity string for notifications."""
        return self.severity.value


class ErrorMessage(Message):
    """Message for error notifications throughout the application."""

    def __init__(self, error_info: ErrorInfo):
        """Initialize the error message.

        Args:
            error_info: The error information
        """
        self.error_info = error_info
        super().__init__()


def handle_error(
    message: str,
    severity: Union[str, ErrorSeverity] = ErrorSeverity.ERROR,
    exception: Optional[Exception] = None,
    context: Optional[Dict[str, Any]] = None,
    log: bool = True,
    notify: bool = True,
    app: Optional[App] = None,
) -> ErrorInfo:
    """
    Handle an error with consistent logging and notification.

    Args:
        message: The error message
        severity: The severity level
        exception: The original exception (if any)
        context: Additional context information
        log: Whether to log the error
        notify: Whether to notify the user
        app: The app instance for notifications

    Returns:
        The error information object
    """
    # Create error info
    error_info = ErrorInfo(message, severity, exception, context)

    # Log the error
    if log:
        log_message = f"{message}"
        if exception:
            log_message += f" Exception: {exception!s}"

        logger.log(error_info.log_level, log_message)

        # Log traceback for higher severity errors
        if error_info.severity in (ErrorSeverity.ERROR, ErrorSeverity.CRITICAL) and error_info.traceback:
            logger.debug(f"Traceback: {error_info.traceback}")

    # Notify the user
    if notify and app:
        try:
            # Cast to Any to bypass type checking, as we know the severity values match what's expected
            app_any = cast(Any, app)
            app_any.notify(message, severity=error_info.ui_severity)
        except Exception as e:
            # If notification fails, just log it
            logger.error(f"Failed to notify user: {e!s}")

    # Post message to the app for potential UI updates
    if app:
        try:
            app.post_message(ErrorMessage(error_info))
        except Exception as e:
            logger.error(f"Failed to post error message: {e!s}")

    return error_info


def try_operation(
    operation: Callable[[], Any],
    error_message: str = "Operation failed",
    severity: Union[str, ErrorSeverity] = ErrorSeverity.ERROR,
    context: Optional[Dict[str, Any]] = None,
    log: bool = True,
    notify: bool = True,
    app: Optional[App] = None,
) -> Tuple[bool, Any, Optional[ErrorInfo]]:
    """
    Attempt an operation and handle any errors.

    Args:
        operation: The operation to attempt
        error_message: The base error message
        severity: The severity level for errors
        context: Additional context information
        log: Whether to log errors
        notify: Whether to notify the user of errors
        app: The app instance for notifications

    Returns:
        Tuple of (success, result, error_info)
    """
    try:
        result = operation()
        return True, result, None
    except Exception as e:
        # Create more specific error message if available
        specific_message = f"{error_message}: {e!s}" if str(e) else error_message

        # Handle the error
        error_info = handle_error(
            message=specific_message, severity=severity, exception=e, context=context, log=log, notify=notify, app=app
        )

        return False, None, error_info


class ErrorDisplay(Container):
    """A widget for displaying error information in the UI."""

    DEFAULT_CSS = """
    ErrorDisplay {
        width: 100%;
        height: auto;
        background: $surface;
        border: solid $error;
        padding: 1;
        display: none;
    }

    ErrorDisplay.visible {
        display: block;
    }

    ErrorDisplay.warning {
        border: solid $warning;
    }

    ErrorDisplay.information {
        border: solid $accent;
    }

    ErrorDisplay #error-title {
        color: $error;
        text-style: bold;
    }

    ErrorDisplay.warning #error-title {
        color: $warning;
    }

    ErrorDisplay.information #error-title {
        color: $accent;
    }

    ErrorDisplay #error-message {
        margin-top: 1;
    }

    ErrorDisplay #error-details {
        margin-top: 1;
        color: $text-muted;
    }
    """

    def __init__(self, error_info: Optional[ErrorInfo] = None, **kwargs):
        """Initialize the error display.

        Args:
            error_info: Initial error information to display
            **kwargs: Additional arguments for the Container
        """
        super().__init__(**kwargs)
        self.error_info = error_info

    def compose(self):
        """Compose the error display widget."""
        from textual.widgets import Button
        from textual.widgets import Static

        # Error title based on severity
        yield Static("Error", id="error-title")

        # Error message
        yield Static("", id="error-message")

        # Additional details (if available)
        yield Static("", id="error-details")

        # Dismiss button
        yield Button("Dismiss", id="dismiss-error", variant="error")

    def on_mount(self) -> None:
        """Handle mounting of the widget."""
        # Hide by default
        self.display = False

        # If we have an error info, display it
        if self.error_info:
            self.show_error(self.error_info)

    def show_error(self, error_info: ErrorInfo) -> None:
        """Show an error in the display.

        Args:
            error_info: The error information to display
        """
        from textual.widgets import Static

        # Store the error info
        self.error_info = error_info

        # Set the appropriate class based on severity
        self.remove_class("error")
        self.remove_class("warning")
        self.remove_class("information")
        self.add_class(error_info.ui_severity)

        # Update the title
        title = self.query_one("#error-title", Static)
        severity_titles = {
            ErrorSeverity.ERROR: "Error",
            ErrorSeverity.WARNING: "Warning",
            ErrorSeverity.INFO: "Information",
            ErrorSeverity.DEBUG: "Debug Info",
        }
        title_text = severity_titles.get(error_info.severity, "Error")
        title.update(title_text)

        # Update the message
        message = self.query_one("#error-message", Static)
        message.update(error_info.message)

        # Update details if available
        details = self.query_one("#error-details", Static)
        if error_info.exception:
            details.update(f"Details: {error_info.exception!s}")
            details.display = True
        else:
            details.update("")
            details.display = False

        # Show the display
        self.display = True
        self.add_class("visible")

    def on_button_pressed(self, event):
        """Handle button press events."""
        if event.button.id == "dismiss-error":
            self.hide_error()

    def hide_error(self) -> None:
        """Hide the error display."""
        self.remove_class("visible")
        self.display = False
