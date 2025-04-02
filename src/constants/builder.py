"""
ASCII UI Builder

This module provides functions for building ASCII UI elements from patterns,
allowing dynamic composition while maintaining the exact visual design.
"""

from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from .patterns import BORDER_CHARS
from .patterns import PATTERNS


def create_button(text: str, width: int = 15, active: bool = False) -> str:
    """
    Create a button with the given text.

    Args:
        text: The text to display in the button
        width: The width of the button
        active: Whether the button is active

    Returns:
        The button as a string
    """
    variant = "ACTIVE" if active else "DEFAULT"
    pattern = PATTERNS["BUTTON"][variant]

    # Center the text
    text = f"  > {text}"
    text = text.ljust(width - 2)

    # Fill the rest with appropriate characters
    fill = "═" * (width - 2) if active else "─" * (width - 2)

    # Format each line
    lines = [line.format(fill=fill, text=text) for line in pattern]

    return "\n".join(lines)


def create_color_button(content: str = " ", active: bool = False) -> str:
    """
    Create a color button with the given content.

    Args:
        content: The content to display in the button (typically a space or color indicator)
        active: Whether the button is active

    Returns:
        The color button as a string
    """
    variant = "ACTIVE" if active else "INACTIVE"
    pattern = PATTERNS["COLOR_BUTTON"][variant]

    # Center the content
    centered_content = content.center(5)

    # Format each line
    lines = [line.format(content=centered_content) for line in pattern]

    return "\n".join(lines)


def create_text_input(label: str, text: str = "", focused: bool = False) -> str:
    """
    Create a text input with the given label and text.

    Args:
        label: The label for the input (e.g., 'HEX', 'name')
        text: The current text in the input
        focused: Whether the input is focused

    Returns:
        The text input as a string
    """
    variant = "FOCUSED" if focused else "DEFAULT"
    pattern = PATTERNS["TEXT_INPUT"][variant]

    # Pattern is a list of strings, so format each line
    formatted_lines = [line.format(label=label, text=text) for line in pattern]

    return "\n".join(formatted_lines)


def create_palette_group(text: str = "", width: int = 16, active: bool = False) -> str:
    """
    Create a palette group with the given text.

    Args:
        text: The text to display in the palette group
        width: The width of the palette group
        active: Whether the palette group is active

    Returns:
        The palette group as a string
    """
    variant = "ACTIVE" if active else "INACTIVE"
    pattern = PATTERNS["PALETTE_GROUP"][variant]

    # Fill characters depend on active state
    fill = "═" * (width - 2) if active else "─" * (width - 2)

    # Format each line
    lines = [line.format(fill=fill, text=text.ljust(width - 4)) for line in pattern]

    return "\n".join(lines)


def create_color_wheel(width: int = 60, height: int = 15, title: str = "COLOR WHEEL") -> str:
    """
    Create a color wheel with the given dimensions and title.

    Args:
        width: The width of the color wheel
        height: The height of the color wheel
        title: The title of the color wheel

    Returns:
        The color wheel as a string
    """
    # Prepare patterns
    header_pattern = PATTERNS["COLOR_WHEEL"]["HEADER"]
    content_pattern = PATTERNS["COLOR_WHEEL"]["CONTENT"]
    footer_pattern = PATTERNS["COLOR_WHEEL"]["FOOTER"]

    # Create title with padding
    title_pad = width - 20  # Accounting for "[⨀] [save]" and some padding
    title_display = title.center(title_pad)

    # Create the color wheel
    lines = []

    # Header
    header = header_pattern.format(fill="─" * (width - 2), title=title_display)
    lines.extend(header.split("\n"))

    # Content (empty space for now, would be filled with color grid)
    lines.extend(content_pattern.format(content=" " * (width - 2)) for _ in range(height - 5))
    # Footer
    footer = footer_pattern.format(fill="─" * (width - 2), input=" " * (width - 10), fill2="─" * (width - 6))
    lines.extend(footer.split("\n"))

    return "\n".join(lines)


