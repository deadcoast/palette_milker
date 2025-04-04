# ApplicationState API Documentation

This document provides detailed information about the `ApplicationState` class in the Palette Milker application. The `ApplicationState` class serves as a central state manager, providing a clean separation between business logic and UI components.

## Class Overview

```python
class ApplicationState:
    """
    Central state manager for the Palette Milker application.
    
    This class manages application-wide state, providing a clean
    separation between business logic and UI components.
    """
```

The `ApplicationState` class is responsible for:

1. Managing application-wide state (theme, view mode, display settings)
2. Coordinating with the palette model
3. Maintaining history for undo/redo functionality
4. Broadcasting state changes to UI components
5. Providing a clean interface for state access and modification

## Message Classes

The ApplicationState module defines several message classes for communication with UI components:

### StateChanged

```python
class StateChanged(Message):
    """Base message for state changes."""
    
    def __init__(self, key: str, value: Any) -> None:
        """
        Initialize with the key and value that changed.
        
        Args:
            key: The name of the state property that changed
            value: The new value of the property
        """
        self.key = key
        self.value = value
        super().__init__()
```

This message is sent whenever a state property changes, allowing components to react to specific state changes.

### ThemeChanged

```python
class ThemeChanged(Message):
    """Message sent when the application theme changes."""
    
    def __init__(self, is_dark: bool) -> None:
        """
        Initialize with the new theme setting.
        
        Args:
            is_dark: Whether dark mode is enabled
        """
        self.is_dark = is_dark
        super().__init__()
```

This specialized message is sent when the theme changes, allowing components to update their appearance.

### ViewMode Enum

```python
class ViewMode(Enum):
    """Different view modes for the application."""
    PALETTE = "palette"
    COLOR_PICKER = "color_picker"
    EXPORT = "export"
    PALETTE_ORGANIZATION = "palette_organization"
    ACCESSIBILITY = "accessibility"
```

An enumeration of the different view modes available in the application.

## Initialization

```python
def __init__(self, app: Any = None) -> None:
    """
    Initialize the application state.
    
    Args:
        app: Optional reference to the main application
    """
```

The constructor initializes default state values and sets up the palette model. The optional `app` parameter can be used to bind the state manager to an application instance for message passing.

## Properties

### State Properties

| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `is_dark_mode` | `bool` | Whether dark mode is enabled | `True` |
| `current_view` | `ViewMode` | Current view mode | `ViewMode.PALETTE` |
| `show_hex_values` | `bool` | Whether to show hex values | `True` |
| `show_color_details` | `bool` | Whether to show color details | `False` |
| `is_help_visible` | `bool` | Whether help is visible | `False` |
| `history` | `List[Dict[str, Any]]` | List of state history snapshots | `[]` |
| `history_index` | `int` | Current index in history | `-1` |

Each of these properties has a corresponding getter and setter, implemented as Python properties. The setters automatically trigger appropriate messages when the value changes.

Example implementation of a property:

```python
@property
def is_dark_mode(self) -> bool:
    """Whether dark mode is enabled."""
    return self._is_dark_mode

@is_dark_mode.setter
def is_dark_mode(self, value: bool) -> None:
    """Set dark mode state."""
    if self._is_dark_mode != value:
        self._is_dark_mode = value
        if self.app:
            self.app.post_message(ThemeChanged(value))
            self.app.post_message(StateChanged("is_dark_mode", value))
```

## Methods

### Palette Management

#### save_palettes

```python
def save_palettes(self) -> bool:
    """
    Save the current palette collection to file.
    
    Returns:
        Boolean indicating success or failure
    """
```

Saves the current palette collection to a JSON file.

### State Manipulation

#### set_dark_mode

```python
def set_dark_mode(self, enabled: bool) -> None:
    """
    Set the dark mode state.
    
    Args:
        enabled: Whether dark mode should be enabled
    """
```

Sets the dark mode state and broadcasts appropriate messages.

#### toggle_dark_mode

```python
def toggle_dark_mode(self) -> bool:
    """
    Toggle the dark mode state.
    
    Returns:
        The new dark mode state
    """
```

Toggles the dark mode state between on and off. Returns the new state.

#### set_view

```python
def set_view(self, view: ViewMode) -> None:
    """
    Set the current view mode.
    
    Args:
        view: The view mode to set
    """
```

Sets the current view mode.

#### toggle_hex_display

```python
def toggle_hex_display(self) -> bool:
    """
    Toggle hex value display.
    
    Returns:
        The new hex display state
    """
```

Toggles whether hex values are shown. Returns the new state.

#### toggle_color_details

```python
def toggle_color_details(self) -> bool:
    """
    Toggle color details display.
    
    Returns:
        The new color details state
    """
```

Toggles whether color details are shown. Returns the new state.

#### toggle_help

```python
def toggle_help(self) -> bool:
    """
    Toggle help visibility.
    
    Returns:
        The new help visibility state
    """
```

