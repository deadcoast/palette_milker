from typing import Optional

from textual.events import Click
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget


class ColorSwatch(Widget):
    """Widget that displays a color swatch and handles interactions."""

    # Define the reactive color property with a default value
    color: reactive[str] = reactive("#FFFFFF")

    class SwatchClicked(Message):
        """Message sent when color swatch is clicked."""

        def __init__(self, sender: Widget, color_hex: str):
            # Always call super().__init__() with no arguments
            super().__init__()
            # Store the color value
            self.color_hex = color_hex

    def __init__(self, color: str = "#FFFFFF", widget_id: Optional[str] = None, classes: Optional[str] = None) -> None:
        """
        Initialize the color swatch widget.

        Args:
            color: The color value as a hex string
            widget_id: Optional widget ID
            classes: Optional CSS classes
        """
        super().__init__(id=widget_id, classes=classes)
        # Set the color property
        self.color = color

    def on_click(self, event: Click) -> None:
        """
        Handle click events on the color swatch.

        Args:
            event: The click event
        """
        # Send message to parent with current color
        self.post_message(self.SwatchClicked(self, self.color))
