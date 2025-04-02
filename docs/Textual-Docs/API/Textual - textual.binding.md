---
title: "Textual - textual.binding"
source: "https://textual.textualize.io/api/binding/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.binding

This module contains the `Binding` class and related objects.

See [bindings](https://textual.textualize.io/guide/input#bindings) in the guide for details.

## BindingIDString [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingIDString "Permanent link")

```
BindingIDString = str
```

The ID of a Binding defined somewhere in the application.

Corresponds to the `id` parameter of the `Binding` class.

## BindingType [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingType "Permanent link")

```
BindingType = (
    "Binding | tuple[str, str] | tuple[str, str, str]"
)
```

The possible types of a binding found in the `BINDINGS` class variable.

## KeyString [¶](https://textual.textualize.io/api/binding/#textual.binding.KeyString "Permanent link")

```
KeyString = str
```

A string that represents a key binding.

For example, "x", "ctrl+i", "ctrl+shift+a", "ctrl+j,space,x", etc.

## Keymap [¶](https://textual.textualize.io/api/binding/#textual.binding.Keymap "Permanent link")

```
Keymap = Mapping[, ]
```

A mapping of binding IDs to key strings, used for overriding default key bindings.

## ActiveBinding [¶](https://textual.textualize.io/api/binding/#textual.binding.ActiveBinding "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

Information about an active binding (returned from [active\_bindings](https://textual.textualize.io/api/screen/#textual.screen.Screen.active_bindings " active_bindings")).

### binding [¶](https://textual.textualize.io/api/binding/#textual.binding.ActiveBinding.binding "Permanent link")

```
binding
```

The binding information.

### enabled [¶](https://textual.textualize.io/api/binding/#textual.binding.ActiveBinding.enabled "Permanent link")

```
enabled
```

Is the binding enabled? (enabled bindings are typically rendered dim)

### node [¶](https://textual.textualize.io/api/binding/#textual.binding.ActiveBinding.node "Permanent link")

```
node
```

The node where the binding is defined.

```
tooltip = ''
```

Optional tooltip shown in Footer.

## Binding [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding "Permanent link")

```
Binding(
    key,
    action,
    description="",
    show=True,
    key_display=None,
    priority=False,
    tooltip="",
    id=None,
    system=False,
)
```

The configuration of a key binding.

### action [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.action "Permanent link")

```
action
```

Action to bind to.

### description [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.description "Permanent link")

```
description = ''
```

Description of action.

### id [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.id "Permanent link")

```
id = None
```

ID of the binding. Intended to be globally unique, but uniqueness is not enforced.

If specified in the App's keymap then Textual will use this ID to lookup the binding, and substitute the `key` property of the Binding with the key specified in the keymap.

### key [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.key "Permanent link")

```
key
```

Key to bind. This can also be a comma-separated list of keys to map multiple keys to a single action.

### key\_display [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.key_display "Permanent link")

```
key_display = None
```

How the key should be shown in footer.

If None, the display of the key will use the result of `App.get_key_display`.

If overridden in a keymap then this value is ignored.

### priority [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.priority "Permanent link")

```
priority = False
```

Enable priority binding for this key.

### show [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.show "Permanent link")

```
show = True
```

Show the action in Footer, or False to hide.

### system [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.system "Permanent link")

```
system = False
```

Make this binding a system binding, which removes it from the key panel.

```
tooltip = ''
```

Optional tooltip to show in footer.

### make\_bindings [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.make_bindings "Permanent link")

```
make_bindings()
```

Convert a list of BindingType (the types that can be specified in BINDINGS) into an Iterable\[Binding\].

Compound bindings like "j,down" will be expanded into 2 Binding instances.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `bindings` [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.make_bindings\(bindings\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | An iterable of BindingType. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | An iterable of Binding. |

### parse\_key [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.parse_key "Permanent link")

```
parse_key()
```

Parse a key into a list of modifiers, and the actual key.

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)], [str](https://docs.python.org/3/library/stdtypes.html#str)]` | A tuple of (MODIFIER LIST, KEY). |

### with\_key [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.with_key "Permanent link")

```
with_key(, =None)
```

Return a new binding with the key and key\_display set to the specified values.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.with_key\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The new key to set. | *required* |
| #### `key_display` [¶](https://textual.textualize.io/api/binding/#textual.binding.Binding.with_key\(key_display\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The new key display to set. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | A new binding with the key set to the specified value. |

## BindingError [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

A binding related error.

## BindingsMap [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap "Permanent link")

```
BindingsMap(=None)
```

Manage a set of bindings.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `bindings` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap\(bindings\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[] \| None` | An optional set of initial bindings. | `None` |

Note

The iterable of bindings can contain either a `Binding` instance, or a tuple of 3 values mapping to the first three properties of a `Binding`.

### key\_to\_bindings [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.key_to_bindings "Permanent link")

```
key_to_bindings = {}
```

Mapping of key (e.g. "ctrl+a") to list of bindings for that key.

### shown\_keys [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.shown_keys "Permanent link")

```
shown_keys
```

A list of bindings for shown keys.

### apply\_keymap [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.apply_keymap "Permanent link")

```
apply_keymap()
```

Replace bindings for keys that are present in `keymap`.

Preserves existing bindings for keys that are not in `keymap`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `keymap` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.apply_keymap\(keymap\) "Permanent link") |  | A keymap to overlay. | *required* |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `KeymapApplyResult` |  | The result of applying the keymap, including any clashed bindings. |

### bind [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.bind "Permanent link")

```
bind(
    ,
    ,
    ="",
    =True,
    =None,
    =False,
)
```

Bind keys to an action.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `keys` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.bind\(keys\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The keys to bind. Can be a comma-separated list of keys. | *required* |
| #### `action` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.bind\(action\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The action to bind the keys to. | *required* |
| #### `description` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.bind\(description\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | An optional description for the binding. | `''` |
| #### `show` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.bind\(show\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | A flag to say if the binding should appear in the footer. | `True` |
| #### `key_display` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.bind\(key_display\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional string to display in the footer for the key. | `None` |
| #### `priority` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.bind\(priority\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Is this a priority binding, checked form app down to focused widget? | `False` |

### copy [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.copy "Permanent link")

```
copy()
```

Return a copy of this instance.

Return

New bindings object.

### from\_keys [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.from_keys "Permanent link")

```
from_keys()
```

Construct a BindingsMap from a dict of keys and bindings.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `keys` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.from_keys\(keys\) "Permanent link") | `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [list](https://docs.python.org/3/library/stdtypes.html#list)[]]` | A dict that maps a key on to a list of `Binding` objects. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New `BindingsMap` |

### get\_bindings\_for\_key [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.get_bindings_for_key "Permanent link")

```
get_bindings_for_key()
```

Get a list of bindings for a given key.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.get_bindings_for_key\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Key to look up. | *required* |

Raises:

| Type | Description |
| --- | --- |
|  | If the binding does not exist. |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of bindings associated with the key. |

### merge [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.merge "Permanent link")

```
merge()
```

Merge a bindings.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `bindings` [¶](https://textual.textualize.io/api/binding/#textual.binding.BindingsMap.merge\(bindings\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | A number of bindings. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | New `BindingsMap`. |

## InvalidBinding [¶](https://textual.textualize.io/api/binding/#textual.binding.InvalidBinding "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Binding key is in an invalid format.

## KeymapApplyResult [¶](https://textual.textualize.io/api/binding/#textual.binding.KeymapApplyResult "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

The result of applying a keymap.

### clashed\_bindings [¶](https://textual.textualize.io/api/binding/#textual.binding.KeymapApplyResult.clashed_bindings "Permanent link")

```
clashed_bindings
```

A list of bindings that were clashed and replaced by the keymap.

## NoBinding [¶](https://textual.textualize.io/api/binding/#textual.binding.NoBinding "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

A binding was not found.