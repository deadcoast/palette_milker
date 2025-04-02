# milky_color_suite/screens/main_screen.py
from textual.app import ComposeResult
from textual.containers import Container, VerticalScroll, Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer, Static  # Add other needed widgets

from ..widgets.color.color_selector import ColorSelector
from ..widgets.color.color_info import ColorInfo

# Import placeholder widgets or actual widgets from steps 2, 3, 4
# from ..widgets.placeholder import PlaceholderWidget # Example


class MainScreen(Screen):
    """Main application screen."""

    BINDINGS = [("q", "quit", "Quit")]

    CSS_PATH = "../app.tcss"  # Optional: Link CSS file

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with VerticalScroll(id="sidebar-container"):
                yield Static("Sidebar Area")
                # Add PaletteList (Step 3), ImageColorPicker (removed/replaced) here
            with Container(id="main-and-palette"):
                with VerticalScroll(id="main-container"):
                    yield Label("Color Tools")  # Add a label/title
                    yield ColorSelector()  # Add the selector
                    yield ColorInfo()  # Add the info display
                    # Add PaletteName (Step 3), ExportPanel (Step 4) here
                with Container(id="palette-container"):
                    yield Static("Palette Area (Step 3)", id="palette-content")
                    # Add PalettePanel (Step 3) here
        yield Footer()

    # Add actions or methods as needed
    # def action_quit(self) -> None:
    #    self.app.exit()
