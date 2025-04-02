
## Step 3: Palette Management System

### Overview

This phase implements the palette management system, allowing users to create, save, and organize color palettes using Textual widgets and Python data structures, persisting data to the file system.

### Prerequisites

* Completed Step 1 & 2 (Python/Textual)
* Understanding of Textual state management and messaging
* Familiarity with Python data structures (lists, dicts) and file I/O (JSON)

### Implementation Tasks

#### 3.1 Palette State Management (Textual Approach)

Manage palette state within the main App or Screen class using reactive attributes and potentially custom messages.

```python
# milky_color_suite/app.py (or main_screen.py)
import json
import uuid
from pathlib import Path
from textual.app import App, ComposeResult # ... other imports
from textual.reactive import reactive
from textual.color import Color

# Define data path
DATA_DIR = Path(__file__).parent / "data"
PALETTES_FILE = DATA_DIR / "palettes.json"

def create_empty_palette(name="Untitled Palette") -> dict:
    """Creates a new palette structure."""
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        # Store colors as hex strings for JSON serialization
        "colors": ["#ffffff"] * 8,
        "createdAt": datetime.now().isoformat(), # Use datetime
    }

class MilkyColorSuiteApp(App): # Or within your MainScreen class
    # ... other reactive attributes (active_color, color_format) ...

    # List of all palettes
    palettes = reactive([])
    # ID of the currently active palette
    active_palette_id = reactive(None)
    # Index of the currently selected color slot (0-7)
    active_slot_index = reactive(0)

    def __init__(self):
        super().__init__()
        self._ensure_data_dir()
        self._load_palettes()

    def _ensure_data_dir(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)

    def _load_palettes(self):
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

    def _create_default_palette(self):
        """Create and set a default palette if none exist."""
        default_palette = create_empty_palette()
        self.palettes = [default_palette]
        self.active_palette_id = default_palette["id"]
        self._save_palettes() # Save the initial default

    def _save_palettes(self):
        """Save palettes to JSON file."""
        try:
            with open(PALETTES_FILE, "w") as f:
                json.dump(self.palettes, f, indent=2)
        except IOError as e:
            self.log.error(f"Failed to save palettes: {e}")

    # --- Watchers to trigger saves and UI updates ---
    def watch_palettes(self, old_palettes, new_palettes):
        self._save_palettes()
        # Notify UI elements that might need refreshing
        self.post_message(self.PalettesChanged())

    def watch_active_palette_id(self, old_id, new_id):
        self.post_message(self.ActivePaletteChanged(new_id))
        # Reset active slot when palette changes? Optional.
        # self.active_slot_index = 0

    def watch_active_slot_index(self, old_index, new_index):
        self.post_message(self.ActiveSlotChanged(new_index))

    # --- Palette Management Methods ---
    @property
    def active_palette(self) -> dict | None:
        """Get the currently active palette object."""
        return next((p for p in self.palettes if p["id"] == self.active_palette_id), None)

    def create_palette(self, name="Untitled Palette"):
        """Create a new empty palette."""
        new_palette = create_empty_palette(name)
        # Use list copy and append for reactive update
        self.palettes = self.palettes + [new_palette]
        self.active_palette_id = new_palette["id"]
        return new_palette

    def update_palette(self, palette_id: str, updates: dict):
        """Update an existing palette."""
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

    def delete_palette(self, palette_id: str):
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

    def set_color_at_slot(self, slot_index: int, color: Color):
        """Set a color at a specific slot in the active palette."""
        if not self.active_palette or not (0 <= slot_index < 8):
            return

        # Make a copy of colors, update, then update the palette
        current_colors = list(self.active_palette["colors"])
        current_colors[slot_index] = color.hex # Store as hex string
        self.update_palette(self.active_palette_id, {"colors": current_colors})

    def duplicate_palette(self, palette_id: str):
         """Duplicate an existing palette."""
         source_palette = next((p for p in self.palettes if p["id"] == palette_id), None)
         if not source_palette:
             return

         new_palette = {
             **source_palette,
             "id": str(uuid.uuid4()),
             "name": f"{source_palette['name']} (Copy)",
             "createdAt": datetime.now().isoformat(),
         }
         self.palettes = self.palettes + [new_palette]
         self.active_palette_id = new_palette["id"]
         return new_palette

    # --- Custom Messages ---
    class PalettesChanged(App.Message): pass
    class ActivePaletteChanged(App.Message):
        def __init__(self, palette_id: str | None) -> None:
            self.palette_id = palette_id
            super().__init__()
    class ActiveSlotChanged(App.Message):
         def __init__(self, slot_index: int) -> None:
             self.slot_index = slot_index
             super().__init__()

    # ... rest of App class ...

```

