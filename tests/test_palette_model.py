"""
Unit tests for the palette_model module.

This module contains tests for the Palette and PaletteCollection classes.
"""

import os
import tempfile
from typing import List
from typing import Union
from typing import cast
from unittest.mock import Mock
from unittest.mock import patch

import pytest

from src.models.color_model import Color
from src.models.palette_model import Palette
from src.models.palette_model import PaletteCollection
from src.models.palette_model import PaletteModel


class TestPalette:
    """Test suite for the Palette class."""

    def test_palette_creation(self) -> None:
        """Test creating a palette."""
        name = "Test Palette"
        colors: List[Union[str, Color]] = ["#FF0000", "#00FF00", "#0000FF"]

        # Create palette with properly typed color list
        palette = Palette(name, colors)

        # Check attributes
        assert palette.name == name
        assert len(palette.colors) == 8  # Palette ensures at least 8 colors
        assert palette.palette_id is not None
        assert isinstance(palette.colors[0], Color)
        assert isinstance(palette.colors[1], Color)
        assert isinstance(palette.colors[2], Color)

        # Check hex colors - using case-insensitive comparison
        # The color library might normalize case (upper or lower)
        for i, expected in enumerate(colors[:3]):
            actual = palette.hex_colors[i]
            assert str(actual).upper() == str(expected).upper()

    def test_palette_equality(self) -> None:
        """Test palette equality comparison."""
        # Two palettes with different IDs should not be equal
        palette1 = Palette("Test", cast(List[Union[str, Color]], ["#FF0000"]))
        palette2 = Palette("Test", cast(List[Union[str, Color]], ["#FF0000"]))
        assert palette1.palette_id != palette2.palette_id

        # Two different palette instances should have different IDs by default
        assert palette1 != palette2

        # Different types are not equal
        assert palette1 != "not a palette"

    def test_palette_length(self) -> None:
        """Test len() operation on palettes."""
        palette = Palette("Test", cast(List[Union[str, Color]], ["#FF0000", "#00FF00", "#0000FF"]))
        assert len(palette) == 8  # Palette ensures at least 8 colors

        # Empty palette
        empty_palette = Palette("Empty", [])
        assert len(empty_palette) == 8  # Palette ensures at least 8 colors

    def test_add_color(self) -> None:
        """Test adding a color to a palette."""
        palette = Palette("Test", cast(List[Union[str, Color]], ["#FF0000"]))
        assert len(palette) == 8  # Palette ensures at least 8 colors

        # Add a color as string
        palette.add_color("#00FF00")
        assert len(palette) == 9
        assert palette.hex_colors[8].upper() == "#00FF00".upper()

        # Add a color as Color instance
        palette.add_color(Color("#0000FF"))
        assert len(palette) == 10
        assert palette.hex_colors[9].upper() == "#0000FF".upper()

    def test_remove_color(self) -> None:
        """Test removing a color from a palette."""
        palette = Palette("Test", cast(List[Union[str, Color]], ["#FF0000", "#00FF00", "#0000FF"]))
        assert len(palette) == 8  # Palette ensures at least 8 colors

        # Remove middle color
        removed = palette.remove_color(1)
        assert removed is not None
        assert removed.hex.upper() == "#00FF00".upper()
        assert palette.hex_colors[0].upper() == "#FF0000".upper()
        assert palette.hex_colors[1].upper() == "#0000FF".upper()

        # Invalid index should return None
        invalid_removed = palette.remove_color(100)
        assert invalid_removed is None

    def test_get_color(self) -> None:
        """Test getting a color from a palette."""
        palette = Palette("Test", cast(List[Union[str, Color]], ["#FF0000", "#00FF00", "#0000FF"]))

        # Get existing color
        color = palette.get_color(1)
        assert color is not None
        assert color.hex.upper() == "#00FF00".upper()

        # Invalid index should return None
        assert palette.get_color(100) is None

    def test_update_color(self) -> None:
        """Test updating a color in a palette."""
        palette = Palette("Test", cast(List[Union[str, Color]], ["#FF0000", "#00FF00", "#0000FF"]))

        # Update with string
        result = palette.update_color(1, "#FFFF00")
        assert result is True
        assert palette.hex_colors[1].upper() == "#FFFF00".upper()

        # Update with Color instance
        result = palette.update_color(2, Color("#00FFFF"))
        assert result is True
        assert palette.hex_colors[2].upper() == "#00FFFF".upper()

        # Invalid index should return False
        result = palette.update_color(100, "#FFFFFF")
        assert result is False

    def test_to_dict(self) -> None:
        """Test converting a palette to a dictionary."""
        palette = Palette("Test", cast(List[Union[str, Color]], ["#FF0000", "#00FF00", "#0000FF"]))

        data = palette.to_dict()
        assert data["name"] == "Test"

        # Check hex colors - using case-insensitive comparison
        saved_colors = [c.upper() for c in data["colors"][:3]]
        expected_colors = ["#FF0000", "#00FF00", "#0000FF"]
        expected_colors = [c.upper() for c in expected_colors]
        assert saved_colors == expected_colors

        assert "id" in data
        assert data["id"] == palette.palette_id


