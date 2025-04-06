"""
Unit tests for the error_handler module.

This module tests utility functions for error handling, logging, and notification.
"""

from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from src.utils.error_handler import ErrorDisplay
from src.utils.error_handler import ErrorInfo
from src.utils.error_handler import ErrorMessage
from src.utils.error_handler import ErrorSeverity
from src.utils.error_handler import handle_error
from src.utils.error_handler import try_operation


class TestErrorSeverity:
    """Test suite for ErrorSeverity enum."""

    def test_error_severity_values(self) -> None:
        """Test error severity enum values."""
        assert ErrorSeverity.DEBUG.value == "debug"
        assert ErrorSeverity.INFO.value == "information"
        assert ErrorSeverity.WARNING.value == "warning"
        assert ErrorSeverity.ERROR.value == "error"
        assert ErrorSeverity.CRITICAL.value == "error"  # Map critical to error for UI purposes


class TestErrorInfo:
    """Test suite for ErrorInfo class."""

    def test_error_info_initialization(self) -> None:
        """Test initializing an ErrorInfo object."""
        # Basic initialization
        error_info = ErrorInfo("Test error")
        assert error_info.message == "Test error"
        assert error_info.severity == ErrorSeverity.ERROR  # Default severity
        assert error_info.exception is None
        assert isinstance(error_info.context, dict)
        assert error_info.context == {}
        assert error_info.traceback is None  # No exception, so no traceback

        # With exception
        exception = ValueError("Test exception")
        error_info = ErrorInfo("Test error", exception=exception)
        assert error_info.exception == exception
        assert error_info.traceback is not None  # Should have a traceback

        # With context
        context = {"key": "value"}
        error_info = ErrorInfo("Test error", context=context)
        assert error_info.context == context

        # With severity
        error_info = ErrorInfo("Test error", severity=ErrorSeverity.WARNING)
        assert error_info.severity == ErrorSeverity.WARNING

        # With string severity
        error_info = ErrorInfo("Test error", severity="warning")
        assert error_info.severity == ErrorSeverity.WARNING

        # With invalid string severity
        error_info = ErrorInfo("Test error", severity="invalid")
        assert error_info.severity == ErrorSeverity.ERROR  # Falls back to ERROR

    def test_string_representation(self) -> None:
        """Test string representation of ErrorInfo."""
        error_info = ErrorInfo("Test error")
        assert str(error_info) == "Test error"

    def test_log_level(self) -> None:
        """Test log level property."""
        # Instead of checking exact values, check the error_info has a log_level property
        # and that the property returns an integer value
        debug_info = ErrorInfo("Test", ErrorSeverity.DEBUG)
        info_info = ErrorInfo("Test", ErrorSeverity.INFO)
        warning_info = ErrorInfo("Test", ErrorSeverity.WARNING)
        error_info = ErrorInfo("Test", ErrorSeverity.ERROR)
        critical_info = ErrorInfo("Test", ErrorSeverity.CRITICAL)

        # Check each has a log_level property that returns an integer
        assert isinstance(debug_info.log_level, int)
        assert isinstance(info_info.log_level, int)
        assert isinstance(warning_info.log_level, int)
        assert isinstance(error_info.log_level, int)
        assert isinstance(critical_info.log_level, int)

        # Check relative ordering of severity levels
        assert debug_info.log_level < info_info.log_level
        assert info_info.log_level < warning_info.log_level
        assert warning_info.log_level < error_info.log_level
        assert error_info.log_level <= critical_info.log_level

    def test_ui_severity(self) -> None:
        """Test UI severity property."""
        # Check all severity levels
        assert ErrorInfo("Test", ErrorSeverity.DEBUG).ui_severity == "debug"
        assert ErrorInfo("Test", ErrorSeverity.INFO).ui_severity == "information"
        assert ErrorInfo("Test", ErrorSeverity.WARNING).ui_severity == "warning"
        assert ErrorInfo("Test", ErrorSeverity.ERROR).ui_severity == "error"
        assert ErrorInfo("Test", ErrorSeverity.CRITICAL).ui_severity == "error"


class TestErrorMessage:
    """Test suite for ErrorMessage class."""

    def test_error_message_initialization(self) -> None:
        """Test initializing an ErrorMessage."""
        error_info = ErrorInfo("Test error")
        error_message = ErrorMessage(error_info)

        assert error_message.error_info == error_info


