"""
Palette management widgets for the Milky Color Suite.

This module contains widgets for managing color palettes,
implementing the exact terminal-based UI design specified.
"""

import uuid
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from colour import Color
from rich.console import Console
from rich.console import RenderableType
from rich.style import Style
from rich.text import Text
from textual import events
from textual.app import ComposeResult
from textual.containers import Container
from textual.containers import Horizontal
from textual.containers import Vertical
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button
from textual.widgets import Input
from textual.widgets import Static

from constants.patterns import PATTERNS
from constants.patterns import create_button
from constants.patterns import create_color_button
from constants.patterns import create_palette_group
from constants.patterns import create_text_input
from widgets.ascii_widget import ASCIIWidget
from .palette_manager import PaletteManager


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

    # Reactive properties
    palettes = reactive([])
    active_palette_id = reactive("")

    def __init__(
        self,
        palettes: List[Dict[str, Any]] = None,
        active_palette_id: str = None,
        name: str = None,
        id: str = None,
        classes: str = None,
    ):
        """Initialize the palette selector.

        Args:
            palettes: List of palette dictionaries
            active_palette_id: ID of the active palette
            name: Widget name
            id: Widget ID
            classes: CSS classes
        """
        super().__init__(name=name, id=id, classes=classes)
        if palettes:
            self.palettes = palettes
        if active_palette_id:
            self.active_palette_id = active_palette_id

    def compose(self) -> ComposeResult:
        """Compose the palette selector with palette buttons."""
        for palette in self.palettes:
            yield PaletteButton(palette=palette, active=palette["id"] == self.active_palette_id)

        # Add a new palette button
        yield TransparentButton(ascii_pattern=PATTERNS["ADD_BUTTON"], id="add-palette")

    def on_mount(self) -> None:
        """Handle widget mounting."""
        self.add_class("palette-selector")

    def watch_palettes(self, palettes: List[Dict[str, Any]]) -> None:
        """Watch for changes to the palettes list."""
        self.remove_children()
        self.mount_all(self._make_buttons())

    def watch_active_palette_id(self, active_id: str) -> None:
        """Watch for changes to the active palette ID."""
        for child in self.query(PaletteButton):
            if isinstance(child, PaletteButton):
                child.active = child.palette["id"] == active_id

    def _make_buttons(self) -> List[Widget]:
        """Create palette buttons from the palettes list."""
        buttons = [
            PaletteButton(palette=palette, active=palette["id"] == self.active_palette_id) for palette in self.palettes
        ]

        # Add a new palette button
        buttons.append(TransparentButton(ascii_pattern=PATTERNS["ADD_BUTTON"], id="add-palette"))

        return buttons

    def on_add_palette_button_pressed(self, event: TransparentButton.Pressed) -> None:
        """Handle the add palette button being pressed."""
        if event.sender.id == "add-palette":
            self.post_message(self.AddPalette())

    def on_palette_button_pressed(self, event: "PaletteButton.Pressed") -> None:
        """Handle a palette button being pressed."""
        self.post_message(self.PaletteSelected(event.sender.palette["id"]))

    # Custom messages
    class PaletteSelected(events.Message):
        """Event sent when a palette is selected."""

        def __init__(self, palette_id: str) -> None:
            """Initialize a palette selected message.

            Args:
                palette_id: ID of the selected palette
            """
            self.palette_id = palette_id
            super().__init__()

    class AddPalette(events.Message):
        """Event sent when the add palette button is pressed."""

        def __init__(self) -> None:
            """Initialize an add palette message."""
            super().__init__()


class PaletteButton(TransparentButton):
    """Button for selecting a palette."""

    # Reactive properties
    palette = reactive({"id": "", "name": "", "colors": []})

    def __init__(
        self, palette: Dict[str, Any], active: bool = False, name: str = None, id: str = None, classes: str = None
    ):
        """Initialize a palette button.

        Args:
            palette: Palette dictionary
            active: Whether the button is active
            name: Widget name
            id: Widget ID
            classes: CSS classes
        """
        pattern = PATTERNS["PALETTE_BUTTON"]["ACTIVE" if active else "DEFAULT"]
        super().__init__(ascii_pattern=pattern, active=active, name=name, id=id, classes=classes)
        self.palette = palette

    def render(self):
        """Render the palette button with the palette name."""
        pattern = PATTERNS["PALETTE_BUTTON"]["ACTIVE" if self.active else "DEFAULT"]

        # Create a text with the pattern and replace a placeholder with the name
        text = Text.from_markup(pattern)
        return text

    def on_click(self, event: events.Click) -> None:
        """Handle the button being clicked."""
        self.post_message(self.Pressed(self))


