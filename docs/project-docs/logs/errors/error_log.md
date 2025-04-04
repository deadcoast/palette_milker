    ~/Cu/palette_milker    master !31 ?41 ▓▒░ ruff check --fix .
src/constants/patterns.py:136:121: E501 Line too long (137 > 120)
    |
134 | …
135 | …─┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐  │\n"
136 | …ty:5}│ │{empty:5}│ │{empty:5}│ │{empty:5}│ │{empty:5}│ │{empty:5}│  │\n"
    |                                                         ^^^^^^^^^^^^^^^^^ E501
137 | …─┘ └─────┘ └─────┘ └─────┘ └─────┘  │"
138 | …
    |

src/main.py:529:13: N806 Variable `SATURATION_STEP` in function should be lowercase
    |
527 |             from .utils.color_adjustment import adjust_saturation
528 |
529 |             SATURATION_STEP = 5  # 5% change in saturation
    |             ^^^^^^^^^^^^^^^ N806
530 |             LIGHTNESS_STEP = 5  # 5% change in lightness
    |

src/main.py:530:13: N806 Variable `LIGHTNESS_STEP` in function should be lowercase
    |
529 |             SATURATION_STEP = 5  # 5% change in saturation
530 |             LIGHTNESS_STEP = 5  # 5% change in lightness
    |             ^^^^^^^^^^^^^^ N806
531 |
532 |             # Apply the adjustment based on property name
    |

src/screens/color_picker.py:109:19: E741 Ambiguous variable name: `l`
    |
108 |             # Update HSL values
109 |             h, s, l = self.selected_color.hsl
    |                   ^ E741
110 |             self.hue_value = h
111 |             self.saturation_value = s
    |

src/screens/color_picker.py:166:15: E741 Ambiguous variable name: `l`
    |
165 |         # Update the HSL values from the new color
166 |         h, s, l = self.selected_color.hsl
    |               ^ E741
167 |         self.hue_value = h
168 |         self.saturation_value = s
    |

src/screens/color_picker.py:189:15: E741 Ambiguous variable name: `l`
    |
188 |         # Update the HSL values from the new color
189 |         h, s, l = self.selected_color.hsl
    |               ^ E741
190 |         self.hue_value = h
191 |         self.saturation_value = s
    |

src/screens/color_picker.py:212:15: E741 Ambiguous variable name: `l`
    |
211 |         # Update the HSL values from the new color
212 |         h, s, l = self.selected_color.hsl
    |               ^ E741
213 |         self.hue_value = h
214 |         self.saturation_value = s
    |

src/screens/color_picker.py:240:23: E741 Ambiguous variable name: `l`
    |
239 |                 # Update HSL values
240 |                 h, s, l = color.hsl
    |                       ^ E741
241 |                 self.hue_value = h
242 |                 self.saturation_value = s
    |

src/screens/color_picker_screen.py:258:15: E741 Ambiguous variable name: `l`
    |
256 |         """
257 |         details = self.query_one("#color-details", ColorDetails)
258 |         h, s, l = details._get_hsl_values()
    |               ^ E741
259 |
260 |         # Adjust hue (wrap around 0-360)
    |

src/screens/color_picker_screen.py:273:15: E741 Ambiguous variable name: `l`
    |
271 |         """
272 |         details = self.query_one("#color-details", ColorDetails)
273 |         h, s, l = details._get_hsl_values()
    |               ^ E741
274 |
275 |         # Adjust saturation (clamp 0-100)
    |

src/screens/color_picker_screen.py:288:15: E741 Ambiguous variable name: `l`
    |
