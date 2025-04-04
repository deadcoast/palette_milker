"""
Export utility functions for the Milky Color Suite.

This module provides utility functions for exporting color palettes
in various formats, implementing the exact export styles specified.
"""

import json
import os
import struct
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from ..models.color_model import Color
from .utter import UTTER


def export_palette_to_utter(palette_data):
    """
    Export a palette to the UTTER format.

    Args:
        palette_data (dict): Dictionary containing palette colors
            e.g. {'colors': ['#FF5500', '#333333', ...], 'name': 'My Palette'}

    Returns:
        dict: UTTER export data containing the formatted output
    """
    # Map palette colors to expected UTTER input format
    colors = palette_data.get("colors", [])

    # Create a dictionary of color references for UTTER
    color_mapping = {
        "primary": colors[0] if len(colors) > 0 else "#000000",
        "secondary": colors[1] if len(colors) > 1 else "#000000",
        "tertiary": colors[2] if len(colors) > 2 else "#000000",
        "dark": colors[3] if len(colors) > 3 else "#000000",
        "light": colors[4] if len(colors) > 4 else "#FFFFFF",
        "accent": colors[5] if len(colors) > 5 else "#000000",
        "altBackground": colors[6] if len(colors) > 6 else "#000000",
        "textPrimary": colors[7] if len(colors) > 7 else "#000000",
    }

    # Add auto-generated derivatives
    color_mapping.update(
        {
            "hoverBackground": color_mapping["primary"] + "22",  # Add alpha for hover state
            "activeBackground": color_mapping["primary"] + "aa",  # Add alpha for active state
            "disabledBackground": "#CCCCCC",
            "cardBackground": color_mapping["light"],
            "modalBackground": color_mapping["light"],
            "dropdownBackground": color_mapping["light"],
            "tooltipBackground": color_mapping["dark"],
            "insetBackground": color_mapping["light"] + "88",
            "elevatedBackground": color_mapping["light"],
            "sunkenBackground": color_mapping["light"] + "dd",
            "textSecondary": color_mapping["dark"],
            "textTertiary": color_mapping["dark"] + "88",
            "textMuted": color_mapping["dark"] + "66",
            "textDisabled": color_mapping["dark"] + "44",
            "textInverse": color_mapping["light"],
            "linkColor": color_mapping["primary"],
            "linkHoverColor": color_mapping["secondary"],
            "borderColor": color_mapping["dark"] + "33",
            "borderColorLight": color_mapping["dark"] + "11",
            "borderColorDark": color_mapping["dark"] + "55",
            "borderColorAccent": color_mapping["primary"],
            "borderColorFocus": color_mapping["primary"] + "88",
            # Add more derivatives as needed
        }
    )

    # Create UTTER instance with our color mapping
    utter_instance = UTTER.create_from_palette(color_mapping)

    # Return the export data
    return {
        "name": palette_data.get("name", "Untitled Palette"),
        "content": utter_instance.to_css(),
        "raw": utter_instance.to_dict(),
        "json": utter_instance.to_json(),
    }


def export_palette(
    colors: List[Union[str, Color]], palette_name: str, format_name: str, output_path: Optional[str] = None
) -> str:
    """
    Export a color palette in the specified format.

    Args:
        colors: List of colors to export (hex strings or Color objects)
        palette_name: Name of the palette
        format_name: Format to export in (e.g., "CSS", "JSON")
        output_path: Path to save the exported palette to (if None, returns content)

    Returns:
        The exported palette as a string if output_path is None,
        otherwise the path to the exported file

    Raises:
        ValueError: If the format is not supported
    """
    # Convert all colors to Color objects
    color_objects = []
    for color in colors:
        if isinstance(color, Color):
            color_objects.append(color)
        else:
            color_objects.append(Color(color))

    # Get the formatter for the specified format
    handlers = get_export_format_handlers()
    if format_name not in handlers:
        raise ValueError(f"Unsupported export format: {format_name}")

    formatter = handlers[format_name]

    # Generate content
    content = formatter(color_objects, palette_name)

    # Save to file if path is provided
    if output_path:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

        # Write to file
        with open(output_path, "w" if isinstance(content, str) else "wb") as f:
            f.write(content)

        return output_path

    return content


