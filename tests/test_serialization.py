"""
Unit tests for the serialization module.

This module tests utility functions for serializing, saving, and loading palettes
in various formats, ensuring proper validation and error handling.
"""

import json
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from unittest.mock import MagicMock
from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from src.utils.serialization import create_empty_palette
from src.utils.serialization import generate_palette_id
from src.utils.serialization import import_palette_from_file
from src.utils.serialization import load_palette_collection
from src.utils.serialization import save_palette_collection
from src.utils.serialization import validate_palette


class TestValidatePalette:
    """Test suite for validate_palette function."""

    def test_valid_palette(self) -> None:
        """Test validation of a valid palette."""
        palette = {
            "id": "test-id",
            "name": "Test Palette",
            "colors": ["#FF0000", "#00FF00", "#0000FF"],
            "createdAt": "2023-01-01T12:00:00Z",
        }

        is_valid, error_message = validate_palette(palette)

        assert is_valid is True
        assert error_message == ""

    def test_missing_required_key(self) -> None:
        """Test validation of a palette with missing keys."""
        # Missing "name" key
        palette = {
            "id": "test-id",
            "colors": ["#FF0000", "#00FF00", "#0000FF"],
            "createdAt": "2023-01-01T12:00:00Z",
        }

        self._extracted_from_test_non_string_color_10(palette, "Missing required key")

    def test_invalid_colors_type(self) -> None:
        """Test validation of a palette with invalid colors type."""
        # "colors" is not a list
        palette = {
            "id": "test-id",
            "name": "Test Palette",
            "colors": "not a list",
            "createdAt": "2023-01-01T12:00:00Z",
        }

        self._extracted_from_test_non_string_color_10(palette, "Colors must be a list")

    def test_empty_colors(self) -> None:
        """Test validation of a palette with empty colors list."""
        palette = {
            "id": "test-id",
            "name": "Test Palette",
            "colors": [],
            "createdAt": "2023-01-01T12:00:00Z",
        }

        self._extracted_from_test_non_string_color_10(
            palette, "Colors list cannot be empty"
        )

    def test_non_string_color(self) -> None:
        """Test validation of a palette with non-string colors."""
        # One of the colors is not a string
        palette = {
            "id": "test-id",
            "name": "Test Palette",
            "colors": ["#FF0000", 123, "#0000FF"],
            "createdAt": "2023-01-01T12:00:00Z",
        }

        self._extracted_from_test_non_string_color_10(
            palette, "Color at index 1 must be a string"
        )

    # TODO Rename this here and in `test_missing_required_key`, `test_invalid_colors_type`, `test_empty_colors` and `test_non_string_color`
    def _extracted_from_test_non_string_color_10(self, palette: Dict[str, Any], arg1: str) -> None:
        is_valid, error_message = validate_palette(palette)
        assert is_valid is False
        assert arg1 in error_message

    def test_invalid_color_format(self) -> None:
        """Test validation of a palette with invalid color format."""
        # Create a function that raises ValueError only for specific cases
        def color_side_effect(color_value: str) -> MagicMock:
            if color_value == "not-a-color":
                raise ValueError("Invalid color")
            # For other values, return a mock Color object
            mock_color = MagicMock()
            mock_color.hex = color_value
            return mock_color

        # One of the colors is not a valid hex color
        with patch("src.utils.serialization.Color", side_effect=color_side_effect):
            palette = {
                "id": "test-id",
                "name": "Test Palette",
                "colors": ["#FF0000", "not-a-color", "#0000FF"],
                "createdAt": "2023-01-01T12:00:00Z",
            }

            is_valid, error_message = validate_palette(palette)

            assert is_valid is False
            assert "Invalid color at index 1" in error_message