#### 3.2 Color Palette Components

##### 3.2.1 Color Slot Widget

```python
# milky_color_suite/widgets/palette/color_slot.py
from textual.app import ComposeResult
from textual.reactive import reactive
from textual.widgets import Static
from textual.color import Color, ColorParseError
from textual.binding import Binding
# from ...constants.ascii_patterns import ASCII_PATTERNS # If using ASCII

class ColorSlot(Static):
    """Displays a single color slot."""

    DEFAULT_CSS = """
    ColorSlot {
        width: 8;
        height: 4;
        border: round $panel;
        text-align: center; /* Requires Textual >= 0.48 */
        vertical-align: middle; /* Requires Textual >= 0.48 */
    }
    ColorSlot:hover {
        border: round $accent;
    }
    ColorSlot.active {
        border: double $accent;
        /* background: $accent-lighten-2; */ /* Optional background indication */
    }
    """
    BINDINGS = [
        Binding("enter", "select_slot", "Select", show=False),
        Binding("d", "set_color", "Set Color", show=False), # Example: 'd' for 'drop' color
    ]

    # --- Reactive Properties ---
    slot_index = reactive(0)
    slot_color_hex = reactive("#ffffff")
    is_active_slot = reactive(False)

    def _get_display_color(self) -> Color:
        """Parse the hex color safely."""
        try:
            return Color.parse(self.slot_color_hex)
        except ColorParseError:
            return Color.parse("red") # Fallback for invalid color

    def render(self) -> str:
        """Render the slot number."""
        # Using render to control content and styling based on state
        color = self._get_display_color()
        self.styles.background = color
        self.styles.color = "black" if color.luminance > 0.5 else "white" # Contrast
        return str(self.slot_index + 1)

        # --- ASCII Pattern Alternative (if not using CSS background) ---
        # pattern = ASCII_PATTERNS["COLOR_SLOT"]["ACTIVE" if self.is_active_slot else "INACTIVE"]
        # return pattern.format(self.slot_index + 1)

    def watch_is_active_slot(self, old_val: bool, new_val: bool) -> None:
        """Update CSS class when active state changes."""
        self.set_class(new_val, "active")
        # Update border or other styles if not using ASCII patterns directly
        # self.styles.border = ("double", "$accent") if new_val else ("round", "$panel")


    def action_select_slot(self) -> None:
        """Notify app that this slot should become active on Enter press."""
        self.app.active_slot_index = self.slot_index
        self.log(f"Slot {self.slot_index} selected via Enter")

    def action_set_color(self) -> None:
        """Set the app's active color into this slot on 'd' press."""
        if self.is_active_slot: # Only allow setting if it's the active slot
             self.app.set_color_at_slot(self.slot_index, self.app.active_color)
             self.log(f"Set color {self.app.active_color.hex} to slot {self.slot_index}")
             # Refresh display manually if needed, though app state change should trigger it
             self.slot_color_hex = self.app.active_color.hex
             self.refresh()
        else:
             self.notify("Select the slot first (Enter) to set color (d).")


    def on_click(self) -> None:
        """Select this slot when clicked."""
        self.app.active_slot_index = self.slot_index
        self.log(f"Slot {self.slot_index} selected via Click")


    # Optional: Handle double click to set color directly
    # def on_click(self, event: events.Click) -> None:
    #     if event.button == 1: # Left click
    #         if event.ctrl: # Example: Ctrl+Click to set color
    #              self.app.set_color_at_slot(self.slot_index, self.app.active_color)
    #              self.refresh()
    #         else:
    #              self.app.active_slot_index = self.slot_index


```

##### 3.2.2 Palette Panel Widget

