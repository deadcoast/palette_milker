
### Step 4 Task List (Python/Textual)

* **UTTER Implementation**
    * [ ] Create UTTER utility module (`utils/utter_export.py`).
    * [ ] Implement `UTTERInstance` class (or similar structure).
    * [ ] Define color role mapping strategy (`_map_colors`).
    * [ ] Implement export methods (`to_utter_array`, `to_css_vars`, `to_color_values`).
    * [ ] (Optional) Implement `get_bottle` method if template usage is needed.
    * [ ] (Optional) Implement other export methods (`toJSON`, `toMarkdown`, `toObject`).
    * [ ] Define `ExportFormat` constants/enum.
* **Export UI Components**
    * [ ] Create `ExportPanel` widget (`widgets/export/export_panel.py`).
    * [ ] Add format selection using `RadioSet`.
    * [ ] Add `Input` for CSS prefix, enable/disable based on format.
    * [ ] Add `TextArea` for export preview (read-only).
    * [ ] Add "Copy" button.
    * [ ] (Optional) Add "Export File..." button and potentially file format selection.
* **Clipboard and File Exports**
    * [ ] Implement Clipboard integration using `pyperclip` in `ExportPanel`.
    * [ ] Add success/error feedback for copy operation (`notify`, temporary message).
    * [ ] (Optional) Create file export utility (`utils/file_export.py`).
    * [ ] (Optional) Implement `export_palette_to_file` function for saving content.
    * [ ] (Optional) Connect "Export File" button to the utility function.
* **Integration**
    * [ ] Connect `ExportPanel` to app state (`active_palette`).
    * [ ] Update `ExportPanel` preview when format, prefix, or active palette changes.
    * [ ] Ensure correct `UTTERInstance` methods are called for selected format.
* **Update App/Screen Component**
    * [ ] Add `ExportPanel` widget to the `MainScreen` layout.
    * [ ] Ensure `ExportPanel` receives necessary updates via messages or watchers.
* **Validation and Testing**
    * [ ] Test UTTER Implementation: Verify output of `to_utter_array`, `to_css_vars`, `to_color_values`.
    * [ ] Test Export Formats: Select each format in UI, check preview content.
    * [ ] Test CSS Prefix: Change prefix, verify CSS output updates correctly.
    * [ ] Test Export Actions: Verify clipboard copy works, check success message.
    * [ ] (Optional) Test file export saves correct content to the expected location.
* **Error Handling and Edge Cases**
    * [ ] Handle clipboard errors (`pyperclip` exceptions).
    * [ ] Handle file I/O errors during export (if implemented).
    * [ ] Handle empty/no active palette case in `ExportPanel`.
    * [ ] Handle invalid characters in CSS prefix or filenames.
* **Documentation and Examples**
    * [ ] Add docstrings to UTTER utility functions and `ExportPanel` widget.
    * [ ] Add comments explaining export logic.

### Final Integration Testing

* Perform end-to-end workflow tests: Create, select, modify, save, and export palettes using various formats.
* Test persistence thoroughly: Close and reopen the app, verify all palettes and colors are restored correctly.
* Test UI responsiveness and layout at different (simulated) terminal sizes if possible.
