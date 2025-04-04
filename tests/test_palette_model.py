"""
Unit tests for the palette_model module.

This module contains tests for the Palette and PaletteCollection classes.
"""

import json
import os
import tempfile
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from src.models.color_model import Color
from src.models.palette_model import Palette
from src.models.palette_model import PaletteCollection
from src.models.palette_model import PaletteModel


class TestPalette:
    """Test suite for the Palette class."""

    def test_palette_creation(self):
        """Test creating a palette."""
        name = "Test Palette"
        colors = ["#FF0000", "#00FF00", "#0000FF"]

        palette = Palette(name, colors)

        # Check attributes
        assert palette.name == name
        assert len(palette.colors) == 3
        assert palette.palette_id is not None
        assert isinstance(palette.colors[0], Color)
        assert isinstance(palette.colors[1], Color)
        assert isinstance(palette.colors[2], Color)

        # Check hex colors
        assert palette.hex_colors == colors

    def test_palette_equality(self):
        """Test palette equality comparison."""
        # Two palettes with same ID should be equal
        palette1 = Palette("Test", ["#FF0000"])
        palette2 = Palette("Different", ["#00FF00"])
        palette2.palette_id = palette1.palette_id  # Force same ID

        assert palette1 == palette2

        # Different IDs should not be equal
        palette3 = Palette("Test", ["#FF0000"])
        assert palette1 != palette3

        # Non-palette objects should not be equal
        assert palette1 != "not a palette"

    def test_palette_length(self):
        """Test len() operation on palettes."""
        palette = Palette("Test", ["#FF0000", "#00FF00", "#0000FF"])
        assert len(palette) == 3

        # Empty palette
        empty_palette = Palette("Empty", [])
        assert len(empty_palette) == 0

    def test_add_color(self):
        """Test adding a color to a palette."""
        palette = Palette("Test", ["#FF0000"])
        assert len(palette) == 1

        # Add a color as string
        palette.add_color("#00FF00")
        assert len(palette) == 2
        assert palette.hex_colors[1] == "#00FF00"

        # Add a color as Color instance
        palette.add_color(Color("#0000FF"))
        assert len(palette) == 3
        assert palette.hex_colors[2] == "#0000FF"

    def test_remove_color(self):
        """Test removing a color from a palette."""
        palette = Palette("Test", ["#FF0000", "#00FF00", "#0000FF"])
        assert len(palette) == 3

        # Remove middle color
        removed = palette.remove_color(1)
        assert len(palette) == 2
        assert removed.hex == "#00FF00"
        assert palette.hex_colors == ["#FF0000", "#0000FF"]

        # Remove with invalid index
        with pytest.raises(IndexError):
            palette.remove_color(10)

    def test_get_color(self):
        """Test getting a color from a palette."""
        palette = Palette("Test", ["#FF0000", "#00FF00", "#0000FF"])

        # Get existing color
        color = palette.get_color(1)
        assert color.hex == "#00FF00"

        # Get with invalid index
        with pytest.raises(IndexError):
            palette.get_color(10)

    def test_set_color(self):
        """Test setting a color in a palette."""
        palette = Palette("Test", ["#FF0000", "#00FF00", "#0000FF"])

        # Set with string
        palette.set_color(1, "#FFFF00")
        assert palette.hex_colors == ["#FF0000", "#FFFF00", "#0000FF"]

        # Set with Color instance
        palette.set_color(2, Color("#00FFFF"))
        assert palette.hex_colors == ["#FF0000", "#FFFF00", "#00FFFF"]

        # Set with invalid index
        with pytest.raises(IndexError):
            palette.set_color(10, "#FFFFFF")

    def test_to_dict(self):
        """Test converting a palette to a dictionary."""
        palette = Palette("Test", ["#FF0000", "#00FF00", "#0000FF"])

        data = palette.to_dict()
        assert data["name"] == "Test"
        assert data["colors"] == ["#FF0000", "#00FF00", "#0000FF"]
        assert "palette_id" in data
        assert data["palette_id"] == palette.palette_id


