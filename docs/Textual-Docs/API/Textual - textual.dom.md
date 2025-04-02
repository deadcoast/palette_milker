---
title: "Textual - textual.dom"
source: "https://textual.textualize.io/api/dom_node/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.dom

The module contains `DOMNode`, the base class for any object within the Textual Document Object Model, which includes all Widgets, Screens, and Apps.

## QueryOneCacheKey [¶](https://textual.textualize.io/api/dom_node/#textual.dom.QueryOneCacheKey "Permanent link")

```
QueryOneCacheKey = 'tuple[int, str, Type[Widget] | None]'
```

The key used to cache query\_one results.

## WalkMethod [¶](https://textual.textualize.io/api/dom_node/#textual.dom.WalkMethod "Permanent link")

```
WalkMethod = Literal['depth', 'breadth']
```

Valid walking methods for the .

## BadIdentifier [¶](https://textual.textualize.io/api/dom_node/#textual.dom.BadIdentifier "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Exception raised if you supply a `id` attribute or class name in the wrong format.

## DOMError [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Base exception class for errors relating to the DOM.

## DOMNode [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode "Permanent link")

```
DOMNode(*, name=None, id=None, classes=None)
```

Bases: `[MessagePump](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump " MessagePump (textual.message_pump.MessagePump)")`

The base class for object that can be in the Textual DOM (App and Widget)

### BINDINGS [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.BINDINGS "Permanent link")

```
BINDINGS = []
```

A list of key bindings.

### BINDING\_GROUP\_TITLE [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.BINDING_GROUP_TITLE "Permanent link")

```
BINDING_GROUP_TITLE = None
```

Title of widget used where bindings are displayed (such as in the key panel).

### COMPONENT\_CLASSES [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = set()
```

Virtual DOM nodes, used to expose styles to line API widgets.

### DEFAULT\_CLASSES [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.DEFAULT_CLASSES "Permanent link")

```
DEFAULT_CLASSES = ''
```

Default classes argument if not supplied.

### DEFAULT\_CSS [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.DEFAULT_CSS "Permanent link")

```
DEFAULT_CSS = ''
```

Default TCSS.

### HELP [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.HELP "Permanent link")

```
HELP = None
```

Optional help text shown in help panel (Markdown format).

### SCOPED\_CSS [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.SCOPED_CSS "Permanent link")

```
SCOPED_CSS = True
```

Should default css be limited to the widget type?

### ancestors [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.ancestors "Permanent link")

```
ancestors
```

A list of ancestor nodes found by tracing a path all the way back to App.

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of nodes. |

### ancestors\_with\_self [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.ancestors_with_self "Permanent link")

```
ancestors_with_self
```

A list of ancestor nodes found by tracing a path all the way back to App.

Note

This is inclusive of `self`.

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of nodes. |

### auto\_refresh [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.auto_refresh "Permanent link")

```
auto_refresh
```

Number of seconds between automatic refresh, or `None` for no automatic refresh.

### background\_colors [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.background_colors "Permanent link")

```
background_colors
```

The background color and the color of the parent's background.

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)"), [Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)")]` | `(<background color>, <color>)` |

### children [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.children "Permanent link")

```
children
```

A view on to the children.

Returns:

| Type | Description |
| --- | --- |
| `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")['Widget']` | The node's children. |

### classes [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.classes "Permanent link")

```
classes = _ClassesDescriptor()
```

CSS class names for this node.

### colors [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.colors "Permanent link")

```
colors
```

The widget's background and foreground colors, and the parent's background and foreground colors.

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)"), [Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)"), [Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)"), [Color](https://textual.textualize.io/api/color/#textual.color.Color " Color (textual.color.Color)")]` | `(<parent background>, <parent color>, <background>, <color>)` |

### css\_identifier [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.css_identifier "Permanent link")

```
css_identifier
```

A CSS selector that identifies this DOM node.

### css\_identifier\_styled [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.css_identifier_styled "Permanent link")

```
css_identifier_styled
```

A syntax highlighted CSS identifier.

Returns:

| Type | Description |
| --- | --- |
| `[Text](https://rich.readthedocs.io/en/stable/reference/text.html#rich.text.Text "rich.text.Text")` | A Rich Text object. |

