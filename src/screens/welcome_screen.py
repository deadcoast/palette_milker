"""
Welcome screen for the Palette Milker application.

This screen is displayed when the application starts,
providing a friendly introduction to the application.
"""

from typing import ClassVar
from typing import List
from typing import Tuple
from typing import Union

from textual.app import App
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.widgets import Button
from textual.widgets import Static

from .base_screen import BaseScreen


class WelcomeScreen(BaseScreen):
    """
    Welcome screen displayed on application startup.

    This screen provides an introduction to the application and
    guides users on how to get started.
    """

    # Screen-specific bindings that extend BaseScreen bindings
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        Binding("enter", "start_app", "Start"),
    ]

    DEFAULT_CSS = """
    WelcomeScreen {
        align: center middle;
    }

    #welcome-container {
        width: 60%;
        height: auto;
        background: $surface;
        border: solid $primary;
        padding: 1 2;
    }

    #welcome-title {
        text-align: center;
        text-style: bold;
        color: $primary;
        width: 100%;
        margin-bottom: 1;
    }

    .welcome-text {
        margin-bottom: 1;
    }

    #continue-button {
        margin-top: 1;
        width: 20;
        align-horizontal: center;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the welcome screen with introduction and continue button."""
        with Container(id="welcome-container"):
            yield Static("Welcome to Palette Milker", id="welcome-title")

            yield Static(
                "Palette Milker is a TUI color palette manager that helps you create, edit, and export color palettes.",
                classes="welcome-text",
            )

            yield Static("Features:", classes="welcome-text")
            yield Static("• Create and manage multiple color palettes", classes="welcome-text")
            yield Static("• Pick colors using an interactive color wheel", classes="welcome-text")
            yield Static("• Export palettes in various formats (CSS, SCSS, JSON, etc.)", classes="welcome-text")
            yield Static("• Save and load palettes from files", classes="welcome-text")

            yield Static("Press F1 at any time to view keyboard shortcuts.", classes="welcome-text")

            yield Button("Continue →", id="continue-button", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "continue-button":
            self.action_continue()

    def action_continue(self) -> None:
        """Continue to the main application."""
        self.app.switch_screen("main")

    def action_start_app(self) -> None:
        """Start the application and go to the main screen."""
        self.app.switch_screen("main")


class MyApp(App):
    def on_mount(self) -> None:
        self.push_screen(WelcomeScreen())
