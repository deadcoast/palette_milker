
### Step 2 Task List (Python/Textual)

* **Color State Management Setup**
    * [ ] Add reactive attributes `active_color` (using `textual.color.Color`) and `color_format` to the main `App` or `Screen` class.
    * [ ] Implement `watch_` methods for these reactive attributes to handle changes (e.g., post messages).
    * [ ] Implement color utility functions (`get_color_string`, `is_color_dark`) using Textual/Python libraries.
    * [ ] (Optional) Define custom `Message` classes for color/format changes.
* **Color Selection Widget**
    * [ ] Create `ColorSelector` widget (`widgets/color/color_selector.py`).
    * [ ] Implement color input using Textual `Input` widget.
    * [ ] Add a color preview `Static` widget.
    * [ ] Handle input changes (`on_input_changed`) to update preview.
    * [ ] Handle input submission (`on_input_submitted`) to update `app.active_color`.
    * [ ] Implement error handling for invalid color input (`ColorParseError`).
    * [ ] (Optional) Add alternative selection methods like color swatches (`Button`s).
* **Color Dropper Tool (TUI Adaptation)**
    * [ ] Remove the Eyedropper concept and `[⨀]` button.
    * [ ] Decide whether to implement the complex external `ImageColorPicker` or rely solely on TUI input methods. (Recommendation: Remove/omit for simplicity).
* **Color Information Display**
    * [ ] Create `ColorInfo` widget (`widgets/color/color_info.py`).
    * [ ] Add color swatch display (`Static` widget styled with background color).
    * [ ] Create format selection buttons (`Button` widgets for HEX/RGB/HSL).
    * [ ] Add display for the formatted color value (`Static` widget).
    * [ ] Implement `on_button_pressed` to change `app.color_format`.
    * [ ] Implement `_update_display` method to refresh the widget based on app state (color and format).
    * [ ] Ensure contrast on the color swatch text.
    * [ ] Connect widget to app state changes (via messages or watching reactive attributes).
* **Integration**
    * [ ] Add `ColorSelector` and `ColorInfo` widgets to the `MainScreen`'s `compose` method.
    * [ ] Ensure widgets correctly read from and update the application's `active_color` and `color_format` state.
* **Validation and Testing**
    * [ ] Test Color Selection: Enter valid/invalid colors in the input, check preview and `active_color` update.
    * [ ] Test Color Info Display: Verify swatch updates, formatted value changes with `active_color`.
    * [ ] Test Format Switching: Click HEX/RGB/HSL buttons, verify `color_format` state changes and the displayed value format updates.
* **Error Handling and Edge Cases**
    * [ ] Handle `ColorParseError` gracefully in `ColorSelector`.
    * [ ] Ensure text contrast on `ColorInfo` swatch for very light/dark colors.
    * [ ] Handle edge case color values if using HSL/RGB inputs/sliders.

### Next Steps

Step 2 implements the core color functionality adapted for Textual. In Step 3, we will:

1.  Create the palette management system using Textual state and file storage.
2.  Implement the 8-slot color palette UI widgets.
3.  Add palette naming and selection functionality.
4.  Develop palette persistence using file I/O (e.g., JSON).