class TestPaletteCollection:
    """Test suite for the PaletteCollection class."""

    def test_collection_creation(self) -> None:
        """Test creating a palette collection."""
        # Empty collection creates a default palette
        collection = PaletteCollection()
        assert len(collection.palettes) == 1  # Creates a default palette

        # Collection with palettes
        palette1 = Palette("Test1", cast(List[Union[str, Color]], ["#FF0000"]))
        palette2 = Palette("Test2", cast(List[Union[str, Color]], ["#00FF00"]))

        collection = PaletteCollection([palette1, palette2])
        assert len(collection.palettes) == 2
        assert palette1 in collection.palettes
        assert palette2 in collection.palettes

    def test_add_palette(self) -> None:
        """Test adding a palette to a collection."""
        # Even with empty list initialization, a default palette is created
        collection = PaletteCollection([])
        assert len(collection.palettes) == 1

        self._add_pallete_to_collection("Test", "#FF0000", collection, 2)
        self._add_pallete_to_collection("Test2", "#00FF00", collection, 3)

    def _add_pallete_to_collection(self, arg0: str, arg1: str, collection: PaletteCollection, arg3: int) -> None:
        # Add a palette
        palette = Palette(arg0, cast(List[Union[str, Color]], [arg1]))
        collection.add_palette(palette)
        assert len(collection.palettes) == arg3
        assert palette in collection.palettes

    def test_remove_palette(self) -> None:
        """Test removing a palette from a collection."""
        palette1 = Palette("Test1", cast(List[Union[str, Color]], ["#FF0000"]))
        palette2 = Palette("Test2", cast(List[Union[str, Color]], ["#00FF00"]))
        collection = PaletteCollection([palette1, palette2])
        initial_count = len(collection.palettes)

        # Remove by palette ID
        removed = collection.remove_palette(palette1.palette_id)
        assert removed == palette1
        assert len(collection.palettes) == initial_count - 1
        assert palette1 not in collection.palettes
        assert palette2 in collection.palettes

        # Remove non-existent palette
        removed = collection.remove_palette("non-existent-id")
        assert removed is None

    def test_get_palette(self) -> None:
        """Test getting a palette by ID."""
        palette1 = Palette("Test1", cast(List[Union[str, Color]], ["#FF0000"]))
        palette2 = Palette("Test2", cast(List[Union[str, Color]], ["#00FF00"]))
        collection = PaletteCollection([palette1, palette2])

        # Get existing palette
        palette = collection.get_palette(palette1.palette_id)
        assert palette == palette1

        # Get non-existent palette
        palette = collection.get_palette("non-existent-id")
        assert palette is None

    def test_get_palette_by_name(self) -> None:
        """Test getting a palette by name."""
        palette1 = Palette("Test1", cast(List[Union[str, Color]], ["#FF0000"]))
        palette2 = Palette("Test2", cast(List[Union[str, Color]], ["#00FF00"]))
        collection = PaletteCollection([palette1, palette2])

        # Get existing palette
        palette = collection.get_palette_by_name("Test1")
        assert palette == palette1

        # Get non-existent palette
        palette = collection.get_palette_by_name("NonExistent")
        assert palette is None

    def test_to_dict(self) -> None:
        """Test converting a collection to a dictionary."""
        palette1 = Palette("Test1", cast(List[Union[str, Color]], ["#FF0000"]))
        palette2 = Palette("Test2", cast(List[Union[str, Color]], ["#00FF00"]))
        collection = PaletteCollection([palette1, palette2])

        data = collection.to_dict()
        assert "palettes" in data
        assert len(data["palettes"]) >= 2  # Could include default palette

        # Find our test palettes in the data
        palette_data = {p["name"]: p for p in data["palettes"]}
        assert "Test1" in palette_data
        assert "Test2" in palette_data

        # Check hex colors - using case-insensitive comparison
        test1_colors = [c.upper() for c in palette_data["Test1"]["colors"][:1]]
        test2_colors = [c.upper() for c in palette_data["Test2"]["colors"][:1]]
        assert test1_colors[0] == "#FF0000".upper()
        assert test2_colors[0] == "#00FF00".upper()

    def test_save_load_from_file(self) -> None:
        """Test saving and loading collection from a file."""
        palette1 = Palette("Test1", cast(List[Union[str, Color]], ["#FF0000"]))
        palette2 = Palette("Test2", cast(List[Union[str, Color]], ["#00FF00"]))
        collection = PaletteCollection([palette1, palette2])
        initial_count = len(collection.palettes)

        # Save to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp_file:
            filename = tmp_file.name
            try:
                self._extracted_from_test_save_load_from_file_13(
                    collection, filename, initial_count
                )
            finally:
                # Clean up
                if os.path.exists(filename):
                    os.unlink(filename)

    # TODO Rename this here and in `test_save_load_from_file`
    def _extracted_from_test_save_load_from_file_13(self, collection: PaletteCollection, filename: str, initial_count: int) -> None:
        # Save
        success = collection.save_to_file(filename)
        assert success is True

        # Load
        loaded_collection = PaletteCollection.load_from_file(filename)
        assert loaded_collection is not None
        assert len(loaded_collection.palettes) == initial_count

        # Match based on parameters we can predict
        palette_by_name = {p.name: p for p in loaded_collection.palettes}
        assert "Test1" in palette_by_name
        assert "Test2" in palette_by_name

        # Check hex colors - case insensitive
        test1 = palette_by_name["Test1"]
        test2 = palette_by_name["Test2"]
        assert test1.hex_colors[0].upper() == "#FF0000".upper()
        assert test2.hex_colors[0].upper() == "#00FF00".upper()

    def test_load_from_nonexistent_file(self) -> None:
        """Test loading from a non-existent file."""
        collection = PaletteCollection.load_from_file("non_existent_file.json")
        assert collection is None