class TestPaletteCollection:
    """Test suite for the PaletteCollection class."""

    def test_collection_creation(self):
        """Test creating a palette collection."""
        # Empty collection
        collection = PaletteCollection()
        assert len(collection.palettes) == 0

        # Collection with palettes
        palette1 = Palette("Test1", ["#FF0000"])
        palette2 = Palette("Test2", ["#00FF00"])

        collection = PaletteCollection([palette1, palette2])
        assert len(collection.palettes) == 2
        assert collection.palettes[0] == palette1
        assert collection.palettes[1] == palette2

    def test_add_palette(self):
        """Test adding a palette to a collection."""
        collection = PaletteCollection()
        assert len(collection.palettes) == 0

        # Add a palette
        palette = Palette("Test", ["#FF0000"])
        collection.add_palette(palette)
        assert len(collection.palettes) == 1
        assert collection.palettes[0] == palette

        # Add another palette
        palette2 = Palette("Test2", ["#00FF00"])
        collection.add_palette(palette2)
        assert len(collection.palettes) == 2
        assert collection.palettes[1] == palette2

    def test_remove_palette(self):
        """Test removing a palette from a collection."""
        palette1 = Palette("Test1", ["#FF0000"])
        palette2 = Palette("Test2", ["#00FF00"])
        collection = PaletteCollection([palette1, palette2])

        # Remove by palette object
        removed = collection.remove_palette(palette1)
        assert removed is True
        assert len(collection.palettes) == 1
        assert collection.palettes[0] == palette2

        # Remove by ID
        collection = PaletteCollection([palette1, palette2])
        removed = collection.remove_palette_by_id(palette2.palette_id)
        assert removed is True
        assert len(collection.palettes) == 1
        assert collection.palettes[0] == palette1

        # Remove non-existent palette
        removed = collection.remove_palette(Palette("NotExists", []))
        assert removed is False

    def test_get_palette_by_id(self):
        """Test getting a palette by ID."""
        palette1 = Palette("Test1", ["#FF0000"])
        palette2 = Palette("Test2", ["#00FF00"])
        collection = PaletteCollection([palette1, palette2])

        # Get existing palette
        palette = collection.get_palette_by_id(palette1.palette_id)
        assert palette == palette1

        # Get non-existent palette
        palette = collection.get_palette_by_id("non-existent-id")
        assert palette is None

    def test_get_palette_by_name(self):
        """Test getting a palette by name."""
        palette1 = Palette("Test1", ["#FF0000"])
        palette2 = Palette("Test2", ["#00FF00"])
        collection = PaletteCollection([palette1, palette2])

        # Get existing palette
        palette = collection.get_palette_by_name("Test1")
        assert palette == palette1

        # Get non-existent palette
        palette = collection.get_palette_by_name("NonExistent")
        assert palette is None

    def test_to_dict_list(self):
        """Test converting a collection to a list of dictionaries."""
        palette1 = Palette("Test1", ["#FF0000"])
        palette2 = Palette("Test2", ["#00FF00"])
        collection = PaletteCollection([palette1, palette2])

        data = collection.to_dict_list()
        assert len(data) == 2
        assert data[0]["name"] == "Test1"
        assert data[1]["name"] == "Test2"
        assert data[0]["colors"] == ["#FF0000"]
        assert data[1]["colors"] == ["#00FF00"]

    def test_save_load_from_file(self):
        """Test saving and loading collection from a file."""
        palette1 = Palette("Test1", ["#FF0000"])
        palette2 = Palette("Test2", ["#00FF00"])
        collection = PaletteCollection([palette1, palette2])

        # Save to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp_file:
            try:
                filename = tmp_file.name

                # Save
                success = collection.save_to_file(filename)
                assert success is True

                # Load
                loaded_collection = PaletteCollection.load_from_file(filename)
                assert loaded_collection is not None
                assert len(loaded_collection.palettes) == 2
                assert loaded_collection.palettes[0].name == "Test1"
                assert loaded_collection.palettes[1].name == "Test2"
                assert loaded_collection.palettes[0].hex_colors == ["#FF0000"]
                assert loaded_collection.palettes[1].hex_colors == ["#00FF00"]
            finally:
                # Clean up
                if os.path.exists(filename):
                    os.unlink(filename)

    def test_load_from_nonexistent_file(self):
        """Test loading from a non-existent file."""
        collection = PaletteCollection.load_from_file("non_existent_file.json")
        assert collection is None