286 |         """
287 |         details = self.query_one("#color-details", ColorDetails)
288 |         h, s, l = details._get_hsl_values()
    |               ^ E741
289 |
290 |         # Adjust lightness (clamp 0-100)
    |

src/screens/color_picker_screen.py:291:9: E741 Ambiguous variable name: `l`
    |
290 |         # Adjust lightness (clamp 0-100)
291 |         l = max(0, min(100, l + amount))
    |         ^ E741
292 |
293 |         self._extracted_from_action_adjust_lightness_15(h, s, l)
    |

src/screens/color_picker_screen.py:296:64: E741 Ambiguous variable name: `l`
    |
295 |     # TODO Rename this here and in `action_adjust_hue`, `action_adjust_saturation` and `action_adjust_lightness`
296 |     def _extracted_from_action_adjust_lightness_15(self, h, s, l):
    |                                                                ^ E741
297 |         import colorsys
    |

src/screens/export_screen.py:273:18: RUF059 Unpacked variable `result` is never used
    |
272 |         # Use the try_operation method from BaseScreen
273 |         success, result, error_info = self.try_operation(
    |                  ^^^^^^ RUF059
274 |             operation=export_operation,
275 |             error_message=f"Error exporting palette to {file_path}",
    |
    = help: Prefix it with an underscore or any other dummy variable pattern

src/screens/export_screen.py:273:26: RUF059 Unpacked variable `error_info` is never used
    |
272 |         # Use the try_operation method from BaseScreen
273 |         success, result, error_info = self.try_operation(
    |                          ^^^^^^^^^^ RUF059
274 |             operation=export_operation,
275 |             error_message=f"Error exporting palette to {file_path}",
    |
    = help: Prefix it with an underscore or any other dummy variable pattern

src/screens/export_screen.py:300:18: RUF059 Unpacked variable `result` is never used
    |
299 |         # Use the try_operation method from BaseScreen
300 |         success, result, error_info = self.try_operation(
    |                  ^^^^^^ RUF059
301 |             operation=copy_operation,
302 |             error_message="Error copying to clipboard",
    |
    = help: Prefix it with an underscore or any other dummy variable pattern

src/screens/export_screen.py:300:26: RUF059 Unpacked variable `error_info` is never used
    |
299 |         # Use the try_operation method from BaseScreen
300 |         success, result, error_info = self.try_operation(
    |                          ^^^^^^^^^^ RUF059
301 |             operation=copy_operation,
302 |             error_message="Error copying to clipboard",
    |
    = help: Prefix it with an underscore or any other dummy variable pattern

src/screens/import_screen.py:178:27: RUF059 Unpacked variable `error_info` is never used
    |
177 |         # Use the try_operation method from BaseScreen
178 |         success, palette, error_info = self.try_operation(
    |                           ^^^^^^^^^^ RUF059
179 |             operation=import_operation,
180 |             error_message=f"Failed to import palette from {file_path}",
    |
    = help: Prefix it with an underscore or any other dummy variable pattern

src/screens/import_screen.py:219:27: RUF059 Unpacked variable `error_info` is never used
    |
218 |         # Use the try_operation method from BaseScreen
219 |         success, palette, error_info = self.try_operation(
    |                           ^^^^^^^^^^ RUF059
220 |             operation=process_operation,
221 |             error_message="Failed to process clipboard content",
    |
    = help: Prefix it with an underscore or any other dummy variable pattern

src/screens/import_screen.py:222:46: F821 Undefined name `palette`
    |
220 |             operation=process_operation,
221 |             error_message="Failed to process clipboard content",
222 |             success_message=f"Extracted {len(palette['colors']) if success and palette else 0} colors from clipboard",
    |                                              ^^^^^^^ F821
223 |             context={"content_preview": content[:50] + "..." if len(content) > 50 else content},
224 |         )
    |

src/screens/import_screen.py:222:68: F821 Undefined name `success`
    |
220 |             operation=process_operation,
221 |             error_message="Failed to process clipboard content",
222 |             success_message=f"Extracted {len(palette['colors']) if success and palette else 0} colors from clipboard",
    |                                                                    ^^^^^^^ F821
223 |             context={"content_preview": content[:50] + "..." if len(content) > 50 else content},
224 |         )
    |

src/screens/import_screen.py:222:80: F821 Undefined name `palette`
    |
220 |             operation=process_operation,
221 |             error_message="Failed to process clipboard content",
222 |             success_message=f"Extracted {len(palette['colors']) if success and palette else 0} colors from clipboard",
    |                                                                                ^^^^^^^ F821
223 |             context={"content_preview": content[:50] + "..." if len(content) > 50 else content},
224 |         )
    |

src/screens/import_screen.py:242:18: RUF059 Unpacked variable `palette` is never used
    |
241 |         # Use the try_operation method from BaseScreen
242 |         success, palette, error_info = self.try_operation(
    |                  ^^^^^^^ RUF059
243 |             operation=add_operation,
244 |             error_message="Failed to add palette to collection",
    |
    = help: Prefix it with an underscore or any other dummy variable pattern

src/screens/import_screen.py:242:27: RUF059 Unpacked variable `error_info` is never used
    |
241 |         # Use the try_operation method from BaseScreen
242 |         success, palette, error_info = self.try_operation(
    |                           ^^^^^^^^^^ RUF059
243 |             operation=add_operation,
244 |             error_message="Failed to add palette to collection",
    |
    = help: Prefix it with an underscore or any other dummy variable pattern

src/utils/color_adjustment.py:31:11: E741 Ambiguous variable name: `l`
   |
30 |     # Get current HSL values
31 |     h, s, l = color.hsl
   |           ^ E741
32 |
33 |     # Adjust hue (keep it in 0-360 range)
   |

src/utils/color_adjustment.py:56:11: E741 Ambiguous variable name: `l`
   |
55 |     # Get current HSL values
56 |     h, s, l = color.hsl
   |           ^ E741
57 |
58 |     # Adjust saturation (clamp between 0-100)
   |

src/utils/color_adjustment.py:81:11: E741 Ambiguous variable name: `l`
   |
80 |     # Get current HSL values
81 |     h, s, l = color.hsl
   |           ^ E741
82 |
83 |     # Adjust lightness (clamp between 0-100)
   |

src/utils/color_adjustment.py:108:11: E741 Ambiguous variable name: `l`
    |
107 |     # Get current HSL values
108 |     h, s, l = color.hsl
    |           ^ E741
109 |
110 |     # Adjust all properties (with appropriate constraints)
    |

src/utils/utter.py:107:17: PERF203 `try`-`except` within a loop incurs performance overhead
    |
105 |                           # Handle non-string values
106 |                           instance.bottles[bottle_name][var_name] = default_color
107 | /                 except Exception as e:
108 | |                     # If any error occurs, use default color and continue
109 | |                     instance.bottles[bottle_name][var_name] = default_color
110 | |                     # Optionally log the error
111 | |                     print(f"Error processing {var_name} in {bottle_name}: {e}")
    | |_______________________________________________________________________________^ PERF203
112 |
113 |           return instance
    |

src/widgets/ascii_widget.py:65:9: A002 Function argument `id` is shadowing a Python builtin
   |
63 |         pattern: str = "",
64 |         name: Optional[str] = None,
65 |         id: Optional[str] = None,
   |         ^^ A002
66 |         widget_id: Optional[str] = None,
67 |         classes: Optional[str] = None,
   |

src/widgets/ascii_widget.py:235:9: A002 Function argument `id` is shadowing a Python builtin
    |
233 |         variant: ButtonVariant = "default",
234 |         name: Optional[str] = None,
235 |         id: Optional[str] = None,
    |         ^^ A002
236 |         widget_id: Optional[str] = None,
237 |         classes: Optional[str] = None,
    |

src/widgets/ascii_widget.py:331:9: A002 Function argument `id` is shadowing a Python builtin
    |
329 |         active: bool = False,
330 |         name: Optional[str] = None,
331 |         id: Optional[str] = None,
    |         ^^ A002
332 |         widget_id: Optional[str] = None,
333 |         classes: Optional[str] = None,
    |

src/widgets/ascii_widget.py:433:16: RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
    |
432 |       # Define key bindings
433 |       BINDINGS = [
    |  ________________^
434 | |         Binding("enter", "submit", "Submit"),
435 | |         Binding("escape", "cancel", "Cancel"),
436 | |     ]
    | |_____^ RUF012
437 |
438 |       # Reactive property with type annotation
    |

src/widgets/ascii_widget.py:447:9: A002 Function argument `id` is shadowing a Python builtin
    |
445 |         focused: bool = False,
446 |         name: Optional[str] = None,
447 |         id: Optional[str] = None,
    |         ^^ A002
448 |         widget_id: Optional[str] = None,
449 |         classes: Optional[str] = None,
    |

src/widgets/ascii_widget.py:548:9: A002 Function argument `id` is shadowing a Python builtin
    |
546 |         selected_color: str = "#FFFFFF",
547 |         name: Optional[str] = None,
548 |         id: Optional[str] = None,
    |         ^^ A002
549 |         widget_id: Optional[str] = None,
550 |         classes: Optional[str] = None,
    |

src/widgets/ascii_widget.py:680:9: A002 Function argument `id` is shadowing a Python builtin
    |
678 |         active_index: int = 0,
679 |         name: Optional[str] = None,
680 |         id: Optional[str] = None,
    |         ^^ A002
681 |         widget_id: Optional[str] = None,
682 |         classes: Optional[str] = None,
    |

src/widgets/ascii_widget.py:919:9: A002 Function argument `id` is shadowing a Python builtin
    |
917 |         self,
918 |         name: Optional[str] = None,
919 |         id: Optional[str] = None,
    |         ^^ A002
920 |         widget_id: Optional[str] = None,
921 |         classes: Optional[str] = None,
    |

src/widgets/ascii_widget.py:1042:9: A002 Function argument `id` is shadowing a Python builtin
     |
1040 |         palette_name: str = "",
1041 |         name: Optional[str] = None,
1042 |         id: Optional[str] = None,
     |         ^^ A002
1043 |         classes: Optional[str] = None,
1044 |     ):
     |

src/widgets/ascii_widget.py:1085:9: F841 Local variable `ok_button` is assigned to but never used
     |
1083 |         """
1084 |         # Instead of using event.sender, we'll get the button by ID
1085 |         ok_button = self.query_one("#naming-ok-button", ButtonWidget)
     |         ^^^^^^^^^ F841