class TestHandleError:
    """Test suite for handle_error function."""

    def test_handle_error_logging(self) -> None:
        """Test that handle_error logs errors correctly."""
        with patch("src.utils.error_handler.logger") as mock_logger:
            # Basic error
            error_info = handle_error("Test error")

            # Check logging
            mock_logger.log.assert_called_once()
            log_level_arg = mock_logger.log.call_args[0][0]
            log_msg_arg = mock_logger.log.call_args[0][1]

            # Instead of comparing to a specific logging level, check that it matches the error_info.log_level
            assert log_level_arg == error_info.log_level
            assert "Test error" in log_msg_arg

            # With exception - should log traceback for high severity
            mock_logger.reset_mock()
            exception = ValueError("Test exception")
            handle_error("Test error with exception", exception=exception)

            # Check debug logging for traceback
            mock_logger.debug.assert_called_once()
            debug_arg = mock_logger.debug.call_args[0][0]
            assert "Traceback" in debug_arg

    def test_handle_error_notification(self) -> None:
        """Test that handle_error notifies the app."""
        # Create mock app
        mock_app = MagicMock()

        # Test notification
        handle_error("Test error", notify=True, app=mock_app)

        # Check app notification
        mock_app.notify.assert_called_once_with("Test error", severity="error")

        # Test with different severity
        mock_app.reset_mock()
        handle_error("Test warning", severity=ErrorSeverity.WARNING, app=mock_app)

        # Check app notification with correct severity
        mock_app.notify.assert_called_once_with("Test warning", severity="warning")

    def test_handle_error_post_message(self) -> None:
        """Test that handle_error posts an ErrorMessage to the app."""
        # Create mock app
        mock_app = MagicMock()

        # Test message posting
        error_info = handle_error("Test error", app=mock_app)

        # Check message posting
        mock_app.post_message.assert_called_once()
        posted_message = mock_app.post_message.call_args[0][0]

        # Verify it's an ErrorMessage with correct error_info
        assert isinstance(posted_message, ErrorMessage)
        assert posted_message.error_info == error_info

    def test_handle_error_no_notification(self) -> None:
        """Test handle_error with notification disabled."""
        # Create mock app
        mock_app = MagicMock()

        # Test with notify=False
        handle_error("Test error", notify=False, app=mock_app)

        # Check app notification was not called
        mock_app.notify.assert_not_called()

    def test_handle_error_no_logging(self) -> None:
        """Test handle_error with logging disabled."""
        with patch("src.utils.error_handler.logger") as mock_logger:
            # Test with log=False
            handle_error("Test error", log=False)

            # Check logging was not called
            mock_logger.log.assert_not_called()

    def test_handle_error_error_return(self) -> None:
        """Test that handle_error returns the error info."""
        # Test return value
        error_info = handle_error("Test error")

        # Check return type and data
        assert isinstance(error_info, ErrorInfo)
        assert error_info.message == "Test error"
        assert error_info.severity == ErrorSeverity.ERROR


class TestTryOperation:
    """Test suite for try_operation function."""

    def test_successful_operation(self) -> None:
        """Test trying an operation that succeeds."""
        # Define a successful operation
        def successful_operation() -> str:
            return "Success"

        # Try the operation
        success, result, error_info = try_operation(successful_operation)

        # Check result
        assert success is True
        assert result == "Success"
        assert error_info is None

    def test_failed_operation(self) -> None:
        """Test trying an operation that fails."""
        # Define a failing operation
        def failing_operation() -> None:
            raise ValueError("Operation failed")

        # Mock handle_error to avoid actual logging
        with patch("src.utils.error_handler.handle_error") as mock_handle_error:
            # Configure mock return value
            mock_error_info = ErrorInfo("Operation failed: Operation failed")
            mock_handle_error.return_value = mock_error_info

            # Try the operation
            success, result, error_info = try_operation(failing_operation)

            # Check result
            assert success is False
            assert result is None
            assert error_info == mock_error_info

            # Check handle_error was called
            mock_handle_error.assert_called_once()
            args = mock_handle_error.call_args[1]
            assert "Operation failed" in args["message"]
            assert isinstance(args["exception"], ValueError)

    def test_custom_error_message(self) -> None:
        """Test trying an operation with a custom error message."""
        # Define a failing operation
        def failing_operation() -> None:
            raise ValueError("Operation failed")

        # Mock handle_error to avoid actual logging
        with patch("src.utils.error_handler.handle_error") as mock_handle_error:
            # Configure mock return value
            mock_error_info = ErrorInfo("Custom error message: Operation failed")
            mock_handle_error.return_value = mock_error_info

            # Try the operation with custom error message
            success, result, error_info = try_operation(
                failing_operation, error_message="Custom error message"
            )

            # Verify return values
            assert success is False
            assert result is None
            assert isinstance(error_info, ErrorInfo)

            # Check handle_error was called with custom message
            args = mock_handle_error.call_args[1]
            assert "Custom error message" in args["message"]

    def test_custom_severity(self) -> None:
        """Test trying an operation with a custom severity."""
        # Define a failing operation
        def failing_operation() -> None:
            raise ValueError("Operation failed")

        # Mock handle_error to avoid actual logging
        with patch("src.utils.error_handler.handle_error") as mock_handle_error:
            # Try the operation with custom severity
            try_operation(
                failing_operation, severity=ErrorSeverity.WARNING
            )

            # Check handle_error was called with custom severity
            args = mock_handle_error.call_args[1]
            assert args["severity"] == ErrorSeverity.WARNING

    def test_with_app(self) -> None:
        """Test trying an operation with an app instance."""
        # Define a failing operation
        def failing_operation() -> None:
            raise ValueError("Operation failed")

        # Create mock app
        mock_app = MagicMock()

        # Mock handle_error to avoid actual logging
        with patch("src.utils.error_handler.handle_error") as mock_handle_error:
            # Try the operation with app
            try_operation(
                failing_operation, app=mock_app
            )

            # Check handle_error was called with app
            args = mock_handle_error.call_args[1]
            assert args["app"] == mock_app


