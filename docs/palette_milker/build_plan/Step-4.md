
## Step 4: UTTER Export Functionality

### Overview

This final phase implements the UTTER (Unified Tiled Tone Export Resource) export system, allowing users to export color palettes in different formats including the custom UTTER array format, CSS variables, and raw color values, using Python utilities and Textual UI components.

### Prerequisites

* Completed Steps 1, 2, & 3 (Python/Textual)
* Understanding of Python classes and basic design patterns (like factory)
* Familiarity with Python string manipulation, file I/O, and clipboard libraries (e.g., `pyperclip`)

### Implementation Tasks

#### 4.1 UTTER Implementation (Python)

Create the core UTTER utility module:

```python
# milky_color_suite/utils/utter_export.py
from typing import Dict, List, Any

class UTTERInstance:
    """Represents a single UTTER instance generated from a palette."""

    # Base UTTER structure - adaptable as needed
    DEFAULT_COLOR_ROLES = [
        "primary", "secondary", "accent", "background",
        "text", "highlight", "muted", "neutral"
    ]

    # Basic template structure (can be expanded)
    BOTTLE_TEMPLATES = {
        "root": {
            "background-color": "$background",
            "color": "$text",
            "accent-color": "$accent",
        },
        "button": {
            "background-color": "$primary",
            "color": "$text",
            "border-color": "$accent",
            "hover-background": "$secondary", # Example - might need blending
            "active-background": "$highlight", # Example
        },
         # Add other templates (panel, form etc.) if desired
    }

    def __init__(self, palette: Dict[str, Any]):
        self.name: str = palette.get("name", "Untitled Palette")
        self.version: str = "1.0.0" # Or derive from app version
        self.colors: Dict[str, str] = {} # Role -> Hex Color mapping
        self._map_colors(palette.get("colors", []))

    def _map_colors(self, palette_colors: List[str]):
        """Maps palette colors to default roles."""
        for i, role in enumerate(self.DEFAULT_COLOR_ROLES):
            if i < len(palette_colors):
                self.colors[role] = palette_colors[i]
            else:
                # Assign default or leave unset if fewer than 8 colors?
                self.colors[role] = "#000000" # Example fallback

    def to_utter_array(self) -> List[str]:
        """Export as UTTER array format."""
        # Simply return the mapped colors in order of roles for consistency
        return [f"utter:{self.colors.get(role, '000000').lstrip('#')}"
                for role in self.DEFAULT_COLOR_ROLES if role in self.colors]

    def to_css_vars(self, prefix: str = "utter") -> str:
        """Convert colors to CSS variables string."""
        prefix = prefix.strip() or "utter" # Ensure valid prefix
        css = ":root {\n"
        for role, value in self.colors.items():
            css += f"  --{prefix}-{role}: {value};\n"
        css += "}\n"
        return css

    def to_color_values(self) -> List[str]:
        """Export as raw color values (hex strings)."""
        return [self.colors.get(role, "#000000")
                for role in self.DEFAULT_COLOR_ROLES if role in self.colors]

    def get_bottle(self, bottle_name: str) -> Dict[str, str] | None:
        """Get a specific 'bottle' (style set) with colors applied."""
        template = self.BOTTLE_TEMPLATES.get(bottle_name)
        if not template:
            return None

        result = {}
        for prop, value in template.items():
            if isinstance(value, str) and value.startswith('$'):
                color_key = value[1:]
                result[prop] = self.colors.get(color_key, value) # Use mapped color or fallback
            else:
                result[prop] = value # Keep non-color values as is
        return result

    # Add toJSON, toMarkdown, toObject etc. as needed based on Step 4-TL

# Factory function (optional, can just instantiate UTTERInstance directly)
def create_utter_from_palette(palette: Dict[str, Any]) -> UTTERInstance:
    """Creates a UTTER instance from a palette dictionary."""
    return UTTERInstance(palette)

# Export formats enum/constants
class ExportFormat:
    UTTER_ARRAY = "utterArray"
    CSS_VARS = "cssVars"
    COLOR_VALUES = "colorValues"
    # Add other formats like JSON, TEXT if implementing file export beyond clipboard
    JSON = "json"
    TEXT = "text"

```