### css\_path\_nodes [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.css_path_nodes "Permanent link")

```
css_path_nodes
```

A list of nodes from the App to this node, forming a "path".

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of nodes, where the first item is the App, and the last is this node. |

### css\_tree [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.css_tree "Permanent link")

```
css_tree
```

A Rich tree to display the DOM, annotated with the node's CSS.

Log this to visualize your app in the textual console.

Example
```
self.log(self.css_tree)
```

Returns:

| Type | Description |
| --- | --- |
| `[Tree](https://rich.readthedocs.io/en/stable/reference/tree.html#rich.tree.Tree "rich.tree.Tree")` | A Tree renderable. |

### display [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.display "Permanent link")

```
display
```

Should the DOM node be displayed?

May be set to a boolean to show or hide the node, or to any valid value for the `display` rule.

Example
```
my_widget.display = False  # Hide my_widget
```

### displayed\_children [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.displayed_children "Permanent link")

```
displayed_children
```

The child nodes which will be displayed.

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")]` | A list of nodes. |

### id [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.id "Permanent link")

```
id
```

The ID of this node, or None if the node has no ID.

```
is_modal
```

Is the node a modal?

### is\_on\_screen [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.is_on_screen "Permanent link")

```
is_on_screen
```

Check if the node was displayed in the last screen update.

### name [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.name "Permanent link")

```
name
```

The name of the node.

### parent [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.parent "Permanent link")

```
parent
```

The parent node.

All nodes have parent once added to the DOM, with the exception of the App which is the *root* node.

### pseudo\_classes [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.pseudo_classes "Permanent link")

```
pseudo_classes
```

A (frozen) set of all pseudo classes.

### rich\_style [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.rich_style "Permanent link")

```
rich_style
```

Get a Rich Style object for this DOMNode.

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | A Rich style. |

### screen [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.screen "Permanent link")

```
screen
```

The screen containing this node.

Returns:

| Type | Description |
| --- | --- |
| `'Screen[object]'` | A screen object. |

Raises:

| Type | Description |
| --- | --- |
|  | If this node isn't mounted (and has no screen). |

### selection\_style [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.selection_style "Permanent link")

```
selection_style
```

The style of selected text.

### text\_style [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.text_style "Permanent link")

```
text_style
```

Get the text style object.

A widget's style is influenced by its parent. for instance if a parent is bold, then the child will also be bold.

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style")` | A Rich Style. |

### tree [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.tree "Permanent link")

```
tree
```

A Rich tree to display the DOM.

Log this to visualize your app in the textual console.

Example
```
self.log(self.tree)
```

Returns:

| Type | Description |
| --- | --- |
| `[Tree](https://rich.readthedocs.io/en/stable/reference/tree.html#rich.tree.Tree "rich.tree.Tree")` | A Tree renderable. |

### visible [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.visible "Permanent link")

```
visible
```

Is this widget visible in the DOM?

If a widget hasn't had its visibility set explicitly, then it inherits it from its DOM ancestors.

This may be set explicitly to override inherited values. The valid values include the valid values for the `visibility` rule and the booleans `True` or `False`, to set the widget to be visible or invisible, respectively.

When a node is invisible, Textual will reserve space for it, but won't display anything.

### workers [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.workers "Permanent link")

```
workers
```

The app's worker manager. Shortcut for `self.app.workers`.

### action\_toggle [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.action_toggle "Permanent link")

```
action_toggle()
```

Toggle an attribute on the node.

