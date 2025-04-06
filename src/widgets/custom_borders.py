"""
Custom border widget implementations for Textual.

This module provides border implementations that match the application's
ASCII-art style while being fully dynamic and compatible with Textual's widget system.
"""

from typing import List
from typing import Optional

from textual.app import ComposeResult
from textual.containers import Container
from textual.containers import Horizontal
from textual.css.query import NoMatches
from textual.widget import Widget
from textual.widgets import Static


class BorderBox(Static):
    """A widget with custom borders that match the ASCII art style."""

    DEFAULT_CSS = """
    BorderBox {
        width: auto;
        height: auto;
        padding: 1;
    }
    """

    def __init__(
        self,
        *children: Widget,
        title: str = "",
        border_style: str = "single",
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ) -> None:
        """
        Initialize a BorderBox with custom borders.

        Args:
            *children: Child widgets to be added inside the border
            title: Optional title to display in the border
            border_style: Border style ("single", "double", or "mixed")
            widget_id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__("", id=widget_id, classes=classes)
        self.title = title
        self.border_style = border_style
        self._children = children

        # Character sets for different border styles
        self.border_chars = {
            "single": {
                "top_left": "┌",
                "top_right": "┐",
                "bottom_left": "└",
                "bottom_right": "┘",
                "horizontal": "─",
                "vertical": "│",
                "t_right": "├",
                "t_left": "┤",
                "t_up": "┴",
                "t_down": "┬",
                "cross": "┼",
            },
            "double": {
                "top_left": "╔",
                "top_right": "╗",
                "bottom_left": "╚",
                "bottom_right": "╝",
                "horizontal": "═",
                "vertical": "║",
                "t_right": "╠",
                "t_left": "╣",
                "t_up": "╩",
                "t_down": "╦",
                "cross": "╬",
            },
            "mixed": {
                "top_left": "╔",
                "top_right": "╗",
                "bottom_left": "╚",
                "bottom_right": "╝",
                "horizontal": "═",
                "vertical": "║",
                "t_right": "╠",
                "t_left": "╣",
                "t_up": "╩",
                "t_down": "╦",
                "cross": "╬",
                "single_horizontal": "─",
                "single_vertical": "│",
                "single_top_left": "┌",
                "single_top_right": "┐",
                "single_bottom_left": "└",
                "single_bottom_right": "┘",
            },
        }

    def compose(self) -> ComposeResult:
        """Compose the widget with child widgets."""
        with Container(id="border-content"):
            yield from self._children

    def render(self) -> str:
        """Render the box with custom borders.

        Returns:
            A string representation of the bordered box
        """
        width = self.size.width
        chars = self.border_chars[self.border_style]

        # Create the box borders
        top_border = chars["top_left"] + chars["horizontal"] * (width - 2) + chars["top_right"]
        bottom_border = chars["bottom_left"] + chars["horizontal"] * (width - 2) + chars["bottom_right"]

        # Add the title if provided
        if self.title:
            title_text = f" {self.title} "
            title_start = (width - len(title_text)) // 2
            top_border = (
                chars["top_left"]
                + chars["horizontal"] * title_start
                + title_text
                + chars["horizontal"] * (width - 2 - title_start - len(title_text))
                + chars["top_right"]
            )

        # Get the content from child containers
        content = self.get_content()

        # Combine everything into a single string with line breaks
        result = [top_border]

        for line in content:
            padded_line = line + " " * (width - 2 - len(line))
            result.append(chars["vertical"] + padded_line + chars["vertical"])

        result.append(bottom_border)

        return "\n".join(result)

    def get_content(self) -> List[str]:
        """Get content from child widgets."""
        try:
            # This is simplified; in a real implementation, we'd need to render
            # the content widget and extract its lines
            return ["Content goes here"]
        except NoMatches:
            return []


class ColorButton(Widget):
    """A color button widget that matches the ASCII art design."""

    DEFAULT_CSS = """
    ColorButton {
        width: 7;
        height: 3;
        content-align: center middle;
    }

    ColorButton.active {
        color: $text;
    }

    ColorButton.inactive {
        color: $text-muted;
    }
    """

    def __init__(
        self, color: str = "", active: bool = False, widget_id: Optional[str] = None, classes: Optional[str] = None
    ):
        """
        Initialize a color button.

        Args:
            color: The color value (hex, RGB, etc.)
            active: Whether this button is active
            widget_id: Optional ID for the widget
            classes: Optional CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
        self.color = color
        self.active = active

    def render(self) -> str:
        """Render the color button with custom borders.

        Returns:
            A string representation of the color button
        """
        # Set the border based on active state
        top_border = "┌█───█┐" if self.active else "┌─────┐"
        middle = "│" + self.color.center(5) + "│"
        bottom_border = "└─────┘"

        # Join them with newlines to create a single string
        return "\n".join([top_border, middle, bottom_border])


class DoubleHeaderBox(Container):
    """A container with a double-line header that matches the ASCII art design."""

    DEFAULT_CSS = """
    DoubleHeaderBox {
        width: auto;
        height: auto;
    }
    """

    def __init__(self, title: str, *children: Widget, widget_id: Optional[str] = None, classes: Optional[str] = None):
        """
        Initialize a box with a double-line header.

        Args:
            title: The title to display in the header
            *children: Child widgets
            widget_id: Optional ID for the widget
            classes: Optional CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
        self.title = title
        self._box_children = children

    def compose(self) -> ComposeResult:
        """Compose the widget with header and child widgets."""
        yield Static("╠═══════════════╗", classes="header-top")
        yield Static(f"├─♢ {self.title.ljust(12)}╠", classes="header-title")
        yield Static("╠═══════════════╝", classes="header-bottom")

        with Container(id="box-content", classes="box-content"):
            yield from self._box_children


class PaletteManagement(Container):
    """A palette management widget that matches the ASCII design."""

    def __init__(self, palette_name: str = "Default", widget_id: Optional[str] = None, classes: Optional[str] = None):
        """
        Initialize the palette management widget.

        Args:
            palette_name: Name of the current palette
            widget_id: Optional ID for the widget
            classes: Optional CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
        self.palette_name = palette_name

    def compose(self) -> ComposeResult:
        """Compose the palette management UI."""
        # Header with color tools
        yield Static("╠───────────────╦", classes="tools-header")
        yield Static("│ > Color Tools │", classes="tools-title")
        yield Static("╠───────────────╝", classes="tools-footer")

        # Color buttons row
        with Horizontal(id="color-buttons"):
            for i in range(8):
                is_active = i == 0  # First button is active by default
                yield ColorButton(color="", active=is_active, widget_id=f"color-{i}")

        # Palette controls
        controls_text = f"╠════════════════╗     Palette: {self.palette_name.ljust(20)}[Add New] [Rename] [Delete]"
        yield Static(controls_text, classes="palette-controls")

        # Active palette
        active_palette_text = (
            f"├─♢{self.palette_name.ljust(14)}╠┬────────────────┬────────────────┬────────────────┬────────────────┐"
        )
        yield Static(active_palette_text, classes="active-palette")

        # Empty palette slots
        yield Static(
            "╠════════════════╝├─               ├─               ├─               ├─               │",
            classes="inactive-palette",
        )