1086 |         cancel_button = self.query_one("#naming-cancel-button", ButtonWidget)
     |
     = help: Remove assignment to unused variable `ok_button`

src/widgets/ascii_widget.py:1086:9: F841 Local variable `cancel_button` is assigned to but never used
     |
1084 |         # Instead of using event.sender, we'll get the button by ID
1085 |         ok_button = self.query_one("#naming-ok-button", ButtonWidget)
1086 |         cancel_button = self.query_one("#naming-cancel-button", ButtonWidget)
     |         ^^^^^^^^^^^^^ F841
1087 |
1088 |         # Determine which button was clicked by checking all buttons
     |
     = help: Remove assignment to unused variable `cancel_button`

src/widgets/ascii_widget.py:1172:15: RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
     |
1171 |       # Available export formats
1172 |       FORMATS = [
     |  _______________^
1173 | |         ("CSS", "CSS Variables"),
1174 | |         ("SCSS", "SCSS Variables"),
1175 | |         ("LESS", "LESS Variables"),
1176 | |         ("JSON", "JSON Format"),
1177 | |         ("UTTER", "UTTER Arrays"),
1178 | |     ]
     | |_____^ RUF012
1179 |
1180 |       # Reactive properties
     |

src/widgets/ascii_widget.py:1187:9: A002 Function argument `id` is shadowing a Python builtin
     |