def get_export_format_handlers() -> Dict[str, Callable]:
    """
    Get a dictionary of export format handlers.

    Returns:
        A dictionary mapping format names to formatter functions
    """
    return {
        "CSS": export_css,
        "SCSS": export_scss,
        "LESS": export_less,
        "JSON": export_json,
        "TXT": export_txt,
        "ASE": export_ase,
        "GPL": export_gpl,
        "ACO": export_aco,
        "HTML": export_html,
    }


def export_css(colors: List[Color], palette_name: str) -> str:
    """
    Export palette as CSS variables.

    Args:
        colors: List of colors to export
        palette_name: Name of the palette

    Returns:
        CSS content as a string
    """
    content = f"/* Palette: {palette_name} */\n:root {{\n"

    for i, color in enumerate(colors):
        content += f"  --color-{i + 1}: {color.hex};\n"

    content += "}\n"
    return content


def export_scss(colors: List[Color], palette_name: str) -> str:
    """
    Export palette as SCSS variables.

    Args:
        colors: List of colors to export
        palette_name: Name of the palette

    Returns:
        SCSS content as a string
    """
    content = f"// Palette: {palette_name}\n"

    for i, color in enumerate(colors):
        content += f"$color-{i + 1}: {color.hex};\n"

    return content


def export_less(colors: List[Color], palette_name: str) -> str:
    """
    Export palette as LESS variables.

    Args:
        colors: List of colors to export
        palette_name: Name of the palette

    Returns:
        LESS content as a string
    """
    content = f"// Palette: {palette_name}\n"

    for i, color in enumerate(colors):
        content += f"@color-{i + 1}: {color.hex};\n"

    return content


def export_json(colors: List[Color], palette_name: str) -> str:
    """
    Export palette as JSON.

    Args:
        colors: List of colors to export
        palette_name: Name of the palette

    Returns:
        JSON content as a string
    """
    data = {"name": palette_name, "colors": [color.hex for color in colors]}

    return json.dumps(data, indent=2)


def export_txt(colors: List[Color], palette_name: str) -> str:
    """
    Export palette as plain text.

    Args:
        colors: List of colors to export
        palette_name: Name of the palette

    Returns:
        Text content as a string
    """
    content = f"Palette: {palette_name}\n\n"

    for i, color in enumerate(colors):
        hex_value = color.hex
        rgb_values = color.rgb
        content += f"Color {i + 1}: {hex_value} (RGB: {rgb_values[0]}, {rgb_values[1]}, {rgb_values[2]})\n"

    return content


def export_ase(colors: List[Color], palette_name: str) -> bytes:
    """
    Export palette as Adobe Swatch Exchange (ASE) file.

    Args:
        colors: List of colors to export
        palette_name: Name of the palette

    Returns:
        ASE file content as bytes
    """
    # ASE file format
    # Reference: https://www.cyotek.com/blog/reading-adobe-swatch-exchange-ase-files-using-csharp

    # ASE header
    ase_signature = b"ASEF"
    ase_version = struct.pack(">HH", 1, 0)  # Major version 1, minor version 0

    # Count of color blocks
    block_count = struct.pack(">I", len(colors))

    # Initialize file content
    content = ase_signature + ase_version + block_count

    # Add each color block
    for color in colors:
        # No need to store block type, just include it directly in the content
        content += struct.pack(">H", 1)  # Block type (1 = color)

        # Block length (will be calculated later)
        block_length_pos = len(content)
        content += struct.pack(">I", 0)  # Placeholder

        # Start of block data
        block_start = len(content)

        # Color name (Pascal string - 2 bytes length + name in UTF-16)
        name = f"{palette_name} - {color.hex}"
        name_utf16 = name.encode("utf-16-be")
        content += struct.pack(">H", len(name)) + name_utf16

        # Color model (RGB)
        color_model = b"RGB "
        content += color_model

        # RGB values (3 floats)
        r, g, b = color.rgb_float
        content += struct.pack(">fff", r, g, b)

        # Color type (0 = global)
        color_type = struct.pack(">H", 0)
        content += color_type

        # Calculate block length and update placeholder
        block_length = len(content) - block_start
        content = content[:block_length_pos] + struct.pack(">I", block_length) + content[block_length_pos + 4 :]

    return content


