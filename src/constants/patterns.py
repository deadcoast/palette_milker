"""
ASCII patterns for UI components.

This module contains reusable ASCII patterns for UI components,
following exactly the designs specified in the documentation.
"""

from typing import Any
from typing import Dict
from typing import List
from typing import Optional


# Character sets for different border styles
BORDER_CHARS = {
    "single": {
        "top_left": "┌",
        "top_right": "┐",
        "bottom_left": "└",
        "bottom_right": "┘",
        "horizontal": "─",
        "vertical": "│",
        "t_right": "├",
        "t_left": "┤",
        "t_up": "┴",
        "t_down": "┬",
        "cross": "┼",
    },
    "double": {
        "top_left": "╔",
        "top_right": "╗",
        "bottom_left": "╚",
        "bottom_right": "╝",
        "horizontal": "═",
        "vertical": "║",
        "t_right": "╠",
        "t_left": "╣",
        "t_up": "╩",
        "t_down": "╦",
        "cross": "╬",
    },
    "mixed": {
        "top_left": "╔",
        "top_right": "╗",
        "bottom_left": "╚",
        "bottom_right": "╝",
        "horizontal": "═",
        "vertical": "║",
        "t_right": "╠",
        "t_left": "╣",
        "t_up": "╩",
        "t_down": "╦",
        "cross": "╬",
        "single_horizontal": "─",
        "single_vertical": "│",
        "single_top_left": "┌",
        "single_top_right": "┐",
        "single_bottom_left": "└",
        "single_bottom_right": "┘",
        "h_connector_right": "╞",  # Double to single horizontal connector
        "h_connector_left": "╡",  # Single to double horizontal connector
        "v_connector_down": "╥",  # Double to single vertical connector
        "v_connector_up": "╨",  # Single to double vertical connector
    },
    "special": {
        "diamond": "♢",
        "plus": "⊕",
        "arrow_right": ">",
        "dropdown": "▼",
        "dropdown_right": "▶",
        "ink_dropper": "⨀",
        "square": "■",
        "empty_square": "□",
        "close": "[x]",
        "up_down": "[↕]",
        "dropdown_arrow": "[▼]",
    },
}

# Main UI Window Pattern
MAIN_WINDOW = [
    "╔───────────────╦───────────────────────────────────────────────────────────────────────╗",
    "│               │                                                                   [x] │",
    "╠───────────────╝                                                                       │",
    "│                                                                                       │",
    "╠                                                                                       │",
    "│                                                                                       │",
    "│                                                                                       │",
    "│                                                                                       │",
    "│                                                                                       │",
    "│                                                                                       │",
    "│                                                                                       │",
    "│                                                                                       │",
    "│                                                                                       │",
    "│                                                                                       │",
    "│                                                                                       │",
    "╠                                                                                       │",
    "│                                                                                       │",
    "╠                                                                                       │",
    "│                                                                                       │",
    "╠                                                                                       │",
    "╠                                                                                       │",
    "│                                                                                       │",
    "╠                                                                                       │",
    "╚─────────────────╩────────────────╩────────────────╩────────────────╩────────────────┴─╝"
]