1185 |         selected_format: str = "CSS",
1186 |         name: Optional[str] = None,
1187 |         id: Optional[str] = None,
     |         ^^ A002
1188 |         classes: Optional[str] = None,
1189 |     ):
     |

src/widgets/ascii_widget.py:1230:9: F841 Local variable `ok_button` is assigned to but never used
     |
1228 |         """
1229 |         # Instead of using event.sender, we'll get the button by ID
1230 |         ok_button = self.query_one("#export-ok-button", ButtonWidget)
     |         ^^^^^^^^^ F841
1231 |         cancel_button = self.query_one("#export-cancel-button", ButtonWidget)
     |
     = help: Remove assignment to unused variable `ok_button`

src/widgets/ascii_widget.py:1231:9: F841 Local variable `cancel_button` is assigned to but never used
     |
1229 |         # Instead of using event.sender, we'll get the button by ID
1230 |         ok_button = self.query_one("#export-ok-button", ButtonWidget)
1231 |         cancel_button = self.query_one("#export-cancel-button", ButtonWidget)
     |         ^^^^^^^^^^^^^ F841
1232 |
1233 |         # Determine which button was clicked by checking all buttons
     |
     = help: Remove assignment to unused variable `cancel_button`

src/widgets/color/color_details.py:142:62: A002 Function argument `id` is shadowing a Python builtin
    |
140 |     display_format: reactive[str] = reactive("hex")
141 |
142 |     def __init__(self, color: Union[str, Color] = "#ffffff", id: Optional[str] = None, classes: Optional[str] = None):
    |                                                              ^^ A002
143 |         """
144 |         Initialize the color details widget.
    |

