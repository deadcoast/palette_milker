"""
Custom Textual widgets that render ASCII UI elements using pattern-based approach.

These widgets dynamically construct ASCII UI elements from patterns,
allowing for consistent styling while maintaining flexibility.
"""

from typing import List
from typing import Optional
from typing import Tuple
from typing import cast

from rich.console import RenderableType
from rich.text import Text
from textual import events
from textual.app import ComposeResult
from textual.color import Color
from textual.containers import Container
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input
from textual.widgets import Static

from src.constants.builder import build_browse_tree
from src.constants.builder import build_color_palette
from src.constants.builder import build_color_wheel
from src.constants.builder import build_export_dialog
from src.constants.builder import build_naming_dialog
from src.constants.builder import build_palette_management
from src.constants.builder import create_button
from src.constants.builder import create_color_button
from src.constants.builder import create_text_input


class ASCIIWidget(Widget):
    """Base widget for rendering ASCII UI elements using patterns."""

    DEFAULT_CSS = """
    ASCIIWidget {
        background:;
    }
    """

    def __init__(self, name: Optional[str] = None, widget_id: Optional[str] = None, classes: Optional[str] = None):
        """
        Initialize the ASCIIWidget.

        Args:
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)

    def render_ascii(self) -> str:
        """
        Render the ASCII pattern.
        Must be implemented by subclasses.

        Returns:
            The ASCII pattern as a string
        """
        raise NotImplementedError("Subclasses must implement render_ascii()")

    def render(self) -> RenderableType:
        """Render the ASCII text."""
        return Text(self.render_ascii())


class ButtonClicked(Message):
    """Message sent when a button is clicked."""

    def __init__(self, sender: Widget):
        """Initialize the message with the sender widget."""
        super().__init__()
        self.sender = sender


class ColorButtonClicked(Message):
    """Message sent when a color button is clicked."""

    def __init__(self, sender: 'ColorButtonWidget'):
        """Initialize the message with the sender widget and color."""
        super().__init__()
        self.sender = sender
        self.color = sender.color


class TextSubmitted(Message):
    """Message sent when text is submitted."""

    def __init__(self, sender: 'TextInputWidget', text: str):
        """Initialize the message with the sender widget and text."""
        super().__init__()
        self.sender = sender
        self.text = text


class ButtonWidget(ASCIIWidget):
    """Widget for rendering a button using ASCII patterns."""

    DEFAULT_CSS = """
    ButtonWidget {
        width: auto;
        height: 3;
    }

    ButtonWidget.active {
        background: $accent-darken-2;
    }
    """

    text: reactive[str] = reactive("")
    active: reactive[bool] = reactive(False)
    width: reactive[int] = reactive(15)

    def __init__(
        self,
        text: str = "Button",
        active: bool = False,
        width: int = 15,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ButtonWidget.

        Args:
            text: The text to display in the button
            active: Whether the button is active
            width: The width of the button
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, widget_id=widget_id, classes=classes)
        self.text = text
        self.active = active
        self.width = width

    def render_ascii(self) -> str:
        """Render the button using the pattern."""
        return create_button(self.text, self.width, self.active)

    def watch_active(self, active: bool) -> None:
        """Watch for changes to the active state."""
        if active:
            self.add_class("active")
        else:
            self.remove_class("active")
        self.refresh()

    def on_click(self, event: events.Click) -> None:
        """Handle click events."""
        self.post_message(ButtonClicked(self))


class ColorButtonWidget(ASCIIWidget):
    """Widget for rendering a color button using ASCII patterns."""

    DEFAULT_CSS = """
    ColorButtonWidget {
        width: 7;
        height: 3;
    }

    ColorButtonWidget.active {
        background: $accent-darken-2;
    }
    """

    color: reactive[str] = reactive("#FFFFFF")
    active: reactive[bool] = reactive(False)

    def __init__(
        self,
        color: str = "#FFFFFF",
        active: bool = False,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ColorButtonWidget.

        Args:
            color: The color to display
            active: Whether the button is active
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, widget_id=widget_id, classes=classes)
        self.color = color
        self.active = active

    def render_ascii(self) -> str:
        """Render the color button using the pattern."""
        return create_color_button(self.color, self.active)

    def watch_active(self, active: bool) -> None:
        """Watch for changes to the active state."""
        if active:
            self.add_class("active")
        else:
            self.remove_class("active")
        self.refresh()

    def watch_color(self, color: str) -> None:
        """Watch for changes to the color."""
        self.refresh()

    def on_click(self, event: events.Click) -> None:
        """Handle click events."""
        self.post_message(ColorButtonClicked(self))


class TextInputWidget(ASCIIWidget):
    """Widget for rendering a text input using ASCII patterns."""

    DEFAULT_CSS = """
    TextInputWidget {
        width: auto;
        height: 1;
    }

    TextInputWidget.focused {
        background: $accent-darken-2;
    }
    """

    label: reactive[str] = reactive("input")
    text: reactive[str] = reactive("")
    focused: reactive[bool] = reactive(False)

    def __init__(
        self,
        label: str = "input",
        text: str = "",
        focused: bool = False,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the TextInputWidget.

        Args:
            label: The label for the input
            text: The text in the input
            focused: Whether the input is focused
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, widget_id=widget_id, classes=classes)
        self.label = label
        self.text = text
        self.focused = focused

    def render_ascii(self) -> str:
        """Render the text input using the pattern."""
        return create_text_input(self.label, self.text, self.focused)

    def watch_focused(self, focused: bool) -> None:
        """Watch for changes to the focused state."""
        if focused:
            self.add_class("focused")
        else:
            self.remove_class("focused")
        self.refresh()

    def watch_text(self, text: str) -> None:
        """Watch for changes to the text."""
        self.refresh()

    def on_key(self, event: events.Key) -> None:
        """Handle key events."""
        if not self.focused:
            return

        if event.key == "enter":
            self.post_message(TextSubmitted(self, self.text))
        elif event.key == "escape":
            self.focused = False
        elif event.key == "backspace":
            self.text = self.text[:-1]
        elif len(event.key) == 1:  # Single character
            self.text += event.key

        event.prevent_default()
        event.stop()

    def on_click(self, event: events.Click) -> None:
        """Handle click events."""
        self.focused = True


class ColorWheelWidget(Container):
    """Widget for rendering a color wheel using ASCII patterns."""

    DEFAULT_CSS = """
    ColorWheelWidget {
        width: auto;
        height: auto;
    }
    """

    width: reactive[int] = reactive(60)
    height: reactive[int] = reactive(15)

    def __init__(
        self,
        width: int = 60,
        height: int = 15,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ColorWheelWidget.

        Args:
            width: The width of the color wheel
            height: The height of the color wheel
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.width = width
        self.height = height

    def compose(self) -> ComposeResult:
        """Compose the widget."""
        # Main container shows the ASCII art
        yield Static(build_color_wheel(self.width, self.height), id="color-wheel-ascii")

        # Hidden functional components that overlay on the ASCII art
        yield TextInputWidget(label="HEX", widget_id="hex-input")
        yield ButtonWidget(text="Pick", widget_id="pick-button")
        yield ButtonWidget(text="Save", widget_id="save-button")

        # The actual color grid (would be a custom widget in practice)
        # This would overlay on the ASCII frame


class PaletteSlots(Container):
    """Container for color slots in a palette."""

    DEFAULT_CSS = """
    PaletteSlots {
        layout: horizontal;
        height: 3;
        margin: 0 1;
    }
    """

    colors: reactive[List[str]] = reactive(["#FFFFFF"] * 8)
    active_index: reactive[int] = reactive(0)
    _border_color_names: reactive[List[str]] = reactive(["$primary"] * 4)

    # Override property to correctly handle the reactive attribute
    @property
    def border_colors(self) -> Tuple[Color, Color, Color, Color]:
        """Get the border colors."""
        return (
            Color.parse("$primary"),
            Color.parse("$primary"),
            Color.parse("$primary"),
            Color.parse("$primary")
        )

    def __init__(
        self,
        colors: Optional[List[str]] = None,
        active_index: int = 0,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the PaletteSlots.

        Args:
            colors: List of colors (hex)
            active_index: Index of the active color
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.colors = colors or ["#FFFFFF"] * 8
        self.active_index = active_index

    def compose(self) -> ComposeResult:
        """Compose the widget."""
        # First show the ASCII representation
        yield Static(build_color_palette(self.colors, self.active_index), id="palette-slots-ascii")

        # Create interactive color buttons that will overlay on the ASCII art
        for i, color in enumerate(self.colors):
            yield ColorButtonWidget(color=color, active=i == self.active_index, widget_id=f"color-slot-{i}")

    def watch_active_index(self, active_index: int) -> None:
        """Watch for changes to the active index."""
        for i, widget in enumerate(self.query(ColorButtonWidget)):
            widget.active = i == active_index

        # Update ASCII representation
        self.query_one("#palette-slots-ascii", Static).update(build_color_palette(self.colors, self.active_index))

    def watch_colors(self, colors: List[str]) -> None:
        """Watch for changes to the colors."""
        for widget, color in zip(self.query(ColorButtonWidget), colors, strict=True):
            widget.color = color

        # Update ASCII representation
        self.query_one("#palette-slots-ascii", Static).update(build_color_palette(self.colors, self.active_index))

    def get_border_colors(self) -> Tuple[Color, Color, Color, Color]:
        """Get the border colors as a tuple of Color objects."""
        return cast(Tuple[Color, Color, Color, Color], tuple(
            Color.parse(color) for color in self._border_color_names
        ))


class PaletteManagementWidget(Container):
    """Widget for rendering the palette management UI."""

    DEFAULT_CSS = """
    PaletteManagementWidget {
        width: auto;
        height: auto;
    }
    """

    palette_name: reactive[str] = reactive("Default")
    active_palette_index: reactive[int] = reactive(0)
    palette_count: reactive[int] = reactive(4)
    width: reactive[int] = reactive(80)

    def __init__(
        self,
        palette_name: str = "Default",
        active_palette_index: int = 0,
        palette_count: int = 4,
        width: int = 80,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the PaletteManagementWidget.

        Args:
            palette_name: Name of the active palette
            active_palette_index: Index of the active palette
            palette_count: Number of palettes
            width: Total width of the UI
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.palette_name = palette_name
        self.active_palette_index = active_palette_index
        self.palette_count = palette_count
        self.width = width

    def compose(self) -> ComposeResult:
        """Compose the widget."""
        # ASCII representation
        yield Static(
            build_palette_management(self.palette_name, self.active_palette_index, self.palette_count, self.width),
            id="palette-management-ascii",
        )

        # Interactive components
        yield ButtonWidget(text="Add New", widget_id="add-palette-button")
        yield ButtonWidget(text="Rename", widget_id="rename-palette-button")
        yield ButtonWidget(text="Delete", widget_id="delete-palette-button")

        # Palette slots
        yield PaletteSlots(widget_id="palette-slots")

    def watch_palette_name(self, palette_name: str) -> None:
        """Watch for changes to the palette name."""
        self._update_ascii()

    def watch_active_palette_index(self, active_palette_index: int) -> None:
        """Watch for changes to the active palette index."""
        self._update_ascii()

    def watch_palette_count(self, palette_count: int) -> None:
        """Watch for changes to the palette count."""
        self._update_ascii()

    def watch_width(self, width: int) -> None:
        """Watch for changes to the width."""
        self._update_ascii()

    def _update_ascii(self) -> None:
        """Update the ASCII representation."""
        self.query_one("#palette-management-ascii", Static).update(
            build_palette_management(self.palette_name, self.active_palette_index, self.palette_count, self.width)
        )


class BrowseTreeWidget(ASCIIWidget):
    """Widget for rendering the browse tree."""

    DEFAULT_CSS = """
    BrowseTreeWidget {
        width: auto;
        height: auto;
    }
    """

    def render_ascii(self) -> str:
        """Render the browse tree."""
        return build_browse_tree()

    def on_click(self, event: events.Click) -> None:
        """Handle click events."""
        # This would handle expanding/collapsing folders and selecting items
        pass


class NamingDialogWidget(Container):
    """Widget for rendering the palette naming dialog."""

    DEFAULT_CSS = """
    NamingDialogWidget {
        width: 45;
        height: 7;
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the widget."""
        # ASCII representation
        yield Static(build_naming_dialog(), id="naming-dialog-ascii")

        # Interactive components
        yield Input(placeholder="Enter palette name", id="palette-name-input")
        yield ButtonWidget(text="OK", widget_id="naming-ok-button")
        yield ButtonWidget(text="Cancel", widget_id="naming-cancel-button")


class ExportDialogWidget(Container):
    """Widget for rendering the export dialog."""

    DEFAULT_CSS = """
    ExportDialogWidget {
        width: 45;
        height: 7;
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        """Compose the widget."""
        # ASCII representation
        yield Static(build_export_dialog(), id="export-dialog-ascii")

        # Interactive components
        yield Input(placeholder="Choose export format", id="export-format-input")
        yield ButtonWidget(text="OK", widget_id="export-ok-button")
        yield ButtonWidget(text="Cancel", widget_id="export-cancel-button")