def create_browse_tree(items: Optional[List[Dict[str, Any]]] = None, width: int = 17) -> str:
    """
    Create a browse tree with the given items.

    Args:
        items: List of items to display in the tree
        width: The width of the tree

    Returns:
        The browse tree as a string
    """
    # Default items if none provided
    if items is None:
        items = [
            {"type": "header", "text": "Browse"},
            {"type": "expanded_folder", "name": "Palettes"},
            {"type": "item", "name": "Palette1"},
            {"type": "expanded_folder", "name": "Arrays"},
            {"type": "item", "name": "UTTERS"},
            {"type": "item", "name": "RGB"},
            {"type": "item", "name": "HEX"},
        ]

    # Prepare patterns
    header_pattern = PATTERNS["BROWSE_TREE"]["HEADER"]
    collapsed_pattern = PATTERNS["BROWSE_TREE"]["COLLAPSED_FOLDER"]
    expanded_pattern = PATTERNS["BROWSE_TREE"]["EXPANDED_FOLDER"]
    item_pattern = PATTERNS["BROWSE_TREE"]["ITEM"]
    footer_pattern = PATTERNS["BROWSE_TREE"]["FOOTER"]

    # Create the browse tree
    lines = []

    # Header
    header = header_pattern.format(
        fill="─" * (width - 2), space=" " * (width - 14)  # Accounting for "│ (⊕) Browse" (14 chars)
    )
    lines.extend(header.split("\n"))

    # Items
    for item in items:
        if item["type"] == "header" or item["type"] not in ["collapsed_folder", "expanded_folder", "item"]:
            continue  # Already handled in header
        elif item["type"] == "collapsed_folder":
            line = collapsed_pattern.format(
                name=item["name"], space=" " * (width - len(item["name"]) - 6)  # Accounting for "│ ▶ " and "│"
            )
        elif item["type"] == "expanded_folder":
            line = expanded_pattern.format(
                name=item["name"], space=" " * (width - len(item["name"]) - 6)  # Accounting for "│ ▼ " and "│"
            )
        else:
            line = item_pattern.format(
                name=item["name"], space=" " * (width - len(item["name"]) - 7)  # Accounting for "│    " and "│"
            )
        lines.append(line)

    # Add blank line if needed
    if len(items) < 6:  # Ensure minimum height
        blank_line = "│" + " " * (width - 2) + "│"
        lines.extend(blank_line for _ in range(6 - len(items)))
    # Footer
    footer = footer_pattern.format(fill="─" * (width - 2))
    lines.append(footer)

    return "\n".join(lines)


def create_dropdown(options: Optional[List[str]] = None, selected_index: int = 0, width: int = 30) -> str:
    """
    Create a dropdown with the given options.

    Args:
        options: List of options to display in the dropdown
        selected_index: Index of the selected option
        width: The width of the dropdown

    Returns:
        The dropdown as a string
    """
    options = options or ["Option 1", "Option 2", "Option 3"]
    selected = options[selected_index] if 0 <= selected_index < len(options) else options[0]

    # Header with selected option
    dropdown_line = f"~DROPDOWN:> {selected} ▼".ljust(width - 2)
    dropdown = f"┌{'─' * (width - 2)}┐\n│ {dropdown_line} │\n└{'─' * (width - 2)}┘"

    return dropdown


def create_export_panel(
    formats: Optional[List[str]] = None, selected_format: Optional[str] = None, content: str = ""
) -> str:
    """
    Create an export panel with the given formats and content.

    Args:
        formats: List of export formats
        selected_format: The selected format
        content: Additional content for the panel

    Returns:
        The export panel as a string
    """
    formats = formats or ["CSS", "JSON", "SCSS", "PNG"]
    selected_format = selected_format or formats[0]

    # Create the header
    header = f"┌{'─' * 33}┐\n│ Export As:                          │"

    # Create the format selector
    format_selector = f"│ ┌{'─' * 29}┐ │\n│ │ ~FORMAT:> {selected_format.ljust(18)}▼ │ │\n│ └{'─' * 29}┘ │"

    # Create the content area
    content_lines = []
    if content:
        for line in content.split("\n"):
            content_lines.append(f"│ {line.ljust(33)} │")
    else:
        content_lines = [f"│ {' ' * 33} │"]

    # Create the buttons
    buttons = f"│ [OK] [CANCEL]                       │"

    # Create the footer
    footer = f"└{'─' * 33}┘"

    # Join all parts
    return "\n".join([header, format_selector, *content_lines, buttons, footer])


