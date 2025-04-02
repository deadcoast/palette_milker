"""
Palette model for the Milky Color Suite.

This module defines the Palette and PaletteCollection classes for managing
color palettes throughout the application.
"""

import json
import os
import uuid
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from .color_model import Color


class Palette:
    """
    Represents a color palette in the Milky Color Suite.

    A palette contains a collection of colors with a name and unique ID.
    """

    def __init__(
        self, name: str, colors: Optional[List[Union[str, Color]]] = None, palette_id: Optional[str] = None
    ) -> None:
        """
        Initialize a Palette instance.

        Args:
            name: Name of the palette
            colors: List of colors (hex strings or Color instances)
            palette_id: Unique ID for the palette (generated if not provided)
        """
        self.name = name
        self.palette_id = palette_id or str(uuid.uuid4())

        # Convert all colors to Color instances
        self._colors: List[Color] = []
        if colors:
            for color in colors:
                if isinstance(color, Color):
                    self._colors.append(color)
                else:
                    self._colors.append(Color(color))

    @property
    def colors(self) -> List[Color]:
        """
        Get the colors in the palette.

        Returns:
            List of Color instances
        """
        return self._colors.copy()

    @property
    def hex_colors(self) -> List[str]:
        """
        Get the colors in the palette as hex strings.

        Returns:
            List of hex color strings
        """
        return [color.hex for color in self._colors]

    def add_color(self, color: Union[str, Color]) -> None:
        """
        Add a color to the palette.

        Args:
            color: Color to add (hex string or Color instance)
        """
        if isinstance(color, Color):
            self._colors.append(color)
        else:
            self._colors.append(Color(color))

    def remove_color(self, index: int) -> Optional[Color]:
        """
        Remove a color from the palette.

        Args:
            index: Index of the color to remove

        Returns:
            The removed color, or None if the index is invalid
        """
        return self._colors.pop(index) if 0 <= index < len(self._colors) else None

    def update_color(self, index: int, color: Union[str, Color]) -> bool:
        """
        Update a color in the palette.

        Args:
            index: Index of the color to update
            color: New color (hex string or Color instance)

        Returns:
            True if the color was updated, False otherwise
        """
        if 0 <= index < len(self._colors):
            self._colors[index] = color if isinstance(color, Color) else Color(color)
            return True
        return False

    def get_color(self, index: int) -> Optional[Color]:
        """
        Get a color from the palette.

        Args:
            index: Index of the color to get

        Returns:
            The color at the specified index, or None if the index is invalid
        """
        return self._colors[index] if 0 <= index < len(self._colors) else None

    def clear(self) -> None:
        """Clear all colors from the palette."""
        self._colors.clear()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the palette to a dictionary.

        Returns:
            Dictionary representation of the palette
        """
        return {"id": self.palette_id, "name": self.name, "colors": self.hex_colors}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Palette":
        """
        Create a Palette instance from a dictionary.

        Args:
            data: Dictionary representation of a palette

        Returns:
            A Palette instance

        Raises:
            ValueError: If the dictionary is invalid
        """
        if any(key not in data for key in ("id", "name", "colors")):
            raise ValueError("Invalid palette data")

        return cls(name=data["name"], colors=data["colors"], palette_id=data["id"])

    def __len__(self) -> int:
        """Get the number of colors in the palette."""
        return len(self._colors)

    def __getitem__(self, index: int) -> Color:
        """Get a color from the palette by index."""
        return self._colors[index]

    def __iter__(self):
        """Iterate over the colors in the palette."""
        return iter(self._colors)


class PaletteCollection:
    """
    Manages a collection of palettes.

    This class provides methods for adding, removing, and retrieving palettes,
    as well as loading and saving palette collections to and from files.
    """

    def __init__(self, palettes: Optional[List[Palette]] = None) -> None:
        """
        Initialize a PaletteCollection instance.

        Args:
            palettes: Initial list of palettes
        """
        self._palettes: Dict[str, Palette] = {}

        if palettes:
            for palette in palettes:
                self._palettes[palette.palette_id] = palette

        # Create a default palette if none provided
        if not self._palettes:
            default_palette = Palette(
                name="Default",
                colors=["#FFFFFF", "#CCCCCC", "#999999", "#666666", "#333333", "#000000", "#FF0000", "#00FF00"],
            )
            self._palettes[default_palette.palette_id] = default_palette

    @property
    def palettes(self) -> List[Palette]:
        """
        Get all palettes in the collection.

        Returns:
            List of Palette instances
        """
        return list(self._palettes.values())

    def add_palette(self, palette: Palette) -> None:
        """
        Add a palette to the collection.

        Args:
            palette: Palette to add
        """
        self._palettes[palette.palette_id] = palette

    def remove_palette(self, palette_id: str) -> Optional[Palette]:
        """
        Remove a palette from the collection.

        Args:
            palette_id: ID of the palette to remove

        Returns:
            The removed palette, or None if the palette was not found
        """
        return self._palettes.pop(palette_id, None)

    def get_palette(self, palette_id: str) -> Optional[Palette]:
        """
        Get a palette from the collection.

        Args:
            palette_id: ID of the palette to get

        Returns:
            The palette with the specified ID, or None if not found
        """
        return self._palettes.get(palette_id)

    def get_palette_by_name(self, name: str) -> Optional[Palette]:
        """
        Get a palette from the collection by name.

        Args:
            name: Name of the palette to get

        Returns:
            The first palette with the specified name, or None if not found
        """
        return next((palette for palette in self._palettes.values() if palette.name == name), None)

    def clear(self) -> None:
        """Clear all palettes from the collection."""
        self._palettes.clear()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the palette collection to a dictionary.

        Returns:
            Dictionary representation of the palette collection
        """
        return {"palettes": [palette.to_dict() for palette in self._palettes.values()]}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PaletteCollection":
        """
        Create a PaletteCollection instance from a dictionary.

        Args:
            data: Dictionary representation of a palette collection

        Returns:
            A PaletteCollection instance

        Raises:
            ValueError: If the dictionary is invalid
        """
        if "palettes" not in data or not isinstance(data["palettes"], list):
            raise ValueError("Invalid palette collection data")

        palettes = [Palette.from_dict(palette_data) for palette_data in data["palettes"]]
        return cls(palettes)

    def save_to_file(self, file_path: str) -> bool:
        """
        Save the palette collection to a file.

        Args:
            file_path: Path to save the file to

        Returns:
            True if the file was saved successfully, False otherwise
        """
        try:
            with open(file_path, "w") as f:
                json.dump(self.to_dict(), f, indent=2)
            return True
        except Exception:
            return False

    @classmethod
    def load_from_file(cls, file_path: str) -> Optional["PaletteCollection"]:
        """
        Load a palette collection from a file.

        Args:
            file_path: Path to load the file from

        Returns:
            A PaletteCollection instance, or None if the file could not be loaded
        """
        try:
            if not os.path.exists(file_path):
                return None

            with open(file_path, "r") as f:
                data = json.load(f)

            return cls.from_dict(data)
        except Exception:
            return None

    def __len__(self) -> int:
        """Get the number of palettes in the collection."""
        return len(self._palettes)

    def __iter__(self):
        """Iterate over the palettes in the collection."""
        return iter(self._palettes.values())
