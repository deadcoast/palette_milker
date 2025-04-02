
## `Terminal` styled Color Wheel GridMockup

* **Visual Reference:**
```
╔───────────────╦───────────────────────────────────────────────────────────────────────╗
│  > Settings   │                                                                   [x] │
╠───────────────╝    ╔────────────────────────────────────────────────────────────────╗ │
│                    │ [↕] [▼]                   COLOR WHEEL                          │ │
╠───────────────╦    ╠────────────────────────────────────────────────────────────────╣ │
│ (⊕) Browse    │    │                                                                │ │
│ ▼ Palettes    │    │                                                                │ │
│    Palette1   │    │                                                                │ │
│               │    │                                                                │ │
│  ▼ Arrays     │    │                                                                │ │
│     UTTERS    │    │                                                                │ │
│     RGB       │    │                                                                │ │
│     HEX       │    │                                                                │ │
│               │    │                                                                │ │
│               │    │                                                                │ │
╠───────────────╝    ╠────────────────────────────────────────────────────────────────╣ │
│                    │ ~HEX:\>                                                        │ │
│                    ╚────┬───────────────────────────────────────────────────────────╝ │
╠───────────────╦      ┌█───█┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │
│ > Color Tools │      │     │ │     │ │     │ │     │ │     │ │     │ │     │ │     │  │
╠───────────────╝      └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘  │
╠════════════════╗     Palette: Default                    [Add New] [Rename] [Delete]  │
├─♢              ╠┬────────────────┬────────────────┬────────────────┬────────────────┐ │
╠════════════════╝├─               ├─               ├─               ├─               │ │
╚─────────────────╩────────────────╩────────────────╩────────────────╩────────────────┴─╝
```

### Main UI Window Outline

```
╔───────────────╦───────────────────────────────────────────────────────────────────────╗ 
│                                                                                   [x] │
╠                                                                                       │
│                                                                                       │
╠                                                                                       │
│                                                                                       │
│                                                                                       │
│                                                                                       │
│                                                                                       │
│                                                                                       │
│                                                                                       │
│                                                                                       │
│                                                                                       │
│                                                                                       │
│                                                                                       │
╠                                                                                       │
│                                                                                       │
╠                                                                                       │
│                                                                                       │
╠                                                                                       │
╠                                                                                       │
│                                                                                       │
╠                                                                                       │
╚─────────────────╩────────────────╩────────────────╩────────────────╩────────────────┴─╝
```

- Main window that all UI elements go inside.
- [x] Closes the application

### Color Extraction and Manipulation

1. **Terminal Styled Color Wheel:**
- The Color Grid(Color Wheel) should not be circular, it should fit and fill the terminal window as a square grid.
- The color contents to select a color goes inside of the Terminal styled window.
- It should fill the entire window
- Bottom line features a `┬` Character below the `~HEX:\>` indicator, this points to the `Active Color` `Button`, helping users understand that the typed HEX will save to the `Active Color` Button.

```
╔────────────────────────────────────────────────────────────────╗
│ [⨀] [save]                DAS COLORS                           │
╠────────────────────────────────────────────────────────────────╣
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
│                                                                │
╠────────────────────────────────────────────────────────────────╣
│ ~HEX:\>                                                        │
╚────┬───────────────────────────────────────────────────────────╝
```

2. **Assets:**

- [⨀] - Ink Dropper Tool Button
- `~HEX:\>` - Text aread for user to type in HEX color code. When executed(hotkey ENTER), the HEX code will save inside of the active color button.
- [save] - an alternative to pressing ENTER in the `~HEX:\>` Textfield.


## Palette Management

1. Full Palette UI Window
- Features `Active` and `Inactive` `Palette Buttons`
- `╠─♢` - Palette Name Input Trigger Button, once clicked brings up the `Palette Naming UI Window`
    - Palettes can only be named when they are `Active`
- `Active` and `Inactive` `Color Buttons`

### Palette Management Mockup

```
╠───────────────╦      ┌█───█┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │
│ > Color Tools │      │     │ │     │ │     │ │     │ │     │ │     │ │     │ │     │  │
╠───────────────╝      └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘  │
╠════════════════╗     Palette: Default                    [Add New] [Rename] [Delete]  │
├─♢              ╠┬────────────────┬────────────────┬────────────────┬────────────────┐ │
╠════════════════╝├─               ├─               ├─               ├─               │ │
╚─────────────────╩────────────────╩────────────────╩────────────────╩────────────────┴─╝
```