src/widgets/color/color_details.py:188:19: E741 Ambiguous variable name: `l`
    |
187 |             # HSL sliders (approximate values)
188 |             h, s, l = self._get_hsl_values()
    |                   ^ E741
189 |             with Container(classes="slider-row"):
190 |                 yield Static("H", classes="slider-label")
    |

src/widgets/color/color_details.py:263:15: E741 Ambiguous variable name: `l`
    |
262 |         # Update HSL slider values
263 |         h, s, l = self._get_hsl_values()
    |               ^ E741
264 |         self.query_one("#hue-slider", Slider).value = h
265 |         self.query_one("#hue-value", Static).update(f"{h}°")
    |

src/widgets/color/color_details.py:289:15: E741 Ambiguous variable name: `l`
    |
287 |     def _get_hsl_string(self) -> str:
288 |         """Get HSL representation of the current color."""
289 |         h, s, l = self._get_hsl_values()
    |               ^ E741
290 |         return f"hsl({h},{s}%,{l}%)"
    |

src/widgets/color/color_details.py:297:12: E741 Ambiguous variable name: `l`
    |
296 |         r, g, b = self.color.normalized
297 |         h, l, s = colorsys.rgb_to_hls(r, g, b)  # Note: rgb_to_hls returns h,l,s
    |            ^ E741
298 |         h_deg = round(h * 360)
299 |         s_pct = round(s * 100)
    |

src/widgets/color/color_details.py:306:15: E741 Ambiguous variable name: `l`
    |
304 |         """Generate harmonious colors based on the current color."""
305 |         # Get HSL values
306 |         h, s, l = self._get_hsl_values()
    |               ^ E741
307 |
308 |         # Calculate complementary color (opposite on color wheel)
    |

src/widgets/color/color_details.py:376:15: E741 Ambiguous variable name: `l`
    |
374 |     def _extracted_from_on_slider_changed_25(self, slider_id, value):
375 |         # Update HSL values
376 |         h, s, l = self._get_hsl_values()
    |               ^ E741
377 |
378 |         if slider_id == "hue-slider":
    |

src/widgets/color/color_details.py:382:13: E741 Ambiguous variable name: `l`
    |
380 |             self.query_one("#hue-value", Static).update(f"{h}°")
381 |         elif slider_id == "lightness-slider":
382 |             l = value
    |             ^ E741
383 |             self.query_one("#lightness-value", Static).update(f"{l}%")
    |

src/widgets/color/color_selector.py:281:52: A002 Function argument `id` is shadowing a Python builtin
    |
279 |             self.data = data or {}
280 |
281 |     def __init__(self, name: Optional[str] = None, id: Optional[str] = None, classes: Optional[str] = None):
    |                                                    ^^ A002
282 |         """Initialize the color picker widget."""
283 |         super().__init__(name=name, id=id, classes=classes)
    |

src/widgets/color/color_selector.py:313:16: RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
    |
