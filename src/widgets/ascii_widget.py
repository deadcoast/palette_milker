"""
Custom Textual widgets that render ASCII UI elements using pattern-based approach.

These widgets dynamically construct ASCII UI elements from patterns,
allowing for consistent styling while maintaining flexibility.
"""

from typing import ClassVar
from typing import List
from typing import Literal
from typing import Optional
from typing import Tuple

from textual import events
from textual.app import ComposeResult
from textual.binding import Binding
from textual.color import Color
from textual.containers import Container
from textual.containers import Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Button
from textual.widgets import Input
from textual.widgets import Static

from src.constants.builder import build_browse_tree
from src.constants.builder import build_color_palette
from src.constants.builder import build_color_wheel
from src.constants.builder import build_export_dialog
from src.constants.builder import build_naming_dialog
from src.constants.builder import build_palette_management


class ASCIIWidget(Container):
    """Base widget for rendering ASCII UI elements using patterns.

    This widget serves as a container that can display ASCII art patterns while
    also containing other widgets. It provides a foundation for creating
    custom UI elements with a text-based aesthetic.

    Attributes:
        ascii_pattern: The ASCII pattern to display as a background
    """

    DEFAULT_CSS = """
    ASCIIWidget {
        background: transparent;
    }

    ASCIIWidget #ascii-content {
        width: 100%;
        height: 100%;
        z-index: 0;
    }
    """

    # Reactive property to store the ASCII pattern
    ascii_pattern: reactive[str] = reactive("")  # The ASCII pattern string to display

    def __init__(
        self,
        pattern: str = "",
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ASCIIWidget.

        Args:
            pattern: The initial ASCII pattern to display
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.ascii_pattern = pattern

    def compose(self) -> ComposeResult:
        """Compose the widget with the ASCII content.

        This method yields a Static widget that displays the ASCII pattern.

        Returns:
            Generator of child widgets
        """
        # Static for displaying the ASCII pattern
        yield Static(self.ascii_pattern, id="ascii-content")

    def on_mount(self) -> None:
        """Handle widget mounting.

        This method is called when the widget is mounted to the DOM.
        It generates the ASCII pattern if none is provided.
        """
        # Generate the ASCII pattern if not already set
        if not self.ascii_pattern:
            self.ascii_pattern = self.generate_ascii_pattern()
            self.update_ascii_content()

    def generate_ascii_pattern(self) -> str:
        """
        Generate the ASCII pattern.

        This method should be overridden by subclasses to provide
        specific ASCII patterns.

        Returns:
            The ASCII pattern as a string
        """
        return ""

    def watch_ascii_pattern(self, old_pattern: str, new_pattern: str) -> None:
        """Watch for changes to the ASCII pattern.

        Args:
            old_pattern: Previous ASCII pattern
            new_pattern: New ASCII pattern
        """
        # Update the ASCII content
        self.update_ascii_content()

    def update_ascii_content(self) -> None:
        """Update the ASCII content Static widget.

        This method updates the displayed ASCII pattern when it changes.
        It handles cases where the widget might not be mounted yet.
        """
        try:
            ascii_content = self.query_one("#ascii-content", Static)
            ascii_content.update(self.ascii_pattern)
        except Exception as e:
            # Widget may not be mounted yet
            print(f"Error updating ASCII content: {e}")

    def update_pattern(self, pattern: str) -> None:
        """
        Update the ASCII pattern.

        This is a convenience method that updates the ascii_pattern
        reactive property.

        Args:
            pattern: The new ASCII pattern
        """
        self.ascii_pattern = pattern


class ButtonClicked(Message):
    """Message sent when a button is clicked."""

    def __init__(self) -> None:
        """Initialize the message.

        The sender is automatically available as message.sender
        """
        super().__init__()


class ColorButtonClicked(Message):
    """Message sent when a color button is clicked."""

    def __init__(self, color: str) -> None:
        """Initialize the message with the color.

        Args:
            color: The color of the button
        """
        super().__init__()
        self.color = color


class TextSubmitted(Message):
    """Message sent when text is submitted."""

    def __init__(self, text: str) -> None:
        """Initialize the message with the text.

        Args:
            text: The submitted text
        """
        super().__init__()
        self.text = text


# Define ButtonVariant type alias for type checking
ButtonVariant = Literal["default", "primary", "success", "warning", "error"]


class ButtonWidget(Button):
    """Widget for rendering a button with proper Textual Button functionality.

    This widget extends Textual's Button class to match the project's design
    while leveraging Textual's built-in button functionality.

    Attributes:
        text: The text displayed on the button (maps to Button's label)
        active: Whether the button is visually active
    """

    DEFAULT_CSS = """
    ButtonWidget {
        width: auto;
        height: 3;
        border: none;
        min-width: 15;
        box-sizing: border-box;
    }

    ButtonWidget.active {
        background: $accent-darken-2;
        color: $text;
    }
    """

    # Define class variables for component classes
    COMPONENT_CLASSES: ClassVar[set[str]] = {"button--active"}

    # Reactive properties with proper type annotations
    # These map to Button's properties
    active: reactive[bool] = reactive(False)  # Whether button is visually active

    def __init__(
        self,
        text: str = "Button",
        active: bool = False,
        width: int = 15,
        variant: ButtonVariant = "default",
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ButtonWidget.

        Args:
            text: The text to display in the button
            active: Whether the button is active
            width: The width of the button
            variant: The button variant (default, primary, success, error, warning)
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        # Initialize the Button parent
        super().__init__(
            label=text,
            variant=variant,
            name=name,
            id=widget_id,
            classes=classes,
        )

        # Set custom properties
        self.active = active
        self.styles.width = width

    def watch_active(self, old_active: bool, new_active: bool) -> None:
        """Watch for changes to the active state.

        Args:
            old_active: Previous active state
            new_active: New active state
        """
        if new_active:
            self.add_class("active")
            self.set_class(True, "button--active")
        else:
            self.remove_class("active")
            self.set_class(False, "button--active")

    def on_click(self, event: events.Click) -> None:
        """Handle click events by posting our custom message.

        Args:
            event: The click event
        """
        # Post our custom message for backward compatibility
        self.post_message(ButtonClicked())
        # Button doesn't have on_click to call super() on


class ColorButtonWidget(Widget):
    """Widget for rendering a color button using proper Textual composition.

    This widget displays a color swatch and allows users to select colors.
    When clicked, it sends a ColorButtonClicked message with the color value.

    Attributes:
        color: The color displayed in the button (hex format)
        active: Whether the button is visually active
    """

    DEFAULT_CSS = """
    ColorButtonWidget {
        width: 7;
        height: 3;
        padding: 0;
    }

    ColorButtonWidget.active {
        background: $accent-darken-2;
    }

    ColorButtonWidget .color-swatch {
        width: 5;
        height: 1;
        content-align: center middle;
    }
    """

    # Use proper type annotations for reactive properties
    color: reactive[str] = reactive("#FFFFFF")  # Color as hex string
    active: reactive[bool] = reactive(False)  # Whether button is active

    def __init__(
        self,
        color: str = "#FFFFFF",
        active: bool = False,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ColorButtonWidget.

        Args:
            color: The color to display (hex format)
            active: Whether the button is active
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.color = color
        self.active = active

    def compose(self) -> ComposeResult:
        """Compose the color button with a proper color swatch.

        Returns:
            Generator of child widgets
        """
        # Create a Static widget with the color hex value and appropriate style
        yield Static(self.color, classes="color-swatch", id="color-display")

    def on_mount(self) -> None:
        """Handle widget mounting.

        Sets up the initial state of the color swatch.
        """
        # Set up initial state
        swatch = self.query_one("#color-display", Static)
        swatch.styles.background = self.color

    def watch_active(self, old_active: bool, new_active: bool) -> None:
        """Watch for changes to the active state.

        Args:
            old_active: Previous active state
            new_active: New active state
        """
        if new_active:
            self.add_class("active")
        else:
            self.remove_class("active")

    def watch_color(self, old_color: str, new_color: str) -> None:
        """Watch for changes to the color.

        Args:
            old_color: Previous color value
            new_color: New color value
        """
        # Update the color swatch safely
        try:
            swatch = self.query_one("#color-display", Static)
            swatch.update(new_color)
            # Set background color on the swatch
            swatch.styles.background = new_color
        except Exception:
            # Widget may not be mounted yet - handle in on_mount
            pass

    def on_click(self, event: events.Click) -> None:
        """Handle click events by posting a ColorButtonClicked message.

        Args:
            event: The click event
        """
        self.post_message(ColorButtonClicked(self.color))


class TextInputWidget(Input):
    """Widget for text input with proper Textual Input functionality.

    This widget extends Textual's Input widget to provide a consistent
    look and feel with the rest of the application's UI components.
    It adds custom messaging for text submission and cancellation.

    Attributes:
        label_text: The text label for the input field
    """

    DEFAULT_CSS = """
    TextInputWidget {
        width: auto;
        height: 1;
        border: none;
        padding: 0;
    }

    TextInputWidget:focus {
        background: $accent-darken-2;
    }
    """

    # Define key bindings
    BINDINGS: ClassVar[List[Binding]] = [
        Binding("enter", "submit", "Submit"),
        Binding("escape", "cancel", "Cancel"),
    ]

    # Reactive property with type annotation
    label_text: reactive[str] = reactive("input")  # Label displayed before input

    def __init__(
        self,
        label: str = "input",
        text: str = "",
        focused: bool = False,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the TextInputWidget.

        Args:
            label: The label for the input field
            text: The initial text in the input
            focused: Whether the input should be focused initially
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(
            value=text,
            name=name,
            id=widget_id,
            classes=classes,
        )

        # Set properties
        self.label_text = label

        # Set focus
        if focused:
            self.focus()

    def watch_label_text(self, old_label: str, new_label: str) -> None:
        """Watch for changes to the label text.

        Updates the placeholder text when the label changes.

        Args:
            old_label: Previous label text
            new_label: New label text
        """
        self.placeholder = f"{new_label}:"
        self.refresh()

    async def action_submit(self) -> None:
        """Submit the current text.

        Posts a TextSubmitted message with the current input value
        and calls the parent class implementation for default behavior.
        """
        self.post_message(TextSubmitted(self.value))
        # Call the parent's implementation
        await super().action_submit()

    def action_cancel(self) -> None:
        """Cancel input and remove focus.

        This removes focus from the input field when
        the user presses the escape key.
        """
        self.blur()
        # Input doesn't have an action_cancel method, we just blur the input


class ColorWheelWidget(Container):
    """Widget for rendering a color wheel using ASCII patterns."""

    DEFAULT_CSS = """
    ColorWheelWidget {
        width: auto;
        height: auto;
    }

    ColorWheelWidget #color-wheel-ascii {
        width: 100%;
        height: auto;
    }

    ColorWheelWidget #controls {
        width: 100%;
        height: auto;
        margin-top: 1;
    }

    ColorWheelWidget #hex-input {
        width: 60%;
    }

    ColorWheelWidget #buttons {
        width: 40%;
    }
    """

    # Reactive properties with proper type annotations
    width: reactive[int] = reactive(60)
    height: reactive[int] = reactive(15)
    selected_color: reactive[str] = reactive("#FFFFFF")

    def __init__(
        self,
        width: int = 60,
        height: int = 15,
        selected_color: str = "#FFFFFF",
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ColorWheelWidget.

        Args:
            width: The width of the color wheel
            height: The height of the color wheel
            selected_color: Initial selected color
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.width = width
        self.height = height
        self.selected_color = selected_color

    def compose(self) -> ComposeResult:
        """Compose the widget with proper container nesting."""
        # Main container shows the ASCII art
        yield Static(build_color_wheel(self.width, self.height), id="color-wheel-ascii")

        # Controls container for inputs and buttons
        with Container(id="controls"):
            with Horizontal():
                # Hex input control
                yield TextInputWidget(label="HEX", text=self.selected_color, id="hex-input")

                # Buttons container
                with Horizontal(id="buttons"):
                    yield ButtonWidget(text="Pick", id="pick-button")
                    yield ButtonWidget(text="Save", id="save-button")

    def on_mount(self) -> None:
        """Handle widget mounting."""
        # Ensure initial state is correct
        self._update_wheel()

    def watch_width(self, old_width: int, new_width: int) -> None:
        """Watch for changes to the width.

        Args:
            old_width: Previous width
            new_width: New width
        """
        self._update_wheel()

    def watch_height(self, old_height: int, new_height: int) -> None:
        """Watch for changes to the height.

        Args:
            old_height: Previous height
            new_height: New height
        """
        self._update_wheel()

    def watch_selected_color(self, old_color: str, new_color: str) -> None:
        """Watch for changes to the selected color.

        Args:
            old_color: Previous selected color
            new_color: New selected color
        """
        # Update the hex input if it exists
        try:
            hex_input = self.query_one("#hex-input", TextInputWidget)
            hex_input.value = new_color
        except Exception:
            # Widget may not be mounted yet
            pass

    def _update_wheel(self) -> None:
        """Update the color wheel ASCII art."""
        try:
            # Get the ASCII representation of the color wheel
            ascii_wheel = build_color_wheel(self.width, self.height)

            # Update the wheel
            wheel = self.query_one("#color-wheel-ascii", Static)
            wheel.update(ascii_wheel)
        except Exception as e:
            # Log any errors that occur during the update
            print(f"Error updating color wheel: {e}")


class PaletteSlots(Container):
    """Container for color slots in a palette.

    This widget displays a horizontal collection of color slots representing
    a palette. It handles slot selection and color updates.

    Attributes:
        palette_colors: The list of colors in the palette (as hex strings)
        active_index: The index of the currently selected color
    """

    DEFAULT_CSS = """
    PaletteSlots {
        layout: horizontal;
        height: 3;
        margin: 0 1;
    }
    """

    # Reactive properties with proper type annotations and documentation
    palette_colors: reactive[List[str]] = reactive(
        ["#FFFFFF"] * 8, always_update=True, repaint=True
    )  # List of hex color strings in the palette

    active_index: reactive[int] = reactive(0)  # Index of the currently selected color in the palette

    # Use a property getter to avoid conflict with border
    @property
    def border_colors(self) -> Tuple[Color, Color, Color, Color]:
        """Get border colors for UI styling.

        Returns:
            Tuple of Color objects for border styling (top, right, bottom, left)
        """
        return (Color.parse("$primary"), Color.parse("$primary"), Color.parse("$primary"), Color.parse("$primary"))

    def __init__(
        self,
        colors: Optional[List[str]] = None,
        active_index: int = 0,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the PaletteSlots widget.

        Args:
            colors: The list of colors in the palette
            active_index: The index of the initially selected color
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.active_index = active_index
        if colors:
            self.palette_colors = colors

    def compose(self) -> ComposeResult:
        """Compose the widget with color slots.

        Returns:
            Generator of child widgets
        """
        # First show the ASCII representation
        yield Static(build_color_palette(self.palette_colors, self.active_index), id="palette-slots-ascii")

        # Create interactive color buttons that will overlay on the ASCII art
        for i, color in enumerate(self.palette_colors):
            yield ColorButtonWidget(color=color, active=i == self.active_index, id=f"color-slot-{i}")

    def watch_active_index(self, old_index: int, new_index: int) -> None:
        """Watch for changes to the active index and update UI accordingly.

        Args:
            old_index: Previous active index value
            new_index: New active index value
        """
        # Update button active states
        for i, widget in enumerate(self.query(ColorButtonWidget)):
            widget.active = i == new_index

        # Update ASCII representation
        self.query_one("#palette-slots-ascii", Static).update(build_color_palette(self.palette_colors, new_index))

    def watch_palette_colors(self, old_colors: List[str], new_colors: List[str]) -> None:
        """Watch for changes to the palette colors and update UI accordingly.

        Args:
            old_colors: Previous colors list
            new_colors: New colors list
        """
        # Update individual color widgets
        for i, (widget, color) in enumerate(zip(self.query(ColorButtonWidget), new_colors, strict=False)):
            if i < len(new_colors):
                widget.color = color

        # Update ASCII representation
        self.query_one("#palette-slots-ascii", Static).update(build_color_palette(new_colors, self.active_index))

    def update_color(self, index: int, color: str) -> None:
        """Update a specific color in the palette.

        Args:
            index: Index of the color to update
            color: New color value (hex)

        Raises:
            IndexError: If the index is outside the valid range
        """
        if not 0 <= index < len(self.palette_colors):
            raise IndexError(f"Color index {index} is out of range (0-{len(self.palette_colors) - 1})")
        # Create a new list to ensure reactive properties detect the change
        new_colors = self.palette_colors.copy()
        new_colors[index] = color
        # Set the entire list to trigger the watcher
        self.palette_colors = new_colors

    def select_color(self, index: int) -> None:
        """Select a color slot by index.

        Args:
            index: Index of the color to select

        Raises:
            IndexError: If the index is outside the valid range
        """
        if 0 <= index < len(self.palette_colors):
            self.active_index = index
        else:
            raise IndexError(f"Color index {index} is out of range (0-{len(self.palette_colors) - 1})")


class PaletteManagementWidget(Container):
    """Widget for rendering the palette management UI."""

    DEFAULT_CSS = """
    PaletteManagementWidget {
        width: auto;
        height: auto;
    }
    """

    # Use proper type annotations for reactive properties
    palette_name: reactive[str] = reactive("Default")
    active_palette_index: reactive[int] = reactive(0)
    palette_count: reactive[int] = reactive(4)
    width: reactive[int] = reactive(80)

    def __init__(
        self,
        palette_name: str = "Default",
        active_palette_index: int = 0,
        palette_count: int = 4,
        width: int = 80,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the PaletteManagementWidget.

        Args:
            palette_name: Name of the active palette
            active_palette_index: Index of the active palette
            palette_count: Number of palettes
            width: Total width of the UI
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.palette_name = palette_name
        self.active_palette_index = active_palette_index
        self.palette_count = palette_count
        self.width = width

    def compose(self) -> ComposeResult:
        """Compose the widget."""
        # ASCII representation
        yield Static(
            build_palette_management(self.palette_name, self.active_palette_index, self.palette_count, self.width),
            id="palette-management-ascii",
        )

        # Interactive components
        yield ButtonWidget(text="Add New", id="add-palette-button")
        yield ButtonWidget(text="Rename", id="rename-palette-button")
        yield ButtonWidget(text="Delete", id="delete-palette-button")

        # Palette slots
        yield PaletteSlots(id="palette-slots")

    def watch_palette_name(self, old_name: str, new_name: str) -> None:
        """Watch for changes to the palette name.

        Args:
            old_name: Previous palette name
            new_name: New palette name
        """
        self._update_ascii()

    def watch_active_palette_index(self, old_index: int, new_index: int) -> None:
        """Watch for changes to the active palette index.

        Args:
            old_index: Previous active palette index
            new_index: New active palette index
        """
        self._update_ascii()

    def watch_palette_count(self, old_count: int, new_count: int) -> None:
        """Watch for changes to the palette count.

        Args:
            old_count: Previous palette count
            new_count: New palette count
        """
        self._update_ascii()

    def watch_width(self, old_width: int, new_width: int) -> None:
        """Watch for changes to the width.

        Args:
            old_width: Previous width
            new_width: New width
        """
        self._update_ascii()

    def _update_ascii(self) -> None:
        """Update the ASCII representation."""
        self.query_one("#palette-management-ascii", Static).update(
            build_palette_management(self.palette_name, self.active_palette_index, self.palette_count, self.width)
        )


class BrowseTreeWidget(ASCIIWidget):
    """Widget for rendering the browse tree."""

    DEFAULT_CSS = """
    BrowseTreeWidget {
        width: auto;
        height: auto;
    }

    BrowseTreeWidget #ascii-content {
        width: 100%;
        height: auto;
    }

    BrowseTreeWidget .tree-item {
        height: 1;
        padding: 0 1;
        cursor: pointer;
    }

    BrowseTreeWidget .tree-item:hover {
        background: $accent;
    }

    BrowseTreeWidget .tree-item.active {
        background: $accent-darken-2;
        color: $text;
    }
    """

    # Reactive properties
    selected_item: reactive[str] = reactive("")
    expanded_items: reactive[List[str]] = reactive([])

    def __init__(
        self,
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """Initialize the BrowseTreeWidget."""
        super().__init__(name=name, widget_id=widget_id, classes=classes)

    def generate_ascii_pattern(self) -> str:
        """Generate the browse tree ASCII pattern."""
        return build_browse_tree()

    def compose(self) -> ComposeResult:
        """Compose the widget with interactable items."""
        # Let the parent compose the ASCII content
        yield from super().compose()

        # Add interactive elements that will be overlaid on the ASCII content
        yield Static("Palettes", classes="tree-item tree-section", id="section-palettes")
        yield Static("Default", classes="tree-item tree-palette", id="palette-default")
        yield Static("Monochrome", classes="tree-item tree-palette", id="palette-monochrome")

        yield Static("Arrays", classes="tree-item tree-section", id="section-arrays")
        yield Static("UTTERS", classes="tree-item tree-array", id="array-utters")
        yield Static("RGB", classes="tree-item tree-array", id="array-rgb")
        yield Static("HEX", classes="tree-item tree-array", id="array-hex")

    def on_static_click(self, event: events.Click) -> None:
        """Handle clicks on tree items."""
        # Check if the target has the tree-item class
        widget = event.widget
        if isinstance(widget, Static) and "tree-item" in widget.classes:
            # Get the item ID
            item_id = widget.id
            if item_id:
                # Update selected item
                self.selected_item = item_id
                # Post a message for the parent to handle
                self.post_message(self.ItemSelected(item_id))

    def watch_selected_item(self, old_item: str, new_item: str) -> None:
        """Watch for changes to the selected item.

        Args:
            old_item: Previously selected item ID
            new_item: Newly selected item ID
        """
        # Update the UI to reflect the selected item
        for item in self.query(".tree-item"):
            if item.id == new_item:
                item.add_class("active")
            else:
                item.remove_class("active")

    class ItemSelected(Message):
        """Message sent when a tree item is selected."""

        def __init__(self, item_id: str) -> None:
            """Initialize the message.

            Args:
                item_id: The ID of the selected item
            """
            super().__init__()
            self.item_id = item_id

    class ItemExpanded(Message):
        """Message sent when a tree section is expanded."""

        def __init__(self, section_id: str) -> None:
            """Initialize the message.

            Args:
                section_id: The ID of the expanded section
            """
            super().__init__()
            self.section_id = section_id


class NamingDialogWidget(Container):
    """Widget for rendering the palette naming dialog."""

    DEFAULT_CSS = """
    NamingDialogWidget {
        width: 45;
        height: 7;
        align: center middle;
        background: $surface;
        border: solid $primary;
    }

    NamingDialogWidget #dialog-content {
        width: 100%;
        height: 100%;
    }

    NamingDialogWidget #palette-name-input {
        width: 80%;
        margin: 1 2;
    }

    NamingDialogWidget #dialog-buttons {
        width: 100%;
        height: 1;
        align-horizontal: center;
        margin-top: 1;
    }

    NamingDialogWidget #naming-ok-button {
        min-width: 10;
    }

    NamingDialogWidget #naming-cancel-button {
        min-width: 10;
    }
    """

    # Reactive properties
    palette_name: reactive[str] = reactive("")

    def __init__(
        self,
        palette_name: str = "",
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the NamingDialogWidget.

        Args:
            palette_name: The initial palette name
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.palette_name = palette_name

    def compose(self) -> ComposeResult:
        """Compose the widget with proper container nesting."""
        # ASCII representation with border
        yield Static(build_naming_dialog(), id="dialog-content")

        # Name input field
        yield Input(value=self.palette_name, placeholder="Enter palette name", id="palette-name-input")

        # Buttons container for layout
        with Horizontal(id="dialog-buttons"):
            yield ButtonWidget(text="OK", id="naming-ok-button", variant="primary")
            yield ButtonWidget(text="Cancel", id="naming-cancel-button")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle changes to the input field.

        Args:
            event: The input changed event
        """
        if event.input.id == "palette-name-input":
            self.palette_name = event.value

    def on_button_clicked(self, event: ButtonClicked) -> None:
        """Handle button clicks.

        Args:
            event: The button clicked event
        """
        # Determine which button was clicked by checking all buttons
        buttons = list(self.query(ButtonWidget))
        for button in buttons:
            if button.has_focus or button.id in ["naming-ok-button", "naming-cancel-button"]:
                if button.id == "naming-ok-button":
                    # Submit the current palette name
                    self.post_message(self.NameSubmitted(self.palette_name))
                elif button.id == "naming-cancel-button":
                    # Cancel the dialog
                    self.post_message(self.Cancelled())

    def on_key(self, event: events.Key) -> None:
        """Handle key events.

        Args:
            event: The key event
        """
        if event.key == "enter":
            # Submit on Enter key
            self.post_message(self.NameSubmitted(self.palette_name))
        elif event.key == "escape":
            # Cancel on Escape key
            self.post_message(self.Cancelled())
            event.stop()

    class NameSubmitted(Message):
        """Message sent when a name is submitted."""

        def __init__(self, name: str) -> None:
            """Initialize the NameSubmitted message.

            Args:
                name: The submitted name
            """
            super().__init__()
            self.name = name

    class Cancelled(Message):
        """Message sent when the dialog is cancelled."""

        def __init__(self) -> None:
            """Initialize the Cancelled message."""
            super().__init__()


class ExportDialogWidget(Container):
    """Widget for rendering the export dialog."""

    DEFAULT_CSS = """
    ExportDialogWidget {
        width: 45;
        height: 7;
        align: center middle;
        background: $surface;
        border: solid $primary;
    }

    ExportDialogWidget #dialog-content {
        width: 100%;
        height: 100%;
    }

    ExportDialogWidget #export-format-select {
        width: 80%;
        margin: 1 2;
    }

    ExportDialogWidget #dialog-buttons {
        width: 100%;
        height: 1;
        align-horizontal: center;
        margin-top: 1;
    }

    ExportDialogWidget #export-ok-button {
        min-width: 10;
    }

    ExportDialogWidget #export-cancel-button {
        min-width: 10;
    }
    """

    # Available export formats
    FORMATS: ClassVar[List[Tuple[str, str]]] = [
        ("CSS", "CSS Variables"),
        ("SCSS", "SCSS Variables"),
        ("LESS", "LESS Variables"),
        ("JSON", "JSON Format"),
        ("UTTER", "UTTER Arrays"),
    ]

    # Reactive properties
    selected_format: reactive[str] = reactive("CSS")

    def __init__(
        self,
        selected_format: str = "CSS",
        name: Optional[str] = None,
        widget_id: Optional[str] = None,
        classes: Optional[str] = None,
    ):
        """
        Initialize the ExportDialogWidget.

        Args:
            selected_format: The initially selected export format
            name: The name of the widget
            widget_id: The ID of the widget
            classes: The CSS classes to apply to the widget
        """
        super().__init__(name=name, id=widget_id, classes=classes)
        self.selected_format = selected_format if selected_format in [f[0] for f in self.FORMATS] else "CSS"

    def compose(self) -> ComposeResult:
        """Compose the widget with proper container nesting."""
        # ASCII representation with border
        yield Static(build_export_dialog(), id="dialog-content")

        # Format selection dropdown (simulated with Input for now)
        yield Input(value=self.selected_format, placeholder="Select export format", id="export-format-select")

        # Buttons container for layout
        with Horizontal(id="dialog-buttons"):
            yield ButtonWidget(text="Export", id="export-ok-button", variant="primary")
            yield ButtonWidget(text="Cancel", id="export-cancel-button")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle changes to the input field.

        Args:
            event: The input changed event
        """
        if event.input.id == "export-format-select" and event.value in [f[0] for f in self.FORMATS]:
            self.selected_format = event.value

    def on_button_clicked(self, event: ButtonClicked) -> None:
        """Handle button clicks.

        Args:
            event: The button clicked event
        """
        # Determine which button was clicked by checking all buttons
        buttons = list(self.query(ButtonWidget))
        for button in buttons:
            if button.has_focus or button.id in ["export-ok-button", "export-cancel-button"]:
                if button.id == "export-ok-button":
                    # Submit the current export format
                    self.post_message(self.FormatSelected(self.selected_format))
                elif button.id == "export-cancel-button":
                    # Cancel the dialog
                    self.post_message(self.Cancelled())

    def on_key(self, event: events.Key) -> None:
        """Handle key events.

        Args:
            event: The key event
        """
        if event.key == "enter":
            # Submit on Enter key
            self.post_message(self.FormatSelected(self.selected_format))
        elif event.key == "escape":
            # Cancel on Escape key
            self.post_message(self.Cancelled())
            event.stop()

    class FormatSelected(Message):
        """Message sent when a format is selected."""

        def __init__(self, format_name: str) -> None:
            """Initialize the FormatSelected message.

            Args:
                format_name: The selected format
            """
            super().__init__()
            self.format_name = format_name

    class Cancelled(Message):
        """Message sent when the dialog is cancelled."""

        def __init__(self) -> None:
            """Initialize the Cancelled message."""
            super().__init__()