#### 4.2 Export Panel Component

Create a Textual widget for handling export options and display.

```python
# milky_color_suite/widgets/export/export_panel.py
import pyperclip # Needs installation: pip install pyperclip
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Button, RadioSet, RadioButton, Input, TextArea, Label
from textual.reactive import reactive
from ...utils.utter_export import UTTERInstance, ExportFormat
# from ...utils.file_export import export_palette_to_file # If implementing file export

class ExportPanel(Static):
    """Widget for exporting the active palette."""

    DEFAULT_CSS = """
    ExportPanel {
        border: thick $accent;
        padding: 1;
        margin-top: 1;
    }
    ExportPanel RadioSet {
        margin-bottom: 1;
    }
    ExportPanel Input {
        margin-bottom: 1;
    }
    ExportPanel TextArea {
        height: 8; /* Example height */
        margin-bottom: 1;
        width: 100%;
    }
    ExportPanel #export-actions Button {
        margin-right: 1;
    }
    ExportPanel #copy-success {
        color: $success;
        margin-left: 1; /* Space before success message */
        display: none; /* Hide initially */
    }
    """

    # --- Reactive State ---
    selected_format = reactive(ExportFormat.UTTER_ARRAY)
    css_prefix = reactive("utter")
    _show_copy_success = reactive(False)

    def compose(self) -> ComposeResult:
        yield Label("Export Palette")
        with RadioSet(id="format-selector"):
            yield RadioButton("UTTER Array", value=ExportFormat.UTTER_ARRAY, id="fmt-utter")
            yield RadioButton("CSS Variables", value=ExportFormat.CSS_VARS, id="fmt-css")
            yield RadioButton("Color Values", value=ExportFormat.COLOR_VALUES, id="fmt-raw")
        yield Input(placeholder="CSS Prefix (e.g., my-app)", id="css-prefix-input", disabled=True)
        yield TextArea(language="text", show_line_numbers=False, id="export-preview", read_only=True)
        with Horizontal(id="export-actions"):
            yield Button("Copy", id="btn-copy")
            # yield Button("Export File...", id="btn-export-file") # Optional file export
            yield Static("Copied!", id="copy-success") # Success message


    def on_mount(self) -> None:
        """Set initial state and subscribe."""
        self.query_one(RadioSet).pressed_index = 0 # Select UTTER Array initially
        self.query_one("#css-prefix-input").value = self._get_default_prefix()
        self.css_prefix = self.query_one("#css-prefix-input").value

        # Subscribe to palette changes to update prefix and preview
        self.app.subscribe(self.app.ActivePaletteChanged, self._handle_palette_change)
        self.app.subscribe(self.app.PalettesChanged, self._handle_palette_change) # If name changes

        self._update_export_preview()

    def _get_default_prefix(self) -> str:
        """Generate default CSS prefix from active palette name."""
        active_palette = self.app.active_palette
        if active_palette:
            name = active_palette.get("name", "utter")
            # Basic slugify
            return "".join(c if c.isalnum() else '-' for c in name.lower()).strip('-')
        return "utter"

    def _handle_palette_change(self, message = None) -> None:
        """Update prefix input and preview when active palette changes."""
        # Update prefix only if CSS format is selected? Or always?
        # For simplicity, let's update the input value but not necessarily the reactive 'css_prefix'
        prefix_input = self.query_one("#css-prefix-input")
        if not prefix_input.has_focus: # Avoid overwriting user input
            new_prefix = self._get_default_prefix()
            prefix_input.value = new_prefix
            # If CSS is selected, also update the reactive property
            if self.selected_format == ExportFormat.CSS_VARS:
                self.css_prefix = new_prefix # This will trigger preview update via watcher

        # Always update preview as colors might have changed
        self._update_export_preview()

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        """Handle changes in the export format selection."""
        self.selected_format = event.pressed.value
        # Enable/disable CSS prefix input
        is_css = self.selected_format == ExportFormat.CSS_VARS
        prefix_input = self.query_one("#css-prefix-input")
        prefix_input.disabled = not is_css
        if is_css:
             self.css_prefix = prefix_input.value # Update reactive var when CSS is selected
        # Update preview triggered by watch_selected_format

    def watch_selected_format(self, old_fmt, new_fmt):
        self._update_export_preview()
        # Update TextArea language for syntax highlighting (basic)
        preview_area = self.query_one(TextArea)
        if new_fmt == ExportFormat.CSS_VARS:
             preview_area.language = "css"
        # elif new_fmt == ExportFormat.JSON: # If JSON export added
        #     preview_area.language = "json"
        else:
             preview_area.language = "text"


    def on_input_changed(self, event: Input.Changed) -> None:
        """Update css_prefix reactive var when input changes."""
        if event.input.id == "css-prefix-input":
             # Update only if CSS format is selected to avoid unnecessary preview updates
             if self.selected_format == ExportFormat.CSS_VARS:
                 self.css_prefix = event.value

    # Using watch is often cleaner for triggering updates based on reactive changes
    def watch_css_prefix(self, old_prefix, new_prefix):
        # Only update preview if CSS format is actually selected
        if self.selected_format == ExportFormat.CSS_VARS:
            self._update_export_preview()


    def _update_export_preview(self):
        """Generate and display the export content."""
        active_palette = self.app.active_palette
        if not active_palette:
            self.query_one(TextArea).load_text("No active palette.")
            return

        utter_instance = UTTERInstance(active_palette)
        content = ""
        if self.selected_format == ExportFormat.UTTER_ARRAY:
            content = "\n".join(utter_instance.to_utter_array())
        elif self.selected_format == ExportFormat.CSS_VARS:
            content = utter_instance.to_css_vars(self.css_prefix)
        elif self.selected_format == ExportFormat.COLOR_VALUES:
            content = "\n".join(utter_instance.to_color_values())
        # Add cases for other formats (JSON, TEXT) if implemented

        self.query_one(TextArea).load_text(content)


    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle Copy and Export File button clicks."""
        if event.button.id == "btn-copy":
            content = self.query_one(TextArea).text
            if content:
                try:
                    pyperclip.copy(content)
                    self.log("Content copied to clipboard.")
                    self.set_timer(2.0, self._hide_copy_success) # Hide after 2 seconds
                    self._show_copy_success = True # Trigger watcher
                except Exception as e:
                    self.log.error(f"Failed to copy to clipboard: {e}")
                    self.notify("Failed to copy to clipboard.", severity="error")
            else:
                 self.notify("Nothing to copy.", severity="warning")

        # elif event.button.id == "btn-export-file":
        #     self._handle_file_export() # Call file export logic

    # Watcher for the success message visibility
    def watch__show_copy_success(self, show: bool) -> None:
        self.query_one("#copy-success").styles.display = "block" if show else "none"

    def _hide_copy_success(self) -> None:
        self._show_copy_success = False

    # --- File Export Logic (Optional) ---
    # def _handle_file_export(self):
    #     active_palette = self.app.active_palette
    #     if not active_palette:
    #         self.notify("No active palette to export.", severity="warning")
    #         return
    #
    #     # Determine format, filename etc. (Could add another RadioSet for file type)
    #     # For simplicity, let's export based on the current preview format
    #     file_format = "text" # Default
    #     extension = ".txt"
    #     if self.selected_format == ExportFormat.CSS_VARS:
    #         file_format = "css"
    #         extension = ".css"
    #     # Add JSON etc. if needed
    #
    #     try:
    #         # Requires the utility function from fileExport.js adapted to Python
    #         export_palette_to_file(
    #             active_palette,
    #             file_format,
    #             self.css_prefix if file_format == "css" else None
    #         )
    #         self.notify(f"Palette exported as {file_format.upper()}. Check downloads.")
    #     except Exception as e:
    #         self.log.error(f"File export failed: {e}")
    #         self.notify("File export failed.", severity="error")

```

