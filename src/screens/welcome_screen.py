from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Button


class WelcomeScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Button("Continue", id="continue")


class MyApp(App):
    def on_mount(self) -> None:
        self.push_screen(WelcomeScreen())
