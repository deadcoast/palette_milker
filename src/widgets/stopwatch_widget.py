from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static


class Stopwatch(Static):
    """A stopwatch widget."""

    time = reactive(0.0)
    running = reactive(False)

    def on_mount(self) -> None:
        """Called when widget is added to the app."""
        self.update_timer = self.set_interval(0.1, self.update_time, pause=True)

    def update_time(self) -> None:
        """Update the time by 0.1 seconds."""
        self.time += 0.1

    def watch_time(self, time: float) -> None:
        """Called when the time attribute changes."""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self) -> None:
        """Start the stopwatch."""
        self.running = True
        self.update_timer.resume()

    def stop(self) -> None:
        """Stop the stopwatch."""
        self.running = False
        self.update_timer.pause()

    def reset(self) -> None:
        """Reset the stopwatch."""
        self.stop()
        self.time = 0.0


class StopwatchApp(App):
    CSS = """
    Stopwatch {
        width: 100%;
        height: 3;
        content-align: center middle;
        text-style: bold;
        border: solid green;
        text-opacity: 0.85;
    }

    Button {
        width: 16;
        margin: 1 2;
    }

    #start {
        background: $success;
    }

    #stop {
        background: $error;
    }

    #reset {
        background: $warning;
    }

    Container {
        align: center middle;
        height: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Stopwatch(), Button("Start", id="start"), Button("Stop", id="stop"), Button("Reset", id="reset")
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Called when a button is pressed."""
        stopwatch = self.query_one(Stopwatch)
        button_id = event.button.id

        if button_id == "start":
            stopwatch.start()
        elif button_id == "stop":
            stopwatch.stop()
        elif button_id == "reset":
            stopwatch.reset()


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
