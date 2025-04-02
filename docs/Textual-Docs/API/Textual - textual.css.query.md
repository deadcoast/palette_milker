---
title: "Textual - textual.css.query"
source: "https://textual.textualize.io/api/query/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.css.query

This module contains the `DOMQuery` class and related objects.

A DOMQuery is a set of DOM nodes returned by [query](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query " query").

The set of nodes may be further refined with and . Additional methods apply actions to all nodes in the query.

Info

If this sounds like JQuery, a (once) popular JS library, it is no coincidence.

## ExpectType [¶](https://textual.textualize.io/api/query/#textual.css.query.ExpectType "Permanent link")

```
ExpectType = TypeVar('ExpectType')
```

Type variable used to further restrict queries.

## QueryType [¶](https://textual.textualize.io/api/query/#textual.css.query.QueryType "Permanent link")

```
QueryType = TypeVar('QueryType', bound='Widget')
```

Type variable used to type generic queries.

## DOMQuery [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery "Permanent link")

```
DOMQuery(
    ,
    *,
    =None,
    =None,
    =True,
    =None
)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[]`

Warning

You won't need to construct this manually, as `DOMQuery` objects are returned by [query](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query " query").

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `node` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery\(node\) "Permanent link") | `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")` | A DOM node. | *required* |
| ### `filter` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery\(filter\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Query to filter children in the node. | `None` |
| ### `exclude` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery\(exclude\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Query to exclude children in the node. | `None` |
| ### `deep` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery\(deep\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Query should be deep, i.e. recursive. | `True` |
| ### `parent` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery\(parent\) "Permanent link") | ` \| None` | The parent query, if this is the result of filtering another query. | `None` |

Raises:

| Type | Description |
| --- | --- |
|  | If the format of the query is invalid. |

### node [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.node "Permanent link")

```
node
```

The node being queried.

### nodes [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.nodes "Permanent link")

```
nodes
```

Lazily evaluate nodes.

### add\_class [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.add_class "Permanent link")

```
add_class(*class_names)
```

Add the given class name(s) to nodes.

### blur [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.blur "Permanent link")

```
blur()
```

Blur the first matching node that is focused.

Returns:

| Type | Description |
| --- | --- |
| `[]` | Query for chaining. |

### exclude [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.exclude "Permanent link")

```
exclude()
```

Exclude nodes that match a given selector.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.exclude\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A CSS selector. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[]` | New DOM query. |

### filter [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.filter "Permanent link")

```
filter()
```

Filter this set by the given CSS selector.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.filter\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A CSS selector. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[]` | New DOM Query. |

### first [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.first "Permanent link")

```
first() ->
```
```
first(: type[]) ->
```

```
first(=None)
```

Get the *first* matching node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `expect_type` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.first\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[] \| None` | Require matched node is of this type, or None for any type. | `None` |

Raises:

| Type | Description |
| --- | --- |
|  | If the wrong type was found. |
|  | If there are no matching nodes in the query. |

Returns:

| Type | Description |
| --- | --- |
| `  \|  ` | The matching Widget. |

### focus [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.focus "Permanent link")

```
focus()
```

Focus the first matching node that permits focus.

Returns:

| Type | Description |
| --- | --- |
| `[]` | Query for chaining. |

### last [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.last "Permanent link")

```
last() ->
```
```
last(: type[]) ->
```

```
last(=None)
```

Get the *last* matching node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `expect_type` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.last\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[] \| None` | Require matched node is of this type, or None for any type. | `None` |

Raises:

| Type | Description |
| --- | --- |
|  | If the wrong type was found. |
|  | If there are no matching nodes in the query. |

Returns:

| Type | Description |
| --- | --- |
| `  \|  ` | The matching Widget. |

### only\_one [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.only_one "Permanent link")

```
only_one() ->
```
```
only_one(: type[]) ->
```

```
only_one(=None)
```

