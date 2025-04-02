"""
Palette Management widget for managing color palettes.

This module provides UI components for managing color palettes, including
adding, renaming, and organizing color palettes.
"""

import json
import uuid
from datetime import datetime
from pathlib import Path

# Avoid circular import, use forward reference for type hints only
from typing import TYPE_CHECKING
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from typing import cast

from textual import events
from textual.app import App
from textual.app import ComposeResult
from textual.color import Color
from textual.containers import Container
from textual.containers import Horizontal
from textual.containers import Vertical
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button
from textual.widgets import Input
from textual.widgets import Static

from constants.paths import Paths


if TYPE_CHECKING:
    from widgets.palette.palette_selector import PaletteSelector

# Constants from paths
DATA_DIR = Paths.DATA_DIR
PALETTES_FILE = Paths.PALETTES_FILE


def create_empty_palette(name: str = "Untitled Palette") -> Dict[str, Any]:
    """Creates a new palette structure."""
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        # Store colors as hex strings for JSON serialization
        "colors": ["#ffffff"] * 8,
        "createdAt": datetime.now().isoformat(),
    }


class PaletteManager(App):
    """Main application class for managing palettes."""

    # List of all palettes
    palettes: reactive[List[Dict[str, Any]]] = reactive([])
    # ID of the currently active palette
    active_palette_id: reactive[Optional[str]] = reactive(None)
    # Index of the currently selected color slot (0-7)
    active_slot_index: reactive[int] = reactive(0)
    active_color: reactive[Color] = reactive(Color.parse("white"))
    # Reactive attribute for the display format
    color_format: reactive[str] = reactive("hex")  # Options: 'hex', 'rgb', 'hsl'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ensure_data_dir()
        self._load_palettes()

    def compose(self) -> ComposeResult:
        from widgets.palette.palette_selector import PaletteSelector
        yield PaletteSelector()

    def on_mount(self) -> None:
        """Set up the application when mounted."""
        from widgets.palette.palette_selector import PaletteSelector

        # Use cast to help type checker understand this is a PaletteSelector
        selector = cast(Any, self.query_one(PaletteSelector))
        # Now safely assign the palettes
        selector.palettes = self.palettes

    def add_palette(self, palette: Dict[str, Any]) -> None:
        self.palettes.append(palette)

    def get_palette(self, palette_id: str) -> Dict[str, Any]:
        return next((p for p in self.palettes if p["id"] == palette_id), {})

    def get_all_palettes(self) -> List[Dict[str, Any]]:
        return self.palettes

    def get_active_palette(self) -> Dict[str, Any]:
        return next((p for p in self.palettes if p.get("active", False)), {})

    def set_active_palette(self, palette_id: str) -> None:
        for p in self.palettes:
            p["active"] = p["id"] == palette_id

    def get_palette_by_name(self, name: str) -> Dict[str, Any]:
        return next((p for p in self.palettes if p["name"] == name), {})

    def get_palette_by_id(self, palette_id: str) -> Dict[str, Any]:
        return next((p for p in self.palettes if p["id"] == palette_id), {})

    def get_palette_by_index(self, index: int) -> Dict[str, Any]:
        if 0 <= index < len(self.palettes):
            return self.palettes[index]
        return {}

    def get_palette_count(self) -> int:
        return len(self.palettes)

    def _ensure_data_dir(self) -> None:
        """Ensure data directory exists."""
        DATA_DIR.mkdir(parents=True, exist_ok=True)

    def watch_active_color(self, old_color: Color, new_color: Color) -> None:
        """Called when active_color changes."""
        # Post a message to notify widgets or update UI directly
        self.post_message(ActiveColorChanged(new_color))

    def watch_color_format(self, old_format: str, new_format: str) -> None:
        """Called when color_format changes."""
        self.post_message(ColorFormatChanged(new_format))

    # --- Utility methods ---
    def get_color_string(self, color: Optional[Color] = None, format: Optional[str] = None) -> str:
        """Convert a color to string in the specified format."""
        color_to_use = color if color is not None else self.active_color
        format_to_use = format if format is not None else self.color_format

        if format_to_use == "hsl":
            return self._use_colorsys(color_to_use)
        elif format_to_use == "rgb":
            r, g, b = color_to_use.rgb
            return f"rgb({r}, {g}, {b})"
        else:
            return color_to_use.hex

    def _use_colorsys(self, color: Color) -> str:
        """Convert color to HSL format string."""
        # Textual Color doesn't directly expose HSL, use colorsys
        import colorsys

        r, g, b = color.normalized
        h, l, s = colorsys.rgb_to_hls(r, g, b)  # HLS! Not HSL
        # Convert HLS to HSL for display consistency if needed, or just display HLS
        # HSL: H stays same, S_hsl = S_hls / (1 - abs(2*L-1)), L_hsl = L
        # Approximate HSL display based on HLS:
        h_deg = round(h * 360)
        s_pct = round(s * 100)
        l_pct = round(l * 100)
        return f"hsl({h_deg}, {s_pct}%, {l_pct}%)"  # Displaying HLS values in HSL format string

    def is_color_dark(self, color: Optional[Color] = None) -> bool:
        """Check if a color is considered dark (for contrast)."""
        color_to_check = color if color is not None else self.active_color
        # Calculate luminance manually from RGB
        r, g, b = color_to_check.rgb
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return luminance < 0.5

    def _load_palettes(self) -> None:
        """Load palettes from JSON file."""
        if PALETTES_FILE.exists():
            try:
                with open(PALETTES_FILE, "r") as f:
                    loaded_palettes = json.load(f)
                    # Basic validation could be added here
                    self.palettes = loaded_palettes
                    if self.palettes:
                        self.active_palette_id = self.palettes[0]["id"]
                    else:
                        self._create_default_palette()
            except (json.JSONDecodeError, IOError) as e:
                self.log.error(f"Failed to load palettes: {e}")
                self._create_default_palette()
        else:
            self._create_default_palette()

    def _create_default_palette(self) -> None:
        """Create and set a default palette if none exist."""
        default_palette = create_empty_palette()
        self.palettes = [default_palette]
        self.active_palette_id = default_palette["id"]
        self._save_palettes()  # Save the initial default

    def _save_palettes(self) -> None:
        """Save palettes to JSON file."""
        try:
            with open(PALETTES_FILE, "w") as f:
                json.dump(self.palettes, f, indent=2)
        except IOError as e:
            self.log.error(f"Failed to save palettes: {e}")

    # --- Watchers to trigger saves and UI updates ---
    def watch_palettes(self, old_palettes: List[Dict[str, Any]], new_palettes: List[Dict[str, Any]]) -> None:
        """React when palettes change."""
        self._save_palettes()
        # Notify UI elements that might need refreshing
        self.post_message(PalettesChanged())

    def watch_active_palette_id(self, old_id: Optional[str], new_id: Optional[str]) -> None:
        """React when active palette changes."""
        self.post_message(ActivePaletteChanged(new_id or ""))
        # Reset active slot when palette changes? Optional.
        # self.active_slot_index = 0

    def watch_active_slot_index(self, old_index: int, new_index: int) -> None:
        """React when active slot changes."""
        self.post_message(ActiveSlotChanged(new_index))

    # --- Palette Management Methods ---
    @property
    def active_palette(self) -> Optional[Dict[str, Any]]:
        """Get the currently active palette object."""
        if not self.active_palette_id:
            return None
        return next((p for p in self.palettes if p["id"] == self.active_palette_id), None)

    def create_palette(self, name: str = "Untitled Palette") -> Dict[str, Any]:
        """Create a new empty palette."""
        new_palette = create_empty_palette(name)
        return self._duplicate_palette(new_palette)

    def update_palette(self, palette_id: str, updates: Dict[str, Any]) -> None:
        """Update an existing palette."""
        if not palette_id:
            return

        updated_list = []
        found = False
        for p in self.palettes:
            if p["id"] == palette_id:
                updated_list.append({**p, **updates})
                found = True
            else:
                updated_list.append(p)
        if found:
            self.palettes = updated_list

    def delete_palette(self, palette_id: str) -> None:
        """Delete a palette."""
        if len(self.palettes) <= 1:
            self.notify("Cannot delete the last palette.", severity="warning")
            return

        # Filter out the palette
        updated_palettes = [p for p in self.palettes if p["id"] != palette_id]
        self.palettes = updated_palettes

        # If the deleted was active, select the first remaining one
        if palette_id == self.active_palette_id:
            self.active_palette_id = self.palettes[0]["id"] if self.palettes else None

    def set_color_at_slot(self, slot_index: int, color: Color) -> None:
        """Set a color at a specific slot in the active palette."""
        if not self.active_palette or not (0 <= slot_index < 8):
            return

        # Make a copy of colors, update, then update the palette
        current_colors = list(self.active_palette["colors"])
        current_colors[slot_index] = color.hex  # Store as hex string
        self.update_palette(self.active_palette_id or "", {"colors": current_colors})

    def duplicate_palette(self, palette_id: str) -> Optional[Dict[str, Any]]:
        """Duplicate an existing palette."""
        source_palette = next((p for p in self.palettes if p["id"] == palette_id), None)
        if not source_palette:
            return None

        new_palette = {
            **source_palette,
            "id": str(uuid.uuid4()),
            "name": f"{source_palette['name']} (Copy)",
            "createdAt": datetime.now().isoformat(),
        }
        return self._duplicate_palette(new_palette)

    def _duplicate_palette(self, new_palette: Dict[str, Any]) -> Dict[str, Any]:
        """Add a new palette to the collection and set it as active."""
        self.palettes = self.palettes + [new_palette]
        self.active_palette_id = new_palette["id"]
        return new_palette