Assumes the attribute is a bool.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `attribute_name` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.action_toggle\(attribute_name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of the attribute. | *required* |

### add\_class [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.add_class "Permanent link")

```
add_class(*, =True)
```

Add class names to this Node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*class_names` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.add_class\(*class_names\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | CSS class names to add. | `()` |
| #### `update` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.add_class\(update\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Also update styles. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | Self. |

### automatic\_refresh [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.automatic_refresh "Permanent link")

```
automatic_refresh()
```

Perform an automatic refresh.

This method is called when you set the `auto_refresh` attribute. You could implement this method if you want to perform additional work during an automatic refresh.

### check\_action [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.check_action "Permanent link")

```
check_action(, )
```

Check whether an action is enabled.

Implement this method to add logic for [dynamic actions](https://textual.textualize.io/guide/actions#dynamic-actions) / bindings.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `action` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.check_action\(action\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The name of an action. | *required* |
| #### `parameters` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.check_action\(parameters\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[object](https://docs.python.org/3/library/functions.html#object), ...]` | A tuple of any action parameters. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool) \| None` | `True` if the action is enabled+visible, `False` if the action is disabled+hidden, `None` if the action is disabled+visible (grayed out in footer) |

### check\_consume\_key [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.check_consume_key "Permanent link")

```
check_consume_key(, )
```

Check if the widget may consume the given key.

This should be implemented in widgets that handle [`Key`](https://textual.textualize.io/api/events/#textual.events.Key " Key") events and stop propagation (such as Input and TextArea).

Implementing this method will hide key bindings from the footer and key panel that would be *consumed* by the focused widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.check_consume_key\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A key identifier. | *required* |
| #### `character` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.check_consume_key\(character\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A character associated with the key, or `None` if there isn't one. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the widget may capture the key in its `Key` event handler, or `False` if it won't. |

### data\_bind [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.data_bind "Permanent link")

```
data_bind(*reactives, **bind_vars)
```

Bind reactive data so that changes to a reactive automatically change the reactive on another widget.

Reactives may be given as positional arguments or keyword arguments. See the [guide on data binding](https://textual.textualize.io/guide/reactivity#data-binding).

Example
```
def compose(self) -> ComposeResult:
    yield WorldClock("Europe/London").data_bind(WorldClockApp.time)
    yield WorldClock("Europe/Paris").data_bind(WorldClockApp.time)
    yield WorldClock("Asia/Tokyo").data_bind(WorldClockApp.time)