Get the *only* matching node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `expect_type` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.only_one\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[] \| None` | Require matched node is of this type, or None for any type. | `None` |

Raises:

| Type | Description |
| --- | --- |
|  | If the wrong type was found. |
|  | If no node matches the query. |
|  | If there is more than one matching node in the query. |

Returns:

| Type | Description |
| --- | --- |
| `  \|  ` | The matching Widget. |

### refresh [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.refresh "Permanent link")

```
refresh(*, =True, =False, =False)
```

Refresh matched nodes.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `repaint` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.refresh\(repaint\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Repaint node(s). | `True` |
| #### `layout` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.refresh\(layout\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Layout node(s). | `False` |
| #### `recompose` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.refresh\(recompose\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Recompose node(s). | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[]` | Query for chaining. |

### remove [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.remove "Permanent link")

```
remove()
```

Remove matched nodes from the DOM.

Returns:

| Type | Description |
| --- | --- |
| `[AwaitRemove](https://textual.textualize.io/api/await_remove/#textual.await_remove.AwaitRemove " AwaitRemove (textual.await_remove.AwaitRemove)")` | An awaitable object that waits for the widgets to be removed. |

### remove\_class [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.remove_class "Permanent link")

```
remove_class(*class_names)
```

Remove the given class names from the nodes.

### results [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.results "Permanent link")

```
results() -> Iterator[]
```
```
results(
    : type[],
) -> Iterator[]
```

```
results(=None)
```

Get query results, optionally filtered by a given type.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `filter_type` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.results\(filter_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[] \| None` | A Widget class to filter results, or None for no filter. | `None` |

Yields:

| Type | Description |
| --- | --- |
| `  \|  ` | Iterator\[Widget \| ExpectType\]: An iterator of Widget instances. |

### set [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set "Permanent link")

```
set(
    =None, =None, =None, =None
)
```

Sets common attributes on matched nodes.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `display` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set\(display\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Set `display` attribute on nodes, or `None` for no change. | `None` |
| #### `visible` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set\(visible\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Set `visible` attribute on nodes, or `None` for no change. | `None` |
| #### `disabled` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Set `disabled` attribute on nodes, or `None` for no change. | `None` |
|  | `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | Set `loading` attribute on nodes, or `None` for no change. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[]` | Query for chaining. |

### set\_class [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set_class "Permanent link")

```
set_class(, *class_names)
```

Set the given class name(s) according to a condition.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `add` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set_class\(add\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Add the classes if True, otherwise remove them. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[]` | Self. |

### set\_classes [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set_classes "Permanent link")

```
set_classes()
```

Set the classes on nodes to exactly the given set.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `classes` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set_classes\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[str](https://docs.python.org/3/library/stdtypes.html#str)]` | A string of space separated classes, or an iterable of class names. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[]` | Self. |

### set\_styles [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set_styles "Permanent link")

```
set_styles(=None, **update_styles)
```

Set styles on matched nodes.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `css` [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set_styles\(css\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | CSS declarations to parser, or None. | `None` |

### toggle\_class [¶](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.toggle_class "Permanent link")

```
toggle_class(*class_names)
```

Toggle the given class names from matched nodes.

## InvalidQueryFormat [¶](https://textual.textualize.io/api/query/#textual.css.query.InvalidQueryFormat "Permanent link")

Bases:

Query did not parse correctly.

## NoMatches [¶](https://textual.textualize.io/api/query/#textual.css.query.NoMatches "Permanent link")

Bases:

No nodes matched the query.

## QueryError [¶](https://textual.textualize.io/api/query/#textual.css.query.QueryError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Base class for a query related error.

## TooManyMatches [¶](https://textual.textualize.io/api/query/#textual.css.query.TooManyMatches "Permanent link")

Bases:

Too many nodes matched the query.

## WrongType [¶](https://textual.textualize.io/api/query/#textual.css.query.WrongType "Permanent link")

Bases:

Query result was not of the correct type.