312 |       # Global keyboard bindings
313 |       BINDINGS = [
    |  ________________^
314 | |         # Standard app actions
315 | |         Binding("q", "quit", "Quit"),
316 | |         Binding("ctrl+s", "save_palette", "Save palette"),
317 | |         Binding("ctrl+o", "load_palette", "Load palette"),
318 | |         # Palette editing actions
319 | |         Binding("n", "add_color", "Add color"),
320 | |         Binding("d", "delete_color", "Delete color"),
321 | |         Binding("r", "rename_palette", "Rename palette"),
322 | |         # View controls
323 | |         Binding("h", "toggle_help", "Toggle help"),
324 | |         Binding("tab", "next_section", "Next section"),
325 | |     ]
    | |_____^ RUF012
326 |
327 |       def compose(self) -> ComposeResult:
    |

src/widgets/color/color_wheel.py:42:9: A002 Function argument `id` is shadowing a Python builtin
   |
40 |         value: str = "",
41 |         on_change: Optional[Callable[[str], None]] = None,
42 |         id: Optional[str] = None,
   |         ^^ A002
43 |         classes: Optional[str] = None,
44 |     ):
   |

src/widgets/color/color_wheel.py:79:48: A002 Function argument `id` is shadowing a Python builtin
   |
77 |     color = reactive("#000000")
78 |
79 |     def __init__(self, color: str = "#000000", id: Optional[str] = None, classes: Optional[str] = None):
   |                                                ^^ A002
80 |         """
81 |         Initialize a color swatch.
   |

src/widgets/color/color_wheel.py:155:52: A002 Function argument `id` is shadowing a Python builtin
    |
153 |     selected_col = reactive(0)
154 |
155 |     def __init__(self, title: str = "COLOR WHEEL", id: Optional[str] = None, classes: Optional[str] = None):
    |                                                    ^^ A002
156 |         """
157 |         Initialize a color wheel widget.
    |

src/widgets/color/color_widget.py:181:13: F841 Local variable `grid_widget` is assigned to but never used
    |
179 |         try:
180 |             # Get the color grid widget
181 |             grid_widget = self.query_one("#color-grid", Static)
    |             ^^^^^^^^^^^ F841
182 |
183 |             # Since we can't directly check event.sender or event.target,
    |
    = help: Remove assignment to unused variable `grid_widget`

src/widgets/color/color_widget.py:307:16: RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
    |
306 |       # Define key bindings
307 |       BINDINGS = [
    |  ________________^
308 | |         Binding("enter", "apply_color", "Apply"),
309 | |         Binding("escape", "reset_color", "Reset"),
310 | |         Binding("backspace", "backspace", "Delete"),
311 | |     ]
    | |_____^ RUF012
312 |
313 |       current_color: reactive[str] = reactive("#FFFFFF")
    |

src/widgets/color/harmony_generator.py:153:58: A002 Function argument `id` is shadowing a Python builtin
    |
152 |     def __init__(
153 |         self, base_color: Union[str, Color] = "#FFFFFF", id: Optional[str] = None, classes: Optional[str] = None
    |                                                          ^^ A002
154 |     ):
155 |         """
    |

src/widgets/color/harmony_generator.py:240:19: E741 Ambiguous variable name: `l`
    |
238 |         elif harmony_type == HarmonyType.MONOCHROMATIC:
239 |             # Base color + variations of saturation and lightness
240 |             h, s, l = base.hsl
    |                   ^ E741
241 |             colors = [base]
    |

src/widgets/color/harmony_generator.py:271:15: E741 Ambiguous variable name: `l`
    |
269 |         # Base color + 2 colors on either side of complementary
270 |         comp = base.complementary()
271 |         h, s, l = comp.hsl
    |               ^ E741
272 |         h1 = (h - 30) % 360
273 |         h2 = (h + 30) % 360
    |

src/widgets/color/harmony_generator.py:287:9: F841 Local variable `colors_per_row` is assigned to but never used
    |
286 |         # Define the maximum number of colors to display per row
287 |         colors_per_row = 4
    |         ^^^^^^^^^^^^^^ F841
288 |
289 |         # Create a container for the harmony grid
    |
    = help: Remove assignment to unused variable `colors_per_row`

src/widgets/color/harmony_generator.py:316:19: E741 Ambiguous variable name: `l`
    |
315 |             # Add color info
316 |             h, s, l = color.hsl
    |                   ^ E741
317 |             info = f"H:{h}° S:{s}% L:{l}%"
318 |             info_label = Static(info, id=f"info-{i}", classes="color-info")
    |

src/widgets/export/export_widget.py:131:15: RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
    |
129 |     """
130 |
131 |     FORMATS = ["CSS", "SCSS", "LESS", "JSON", "TXT", "ASE", "GPL"]
    |               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ RUF012