class TestPaletteModel:
    """Test suite for the PaletteModel class."""

    def test_model_initialization(self) -> None:
        """Test initializing a palette model."""
        # Create a collection with palettes
        palette1 = Palette("Test1", cast(List[Union[str, Color]], ["#FF0000"]))
        palette2 = Palette("Test2", cast(List[Union[str, Color]], ["#00FF00"]))
        collection = PaletteCollection([palette1, palette2])

        # Create model
        model = PaletteModel(collection)

        # Check attributes
        assert model._collection == collection
        assert model.active_palette_id is not None
        assert model.active_color_index == 0
        assert model.active_palette is not None

    def test_set_active_palette(self) -> None:
        """Test setting the active palette."""
        # Create a collection with palettes
        palette1 = Palette("Test1", cast(List[Union[str, Color]], ["#FF0000"]))
        palette2 = Palette("Test2", cast(List[Union[str, Color]], ["#00FF00"]))
        collection = PaletteCollection([palette1, palette2])

        # Create model
        model = PaletteModel(collection)

        # Set active palette to the second palette
        model.set_active_palette(palette2.palette_id)
        assert model.active_palette_id == palette2.palette_id
        assert model.active_palette == palette2

        # Set to non-existent palette
        model.set_active_palette("non-existent")
        # Should remain unchanged
        assert model.active_palette_id == palette2.palette_id

    def test_set_active_color_index(self) -> None:
        """Test setting the active color index."""
        # Create a collection with a palette
        palette = Palette("Test", cast(List[Union[str, Color]], ["#FF0000", "#00FF00", "#0000FF"]))
        collection = PaletteCollection([palette])

        # Create model and set active palette
        model = PaletteModel(collection)
        model.set_active_palette(palette.palette_id)

        # Default index is 0
        assert model.active_color_index == 0
        self._extracted_from_test_set_active_color_index_13(model, "#FF0000", 1)
        self._extracted_from_test_set_active_color_index_13(model, "#00FF00", 10)

    # TODO Rename this here and in `test_set_active_color_index`
    def _extracted_from_test_set_active_color_index_13(self, model: PaletteModel, arg1: str, arg2: int) -> None:
        assert model.active_color is not None
        assert model.active_color.hex.upper() == arg1.upper()

        # Set to valid index
        model.set_active_color_index(arg2)
        assert model.active_color_index == 1

    @patch('src.models.palette_model.PaletteModel.post_message')
    def test_add_palette(self, mock_post_message: Mock) -> None:
        """Test adding a palette through the model."""
        collection = PaletteCollection([])
        initial_count = len(collection.palettes)

        # Create model
        model = PaletteModel(collection)

        # Add a palette
        palette = model.add_palette("Test", cast(List[Union[str, Color]], ["#FF0000", "#00FF00"]))
        assert len(model._collection.palettes) == initial_count + 1
        assert palette in model._collection.palettes
        assert palette.name == "Test"

        # Check hex colors - case insensitive
        hex_colors = [c.upper() for c in palette.hex_colors[:2]]
        expected_colors = ["#FF0000".upper(), "#00FF00".upper()]
        assert hex_colors == expected_colors

        # Make sure the palette has a valid ID
        assert palette.palette_id is not None

        # Verify post_message was called
        mock_post_message.assert_called_once()

    @patch('src.models.palette_model.PaletteModel.post_message')
    def test_update_active_color(self, mock_post_message: Mock) -> None:
        """Test updating the active color."""
        # Create a collection with a palette
        palette = Palette("Test", cast(List[Union[str, Color]], ["#FF0000", "#00FF00", "#0000FF"]))
        collection = PaletteCollection([palette])

        # Create model with mocked post_message
        model = PaletteModel(collection)
        model.set_active_palette(palette.palette_id)
        model.set_active_color_index(1)  # Green

        # Update color to yellow
        model.update_active_color("#FFFF00")
        assert model.active_color is not None
        assert model.active_color.hex.upper() == "#FFFF00".upper()
        assert palette.hex_colors[1].upper() == "#FFFF00".upper()

        # Verify post_message was called
        mock_post_message.assert_called_once()

        # Update with no active palette should not raise error
        mock_post_message.reset_mock()
        model._active_palette_id = None
        model.update_active_color("#FFFFFF")  # Should not raise

        # post_message should not be called without an active palette
        mock_post_message.assert_not_called()


if __name__ == "__main__":
    pytest.main(["-v", "test_palette_model.py"])
