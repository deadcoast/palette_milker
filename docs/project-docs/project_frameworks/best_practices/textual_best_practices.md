# Textual Best Practices Guide

This guide explains the best practices for building robust applications with the Textual framework, based on our refactoring experience.

## 1. Reactive Properties

### Proper Definition

Reactive properties should be defined at the class level using the `reactive` decorator with proper typing:

```python
from textual.reactive import reactive

class ExampleWidget(Widget):
    # Define at class level with type annotations
    count: reactive[int] = reactive(0)
    name: reactive[str] = reactive("Default")
    colors: reactive[List[str]] = reactive(["#000000"])
```

### Watchers

Implement watchers for reactive properties to respond to changes:

```python
def watch_count(self, old_value: int, new_value: int) -> None:
    """Called when count changes."""
    if old_value != new_value:  # Avoid unnecessary updates
        self.update(f"Count: {new_value}")
```

### Setting Values

Always set reactive properties directly without workarounds:

```python
# Correct
self.count = 5

# Incorrect - don't use these approaches
object.__setattr__(self, "count", 5)  # Avoid this
```

## 2. Message Handling

### Message Classes

Define proper message classes following Textual's pattern:

```python
from textual.message import Message
from textual.widget import Widget

class ColorChangeRequest(Message):
    """Message sent to request a color change."""
    
    def __init__(self, sender: Widget, color: str) -> None:
        """Initialize with sender and color."""
        super().__init__()  # Always call super().__init__()
        self.color = color
```

### Posting Messages

Post messages using the standard method:

```python
# Sending a message
self.post_message(ColorChangeRequest(self, "#FF0000"))
```

### Handling Messages

Handle messages with properly named message handler methods:

```python
# Generic handler for a message type
def on_color_change_request(self, message: ColorChangeRequest) -> None:
    """Handle color change requests from any sender."""
    self.log(f"Changing color to {message.color}")

# Specific handler for messages from a specific widget
def on_color_button_color_change_request(self, message: ColorChangeRequest) -> None:
    """Handle color change requests from the color button."""
    self.log(f"Color button requested color change to {message.color}")
```

## 3. Widget Composition

### Compose Method

Use the `compose` method to define child widgets:

```python
def compose(self) -> ComposeResult:
    """Create child widgets."""
    # Use container context managers
    with Container(id="header"):
        yield Static("Header")
    
    # Yield widgets
    yield Button("Click Me", id="button")
    
    with Container(id="footer"):
        yield Static("Footer")
```

### Mounting Widgets

Mount widgets using the proper methods:

```python
# Mount a new widget
new_widget = Button("New")
self.mount(new_widget)

# Mount at a specific position
self.mount(new_widget, before=0)  # Add at the beginning
```

### Accessing Child Widgets

Use query methods to find child widgets:

```python
# Get a single widget by selector
button = self.query_one("#submit-button", Button)

# Get multiple widgets
items = self.query(".list-item")
```

## 4. Type Safety in Textual

### Class Variables

Use `ClassVar` for class-level constants:

```python
from typing import ClassVar, List, Union, Tuple
from textual.binding import Binding

class MyScreen(Screen):
    # Properly typed BINDINGS
    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        Binding("q", "quit", "Quit"),
    ]
```

### Generic Types

Use proper generic type annotations:

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class DataContainer(Generic[T]):
    """Container for data of type T."""
    
    def __init__(self, data: T) -> None:
        self.data = data
```

### Type Conversions

Handle type conversions explicitly when needed:

```python
# When you need to convert between compatible types
def process_colors(self, hex_colors: List[str]) -> None:
    """Process a list of hex colors."""
    # Convert strings to Color objects when needed
    color_objects = [Color(color) for color in hex_colors]
    # Process the colors...
```

## 5. Error Handling

### Try-Except Blocks

Use try-except blocks for operations that might fail:

```python
try:
    result = self.perform_operation()
    self.notify("Operation successful", severity="information")
except Exception as e:
    self.log.error(f"Operation failed: {e}")
    self.notify(f"Operation failed: {e}", severity="error")
```

### Safe Widget Queries

Use safe query patterns for widget access:

```python
try:
    button = self.query_one("#submit-button", Button)
    button.label = "Submit"
except Exception:
    self.log.warning("Submit button not found")
```

## 6. Bindings and Actions

### Define Bindings

Define bindings at the class level:

```python
BINDINGS = [
    # Simple binding
    Binding("q", "quit", "Quit"),
    
    # Binding with arguments
    Binding("c", "change_color('#ff0000')", "Red"),
    
    # Priority binding (works even in input fields)
    Binding("ctrl+s", "save", "Save", priority=True),
    
    # Hidden binding (not shown in footer)
    Binding("f1", "help", "Help", show=False),
]
```

### Implement Actions

Implement action methods for bindings:

```python
def action_quit(self) -> None:
    """Quit the application."""
    self.app.exit()

def action_change_color(self, color: str) -> None:
    """Change the color.
    
    Args:
        color: The color to change to
    """
    self.log(f"Changing color to {color}")
```

## 7. Screen Management

### Screen Navigation

Use proper screen navigation methods:

```python
# Push a screen onto the stack
self.app.push_screen("settings")

# Switch screens (replacing the current screen)
self.app.switch_screen("main")

# Pop the top screen from the stack
self.app.pop_screen()
```

### Modal Screens

Create modal screens that pause the application:

```python
class ConfirmDialog(ModalScreen):
    """Modal confirmation dialog."""
    
    def compose(self) -> ComposeResult:
        with Container():
            yield Static("Are you sure?")
            with Horizontal():
                yield Button("Yes", id="yes")
                yield Button("No", id="no")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.dismiss(True)
        else:
            self.dismiss(False)
```

## 8. Performance Optimization

### Minimize Refresh Calls

Avoid unnecessary refreshes:

```python
def update_multiple_properties(self) -> None:
    """Update multiple properties efficiently."""
    # Defer repaint during intermediate updates
    self.refresh(repaint=False)
    
    # Make all your updates
    self.property1 = "value1"
    self.property2 = "value2"
    
    # Final refresh to update the display
    self.refresh()
```

### Use Batch Updates

Group related updates together:

```python
def update_palettes(self, palettes: List[Dict[str, Any]]) -> None:
    """Update multiple palettes in batch."""
    with self.batch_update():
        for palette in palettes:
            self.add_palette(palette)
```

## Conclusion

Following these Textual best practices will help you build robust, maintainable applications with fewer bugs and better performance. These patterns ensure your code works well with Textual's reactive system and component lifecycle. 
