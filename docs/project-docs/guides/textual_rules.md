
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

These best practices address the issues found in your codebase and provide a solid foundation for building robust Textual applications. The file serves as both documentation and code examples that can be referenced when developing your application.
