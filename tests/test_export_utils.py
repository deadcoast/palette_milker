"""
Unit tests for the export_utils module.

This module tests utility functions for exporting color palettes in various formats.
"""

import json
import struct
from pathlib import Path
from typing import List
from typing import Union
from typing import cast
from unittest.mock import MagicMock
from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from src.models.color_model import Color
from src.utils.export_utils import export_aco
from src.utils.export_utils import export_ase
from src.utils.export_utils import export_css
from src.utils.export_utils import export_gpl
from src.utils.export_utils import export_html
from src.utils.export_utils import export_json
from src.utils.export_utils import export_less
from src.utils.export_utils import export_palette
from src.utils.export_utils import export_palette_to_utter
from src.utils.export_utils import export_scss
from src.utils.export_utils import export_txt
from src.utils.export_utils import get_export_format_handlers


class TestExportPalette:
    """Test suite for export_palette function."""

    @pytest.fixture
    def sample_colors(self) -> List[Color]:
        """Return a list of sample colors for testing."""
        return [Color("#FF0000"), Color("#00FF00"), Color("#0000FF")]

    def test_export_css(self, sample_colors: List[Color]) -> None:
        """Test exporting a palette as CSS variables."""
        # Call function
        result = export_css(sample_colors, "Test Palette")

        # Verify output
        assert "/* Palette: Test Palette */" in result
        assert ":root {" in result
        assert "  --color-1: #ff0000;" in result
        assert "  --color-2: #00ff00;" in result
        assert "  --color-3: #0000ff;" in result
        assert "}" in result

    def test_export_scss(self, sample_colors: List[Color]) -> None:
        """Test exporting a palette as SCSS variables."""
        # Call function
        result = export_scss(sample_colors, "Test Palette")

        # Verify output
        assert "// Palette: Test Palette" in result
        assert "$color-1: #ff0000;" in result
        assert "$color-2: #00ff00;" in result
        assert "$color-3: #0000ff;" in result

    def test_export_less(self, sample_colors: List[Color]) -> None:
        """Test exporting a palette as LESS variables."""
        # Call function
        result = export_less(sample_colors, "Test Palette")

        # Verify output
        assert "// Palette: Test Palette" in result
        assert "@color-1: #ff0000;" in result
        assert "@color-2: #00ff00;" in result
        assert "@color-3: #0000ff;" in result

    def test_export_json(self, sample_colors: List[Color]) -> None:
        """Test exporting a palette as JSON."""
        # Call function
        result = export_json(sample_colors, "Test Palette")

        # Verify output by parsing JSON and checking contents
        data = json.loads(result)
        assert data["name"] == "Test Palette"
        assert isinstance(data["colors"], list)
        assert len(data["colors"]) == 3
        assert data["colors"][0].lower() == "#ff0000"
        assert data["colors"][1].lower() == "#00ff00"
        assert data["colors"][2].lower() == "#0000ff"

    def test_export_txt(self, sample_colors: List[Color]) -> None:
        """Test exporting a palette as plain text."""
        # Call function
        result = export_txt(sample_colors, "Test Palette")

        # Verify output
        assert "Palette: Test Palette" in result
        # Check just the hex values instead of the full line
        assert "#ff0000" in result.lower()
        assert "#00ff00" in result.lower()
        assert "#0000ff" in result.lower()

    def test_export_gpl(self, sample_colors: List[Color]) -> None:
        """Test exporting a palette as GIMP Palette (GPL)."""
        # Call function
        result = export_gpl(sample_colors, "Test Palette")

        # Verify output
        assert "GIMP Palette" in result
        assert "Name: Test Palette" in result
        assert "Columns: 8" in result
        # Look for the RGB values
        assert "255 0 0" in result  # Red
        assert "0 255 0" in result  # Green
        assert "0 0 255" in result  # Blue

    def test_export_ase(self, sample_colors: List[Color]) -> None:
        """Test exporting a palette as Adobe Swatch Exchange (ASE)."""
        # Call function - this returns binary data
        result = export_ase(sample_colors, "Test Palette")

        # Verify it's binary data
        assert isinstance(result, bytes)
        # ASE file starts with "ASEF"
        assert result.startswith(b"ASEF")
        # Check block count (3 colors)
        # Skip 8 bytes (header), read 4 bytes as big-endian unsigned int
        block_count = struct.unpack(">I", result[8:12])[0]
        assert block_count == 3

    def test_export_aco(self, sample_colors: List[Color]) -> None:
        """Test exporting a palette as Adobe Color (ACO)."""
        # Call function - this returns binary data
        result = export_aco(sample_colors, "Test Palette")

        # Verify it's binary data
        assert isinstance(result, bytes)
        # ACO files have a version number at offset 0-1 (should be 1 for v1)
        version_v1 = struct.unpack(">H", result[:2])[0]
        assert version_v1 == 1
        # Count of colors follows (2 bytes)
        count_v1 = struct.unpack(">H", result[2:4])[0]
        assert count_v1 == 3

    def test_export_html(self, sample_colors: List[Color]) -> None:
        """Test exporting a palette as HTML."""
        # Call function
        result = export_html(sample_colors, "Test Palette")

        # Verify output
        result_lower = result.lower()
        assert "<html lang=" in result_lower
        assert "<title>" in result_lower
        assert "#ff0000" in result_lower
        assert "#00ff00" in result_lower
        assert "#0000ff" in result_lower
        assert "</html>" in result_lower

    def test_export_with_file_output(self, sample_colors: List[Color], tmp_path: Path) -> None:
        """Test exporting a palette to a file."""
        output_path = tmp_path / "test_palette.css"
        output_path_str = str(output_path)

        # Convert using cast to satisfy type checker
        colors = cast(List[Union[str, Color]], sample_colors)

        # Call function with file output
        with patch("builtins.open", mock_open()) as m:
            result = export_palette(colors, "Test Palette", "CSS", output_path_str)

            # Verify file was written
            m.assert_called_once_with(output_path_str, "w")
            # Result should be the output path
            assert result == output_path_str

    def test_unsupported_format(self, sample_colors: List[Color]) -> None:
        """Test handling of unsupported format."""
        # Convert using cast to satisfy type checker
        colors = cast(List[Union[str, Color]], sample_colors)

        with pytest.raises(ValueError, match="Unsupported export format"):
            export_palette(colors, "Test Palette", "UNSUPPORTED")

    def test_get_export_format_handlers(self) -> None:
        """Test getting the dictionary of export format handlers."""
        handlers = get_export_format_handlers()

        assert isinstance(handlers, dict)
        assert "CSS" in handlers
        assert "SCSS" in handlers
        assert "LESS" in handlers
        assert "JSON" in handlers
        assert "ASE" in handlers
        assert len(handlers) >= 8  # At least 8 formats should be supported