def build_color_wheel(width: int = 60, height: int = 15) -> str:
    """
    Build a color wheel UI with the exact specified design.

    Args:
        width: The width of the color wheel
        height: The height of the color wheel

    Returns:
        The color wheel as a string
    """
    # Create the window for the color wheel
    top_border = f"╔{'─' * (width - 2)}╗"
    header = f"│ [⨀] [save]                DAS COLORS{' ' * (width - 40)}│"
    separator = f"╠{'─' * (width - 2)}╣"
    bottom_separator = separator
    content_line = f"│{' ' * (width - 2)}│"
    input_line = f"│ ~HEX:\\>{' ' * (width - 10)}│"
    bottom_border = f"╚────┬{'─' * (width - 6)}╝"

    # Build the color wheel
    lines = [top_border, header, separator]

    # Add content lines
    for _ in range(height - 5):  # -5 for top border, header, separator, input, bottom border
        lines.append(content_line)

    # Add input and bottom
    lines.append(bottom_separator)
    lines.append(input_line)
    lines.append(bottom_border)

    return "\n".join(lines)


def build_color_palette(colors: List[str] = None, active_index: int = 0) -> str:
    """
    Build a color palette with the exact specified design.

    Args:
        colors: List of colors to display (up to 8)
        active_index: Index of the active color

    Returns:
        The color palette as a string
    """
    # Default to 8 empty colors if none provided
    colors = colors or [""] * 8
    colors = colors[:8]  # Ensure at most 8 colors
    while len(colors) < 8:
        colors.append("")  # Pad to 8 colors

    # Create the buttons
    buttons = []
    for i, color in enumerate(colors):
        active = i == active_index
        button = create_color_button(color, active)
        buttons.append(button.split("\n"))

    # Join the buttons horizontally
    lines = []
    for i in range(3):  # Each button is 3 lines tall
        line = ""
        for j, button in enumerate(buttons):
            line += button[i]
            if j < len(buttons) - 1:
                line += " "  # Add space between buttons
        lines.append(line)

    return "\n".join(lines)


def build_palette_management(
    palette_name: str = "Default", active_palette_index: int = 0, palette_count: int = 4, width: int = 80
) -> str:
    """
    Build the palette management UI with the exact specified design.

    Args:
        palette_name: Name of the active palette
        active_palette_index: Index of the active palette
        palette_count: Number of palettes
        width: Total width of the UI

    Returns:
        The palette management UI as a string
    """
    # Calculate available width for each palette group
    palette_group_width = (width - 10) // palette_count

    # Create the header
    color_tools = "╠───────────────╦"
    color_tools_text = "│ > Color Tools │"
    color_tools_bottom = "╠───────────────╝"

    # Create the palette slots placeholder (would be filled with actual color buttons)
    palette_slots = f"{'  ' * 9}"

    # Create the palette info line
    palette_info = f"Palette: {palette_name}{' ' * (40 - len(palette_name))}[Add New] [Rename] [Delete]"

    # Create the palette groups
    palette_groups_top = "╠════════════════╗"
    palette_groups_middle = "├─♢              ╠"
    palette_groups_bottom = "╠════════════════╝"

    palette_groups = []
    for i in range(palette_count):
        if i == active_palette_index:
            # Active palette group
            top = "┬" + "─" * (palette_group_width - 2) + "┐"
            middle = "├─" + " " * (palette_group_width - 3) + "│"
            bottom = "┴" + "─" * (palette_group_width - 2) + "┘"
        else:
            # Inactive palette group
            top = "┬" + "─" * (palette_group_width - 2) + "┐"
            middle = "├─" + " " * (palette_group_width - 3) + "│"
            bottom = "┴" + "─" * (palette_group_width - 2) + "┘"

        palette_groups.append((top, middle, bottom))

    # Horizontal joining of palette groups
    palette_groups_lines = []
    for i in range(3):  # Each palette group is 3 lines
        line = ""
        for j in range(palette_count):
            line += palette_groups[j][i]
        if i == 2 and palette_count > 0:  # Add the closing character to the last line
            line += "┴─"
        palette_groups_lines.append(line)

    # Build the complete palette management UI
    lines = []
    lines.append(f"{color_tools}{' ' * 6}{'  ' * 8}")
    lines.append(f"{color_tools_text}{' ' * 6}{'  ' * 8}")
    lines.append(f"{color_tools_bottom}{' ' * 6}{'  ' * 8}")
    lines.append(f"{palette_groups_top}{' ' * 5}{palette_info}")
    lines.append(f"{palette_groups_middle}" + palette_groups_lines[0])
    lines.append(f"{palette_groups_bottom}" + palette_groups_lines[1])
    lines.append("╚" + "─" * 9 + "┴" + "─" * 4 + palette_groups_lines[2])

    return "\n".join(lines)


