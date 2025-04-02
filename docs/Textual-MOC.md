# Textual Framework Documentation Map

This document serves as a navigation guide to the Textual documentation, organizing the content by functionality and purpose to facilitate quick reference during development.

## 1. Getting Started

- **Basic Tutorials**
  - [Getting Started](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Textual - Getting started.md) - Installation and requirements
  - [Tutorial](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Textual - Tutorial.md) - Step-by-step tutorial building a stopwatch app
  
- **Installation**
  - **Requirements:** Python 3.8 or later
  - **Terminal Requirements:**
    - Linux: Built-in terminal emulator
    - macOS: Recommended [iterm2](https://iterm2.com/), [Ghostty](https://ghostty.org/), [Kitty](https://sw.kovidgoyal.net/kitty/), or [WezTerm](https://wezfurlong.org/wezterm/)
    - Windows: [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701)
  - **Install Command:** `pip install textual`
  - **Developer Tools:** `pip install textual-dev`
  - **Syntax Highlighting:** `pip install "textual[syntax]"`
  - **Conda Installation:** `micromamba install -c conda-forge textual`

## 2. Core Concepts

- **App Structure**
  - [App Basics](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - App Basics.md) - Fundamentals of the App class
  - [Screens](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Screens.md) - Working with multiple application screens

- **Widget System**
  - [Widgets](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Widgets.md) - Working with and creating widgets
  - [Widgets Gallery](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Widgets Gallery.md) - Overview of all available widgets

- **Layout**
  - [Layout](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Layout.md) - Layout systems (vertical, horizontal, grid)
  - [Content](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Content.md) - Working with widget content
  - [Design a Layout](/Users/deadcoast/Documents/milky_suite/Textual-Docs/How%20To/Textual%20-%20Design%20a%20Layout.md) - Practical guide to creating layouts
  - [Center Things](/Users/deadcoast/Documents/milky_suite/Textual-Docs/How%20To/Textual%20-%20Center%20things.md) - How to center content

- **Styling**
  - [Textual CSS](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Textual CSS.md) - CSS styling system
  - [Styles](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Styles.md) - Available style properties
  - [Themes](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Themes.md) - Working with themes
  - [Style Inline Apps](/Users/deadcoast/Documents/milky_suite/Textual-Docs/How%20To/Textual%20-%20Style%20Inline%20Apps.md) - Styling apps without external CSS files

- **Interactivity**
  - [Events and Messages](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Events and Messages.md) - Event handling system
  - [Input](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Input.md) - Handling user input
  - [Reactivity](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Reactivity.md) - Reactive programming model
  - [Actions](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Actions.md) - Application actions system
  - [Animation](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Animation.md) - Creating animations

## 3. Widget Reference

### 3.1 Container Widgets
- Container - Basic container
- Horizontal - Horizontal layout
- Vertical - Vertical layout
- Grid - Grid layout
- [TabbedContent](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - TabbedContent.md) - Tabbed interface
- [ContentSwitcher](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - ContentSwitcher.md) - Dynamic content switching

### 3.2 Input Widgets
- [Button](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Button.md) - Clickable button
- [Input](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Input.md) - Text input field
- [Checkbox](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Checkbox.md) - Checkbox control
- [RadioButton](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - RadioButton.md) - Radio button control
- [RadioSet](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - RadioSet.md) - Group of radio buttons
- [Select](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Select.md) - Dropdown selection
- [Switch](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Switch.md) - Toggle switch
- [TextArea](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - TextArea.md) - Multiline text input

### 3.3 Display Widgets
- [Static](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Static.md) - Static text display
- [Label](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Label.md) - Text label
- [Markdown](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Markdown.md) - Rendered markdown content
- [MarkdownViewer](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - MarkdownViewer.md) - Scrollable markdown viewer
- [ProgressBar](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - ProgressBar.md) - Progress indicator
- [Rule](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Rule.md) - Horizontal or vertical line separator
- [Header](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Header.md) - Application header
- [Footer](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Footer.md) - Application footer

### 3.4 Data Visualization
- [DataTable](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - DataTable.md) - Tabular data with selection
- [Tree](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Tree.md) - Hierarchical data display
- [DirectoryTree](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - DirectoryTree.md) - File system tree
- [ListView](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - ListView.md) - Scrollable list
- [ListItem](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - ListItem.md) - Item in a list
- [OptionList](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - OptionList.md) - List of selectable options
- [SelectionList](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - SelectionList.md) - List with selection
- [Pretty](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Pretty.md) - Pretty-printed data
- [Sparkline](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Sparkline.md) - Simple sparkline chart

### 3.5 Utility Widgets
- [Placeholder](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Placeholder.md) - Temporary placeholder
- [LoadingIndicator](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - LoadingIndicator.md) - Loading spinner
- [Log](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - Log.md) - Logging output
- [RichLog](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Widgets/Textual - RichLog.md) - Rich formatted logging

## 4. CSS Reference

### 4.1 Layout Properties
- [Align](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Align.md) - Alignment of children
- [Width](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Width.md) - Width of element
- [Height](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Height.md) - Height of element
- [Min/Max Width/Height](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Min-width.md) - Min/max constraints
- [Margin](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Margin.md) - Space around elements
- [Padding](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Padding.md) - Space inside elements
- [Display](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Display.md) - Display behavior
- [Position](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Position.md) - Positioning method
- [Dock](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Dock.md) - Dock to edges

### 4.2 Grid Properties
- [Grid Columns](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Grid-columns.md)
- [Grid Rows](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Grid-rows.md)
- [Grid Size](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Grid-size.md)
- [Grid Gutter](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Grid-gutter.md)
- [Column Span](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Column-span.md)
- [Row Span](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Row-span.md)

### 4.3 Appearance Properties
- [Background](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Background.md)
- [Color](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Color.md)
- [Border](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Border.md)
- [Outline](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Outline.md)
- [Text Style](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Text-style.md)
- [Text Align](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Text-align.md)
- [Opacity](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Styles/Textual - Opacity.md)

### 4.4 Media Queries
```css
/* Small screen */
@media (width < 80) {
    .sidebar {
        display: none;
    }
}

/* Large screen */
@media (width >= 80) {
    .sidebar {
        width: 20%;
    }
}
```

## 5. Advanced Features

- **Additional Functionality**
  - [Workers](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Workers.md) - Background task processing
  - [Command Palette](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Command Palette.md) - Command UI
  - [DOM Queries](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - DOM Queries.md) - Query selectors
  - [Actions](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Actions.md) - Application actions
  - [Render and Compose](/Users/deadcoast/Documents/milky_suite/Textual-Docs/How%20To/Textual%20-%20Render%20and%20compose.md) - Understanding rendering lifecycle

- **Developer Tools**
  - [Devtools](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Devtools.md) - Development tools
  - [Testing](/Users/deadcoast/Documents/milky_suite/Textual-Docs/Guide/Textual - Testing.md) - Testing Textual applications
  - [Package a Textual App](/Users/deadcoast/Documents/milky_suite/Textual-Docs/How%20To/Textual%20-%20Package%20a%20Textual%20app%20with%20Hatch.md) - Packaging with Hatch

## 6. Events Reference

### 6.1 Mouse Events
- [Click](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - Click.md)
- [MouseDown](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - MouseDown.md)
- [MouseUp](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - MouseUp.md)
- [MouseMove](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - MouseMove.md)
- [MouseScrollDown](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - MouseScrollDown.md)
- [MouseScrollUp](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - MouseScrollUp.md)

### 6.2 Keyboard Events
- [Key](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - Key.md)
- [Paste](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - Paste.md)

### 6.3 Focus Events
- [Focus](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - Focus.md)
- [Blur](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - Blur.md)
- [DescendantFocus](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - DescendantFocus.md)
- [DescendantBlur](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - DescendantBlur.md)

### 6.4 Lifecycle Events
- [Mount](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - Mount.md)
- [Show](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - Show.md)
- [Hide](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - Hide.md)
- [Load](/Users/deadcoast/Documents/milky_suite/Textual-Docs/References/Events/Textual - Load.md)

## 7. Quick Reference

### 7.1 Key App Fundamentals

#### App Lifecycle Methods
```python
def on_mount(self) -> None:
    """Called when app is mounted and ready for user input."""
    # Initialize application state here
    pass

def on_load(self) -> None:
    """Called when DOM is ready, but before mounting."""
    # Set up data before mount
    pass
    
def on_screen_resume(self) -> None:
    """Called when a screen is resumed from the stack."""
    pass
    
def on_screen_suspend(self) -> None:
    """Called when a screen is suspended (another pushed on top)."""
    pass
```

#### Key Binding Example
```python
BINDINGS = [
    ("q", "quit", "Quit the application"),
    ("d", "toggle_dark", "Toggle dark mode"),
    ("ctrl+s", "save", "Save file"),
    Binding("f1", "help", "Show help", show=False),  # Hidden from UI
]

def action_toggle_dark(self) -> None:
    """Toggle between light and dark mode."""
    self.theme = (
        "textual-dark" if self.theme == "textual-light" else "textual-light"
    )
```

### 7.2 Common Development Patterns

#### Basic App Structure
```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class MyApp(App):
    CSS_PATH = "my_app.css"
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Static("Main content", id="content")
        yield Footer()
        
    def on_mount(self) -> None:
        """Initialize app state after mounting."""
        self.title = "My Textual App"

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

#### Custom Widget
```python
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Button

class CustomWidget(Widget):
    DEFAULT_CSS = """
    CustomWidget {
        width: 100%;
        height: auto;
        padding: 1;
    }
    """
    
    def compose(self) -> ComposeResult:
        yield Button("Click Me")
        
    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Handle button press
        pass
```

#### Reactive Variables
```python
from textual.reactive import reactive

class ReactiveWidget(Widget):
    count = reactive(0)
    
    def on_mount(self) -> None:
        self.set_interval(1, self.increment)
    
    def increment(self) -> None:
        self.count += 1
    
    def watch_count(self, value: int) -> None:
        # Called when count changes
        self.update(f"Count: {value}")
```

#### Handling Events
```python
def on_key(self, event: Key) -> None:
    if event.key == "q":
        self.app.exit()
    elif event.key == "r":
        self.reset()
        
def on_click(self, event: Click) -> None:
    if event.button == 1:  # Left click
        self.toggle_selection(event.target)
```

#### Working with Timers
```python
def on_mount(self) -> None:
    # Run once after 1 second
    self.set_timer(1, self.do_once)
    
    # Run every 1 second
    self.set_interval(1, self.do_repeatedly)
```

#### Worker Example
```python
from textual.worker import Worker, get_current_worker

def on_mount(self) -> None:
    self.run_worker(self.background_task())
    
@staticmethod
async def background_task() -> None:
    worker = get_current_worker()
    for i in range(100):
        if worker.is_cancelled:
            break
        # Do work here
        await worker.update(i)  # Send progress update
```

### 7.3 Common CSS Patterns

#### Grid Layout
```css
Grid {
    grid-size: 3 2;  /* 3 columns, 2 rows */
    grid-gutter: 1;
    grid-columns: 1fr 2fr 1fr;  /* Proportional widths */
    grid-rows: 5 1fr;  /* First row 5 lines, second row flexible */
}

#span-item {
    column-span: 2;  /* Span 2 columns */
    row-span: 2;     /* Span 2 rows */
}
```

#### Responsive Layout
```css
/* Small screen */
@media (width < 80) {
    .sidebar {
        display: none;
    }
    .content {
        width: 100%;
    }
}

