from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.worker import Worker, WorkerState


class WorkerApp(App):
    def compose(self) -> ComposeResult:
        yield Button("Start Long Task", id="start")
        yield Static(id="status")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            self.run_worker(self.long_task())

    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        status = self.query_one("#status")
        if event.state == WorkerState.RUNNING:
            status.update("Task running...")
        elif event.state == WorkerState.SUCCESS:
            status.update(f"Task completed with result: {event.result}")

    async def long_task(self) -> str:
        # Simulate a long-running task
        await self.sleep(5)
        return "Completed successfully"
