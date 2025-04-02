from textual.app import App, ComposeResult
from textual.command import Command
from textual.widgets import Header


class CommandApp(App):
    def compose(self) -> ComposeResult:
        yield Header()

    def action_change_color(self) -> None:
        """Change the background color."""
        # Implementation here

    class ToggleDarkMode(Command):
        """Toggle between light and dark mode."""

        name = "toggle_dark_mode"

        def execute(self) -> None:
            # Implementation here
            pass

        def render(self) -> str:
            return "Toggle Dark Mode"