1. **Color Palette Full Size(8slots):**

- The active `Color Button` slot is raised and styled differently than the others
- Active Color Button:
```
┌█───█┐
│     │
└─────┘
```

- Inactive Color Button:
```
┌─────┐
│     │
└─────┘
```

- Active Palette Group
-
```
╔════════════════╗
╠─♢              ╠
╠════════════════╝
```

- Inactive Palette Group
```
┬───────────────┐
├─              │
┴───────────────┘
```

2. **Palette Naming UI Window:**

   ```
   ┌─────────────────────────────────────┐
   │ Palette Name:                       │
   │ ┌─────────────────────────────────┐ │
   │ │ ~name:\>                        │ │
   │ └─────────────────────────────────┘ │
   │ [OK] [CANCEL]                       │
   └─────────────────────────────────────┘
   ```

### UTTER Export System

1. **Export Options:**
```
   ┌─────────────────────────────────────┐
   │ Export As:                          │
   │ ┌─────────────────────────────────┐ │
   │ │ ~UTTER:\> ▼ [Dropdown Window]   │ │
   │ └─────────────────────────────────┘ │
   │ [OK] [CANCEL]                       │
   └─────────────────────────────────────┘
```
- The Dropdown Window contains the following options:
  - UTTER Array
  - CSS Vars
  - Color Values


### Color Tools UI Container

- Clicking the Color Tools button in the main UI Opens the Color Tools UI Container

```
╠───────────────╦
│ > Color Tools │
╠───────────────╝
```

### Color Tools UI Container

```
╔═════════════════╗     ╔══════════════════════════════════╗
║  Milky Suite    ║     ║ Color Input                      ║
║   ─────────     ║     ╟──────────────────────────────────╢
║  Color Tools    ║     ║ ~HEX:\> #FF5500                  ║
║                 ║     ╚══════════════════════════════════╝
║ > Palette List  ║     ╔══════════════════════════════════╗
║ > UTTERS List   ║     ║ Current Color                    ║
║ > Bottles List  ║     ╟──────────────────────────────────╢
║                 ║     ║ █████████████ #FF5500            ║
╚═════════════════╝     ╚══════════════════════════════════╝
╔═════════════════╗     ╔══════════════════════════════════╗
║ Palette_Name    ║     ║ Export                           ║
╟─────────────────╢     ╟──────────────────────────────────╢
║ ┌─────┐ ┌─────┐ ║     ║                                  ║
║ │     │ │     │ ║     ║ [UTTER] [CSS Vars] [Bottles]     ║
║ └─────┘ └─────┘ ║     ║                                  ║
║ ┌─────┐ ┌─────┐ ║     ║                                  ║
║ │     │ │     │ ║     ║ utter:FF5500                     ║
║ └─────┘ └─────┘ ║     ║ utter:FFFFFF                     ║
║ ┌─────┐ ┌─────┐ ║     ║ utter:FFFFFF                     ║
║ │     │ │     │ ║     ║                                  ║
║ └─────┘ └─────┘ ║     ║ [Export] [Copy]                  ║
║ ┌─────┐ ┌─────┐ ║     ║                                  ║
║ │     │ │     │ ║     ║                                  ║
║ └─────┘ └─────┘ ║     ║                                  ║
╚═════════════════╝     ╚══════════════════════════════════╝
```

### Browse Tree Style Window

- Tree style window with dropdown menus listing the available Palettes, Bottles and Export Arrays.

```
╔───────────────╗
│ (⊕) Browse    │
│               │
│ ▼ Palettes    │
│    Palette1   │
│               │
│ ▼ Bottles     │
│    Bottles1   │
│               │
│ ▼ Arrays      │
│    UTTERS     │
│    RGB        │
│    HEX        │
╚───────────────╝
```

## Key Mapping

- **q**: Quit the application
- **n**: Create new palette
- **r**: Rename current palette
- **d**: Delete current palette
- **c**: Copy selected color to clipboard
- **1-8**: Select color slot
- **e**: Show export panel
- **Arrow keys**: Navigate between UI elements
- **Enter**: Confirm/activate current selection
- **Tab**: Move between input fields

## Conclusion

This Textual implementation of the Milky Color Suite preserves the unique ASCII-styled interface concept while adapting it to the terminal environment. The use of Textual's reactive programming model provides a clean state management approach similar to React, while the widget system allows for component composition like the original web design.

The implementation follows Textual's best practices for event handling, message passing, and styling, ensuring a responsive and maintainable application.
