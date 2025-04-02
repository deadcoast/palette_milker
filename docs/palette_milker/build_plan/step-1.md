# Milky Color Suite - Python/Textual Project Plan

## Step 1: Project Setup and Core UI Framework

### Overview

This phase establishes the foundation for the Milky Color Suite by creating the project structure using Python and Textual, implementing the core UI framework with standard Textual widgets and ASCII styling capability, and setting up the core layout system.

### Prerequisites

* Python (v3.7+)
* `pip` or `poetry` for package management
* Basic knowledge of Python and the Textual framework

### Implementation Tasks

#### 1.1 Project Initialization

```bash
# Create project directory
mkdir milky-color-suite
cd milky-color-suite

# Set up a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install Textual and color library
pip install textual rich # Or use poetry add textual rich

# (Optional) Install textual-dev tools for development
pip install textual-dev
```

#### 1.2 Project Structure Setup

Create the following directory structure:

```
milky-color-suite/
├── milky_color_suite/
│   ├── widgets/          # Custom Textual widgets
│   │   ├── color/          # Color extraction and manipulation tools (Step 2)
│   │   ├── palette/        # Palette management components (Step 3)
│   │   └── export/         # UTTER export functionality (Step 4)
│   ├── screens/          # Application screens
│   ├── utils/            # Utility functions
│   ├── constants/        # ASCII patterns and other constants
│   ├── data/             # For storing palettes (alternative to LocalStorage)
│   ├── main.py           # Main application entry point
│   └── app.tcss          # Main CSS file (optional)
├── tests/                # Unit tests
└── README.md
```

Execute:
```bash
# Create directory structure
mkdir -p milky_color_suite/widgets/color milky_color_suite/widgets/palette milky_color_suite/widgets/export milky_color_suite/screens milky_color_suite/utils milky_color_suite/constants milky_color_suite/data tests
touch milky_color_suite/main.py milky_color_suite/__init__.py milky_color_suite/widgets/__init__.py tests/__init__.py README.md
# Optionally create main CSS file
touch milky_color_suite/app.tcss
```

#### 1.3 ASCII Patterns Library

Create a constants file to store all ASCII patterns:

```python
# milky_color_suite/constants/ascii_patterns.py

# [!ASCII_MARKER] Patterns below need defining based on desired TUI appearance

ASCII_PATTERNS = {
    # Patterns for standard Textual buttons (maybe borders or styles)
    "BUTTON": {
        "DEFAULT": "[ Save ]", # Example
        "ACTIVE": "[*Save*]", # Example
        "EYEDROPPER": "[⨀]",  # From Step 2-TL
        "SAVE_COLOR": "[save]", # From Step 2-TL
        # Add other button patterns (e.g., ADD_PALETTE, COPY, EXPORT)
    },
    # Patterns for containers, windows, etc. (can be styled with CSS or borders)
    "WINDOW": {
        # Example: Can use Textual's Border widget or CSS
        "DEFAULT": """
╔════════════════════════════════════════╗
║                                        ║
║ Content Here                           ║
║                                        ║
╚════════════════════════════════════════╝
""",
        "COLOR_WHEEL_CONTAINER": """
╔────────────────────────────────────────────────────────────────╗
│ [⨀] [save]                COLOR WHEEL                          │
╠────────────────────────────────────────────────────────────────╣
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
╠────────────────────────────────────────────────────────────────╣
│ ~HEX:>                                                        │
╚────────────────────────────────────────────────────────────────╝
""", # From Step 2-TL
        "PALETTE_NAME_EDITOR": """
┌─────────────────────────────────────┐
│ Palette Name:                       │
│ ┌─────────────────────────────────┐ │
│ │ ~name:>                        │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
""", # From Step 3-TL
        "EXPORT_OPTIONS_DROPDOWN": """
   ┌─────────────────────────────────────┐
   │ Export As:                          │
   │ ┌─────────────────────────────────┐ │
   │ │ ~Array:> ▼ [Dropdown Window]   │ │
   │ └─────────────────────────────────┘ │
   └─────────────────────────────────────┘
""", # From Step 3-TL
       # Add other window/panel patterns if needed
    },
    "SIDEBAR": {
        # Example: Maybe just a styled container via CSS
        "DEFAULT": ""
    },
    # Patterns for color slots
    "COLOR_SLOT": {
        "ACTIVE": """
┌█───█┐
│  {} │
└─────┘
""", # Placeholder for number. From Step 2-TL
        "INACTIVE": """
┌─────┐
│  {} │
└─────┘
""" # Placeholder for number. From Step 2-TL
    },
    # Patterns for palette groups/tabs
    "PALETTE_GROUP": {
        "ACTIVE": """
╔════════════════╗
╠─♢ {}         ╠
╠════════════════╝
""", # Placeholder for name. Adapted from Step 2-TL
        "INACTIVE": """
┬────────────────┐
├─ {}            │
┴────────────────┘
""" # Placeholder for name. Adapted from Step 2-TL
    },
     "PALETTE_PANEL": """
╔════════════════╗
╠─♢ Palette      ╠┬────────────────┬────────────────┬───────────────┐
╠════════════════╝├─ Palette 2     ├─ Palette 3     ├─ Palette 4    │
╠─────────────────┴────────────────┴────────────────┴───────────────╣
║  {}                                                              ║ # Placeholder for slots row
╚═══════════════════════════════════════════════════════════════════╝
""", # From Step 2-TL (Structure only, slots go inside)
    # Patterns for Textual Input widgets
    "FORM_FIELD": {
         # Example: Textual Input widgets handle their own display
        "DEFAULT": "",
        "COLOR_VALUE_INPUT": """
╠────────────────────────────────────────────────────────────────╣
│ ~HEX:> {}                                                      │
╚────────────────────────────────────────────────────────────────╝
""" # Placeholder for value. From Step 2-TL
    },
     # Patterns for Export UI (Step 4-TL)
    "EXPORT_PANEL": { # Base container for export section
         "DEFAULT": ""
    },
    "EXPORT_FORMAT_SELECTOR": { # Radio buttons/tabs for format
        "UTTER_BTN": "[ UTTER Array ]",
        "CSS_BTN": "[ CSS Vars ]",
        "RAW_BTN": "[ Color Values ]",
    },
    "EXPORT_PREVIEW": { # Text area for preview
        "DEFAULT": ""
    },
    "EXPORT_ACTION_BUTTONS": {
        "COPY_BTN": "[ Copy ]",
        "DOWNLOAD_BTN": "[ Download ]"
    }
}

# Function to easily get patterns if needed
def get_pattern(category, name):
    return ASCII_PATTERNS.get(category, {}).get(name, "")
```

