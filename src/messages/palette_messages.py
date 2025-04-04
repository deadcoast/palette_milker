"""
Standardized message classes for palette interactions.

This module defines message classes following Textual best practices
for communication between palette components.
"""

from typing import Union

from textual.message import Message
from textual.widget import Widget

from ..models.color_model import Color


class PaletteChangeRequest(Message):
    """Message sent to request a palette change."""

    def __init__(self, sender: Widget, palette_id: str) -> None:
        """
        Initialize a palette change request.

        Args:
            sender: The widget sending the request
            palette_id: ID of the palette to change to
        """
        super().__init__()
        self.palette_id = palette_id


class ColorChangeRequest(Message):
    """Message sent to request a color change in a palette."""

    def __init__(self, sender: Widget, color_index: int, color: Union[str, Color]) -> None:
        """
        Initialize a color change request.

        Args:
            sender: The widget sending the request
            color_index: Index of the color to change
            color: New color value
        """
        super().__init__()
        self.color_index = color_index
        self.color = color


class PaletteSelectionChanged(Message):
    """Message sent when the selected palette changes."""

    def __init__(self, sender: Widget, palette_id: str) -> None:
        """
        Initialize a palette selection changed message.

        Args:
            sender: The widget sending the message
            palette_id: ID of the newly selected palette
        """
        super().__init__()
        self.palette_id = palette_id


class ColorSelectionChanged(Message):
    """Message sent when the selected color changes."""

    def __init__(self, sender: Widget, color_index: int, color: Union[str, Color]) -> None:
        """
        Initialize a color selection changed message.

        Args:
            sender: The widget sending the message
            color_index: Index of the newly selected color
            color: Selected color value
        """
        super().__init__()
        self.color_index = color_index
        self.color = color


class PaletteCreated(Message):
    """Message sent when a new palette is created."""

    def __init__(self, sender: Widget, palette_id: str, palette_name: str) -> None:
        """
        Initialize a palette created message.

        Args:
            sender: The widget sending the message
            palette_id: ID of the newly created palette
            palette_name: Name of the newly created palette
        """
        super().__init__()
        self.palette_id = palette_id
        self.palette_name = palette_name


class PaletteDeleted(Message):
    """Message sent when a palette is deleted."""

    def __init__(self, sender: Widget, palette_id: str) -> None:
        """
        Initialize a palette deleted message.

        Args:
            sender: The widget sending the message
            palette_id: ID of the deleted palette
        """
        super().__init__()
        self.palette_id = palette_id


class PaletteUpdated(Message):
    """Message sent when a palette is updated."""

    def __init__(self, sender: Widget, palette_id: str) -> None:
        """
        Initialize a palette updated message.

        Args:
            sender: The widget sending the message
            palette_id: ID of the updated palette
        """
        super().__init__()
        self.palette_id = palette_id
