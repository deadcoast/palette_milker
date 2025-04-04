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

## 8. Textual Rules and Best Practises

```python
"""
textual_rules.py - Best Practices and Guidelines for Textual Applications

This file contains comprehensive guidelines, patterns, and type annotations
for building robust Textual TUI applications. Following these guidelines will
help ensure type safety, proper message handling, and consistent code structure.
"""

from typing import Any, ClassVar, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.message import Message
from textual.reactive import reactive
from textual.screen import Screen
from textual.widget import Widget
from textual.widgets import Static


# -------------------------------------------------------------------------
# TYPE DEFINITIONS AND ANNOTATIONS
# -------------------------------------------------------------------------

# Correct type annotation for BINDINGS in App and Screen classes
BindingType = Union[Binding, Tuple[str, str], Tuple[str, str, str]]
BindingListType = List[BindingType]

# Example class with properly typed BINDINGS
class CorrectBindingsExample(App):
    """Example of correctly typed BINDINGS."""
    
    # Note the use of ClassVar and the correct Union type
    BINDINGS: ClassVar[List[BindingType]] = [
        # All valid binding formats
        Binding("ctrl+q", "quit", "Quit", priority=True),  # Full Binding object
        ("a", "action_a", "Action A"),  # 3-tuple format
        ("b", "action_b"),  # 2-tuple format
    ]


# -------------------------------------------------------------------------
# MESSAGE PATTERNS
# -------------------------------------------------------------------------

class MessagePatterns:
    """Demonstrates correct message usage patterns in Textual."""
    
    class CorrectMessage(Message):
        """A properly defined message class."""
        
        def __init__(self, sender: Widget, value: str) -> None:
            """Initialize with sender and value.
            
            Args:
                sender: The widget sending the message
                value: The value to include in the message
            """
            # Always call super().__init__() with no arguments
            super().__init__()
            # Then set any custom attributes after
            self.value = value
            # Do not set self.sender as it's already handled by Message


class MessageSender(Widget):
    """Example widget that correctly sends messages."""
    
    def action(self) -> None:
        """Send a message to parent widgets."""
        # Post a message using the correct pattern
        self.post_message(MessagePatterns.CorrectMessage(self, "hello"))


class MessageReceiver(App):
    """Example of correctly handling messages from widgets."""
    
    def on_mount(self) -> None:
        """App is mounted."""
        self.sender = MessageSender()
        self.mount(self.sender)
    
    # Generic message handler - receives all messages of this type
    def on_correct_message(self, message: MessagePatterns.CorrectMessage) -> None:
        """Handles messages from any sender."""
        self.log(f"Received message with value: {message.value}")
    
    # Specific message handler - only receives messages from a specific widget
    def on_message_sender_correct_message(self, message: MessagePatterns.CorrectMessage) -> None:
        """Handles messages only from MessageSender with ID 'message_sender'."""
        self.log(f"Received message from message_sender with value: {message.value}")


# -------------------------------------------------------------------------
# WIDGET PATTERNS
# -------------------------------------------------------------------------

class WidgetPatterns:
    """Demonstrates correct widget patterns in Textual."""
    
    class ReactiveWidget(Widget):
        """Example widget with correctly defined reactive attributes."""
        
        # Reactive attributes are defined at class level
        color: reactive[str] = reactive("#ffffff")
        value: reactive[int] = reactive(0)
        
        # Initialize instance attributes properly
        def __init__(
            self, 
            initial_color: str = "#ffffff",
            *,  # Force keyword arguments for clarity
            name: Optional[str] = None,
            id: Optional[str] = None,
            classes: Optional[str] = None
        ) -> None:
            """Initialize the widget.
            
            Args:
                initial_color: Initial color value
                name: Optional widget name
                id: Optional widget ID (preferred over 'widget_id')
                classes: Optional CSS classes
            """
            # Always call super().__init__
            super().__init__(name=name, id=id, classes=classes)
            # Set reactive attributes after super().__init__
            self.color = initial_color
        
        # Add watchers for reactive attributes
        def watch_color(self, new_color: str) -> None:
            """Watch for changes to the color reactive attribute."""
            self.refresh()
    
    
    class ComposingWidget(Widget):
        """Example widget that composes other widgets."""
        
        def compose(self) -> ComposeResult:
            """Create child widgets.
            
            Returns:
                A ComposeResult containing child widgets.
            """
            # Use context managers for container widgets
            # Yield widgets to be added as children
            yield Static("Example Static Widget")
            yield WidgetPatterns.ReactiveWidget(id="reactive-widget")
        
        def on_mount(self) -> None:
            """Called when widget is added to the DOM.
            
            This is the right place to query for child widgets.
            """
            # Query for child widgets using CSS selectors
            # Always specify the expected type for clarity and type safety
            reactive_widget = self.query_one("#reactive-widget", WidgetPatterns.ReactiveWidget)
            
            # Update reactive properties
            reactive_widget.color = "#ff0000"


# -------------------------------------------------------------------------
# KEY BINDINGS AND ACTIONS
# -------------------------------------------------------------------------

class BindingPatterns:
    """Demonstrates correct binding patterns in Textual."""
    
    class BindingApp(App):
        """Example app with well-structured bindings."""
        
        BINDINGS: ClassVar[List[BindingType]] = [
            # Simple action binding
            Binding("q", "quit", "Quit"),
            
            # Action with arguments
            Binding("c", "change_color('red')", "Red"),
            
            # Global binding that takes priority
            Binding("ctrl+s", "save", "Save", priority=True),
            
            # Hidden binding (not shown in the footer)
            Binding("f1", "help", "Help", show=False),
        ]
        
        def action_change_color(self, color: str) -> None:
            """Change the color.
            
            Args:
                color: The color to change to
            """
            self.log(f"Changing color to {color}")
        
        def action_save(self) -> None:
            """Save the current state."""
            self.log("Saving...")
        
        def action_help(self) -> None:
            """Show help information."""
            self.log("Showing help...")


# -------------------------------------------------------------------------
# ERROR HANDLING
# -------------------------------------------------------------------------

class ErrorHandlingPatterns:
    """Demonstrates proper error handling in Textual apps."""
    
    def safe_query(self, app: App, selector: str, widget_cls: Type[Widget]) -> Optional[Widget]:
        """Safely query for a widget without raising exceptions.
        
        Args:
            app: The app instance
            selector: CSS selector
            widget_cls: Expected widget class
            
        Returns:
            The widget if found, None otherwise
        """
        try:
            return app.query_one(selector, widget_cls)
        except Exception as e:
            app.log(f"Error querying for {selector}: {e}")
            return None
    
    def safe_action(self, action_fn: callable, *args, **kwargs) -> None:
        """Safely execute an action function with error handling.
        
        Args:
            action_fn: The action function to call
            *args: Positional arguments
            **kwargs: Keyword arguments
        """
        try:
            action_fn(*args, **kwargs)
        except Exception as e:
            # Log the error but don't crash
            self.log(f"Error in action: {e}")


# -------------------------------------------------------------------------
# SCREEN MANAGEMENT
# -------------------------------------------------------------------------

class ScreenManagementPatterns:
    """Demonstrates correct screen management patterns."""
    
    class MainScreen(Screen):
        """Main application screen."""
        
        BINDINGS: ClassVar[List[BindingType]] = [
            Binding("s", "switch_to_settings", "Settings"),
        ]
        
        def action_switch_to_settings(self) -> None:
            """Switch to the settings screen."""
            # Use the correct method to switch screens
            self.app.push_screen("settings")
    
    class SettingsScreen(Screen):
        """Settings screen example."""
        
        BINDINGS: ClassVar[List[BindingType]] = [
            Binding("escape", "pop_screen", "Back"),
        ]
        
        def action_pop_screen(self) -> None:
            """Return to the previous screen."""
            self.app.pop_screen()
    
    class ModalScreen(Screen):
        """Modal screen example."""
        
        def on_mount(self) -> None:
            """Initialize the modal screen."""
            # Example of properly suspending the parent screen
            self.previous_screen = self.app.screen
            self.app.switch_screen(self)
        
        def on_key(self, event) -> None:
            """Handle key events."""
            if event.key == "escape":
                # Restore the previous screen
                self.app.switch_screen(self.previous_screen)


# -------------------------------------------------------------------------
# COMMON PITFALLS AND SOLUTIONS
# -------------------------------------------------------------------------

class CommonPitfalls:
    """Common pitfalls to avoid in Textual applications."""
    
    def avoid_direct_attribute_access(self) -> None:
        """Avoid directly accessing widget attributes that might not exist."""
        # INCORRECT:
        # color = self.color  # Might not exist
        
        # CORRECT:
        # Use hasattr to check if attribute exists
        if hasattr(self, "color"):
            color = self.color
        else:
            color = "#ffffff"  # Default value
    
    def avoid_missing_super_calls(self) -> None:
        """Always call super() in lifecycle methods."""
        # INCORRECT:
        # def on_mount(self) -> None:
        #     self.log("Mounted")  # Missing super() call
        
        # CORRECT:
        def on_mount(self) -> None:
            super().on_mount()  # Call super first
            self.log("Mounted")
    
    def avoid_incorrect_type_annotations(self) -> None:
        """Use correct type annotations for Textual classes."""
        # INCORRECT:
        # BINDINGS: List[Tuple[str, str, str]] = [...]  # Missing Union
        
        # CORRECT:
        BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = []
    
    def avoid_direct_widget_assignment(self) -> None:
        """Avoid assigning widgets directly."""
        # INCORRECT:
        # self.my_widget = Static("Text")  # Not mounted
        
        # CORRECT:
        # Mount widgets using mount() or yield in compose()
        def add_widget(self) -> None:
            self.mount(Static("Text"), before=0)  # Mount at start


# -------------------------------------------------------------------------
# PERFORMANCE TIPS
# -------------------------------------------------------------------------

class PerformanceTips:
    """Tips for optimizing Textual application performance."""
    
    def minimize_refresh_calls(self) -> None:
        """Minimize unnecessary refresh calls."""
        # INCORRECT:
        # def on_key(self, event) -> None:
        #     self.refresh()  # Refreshes on every key press
        
        # CORRECT:
        def on_key(self, event) -> None:
            if event.key == "r":
                self.refresh()  # Only refresh when needed
    
    def use_batch_updates(self) -> None:
        """Batch multiple updates to avoid frequent refreshes."""
        # Example of batching updates
        def update_multiple_properties(self) -> None:
            self.refresh(repaint=False)  # Defer repaint
            self.update_property1()
            self.update_property2()
            self.update_property3()
            self.refresh()  # Final refresh
    
    def optimize_rendering(self) -> None:
        """Optimize rendering of complex widgets."""
        # Use caching for expensive rendering operations
        _cache = {}
        
        def render_complex_widget(self, data: Any) -> str:
            """Render a complex widget with caching."""
            cache_key = hash(data)
            if cache_key in self._cache:
                return self._cache[cache_key]
            
            # Expensive rendering operation
            result = self.expensive_render(data)
            
            # Cache the result
            self._cache[cache_key] = result
            return result


# Example usage of the patterns and rules
if __name__ == "__main__":
    class ExampleApp(App):
        """Example application following best practices."""
        
        BINDINGS: ClassVar[List[BindingType]] = [
            Binding("q", "quit", "Quit"),
        ]
        
        def compose(self) -> ComposeResult:
            """Create the application layout."""
            yield WidgetPatterns.ComposingWidget()
        
        def on_mount(self) -> None:
            """Initialize the application."""
            self.title = "Example Following Best Practices"
    
    app = ExampleApp()
    app.run()
```

This comprehensive `textual_rules.py` file covers the most important practices for working with Textual:

1. **Correct Type Annotations**
   - Properly defines types for `BINDINGS` to avoid type errors
   - Shows how to use `ClassVar` for class variables
   - Demonstrates proper generic typing with `reactive`

2. **Message Handling**
   - Correct message class implementation
   - Proper sender/receiver patterns
   - Widget-specific vs. generic message handlers

3. **Widget Structure**
   - Proper composition with `compose()`
   - Correct initialization pattern
   - Handling reactive properties

4. **Key Bindings and Actions**
   - All supported binding formats
   - Action methods with parameters
   - Binding options (priority, visibility)

5. **Error Handling**
   - Safe query methods
   - Exception handling patterns
   - Defensive programming techniques

6. **Screen Management**
   - Switching between screens
   - Modal screens
   - Screen lifecycle

7. **Common Pitfalls**
   - Direct attribute access issues
   - Missing super() calls
   - Incorrect type annotations
   - Widget mounting errors

8. **Performance Optimization**
   - Minimizing refreshes
   - Batch updates
   - Rendering optimization
