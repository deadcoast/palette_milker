
### Step 3 Task List (Python/Textual)

* **Palette Context Setup (App State)**
    * [ ] Add reactive attributes `palettes`, `active_palette_id`, `active_slot_index` to App/Screen.
    * [ ] Implement palette data structure (`create_empty_palette` function).
    * [ ] Implement palette management functions (`create_palette`, `delete_palette`, `update_palette`, `duplicate_palette`).
    * [ ] Implement color slot functions (`set_color_at_slot`).
    * [ ] (Optional) Define custom `Message` classes for palette state changes.
* **Local Storage Persistence (File I/O)**
    * [ ] Define data storage path (`DATA_DIR`, `PALETTES_FILE`).
    * [ ] Implement `_load_palettes` function (using `json.load`).
    * [ ] Implement `_save_palettes` function (using `json.dump`).
    * [ ] Call `_load_palettes` on app initialization.
    * [ ] Call `_save_palettes` in `watch_palettes` or after modification functions.
    * [ ] Handle file load errors/initial creation.
* **Palette List Component**
    * [ ] Create `PaletteList` widget (`widgets/palette/palette_list.py`).
    * [ ] Use Textual `ListView` to display palette items (`PaletteListItem`).
    * [ ] Implement `_update_list` to populate/refresh the `ListView`.
    * [ ] Implement `_update_highlight` to show the active palette.
    * [ ] Handle `ListView.Selected` event to update `app.active_palette_id`.
    * [ ] Add action buttons ("New", "Duplicate", "Delete") and handle `Button.Pressed`.
    * [ ] Connect widget updates to app messages (`PalettesChanged`, `ActivePaletteChanged`).
* **Color Slot Grid Component**
    * [ ] Create `PalettePanel` widget (`widgets/palette/palette_panel.py`).
    * [ ] Use `Horizontal` container to hold 8 `ColorSlot` widgets.
    * [ ] Implement `_update_slots` to set color/active state for all slots based on `app.active_palette`.
    * [ ] Implement `_update_active_highlight` for efficient active state updates.
    * [ ] Connect widget updates to app messages (`ActivePaletteChanged`, `ActiveSlotChanged`, `PalettesChanged`).
* **Color Slot Component**
    * [ ] Create `ColorSlot` widget (`widgets/palette/color_slot.py`).
    * [ ] Add reactive properties `slot_index`, `slot_color_hex`, `is_active_slot`.
    * [ ] Implement `render` or use CSS background to display the color.
    * [ ] Use CSS classes or `render` updates for active state indication.
    * [ ] Handle `on_click` to update `app.active_slot_index`.
    * [ ] Implement `action_` methods (e.g., `action_set_color`) for keyboard interactions.
* **Palette Name Editor**
    * [ ] Create `PaletteName` widget (`widgets/palette/palette_name.py`).
    * [ ] Use Textual `Input` widget for editing.
    * [ ] Implement `_update_name_display` to load name from `app.active_palette`.
    * [ ] Handle `Input.Submitted` event to call `app.update_palette`.
    * [ ] Add validation for empty names.
    * [ ] Connect widget updates to app messages (`ActivePaletteChanged`, `PalettesChanged`).
* **Integration with Color Tools**
    * [ ] Add "Save Color" button (e.g., in `ColorInfo`) or action (e.g., in `ColorSlot`).
    * [ ] Connect the save action to call `app.set_color_at_slot(app.active_slot_index, app.active_color)`.
* **Update App/Screen Component**
    * [ ] Add `PaletteList`, `PalettePanel`, `PaletteName` to the `MainScreen` layout.
    * [ ] Ensure correct widget placement and communication.
* **Validation and Testing**
    * [ ] Test Palette Creation/Deletion/Duplication: Verify list updates and file persistence.
    * [ ] Test Palette Selection: Confirm active palette changes and `PalettePanel` updates.
    * [ ] Test Palette Renaming: Check input updates and file persistence.
    * [ ] Test Color Slot Functionality: Select slots (click/Enter), save colors, verify `PalettePanel` updates and persistence.
    * [ ] Test File Persistence: Create/modify palettes, close and reopen app, verify state is restored.
* **Error Handling and Edge Cases**
    * [ ] Handle file I/O errors during load/save.
    * [ ] Prevent deleting the last palette.
    * [ ] Handle potentially corrupted JSON data on load.
    * [ ] Handle cases with no active palette initially or after deletion.

### Next Steps

Step 3 implements the palette management system. In Step 4, we will:

1.  Create the UTTER export functionality in Python.
2.  Implement different export formats (UTTER Array, CSS Variables, Color Values).
3.  Add clipboard integration.
4.  Develop file export options using Python.