# Define custom messages for communication
class ActiveColorChanged(Message):
    """Message sent when the active color changes."""

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()


class ColorFormatChanged(Message):
    """Message sent when the color format changes."""

    def __init__(self, format: str) -> None:
        self.format = format
        super().__init__()


class PalettesChanged(Message):
    """Message sent when the palettes list changes."""
    pass


class ActivePaletteChanged(Message):
    """Message sent when the active palette changes."""

    def __init__(self, palette_id: str) -> None:
        self.palette_id = palette_id
        super().__init__()


class ActiveSlotChanged(Message):
    """Message sent when the active color slot changes."""

    def __init__(self, slot_index: int) -> None:
        self.slot_index = slot_index
        super().__init__()


class ColorSlot(Static):
    """A color slot in a palette that can display a color."""

    DEFAULT_CSS = """
    ColorSlot {
        width: 7;
        height: 3;
        content-align: center middle;
    }

    ColorSlot.active {
        border: heavy $accent;
    }
    """

    color = reactive("")
    active = reactive(False)

    def __init__(
        self,
        color: str = "",
        active: bool = False,
        id: Optional[str] = None,
        classes: Optional[str] = None
    ):
        """
        Initialize a color slot.

        Args:
            color: The color hex value
            active: If this is the active color slot
            id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__("", id=id, classes=classes)
        self.color = color
        self.active = active

    def render(self) -> str:
        """Render the color slot with its border."""
        if self.active:
            return f"┌█───█┐\n│{self.color:^5}│\n└─────┘"
        else:
            return f"┌─────┐\n│{self.color:^5}│\n└─────┘"

    def watch_color(self, color: str) -> None:
        """Update background when color changes."""
        if color:
            self.styles.background = color

    def watch_active(self, active: bool) -> None:
        """Update styling when active state changes."""
        self.refresh()
        if active:
            self.add_class("active")
        else:
            self.remove_class("active")


# Renamed to avoid conflict with imported module
class PaletteSelectorWidget(Container):
    """A palette selector widget that displays available palettes."""

    DEFAULT_CSS = """
    PaletteSelectorWidget {
        width: 100%;
        height: auto;
    }

    PaletteSelectorWidget .active-palette {
        background: $primary-darken-1;
    }
    """

    current_palette = reactive("")

    def __init__(
        self,
        palettes: Optional[List[str]] = None,
        on_select: Optional[Callable[[str], None]] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None
    ):
        """
        Initialize a palette selector.

        Args:
            palettes: List of palette names
            on_select: Callback when a palette is selected
            id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=id, classes=classes)
        self.palettes = palettes or ["Default"]
        self.on_select_callback = on_select
        self.current_palette = self.palettes[0] if self.palettes else ""

    def compose(self) -> ComposeResult:
        """Compose the palette selector with active and inactive palettes."""
        # Active palette
        palette_name = self.current_palette
        yield Static(
            f"╠════════════════╗\n├─♢ {palette_name.ljust(14)}╠",
            id="active-palette",
            classes="active-palette"
        )

        # Inactive palettes
        for palette in self.palettes:
            if palette != self.current_palette:
                yield Static(
                    f"┬───────────────┐\n├─ {palette.ljust(14)}│",
                    id=f"palette-{palette}",
                    classes="inactive-palette"
                )

    def on_click(self, event: events.Click) -> None:
        """Handle click events on palettes."""
        widget = event.widget
        if isinstance(widget, Static):
            widget_id = widget.id
            if widget_id and widget_id.startswith("palette-"):
                palette_name = widget_id[8:]  # Remove "palette-" prefix
                self.current_palette = palette_name
                if self.on_select_callback:
                    self.on_select_callback(palette_name)