```python
# milky_color_suite/widgets/palette/palette_panel.py
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static
from textual.color import Color
from .color_slot import ColorSlot

class PalettePanel(Static):
    """Displays the 8 color slots of the active palette."""

    DEFAULT_CSS = """
    PalettePanel {
        border-top: thick $accent; /* Example border */
        height: auto; /* Adjust based on ColorSlot height */
        padding: 1;
    }
    PalettePanel Horizontal {
        height: auto;
        align: center middle;
        /* Add spacing between slots if needed */
    }
    """

    def compose(self) -> ComposeResult:
        """Create the color slots."""
        with Horizontal():
            for i in range(8):
                yield ColorSlot(id=f"slot-{i}")

    def on_mount(self) -> None:
        """Subscribe to app messages and update slots."""
        self.app.subscribe(self.app.ActivePaletteChanged, self._update_slots)
        self.app.subscribe(self.app.ActiveSlotChanged, self._update_active_highlight)
        self.app.subscribe(self.app.PalettesChanged, self._update_slots) # If colors changed
        self._update_slots() # Initial update

    def _update_slots(self, message = None) -> None:
        """Update colors and active state of all slots based on app state."""
        active_palette = self.app.active_palette
        active_slot_index = self.app.active_slot_index

        if not active_palette:
            # Handle case where there's no active palette (e.g., clear slots)
            for i in range(8):
                slot = self.query_one(f"#slot-{i}", ColorSlot)
                slot.slot_index = i
                slot.slot_color_hex = "#000000" # Default or empty indicator
                slot.is_active_slot = False
            return

        colors = active_palette.get("colors", ["#ffffff"] * 8)
        for i in range(8):
            slot = self.query_one(f"#slot-{i}", ColorSlot)
            slot.slot_index = i
            slot.slot_color_hex = colors[i] if i < len(colors) else "#ffffff"
            slot.is_active_slot = (i == active_slot_index)
            slot.refresh() # Ensure render() is called

    def _update_active_highlight(self, message: 'MilkyColorSuiteApp.ActiveSlotChanged') -> None:
        """Update only the active highlight more efficiently."""
        active_slot_index = message.slot_index
        for i in range(8):
            slot = self.query_one(f"#slot-{i}", ColorSlot)
            slot.is_active_slot = (i == active_slot_index)
            # refresh() might not be needed if only CSS class changes

```

#### 3.3 Palette Management Components

##### 3.3.1 Palette List Widget

```python
# milky_color_suite/widgets/palette/palette_list.py
from textual.app import ComposeResult
from textual.widgets import Static, Button, ListView, ListItem, Label
from textual.containers import VerticalScroll, Horizontal

class PaletteListItem(ListItem):
    """A ListItem that displays palette information."""
    def __init__(self, palette: dict) -> None:
        super().__init__()
        self.palette = palette

    def compose(self) -> ComposeResult:
        # Display palette name and maybe color swatches or ID
        yield Label(self.palette.get("name", "Unnamed Palette"))
        # Add small color previews if desired

class PaletteList(Static):
    """Widget for Browse, selecting, creating, and deleting palettes."""

    DEFAULT_CSS = """
    PaletteList {
        border: thick $accent;
        padding: 1;
        height: 15; /* Example height */
    }
    PaletteList ListView {
        border: thin $primary;
        margin-bottom: 1;
        height: 8; /* Example */
    }
    PaletteList #palette-controls Button {
        margin-top: 1;
        margin-right: 1; /* Spacing */
        width: 10; /* Adjust */
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Palettes")
        yield ListView(id="palette-list-view")
        with Horizontal(id="palette-controls"):
             yield Button("New", id="btn-new-palette", variant="success")
             yield Button("Dupe", id="btn-dupe-palette")
             yield Button("Delete", id="btn-del-palette", variant="error")


    def on_mount(self) -> None:
        """Subscribe to app messages and populate list."""
        self.app.subscribe(self.app.PalettesChanged, self._update_list)
        self.app.subscribe(self.app.ActivePaletteChanged, self._update_highlight)
        self._update_list() # Initial population

    def _update_list(self, message = None) -> None:
        """Update the ListView with current palettes."""
        list_view = self.query_one(ListView)
        list_view.clear() # Clear existing items
        for palette in self.app.palettes:
            list_view.append(PaletteListItem(palette))
        self._update_highlight()

    def _update_highlight(self, message = None) -> None:
        """Highlight the active palette in the list."""
        list_view = self.query_one(ListView)
        active_id = self.app.active_palette_id
        for i, item in enumerate(list_view.children):
            if isinstance(item, PaletteListItem) and item.palette.get("id") == active_id:
                list_view.index = i # Set current item
                break
        # Disable delete button if only one palette exists
        self.query_one("#btn-del-palette").disabled = len(self.app.palettes) <= 1

    # Handle selection changes in the ListView
    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """Update the app's active palette ID when an item is selected."""
        if isinstance(event.item, PaletteListItem):
            self.app.active_palette_id = event.item.palette.get("id")

    # Handle button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle palette action button clicks."""
        if event.button.id == "btn-new-palette":
            self.app.create_palette() # App state change triggers list update
        elif event.button.id == "btn-dupe-palette":
            if self.app.active_palette_id:
                self.app.duplicate_palette(self.app.active_palette_id)
        elif event.button.id == "btn-del-palette":
             if self.app.active_palette_id:
                 self.app.delete_palette(self.app.active_palette_id)

```

