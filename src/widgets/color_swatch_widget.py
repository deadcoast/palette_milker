from textual.message import Message
from textual.widget import Widget


class ColorSwatch(Widget):
    """Widget that displays a color swatch and handles interactions."""

    class SwatchClicked(Message):
        """Message sent when color swatch is clicked."""

        def __init__(self, sender: Widget, color_hex: str):
            super().__init__(sender)
            self.color_hex = color_hex

    def on_click(self, event) -> None:
        """Handle click events on the color swatch."""
        # Get the color at this swatch
        color = self.color
        # Send message to parent
        self.post_message(self.SwatchClicked(self, color))