class PaletteControls(Horizontal):
    """Controls for managing palettes."""

    DEFAULT_CSS = """
    PaletteControls {
        width: 100%;
        height: 1;
    }

    PaletteControls .name {
        width: 35%;
    }

    PaletteControls .controls {
        width: 65%;
        content-align: right middle;
    }
    """

    def __init__(
        self,
        palette_name: str = "Default",
        on_add: Optional[Callable[[], None]] = None,
        on_rename: Optional[Callable[[], None]] = None,
        on_delete: Optional[Callable[[], None]] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None
    ):
        """
        Initialize palette controls.

        Args:
            palette_name: Current palette name
            on_add: Callback for add action
            on_rename: Callback for rename action
            on_delete: Callback for delete action
            id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=id, classes=classes)
        self.palette_name = palette_name
        self.on_add = on_add
        self.on_rename = on_rename
        self.on_delete = on_delete

    def compose(self) -> ComposeResult:
        """Compose the palette controls UI."""
        yield Static(f"Palette: {self.palette_name}", classes="name")

        with Container(classes="controls"):
            yield Button("Add New", id="add-palette")
            yield Button("Rename", id="rename-palette")
            yield Button("Delete", id="delete-palette")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id
        if button_id == "add-palette" and self.on_add:
            self.on_add()
        elif button_id == "rename-palette" and self.on_rename:
            self.on_rename()
        elif button_id == "delete-palette" and self.on_delete:
            self.on_delete()


class PaletteNameDialog(Container):
    """Dialog for naming or renaming a palette."""

    DEFAULT_CSS = """
    PaletteNameDialog {
        width: 35;
        height: 7;
        border: solid $primary;
        background: $surface;
        align: center middle;
    }

    PaletteNameDialog .title {
        width: 100%;
        height: 1;
        text-align: center;
    }

    PaletteNameDialog .input-container {
        width: 100%;
        height: 3;
        padding: 0 1;
    }

    PaletteNameDialog .buttons {
        width: 100%;
        height: 1;
        content-align: center middle;
    }
    """

    def __init__(
        self,
        initial_name: str = "",
        on_confirm: Optional[Callable[[str], None]] = None,
        on_cancel: Optional[Callable[[], None]] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None
    ):
        """
        Initialize a palette name dialog.

        Args:
            initial_name: Initial palette name
            on_confirm: Callback for OK action with new name
            on_cancel: Callback for cancel action
            id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=id, classes=classes)
        self.initial_name = initial_name
        self.on_confirm = on_confirm
        self.on_cancel = on_cancel

    def compose(self) -> ComposeResult:
        """Compose the dialog UI."""
        yield Static("Palette Name:", classes="title")

        with Container(classes="input-container"):
            yield Input(
                value=self.initial_name,
                placeholder="Enter palette name",
                id="palette-name-input"
            )

        with Container(classes="buttons"):
            yield Button("OK", id="ok-button", variant="primary")
            yield Button("Cancel", id="cancel-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id
        if button_id == "ok-button" and self.on_confirm:
            name_input = self.query_one("#palette-name-input", Input)
            self.on_confirm(name_input.value)
        elif button_id == "cancel-button" and self.on_cancel:
            self.on_cancel()


class PaletteManagement(Container):
    """A palette management widget that manages palettes and colors."""

    DEFAULT_CSS = """
    PaletteManagement {
        width: 100%;
        height: auto;
        layout: vertical;
    }

    PaletteManagement .header {
        width: 100%;
        height: 3;
    }

    PaletteManagement .color-buttons {
        width: 100%;
        height: 3;
    }

    PaletteManagement .palette-selector {
        width: 100%;
        height: auto;
    }
    """

    current_palette = reactive("Default")
    active_color_index = reactive(0)

    def __init__(
        self,
        palettes: Optional[Dict[str, List[str]]] = None,
        id: Optional[str] = None,
        classes: Optional[str] = None
    ):
        """
        Initialize the palette management widget.

        Args:
            palettes: Dictionary of palette names to color lists
            id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=id, classes=classes)
        self.palettes = palettes or {"Default": ["#000000"] * 8}

    def compose(self) -> ComposeResult:
        """Compose the palette management UI."""
        # Header with color tools
        with Container(classes="header"):
            yield Static("╠───────────────╦", classes="header-top")
            yield Static("│ > Color Tools │", classes="header-middle")
            yield Static("╠───────────────╝", classes="header-bottom")

        # Color buttons row
        with Horizontal(classes="color-buttons"):
            colors = self.palettes.get(self.current_palette, [""] * 8)
            for i in range(8):
                is_active = (i == self.active_color_index)
                color = colors[i] if i < len(colors) else ""
                yield ColorSlot(
                    color=color,
                    active=is_active,
                    id=f"color-slot-{i}"
                )

        # Palette controls
        yield PaletteControls(
            palette_name=self.current_palette,
            on_add=self.add_palette,
            on_rename=self.rename_palette,
            on_delete=self.delete_palette,
            id="palette-controls"
        )

        # Palette selector
        yield PaletteSelectorWidget(
            palettes=list(self.palettes.keys()),
            on_select=self.select_palette,
            id="palette-selector",
            classes="palette-selector"
        )

    def on_click(self, event: events.Click) -> None:
        """Handle click events on color slots."""
        widget = event.widget
        if isinstance(widget, ColorSlot):
            widget_id = widget.id
            if widget_id and widget_id.startswith("color-slot-"):
                index = int(widget_id.split("-")[-1])
                self.active_color_index = index

    def add_palette(self) -> None:
        """Add a new palette."""
        # In a real implementation, we would show the name dialog and create a new palette
        pass

    def rename_palette(self) -> None:
        """Rename the current palette."""
        # In a real implementation, we would show the name dialog
        pass

    def delete_palette(self) -> None:
        """Delete the current palette."""
        # In a real implementation, we would show a confirmation dialog
        pass

    def select_palette(self, palette_name: str) -> None:
        """Select a palette."""
        if palette_name in self.palettes:
            self.current_palette = palette_name

    def watch_current_palette(self, old_palette: str, new_palette: str) -> None:
        """React to palette changes."""
        # Update the UI when the current palette changes
        self.refresh()

    def watch_active_color_index(self, old_index: int, new_index: int) -> None:
        """React to active color index changes."""
        # Update all color slots to reflect the active one
        for i in range(8):
            try:
                slot = self.query_one(f"#color-slot-{i}", ColorSlot)
                slot.active = (i == new_index)
            except Exception:
                pass