##### 3.3.2 Palette Naming Widget

```python
# milky_color_suite/widgets/palette/palette_name.py
from textual.app import ComposeResult
from textual.widgets import Static, Input, Label
from textual.reactive import reactive

class PaletteName(Static):
    """Widget for displaying and editing the active palette name."""

    DEFAULT_CSS = """
    PaletteName {
        border: thick $accent;
        padding: 1;
        margin-top: 1;
    }
    PaletteName Input {
        width: 100%; /* Take full width */
    }
    """
    # Use internal state synced via messages, or directly read/write app state
    _current_name = reactive("")

    def compose(self) -> ComposeResult:
        yield Label("Palette Name:")
        yield Input(placeholder="Enter palette name", id="palette-name-input")

    def on_mount(self) -> None:
        """Subscribe to app messages and set initial name."""
        self.app.subscribe(self.app.ActivePaletteChanged, self._update_name_display)
        self.app.subscribe(self.app.PalettesChanged, self._update_name_display) # If name changed
        self._update_name_display() # Initial load

    def _update_name_display(self, message = None) -> None:
        """Update the input field with the active palette's name."""
        active_palette = self.app.active_palette
        name = active_palette.get("name", "") if active_palette else ""
        self._current_name = name # Update internal state first
        input_widget = self.query_one(Input)
        if input_widget.value != name: # Avoid redundant updates/cursor jumps
             input_widget.value = name

    # Use watch for internal state change if needed
    # def watch__current_name(self, old_name, new_name):
        # Optional logic if name changes internally

    def on_input_changed(self, event: Input.Changed) -> None:
        """Update internal state as user types (optional)."""
        # Could add validation here if needed
        pass

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Update the palette name in the app state when Enter is pressed."""
        new_name = event.value.strip()
        if not new_name:
            self.notify("Palette name cannot be empty.", severity="warning")
            # Revert input to current name
            event.input.value = self._current_name
            return

        if self.app.active_palette and new_name != self._current_name:
            self.app.update_palette(self.app.active_palette_id, {"name": new_name})
            self.notify(f"Palette renamed to '{new_name}'")
            self._current_name = new_name # Sync internal state
        else:
             # If name hasn't actually changed, just blur the input maybe
             pass


    # Optional: Update on blur? Textual doesn't have a direct blur event like web JS.
    # Input.Submitted (Enter key) is the primary way.
```

#### 3.4 Save Current Color Feature

Update the `ColorSelector` or add a dedicated "Save" button to use the `app.set_color_at_slot` method.

```python
# Example: Adding a Save button to ColorInfo widget
# milky_color_suite/widgets/color/color_info.py

# ... inside ColorInfo.compose method, after format buttons:
yield Button("Save Color", id="btn-save-to-slot")

# ... inside ColorInfo class:
def on_button_pressed(self, event: Button.Pressed) -> None:
    # ... handle format buttons ...
    if event.button.id == "btn-save-to-slot":
        self.app.set_color_at_slot(self.app.active_slot_index, self.app.active_color)
        self.notify(f"Color saved to slot {self.app.active_slot_index + 1}")

# --- OR --- Integrate into ColorSlot directly (like the 'd' binding example)
```

#### 3.5 Integration with App/Screen

Add the new palette widgets to the main screen (`main_screen.py`):

```python
# milky_color_suite/screens/main_screen.py
# ... other imports
from ..widgets.palette.palette_list import PaletteList
from ..widgets.palette.palette_panel import PalettePanel
from ..widgets.palette.palette_name import PaletteName

class MainScreen(Screen):
    # ... BINDINGS, CSS_PATH ...

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
             with VerticalScroll(id="sidebar-container"):
                 yield PaletteList() # Add PaletteList to sidebar
                 # Add ImageColorPicker replacement/placeholder here
             with Container(id="main-and-palette"):
                 with VerticalScroll(id="main-container"):
                     yield Label("Color Tools")
                     yield ColorSelector()
                     yield ColorInfo()
                     yield PaletteName() # Add PaletteName below ColorInfo
                     # Add ExportPanel (Step 4) here
                 with Container(id="palette-container"):
                     yield PalettePanel() # Add PalettePanel to bottom area
        yield Footer()

    # ... actions ...
```