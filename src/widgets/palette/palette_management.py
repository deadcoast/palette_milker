"""
Palette Management widget for managing color palettes.

This module provides UI components for managing color palettes, including
adding, renaming, and organizing color palettes.
"""

import json
import uuid
from datetime import datetime

# Avoid circular import, use forward reference for type hints only
from typing import TYPE_CHECKING
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import cast

from textual import events
from textual.app import App
from textual.app import ComposeResult
from textual.color import Color
from textual.containers import Container
from textual.containers import Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Static

from constants.paths import Paths


if TYPE_CHECKING:
    pass

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
    palettes: reactive[List[Dict[str, Any]]] = reactive([], always_update=True, repaint=True)
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
        from .palette_widget import PaletteSelector

        yield PaletteSelector()

    def on_mount(self) -> None:
        """Set up the application when mounted."""
        from .palette_widget import PaletteSelector

        # Use cast to help type checker understand this is a PaletteSelector
        selector = cast(Any, self.query_one(PaletteSelector))
        # Now safely assign the palettes
        selector.palettes = self.palettes

    def add_palette(self, palette: Dict[str, Any]) -> None:
        """Add a palette to the collection.

        Args:
            palette: The palette to add
        """
        # Create a copy of the current palettes list
        updated_palettes = self.palettes.copy()
        updated_palettes.append(palette)
        # Set the entire list to trigger the watcher
        self.palettes = updated_palettes

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
        return self.palettes[index] if 0 <= index < len(self.palettes) else {}

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
    def get_color_string(self, color: Optional[Color] = None, color_format: Optional[str] = None) -> str:
        """Convert a color to string in the specified format."""
        color_to_use = color if color is not None else self.active_color
        format_to_use = color_format if color_format is not None else self.color_format

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
        h, lightness, s = colorsys.rgb_to_hls(r, g, b)  # HLS! Not HSL
        # Convert HLS to HSL for display consistency if needed, or just display HLS
        # HSL: H stays same, S_hsl = S_hls / (1 - abs(2*L-1)), L_hsl = L
        # Approximate HSL display based on HLS:
        h_deg = round(h * 360)
        s_pct = round(s * 100)
        l_pct = round(lightness * 100)
        return f"hsl({h_deg}, {s_pct}%, {l_pct}%)"  # Displaying HLS values in HSL format string

    def is_color_dark(self, color: Optional[Color] = None) -> bool:
        """Check if a color is considered dark (for contrast)."""
        color_to_check = color if color is not None else self.active_color
        # Calculate luminance manually from RGB
        r, g, b = color_to_check.rgb
        return 0.299 * r + 0.587 * g + 0.114 * b < 127.5

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

    def watch_active_color_index(self, old_index: int, new_index: int) -> None:
        """Watch for changes to the active color index."""
        # Update the UI when active color index changes
        if old_index != new_index:
            # Get all color slots first, before the loop
            # This avoids using try-except inside the loop
            color_slots = {}

            # Query all slots at once to avoid repeated queries in the loop
            for slot in self.query(ColorSlot):
                if slot.id is not None and slot.id.startswith("color-slot-"):
                    try:
                        # Extract the index from the ID
                        slot_idx = int(slot.id.replace("color-slot-", ""))
                        color_slots[slot_idx] = slot
                    except ValueError:
                        # Skip slots with invalid IDs
                        pass

            # Now update only the slots that exist
            for i in range(8):
                if i in color_slots:
                    color_slots[i].active = i == new_index

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
        """Update an existing palette.

        Args:
            palette_id: ID of the palette to update
            updates: Dictionary of fields to update
        """
        if not palette_id:
            return

        updated_palettes = []
        found = False
        for p in self.palettes:
            if p["id"] == palette_id:
                # Create a new dictionary with updated values
                updated_palette = {**p, **updates}
                updated_palettes.append(updated_palette)
                found = True
            else:
                # Keep original unchanged palettes
                updated_palettes.append(p.copy())

        if found:
            # Set the entire list to trigger the watcher
            self.palettes = updated_palettes

    def delete_palette(self, palette_id: str) -> None:
        """Delete a palette.

        Args:
            palette_id: ID of the palette to delete
        """
        if len(self.palettes) <= 1:
            self.notify("Cannot delete the last palette.", severity="warning")
            return

        # Filter out the palette and create a new list
        updated_palettes = [p.copy() for p in self.palettes if p["id"] != palette_id]

        # If the deleted was active, select the first remaining one
        if palette_id == self.active_palette_id:
            # Update the reactive property after setting palettes
            new_active_id = updated_palettes[0]["id"] if updated_palettes else None
            self.palettes = updated_palettes
            self.active_palette_id = new_active_id
        else:
            # Just update the palettes list
            self.palettes = updated_palettes

    def set_color_at_slot(self, slot_index: int, color: Color) -> None:
        """Set a color at a specific slot in the active palette.

        Args:
            slot_index: Index of the slot to update (0-7)
            color: New color to set
        """
        active_palette = self.active_palette
        if not active_palette or not (0 <= slot_index < 8):
            return

        # Make a copy of the active palette
        palette_copy = {**active_palette}

        # Make a copy of colors, update the specific slot
        current_colors = list(palette_copy["colors"])
        current_colors[slot_index] = color.hex  # Store as hex string

        # Update the colors in the palette copy
        palette_copy["colors"] = current_colors

        # Update the palette using the copy
        self.update_palette(self.active_palette_id or "", palette_copy)

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
        """Add a new palette to the collection and set it as active.

        Args:
            new_palette: The new palette to add

        Returns:
            The newly added palette
        """
        # Create a copy of the current palettes list
        updated_palettes = [p.copy() for p in self.palettes]

        # Add the new palette
        updated_palettes.append(new_palette)

        # Update both reactive properties
        self.palettes = updated_palettes
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

    def __init__(self, color_format: str) -> None:
        self.color_format = color_format
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
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize a ColorSlot.

        Args:
            color: The color to display (hex format)
            active: Whether the slot is active
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
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