def export_gpl(colors: List[Color], palette_name: str) -> str:
    """
    Export palette as GIMP Palette (GPL) file.

    Args:
        colors: List of colors to export
        palette_name: Name of the palette

    Returns:
        GPL file content as a string
    """
    content = "GIMP Palette\n"
    content += f"Name: {palette_name}\n"
    content += "Columns: 8\n"
    content += "#\n"

    for color in colors:
        r, g, b = color.rgb
        content += f"{r} {g} {b} {color.hex}\n"

    return content


def export_aco(colors: List[Color], palette_name: str) -> bytes:
    """
    Export palette as Adobe Color (ACO) file.

    Args:
        colors: List of colors to export
        palette_name: Name of the palette

    Returns:
        ACO file content as bytes
    """
    content_v1 = _extracted_from_export_aco_16(1, colors)
    # Add each color block (version 1)
    for color in colors:
        # Color space (0 = RGB)
        color_space = struct.pack(">H", 0)

        # RGB values (3 unsigned 16-bit values, 0-65535)
        r, g, b = color.rgb
        r_v1 = struct.pack(">H", (r * 65535) // 255)
        g_v1 = struct.pack(">H", (g * 65535) // 255)
        b_v1 = struct.pack(">H", (b * 65535) // 255)

        # Zero value
        zero = struct.pack(">H", 0)

        content_v1 += color_space + r_v1 + g_v1 + b_v1 + zero

    content_v2 = _extracted_from_export_aco_16(2, colors)
    # Add each color block (version 2)
    for i, color in enumerate(colors):
        # Color space (0 = RGB)
        color_space = struct.pack(">H", 0)

        # RGB values (3 unsigned 16-bit values, 0-65535)
        r, g, b = color.rgb
        r_v2 = struct.pack(">H", (r * 65535) // 255)
        g_v2 = struct.pack(">H", (g * 65535) // 255)
        b_v2 = struct.pack(">H", (b * 65535) // 255)

        # Zero value
        zero = struct.pack(">H", 0)

        # Color name (Pascal string - 4 bytes length + name in UTF-16)
        name = f"{palette_name} - {i + 1}"
        name_utf16 = name.encode("utf-16-be")
        name_length = struct.pack(">I", len(name) + 1)  # +1 for null terminator

        # Null terminator
        null = struct.pack(">H", 0)

        content_v2 += color_space + r_v2 + g_v2 + b_v2 + zero + name_length + name_utf16 + null

    # Combine version 1 and 2 content
    return content_v1 + content_v2


# TODO Rename this here and in `export_aco`
def _extracted_from_export_aco_16(arg0, colors):
    # ACO file format version 2
    # Reference: http://www.nomodes.com/aco.html

    # ACO header
    aco_version1 = struct.pack(">H", arg0)
    aco_count1 = struct.pack(">H", len(colors))

    return aco_version1 + aco_count1


def export_html(colors: List[Color], palette_name: str) -> str:
    """
    Export palette as HTML preview.

    Args:
        colors: List of colors to export
        palette_name: Name of the palette

    Returns:
        HTML content as a string
    """
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{palette_name} - Color Palette</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .palette {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-bottom: 40px;
        }}
        .color-item {{
            width: 150px;
            height: 180px;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }}
        .color-swatch {{
            height: 120px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-shadow: 0 0 4px rgba(0,0,0,0.5);
            font-weight: bold;
        }}
        .color-info {{
            padding: 10px;
            font-size: 14px;
            background-color: white;
            height: 60px;
        }}
        .hex {{
            font-weight: bold;
            margin-bottom: 4px;
        }}
        .rgb {{
            font-size: 12px;
            color: #666;
        }}
    </style>
</head>
<body>
    <h1>{palette_name} Color Palette</h1>
    <div class="palette">
"""

    for i, color in enumerate(colors):
        hex_value = color.hex
        r, g, b = color.rgb

        # Determine text color based on background brightness
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        text_color = "#000" if brightness > 125 else "#fff"

        content += f"""        <div class="color-item">
            <div class="color-swatch" style="background-color: {hex_value}; color: {text_color};">
                {i + 1}
            </div>
            <div class="color-info">
                <div class="hex">{hex_value}</div>
                <div class="rgb">RGB: {r}, {g}, {b}</div>
            </div>
        </div>
"""

    content += """    </div>
    <div style="text-align: center; font-size: 12px; color: #666;">
        Generated by Milky Color Suite
    </div>
</body>
</html>
"""

    return content