/* Large screen */
@media (width >= 80) {
    .sidebar {
        width: 20%;
    }
    .content {
        width: 80%;
    }
}
```

#### Theme Variables
```css
/* Using built-in theme variables */
Button {
    background: $primary;
    color: $text;
    border: solid $secondary;
}

Button:hover {
    background: $primary-darken-1;
}
```

#### Class and ID Selectors
```css
/* Class selector (multiple elements) */
.warning {
    color: $warning;
    background: $warning-darken-3;
}

/* ID selector (single element) */
#main-content {
    height: 100%;
    padding: 1 2;
}

/* Pseudo-classes */
Button:hover {
    background: $accent;
}

Input:focus {
    border: thick $accent;
}
```

### 7.4 CLI Commands

```bash
# Install Textual and development tools
pip install textual
pip install textual-dev

# Run an app with dev tools
textual run myapp.py --dev

# Show console output
textual console

# Create a new Textual app from template
textual new myproject

# Start CSS watcher for live-editing CSS
textual css-watch myapp.py

# Generate CSS stylesheet for a widget
textual css-to-python mywidget.py
```

### 7.5 Best Practices

#### Optimal Performance
- Use `watch_*` methods over subclassing for reactive variables
- Leverage workers for CPU-intensive or blocking operations
- Use CSS for styling instead of programmatic style manipulation
- Apply `loading=True` for widgets that require time to load

#### Error Handling
```python
try:
    await self.do_something_risky()
except Exception:
    self.notify("An error occurred", severity="error")
```

#### DOM Navigation
```python
# Query a single widget by CSS selector
button = self.query_one("#submit-button", Button)

# Query multiple widgets
items = self.query(".list-item")

# Walk the DOM tree
parent = self.parent
children = self.children
first_child = self.children[0]
```

#### Debugging Techniques
```python
# Log to console
from rich import print as rprint
rprint("[bold red]Debug:[/] Value is", value)

# Use console command
# textual console
self.log("Debug value:", value)
```

This document map provides a structured overview of the Textual documentation for quick reference when developing applications. The categorization and links make it easy to find specific information when needed.