```

Raises:

| Type | Description |
| --- | --- |
| `[ReactiveError](https://textual.textualize.io/api/reactive/#textual.reactive.ReactiveError " ReactiveError (textual.reactive.ReactiveError)")` | If the data wasn't bound. |

Returns:

| Type | Description |
| --- | --- |
| `Self` | Self. |

### get\_component\_styles [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.get_component_styles "Permanent link")

```
get_component_styles(*names)
```

Get a "component" styles object (must be defined in COMPONENT\_CLASSES classvar).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `names` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.get_component_styles\(names\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Names of the components. | `()` |

Raises:

| Type | Description |
| --- | --- |
| `[KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)` | If the component class doesn't exist. |

Returns:

| Type | Description |
| --- | --- |
| `[RenderStyles](https://textual.textualize.io/api/types/#textual.types.RenderStyles " RenderStyles (textual.css.styles.RenderStyles)")` | A Styles object. |

### get\_pseudo\_classes [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.get_pseudo_classes "Permanent link")

```
get_pseudo_classes()
```

Pseudo classes for a widget.

Returns:

| Type | Description |
| --- | --- |
| `[set](https://docs.python.org/3/library/stdtypes.html#set)[[str](https://docs.python.org/3/library/stdtypes.html#str)]` | Names of the pseudo classes. |

### has\_class [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.has_class "Permanent link")

```
has_class(*)
```

Check if the Node has all the given class names.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*class_names` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.has_class\(*class_names\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | CSS class names to check. | `()` |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the node has all the given class names, otherwise `False`. |

### has\_pseudo\_class [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.has_pseudo_class "Permanent link")

```
has_pseudo_class()
```

Check the node has the given pseudo class.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `class_name` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.has_pseudo_class\(class_name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The pseudo class to check for. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the DOM node has the pseudo class, `False` if not. |

### has\_pseudo\_classes [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.has_pseudo_classes "Permanent link")

```
has_pseudo_classes()
```

Check the node has all the given pseudo classes.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `class_names` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.has_pseudo_classes\(class_names\) "Permanent link") | `[set](https://docs.python.org/3/library/stdtypes.html#set)[[str](https://docs.python.org/3/library/stdtypes.html#str)]` | Set of class names to check for. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if all pseudo class names are present. |

### mutate\_reactive [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.mutate_reactive "Permanent link")

```
mutate_reactive()
```

Force an update to a mutable reactive.

Example
```
self.reactive_name_list.append("Jessica")
self.mutate_reactive(MyClass.reactive_name_list)
```

Textual will automatically detect when a reactive is set to a new value, but it is unable to detect if a value is *mutated* (such as updating a list, dict, or attribute of an object). If you do wish to use a collection or other mutable object in a reactive, then you can call this method after your reactive is updated. This will ensure that all the reactive *superpowers* work.

Note

This method will cause watchers to be called, even if the value hasn't changed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `reactive` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.mutate_reactive\(reactive\) "Permanent link") | `[Reactive](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive " Reactive (textual.reactive.Reactive)")[ReactiveType]` | A reactive property (use the class scope syntax, i.e. `MyClass.my_reactive`). | *required* |

### notify\_style\_update [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.notify_style_update "Permanent link")

```
notify_style_update()
```

Called after styles are updated.

Implement this in a subclass if you want to clear any cached data when the CSS is reloaded.

### query [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query "Permanent link")

```
query(: str | None = None) -> DOMQuery[Widget]
```
```
query(: type[QueryType]) -> DOMQuery[QueryType]
```

```
query(=None)
```

Query the DOM for children that match a selector or widget type.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")] \| None` | A CSS selector, widget type, or `None` for all nodes. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[DOMQuery](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery " DOMQuery (textual.css.query.DOMQuery)")[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")] \| [DOMQuery](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery " DOMQuery (textual.css.query.DOMQuery)")[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")]` | A query object. |

### query\_ancestor [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_ancestor "Permanent link")

```
query_ancestor(: str) ->
```
```
query_ancestor(: type[QueryType]) -> QueryType
```
```
query_ancestor(
    : str, : type[QueryType]
) -> QueryType
```

```
query_ancestor(, =None)
```

Get an ancestor which matches a query.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_ancestor\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")]` | A TCSS selector. | *required* |
| #### `expect_type` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_ancestor\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")] \| None` | Expected type, or `None` for any DOMNode. | `None` |

Raises:

| Type | Description |
| --- | --- |
| `[InvalidQueryFormat](https://textual.textualize.io/api/query/#textual.css.query.InvalidQueryFormat " InvalidQueryFormat (textual.css.query.InvalidQueryFormat)")` | If the selector is invalid. |
| `[NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches (textual.css.query.NoMatches)")` | If there are no matching ancestors. |

Returns:

| Type | Description |
| --- | --- |
| ` \| None` | A DOMNode or subclass if `expect_type` is provided. |

### query\_children [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_children "Permanent link")

```
query_children(
    : str | None = None,
) -> DOMQuery[Widget]
```
```
query_children(
    : type[QueryType],
) -> DOMQuery[QueryType]
```

```
query_children(=None)
```

Query the DOM for the immediate children that match a selector or widget type.

Note that this will not return child widgets more than a single level deep. If you want to a query to potentially match all children in the widget tree, see .

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_children\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")] \| None` | A CSS selector, widget type, or `None` for all nodes. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[DOMQuery](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery " DOMQuery (textual.css.query.DOMQuery)")[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")] \| [DOMQuery](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery " DOMQuery (textual.css.query.DOMQuery)")[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")]` | A query object. |

### query\_exactly\_one [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_exactly_one "Permanent link")

```
query_exactly_one(: str) -> Widget
```
```
query_exactly_one(: type[QueryType]) -> QueryType
```
```
query_exactly_one(
    : str, : type[QueryType]
) -> QueryType
```

```
query_exactly_one(, =None)
```

Get a widget from this widget's children that matches a selector or widget type.

Note

This method is similar to . The only difference is that it will raise `TooManyMatches` if there is more than a single match.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_exactly_one\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")]` | A selector or widget type. | *required* |
| #### `expect_type` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_exactly_one\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")] \| None` | Require the object be of the supplied type, or None for any type. | `None` |

Raises:

| Type | Description |
| --- | --- |
| `[WrongType](https://textual.textualize.io/api/query/#textual.css.query.WrongType " WrongType (textual.css.query.WrongType)")` | If the wrong type was found. |
| `[NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches (textual.css.query.NoMatches)")` | If no node matches the query. |
| `[TooManyMatches](https://textual.textualize.io/api/query/#textual.css.query.TooManyMatches " TooManyMatches (textual.css.query.TooManyMatches)")` | If there is more than one matching node in the query (and `exactly_one==True`). |

Returns:

| Type | Description |
| --- | --- |
| `[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)") \| [Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A widget matching the selector. |

### query\_one [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_one "Permanent link")

```
query_one(: str) -> Widget
```
```
query_one(: type[QueryType]) -> QueryType
```
```
query_one(
    : str, : type[QueryType]
) -> QueryType
```

```
query_one(, =None)
```

Get a widget from this widget's children that matches a selector or widget type.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_one\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")]` | A selector or widget type. | *required* |
| #### `expect_type` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_one\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)")] \| None` | Require the object be of the supplied type, or None for any type. | `None` |

Raises:

| Type | Description |
| --- | --- |
| `[WrongType](https://textual.textualize.io/api/query/#textual.css.query.WrongType " WrongType (textual.css.query.WrongType)")` | If the wrong type was found. |
| `[NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches (textual.css.query.NoMatches)")` | If no node matches the query. |

Returns:

| Type | Description |
| --- | --- |
| `[QueryType](https://textual.textualize.io/api/query/#textual.css.query.QueryType " QueryType (textual.css.query.QueryType)") \| [Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A widget matching the selector. |

### refresh\_bindings [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.refresh_bindings "Permanent link")

```
refresh_bindings()
```

Call to prompt widgets such as the [Footer](https://textual.textualize.io/widgets/footer/#textual.widgets.Footer " Footer") to update the display of key bindings.

See [actions](https://textual.textualize.io/guide/actions#dynamic-actions) for how to use this method.

### remove\_class [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.remove_class "Permanent link")

```
remove_class(*, =True)
```

Remove class names from this Node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*class_names` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.remove_class\(*class_names\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | CSS class names to remove. | `()` |
| #### `update` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.remove_class\(update\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Also update styles. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | Self. |

### reset\_styles [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.reset_styles "Permanent link")

```
reset_styles()
```

Reset styles back to their initial state.

### run\_worker [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.run_worker "Permanent link")

```
run_worker(
    ,
    ="",
    ="default",
    ="",
    =True,
    =True,
    =False,
    =False,
)
```

Run work in a worker.

A worker runs a function, coroutine, or awaitable, in the *background* as an async task or as a thread.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `work` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.run_worker\(work\) "Permanent link") | `[WorkType](https://textual.textualize.io/api/worker/#textual.worker.WorkType " WorkType (textual.worker.WorkType)")[ResultType]` | A function, async function, or an awaitable object to run in a worker. | *required* |
| #### `name` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.run_worker\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A short string to identify the worker (in logs and debugging). | `''` |
| #### `group` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.run_worker\(group\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A short string to identify a group of workers. | `'default'` |
| #### `description` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.run_worker\(description\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A longer string to store longer information on the worker. | `''` |
| #### `exit_on_error` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.run_worker\(exit_on_error\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Exit the app if the worker raises an error. Set to `False` to suppress exceptions. | `True` |
| #### `start` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.run_worker\(start\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Start the worker immediately. | `True` |
| #### `exclusive` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.run_worker\(exclusive\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Cancel all workers in the same group. | `False` |
| #### `thread` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.run_worker\(thread\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Mark the worker as a thread worker. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[Worker](https://textual.textualize.io/api/worker/#textual.worker.Worker " Worker (textual.worker.Worker)")[ResultType]` | New Worker instance. |

### set\_class [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_class "Permanent link")

```
set_class(, *class_names, =True)
```

Add or remove class(es) based on a condition.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `add` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_class\(add\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Add the classes if True, otherwise remove them. | *required* |
| #### `update` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_class\(update\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Also update styles. | `True` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | Self. |

### set\_classes [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_classes "Permanent link")

```
set_classes()
```

Replace all classes.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `classes` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_classes\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[str](https://docs.python.org/3/library/stdtypes.html#str)]` | A string containing space separated classes, or an iterable of class names. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Self` | Self. |

### set\_reactive [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_reactive "Permanent link")

```
set_reactive(, )
```

Sets a reactive value *without* invoking validators or watchers.

Example
```
self.set_reactive(App.theme, "textual-light")
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `reactive` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_reactive\(reactive\) "Permanent link") | `[Reactive](https://textual.textualize.io/api/reactive/#textual.reactive.Reactive " Reactive (textual.reactive.Reactive)")[ReactiveType]` | A reactive property (use the class scope syntax, i.e. `MyClass.my_reactive`). | *required* |
| #### `value` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_reactive\(value\) "Permanent link") | `ReactiveType` | New value of reactive. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[AttributeError](https://docs.python.org/3/library/exceptions.html#AttributeError)` | If the first argument is not a reactive. |

### set\_styles [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_styles "Permanent link")

```
set_styles(=None, **update_styles)
```

Set custom styles on this object.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `css` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_styles\(css\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Styles in CSS format. | `None` |
| #### `update_styles` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.set_styles\(update_styles\) "Permanent link") | `[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | Keyword arguments map style names onto style values. | `{}` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | Self. |

### sort\_children [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.sort_children "Permanent link")

```
sort_children(*, =None, =False)
```

Sort child widgets with an optional key function.

If `key` is not provided then widgets will be sorted in the order they are constructed.

Example
```
# Sort widgets by name
screen.sort_children(key=lambda widget: widget.name or "")
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.sort_children\(key\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")], SupportsRichComparison] \| None` | A callable which accepts a widget and returns something that can be sorted, or `None` to sort without a key function. | `None` |
| #### `reverse` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.sort_children\(reverse\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Sort in descending order. | `False` |

### toggle\_class [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.toggle_class "Permanent link")

```
toggle_class(*)
```

Toggle class names on this Node.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*class_names` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.toggle_class\(*class_names\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | CSS class names to toggle. | `()` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | Self. |

### walk\_children [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.walk_children "Permanent link")

```
walk_children(
    : type[WalkType],
    *,
    : bool = False,
    :  = "depth",
    : bool = False
) -> list[WalkType]
```
```
walk_children(
    *,
    : bool = False,
    :  = "depth",
    : bool = False
) -> list[]
```

```
walk_children(
    =None,
    *,
    =False,
    ="depth",
    =False
)
```

Walk the subtree rooted at this node, and return every descendant encountered in a list.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `filter_type` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.walk_children\(filter_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[WalkType] \| None` | Filter only this type, or None for no filter. | `None` |
| #### `with_self` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.walk_children\(with_self\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Also yield self in addition to descendants. | `False` |
| #### `method` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.walk_children\(method\) "Permanent link") |  | One of "depth" or "breadth". | `'depth'` |
| #### `reverse` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.walk_children\(reverse\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Reverse the order (bottom up). | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[] \| [list](https://docs.python.org/3/library/stdtypes.html#list)[WalkType]` | A list of nodes. |

### watch [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.watch "Permanent link")

```
watch(, , , =True)
```

Watches for modifications to reactive attributes on another object.

Example
```
def on_theme_change(old_value:str, new_value:str) -> None:
    # Called when app.theme changes.
    print(f"App.theme went from {old_value} to {new_value}")

self.watch(self.app, "theme", self.on_theme_change, init=False)
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `obj` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.watch\(obj\) "Permanent link") |  | Object containing attribute to watch. | *required* |
| #### `attribute_name` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.watch\(attribute_name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Attribute to watch. | *required* |
| #### `callback` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.watch\(callback\) "Permanent link") | `[WatchCallbackType](https://textual.textualize.io/api/types/#textual.types.WatchCallbackType " WatchCallbackType (textual._types.WatchCallbackType)")` | A callback to run when attribute changes. | *required* |
| #### `init` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.watch\(init\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Check watchers on first call. | `True` |

## NoScreen [¶](https://textual.textualize.io/api/dom_node/#textual.dom.NoScreen "Permanent link")

Bases:

Raised when the node has no associated screen.

## check\_identifiers [¶](https://textual.textualize.io/api/dom_node/#textual.dom.check_identifiers "Permanent link")

```
check_identifiers(, *)
```

Validate identifier and raise an error if it fails.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `description` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.check_identifiers\(description\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Description of where identifier is used for error message. | *required* |
| ### `*names` [¶](https://textual.textualize.io/api/dom_node/#textual.dom.check_identifiers\(*names\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Identifiers to check. | `()` |