def build_naming_dialog() -> str:
    """
    Build the palette naming dialog with the exact specified design.

    Returns:
        The palette naming dialog as a string
    """
    lines = [
        "┌─────────────────────────────────────┐",
        "│ Palette Name:                       │",
        "│ ┌─────────────────────────────────┐ │",
        "│ │ ~name:\\>                       │ │",
        "│ └─────────────────────────────────┘ │",
        "│ [OK] [CANCEL]                       │",
        "└─────────────────────────────────────┘",
    ]

    return "\n".join(lines)


def build_export_dialog() -> str:
    """
    Build the export dialog with the exact specified design.

    Returns:
        The export dialog as a string
    """
    lines = [
        "┌─────────────────────────────────────┐",
        "│ Export As:                          │",
        "│ ┌─────────────────────────────────┐ │",
        "│ │ ~UTTER:\\> ▼ [Dropdown Window]  │ │",
        "│ └─────────────────────────────────┘ │",
        "│ [OK] [CANCEL]                       │",
        "└─────────────────────────────────────┘",
    ]

    return "\n".join(lines)


def build_browse_tree() -> str:
    """
    Build the browse tree with the exact specified design.

    Returns:
        The browse tree as a string
    """
    lines = [
        "╔───────────────╗",
        "│ (⊕) Browse    │",
        "│               │",
        "│ ▼ Palettes    │",
        "│    Palette1   │",
        "│               │",
        "│  ▼ Arrays     │",
        "│     UTTERS    │",
        "│     RGB       │",
        "│     HEX       │",
        "╚───────────────╝",
    ]

    return "\n".join(lines)


def compose_complete_ui(width: int = 80, height: int = 25) -> str:
    """
    Compose the complete UI by combining all elements.

    Args:
        width: The width of the UI
        height: The height of the UI

    Returns:
        The complete UI as a string
    """
    # Define component positions
    components = {
        (0, 0): "╔───────────────╦" + "─" * (width - 17) + "╗\n" + "│  > Settings   │" + " " * (width - 19) + "[x] │",
        (2, 0): "╠───────────────╝    ╔"
        + "─" * (width - 32)
        + "╗ │\n"
        + "│                    │ [↕] [▼]                   COLOR WHEEL"
        + " " * 10
        + "│ │",
        (4, 0): "╠───────────────╦    ╠" + "─" * (width - 32) + "╣ │",
        (4, 1): build_browse_tree(),
        (5, 25): build_color_wheel(width - 32, height - 15),
        (height - 10, 0): "╠───────────────╝    ╠"
        + "─" * (width - 32)
        + "╣ │\n"
        + "│                    │ ~HEX:\\>"
        + " " * (width - 42)
        + "│ │\n"
        + "│                    ╚────┬"
        + "─" * (width - 38)
        + "╝ │",
        (height - 7, 0): build_palette_management(width=width),
    }

    # Build the layout
    return build_layout(components)