class TestSavePaletteCollection:
    """Test suite for save_palette_collection function."""

    @pytest.fixture
    def valid_palettes(self) -> List[Dict[str, Any]]:
        """Return a list of valid palettes for testing."""
        return [
            {
                "id": "palette-1",
                "name": "Palette 1",
                "colors": ["#FF0000", "#00FF00", "#0000FF"],
                "createdAt": "2023-01-01T12:00:00Z",
            },
            {
                "id": "palette-2",
                "name": "Palette 2",
                "colors": ["#FFFF00", "#FF00FF", "#00FFFF"],
                "createdAt": "2023-01-01T12:30:00Z",
            },
        ]

    def test_save_valid_palettes(self, valid_palettes: List[Dict[str, Any]], tmp_path: Path) -> None:
        """Test saving valid palettes to a file."""
        file_path = tmp_path / "palettes.json"

        # Mock open to avoid actual file I/O
        with patch("builtins.open", mock_open()) as m:
            self._extract_write_error(
                valid_palettes, file_path, True, "Successfully saved"
            )
            # Check file was written to
            m.assert_called_once_with(file_path, "w")

            # Check that write was called at least once (json.dump may make multiple writes)
            handle = m()
            assert handle.write.call_count > 0

            written_data = "".join(
                call_args[0][0] for call_args in handle.write.call_args_list
            )
            # Parse the written data as JSON and check it
            parsed_data = json.loads(written_data)
            assert len(parsed_data) == 2
            assert parsed_data[0]["id"] == "palette-1"
            assert parsed_data[1]["id"] == "palette-2"

    def test_save_invalid_palette(self, valid_palettes: List[Dict[str, Any]], tmp_path: Path) -> None:
        """Test saving a collection with an invalid palette."""
        file_path = tmp_path / "palettes.json"

        # Add an invalid palette
        invalid_palettes = valid_palettes.copy()
        invalid_palettes.append({"id": "invalid", "name": "Invalid"})  # Missing colors

        self._extract_write_error(
            invalid_palettes, file_path, False, "Invalid palette"
        )

    def test_create_parent_directories(self, valid_palettes: List[Dict[str, Any]], tmp_path: Path) -> None:
        """Test creating parent directories when they don't exist."""
        file_path = tmp_path / "subdir" / "nested" / "palettes.json"

        # Mock mkdir to check it was called
        with patch.object(Path, "mkdir") as mkdir_mock:
            with patch("builtins.open", mock_open()):
                success, _ = save_palette_collection(valid_palettes, file_path)

                # Check directory creation
                mkdir_mock.assert_called_once_with(parents=True, exist_ok=True)
                assert success is True

    def test_file_write_error(self, valid_palettes: List[Dict[str, Any]], tmp_path: Path) -> None:
        """Test handling of file write errors."""
        file_path = tmp_path / "palettes.json"

        # Mock open to raise an exception
        with patch("builtins.open", side_effect=IOError("Write error")):
            self._extract_write_error(
                valid_palettes, file_path, False, "Error saving palettes"
            )

    def _extract_write_error(self, arg0, file_path, arg2, arg3):
        """Helper method to extract common logic for testing file write errors."""
        success, message = save_palette_collection(arg0, file_path)
        assert success is arg2
        assert arg3 in message


class TestLoadPaletteCollection:
    """Test suite for load_palette_collection function."""

    @pytest.fixture
    def valid_palette_json(self) -> str:
        """Return valid palette JSON for testing."""
        return json.dumps([
            {
                "id": "palette-1",
                "name": "Palette 1",
                "colors": ["#FF0000", "#00FF00", "#0000FF"],
                "createdAt": "2023-01-01T12:00:00Z",
            },
            {
                "id": "palette-2",
                "name": "Palette 2",
                "colors": ["#FFFF00", "#FF00FF", "#00FFFF"],
                "createdAt": "2023-01-01T12:30:00Z",
            },
        ])

    def test_load_valid_palettes(self, valid_palette_json: str, tmp_path: Path) -> None:
        """Test loading valid palettes from a file."""
        file_path = tmp_path / "palettes.json"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=True):
            # Mock open to return test data
            with patch("builtins.open", mock_open(read_data=valid_palette_json)):
                result = self._extract_logic(file_path, 2)
                assert result[1]["id"] == "palette-2"

    def test_file_not_found(self, tmp_path: Path) -> None:
        """Test handling when file doesn't exist."""
        file_path = tmp_path / "nonexistent.json"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=False):
            self._extract_logic_invalid(file_path, "File not found")

    def test_invalid_json(self, tmp_path: Path) -> None:
        """Test handling of invalid JSON."""
        file_path = tmp_path / "invalid.json"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=True):
            # Mock open to return invalid JSON
            with patch("builtins.open", mock_open(read_data="invalid json")):
                self._extract_logic_invalid(file_path, "Invalid JSON format")

    def test_non_list_data(self, tmp_path: Path) -> None:
        """Test handling when JSON data is not a list."""
        file_path = tmp_path / "not_list.json"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=True):
            # Mock open to return JSON object, not array
            with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
                self._extract_logic_invalid(
                    file_path, "Invalid palette collection format"
                )

    def test_invalid_palettes_in_list(self, tmp_path: Path) -> None:
        """Test handling of invalid palettes within the list."""
        # One valid, one invalid palette
        json_data = json.dumps([
            {
                "id": "palette-1",
                "name": "Palette 1",
                "colors": ["#FF0000", "#00FF00", "#0000FF"],
                "createdAt": "2023-01-01T12:00:00Z",
            },
            {
                "id": "invalid",
                "name": "Invalid",
                # Missing colors key
                "createdAt": "2023-01-01T12:30:00Z",
            },
        ])

        file_path = tmp_path / "mixed.json"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=True):
            # Mock open to return mixed data
            with patch("builtins.open", mock_open(read_data=json_data)):
                # Mock print to avoid output during tests
                with patch("builtins.print"):
                    result = self._extract_logic(file_path, 1)
                    # Verify the correct palette was kept
                    assert result[0]["name"] == "Palette 1"

    def _extract_logic(self, file_path: Path, arg1: int) -> List[Dict[str, Any]]:
        """Helper method to extract common logic for testing invalid palettes."""
        success, result = load_palette_collection(file_path)
        assert success is True
        assert isinstance(result, list)
        assert len(result) == arg1
        assert result[0]["id"] == "palette-1"
        return result

    def test_no_valid_palettes(self, tmp_path: Path) -> None:
        """Test handling when no valid palettes are found."""
        # One invalid palette
        json_data = json.dumps([
            {
                "id": "invalid",
                "name": "Invalid",
                # Missing colors key
                "createdAt": "2023-01-01T12:30:00Z",
            },
        ])

        file_path = tmp_path / "invalid_all.json"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=True):
            # Mock open to return invalid data
            with patch("builtins.open", mock_open(read_data=json_data)):
                # Mock print to avoid output during tests
                with patch("builtins.print"):
                    self._extract_logic_invalid(
                        file_path, "No valid palettes found"
                    )

    # TODO Rename this here and in `test_file_not_found`, `test_invalid_json`, `test_non_list_data` and `test_no_valid_palettes`
    def _extract_logic_invalid(self, file_path: Path, arg1: str) -> None:
        """Helper method to extract common logic for testing invalid palettes."""
        success, message = load_palette_collection(file_path)
        assert success is False
        assert arg1 in message


