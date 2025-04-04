"""
Palette management widgets for the Milky Color Suite.

This module contains widgets for managing color palettes,
implementing the exact terminal-based UI design specified.
"""

from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from rich.console import Console
from rich.console import RenderableType
from rich.style import Style
from rich.text import Text
from textual import events
from textual.app import ComposeResult
from textual.containers import Container
from textual.containers import Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button
from textual.widgets import Input

from constants.patterns import PATTERNS
from widgets.ascii_widget import ASCIIWidget


class TransparentWidget(Widget):
    """Base widget for transparent UI elements."""

    DEFAULT_CSS = """
    TransparentWidget {
        background: transparent;
    }
    """

    def __init__(
        self,
        ascii_pattern: str,
        interactive: bool = True,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the TransparentWidget.

        Args:
            ascii_pattern: ASCII pattern to display
            interactive: Whether the widget is interactive
            name: Widget name
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.ascii_pattern = ascii_pattern
        self.interactive = interactive

    def render(self) -> RenderableType:
        """Render the widget."""
        return Text.from_markup(self.ascii_pattern)


class TransparentButton(TransparentWidget):
    """Button that appears transparent."""

    # Reactive properties
    active = reactive(False)

    def __init__(
        self,
        ascii_pattern: str,
        active: bool = False,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the TransparentButton.

        Args:
            ascii_pattern: ASCII pattern to display
            active: Whether the button is active
            name: Widget name
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(ascii_pattern=ascii_pattern, name=name, widget_id=widget_id, classes=classes)
        self.active = active

    def on_click(self, event: events.Click) -> None:
        """Handle the button being clicked."""
        self.post_message(self.Pressed(self))

    class Pressed(Message):
        """Event sent when the button is pressed."""

        def __init__(self, sender: "TransparentButton") -> None:
            """
            Initialize a button pressed message.

            Args:
                sender: The button that was pressed
            """
            super().__init__()
            self.sender = sender


class PaletteSelector(Container):
    """Widget for selecting and managing palettes."""

    DEFAULT_CSS = """
    PaletteSelector {
        width: 100%;
        height: auto;
        layout: horizontal;
        overflow-x: auto;
    }
    """

    # Reactive properties with proper type annotations
    palettes: reactive[List[Dict[str, Any]]] = reactive([])
    active_palette_id: reactive[str] = reactive("")

    def __init__(
        self,
        palettes: Optional[List[Dict[str, Any]]] = None,
        active_palette_id: Optional[str] = None,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """Initialize the palette selector.

        Args:
            palettes: List of palette dictionaries
            active_palette_id: ID of the active palette
            name: Widget name
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        if palettes:
            self.palettes = palettes
        if active_palette_id:
            self.active_palette_id = active_palette_id

    def compose(self) -> ComposeResult:
        """Compose the palette selector with palette buttons."""
        for palette in self.palettes:
            yield PaletteButton(palette=palette, active=palette["id"] == self.active_palette_id)

        # Add a new palette button
        yield TransparentButton(ascii_pattern=PATTERNS["ADD_BUTTON"], widget_id="add-palette")

    def on_mount(self) -> None:
        """Handle widget mounting."""
        self.add_class("palette-selector")

    def watch_palettes(self, old_palettes: List[Dict[str, Any]], new_palettes: List[Dict[str, Any]]) -> None:
        """Watch for changes to the palettes list.

        Args:
            old_palettes: Previous palettes list
            new_palettes: New palettes list
        """
        self.remove_children()
        self.mount_all(self._make_buttons())

    def watch_active_palette_id(self, old_id: str, new_id: str) -> None:
        """Watch for changes to the active palette ID.

        Args:
            old_id: Previous active palette ID
            new_id: New active palette ID
        """
        for child in self.query(PaletteButton):
            if isinstance(child, PaletteButton):
                child.active = child.palette["id"] == new_id

    def _make_buttons(self) -> List[Widget]:
        """Create palette buttons from the palettes list."""
        # Create buttons with explicit type annotation
        buttons: List[Widget] = []

        # Add palette buttons
        buttons.extend(
            PaletteButton(palette=palette, active=palette["id"] == self.active_palette_id) for palette in self.palettes
        )
        # Add a new palette button
        buttons.append(TransparentButton(ascii_pattern=PATTERNS["ADD_BUTTON"], widget_id="add-palette"))

        return buttons

    def on_transparent_button_pressed(self, event: TransparentButton.Pressed) -> None:
        """Handle the add palette button being pressed.

        Args:
            event: The pressed event with sender available as event.sender
        """
        # Check the ID of the sender to determine which button was pressed
        # sender is automatically set by the Textual framework
        if isinstance(event.sender, TransparentButton) and event.sender.id == "add-palette":
            self.post_message(self.AddPalette())

    def on_palette_button_pressed(self, event: "PaletteButton.Pressed") -> None:
        """Handle a palette button being pressed.

        Args:
            event: The pressed event with sender available as event.sender
        """
        # Make sure we only handle PaletteButton presses
        # sender is automatically set by the Textual framework
        if isinstance(event.sender, PaletteButton):
            # Cast to ensure type safety
            palette_id = str(event.sender.palette["id"])
            self.post_message(self.PaletteSelected(palette_id))

    # Custom messages
    class PaletteSelected(Message):
        """Event sent when a palette is selected."""

        def __init__(self, palette_id: str) -> None:
            """Initialize a palette selected message.

            Args:
                palette_id: ID of the selected palette
            """
            self.palette_id = palette_id
            super().__init__()

    class AddPalette(Message):
        """Event sent when the add palette button is pressed."""

        def __init__(self) -> None:
            """Initialize an add palette message."""
            super().__init__()


class PaletteButton(TransparentButton):
    """Button for selecting a palette."""

    # Reactive property with proper type annotation
    palette: reactive[Dict[str, Any]] = reactive({"id": "", "name": "", "colors": []})

    def __init__(
        self,
        palette: Dict[str, Any],
        active: bool = False,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """Initialize a palette button.

        Args:
            palette: Palette dictionary
            active: Whether the button is active
            name: Widget name
            widget_id: Widget ID
            classes: CSS classes
        """
        pattern = PATTERNS["PALETTE_BUTTON"]["ACTIVE" if active else "DEFAULT"]
        super().__init__(ascii_pattern=pattern, active=active, name=name, widget_id=widget_id, classes=classes)
        self.palette = palette

    def watch_palette(self, old_palette: Dict[str, Any], new_palette: Dict[str, Any]) -> None:
        """Watch for changes to the palette object.

        Args:
            old_palette: Previous palette object
            new_palette: New palette object
        """
        self.refresh()

    def render(self):
        """Render the palette button with the palette name."""
        pattern = PATTERNS["PALETTE_BUTTON"]["ACTIVE" if self.active else "DEFAULT"]
        # We should use the palette name in the pattern but this is a simplified example
        return Text.from_markup(pattern)


class ColorSlots(Container):
    """Widget for displaying and selecting color slots."""

    DEFAULT_CSS = """
    ColorSlots {
        width: 100%;
        height: auto;
        layout: horizontal;
        background: $surface;
    }
    """

    def __init__(
        self,
        colors: Optional[List[str]] = None,
        active_slot_index: int = 0,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """Initialize the color slots widget.

        Args:
            colors: List of color strings
            active_slot_index: Index of the active slot
            name: Widget name
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self._colors = colors or ["#FFFFFF"] * 8
        self._active_slot_index = active_slot_index

    # Use methods instead of properties to avoid conflicts with DOMNode
    def get_colors(self) -> List[str]:
        """Get the current colors.

        Returns:
            The list of colors
        """
        return self._colors

    def set_colors(self, colors: List[str]) -> None:
        """Set the colors list.

        Args:
            colors: New list of colors
        """
        self._colors = colors
        if hasattr(self, "children") and self.children:
            self._update_slot_colors()

    def get_active_slot_index(self) -> int:
        """Get the active slot index.

        Returns:
            The active slot index
        """
        return self._active_slot_index

    def set_active_slot_index(self, index: int) -> None:
        """Set the active slot index.

        Args:
            index: New active index
        """
        self._active_slot_index = index
        if hasattr(self, "children") and self.children:
            self._update_slot_active_states()

    def compose(self) -> ComposeResult:
        """Compose the color slots."""
        for i, color in enumerate(self._colors):
            yield ColorSlot(color=color, index=i, active=i == self._active_slot_index)

    def _update_slot_colors(self) -> None:
        """Update the colors of all slots."""
        for i, color in enumerate(self._colors):
            if i < len(self.query(ColorSlot)):
                slot = self.query(ColorSlot)[i]
                # Ensure color is a string
                slot.color = str(color)

    def _update_slot_active_states(self) -> None:
        """Update the active state of all slots."""
        for slot in self.query(ColorSlot):
            slot.active = slot.index == self._active_slot_index

    def on_color_slot_clicked(self, event: "ColorSlot.Clicked") -> None:
        """Handle a color slot being clicked.

        Args:
            event: The clicked event with sender available as event.sender
        """
        # sender is automatically set by the Textual framework
        if isinstance(event.sender, ColorSlot):
            self.post_message(self.SlotSelected(event.sender.index))

    def on_color_slot_double_clicked(self, event: "ColorSlot.DoubleClicked") -> None:
        """Handle a color slot being double-clicked.

        Args:
            event: The double-clicked event with sender available as event.sender
        """
        # sender is automatically set by the Textual framework
        if isinstance(event.sender, ColorSlot):
            self.post_message(self.SlotDoubleClicked(event.sender.index))

    # Custom messages
    class SlotSelected(Message):
        """Event sent when a slot is selected."""

        def __init__(self, slot_index: int) -> None:
            """Initialize a slot selected message.

            Args:
                slot_index: Index of the selected slot
            """
            self.slot_index = slot_index
            super().__init__()

    class SlotDoubleClicked(Message):
        """Event sent when a slot is double-clicked."""

        def __init__(self, slot_index: int) -> None:
            """Initialize a slot double-clicked message.

            Args:
                slot_index: Index of the double-clicked slot
            """
            self.slot_index = slot_index
            super().__init__()


class ColorSlot(Widget):
    """A single color slot in the palette."""

    DEFAULT_CSS = """
    ColorSlot {
        width: 5;
        height: 3;
        margin: 0 1;
        background: $background;
        border: solid $primary;
        content-align: center middle;
        cursor: pointer;
    }

    ColorSlot:hover {
        border: solid $accent;
    }

    ColorSlot.active {
        border: solid $accent;
    }
    """

    # Reactive properties with proper type annotations
    color: reactive[str] = reactive("#FFFFFF")
    index: reactive[int] = reactive(0)
    active: reactive[bool] = reactive(False)

    def __init__(
        self,
        color: str = "#FFFFFF",
        index: int = 0,
        active: bool = False,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """Initialize a color slot.

        Args:
            color: Color string
            index: Slot index
            active: Whether the slot is active
            name: Widget name
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.color = color
        self.index = index
        self.active = active

    def on_mount(self) -> None:
        """Handle widget mounting."""
        if self.active:
            self.add_class("active")

    def watch_active(self, old_active: bool, new_active: bool) -> None:
        """Watch for changes to the active state.

        Args:
            old_active: Previous active state
            new_active: New active state
        """
        if new_active:
            self.add_class("active")
        else:
            self.remove_class("active")

    def watch_color(self, old_color: str, new_color: str) -> None:
        """Watch for changes to the color.

        Args:
            old_color: Previous color value
            new_color: New color value
        """
        # Apply the background color
        self.styles.background = new_color
        self.refresh()

    def render(self):
        """Render the color slot."""
        # Create a color block
        style = Style(bgcolor=self.color)
        console = Console()
        with console.capture() as capture:
            # Display slot index on the color background
            console.print(f" {self.index + 1} ", style=style)

        return capture.get()

    def on_click(self, event: events.Click) -> None:
        """Handle the slot being clicked."""
        self.post_message(self.Clicked(self))

    def on_double_click(self, event: events.Click) -> None:
        """Handle the slot being double-clicked."""
        self.post_message(self.DoubleClicked(self))

    # Custom messages
    class Clicked(Message):
        """Event sent when the slot is clicked."""

        def __init__(self, sender: "ColorSlot") -> None:
            """Initialize a clicked message.

            Args:
                sender: The slot that was clicked
            """
            super().__init__()
            self.sender = sender

    class DoubleClicked(Message):
        """Event sent when the slot is double-clicked."""

        def __init__(self, sender: "ColorSlot") -> None:
            """Initialize a double-clicked message.

            Args:
                sender: The slot that was double-clicked
            """
            super().__init__()
            self.sender = sender


class PaletteNameInput(Container):
    """
    A dialog for entering a palette name.

    This widget displays a dialog for entering a name for a palette,
    with OK and Cancel buttons.
    """

    DEFAULT_CSS = """
    PaletteNameInput {
        width: 45;
        height: 7;
        align: center middle;
        background: $surface;
        border: solid $primary;
    }

    PaletteNameInput #name-input {
        width: 100%;
        height: 1;
    }

    PaletteNameInput #dialog-buttons {
        width: 100%;
        height: 1;
        align-horizontal: center;
    }
    """

    # Reactive property with proper type annotation
    current_name: reactive[str] = reactive("")

    def __init__(
        self,
        current_name: str = "",
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the PaletteNameInput widget.

        Args:
            current_name: The current name of the palette
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.current_name = current_name

    def watch_current_name(self, old_name: str, new_name: str) -> None:
        """Watch for changes to the current name.

        Args:
            old_name: Previous palette name
            new_name: New palette name
        """
        # Update the input field if it exists
        try:
            name_input = self.query_one("#name-input", Input)
            name_input.value = new_name
        except Exception:
            # Widget may not be mounted yet
            pass

    def compose(self) -> ComposeResult:
        """Compose the PaletteNameInput widget."""
        # ASCII dialog frame - use correct parameter names (name and widget_id)
        yield ASCIIWidget(name="palette-name-dialog", widget_id="palette-name-dialog")

        # Input for the palette name
        yield Input(value=self.current_name, placeholder="Enter palette name", id="name-input")

        # Buttons
        with Horizontal(id="dialog-buttons"):
            yield Button("OK", id="ok-button", variant="primary")
            yield Button("Cancel", id="cancel-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events.

        Args:
            event: The button press event
        """
        button_id = event.button.id

        if button_id == "cancel-button":
            self.post_message(self.Cancelled())
        elif button_id == "ok-button":
            # Get the entered name
            name_input = self.query_one("#name-input", Input)
            new_name = name_input.value

            # Validate
            if new_name.strip():
                self.post_message(self.NameSubmitted(new_name))

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """
        Handle input submit events.

        Args:
            event: The input submit event
        """
        if event.input.id == "name-input":
            new_name = event.input.value

            # Validate
            if new_name.strip():
                self.post_message(self.NameSubmitted(new_name))

    class NameSubmitted(Message):
        """Message sent when a name is submitted."""

        def __init__(self, name: str) -> None:
            """
            Initialize the NameSubmitted message.

            Args:
                name: The submitted name
            """
            self.name = name
            super().__init__()

    class Cancelled(Message):
        """Message sent when the dialog is cancelled."""

        pass
