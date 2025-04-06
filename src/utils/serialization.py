"""
Serialization utilities for the Palette Milker application.

This module provides functions for serializing, saving, and loading palettes
in various formats, ensuring proper validation and error handling.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

from ..models.color_model import Color


def validate_palette(palette_data: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Validate palette data to ensure it has the required structure.

    Args:
        palette_data: The palette data to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check if required keys exist
    required_keys = ["id", "name", "colors", "createdAt"]
    for key in required_keys:
        if key not in palette_data:
            return False, f"Missing required key: {key}"

    # Validate colors array
    colors = palette_data.get("colors", [])
    if not isinstance(colors, list):
        return False, "Colors must be a list"

    if len(colors) == 0:
        return False, "Colors list cannot be empty"

    # Validate each color
    for i, color in enumerate(colors):
        if not isinstance(color, str):
            return False, f"Color at index {i} must be a string"

        # Verify color is a valid hex value
        try:
            Color(color)
        except Exception as e:
            return False, f"Invalid color at index {i}: {color} - {e!s}"

    return True, ""


def save_palette_collection(
    palettes: List[Dict[str, Any]], file_path: Union[str, Path], create_dirs: bool = True
) -> Tuple[bool, str]:
    """
    Save a collection of palettes to a JSON file.

    Args:
        palettes: List of palette dictionaries to save
        file_path: Path to save the file to
        create_dirs: Whether to create parent directories if they don't exist

    Returns:
        Tuple of (success, message)
    """
    # Ensure file_path is a Path object
    if isinstance(file_path, str):
        file_path = Path(file_path)

    # Create parent directories if needed
    if create_dirs:
        file_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Validate each palette before saving
        for i, palette in enumerate(palettes):
            is_valid, error_message = validate_palette(palette)
            if not is_valid:
                return False, f"Invalid palette at index {i}: {error_message}"

        # Write to file
        with open(file_path, "w") as f:
            json.dump(palettes, f, indent=2)

        return True, f"Successfully saved {len(palettes)} palettes to {file_path}"

    except Exception as e:
        return False, f"Error saving palettes: {e!s}"


def load_palette_collection(file_path: Union[str, Path]) -> Tuple[bool, Union[List[Dict[str, Any]], str]]:
    """
    Load a collection of palettes from a JSON file.

    Args:
        file_path: Path to load the file from

    Returns:
        Tuple of (success, data_or_error_message)
    """
    # Ensure file_path is a Path object
    if isinstance(file_path, str):
        file_path = Path(file_path)

    # Check if file exists
    if not file_path.exists():
        return False, f"File not found: {file_path}"

    try:
        return _extracted_from_load_palette_collection_23(file_path)
    except json.JSONDecodeError:
        return False, "Invalid JSON format"
    except Exception as e:
        return False, f"Error loading palettes: {e!s}"


# TODO Rename this here and in `load_palette_collection`
def _extracted_from_load_palette_collection_23(file_path: Path) -> Tuple[bool, Union[List[Dict[str, Any]], str]]:
    """
    Extract the palette collection from a file.

    Args:
        file_path: Path to the file to read from

    Returns:
        Tuple containing (success, data or error message)
    """
    # Read from file
    with open(file_path, "r") as f:
        data = json.load(f)

    # Validate loaded data
    if not isinstance(data, list):
        return False, "Invalid palette collection format: Expected a list"

    # Validate each palette
    valid_palettes = []
    for i, palette in enumerate(data):
        is_valid, error_message = validate_palette(palette)
        if is_valid:
            valid_palettes.append(palette)
        else:
            print(f"Warning: Skipping invalid palette at index {i}: {error_message}")

    if not valid_palettes:
        return False, "No valid palettes found in file"

    return True, valid_palettes


def import_palette_from_file(file_path: Union[str, Path]) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """
    Import a single palette from various file formats.

    Args:
        file_path: Path to the file to import

    Returns:
        Tuple of (success, palette_or_error_message)
    """
    # Ensure file_path is a Path object
    if isinstance(file_path, str):
        file_path = Path(file_path)

    # Check if file exists
    if not file_path.exists():
        return False, f"File not found: {file_path}"

    # Get file extension
    file_ext = file_path.suffix.lower()

    try:
        # Handle different file formats
        if file_ext == ".json":
            return _import_from_json(file_path)
        elif file_ext in [".css", ".scss", ".less"]:
            return _import_from_css_like(file_path)
        elif file_ext == ".gpl":
            return _import_from_gpl(file_path)
        elif file_ext == ".ase":
            return _import_from_ase(file_path)
        elif file_ext in [".txt", ".text"]:
            return _import_from_txt(file_path)
        else:
            return False, f"Unsupported file format: {file_ext}"

    except Exception as e:
        return False, f"Error importing palette: {e!s}"


def _import_from_json(file_path: Path) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """Import a palette from a JSON file."""
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        # Check if this is a single palette
        if isinstance(data, dict) and "colors" in data:
            # Create a valid palette structure
            palette = {
                "id": data.get("id", generate_palette_id()),
                "name": data.get("name", file_path.stem),
                "colors": data.get("colors", []),
                "createdAt": data.get("createdAt", datetime.now().isoformat()),
            }

            # Validate the palette
            is_valid, error_message = validate_palette(palette)
            return (True, palette) if is_valid else (False, error_message)
        elif isinstance(data, list) and all(isinstance(item, str) for item in data):
            # Create a valid palette structure
            palette = {
                "id": generate_palette_id(),
                "name": file_path.stem,
                "colors": data,
                "createdAt": datetime.now().isoformat(),
            }

            # Validate the palette
            is_valid, error_message = validate_palette(palette)
            return (True, palette) if is_valid else (False, error_message)
        else:
            return False, "Invalid JSON palette format"

    except json.JSONDecodeError:
        return False, "Invalid JSON format"


def _import_from_css_like(file_path: Path) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """Import a palette from CSS-like files (CSS, SCSS, LESS)."""
    try:
        # Read the file
        with open(file_path, "r") as f:
            content = f.read()

        # Look for hex color values
        import re

        hex_pattern = r"#[0-9A-Fa-f]{3,8}\b"
        colors = [match.group(0) for match in re.finditer(hex_pattern, content)]
        # Look for rgb/rgba values
        rgb_pattern = r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)"
        rgba_pattern = r"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([0-9.]+)\s*\)"

        for match in re.finditer(rgb_pattern, content):
            r, g, b = map(int, match.groups())
            color = Color({"r": r, "g": g, "b": b})
            colors.append(color.hex)

        for match in re.finditer(rgba_pattern, content):
            r, g, b, a = match.groups()
            color = Color({"r": int(r), "g": int(g), "b": int(b)})
            # Convert alpha to hex format
            # Explicitly convert alpha to float first to fix type issue
            alpha_float = float(a)
            alpha_hex = hex(int(alpha_float * 255))[2:].zfill(2)
            colors.append(f"{color.hex}{alpha_hex}")

        # Remove duplicates
        colors = list(dict.fromkeys(colors))

        if not colors:
            return False, "No valid colors found in file"

        # Create a valid palette structure
        palette = {
            "id": generate_palette_id(),
            "name": file_path.stem,
            "colors": colors,
            "createdAt": datetime.now().isoformat(),
        }

        # Validate the palette
        is_valid, error_message = validate_palette(palette)
        return (True, palette) if is_valid else (False, error_message)
    except Exception as e:
        return False, f"Error parsing CSS-like file: {e!s}"


def _import_from_gpl(file_path: Path) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """Import a palette from a GIMP Palette (GPL) file."""
    try:
        # Read the file
        with open(file_path, "r") as f:
            lines = f.readlines()

        palette_name = file_path.stem
        colors = []

        # Extract palette name if present
        for line in lines:
            line = line.strip()
            if line.startswith("Name:"):
                palette_name = line[5:].strip()
                break

        # Parse colors
        for line in lines:
            line = line.strip()
            # Skip comments and empty lines
            if line.startswith("#") or not line:
                continue

            # GIMP palette format: R G B [Name]
            parts = line.split()
            if len(parts) >= 3:
                try:
                    r, g, b = map(int, parts[:3])
                    # Ensure values are in valid range
                    r = max(0, min(255, r))
                    g = max(0, min(255, g))
                    b = max(0, min(255, b))

                    # Convert to hex
                    hex_color = f"#{r:02x}{g:02x}{b:02x}"
                    colors.append(hex_color)
                except ValueError:
                    # Skip invalid lines
                    continue

        if not colors:
            return False, "No valid colors found in GPL file"

        # Create a valid palette structure
        palette = {
            "id": generate_palette_id(),
            "name": palette_name,
            "colors": colors,
            "createdAt": datetime.now().isoformat(),
        }

        # Validate the palette
        is_valid, error_message = validate_palette(palette)
        return (True, palette) if is_valid else (False, error_message)
    except Exception as e:
        return False, f"Error parsing GPL file: {e!s}"


def _import_from_ase(file_path: Path) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """Import a palette from an Adobe Swatch Exchange (ASE) file."""
    try:
        # Read the binary file
        with open(file_path, "rb") as f:
            content = f.read()

        # Check header
        if not content.startswith(b"ASEF"):
            return False, "Invalid ASE file format"

        # Parse ASE file
        colors = _parse_ase_content(content)

        if not colors:
            return False, "No valid colors found in ASE file"

        # Create a valid palette structure
        palette = {
            "id": generate_palette_id(),
            "name": file_path.stem,
            "colors": colors,
            "createdAt": datetime.now().isoformat(),
        }

        # Validate the palette
        is_valid, error_message = validate_palette(palette)
        return (True, palette) if is_valid else (False, error_message)
    except Exception as e:
        return False, f"Error parsing ASE file: {e!s}"


def _parse_ase_content(content: bytes) -> List[str]:
    """Parse ASE file content and extract colors."""
    import struct

    colors: List[str] = []

    # Skip header (signature + version): 8 bytes
    pos = 8

    try:
        # Get number of blocks
        block_count_bytes = content[pos : pos + 4]
        block_count = struct.unpack(">I", block_count_bytes)[0]
        pos += 4

        # Process each block
        for _ in range(block_count):
            # Get block type
            block_type_bytes = content[pos : pos + 2]
            block_type = struct.unpack(">H", block_type_bytes)[0]
            pos += 2

            # Get block length
            block_length_bytes = content[pos : pos + 4]
            block_length = struct.unpack(">I", block_length_bytes)[0]
            pos += 4

            # Process color block (type 1)
            if block_type == 1:
                # Skip color name
                name_length_bytes = content[pos : pos + 2]
                # Manually convert to int to avoid mypy confusion
                name_length_value = struct.unpack(">H", name_length_bytes)[0]
                # Force to int and multiply by 2 for UTF-16 chars
                name_length = 2 * int(str(name_length_value))
                pos += 2 + name_length

                # Get color model
                color_model = content[pos : pos + 4].decode("ascii").strip()
                pos += 4

                if color_model == "RGB":
                    # Get RGB values
                    rgb_bytes = content[pos : pos + 12]
                    r_f, g_f, b_f = struct.unpack(">fff", rgb_bytes)
                    pos += 12

                    # Convert to hex
                    r = int(r_f * 255)
                    g = int(g_f * 255)
                    b = int(b_f * 255)
                    hex_color = f"#{r:02x}{g:02x}{b:02x}"
                    colors.append(hex_color)
                else:
                    # Skip unknown color model
                    pos += block_length - 6 - name_length
            else:
                # Skip other block types
                pos += block_length
    except Exception as e:
        # Log error and continue
        print(f"Error parsing ASE content: {e}")

    return colors


def _import_from_txt(file_path: Path) -> Tuple[bool, Union[Dict[str, Any], str]]:
    """Import a palette from a text file."""
    try:
        # Read the file
        with open(file_path, "r") as f:
            content = f.read()

        palette_name = file_path.stem

        # Extract colors
        import re

        # Look for hex color values
        hex_pattern = r"#[0-9A-Fa-f]{3,8}\b"
        colors = [match.group(0) for match in re.finditer(hex_pattern, content)]

        # Look for RGB values in various formats
        rgb_pattern = r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)"
        for match in re.finditer(rgb_pattern, content):
            r, g, b = map(int, match.groups())
            color = Color({"r": r, "g": g, "b": b})
            colors.append(color.hex)

        # Remove duplicates
        colors = list(dict.fromkeys(colors))

        if not colors:
            return False, "No valid colors found in text file"

        # Limit to 8 colors (or whatever makes sense for your app)
        colors = colors[:8]

        # Create a valid palette structure
        palette = {
            "id": generate_palette_id(),
            "name": palette_name,
            "colors": colors,
            "createdAt": datetime.now().isoformat(),
        }

        # Validate the palette
        is_valid, error_message = validate_palette(palette)
        return (True, palette) if is_valid else (False, error_message)
    except Exception as e:
        return False, f"Error parsing text file: {e!s}"


def generate_palette_id() -> str:
    """Generate a unique ID for a palette."""
    import uuid

    return str(uuid.uuid4())


def create_empty_palette(name: str = "Untitled Palette") -> Dict[str, Any]:
    """
    Create a new empty palette with default values.

    Args:
        name: Name of the palette

    Returns:
        A dictionary representing a palette
    """
    return {
        "id": generate_palette_id(),
        "name": name,
        "colors": ["#FFFFFF"] * 8,  # Default to 8 white slots
        "createdAt": datetime.now().isoformat(),
    }
