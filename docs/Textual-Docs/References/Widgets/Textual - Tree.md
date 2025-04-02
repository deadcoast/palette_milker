---
title: "Textual - Tree"
source: "https://textual.textualize.io/widgets/tree/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Tree¶

Added in version 0.6.0

A tree control widget.

- Focusable
- Container

## Example¶

The example below creates a simple tree.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Tree

class TreeApp(App):
    def compose(self) -> ComposeResult:
        tree: Tree[str] = Tree("Dune")
        tree.root.expand()
        characters = tree.root.add("Characters", expand=True)
        characters.add_leaf("Paul")
        characters.add_leaf("Jessica")
        characters.add_leaf("Chani")
        yield tree

if __name__ == "__main__":
    app = TreeApp()
    app.run()
```

Tree widgets have a "root" attribute which is an instance of a . Call or to add new nodes underneath the root. Both these methods return a TreeNode for the child which you can use to add additional levels.

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `show_root` | `bool` | `True` | Show the root node. |
| `show_guides` | `bool` | `True` | Show guide lines between levels. |
| `guide_depth` | `int` | `4` | Amount of indentation between parent and child. |

## Messages¶

## Bindings¶

The tree widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| enter | Select the current item. |
| space | Toggle the expand/collapsed space of the current item. |
| up | Move the cursor up. |
| down | Move the cursor down. |

## Component Classes¶

The tree widget provides the following component classes:

| Class | Description |
| --- | --- |
| `tree--cursor` | Targets the cursor. |
| `tree--guides` | Targets the indentation guides. |
| `tree--guides-hover` | Targets the indentation guides under the cursor. |
| `tree--guides-selected` | Targets the indentation guides that are selected. |
| `tree--highlight` | Targets the highlighted items. |
| `tree--highlight-line` | Targets the lines under the cursor. |
| `tree--label` | Targets the (text) labels of the items. |

---

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[ScrollView](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView " ScrollView (textual.scroll_view.ScrollView)")`

A widget for displaying and navigating data in a tree.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `label` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree\(label\) "Permanent link") | `TextType` | The label of the root node of the tree. | *required* |
| ## `data` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree\(data\) "Permanent link") | ` \| None` | The optional data to associate with the root node of the tree. | `None` |
| ## `name` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the Tree. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the tree in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the tree. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the tree is disabled or not. | `False` |

## BINDINGS [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding(
        "shift+left",
        "cursor_parent",
        "Cursor to parent",
        show=False,
    ),
    Binding(
        "shift+right",
        "cursor_parent_next_sibling",
        "Cursor to next ancestor",
        show=False,
    ),
    Binding(
        "shift+up",
        "cursor_previous_sibling",
        "Cursor to previous sibling",
        show=False,
    ),
    Binding(
        "shift+down",
        "cursor_next_sibling",
        "Cursor to next sibling",
        show=False,
    ),
    Binding("enter", "select_cursor", "Select", show=False),
    Binding("space", "toggle_node", "Toggle", show=False),
    Binding(
        "shift+space",
        "toggle_expand_all",
        "Expand or collapse all",
        show=False,
    ),
    Binding("up", "cursor_up", "Cursor Up", show=False),
    Binding(
        "down", "cursor_down", "Cursor Down", show=False
    ),
]
```

| Key(s) | Description |
| --- | --- |
| enter | Select the current item. |
| space | Toggle the expand/collapsed space of the current item. |
| up | Move the cursor up. |
| down | Move the cursor down. |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {
    "tree--cursor",
    "tree--guides",
    "tree--guides-hover",
    "tree--guides-selected",
    "tree--highlight",
    "tree--highlight-line",
    "tree--label",
}
```

| Class | Description |
| --- | --- |
| `tree--cursor` | Targets the cursor. |
| `tree--guides` | Targets the indentation guides. |
| `tree--guides-hover` | Targets the indentation guides under the cursor. |
| `tree--guides-selected` | Targets the indentation guides that are selected. |
| `tree--highlight` | Targets the highlighted items. |
| `tree--highlight-line` | Targets the lines under the cursor. |
| `tree--label` | Targets the (text) labels of the items. |

## ICON\_NODE [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.ICON_NODE "Permanent link")

```
ICON_NODE = '▶ '
```

Unicode 'icon' to use for an expandable node.

