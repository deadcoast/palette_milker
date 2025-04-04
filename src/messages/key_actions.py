"""
Key action message classes for the Palette Milker application.

This module defines standard message classes for key and palette actions
to ensure consistent communication between components.
"""

from typing import Any
from typing import Dict
from typing import Optional

from textual.message import Message


class KeyActionRequest(Message):
    """
    Message sent when a key action is requested.

    This standardized message replaces custom key handlers with
    a more consistent approach using Textual's message system.
    """

    def __init__(self, action: str, key: Optional[str] = None, data: Optional[Dict[str, Any]] = None) -> None:
        """
        Initialize a key action request message.

        Args:
            action: The action to perform (corresponds to action_* methods)
            key: Optional key that triggered the action
            data: Optional data associated with the action
        """
        super().__init__()
        self.action = action
        self.key = key
        self.data = data or {}


class PaletteActionRequest(Message):
    """
    Message sent when a palette action is requested.

    This standardized message handles palette-specific actions.
    """

    def __init__(self, action: str, palette_id: Optional[str] = None, data: Optional[Dict[str, Any]] = None) -> None:
        """
        Initialize a palette action request message.

        Args:
            action: The action to perform (corresponds to action_* methods)
            palette_id: Optional ID of the palette to act on
            data: Optional data associated with the action
        """
        super().__init__()
        self.action = action
        self.palette_id = palette_id
        self.data = data or {}