# UI Component Patterns
PATTERNS = {
    "LABEL": {"DEFAULT": "{text}", "TITLE": "╠{fill}╣"},

    "WINDOW": {"DEFAULT": ["╔{fill}╗", "│{content}│", "╚{fill}╝"],
               "ACTIVE": ["╔{fill}╗", "║{content}║", "╚{fill}╝"]},

    "TEXT_INPUT": {"DEFAULT": ["~{label}:\\> {text}"],
                   "FOCUSED": ["~{label}:\\> {text}█"]},

    "BUTTON": {
        "DEFAULT": ["[{text}]"],
        "ACTIVE": ["[{text}]"],
        "INACTIVE": ["[{text}]"],
        "STANDARD": ["┌{fill}┐", "│{text}│", "└{fill}┘"],
    },

    "COLOR_BUTTON": {
        "ACTIVE": ["┌█───█┐", "│{content}│", "└─────┘"],
        "INACTIVE": ["┌─────┐", "│{content}│", "└─────┘"],
    },

    "PALETTE_GROUP": {
        "ACTIVE": ["╠════════════════╗", "├─♢{text:14}╠", "╠════════════════╝"],
        "INACTIVE": ["┬───────────────┐", "├─{text:14}│", "┴───────────────┘"],
    },

    "HEADER": {
        "DEFAULT": ["╔───────────────╦───────────────────────────────────────────────────────────────────────╗",
                    "│{text:15}│{text2:67}[x] │",
                    "╠───────────────╝{fill:67} │"],
        "SETTINGS": ["╔───────────────╦───────────────────────────────────────────────────────────────────────╗",
                    "│  > Settings   │{text2:67}[x] │",
                    "╠───────────────╝{fill:67} │"],
    },

    "PALETTE_MANAGEMENT": {
        "HEADER": "╠───────────────╦      ┌█───█┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │\n│ > Color Tools │      │{empty:5}│ │{empty:5}│ │{empty:5}│ │{empty:5}│ │{empty:5}│ │{empty:5}│ │{empty:5}│ │{empty:5}│  │\n╠───────────────╝      └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘  │",
        "CONTROLS": "╠════════════════╗     Palette: {name:20}[Add New] [Rename] [Delete]  │",
        "ACTIVE_PALETTE": "├─♢{name:14}╠┬────────────────┬────────────────┬────────────────┬────────────────┐ │",
        "INACTIVE_PALETTE": "╠════════════════╝├─{empty:15}├─{empty:15}├─{empty:15}├─{empty:15}│ │",
        "FOOTER": "╚─────────────────╩────────────────╩────────────────╩────────────────╩────────────────┴─╝",
    },

    "DIALOG": {
        "PALETTE_NAMING": [
            "┌─────────────────────────────────────┐",
            "│ Palette Name:                       │",
            "│ ┌─────────────────────────────────┐ │",
            "│ │ ~name:\\> {name}                │ │",
            "│ └─────────────────────────────────┘ │",
            "│ [OK] [CANCEL]                       │",
            "└─────────────────────────────────────┘"
        ],
        "EXPORT_OPTIONS": [
            "┌─────────────────────────────────────┐",
            "│ Export As:                          │",
            "│ ┌─────────────────────────────────┐ │",
            "│ │ ~UTTER:\\> ▼ [Dropdown Window]  │ │",
            "│ └─────────────────────────────────┘ │",
            "│ [OK] [CANCEL]                       │",
            "└─────────────────────────────────────┘"
        ],
    },

    "COLOR_WHEEL": {
        "HEADER": "╔────────────────────────────────────────────────────────────────╗\n│ [↕] [▼]{title:43}│\n╠────────────────────────────────────────────────────────────────╣",
        "CONTENT": "│{content:64}│",
        "FOOTER": "╠────────────────────────────────────────────────────────────────╣\n│ ~HEX:\\>{input:56}│\n╚────┬───────────────────────────────────────────────────────────╝",
    },

    "COLOR_EXTRACTION": {
        "HEADER": "╔────────────────────────────────────────────────────────────────╗\n│ [⨀] [save]{title:43}│\n╠────────────────────────────────────────────────────────────────╣",
        "CONTENT": "│{content:64}│",
        "FOOTER": "╠────────────────────────────────────────────────────────────────╣\n│ ~HEX:\\>{input:56}│\n╚────┬───────────────────────────────────────────────────────────╝",
    },

    "BROWSE_TREE": {
        "HEADER": "╠───────────────╦\n│ (⊕) Browse    │\n╠───────────────╝",
        "COLLAPSED_FOLDER": "│ ▶ {name}{space}│",
        "EXPANDED_FOLDER": "│ ▼ {name}{space}│",
        "ITEM": "│    {name}{space}│",
        "PALETTES_SECTION": "│ ▼ Palettes    │\n│    Palette1   │\n│               │",
        "ARRAYS_SECTION": "│  ▼ Arrays     │\n│     UTTERS    │\n│     RGB       │\n│     HEX       │\n│               │\n│               │",
        "FOOTER": "╠───────────────╝",
    },

    "COLOR_TOOLS": {
        "HEADER": "╠───────────────╦\n│ > Color Tools │\n╠───────────────╝",
    },

    "COLOR_TOOLS_CONTAINER": {
        "HEADER": "╔═════════════════╗     ╔══════════════════════════════════╗\n║  Milky Suite    ║     ║ Color Input                      ║\n║   ─────────     ║     ╟──────────────────────────────────╢\n║  Color Tools    ║     ║ ~HEX:\\> {hex_value}               ║\n║                 ║     ╚══════════════════════════════════╝",
        "NAVIGATION": "║ > Palette List  ║     ╔══════════════════════════════════╗\n║ > UTTERS List   ║     ║ Current Color                    ║\n║ > Bottles List  ║     ╟──────────────────────────────────╢\n║                 ║     ║ {color_box} {hex_value}            ║\n╚═════════════════╝     ╚══════════════════════════════════╝",
        "PALETTE": "╔═════════════════╗     ╔══════════════════════════════════╗\n║ {palette_name:15} ║     ║ Export                           ║\n╟─────────────────╢     ╟──────────────────────────────────╢",
        "COLOR_ROWS": "║ ┌─────┐ ┌─────┐ ║     ║                                  ║\n║ │{c1:5}│ │{c2:5}│ ║     ║ [UTTER] [CSS Vars] [Bottles]     ║\n║ └─────┘ └─────┘ ║     ║                                  ║\n║ ┌─────┐ ┌─────┐ ║     ║                                  ║\n║ │{c3:5}│ │{c4:5}│ ║     ║ utter:{utter1}                     ║\n║ └─────┘ └─────┘ ║     ║ utter:{utter2}                     ║\n║ ┌─────┐ ┌─────┐ ║     ║ utter:{utter3}                     ║\n║ │{c5:5}│ │{c6:5}│ ║     ║                                  ║\n║ └─────┘ └─────┘ ║     ║ [Export] [Copy]                  ║\n║ ┌─────┐ ┌─────┐ ║     ║                                  ║\n║ │{c7:5}│ │{c8:5}│ ║     ║                                  ║\n║ └─────┘ └─────┘ ║     ║                                  ║\n╚═════════════════╝     ╚══════════════════════════════════╝",
    },
}