#### 4.3 File Export Utility (Python Adaptation)

Create a utility function for saving content to a file (this doesn't directly prompt the user for location like a browser download).

```python
# milky_color_suite/utils/file_export.py
import json
from pathlib import Path
from typing import Dict, Any
from .utter_export import UTTERInstance # Import necessary class

# Define where to save files (e.g., a subdirectory or user's home/downloads)
# Using a subdir in the project for simplicity here:
EXPORT_DIR = Path(__file__).parent.parent / "exports"

def _ensure_export_dir():
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

def export_palette_to_file(palette: Dict[str, Any], format_key: str, css_prefix: str | None = None):
    """Exports the palette content to a file in the EXPORT_DIR."""
    _ensure_export_dir()

    content = ""
    extension = ".txt"
    utter_instance = UTTERInstance(palette) # Create instance for formatting

    if format_key == "css":
        content = utter_instance.to_css_vars(css_prefix or "utter")
        extension = ".css"
    elif format_key == "json":
        # Export the raw palette data as JSON
        content = json.dumps(palette, indent=2)
        extension = ".json"
    elif format_key == "utter": # Export UTTER Array format
         content = "\n".join(utter_instance.to_utter_array())
         extension = ".txt" # Or maybe .utter?
    elif format_key == "text": # Export raw color values
        content = "\n".join(utter_instance.to_color_values())
        extension = ".txt"
    else: # Default to raw color values
        content = "\n".join(utter_instance.to_color_values())

    # Generate filename (similar to CSS prefix logic)
    base_name = palette.get("name", "palette")
    file_name_base = "".join(c if c.isalnum() else '_' for c in base_name.lower()).strip('_')
    file_path = EXPORT_DIR / f"{file_name_base}{extension}"

    try:
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Palette exported successfully to: {file_path}") # Log or notify user
        return str(file_path) # Return path on success
    except IOError as e:
        print(f"Error exporting palette to {file_path}: {e}") # Log error
        raise # Re-raise exception for handling in UI

```

#### 4.4 File Export Component Integration

Uncomment and adjust the file export button and logic in `ExportPanel` if file export is desired. Ensure the `export_palette_to_file` utility is imported and called correctly. You might need to add another `RadioSet` or `Select` widget to choose the *file* format specifically if it differs from the preview format.

#### 4.5 Integration with App/Screen

Add the `ExportPanel` to the main screen layout (`main_screen.py`):

```python
# milky_color_suite/screens/main_screen.py
# ... other imports
from ..widgets.export.export_panel import ExportPanel

class MainScreen(Screen):
    # ... BINDINGS, CSS_PATH ...

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
             with VerticalScroll(id="sidebar-container"):
                 yield PaletteList()
                 # ... other sidebar widgets
             with Container(id="main-and-palette"):
                 with VerticalScroll(id="main-container"):
                     yield Label("Color Tools")
                     yield ColorSelector()
                     yield ColorInfo()
                     yield PaletteName()
                     yield ExportPanel() # Add ExportPanel to main content area
                 with Container(id="palette-container"):
                     yield PalettePanel()
        yield Footer()
    # ... actions ...

```

#### 4.6 Extra UTTER Utilities (Python Adaptation)

Add parsing and import utilities if needed:

```python
# milky_color_suite/utils/utter_export.py

# ... (inside or outside UTTERInstance class) ...

def parse_utter_array(utter_array: List[str]) -> List[str]:
    """Parse UTTER array strings back into hex color values."""
    colors = []
    for item in utter_array:
        if isinstance(item, str) and item.startswith("utter:"):
            hex_val = item[6:].lstrip('#')
            # Basic validation for hex length
            if len(hex_val) in [3, 6]:
                 colors.append(f"#{hex_val}")
            else:
                 colors.append("#000000") # Fallback for invalid length
    return colors

def create_palette_from_utter(utter_array: List[str], name: str = "Imported Palette") -> Dict[str, Any]:
    """Create a palette dict from UTTER array (basic implementation)."""
    from datetime import datetime # Import locally if needed
    import uuid # Import locally if needed

    colors = parse_utter_array(utter_array)

    # Pad or trim to 8 colors
    final_colors = (colors + ["#ffffff"] * 8)[:8]

    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "colors": final_colors,
        "createdAt": datetime.now().isoformat(),
    }
```