class ColorSlots(TransparentWidget):
    """Widget for displaying and selecting color slots."""

    DEFAULT_CSS = """
    ColorSlots {
        width: 100%;
        height: auto;
        layout: horizontal;
        background: $surface;
    }
    """

    # Reactive properties
    colors = reactive(["#FFFFFF"] * 8)
    active_slot_index = reactive(0)

    def __init__(
        self,
        colors: List[str] = None,
        active_slot_index: int = 0,
        name: str = None,
        id: str = None,
        classes: str = None,
    ):
        """Initialize the color slots widget.

        Args:
            colors: List of color strings
            active_slot_index: Index of the active slot
            name: Widget name
            id: Widget ID
            classes: CSS classes
        """
        super().__init__(ascii_pattern=PATTERNS["PALETTE_AREA"], interactive=False, name=name, id=id, classes=classes)
        if colors:
            self.colors = colors
        self.active_slot_index = active_slot_index

    def compose(self) -> ComposeResult:
        """Compose the color slots."""
        for i, color in enumerate(self.colors):
            yield ColorSlot(color=color, index=i, active=i == self.active_slot_index)

    def watch_colors(self, colors: List[str]) -> None:
        """Watch for changes to the colors list."""
        for i, color in enumerate(colors):
            if i < len(self.query(ColorSlot)):
                slot = self.query(ColorSlot)[i]
                slot.color = color

    def watch_active_slot_index(self, index: int) -> None:
        """Watch for changes to the active slot index."""
        for slot in self.query(ColorSlot):
            slot.active = slot.index == index

    def on_color_slot_clicked(self, event: "ColorSlot.Clicked") -> None:
        """Handle a color slot being clicked."""
        self.post_message(self.SlotSelected(event.sender.index))

    def on_color_slot_double_clicked(self, event: "ColorSlot.DoubleClicked") -> None:
        """Handle a color slot being double-clicked."""
        self.post_message(self.SlotDoubleClicked(event.sender.index))

    # Custom messages
    class SlotSelected(events.Message):
        """Event sent when a slot is selected."""

        def __init__(self, slot_index: int) -> None:
            """Initialize a slot selected message.

            Args:
                slot_index: Index of the selected slot
            """
            self.slot_index = slot_index
            super().__init__()

    class SlotDoubleClicked(events.Message):
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

    # Reactive properties
    color = reactive("#FFFFFF")
    index = reactive(0)
    active = reactive(False)

    def __init__(
        self,
        color: str = "#FFFFFF",
        index: int = 0,
        active: bool = False,
        name: str = None,
        id: str = None,
        classes: str = None,
    ):
        """Initialize a color slot.

        Args:
            color: Color string
            index: Slot index
            active: Whether the slot is active
            name: Widget name
            id: Widget ID
            classes: CSS classes
        """
        super().__init__(name=name, id=id, classes=classes)
        self.color = color
        self.index = index
        self.active = active

    def on_mount(self) -> None:
        """Handle widget mounting."""
        if self.active:
            self.add_class("active")

    def watch_active(self, active: bool) -> None:
        """Watch for changes to the active state."""
        if active:
            self.add_class("active")
        else:
            self.remove_class("active")

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
    class Clicked(events.Message):
        """Event sent when the slot is clicked."""

        def __init__(self, sender: "ColorSlot") -> None:
            """Initialize a clicked message.

            Args:
                sender: The slot that was clicked
            """
            self.sender = sender
            super().__init__()

    class DoubleClicked(events.Message):
        """Event sent when the slot is double-clicked."""

        def __init__(self, sender: "ColorSlot") -> None:
            """Initialize a double-clicked message.

            Args:
                sender: The slot that was double-clicked
            """
            self.sender = sender
            super().__init__()


