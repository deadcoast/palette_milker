---
title: "Textual - DirectoryTree"
source: "https://textual.textualize.io/widgets/directory_tree/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## DirectoryTree¶

A tree control to navigate the contents of your filesystem.

- Focusable
- Container

## Example¶

The example below creates a simple tree to navigate the current working directory.

```
from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree

class DirectoryTreeApp(App):
    def compose(self) -> ComposeResult:
        yield DirectoryTree("./")

if __name__ == "__main__":
    app = DirectoryTreeApp()
    app.run()
```

## Filtering¶

There may be times where you want to filter what appears in the `DirectoryTree`. To do this inherit from `DirectoryTree` and implement your own version of the `filter_paths` method. It should take an iterable of Python `Path` objects, and return those that pass the filter. For example, if you wanted to take the above code an filter out all of the "hidden" files and directories:

<!-- SVG content removed by SVG Remover -->

```
from pathlib import Path
from typing import Iterable

from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree

class FilteredDirectoryTree(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if not path.name.startswith(".")]

class DirectoryTreeApp(App):
    def compose(self) -> ComposeResult:
        yield FilteredDirectoryTree("./")

if __name__ == "__main__":
    app = DirectoryTreeApp()
    app.run()
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `show_root` | `bool` | `True` | Show the root node. |
| `show_guides` | `bool` | `True` | Show guide lines between levels. |
| `guide_depth` | `int` | `4` | Amount of indentation between parent and child. |

## Messages¶

## Bindings¶

The directory tree widget inherits [the bindings from the tree widget](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.BINDINGS " BINDINGS").

## Component Classes¶

The directory tree widget provides the following component classes:

| Class | Description |
| --- | --- |
| `directory-tree--extension` | Target the extension of a file name. |
| `directory-tree--file` | Target files in the directory structure. |
| `directory-tree--folder` | Target folders in the directory structure. |
| `directory-tree--hidden` | Target hidden items in the directory structure. |

See also the [component classes for `Tree`](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.COMPONENT_CLASSES " COMPONENT_CLASSES").

## See Also¶

- [Tree](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree " Tree") code reference

---

Bases: `[Tree](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree " Tree (textual.widgets._tree.Tree)")[[DirEntry](https://textual.textualize.io/api/types/#textual.types.DirEntry " DirEntry (textual.widgets._directory_tree.DirEntry)")]`

A Tree widget that presents files and directories.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `path` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree\(path\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")` | Path to directory. | *required* |
| ## `name` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget, or None for no name. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM, or None for no ID. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A space-separated list of classes, or None for no classes. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the directory tree is disabled or not. | `False` |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {
    "directory-tree--extension",
    "directory-tree--file",
    "directory-tree--folder",
    "directory-tree--hidden",
}
```

| Class | Description |
| --- | --- |
| `directory-tree--extension` | Target the extension of a file name. |
| `directory-tree--file` | Target files in the directory structure. |
| `directory-tree--folder` | Target folders in the directory structure. |
| `directory-tree--hidden` | Target hidden items in the directory structure. |

See also the [component classes for `Tree`](https://textual.textualize.io/widgets/tree/#textual.widgets.Tree.COMPONENT_CLASSES " COMPONENT_CLASSES").

## ICON\_FILE [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.ICON_FILE "Permanent link")

```
ICON_FILE = '📄 '
```

Unicode 'icon' to represent a file.

## PATH [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.PATH "Permanent link")

```
PATH = Path
```

Callable that returns a fresh path object.

## path [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.path "Permanent link")

```
path =
```

The path that is the root of the directory tree.

Note

This can be set to either a `str` or a `pathlib.Path` object, but the value will always be a `pathlib.Path` object.

## DirectorySelected [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.DirectorySelected "Permanent link")

```
DirectorySelected(, )
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when a directory is selected.

Can be handled using `on_directory_tree_directory_selected` in a subclass of `DirectoryTree` or in a parent widget in the DOM.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.DirectorySelected\(node\) "Permanent link") | `[TreeNode](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode " TreeNode (textual.widgets._tree.TreeNode)")[[DirEntry](https://textual.textualize.io/api/types/#textual.types.DirEntry " DirEntry (textual.widgets._directory_tree.DirEntry)")]` | The tree node for the directory that was selected. | *required* |
| ### `path` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.DirectorySelected\(path\) "Permanent link") | `[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")` | The path of the directory that was selected. | *required* |

### control [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.DirectorySelected.control "Permanent link")

```
control
```

The `Tree` that had a directory selected.

### node [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.DirectorySelected.node "Permanent link")

```
node =
```

The tree node of the directory that was selected.

### path [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.DirectorySelected.path "Permanent link")

```
path =
```

The path of the directory that was selected.

## FileSelected [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.FileSelected "Permanent link")

```
FileSelected(, )
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when a file is selected.

Can be handled using `on_directory_tree_file_selected` in a subclass of `DirectoryTree` or in a parent widget in the DOM.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.FileSelected\(node\) "Permanent link") | `[TreeNode](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode " TreeNode (textual.widgets._tree.TreeNode)")[[DirEntry](https://textual.textualize.io/api/types/#textual.types.DirEntry " DirEntry (textual.widgets._directory_tree.DirEntry)")]` | The tree node for the file that was selected. | *required* |
| ### `path` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.FileSelected\(path\) "Permanent link") | `[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")` | The path of the file that was selected. | *required* |

### control [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.FileSelected.control "Permanent link")

```
control
```

The `Tree` that had a file selected.

### node [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.FileSelected.node "Permanent link")

```
node =
```

The tree node of the file that was selected.

### path [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.FileSelected.path "Permanent link")

```
path =
```

The path of the file that was selected.

## clear\_node [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.clear_node "Permanent link")

```
clear_node(node)
```

Clear all nodes under the given node.

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Tree` instance. |

## filter\_paths [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.filter_paths "Permanent link")

```
filter_paths()
```

Filter the paths before adding them to the tree.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `paths` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.filter_paths\(paths\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")]` | The paths to be filtered. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")]` | The filtered paths. |

By default this method returns all of the paths provided. To create a filtered `DirectoryTree` inherit from it and implement your own version of this method.

## process\_label [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.process_label "Permanent link")

```
process_label()
```

Process a str or Text into a label. May be overridden in a subclass to modify how labels are rendered.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `label` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.process_label\(label\) "Permanent link") | `TextType` | Label. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Text](https://rich.readthedocs.io/en/stable/reference/text.html#rich.text.Text "rich.text.Text")` | A Rich Text object. |

## reload [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.reload "Permanent link")

```
reload()
```

Reload the `DirectoryTree` contents.

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An optionally awaitable that ensures the tree has finished reloading. |

## reload\_node [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.reload_node "Permanent link")

```
reload_node()
```

Reload the given node's contents.

The return value may be awaited to ensure the DirectoryTree has reached a stable state and is no longer performing any node reloading (of this node or any other nodes).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.reload_node\(node\) "Permanent link") | `[TreeNode](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode " TreeNode (textual.widgets._tree.TreeNode)")[[DirEntry](https://textual.textualize.io/api/types/#textual.types.DirEntry " DirEntry (textual.widgets._directory_tree.DirEntry)")]` | The root of the subtree to reload. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | An optionally awaitable that ensures the subtree has finished reloading. |

## render\_label [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.render_label "Permanent link")

```
render_label(, , )
```

Render a label for the given node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.render_label\(node\) "Permanent link") | `[TreeNode](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode " TreeNode (textual.widgets._tree.TreeNode)")[[DirEntry](https://textual.textualize.io/api/types/#textual.types.DirEntry " DirEntry (textual.widgets._directory_tree.DirEntry)")]` | A tree node. | *required* |
| ### `base_style` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.render_label\(base_style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | The base style of the widget. | *required* |
| ### `style` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.render_label\(style\) "Permanent link") | `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | The additional style for the label. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Text](https://rich.readthedocs.io/en/stable/reference/text.html#rich.text.Text "rich.text.Text")` | A Rich Text object containing the label. |