## ICON\_NODE\_EXPANDED [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.ICON_NODE_EXPANDED "Permanent link")

```
ICON_NODE_EXPANDED = '▼ '
```

Unicode 'icon' to use for an expanded node.

## auto\_expand [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.auto_expand "Permanent link")

```
auto_expand = var(True)
```

Auto expand tree nodes when they are selected.

## center\_scroll [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.center_scroll "Permanent link")

```
center_scroll = var(False)
```

Keep selected node in the center of the control, where possible.

## cursor\_line [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.cursor_line "Permanent link")

```
cursor_line = var(-1, always_update=True)
```

The line with the cursor, or -1 if no cursor.

## cursor\_node [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.cursor_node "Permanent link")

```
cursor_node
```

The currently selected node, or `None` if no selection.

## guide\_depth [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.guide_depth "Permanent link")

```
guide_depth = reactive(4, init=False)
```

The indent depth of tree nodes.

## hover\_line [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.hover_line "Permanent link")

```
hover_line = var(-1)
```

The line number under the mouse pointer, or -1 if not under the mouse pointer.

## last\_line [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.last_line "Permanent link")

```
last_line
```

The index of the last line.

## root [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.root "Permanent link")

```
root = _add_node(None, text_label, )
```

The root node of the tree.

## show\_guides [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.show_guides "Permanent link")

```
show_guides = reactive(True)
```

Enable display of tree guide lines.

## show\_root [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.show_root "Permanent link")

```
show_root = reactive(True)
```

Show the root of the tree.

## NodeCollapsed [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeCollapsed "Permanent link")

```
NodeCollapsed(node)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Event sent when a node is collapsed.

Can be handled using `on_tree_node_collapsed` in a subclass of `Tree` or in a parent node in the DOM.

### control [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeCollapsed.control "Permanent link")

```
control
```

The tree that sent the message.

### node [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeCollapsed.node "Permanent link")

```
node = node
```

The node that was collapsed.

## NodeExpanded [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeExpanded "Permanent link")

```
NodeExpanded(node)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Event sent when a node is expanded.

Can be handled using `on_tree_node_expanded` in a subclass of `Tree` or in a parent node in the DOM.

### control [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeExpanded.control "Permanent link")

```
control
```

The tree that sent the message.

### node [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeExpanded.node "Permanent link")

```
node = node
```

The node that was expanded.

## NodeHighlighted [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeHighlighted "Permanent link")

```
NodeHighlighted(node)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Event sent when a node is highlighted.

Can be handled using `on_tree_node_highlighted` in a subclass of `Tree` or in a parent node in the DOM.

### control [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeHighlighted.control "Permanent link")

```
control
```

The tree that sent the message.

### node [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeHighlighted.node "Permanent link")

```
node = node
```

The node that was highlighted.

## NodeSelected [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeSelected "Permanent link")

```
NodeSelected(node)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`, `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Event sent when a node is selected.

Can be handled using `on_tree_node_selected` in a subclass of `Tree` or in a parent node in the DOM.

### control [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeSelected.control "Permanent link")

```
control
```

The tree that sent the message.

### node [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.NodeSelected.node "Permanent link")

```
node = node
```

The node that was selected.

## action\_cursor\_down [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_cursor_down "Permanent link")

```
action_cursor_down()
```

Move the cursor down one node.

## action\_cursor\_next\_sibling [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_cursor_next_sibling "Permanent link")

```
action_cursor_next_sibling()
```

Move the cursor to the next sibling, or to the paren't sibling if there are no more siblings.

## action\_cursor\_parent [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_cursor_parent "Permanent link")

```
action_cursor_parent()
```

Move the cursor to the parent node.

## action\_cursor\_parent\_next\_sibling [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_cursor_parent_next_sibling "Permanent link")

```
action_cursor_parent_next_sibling()
```

Move the cursor to the parent's next sibling.

## action\_cursor\_previous\_sibling [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_cursor_previous_sibling "Permanent link")

```
action_cursor_previous_sibling()
```

Move the cursor to previous sibling, or to the parent if there are no more siblings.

## action\_cursor\_up [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_cursor_up "Permanent link")

```
action_cursor_up()
```

Move the cursor up one node.

## action\_page\_down [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_page_down "Permanent link")