132 |
133 |     selected_format: reactive[str] = reactive("CSS")
    |

src/widgets/export/export_widget.py:140:9: A002 Function argument `id` is shadowing a Python builtin
    |
138 |         selected_format: str = "CSS",
139 |         name: Optional[str] = None,
140 |         id: Optional[str] = None,
    |         ^^ A002
141 |         classes: Optional[str] = None,
142 |     ):
    |

src/widgets/export/export_widget.py:280:9: A002 Function argument `id` is shadowing a Python builtin
    |
278 |         formats: Optional[List[str]] = None,
279 |         name: Optional[str] = None,
280 |         id: Optional[str] = None,
    |         ^^ A002
281 |         classes: Optional[str] = None,
282 |     ):
    |

src/widgets/export/export_widget.py:403:9: A002 Function argument `id` is shadowing a Python builtin
    |
401 |         selected_format: str = "CSS",
402 |         name: Optional[str] = None,
403 |         id: Optional[str] = None,
    |         ^^ A002
404 |         classes: Optional[str] = None,
405 |     ):
    |

src/widgets/export/export_widget.py:532:13: PERF203 `try`-`except` within a loop incurs performance overhead
    |
530 |                   c = Color(color)
531 |                   sanitized_colors.append(c.hex_l)
532 | /             except Exception:
533 | |                 # Fall back to white for invalid colors
534 | |                 sanitized_colors.append("#FFFFFF")
    | |__________________________________________________^ PERF203
535 |
536 |           # Use sanitized colors for all format generation
    |

src/widgets/input_handler.py:103:52: A002 Function argument `id` is shadowing a Python builtin
    |
101 |             self.key = key
102 |
103 |     def __init__(self, name: Optional[str] = None, id: Optional[str] = None, classes: Optional[str] = None):
    |                                                    ^^ A002
104 |         """Initialize the input handler widget."""
105 |         # Ensure a default ID if not provided
    |

src/widgets/input_handler.py:107:13: A001 Variable `id` is shadowing a Python builtin
    |
105 |         # Ensure a default ID if not provided
106 |         if id is None:
107 |             id = "input_handler"
    |             ^^ A001
108 |         super().__init__(name=name, id=id, classes=classes)
    |

src/widgets/input_handler.py:185:16: RUF012 Mutable class attributes should be annotated with `typing.ClassVar`
    |
184 |       # Global keyboard bindings
185 |       BINDINGS = [
    |  ________________^
186 | |         # Standard app actions
187 | |         Binding("q", "quit", "Quit"),
188 | |         Binding("ctrl+s", "save_palette", "Save palette"),
189 | |         Binding("ctrl+o", "load_palette", "Load palette"),
190 | |         # Palette editing actions
191 | |         Binding("n", "add_color", "Add color"),
192 | |         Binding("d", "delete_color", "Delete color"),
193 | |         Binding("r", "rename_palette", "Rename palette"),
194 | |         # View controls
195 | |         Binding("h", "toggle_help", "Toggle help"),
196 | |         Binding("tab", "next_section", "Next section"),
197 | |     ]
    | |_____^ RUF012
198 |
199 |       def compose(self) -> ComposeResult:
    |

src/widgets/palette/palette_management.py:415:9: A002 Function argument `id` is shadowing a Python builtin
    |
413 |         color: str = "",
414 |         active: bool = False,
415 |         id: Optional[str] = None,
    |         ^^ A002