## reset\_node [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.reset_node "Permanent link")

```
reset_node(, , =None)
```

Clear the subtree and reset the given node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.reset_node\(node\) "Permanent link") | `[TreeNode](https://textual.textualize.io/widgets/tree/#textual.widgets.tree.TreeNode " TreeNode (textual.widgets._tree.TreeNode)")[[DirEntry](https://textual.textualize.io/api/types/#textual.types.DirEntry " DirEntry (textual.widgets._directory_tree.DirEntry)")]` | The node to reset. | *required* |
| ### `label` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.reset_node\(label\) "Permanent link") | `TextType` | The label for the node. | *required* |
| ### `data` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.reset_node\(data\) "Permanent link") | `[DirEntry](https://textual.textualize.io/api/types/#textual.types.DirEntry " DirEntry (textual.widgets._directory_tree.DirEntry)") \| None` | Optional data for the node. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `Tree` instance. |

## validate\_path [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.validate_path "Permanent link")

```
validate_path()
```

Ensure that the path is of the `Path` type.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `path` [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.validate_path\(path\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")` | The path to validate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")` | The validated Path value. |

Note

The result will always be a Python `Path` object, regardless of the value given.

## watch\_path [¶](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree.watch_path "Permanent link")

```
watch_path()
```

Watch for changes to the `path` of the directory tree.

If the path is changed the directory tree will be repopulated using the new value as the root.