```
action_page_down()
```

Move the cursor down a page's-worth of nodes.

## action\_page\_up [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_page_up "Permanent link")

```
action_page_up()
```

Move the cursor up a page's-worth of nodes.

## action\_scroll\_end [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_scroll_end "Permanent link")

```
action_scroll_end()
```

Move the cursor to the bottom of the tree.

Note

Here bottom means vertically, not branch depth.

## action\_scroll\_home [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_scroll_home "Permanent link")

```
action_scroll_home()
```

Move the cursor to the top of the tree.

## action\_select\_cursor [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_select_cursor "Permanent link")

```
action_select_cursor()
```

Cause a select event for the target node.

Note

If `auto_expand` is `True` use of this action on a non-leaf node will cause both an expand/collapse event to occur, as well as a selected event.

## action\_toggle\_expand\_all [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_toggle_expand_all "Permanent link")

```
action_toggle_expand_all()
```

Expand or collapse all siblings.

If all the siblings are collapsed then they will be expanded. Otherwise they will all be collapsed.

## action\_toggle\_node [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.action_toggle_node "Permanent link")

```
action_toggle_node()
```

Toggle the expanded state of the target node.

## add\_json [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.add_json "Permanent link")

```
add_json(, =None)
```

Adds JSON data to a node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `json_data` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.add_json\(json_data\) "Permanent link") | `[object](https://docs.python.org/3/library/functions.html#object)` | An object decoded from JSON. | *required* |
| ### `node` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.add_json\(node\) "Permanent link") | ` \| None` | Node to add data to. | `None` |

## clear [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.clear "Permanent link")

```
clear()
```

Clear all nodes under root.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Tree` instance. |

## get\_label\_width [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.get_label_width "Permanent link")

```
get_label_width()
```

Get the width of the nodes label.

The default behavior is to call `render_label` and return the cell length. This method may be overridden in a sub-class if it can be done more efficiently.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.get_label_width\(node\) "Permanent link") | `[]` | A node. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | Width in cells. |

## get\_node\_at\_line [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.get_node_at_line "Permanent link")

```
get_node_at_line()
```

Get the node for a given line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `line_no` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.get_node_at_line\(line_no\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | A line number. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[] \| None` | A tree node, or `None` if there is no node at that line. |

## get\_node\_by\_id [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.get_node_by_id "Permanent link")

```
get_node_by_id()
```

Get a tree node by its ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node_id` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.get_node_by_id\(node_id\) "Permanent link") |  | The ID of the node to get. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[]` | The node associated with that ID. |

Raises:

| Type | Description |
| --- | --- |
|  | Raised if the `TreeNode` ID is unknown. |

## move\_cursor [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.move_cursor "Permanent link")

```
move_cursor(, =False)
```

Move the cursor to the given node, or reset cursor.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.move_cursor\(node\) "Permanent link") | `[] \| None` | A tree node, or None to reset cursor. | *required* |
| ### `animate` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.move_cursor\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable animation | `False` |

## move\_cursor\_to\_line [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.move_cursor_to_line "Permanent link")

```
move_cursor_to_line(, =False)
```

Move the cursor to the given line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `line` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.move_cursor_to_line\(line\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The line number (negative indexes are offsets from the last line). | *required* |
| ### `animate` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.move_cursor_to_line\(animate\) "Permanent link") |  | Enable scrolling animation. | `False` |

Raises:

| Type | Description |
| --- | --- |
| `[IndexError](https://docs.python.org/3/library/exceptions.html#IndexError)` | If the line doesn't exist. |

## process\_label [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.process_label "Permanent link")

```
process_label()
```

Process a `str` or `Text` value into a label.

May be overridden in a subclass to change how labels are rendered.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `label` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.process_label\(label\) "Permanent link") | `TextType` | Label. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Text](https://rich.readthedocs.io/en/stable/reference/text.html#rich.text.Text "rich.text.Text")` | A Rich Text object. |

## render\_label [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.render_label "Permanent link")

```
render_label(, , )
```

Render a label for the given node. Override this to modify how labels are rendered.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.render_label\(node\) "Permanent link") | `[]` | A tree node. | *required* |
| ### `base_style` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.render_label\(base_style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | The base style of the widget. | *required* |
| ### `style` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.render_label\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | The additional style for the label. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Text](https://rich.readthedocs.io/en/stable/reference/text.html#rich.text.Text "rich.text.Text")` | A Rich Text object containing the label. |

