# Textual Navigation Best Practices

This guide outlines best practices for implementing effective navigation in Textual applications, based on our work in RERUN_11 of the Palette Milker project.

## 1. Keyboard Navigation

### Consistent Keyboard Shortcuts

Define consistent keyboard shortcuts across your application:

```python
BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
    # Navigation between screens
    Binding("1", "view_palette", "Palette view"),
    Binding("2", "view_color_picker", "Color picker"),
    Binding("3", "view_export", "Export options"),
    
    # Universal navigation
    Binding("escape", "back", "Back", priority=True),
    Binding("f1", "help", "Help"),
]
```

### Action Methods

Implement clear action methods for your bindings:

```python
def action_view_palette(self) -> None:
    """Switch to palette view."""
    self.app.switch_screen("main")

def action_view_color_picker(self) -> None:
    """Switch to color picker view."""
    self.app.switch_screen(ColorPickerScreen())

def action_back(self) -> None:
    """Go back to the previous screen."""
    if isinstance(self, ModalScreen):
        self.dismiss()
    else:
        self.app.switch_screen("main")
```

### Keyboard Focus Management

Ensure keyboard focus is managed properly:

```python
def on_mount(self) -> None:
    """Set initial focus when the screen mounts."""
    # Focus the main interactive element
    self.query_one("#main-button").focus()
```

## 2. Screen Management

### Screen Navigation Flow

Design a clear navigation flow between screens:

```python
def on_button_pressed(self, event: Button.Pressed) -> None:
    """Handle button press events."""
    button_id = event.button.id
    
    if button_id == "settings":
        # Push settings screen onto the stack (can return with Escape)
        self.app.push_screen(SettingsScreen())
    elif button_id == "new-document":
        # Switch to a new screen (replace current)
        self.app.switch_screen(DocumentScreen())
    elif button_id == "help":
        # Show modal screen on top
        self.app.push_screen(HelpScreen())
```

### Modal Dialogs

Use modal screens for focused interaction:

```python
class ConfirmDialog(ModalScreen):
    """Modal confirmation dialog that returns a boolean result."""
    
    def compose(self) -> ComposeResult:
        with Container():
            yield Static("Are you sure?")
            with Horizontal():
                yield Button("Yes", id="confirm", variant="primary")
                yield Button("No", id="cancel")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "confirm":
            self.dismiss(True)
        else:
            self.dismiss(False)

# Usage:
async def confirm_action(self) -> None:
    confirmed = await self.app.push_screen(ConfirmDialog())
    if confirmed:
        self.perform_action()
```

## 3. Tab Order Control

### Logical Tab Sequence

Ensure a logical tab sequence for interactive elements:

```python
def compose(self) -> ComposeResult:
    """Compose the UI with a logical tab order."""
    # Elements will be focused in the order they're yielded
    yield Button("1. First", id="first")
    yield Button("2. Second", id="second")
    yield Button("3. Third", id="third")
```

### Tabulation Groups

Group related controls for tabbing:

```python
def compose(self) -> ComposeResult:
    """Group related controls for tabbing."""
    with Container(id="form-group"):
        yield Input(placeholder="Username")
        yield Input(placeholder="Password", password=True)
        yield Button("Log In", variant="primary")
    
    # Tab will cycle within the form-group before moving on
    with Container(id="secondary-group"):
        yield Button("Register")
        yield Button("Forgot Password")
```

## 4. Visual Feedback

### Focus Indicators

Provide clear visual feedback for focused elements:

```css
/* In your CSS */
Button:focus {
    border: tall $accent;
    background: $accent-darken-1;
}

Input:focus {
    border: tall $accent;
}
```

### Active Element Indication

Clearly indicate the active element or section:

```python
def on_button_pressed(self, event: Button.Pressed) -> None:
    """Handle selection and update active state."""
    button_id = event.button.id
    
    # Remove active class from all buttons
    for button in self.query(Button):
        button.remove_class("active")
    
    # Add active class to selected button
    event.button.add_class("active")
    
    # Update content based on selection
    self.update_content(button_id)
```

## 5. Help and Documentation

### Contextual Help

Provide contextual help for navigation:

```python
def compose(self) -> ComposeResult:
    with Container():
        yield Static("Press 'h' for help on this screen", id="help-tip")
        # Main content...
```

### Keyboard Shortcut Display

Display available keyboard shortcuts:

```python
def on_mount(self) -> None:
    """Show keyboard shortcuts reminder."""
    shortcuts = [
        ("↑/↓", "Navigate items"),
        ("Enter", "Select"),
        ("Esc", "Go back")
    ]
    
    shortcut_text = " | ".join([f"{key}: {desc}" for key, desc in shortcuts])
    self.query_one("#shortcuts-bar").update(shortcut_text)
```

### Help Screen

Implement a comprehensive help screen:

```python
class HelpScreen(ModalScreen):
    """Help screen showing available commands."""
    
    BINDINGS = [Binding("escape", "dismiss", "Close")]
    
    def compose(self) -> ComposeResult:
        with ScrollableContainer():
            yield Static("KEYBOARD SHORTCUTS", classes="title")
            
            yield Static("Navigation", classes="category")
            with Grid():
                yield Static("Tab/Shift+Tab", classes="shortcut-key")
                yield Static("Navigate between elements", classes="description")
                # More shortcuts...
```

## 6. Error Navigation

### Error Recovery

Help users recover from errors:

```python
def action_submit_form(self) -> None:
    """Submit form with error navigation."""
    try:
        # Validate form
        errors = self.validate_form()
        
        if errors:
            # Focus the first field with an error
            first_error_field = self.query_one(f"#{errors[0]['field']}", Input)
            first_error_field.focus()
            
            # Show error message
            self.notify(errors[0]['message'], severity="error")
            return
            
        # Process valid form
        self.submit_form()
    except Exception as e:
        self.notify(f"Error: {str(e)}", severity="error")
```

## 7. Message-Based Navigation

### Navigation Messages

Use messages for navigation between components:

```python
class NavigationRequest(Message):
    """Message to request navigation to a specific screen."""
    
    def __init__(self, screen_name: str, params: Optional[Dict] = None) -> None:
        self.screen_name = screen_name
        self.params = params or {}
        super().__init__()

# Child widget can request navigation
self.post_message(NavigationRequest("settings", {"section": "display"}))

# Parent handles the request
def on_navigation_request(self, message: NavigationRequest) -> None:
    """Handle navigation requests from child widgets."""
    if message.screen_name == "settings":
        self.app.push_screen(SettingsScreen(**message.params))
```

## 8. Responsive Navigation

### Adapt to Available Space

Adapt navigation patterns based on available space:

```python
def on_resize(self) -> None:
    """Adjust navigation style based on available width."""
    if self.size.width < 80:
        # Switch to compact navigation
        self.add_class("compact-nav")
    else:
        # Use full navigation
        self.remove_class("compact-nav")
```

## Conclusion

Implementing proper navigation is essential for creating usable Textual applications. By following these best practices, you can ensure your application is accessible, intuitive, and pleasant to use with both keyboard and mouse navigation.

Remember that good navigation should be:
- Consistent across the application
- Clearly visible and discoverable
- Accessible via both keyboard and mouse
- Well-documented with help available when needed 
