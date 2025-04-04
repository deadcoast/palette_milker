"""
Palette organization screen for the Palette Milker application.

This screen provides a comprehensive interface for managing palettes,
including options to create, rename, duplicate, delete, and export palettes.
"""

from typing import ClassVar
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container
from textual.containers import ScrollableContainer
from textual.message import Message
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Button
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import Input
from textual.widgets import Static

from ..models.palette_model import Palette
from ..models.palette_model import PaletteCollection


class PaletteActionRequest(Message):
    """Message requesting a palette action."""

    def __init__(self, action: str, palette_id: str, data: Optional[Dict] = None) -> None:
        """
        Initialize with action, palette ID, and optional data.

        Args:
            action: Action to perform (rename, duplicate, delete, etc.)
            palette_id: ID of the palette to act on
            data: Optional additional data for the action
        """
        self.action = action
        self.palette_id = palette_id
        self.data = data or {}
        super().__init__()


class PaletteOrganizationScreen(Screen):
    """
    Screen for managing and organizing palettes.

    This screen provides a user interface for renaming, duplicating,
    deleting, and reordering palettes.
    """

    BINDINGS: ClassVar[List[Union[Binding, Tuple[str, str], Tuple[str, str, str]]]] = [
        # Navigation
        Binding("escape", "app.view_palette", "Back to palettes"),
        Binding("ctrl+n", "new_palette", "New palette"),
        # Direct actions
        Binding("d", "delete_palette", "Delete palette"),
        Binding("r", "rename_palette", "Rename palette"),
        Binding("c", "duplicate_palette", "Duplicate palette"),
        Binding("e", "export_palette", "Export palette"),
        # Organization
        Binding("up", "move_up", "Move palette up"),
        Binding("down", "move_down", "Move palette down"),
    ]

    DEFAULT_CSS = """
    PaletteOrganizationScreen {
        background: $surface;
    }

    #org-header {
        dock: top;
        height: 1;
        background: $primary;
        color: $text;
        text-align: center;
        padding: 0 1;
    }

    #palette-list {
        width: 100%;
        height: 1fr;
        padding: 0 1;
    }

    .palette-card {
        width: 100%;
        min-height: 7;
        margin: 1 0;
        background: $panel;
        border: solid $primary;
    }

    .palette-card-selected {
        border: tall $accent;
    }

    .palette-header {
        width: 100%;
        height: 1;
        background: $primary;
        color: $text;
        padding: 0 1;
    }

    .palette-colors {
        width: 100%;
        height: 3;
        layout: horizontal;
    }

    .palette-color {
        width: 1fr;
        height: 100%;
        border: solid $background;
    }

    .palette-actions {
        width: 100%;
        height: 3;
        layout: horizontal;
        padding: 0 1;
    }

    .palette-actions Button {
        margin-right: 1;
        min-width: 10;
    }

    #bottom-actions {
        dock: bottom;
        width: 100%;
        height: 3;
        layout: horizontal;
        background: $panel-darken-1;
        padding: 0 1;
    }

    #bottom-actions Button {
        margin-right: 1;
        min-width: 12;
    }

    #rename-dialog {
        width: 100%;
        height: 3;
        layout: horizontal;
        background: $panel;
        display: none;
    }

    #rename-dialog.visible {
        display: block;
    }

    #rename-input {
        width: 70%;
    }

    #rename-buttons {
        width: 30%;
        layout: horizontal;
    }
    """

    # Reactive properties
    selected_palette_id: reactive[Optional[str]] = reactive(None)

    def __init__(self, palette_collection: PaletteCollection):
        """
        Initialize the palette organization screen.

        Args:
            palette_collection: Collection of palettes to manage
        """
        super().__init__()
        self.palette_collection = palette_collection
        # Initialize selected palette to first palette if available
        if palette_collection.palettes:
            self.selected_palette_id = palette_collection.palettes[0].palette_id

    def compose(self) -> ComposeResult:
        """Compose the palette organization screen UI."""
        # Header and title
        yield Header()
        yield Static("PALETTE ORGANIZATION", id="org-header")

        # Main content - scrollable list of palettes
        palette_list = ScrollableContainer(id="palette-list")
        yield palette_list

        # Create and mount palette cards
        for palette in self.palette_collection.palettes:
            card = self._create_palette_card(palette)
            palette_list.mount(card)

        # Bottom action buttons
        with Container(id="bottom-actions"):
            yield Button("New Palette", id="new-palette", variant="primary")
            yield Button("Import", id="import-palette")
            yield Button("Back", id="back-button")

        # Rename dialog (initially hidden)
        with Container(id="rename-dialog"):
            yield Input(placeholder="New palette name", id="rename-input")
            with Container(id="rename-buttons"):
                yield Button("OK", id="rename-confirm", variant="primary")
                yield Button("Cancel", id="rename-cancel")

        yield Footer()

    def _create_palette_card(self, palette: Palette) -> Container:
        """
        Create a card container for a palette.

        Args:
            palette: The palette to create a card for

        Returns:
            A Container widget representing the palette card
        """
        # Determine if this palette is selected
        is_selected = palette.palette_id == self.selected_palette_id
        classes = "palette-card"
        if is_selected:
            classes += " palette-card-selected"

        # Create the palette card container
        card = Container(id=f"palette-{palette.palette_id}", classes=classes)

        # Palette header with name
        header = Static(palette.name, classes="palette-header")
        card.mount(header)

        # Color swatches container
        colors_container = Container(classes="palette-colors")
        card.mount(colors_container)

        # Add color swatches
        for color_hex in palette.hex_colors:
            color_swatch = Static("", classes="palette-color")
            color_swatch.styles.background = color_hex
            colors_container.mount(color_swatch)

        # Action buttons container
        actions_container = Container(classes="palette-actions")
        card.mount(actions_container)

        # Add action buttons
        actions_container.mount(Button("Rename", id=f"rename-{palette.palette_id}"))
        actions_container.mount(Button("Duplicate", id=f"duplicate-{palette.palette_id}"))
        actions_container.mount(Button("Delete", id=f"delete-{palette.palette_id}", variant="error"))
        actions_container.mount(Button("Export", id=f"export-{palette.palette_id}"))

        return card

    def watch_selected_palette_id(self, old_id: Optional[str], new_id: Optional[str]) -> None:
        """React to changes in the selected palette."""
        # Remove selection from all cards
        for card in self.query(".palette-card"):
            card.remove_class("palette-card-selected")

        # Add selection to the selected card
        if new_id:
            try:
                card = self.query_one(f"#palette-{new_id}", Container)
                card.add_class("palette-card-selected")
            except Exception:
                # Ignore if the card doesn't exist
                pass

    def on_container_click(self, event) -> None:
        """Handle clicks on palette cards."""
        # Check if this is a palette card
        container = event.widget
        container_id = container.id

        if not container_id or not container_id.startswith("palette-"):
            return

        # Extract the palette ID
        palette_id = container_id[len("palette-") :]
        self.selected_palette_id = palette_id

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id

        # Bottom action buttons
        if button_id == "new-palette":
            self.action_new_palette()
        elif button_id == "import-palette":
            self.app.switch_screen("import")
        elif button_id == "back-button":
            self.app.switch_screen("main")

        # Rename dialog buttons
        elif button_id == "rename-confirm":
            self._confirm_rename()
        elif button_id == "rename-cancel":
            self._cancel_rename()

        # Palette action buttons
        elif button_id and "-" in button_id:
            action, palette_id = button_id.split("-", 1)

            if action == "rename":
                self._show_rename_dialog(palette_id)
            elif action == "duplicate":
                self.action_duplicate_palette(palette_id)
            elif action == "delete":
                self.action_delete_palette(palette_id)
            elif action == "export":
                self.action_export_palette(palette_id)

    def _show_rename_dialog(self, palette_id: str) -> None:
        """
        Show the rename dialog for a palette.

        Args:
            palette_id: ID of the palette to rename
        """
        # Store the palette ID for the confirmation handler
        self._renaming_palette_id = palette_id

        # Set the initial value to the current name
        palette = self.palette_collection.get_palette(palette_id)
        if palette:
            rename_input = self.query_one("#rename-input", Input)
            rename_input.value = palette.name

        # Show the dialog
        rename_dialog = self.query_one("#rename-dialog", Container)
        rename_dialog.add_class("visible")

        # Focus the input
        rename_input = self.query_one("#rename-input", Input)
        rename_input.focus()

    def _confirm_rename(self) -> None:
        """Confirm renaming the palette."""
        # Get the new name from the input
        rename_input = self.query_one("#rename-input", Input)
        new_name = rename_input.value

        if not hasattr(self, "_renaming_palette_id") or not new_name:
            return

        # Post message to rename the palette
        self.post_message(
            PaletteActionRequest(action="rename", palette_id=self._renaming_palette_id, data={"new_name": new_name})
        )

        # Update the UI
        self._update_palette_card(self._renaming_palette_id)

        # Hide the dialog
        rename_dialog = self.query_one("#rename-dialog", Container)
        rename_dialog.remove_class("visible")

        # Clear the stored ID
        delattr(self, "_renaming_palette_id")

    def _cancel_rename(self) -> None:
        """Cancel renaming the palette."""
        # Hide the dialog
        rename_dialog = self.query_one("#rename-dialog", Container)
        rename_dialog.remove_class("visible")

        # Clear the stored ID
        if hasattr(self, "_renaming_palette_id"):
            delattr(self, "_renaming_palette_id")

    def _update_palette_cards(self) -> None:
        """Update all palette cards to reflect the current state."""
        # Get the container for the palette list
        container = self.query_one("#palette-list", ScrollableContainer)

        # Remove existing cards
        container.remove_children()

        # Add cards for all palettes
        for palette in self.palette_collection.palettes:
            card = self._create_palette_card(palette)
            container.mount(card)

    def _update_palette_card(self, palette_id: str) -> None:
        """
        Update a single palette card.

        Args:
            palette_id: ID of the palette to update
        """
        # Find the palette
        palette = self.palette_collection.get_palette(palette_id)
        if not palette:
            return

        # Find the card
        try:
            card = self.query_one(f"#palette-{palette_id}", Container)

            # Update the header with the new name
            header = card.query_one(".palette-header", Static)
            header.update(palette.name)

            # Update the color swatches
            color_swatches = card.query(".palette-color")
            for i, swatch in enumerate(color_swatches):
                if i < len(palette.hex_colors):
                    swatch.styles.background = palette.hex_colors[i]

        except Exception:
            # If the card doesn't exist, rebuild all cards
            self._update_palette_cards()

    # Action methods
    def action_new_palette(self) -> None:
        """Create a new palette."""
        self.post_message(
            PaletteActionRequest(
                action="new",
                palette_id="",  # No ID needed for new palettes
                data={"name": f"New Palette {len(self.palette_collection)}"},
            )
        )

    def action_delete_palette(self, palette_id: Optional[str] = None) -> None:
        """
        Delete a palette.

        Args:
            palette_id: ID of the palette to delete, uses selected palette if None
        """
        target_id = palette_id or self.selected_palette_id
        if not target_id:
            return

        self.post_message(PaletteActionRequest(action="delete", palette_id=target_id))

        # Update UI
        self._update_palette_cards()

        # Select first palette if available
        if self.palette_collection.palettes:
            self.selected_palette_id = self.palette_collection.palettes[0].palette_id
        else:
            self.selected_palette_id = None

    def action_duplicate_palette(self, palette_id: Optional[str] = None) -> None:
        """
        Duplicate a palette.

        Args:
            palette_id: ID of the palette to duplicate, uses selected palette if None
        """
        target_id = palette_id or self.selected_palette_id
        if not target_id:
            return

        self.post_message(PaletteActionRequest(action="duplicate", palette_id=target_id))

        # Update UI
        self._update_palette_cards()

    def action_rename_palette(self) -> None:
        """Show rename dialog for the selected palette."""
        if not self.selected_palette_id:
            return

        self._show_rename_dialog(self.selected_palette_id)

    def action_export_palette(self, palette_id: Optional[str] = None) -> None:
        """
        Export a palette.

        Args:
            palette_id: ID of the palette to export, uses selected palette if None
        """
        target_id = palette_id or self.selected_palette_id
        if not target_id:
            return

        self.post_message(PaletteActionRequest(action="export", palette_id=target_id))

    def action_move_up(self) -> None:
        """Move the selected palette up in the list."""
        if not self.selected_palette_id:
            return

        self.post_message(
            PaletteActionRequest(action="move", palette_id=self.selected_palette_id, data={"direction": "up"})
        )

        # Update UI
        self._update_palette_cards()

    def action_move_down(self) -> None:
        """Move the selected palette down in the list."""
        if not self.selected_palette_id:
            return

        self.post_message(
            PaletteActionRequest(action="move", palette_id=self.selected_palette_id, data={"direction": "down"})
        )

        # Update UI
        self._update_palette_cards()
