# milky_color_suite/screens/main_screen.py

from typing import ClassVar
from typing import List
from typing import Tuple
from typing import Union

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.containers import VerticalScroll
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import Label
from textual.widgets import Static

from ..widgets.color.color_info import ColorInfo
from ..widgets.color.color_selector import ColorSelector
from .base_screen import BaseScreen


# Import placeholder widgets or actual widgets from steps 2, 3, 4
# from ..widgets.placeholder import PlaceholderWidget # Example


class MainScreen(BaseScreen):
    """Main application screen."""

    # Define screen-specific bindings that extend BaseScreen bindings
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Color manipulation bindings specific to this screen
        Binding("a", "app.add_color", "Add color"),
        Binding("d", "app.delete_color", "Delete color"),
        Binding("e", "app.edit_color", "Edit color"),
        # Display options specific to main screen
        Binding("h", "app.toggle_hex_display", "Toggle hex values"),
        Binding("space", "app.toggle_color_details", "Toggle details"),
    ]

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