class TestImportPaletteFromFile:
    """Test suite for import_palette_from_file function."""

    def test_file_not_found(self, tmp_path: Path) -> None:
        """Test handling when file doesn't exist."""
        file_path = tmp_path / "nonexistent.json"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=False):
            self._extracted_from_test_general_error_7(file_path, "File not found")

    def test_unsupported_format(self, tmp_path: Path) -> None:
        """Test handling of unsupported file format."""
        file_path = tmp_path / "file.unsupported"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=True):
            self._extracted_from_test_general_error_7(file_path, "Unsupported file format")

    def test_import_from_json(self, tmp_path: Path) -> None:
        """Test importing a palette from a JSON file."""
        file_path = tmp_path / "palette.json"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=True):
            # Mock _import_from_json function
            expected_result = (True, {"id": "test", "name": "Test", "colors": ["#FF0000"]})
            with patch("src.utils.serialization._import_from_json", return_value=expected_result):
                self._extracted_from_test_import_from_css_10(file_path, expected_result)

    def test_import_from_css(self, tmp_path: Path) -> None:
        """Test importing a palette from a CSS file."""
        file_path = tmp_path / "palette.css"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=True):
            # Mock _import_from_css_like function
            expected_result = (True, {"id": "test", "name": "Test", "colors": ["#FF0000"]})
            with patch("src.utils.serialization._import_from_css_like", return_value=expected_result):
                self._extracted_from_test_import_from_css_10(file_path, expected_result)

    # TODO Rename this here and in `test_import_from_json` and `test_import_from_css`
    def _extracted_from_test_import_from_css_10(self, file_path, expected_result):
        success, result = import_palette_from_file(file_path)
        assert success is True
        assert result == expected_result[1]

    def test_general_error(self, tmp_path: Path) -> None:
        """Test handling of general errors during import."""
        file_path = tmp_path / "palette.json"

        # Mock file existence check
        with patch.object(Path, "exists", return_value=True):
            # Mock _import_from_json to raise an exception
            with patch("src.utils.serialization._import_from_json", side_effect=Exception("Test error")):
                self._extracted_from_test_general_error_7(file_path, "Error importing palette")

    # TODO Rename this here and in `test_file_not_found`, `test_unsupported_format` and `test_general_error`
    def _extracted_from_test_general_error_7(self, file_path, arg1):
        success, message = import_palette_from_file(file_path)
        assert success is False
        assert arg1 in message


class TestHelperFunctions:
    """Test suite for helper functions in serialization module."""

    def test_generate_palette_id(self) -> None:
        """Test generating a palette ID."""
        # Generate two IDs and check they're different
        id1 = generate_palette_id()
        id2 = generate_palette_id()

        assert isinstance(id1, str)
        assert len(id1) > 0
        assert id1 != id2  # IDs should be unique

    def test_create_empty_palette(self) -> None:
        """Test creating an empty palette."""
        # Default name
        palette = create_empty_palette()

        assert palette["id"] is not None
        assert palette["name"] == "Untitled Palette"
        assert isinstance(palette["colors"], list)
        assert len(palette["colors"]) > 0  # Should have at least one color
        assert "createdAt" in palette

        # Custom name
        custom_name = "Custom Palette"
        palette = create_empty_palette(custom_name)

        assert palette["name"] == custom_name


if __name__ == "__main__":
    pytest.main(["-v", "test_serialization.py"])