class ColorSlots(Container):
    """
    A container of color slots for a palette.

    This widget displays a row of color slots, with one active slot
    that can be selected by the user.
    """

    DEFAULT_CSS = """
    ColorSlots {
        layout: horizontal;
        height: 3;
        width: auto;
    }

    ColorSlots > .slot {
        width: 7;
        height: 3;
        margin: 0 1 0 0;
    }

    ColorSlots > .slot.active {
        color: $accent;
    }
    """

    colors: reactive[List[str]] = reactive(["#FFFFFF"] * 8)
    active_index: reactive[int] = reactive(0)

    def __init__(
        self,
        colors: Optional[List[str]] = None,
        active_index: int = 0,
        name: Optional[str] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ColorSlots widget.

        Args:
            colors: List of colors (hex strings)
            active_index: Index of the active color slot
            name: The name of the widget
            id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=id, classes=classes)
        if colors is not None:
            # Ensure we have exactly 8 colors
            self.colors = (colors + ["#FFFFFF"] * 8)[:8]
        else:
            self.colors = ["#FFFFFF"] * 8
        self.active_index = active_index

    def compose(self) -> ComposeResult:
        """Compose the ColorSlots widget."""
        # Create a slot for each color
        for i, color in enumerate(self.colors):
            active = i == self.active_index
            yield ASCIIWidget(
                ascii_pattern=create_color_button(color, active),
                id=f"slot-{i}",
                classes=f"slot {'active' if active else ''}",
            )

    def watch_active_index(self, active_index: int) -> None:
        """
        Watch for changes to the active index.

        Args:
            active_index: The new active index
        """
        # Update the active state of all slots
        for i in range(8):
            slot = self.query_one(f"#slot-{i}", ASCIIWidget)
            if i == active_index:
                slot.update_pattern(create_color_button(self.colors[i], True))
                slot.add_class("active")
            else:
                slot.update_pattern(create_color_button(self.colors[i], False))
                slot.remove_class("active")

    def watch_colors(self, colors: List[str]) -> None:
        """
        Watch for changes to the colors.

        Args:
            colors: The new colors
        """
        # Update the pattern of each slot
        for i, color in enumerate(colors):
            slot = self.query_one(f"#slot-{i}", ASCIIWidget)
            active = i == self.active_index
            slot.update_pattern(create_color_button(color, active))

    def on_click(self, event: events.Click) -> None:
        """
        Handle click events.

        Args:
            event: The click event
        """
        # Determine which slot was clicked
        target = event.target
        if isinstance(target, ASCIIWidget) and "slot" in target.classes:
            # Extract the index from the ID
            index = int(target.id.split("-")[1])

            # Update the active index
            self.active_index = index

            # Notify of slot selection
            self.post_message(self.SlotSelected(index, self.colors[index]))

    def update_color(self, index: int, color: str) -> None:
        """
        Update a specific color in the palette.

        Args:
            index: The index of the color to update
            color: The new color (hex string)
        """
        if 0 <= index < len(self.colors):
            colors = self.colors.copy()
            colors[index] = color
            self.colors = colors

    class SlotSelected(Message):
        """Message sent when a color slot is selected."""

        def __init__(self, index: int, color: str) -> None:
            """
            Initialize the SlotSelected message.

            Args:
                index: The index of the selected slot
                color: The color of the selected slot
            """
            self.index = index
            self.color = color
            super().__init__()