class TestExportPaletteToUtter:
    """Test suite for export_palette_to_utter function."""

    def test_export_to_utter(self) -> None:
        """Test exporting a palette to UTTER format."""
        # Sample palette data
        palette_data = {
            "name": "Test Palette",
            "colors": ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#000000", "#FFFFFF"]
        }

        # Instead of mocking the UTTER class directly, which is hard to patch correctly,
        # we can test the function's behavior based on the returned result
        with patch("src.utils.export_utils.UTTER") as mock_utter:
            # Configure mock - this approach patches the import within export_utils
            mock_utter_instance = MagicMock()
            mock_utter_instance.to_css.return_value = "/* CSS output */"
            mock_utter_instance.to_dict.return_value = {"key": "value"}
            mock_utter_instance.to_json.return_value = "{\"key\": \"value\"}"
            mock_utter.create_from_palette.return_value = mock_utter_instance

            # Call function
            result = export_palette_to_utter(palette_data)

            # Just verify the result has expected values
            assert result["name"] == "Test Palette"
            assert result["content"] == "/* CSS output */"
            assert result["raw"] == {"key": "value"}
            assert result["json"] == "{\"key\": \"value\"}"

            # Verify a color mapping was created (without checking values)
            assert mock_utter.create_from_palette.call_count > 0


if __name__ == "__main__":
    pytest.main(["-v", "test_export_utils.py"])