#### 1.4 Core Textual Widget System

* **No Base Transparent Component:** Textual widgets provide their own rendering. Styling is done via Textual CSS or inline styles.
* **Standard Widgets:** Use built-in Textual widgets like `Button`, `Static`, `Input`, `Container`, `Header`, `Footer`, `ListView`, `DataTable`, `TextArea`, `RadioSet` etc.

#### 1.5 Main Application Layout

```python
# milky_color_suite/screens/main_screen.py
from textual.app import ComposeResult
from textual.containers import Container, VerticalScroll, Horizontal
from textual.screen import Screen
from textual.widgets import Header, Footer, Static # Add other needed widgets

# Import placeholder widgets or actual widgets from steps 2, 3, 4
# from ..widgets.placeholder import PlaceholderWidget # Example

class MainScreen(Screen):
    """Main application screen."""

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    CSS_PATH = "../app.tcss" # Optional: Link CSS file

    def compose(self) -> ComposeResult:
        """Create child widgets for the screen."""
        yield Header()
        with Container(id="app-grid"):
             # Use Textual layout (e.g., Grid, Horizontal, Vertical)
             # Example using Horizontal layout:
             with VerticalScroll(id="sidebar-container"):
                 yield Static("Sidebar Area (Step 2/3)", id="sidebar-content")
                 # Add PaletteList, ImageColorPicker placeholder here
             with Container(id="main-and-palette"):
                 with VerticalScroll(id="main-container"):
                     yield Static("Main Content Area (Step 2/4)", id="main-content")
                     # Add ColorWheel, ColorInfo, PaletteName, ExportPanel placeholders here
                 with Container(id="palette-container"):
                     yield Static("Palette Area (Step 3)", id="palette-content")
                     # Add PalettePanel placeholder here
        yield Footer()

    # Add actions or methods as needed
    # def action_quit(self) -> None:
    #    self.app.exit()

# milky_color_suite/main.py
from textual.app import App
from .screens.main_screen import MainScreen

class MilkyColorSuiteApp(App):
    """A Textual app to manage color palettes."""

    CSS_PATH = "app.tcss" # Optional: Load main CSS
    SCREENS = {"main": MainScreen()}

    def on_mount(self) -> None:
        """Called when the app is mounted."""
        self.push_screen("main")

if __name__ == "__main__":
    app = MilkyColorSuiteApp()
    app.run()

```

#### 1.6 Form Input Components

* **Text Input:** Use Textual's built-in `Input` widget. Styling and placeholders are handled by the widget's properties and CSS. The `TransparentInput` concept is not needed.

#### 1.7 Application Entry Point

* Covered in section 1.5 (`main.py`).

#### 1.8 Basic Styling

```css
/* milky_color_suite/app.tcss (Optional) */

Screen {
    /* Grid layout example */
    grid-size: 2;
    grid-gutter: 1 2;
    grid-columns: 30 1fr; /* Sidebar 30 cells, main takes rest */
    grid-rows: auto 1fr 8; /* Header auto, content flex, palette 8 rows */
    background: $panel;
    color: $text;
}

#app-grid {
    grid-column: 1 / 3; /* Span both columns */
    grid-row: 2;        /* Middle row */
    border: thick $accent;
    display: grid; /* Use grid for app content area */
    grid-columns: 30 1fr;
    grid-rows: 1fr auto; /* Main area flex, palette fixed */
}

#sidebar-container {
    grid-column: 1;
    grid-row: 1 / 3; /* Span both rows */
    border: thick $accent;
    padding: 1;
}

#main-and-palette {
    grid-column: 2;
    grid-row: 1 / 3; /* Span both rows */
    display: grid;
    grid-rows: 1fr auto; /* Main content flex, palette fixed */
}


#main-container {
    grid-row: 1;
    padding: 1;
    border: thick $accent;
}

#palette-container {
    grid-row: 2;
    height: 10; /* Example fixed height */
    border: thick $accent;
    padding: 1;
}


Header {
    grid-column: 1 / 3;
    grid-row: 1;
    border: thick $accent;
}

Footer {
    grid-column: 1 / 3;
    grid-row: 3;
    border: thick $accent;
}

/* Style other widgets as needed */
Button {
    min-width: 8;
    border: thick $secondary;
}

Input {
    border: thick $accent;
}
```