class PaletteSelector(Container):
    """
    A widget for selecting and managing palettes.

    This widget displays a selector for choosing between different palettes,
    as well as buttons for adding, renaming, and deleting palettes.
    """

    DEFAULT_CSS = """
    PaletteSelector {
        width: 100%;
        height: auto;
    }

    PaletteSelector .header {
        width: 100%;
        height: 1;
    }

    PaletteSelector .palette-tabs {
        width: 100%;
        height: 3;
    }

    PaletteSelector .palette-tab {
        width: auto;
        height: 3;
        margin: 0 1 0 0;
    }

    PaletteSelector .palette-tab.active {
        color: $accent;
    }

    PaletteSelector .palette-actions {
        width: auto;
        height: 1;
        dock: right;
    }
    """

    palettes: reactive[List[Dict[str, Any]]] = reactive([])
    active_palette_id: reactive[str] = reactive("")

    def __init__(
        self,
        palettes: Optional[List[Dict[str, Any]]] = None,
        active_palette_id: Optional[str] = None,
        name: Optional[str] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the PaletteSelector widget.

        Args:
            palettes: List of palette dictionaries
            active_palette_id: ID of the active palette
            name: The name of the widget
            id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=id, classes=classes)

        # Create a default palette if none provided
        if not palettes:
            palettes = [{"id": str(uuid.uuid4()), "name": "Default", "colors": ["#FFFFFF"] * 8}]

        self.palettes = palettes

        # Set the active palette ID (default to first palette)
        if active_palette_id and any(p["id"] == active_palette_id for p in palettes):
            self.active_palette_id = active_palette_id
        else:
            self.active_palette_id = palettes[0]["id"]

    def compose(self) -> ComposeResult:
        """Compose the PaletteSelector widget."""
        # Header with palette name and actions
        with Horizontal(classes="header"):
            active_palette = self.get_active_palette()
            yield Static(f"Palette: {active_palette['name']}", id="palette-name")

            with Horizontal(classes="palette-actions"):
                yield Button("Add New", id="add-palette-button", classes="action")
                yield Button("Rename", id="rename-palette-button", classes="action")
                yield Button("Delete", id="delete-palette-button", classes="action")

        # Palette tabs
        with Horizontal(classes="palette-tabs"):
            for palette in self.palettes:
                active = palette["id"] == self.active_palette_id
                yield ASCIIWidget(
                    ascii_pattern=create_palette_group(text=palette["name"][:10], active=active),  # Truncate long names
                    id=f"palette-tab-{palette['id']}",
                    classes=f"palette-tab {'active' if active else ''}",
                )

    def get_active_palette(self) -> Dict[str, Any]:
        """
        Get the active palette.

        Returns:
            The active palette dictionary
        """
        for palette in self.palettes:
            if palette["id"] == self.active_palette_id:
                return palette

        # Fallback if active palette not found
        return self.palettes[0]

    def watch_active_palette_id(self, active_palette_id: str) -> None:
        """
        Watch for changes to the active palette ID.

        Args:
            active_palette_id: The new active palette ID
        """
        # Update the active state of all palette tabs
        for palette in self.palettes:
            tab_id = f"palette-tab-{palette['id']}"
            if tab_id in self.query_one(".palette-tabs").query_dict:
                tab = self.query_one(f"#{tab_id}", ASCIIWidget)
                active = palette["id"] == active_palette_id
                tab.update_pattern(create_palette_group(text=palette["name"][:10], active=active))
                if active:
                    tab.add_class("active")
                else:
                    tab.remove_class("active")

        # Update the palette name in the header
        active_palette = self.get_active_palette()
        self.query_one("#palette-name", Static).update(f"Palette: {active_palette['name']}")

        # Notify of palette selection
        self.post_message(self.PaletteSelected(active_palette["id"], active_palette["name"], active_palette["colors"]))

    def watch_palettes(self, palettes: List[Dict[str, Any]]) -> None:
        """
        Watch for changes to the palettes.

        Args:
            palettes: The new palettes
        """
        # Refresh the entire component
        self.refresh()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events.

        Args:
            event: The button press event
        """
        button_id = event.button.id

        if button_id == "add-palette-button":
            self.post_message(self.AddPalette())
        elif button_id == "rename-palette-button":
            self.post_message(self.RenamePalette(self.active_palette_id))
        elif button_id == "delete-palette-button":
            self.post_message(self.DeletePalette(self.active_palette_id))

    def on_click(self, event: events.Click) -> None:
        """
        Handle click events.

        Args:
            event: The click event
        """
        # Check if a palette tab was clicked
        target = event.target
        if isinstance(target, ASCIIWidget) and "palette-tab" in target.classes:
            # Extract the palette ID from the tab ID
            palette_id = target.id.split("-")[-1]

            # Set the active palette ID
            self.active_palette_id = palette_id

    def add_palette(self, name: str, colors: Optional[List[str]] = None) -> str:
        """
        Add a new palette.

        Args:
            name: The name of the new palette
            colors: The colors for the new palette

        Returns:
            The ID of the new palette
        """
        if not colors:
            colors = ["#FFFFFF"] * 8

        # Create new palette
        new_id = str(uuid.uuid4())
        new_palette = {"id": new_id, "name": name, "colors": colors}

        # Add to palettes
        palettes = self.palettes.copy()
        palettes.append(new_palette)
        self.palettes = palettes

        # Set as active
        self.active_palette_id = new_id

        return new_id

    def rename_palette(self, palette_id: str, new_name: str) -> bool:
        """
        Rename a palette.

        Args:
            palette_id: The ID of the palette to rename
            new_name: The new name for the palette

        Returns:
            True if the palette was renamed, False otherwise
        """
        palettes = self.palettes.copy()
        for i, palette in enumerate(palettes):
            if palette["id"] == palette_id:
                palettes[i] = {**palette, "name": new_name}
                self.palettes = palettes
                return True

        return False

    def delete_palette(self, palette_id: str) -> bool:
        """
        Delete a palette.

        Args:
            palette_id: The ID of the palette to delete

        Returns:
            True if the palette was deleted, False otherwise
        """
        # Don't delete the last palette
        if len(self.palettes) <= 1:
            return False

        palettes = self.palettes.copy()
        for i, palette in enumerate(palettes):
            if palette["id"] == palette_id:
                # Remove the palette
                palettes.pop(i)

                # Update the active palette ID if needed
                if palette_id == self.active_palette_id:
                    self.active_palette_id = palettes[0]["id"]

                self.palettes = palettes
                return True

        return False

    def update_palette_colors(self, palette_id: str, colors: List[str]) -> bool:
        """
        Update the colors of a palette.

        Args:
            palette_id: The ID of the palette to update
            colors: The new colors for the palette

        Returns:
            True if the palette was updated, False otherwise
        """
        palettes = self.palettes.copy()
        for i, palette in enumerate(palettes):
            if palette["id"] == palette_id:
                palettes[i] = {**palette, "colors": colors}
                self.palettes = palettes
                return True

        return False

    class PaletteSelected(Message):
        """Message sent when a palette is selected."""

        def __init__(self, palette_id: str, name: str, colors: List[str]) -> None:
            """
            Initialize the PaletteSelected message.

            Args:
                palette_id: The ID of the selected palette
                name: The name of the selected palette
                colors: The colors of the selected palette
            """
            self.palette_id = palette_id
            self.name = name
            self.colors = colors
            super().__init__()

    class AddPalette(Message):
        """Message sent when the add palette button is pressed."""

        pass

    class RenamePalette(Message):
        """Message sent when the rename palette button is pressed."""

        def __init__(self, palette_id: str) -> None:
            """
            Initialize the RenamePalette message.

            Args:
                palette_id: The ID of the palette to rename
            """
            self.palette_id = palette_id
            super().__init__()

    class DeletePalette(Message):
        """Message sent when the delete palette button is pressed."""

        def __init__(self, palette_id: str) -> None:
            """
            Initialize the DeletePalette message.

            Args:
                palette_id: The ID of the palette to delete
            """
            self.palette_id = palette_id
            super().__init__()


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

    current_name: reactive[str] = reactive("")

    def __init__(
        self,
        current_name: str = "",
        name: Optional[str] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the PaletteNameInput widget.

        Args:
            current_name: The current name of the palette
            name: The name of the widget
            id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=id, classes=classes)
        self.current_name = current_name

    def compose(self) -> ComposeResult:
        """Compose the PaletteNameInput widget."""
        # ASCII dialog frame
        yield ASCIIWidget(
            ascii_pattern="""┌─────────────────────────────────────┐
│ Palette Name:                       │
│ ┌─────────────────────────────────┐ │
│ │ ~name:\\>                        │ │
│ └─────────────────────────────────┘ │
│ [OK] [CANCEL]                       │
└─────────────────────────────────────┘""",
            id="palette-name-dialog",
        )

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