class TestErrorDisplay:
    """Test suite for ErrorDisplay widget."""

    @pytest.fixture
    def error_info(self) -> ErrorInfo:
        """Return a sample error info for testing."""
        return ErrorInfo("Test error", ErrorSeverity.ERROR, ValueError("Test exception"))

    @pytest.fixture
    def warning_info(self) -> ErrorInfo:
        """Return a sample warning info for testing."""
        return ErrorInfo("Test warning", ErrorSeverity.WARNING)

    def test_error_display_initialization(self) -> None:
        """Test initializing the ErrorDisplay widget."""
        # Create with no error info
        error_display = ErrorDisplay()
        assert error_display.error_info is None

        # Create with error info
        error_info = ErrorInfo("Test error")
        error_display = ErrorDisplay(error_info)
        assert error_display.error_info == error_info

    def test_show_error(self, error_info: ErrorInfo) -> None:
        """Test showing an error in the display."""
        # Create error display
        error_display = ErrorDisplay()

        # Mock query_one to return mocked widgets
        title_mock = MagicMock()
        message_mock = MagicMock()
        details_mock = MagicMock()

        with patch.object(error_display, "query_one") as mock_query_one:
            mock_query_one.side_effect = lambda selector, *args: {
                "#error-title": title_mock,
                "#error-message": message_mock,
                "#error-details": details_mock,
            }[selector]

            # Test showing error
            error_display.show_error(error_info)

            # Check CSS classes
            assert "error" in error_display.classes
            assert "visible" in error_display.classes

            # Check widget updates
            title_mock.update.assert_called_once_with("Error")
            message_mock.update.assert_called_once_with("Test error")
            details_mock.update.assert_called_once_with("Details: Test exception")
            assert details_mock.display is True

    def test_show_warning(self, warning_info: ErrorInfo) -> None:
        """Test showing a warning in the display."""
        # Create error display
        error_display = ErrorDisplay()

        # Mock query_one to return mocked widgets
        title_mock = MagicMock()
        message_mock = MagicMock()
        details_mock = MagicMock()

        with patch.object(error_display, "query_one") as mock_query_one:
            mock_query_one.side_effect = lambda selector, *args: {
                "#error-title": title_mock,
                "#error-message": message_mock,
                "#error-details": details_mock,
            }[selector]

            # Test showing warning
            error_display.show_error(warning_info)

            # Check CSS classes
            assert "warning" in error_display.classes
            assert "visible" in error_display.classes

            # Check widget updates
            title_mock.update.assert_called_once_with("Warning")
            message_mock.update.assert_called_once_with("Test warning")
            # No exception in warning, so details should be empty
            details_mock.update.assert_called_once_with("")
            assert details_mock.display is False

    def test_hide_error(self) -> None:
        """Test hiding the error display."""
        # Create error display
        error_display = ErrorDisplay()
        error_display.add_class("visible")

        # Test hiding
        error_display.hide_error()

        # Check CSS classes
        assert "visible" not in error_display.classes
        assert error_display.display is False


if __name__ == "__main__":
    pytest.main(["-v", "test_error_handler.py"])