416 |         widget_id: Optional[str] = None,
417 |         classes: Optional[str] = None,
    |

src/widgets/palette/palette_management.py:472:9: A002 Function argument `id` is shadowing a Python builtin
    |
470 |         on_rename: Optional[Callable[[], None]] = None,
471 |         on_delete: Optional[Callable[[], None]] = None,
472 |         id: Optional[str] = None,
    |         ^^ A002
473 |         widget_id: Optional[str] = None,
474 |         classes: Optional[str] = None,
    |

src/widgets/palette/palette_management.py:517:9: A002 Function argument `id` is shadowing a Python builtin
    |
515 |         palettes: Optional[List[str]] = None,
516 |         on_select: Optional[Callable[[str], None]] = None,
517 |         id: Optional[str] = None,
    |         ^^ A002
518 |         widget_id: Optional[str] = None,
519 |         classes: Optional[str] = None,
    |

src/widgets/palette/palette_management.py:604:9: A002 Function argument `id` is shadowing a Python builtin
    |
602 |         active_color_index: Optional[int] = None,
603 |         palettes: Optional[Dict[str, List[str]]] = None,
604 |         id: Optional[str] = None,
    |         ^^ A002
605 |         classes: Optional[str] = None,
606 |     ):
    |

src/widgets/palette/palette_management.py:730:17: PERF203 `try`-`except` within a loop incurs performance overhead
    |
728 |                       slot = self.query_one(f"#color-slot-{i}", ColorSlot)
729 |                       slot.active = i == new_index
730 | /                 except Exception:
731 | |                     # Handle the case where a slot couldn't be found
732 | |                     pass
    | |________________________^ PERF203
733 |
734 |       def update_palette(
    |

src/widgets/palette/palette_widget.py:45:9: A002 Function argument `id` is shadowing a Python builtin
   |
43 |         interactive: bool = True,
44 |         name: Optional[str] = None,
45 |         id: Optional[str] = None,
   |         ^^ A002
46 |         classes: Optional[str] = None,
47 |     ):
   |

src/widgets/palette/palette_widget.py:78:9: A002 Function argument `id` is shadowing a Python builtin
   |
76 |         active: bool = False,
77 |         name: Optional[str] = None,
78 |         id: Optional[str] = None,
   |         ^^ A002
79 |         classes: Optional[str] = None,
80 |     ):
   |

src/widgets/palette/palette_widget.py:133:9: A002 Function argument `id` is shadowing a Python builtin
    |
131 |         active_palette_id: Optional[str] = None,
132 |         name: Optional[str] = None,
133 |         id: Optional[str] = None,
    |         ^^ A002
134 |         classes: Optional[str] = None,
135 |     ):
    |

src/widgets/palette/palette_widget.py:254:9: A002 Function argument `id` is shadowing a Python builtin
    |
252 |         active: bool = False,
253 |         name: Optional[str] = None,
254 |         id: Optional[str] = None,
    |         ^^ A002
255 |         classes: Optional[str] = None,
256 |     ):
    |

src/widgets/palette/palette_widget.py:303:9: A002 Function argument `id` is shadowing a Python builtin
    |
301 |         active_slot_index: int = 0,
302 |         name: Optional[str] = None,
303 |         id: Optional[str] = None,
    |         ^^ A002
304 |         classes: Optional[str] = None,
305 |     ):
    |

src/widgets/palette/palette_widget.py:454:9: A002 Function argument `id` is shadowing a Python builtin
    |
452 |         active: bool = False,
453 |         name: Optional[str] = None,
454 |         id: Optional[str] = None,
    |         ^^ A002
455 |         classes: Optional[str] = None,
456 |     ):
    |

src/widgets/palette/palette_widget.py:581:9: A002 Function argument `id` is shadowing a Python builtin
    |
579 |         current_name: str = "",
580 |         name: Optional[str] = None,
581 |         id: Optional[str] = None,
    |         ^^ A002
582 |         classes: Optional[str] = None,
583 |     ):
    |

Found 208 errors (124 fixed, 84 remaining).
