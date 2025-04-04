"""
Worker module for handling background tasks in Textual.

This module provides a simple worker implementation for the Textual TUI framework
to handle long-running tasks without blocking the UI.
"""

import asyncio

from textual.app import App
from textual.app import ComposeResult
from textual.widgets import Button
from textual.widgets import Static
from textual.worker import Worker
from textual.worker import WorkerState


class WorkerApp(App):
    """
    Demo application showing how to use Textual workers for background tasks.

    This example creates a button that starts a background task and updates
    the UI when the task's state changes.
    """

    def compose(self) -> ComposeResult:
        """Compose the UI layout."""
        yield Button("Start Long Task", id="start")
        yield Static(id="status")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events to start the long task."""
        if event.button.id == "start":
            self.run_worker(self.long_task())

    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        """
        Handle worker state change events.

        Updates the status widget with information about the task's progress.

        Args:
            event: The worker state changed event
        """
        status = self.query_one("#status", Static)
        if event.state == WorkerState.RUNNING:
            # Use update_content instead of update for Static widgets
            status.update("Task running...")
        elif event.state == WorkerState.SUCCESS:
            # The worker's result is accessed directly from the worker
            # rather than from the event
            status.update(f"Task completed with result: {event.worker.result}")

    async def long_task(self) -> str:
        """
        Simulate a long-running task.

        Returns:
            A success message
        """
        # Simulate a long-running task
        # Use asyncio.sleep instead of self.sleep
        await asyncio.sleep(5)
        return "Completed successfully"
