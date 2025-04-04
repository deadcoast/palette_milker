from typing import ClassVar
from typing import List
from typing import Tuple
from typing import Union

from textual.app import App
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Grid
from textual.containers import Horizontal
from textual.containers import Vertical
from textual.reactive import reactive
from textual.widgets import Button
from textual.widgets import DataTable
from textual.widgets import Static


"""
App Class Variables
  CSS_PATH: Path(s) to CSS file(s)
  BINDINGS: Key bindings for the app
  TITLE: Window title
  SUB_TITLE: Subtitle displayed in the header

Widget Variables
  DEFAULT_CSS: Default CSS for the widget
  COMPONENT_CLASSES: Component classes that can be targeted in CSS
  SCOPED_CSS: Whether CSS is scoped to the widget (default: True)
"""


class StyledApp(App):
    """
    /* Using variables in CSS */
    Button {
        background: $accent;
        color: $text;
        border: solid $primary;
        padding: 1 2;
    }
    """

    CSS_PATH = "example.tcss"
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [Binding("q", "quit", "Quit")]
    TITLE = "Styled App"
    SUB_TITLE = "Using variables in CSS"
    DEFAULT_CSS = """
    Button {
        background: $accent;
        color: $text;
        border: solid $primary;
        padding: 1 2;
    }
    """


class ReactiveApp(App):
    count = reactive(0)

    def compose(self) -> ComposeResult:
        yield Static(id="counter")

    def on_mount(self) -> None:
        self.set_interval(1, self.increment_counter)

    def increment_counter(self) -> None:
        self.count += 1

    def watch_count(self, value: int) -> None:
        # Get the Static widget and update its renderable
        counter_widget = self.query_one("#counter", Static)
        counter_widget.update(f"Count: {value}")


class LayoutApp(App):
    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal():
                yield Button("Top Left")
                yield Button("Top Right")
            yield Button("Bottom")


class GridApp(App):
    CSS = """
    Grid {
        grid-size: 3 2;
        grid-gutter: 1;
    }
    #btn1 {
        column-span: 2;
    }
    """

    def compose(self) -> ComposeResult:
        with Grid():
            yield Button("Spans 2 columns", id="btn1")
            yield Button("Third column")
            yield Button("Bottom left")
            yield Button("Bottom middle")
            yield Button("Bottom right")


class TableApp(App):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("ID", "Name", "Value")
        table.add_rows([(1, "Item A", "$10.00"), (2, "Item B", "$20.00"), (3, "Item C", "$30.00")])