# Complete layouts for specific screens
LAYOUTS = {
    "MAIN_APP": {
        "HEADER": "╔───────────────╦───────────────────────────────────────────────────────────────────────╗\n│  > Settings   │                                                                   [x] │\n╠───────────────╝    ╔────────────────────────────────────────────────────────────────╗ │",
        "COLOR_WHEEL": "│                    │ [↕] [▼]                   COLOR WHEEL                          │ │\n╠───────────────╦    ╠────────────────────────────────────────────────────────────────╣ │",
        "BROWSE_TREE": "│ (⊕) Browse    │    │                                                                │ │\n│ ▼ Palettes    │    │                                                                │ │\n│    Palette1   │    │                                                                │ │\n│               │    │                                                                │ │\n│  ▼ Arrays     │    │                                                                │ │\n│     UTTERS    │    │                                                                │ │\n│     RGB       │    │                                                                │ │\n│     HEX       │    │                                                                │ │\n│               │    │                                                                │ │\n│               │    │                                                                │ │",
        "COLOR_INPUT": "╠───────────────╝    ╠────────────────────────────────────────────────────────────────╣ │\n│                    │ ~HEX:\\>                                                        │ │\n│                    ╚────┬───────────────────────────────────────────────────────────╝ │",
        "COLOR_TOOLS": "╠───────────────╦      ┌█───█┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │\n│ > Color Tools │      │     │ │     │ │     │ │     │ │     │ │     │ │     │ │     │  │\n╠───────────────╝      └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘  │",
        "PALETTE": "╠════════════════╗     Palette: Default                    [Add New] [Rename] [Delete]  │\n├─♢              ╠┬────────────────┬────────────────┬────────────────┬────────────────┐ │\n╠════════════════╝├─               ├─               ├─               ├─               │ │\n╚─────────────────╩────────────────╩────────────────╩────────────────╩────────────────┴─╝",
    }
}