## reset [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.reset "Permanent link")

```
reset(, =None)
```

Clear the tree and reset the root node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `label` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.reset\(label\) "Permanent link") | `TextType` | The label for the root node. | *required* |
| ### `data` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.reset\(data\) "Permanent link") | ` \| None` | Optional data for the root node. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Tree` instance. |

## scroll\_to\_line [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.scroll_to_line "Permanent link")

```
scroll_to_line(, =True)
```

Scroll to the given line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `line` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.scroll_to_line\(line\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | A line number. | *required* |
| ### `animate` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.scroll_to_line\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable animation. | `True` |

## scroll\_to\_node [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.scroll_to_node "Permanent link")

```
scroll_to_node(, =True)
```

Scroll to the given node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.scroll_to_node\(node\) "Permanent link") | `[]` | Node to scroll into view. | *required* |
| ### `animate` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.scroll_to_node\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Animate scrolling. | `True` |

## select\_node [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.select_node "Permanent link")

```
select_node()
```

Move the cursor to the given node and select it, or reset cursor.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.select_node\(node\) "Permanent link") | `[] \| None` | A tree node to move the cursor to and select, or None to reset cursor. | *required* |

## unselect [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.unselect "Permanent link")

```
unselect()
```

Hide and reset the cursor.

## validate\_cursor\_line [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.validate_cursor_line "Permanent link")

```
validate_cursor_line()
```

Prevent cursor line from going outside of range.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `value` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.validate_cursor_line\(value\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The value to test. | *required* |

Return

A valid version of the given value.

## validate\_guide\_depth [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.validate_guide_depth "Permanent link")

```
validate_guide_depth()
```

Restrict guide depth to reasonable range.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `value` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.validate_guide_depth\(value\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The value to test. | *required* |

Return

A valid version of the given value.

---

Make non-widget Tree support classes available.

## EventTreeDataType [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.EventTreeDataType "Permanent link")

```
EventTreeDataType = TypeVar('EventTreeDataType')
```

The type of the data for a given instance of a .

Similar to but used for `Tree` messages.

## NodeID [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.NodeID "Permanent link")

```
NodeID = NewType('NodeID', int)
```

The type of an ID applied to a .

## TreeDataType [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeDataType "Permanent link")

```
TreeDataType = TypeVar('TreeDataType')
```

The type of the data for a given instance of a .

## AddNodeError [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.AddNodeError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Exception raised when there is an error with a request to add a node.

## RemoveRootError [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.RemoveRootError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Exception raised when trying to remove the root of a .

## TreeNode [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode "Permanent link")

```
TreeNode(
    ,
    ,
    ,
    ,
    =None,
    *,
    =True,
    =True
)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`

An object that represents a "node" in a tree control.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `tree` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode\(tree\) "Permanent link") | `[]` | The tree that the node is being attached to. | *required* |
| ### `parent` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode\(parent\) "Permanent link") | `[] \| None` | The parent node that this node is being attached to. | *required* |
| ### `id` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode\(id\) "Permanent link") |  | The ID of the node. | *required* |
| ### `label` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode\(label\) "Permanent link") | `[Text](https://rich.readthedocs.io/en/stable/reference/text.html#rich.text.Text "rich.text.Text")` | The label for the node. | *required* |
| ### `data` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode\(data\) "Permanent link") | ` \| None` | Optional data to associate with the node. | `None` |
| ### `expanded` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode\(expanded\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Should the node be attached in an expanded state? | `True` |
| ### `allow_expand` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode\(allow_expand\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Should the node allow being expanded by the user? | `True` |

### allow\_expand [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.allow_expand "Permanent link")

```
allow_expand
```

Is this node allowed to expand?

### children [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.children "Permanent link")

```
children
```

The child nodes of a TreeNode.

### data [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.data "Permanent link")

```
data =
```

Optional data associated with the tree node.

### id [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.id "Permanent link")

```
id
```

The ID of the node.

### is\_collapsed [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.is_collapsed "Permanent link")

```
is_collapsed
```

Is the node collapsed?

### is\_expanded [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.is_expanded "Permanent link")

```
is_expanded
```

Is the node expanded?

### is\_last [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.is_last "Permanent link")

```
is_last
```

Is this the last child node of its parent?

### is\_root [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.is_root "Permanent link")

```
is_root
```

Is this node the root of the tree?

### label [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.label "Permanent link")

```
label
```

The label for the node.

### line [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.line "Permanent link")

```
line
```

The line number for this node, or -1 if it is not displayed.

### next\_sibling [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.next_sibling "Permanent link")

```
next_sibling
```

The next sibling below the node.

### parent [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.parent "Permanent link")

```
parent
```

The parent of the node.

### previous\_sibling [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.previous_sibling "Permanent link")

```
previous_sibling
```

The previous sibling below the node.

### siblings [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.siblings "Permanent link")

```
siblings
```

The siblings of this node (includes self).

### tree [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.tree "Permanent link")

```
tree
```

The tree that this node is attached to.

### add [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add "Permanent link")

```
add(
    ,
    =None,
    *,
    =None,
    =None,
    =False,
    =True
)
```

Add a node to the sub-tree.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `label` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add\(label\) "Permanent link") | `TextType` | The new node's label. | *required* |
| #### `data` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add\(data\) "Permanent link") | ` \| None` | Data associated with the new node. | `None` |
| #### `before` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add\(before\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [] \| None` | Optional index or `TreeNode` to add the node before. | `None` |
| #### `after` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add\(after\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [] \| None` | Optional index or `TreeNode` to add the node after. | `None` |
| #### `expand` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add\(expand\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Node should be expanded. | `False` |
| #### `allow_expand` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add\(allow_expand\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow user to expand the node via keyboard or mouse. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `[]` | A new Tree node |