class PaletteControls(Horizontal):
    """Controls for managing palettes."""

    DEFAULT_CSS = """
    PaletteControls {
        width: 100%;
        height: 3;
    }
    """

    def __init__(
        self,
        palette_name: str = "Default",
        on_add: Optional[Callable[[], None]] = None,
        on_rename: Optional[Callable[[], None]] = None,
        on_delete: Optional[Callable[[], None]] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize PaletteControls.

        Args:
            palette_name: Name of the currently active palette
            on_add: Callback for add button
            on_rename: Callback for rename button
            on_delete: Callback for delete button
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
        self.palette_name = palette_name
        self.on_add = on_add
        self.on_rename = on_rename
        self.on_delete = on_delete


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
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize PaletteSelectorWidget.

        Args:
            palettes: List of palette names
            on_select: Callback when a palette is selected
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
        self.palettes = palettes or []
        self.on_select = on_select

    def compose(self) -> ComposeResult:
        """Compose the palette selector with active and inactive palettes."""
        # Active palette
        palette_name = self.current_palette
        yield Static(
            f"╠════════════════╗\n├─♢ {palette_name.ljust(14)}╠", id="active-palette", classes="active-palette"
        )

        # Inactive palettes
        for palette in self.palettes:
            if palette != self.current_palette:
                yield Static(
                    f"┬───────────────┐\n├─ {palette.ljust(14)}│", id=f"palette-{palette}", classes="inactive-palette"
                )

    def on_click(self, event: events.Click) -> None:
        """Handle click events on palettes."""
        widget = event.widget
        if isinstance(widget, Static):
            widget_id = widget.id
            if widget_id and widget_id.startswith("palette-"):
                palette_name = widget_id[8:]  # Remove "palette-" prefix
                self.current_palette = palette_name
                if self.on_select:
                    self.on_select(palette_name)


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

    # Reactive properties defined at class level, following Textual best practices
    palette_id: reactive[str] = reactive("")
    palette_name: reactive[str] = reactive("Default")
    palette_colors: reactive[List[str]] = reactive(["#000000"] * 8)
    active_color_index: reactive[int] = reactive(0)

    def __init__(
        self,
        *,  # Force keyword arguments for clarity
        palette_id: Optional[str] = None,
        palette_name: Optional[str] = None,
        colors: Optional[List[str]] = None,
        active_color_index: Optional[int] = None,
        palettes: Optional[Dict[str, List[str]]] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the palette management widget.

        Args:
            palette_id: ID of the active palette
            palette_name: Name of the active palette
            colors: List of colors in the active palette
            active_color_index: Index of the active color
            palettes: Dictionary of palette names to color lists
            widget_id: Widget ID
            classes: CSS classes
        """
        super().__init__(id=widget_id, classes=classes)

        # Set reactive properties if provided
        if palette_id is not None:
            self.palette_id = palette_id
        if palette_name is not None:
            self.palette_name = palette_name
        if colors is not None:
            self.palette_colors = colors.copy() if colors else ["#000000"] * 8
        if active_color_index is not None:
            self.active_color_index = active_color_index

        # Initialize other properties
        self.palettes = palettes or {self.palette_name: self.palette_colors.copy()}

    def compose(self) -> ComposeResult:
        """Compose the palette management UI."""
        # Header with color tools
        with Container(classes="header"):
            yield Static("╠───────────────╦", classes="header-top")
            yield Static("│ > Color Tools │", classes="header-middle")
            yield Static("╠───────────────╝", classes="header-bottom")

        # Color buttons row
        with Horizontal(classes="color-buttons"):
            for i in range(8):
                is_active = i == self.active_color_index
                color = self.palette_colors[i] if i < len(self.palette_colors) else ""
                yield ColorSlot(color=color, active=is_active, widget_id=f"color-slot-{i}")

        # Palette controls
        yield PaletteControls(
            palette_name=self.palette_name,
            on_add=self.add_palette,
            on_rename=self.rename_palette,
            on_delete=self.delete_palette,
            widget_id="palette-controls",
        )

        # Palette selector
        yield PaletteSelectorWidget(
            palettes=list(self.palettes.keys()),
            on_select=self.select_palette,
            widget_id="palette-selector",
            classes="palette-selector",
        )

    def on_mount(self) -> None:
        """Handle widget mount event."""
        # Initialize any additional state here
        pass

    def on_click(self, event: events.Click) -> None:
        """Handle click events on color slots."""
        widget = event.widget
        if isinstance(widget, ColorSlot):
            widget_id = widget.id
            if widget_id and widget_id.startswith("color-slot-"):
                index = int(widget_id.split("-")[-1])
                self.active_color_index = index
                # Post a message to notify about color selection change
                from ...messages.palette_messages import ColorSelectionChanged

                self.post_message(ColorSelectionChanged(self, index, self.palette_colors[index]))

    # Watchers for reactive properties
    def watch_palette_name(self, old_name: str, new_name: str) -> None:
        """Watch for changes to the palette name."""
        # Update the UI when palette name changes
        if old_name != new_name:
            # Update the palette controls
            palette_controls = self.query_one("#palette-controls", PaletteControls)
            palette_controls.palette_name = new_name

            # Ensure the palette exists in palettes dictionary
            if new_name not in self.palettes:
                self.palettes[new_name] = self.palette_colors.copy()

            # Post a message about the palette change
            from ...messages.palette_messages import PaletteUpdated

            self.post_message(PaletteUpdated(self, self.palette_id))

    def watch_palette_colors(self, old_colors: List[str], new_colors: List[str]) -> None:
        """Watch for changes to the palette colors."""
        # Update the UI when colors change
        if old_colors != new_colors:
            # Update the color slots
            for i, color in enumerate(new_colors):
                if i < 8:  # Limit to 8 colors
                    slot = self.query_one(f"#color-slot-{i}", ColorSlot)
                    slot.color = color

            # Update the palette in the palettes dictionary
            if self.palette_name in self.palettes:
                self.palettes[self.palette_name] = new_colors.copy()

            # Post a message about the palette change
            from ...messages.palette_messages import PaletteUpdated

            self.post_message(PaletteUpdated(self, self.palette_id))

    def watch_active_color_index(self, old_index: int, new_index: int) -> None:
        """Watch for changes to the active color index."""
        # Update the UI when active color index changes
        if old_index != new_index:
            # Get all color slots first, before the loop
            # This avoids using try-except inside the loop
            color_slots = {}

            # Query all slots at once to avoid repeated queries in the loop
            for slot in self.query(ColorSlot):
                if slot.id is not None and slot.id.startswith("color-slot-"):
                    try:
                        # Extract the index from the ID
                        slot_idx = int(slot.id.replace("color-slot-", ""))
                        color_slots[slot_idx] = slot
                    except ValueError:
                        # Skip slots with invalid IDs
                        pass

            # Now update only the slots that exist
            for i in range(8):
                if i in color_slots:
                    color_slots[i].active = i == new_index

    def update_palette(
        self,
        palette_id: Optional[str] = None,
        palette_name: Optional[str] = None,
        colors: Optional[List[str]] = None,
        active_color_index: Optional[int] = None,
    ) -> None:
        """
        Update the palette management widget with new data.

        Args:
            palette_id: ID of the active palette
            palette_name: Name of the active palette
            colors: List of colors in the active palette
            active_color_index: Index of the active color
        """
        if palette_id is not None:
            self.palette_id = palette_id

        if palette_name is not None:
            self.palette_name = palette_name

        if colors is not None:
            self.palette_colors = colors.copy() if colors else ["#000000"] * 8

        if active_color_index is not None:
            self.active_color_index = active_color_index

    def add_palette(self) -> None:
        """Add a new palette."""
        # Create a new palette name
        new_name = f"New Palette {len(self.palettes)}"

        # Create a new palette with default colors
        self.palettes[new_name] = ["#FFFFFF"] * 8

        # Set as current
        self.palette_name = new_name
        self.palette_colors = self.palettes[new_name].copy()
        self.active_color_index = 0

        # Post a message about the new palette
        from ...messages.palette_messages import PaletteCreated

        self.post_message(PaletteCreated(self, self.palette_id, new_name))

    def rename_palette(self) -> None:
        """Rename the current palette."""
        # In a real implementation, we would show a dialog
        # For now, just append " (Renamed)" to the current name
        new_name = f"{self.palette_name} (Renamed)"

        # Update the palettes dictionary
        if self.palette_name in self.palettes:
            colors = self.palettes.pop(self.palette_name)
            self.palettes[new_name] = colors

            # Update the reactive property
            self.palette_name = new_name

            # Post a message about the renamed palette
            from ...messages.palette_messages import PaletteUpdated

            self.post_message(PaletteUpdated(self, self.palette_id))

    def delete_palette(self) -> None:
        """Delete the current palette."""
        # Ensure we don't delete the last palette
        if len(self.palettes) <= 1:
            return

        # Remove the current palette
        if self.palette_name in self.palettes:
            self.palettes.pop(self.palette_name)

            # Set a new active palette
            new_name = next(iter(self.palettes.keys()))
            self.palette_name = new_name
            self.palette_colors = self.palettes[new_name].copy()
            self.active_color_index = 0

            # Post a message about the deleted palette
            from ...messages.palette_messages import PaletteDeleted

            self.post_message(PaletteDeleted(self, self.palette_id))

    def select_palette(self, palette_name: str) -> None:
        """Select a palette."""
        if palette_name in self.palettes:
            self.palette_name = palette_name
            self.palette_colors = self.palettes[palette_name].copy()
            self.active_color_index = 0

            # Post a message about the selected palette
            from ...messages.palette_messages import PaletteSelectionChanged

            self.post_message(PaletteSelectionChanged(self, self.palette_id))