class TestPaletteModel:
    """Test suite for the PaletteModel class."""

    def test_model_initialization(self):
        """Test initializing a palette model."""
        # Create a collection with palettes
        palette1 = Palette("Test1", ["#FF0000"])
        palette2 = Palette("Test2", ["#00FF00"])
        collection = PaletteCollection([palette1, palette2])

        # Create model
        model = PaletteModel(collection)

        # Check attributes
        assert model._collection == collection
        assert model.active_palette_id is None
        assert model.active_color_index == 0
        assert model.active_palette is None
        assert model.active_color is None

    def test_set_active_palette(self):
        """Test setting the active palette."""
        # Create a collection with palettes
        palette1 = Palette("Test1", ["#FF0000"])
        palette2 = Palette("Test2", ["#00FF00"])
        collection = PaletteCollection([palette1, palette2])

        # Create model
        model = PaletteModel(collection)

        # Initially no active palette
        assert model.active_palette is None

        # Set active palette
        model.set_active_palette(palette1.palette_id)
        assert model.active_palette_id == palette1.palette_id
        assert model.active_palette == palette1

        # Set to non-existent palette
        model.set_active_palette("non-existent")
        # Should still be palette1 since non-existent ID is invalid
        assert model.active_palette_id == palette1.palette_id

    def test_set_active_color_index(self):
        """Test setting the active color index."""
        # Create a collection with a palette
        palette = Palette("Test", ["#FF0000", "#00FF00", "#0000FF"])
        collection = PaletteCollection([palette])

        # Create model and set active palette
        model = PaletteModel(collection)
        model.set_active_palette(palette.palette_id)

        # Default index is 0
        assert model.active_color_index == 0
        assert model.active_color.hex == "#FF0000"

        # Set to valid index
        model.set_active_color_index(1)
        assert model.active_color_index == 1
        assert model.active_color.hex == "#00FF00"

        # Set to invalid index (negative)
        model.set_active_color_index(-1)
        # Should clamp to 0
        assert model.active_color_index == 0

        # Set to invalid index (too large)
        model.set_active_color_index(10)
        # Should clamp to max index (2)
        assert model.active_color_index == 2

    def test_add_palette(self):
        """Test adding a palette through the model."""
        # Create an empty collection
        collection = PaletteCollection()

        # Create model
        model = PaletteModel(collection)
        assert len(model._collection.palettes) == 0

        # Add a palette
        palette = model.add_palette("Test", ["#FF0000", "#00FF00"])
        assert len(model._collection.palettes) == 1
        assert model._collection.palettes[0] == palette
        assert palette.name == "Test"
        assert palette.hex_colors == ["#FF0000", "#00FF00"]

        # Make sure the palette has a valid ID
        assert palette.palette_id is not None

    def test_update_active_color(self):
        """Test updating the active color."""
        # Create a collection with a palette
        palette = Palette("Test", ["#FF0000", "#00FF00", "#0000FF"])
        collection = PaletteCollection([palette])

        # Create model and set active palette
        model = PaletteModel(collection)
        model.set_active_palette(palette.palette_id)
        model.set_active_color_index(1)  # Green

        # Update color to yellow
        model.update_active_color("#FFFF00")
        assert model.active_color.hex == "#FFFF00"
        assert palette.hex_colors == ["#FF0000", "#FFFF00", "#0000FF"]

        # Update with no active palette should not raise error
        model._active_palette_id = None
        model.update_active_color("#FFFFFF")  # Should not raise


if __name__ == "__main__":
    pytest.main(["-v", "test_palette_model.py"])