Raises:

| Type | Description |
| --- | --- |
|  | If there is a problem with the addition request. |

Note

Only one of `before` or `after` can be provided. If both are provided a `AddNodeError` will be raised.

### add\_leaf [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add_leaf "Permanent link")

```
add_leaf(, =None, *, =None, =None)
```

Add a 'leaf' node (a node that can not expand).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `label` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add_leaf\(label\) "Permanent link") | `TextType` | Label for the node. | *required* |
| #### `data` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add_leaf\(data\) "Permanent link") | ` \| None` | Optional data. | `None` |
| #### `before` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add_leaf\(before\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [] \| None` | Optional index or `TreeNode` to add the node before. | `None` |
| #### `after` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.add_leaf\(after\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [] \| None` | Optional index or `TreeNode` to add the node after. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[]` | New node. |

Raises:

| Type | Description |
| --- | --- |
|  | If there is a problem with the addition request. |

Note

Only one of `before` or `after` can be provided. If both are provided a `AddNodeError` will be raised.

### collapse [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.collapse "Permanent link")

```
collapse()
```

Collapse the node (hide its children).

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `TreeNode` instance. |

### collapse\_all [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.collapse_all "Permanent link")

```
collapse_all()
```

Collapse the node (hide its children) and all those below it.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `TreeNode` instance. |

### expand [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.expand "Permanent link")

```
expand()
```

Expand the node (show its children).

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `TreeNode` instance. |

### expand\_all [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.expand_all "Permanent link")

```
expand_all()
```

Expand the node (show its children) and all those below it.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `TreeNode` instance. |

### refresh [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.refresh "Permanent link")

```
refresh()
```

Initiate a refresh (repaint) of this node.

### remove [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.remove "Permanent link")

```
remove()
```

Remove this node from the tree.

Raises:

| Type | Description |
| --- | --- |
|  | If there is an attempt to remove the root. |

### remove\_children [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.remove_children "Permanent link")

```
remove_children()
```

Remove any child nodes of this node.

### set\_label [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.set_label "Permanent link")

```
set_label()
```

Set a new label for the node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `label` [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.set_label\(label\) "Permanent link") | `TextType` | A `str` or `Text` object with the new label. | *required* |

### toggle [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.toggle "Permanent link")

```
toggle()
```

Toggle the node's expanded state.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `TreeNode` instance. |

### toggle\_all [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode.toggle_all "Permanent link")

```
toggle_all()
```

Toggle the node's expanded state and make all those below it match.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `TreeNode` instance. |

## UnknownNodeID [¶](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.UnknownNodeID "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Exception raised when referring to an unknown ID.