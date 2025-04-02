from textual.app import App
from textual.widgets import Widget
from textual.key import Key
from textual.events import Click


class InputHandler(Widget):
    def on_key(self, event: Key) -> None:
        if event.key == "q":
            self.app.exit()

    def on_click(self, event: Click) -> None:
        self.app.bell()  # Make a sound
