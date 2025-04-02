---
title: "Textual - textual.walk"
source: "https://textual.textualize.io/api/walk/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.walk

Functions for *walking* the DOM.

Note

For most purposes you would be better off using [query](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query " query"), which uses these functions internally.

## walk\_breadth\_first [¶](https://textual.textualize.io/api/walk/#textual.walk.walk_breadth_first "Permanent link")

```
walk_breadth_first(
    : DOMNode, *, : bool = True
) -> Iterable[DOMNode]
```
```
walk_breadth_first(
    : WalkType,
    : type[WalkType],
    *,
    : bool = True
) -> Iterable[WalkType]
```

```
walk_breadth_first(
    , =None, *, =True
)
```

Walk the tree breadth first (children first).

Note

Avoid changing the DOM (mounting, removing etc.) while iterating with this function. Consider [walk\_children](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.walk_children " walk_children") which doesn't have this limitation.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `root` [¶](https://textual.textualize.io/api/walk/#textual.walk.walk_breadth_first\(root\) "Permanent link") | `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")` | The root note (starting point). | *required* |
| ### `filter_type` [¶](https://textual.textualize.io/api/walk/#textual.walk.walk_breadth_first\(filter_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[WalkType] \| None` | Optional DOMNode subclass to filter by, or `None` for no filter. | `None` |
| ### `with_root` [¶](https://textual.textualize.io/api/walk/#textual.walk.walk_breadth_first\(with_root\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Include the root in the walk. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")] \| [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[WalkType]` | An iterable of DOMNodes, or the type specified in `filter_type`. |

## walk\_depth\_first [¶](https://textual.textualize.io/api/walk/#textual.walk.walk_depth_first "Permanent link")

```
walk_depth_first(
    : DOMNode, *, : bool = True
) -> Iterable[DOMNode]
```
```
walk_depth_first(
    : WalkType,
    : type[WalkType],
    *,
    : bool = True
) -> Iterable[WalkType]
```

```
walk_depth_first(, =None, *, =True)
```

Walk the tree depth first (parents first).

Note

Avoid changing the DOM (mounting, removing etc.) while iterating with this function. Consider [walk\_children](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.walk_children " walk_children") which doesn't have this limitation.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `root` [¶](https://textual.textualize.io/api/walk/#textual.walk.walk_depth_first\(root\) "Permanent link") | `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")` | The root note (starting point). | *required* |
| ### `filter_type` [¶](https://textual.textualize.io/api/walk/#textual.walk.walk_depth_first\(filter_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[WalkType] \| None` | Optional DOMNode subclass to filter by, or `None` for no filter. | `None` |
| ### `with_root` [¶](https://textual.textualize.io/api/walk/#textual.walk.walk_depth_first\(with_root\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Include the root in the walk. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")] \| [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[WalkType]` | An iterable of DOMNodes, or the type specified in `filter_type`. |