Toggles whether help is visible. Returns the new state.

### History Management

#### add_to_history

```python
def add_to_history(self, state: Dict[str, Any]) -> None:
    """
    Add a state snapshot to the history for undo/redo.
    
    Args:
        state: The state snapshot to add
    """
```

Adds a state snapshot to the history. If the history index is not at the end, truncates the history at the current index before adding the new state.

#### can_undo

```python
def can_undo(self) -> bool:
    """
    Check if undo is available.
    
    Returns:
        True if undo is available, False otherwise
    """
```

Returns whether an undo operation is available (i.e., if the history index is greater than 0).

#### can_redo

```python
def can_redo(self) -> bool:
    """
    Check if redo is available.
    
    Returns:
        True if redo is available, False otherwise
    """
```

Returns whether a redo operation is available (i.e., if the history index is less than the last index in the history).

#### undo

```python
def undo(self) -> Optional[Dict[str, Any]]:
    """
    Undo the last action by restoring a previous state.
    
    Returns:
        The restored state, or None if undo is not available
    """
```

Undoes the last action by moving back in history. Returns the restored state or None if undo is not available.

#### redo

```python
def redo(self) -> Optional[Dict[str, Any]]:
    """
    Redo a previously undone action.
    
    Returns:
        The restored state, or None if redo is not available
    """
```

Redoes a previously undone action by moving forward in history. Returns the restored state or None if redo is not available.

#### capture_current_state

```python
def capture_current_state(self) -> Dict[str, Any]:
    """
    Capture the current application state for history.
    
    Returns:
        Dictionary with the current state
    """
```

Captures the current application state as a dictionary, suitable for adding to history.

### Application Binding

#### bind_to_app

```python
def bind_to_app(self, app: Any) -> None:
    """
    Bind this state manager to an application.
    
    Args:
        app: The application to bind to
    """
```

Binds the state manager to an application instance, allowing it to send messages to the application.

### Palette Model Delegation

The ApplicationState class provides several methods that delegate to the underlying palette model:

#### get_active_palette

```python
def get_active_palette(self) -> Optional[Palette]:
    """
    Get the active palette.
    
    Returns:
        The active palette or None
    """
```

Returns the active palette or None if no palette is active.

#### get_active_color

```python
def get_active_color(self) -> Optional[Color]:
    """
    Get the active color.
    
    Returns:
        The active color or None
    """
```

Returns the active color or None if no color is active.

#### set_active_palette

```python
def set_active_palette(self, palette_id: str) -> None:
    """
    Set the active palette.
    
    Args:
        palette_id: ID of the palette to activate
    """
```

Sets the active palette by ID.

#### set_active_color_index

```python
def set_active_color_index(self, index: int) -> None:
    """
    Set the active color index.
    
    Args:
        index: Index of the color to activate
    """
```

Sets the active color index.

#### update_active_color

```python
def update_active_color(self, color: Union[str, Color]) -> None:
    """
    Update the active color.
    
    Args:
        color: New color value
    """
```

Updates the active color with a new value.

## Example Usage

```python
# Create application state manager
app_state = ApplicationState()

# Toggle dark mode
is_dark = app_state.toggle_dark_mode()
print(f"Dark mode enabled: {is_dark}")

# Set the view mode
app_state.set_view(ViewMode.COLOR_PICKER)

# Capture the current state for history
state = app_state.capture_current_state()
app_state.add_to_history(state)

# Create a new palette
palette = app_state.palette_model.add_palette(
    name="My Palette", 
    colors=["#FF0000", "#00FF00", "#0000FF"]
)

# Set as active palette
app_state.set_active_palette(palette.palette_id)

# Select the second color
app_state.set_active_color_index(1)

# Update the active color
app_state.update_active_color("#FFFF00")

# Save palettes
success = app_state.save_palettes()
print(f"Palettes saved: {success}")
```

## Implementation Details

### State Initialization

The ApplicationState class initializes several private state variables in its constructor:

```python
self._is_dark_mode = True
self._current_view = ViewMode.PALETTE
self._show_hex_values = True
self._show_color_details = False
self._is_help_visible = False
self._history = []
self._history_index = -1
```

Each of these private variables has a corresponding public property with a getter and setter.

### Palette Model Initialization

The ApplicationState class initializes a palette model in its constructor:

```python
def _initialize_palette_model(self) -> None:
    """Initialize the palette model with default data."""
    # Create a default palette collection
    self.palette_collection = self._create_default_palette_collection()
    
    # Create palette model
    self.palette_model = PaletteModel(self.palette_collection)
    
    # Bind the model to this state manager for message handling
    if self.app:
        self.palette_model.bind_to_app(self.app)
```

### Message Broadcasting

When a state property changes, the ApplicationState class broadcasts appropriate messages to the application:

```python
if self.app:
    self.app.post_message(StateChanged("property_name", new_value))
```

This allows UI components to react to state changes through the Textual message system. 
