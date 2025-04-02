---
title: "Textual - textual.types"
source: "https://textual.textualize.io/api/types/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.types

Export some objects that are used by Textual and that help document other features.

## ActionParseResult [¶](https://textual.textualize.io/api/types/#textual.types.ActionParseResult "Permanent link")

```
ActionParseResult = 'tuple[str, str, tuple[object, ...]]'
```

An action is its name and the arbitrary tuple of its arguments.

## AnimationLevel [¶](https://textual.textualize.io/api/types/#textual.types.AnimationLevel "Permanent link")

```
AnimationLevel = Literal['none', 'basic', 'full']
```

The levels that the [`TEXTUAL_ANIMATIONS`](https://textual.textualize.io/api/constants/#textual.constants.TEXTUAL_ANIMATIONS " TEXTUAL_ANIMATIONS") env var can be set to.

## CSSPathType [¶](https://textual.textualize.io/api/types/#textual.types.CSSPathType "Permanent link")

```
CSSPathType = Union[
    str, PurePath, List[Union[str, PurePath]]
]
```

Valid ways of specifying paths to CSS files.

## CallbackType [¶](https://textual.textualize.io/api/types/#textual.types.CallbackType "Permanent link")

```
CallbackType = Union[
    Callable[[], Awaitable[None]], Callable[[], None]
]
```

Type used for arbitrary callables used in callbacks.

## Direction [¶](https://textual.textualize.io/api/types/#textual.types.Direction "Permanent link")

```
Direction = Literal[-1, 1]
```

Valid values to determine navigation direction.

In a vertical setting, 1 points down and -1 points up. In a horizontal setting, 1 points right and -1 points left.

## EasingFunction [¶](https://textual.textualize.io/api/types/#textual.types.EasingFunction "Permanent link")

```
EasingFunction = Callable[[float], float]
```

Signature for a function that parametrizes animation speed.

An easing function must map the interval \[0, 1\] into the interval \[0, 1\].

## IgnoreReturnCallbackType [¶](https://textual.textualize.io/api/types/#textual.types.IgnoreReturnCallbackType "Permanent link")

```
IgnoreReturnCallbackType = Union[
    Callable[[], Awaitable[Any]], Callable[[], Any]
]
```

A callback which ignores the return type.

## InputValidationOn [¶](https://textual.textualize.io/api/types/#textual.types.InputValidationOn "Permanent link")

```
InputValidationOn = Literal['blur', 'changed', 'submitted']
```

Possible messages that trigger input validation.

## OptionListContent [¶](https://textual.textualize.io/api/types/#textual.types.OptionListContent "Permanent link")

```
OptionListContent = 'Option | VisualType | None'
```

Types accepted in OptionList constructor and \[add\_options()\]\[textual.widgets.OptionList.ads\_options\].

## PlaceholderVariant [¶](https://textual.textualize.io/api/types/#textual.types.PlaceholderVariant "Permanent link")

```
PlaceholderVariant = Literal['default', 'size', 'text']
```

The different variants of placeholder.

## SelectType [¶](https://textual.textualize.io/api/types/#textual.types.SelectType "Permanent link")

```
SelectType = TypeVar('SelectType')
```

The type used for data in the Select.

## WatchCallbackType [¶](https://textual.textualize.io/api/types/#textual.types.WatchCallbackType "Permanent link")

```
WatchCallbackType = Union[
    WatchCallbackBothValuesType,
    WatchCallbackNewValueType,
    WatchCallbackNoArgsType,
]
```

Type used for callbacks passed to the `watch` method of widgets.

## Animatable [¶](https://textual.textualize.io/api/types/#textual.types.Animatable "Permanent link")

Bases: `Protocol`

Protocol for objects that can have their intrinsic values animated.

For example, the transition between two colors can be animated because the class [`Color`](https://textual.textualize.io/api/color/#textual.color.Color.blend " blend") satisfies this protocol.

## CSSPathError [¶](https://textual.textualize.io/api/types/#textual.types.CSSPathError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when supplied CSS path(s) are invalid.

## DirEntry [¶](https://textual.textualize.io/api/types/#textual.types.DirEntry "Permanent link")

```
DirEntry(path, loaded=False)
```

Attaches directory information to a [`DirectoryTree`](https://textual.textualize.io/widgets/directory_tree/#textual.widgets.DirectoryTree " DirectoryTree") node.

### loaded [¶](https://textual.textualize.io/api/types/#textual.types.DirEntry.loaded "Permanent link")

```
loaded = False
```

Has this been loaded?

### path [¶](https://textual.textualize.io/api/types/#textual.types.DirEntry.path "Permanent link")

```
path
```

The path of the directory entry.

## DuplicateID [¶](https://textual.textualize.io/api/types/#textual.types.DuplicateID "Permanent link")

Bases: `OptionListError`

Raised if a duplicate ID is used when adding options to an option list.

## MessageTarget [¶](https://textual.textualize.io/api/types/#textual.types.MessageTarget "Permanent link")

Bases: `Protocol`

Protocol that must be followed by objects that can receive messages.

## NoActiveAppError [¶](https://textual.textualize.io/api/types/#textual.types.NoActiveAppError "Permanent link")

Bases: `[RuntimeError](https://docs.python.org/3/library/exceptions.html#RuntimeError)`

Runtime error raised if we try to retrieve the active app when there is none.

## NoSelection [¶](https://textual.textualize.io/api/types/#textual.types.NoSelection "Permanent link")

Used by the `Select` widget to flag the unselected state. See [`Select.BLANK`](https://textual.textualize.io/widgets/select/#textual.widgets.Select.BLANK " BLANK").

## OptionDoesNotExist [¶](https://textual.textualize.io/api/types/#textual.types.OptionDoesNotExist "Permanent link")

Bases: `OptionListError`

Raised when a request has been made for an option that doesn't exist.

## RenderStyles [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles "Permanent link")

```
RenderStyles(node, base, inline_styles)
```

Bases: `StylesBase`

Presents a combined view of two Styles object: a base Styles and inline Styles.

### base [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.base "Permanent link")

```
base
```

Quick access to base (css) style.

### css [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.css "Permanent link")

```
css
```

Get the CSS for the combined styles.

### gutter [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.gutter "Permanent link")

```
gutter
```

Get space around widget.

Returns:

| Type | Description |
| --- | --- |
| `[Spacing](https://textual.textualize.io/api/geometry/#textual.geometry.Spacing " Spacing (textual.geometry.Spacing)")` | Space around widget content. |

### inline [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.inline "Permanent link")

```
inline
```

Quick access to the inline styles.

### rich\_style [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.rich_style "Permanent link")

```
rich_style
```

Get a Rich style for this Styles object.

### animate [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate "Permanent link")

```
animate(
    ,
    ,
    *,
    =...,
    =None,
    =None,
    =0.0,
    =DEFAULT_EASING,
    =None,
    ="full"
)
```

Animate an attribute.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `attribute` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate\(attribute\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of the attribute to animate. | *required* |
| #### `value` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [float](https://docs.python.org/3/library/functions.html#float) \| ` | The value to animate to. | *required* |
| #### `final_value` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate\(final_value\) "Permanent link") | `[object](https://docs.python.org/3/library/functions.html#object)` | The final value of the animation. Defaults to `value` if not set. | `...` |
| #### `duration` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The duration (in seconds) of the animation. | `None` |
| #### `speed` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The speed of the animation. | `None` |
| #### `delay` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate\(delay\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | A delay (in seconds) before the animation starts. | `0.0` |
| #### `easing` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate\(easing\) "Permanent link") | ` \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | An easing method. | `DEFAULT_EASING` |
| #### `on_complete` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate\(on_complete\) "Permanent link") | ` \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.animate\(level\) "Permanent link") |  | Minimum level required for the animation to take place (inclusive). | `'full'` |

### clear\_rule [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.clear_rule "Permanent link")

```
clear_rule(rule_name)
```

Clear a rule (from inline).

### get\_rules [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.get_rules "Permanent link")

```
get_rules()
```

Get rules as a dictionary

### has\_any\_rules [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.has_any_rules "Permanent link")

```
has_any_rules(*rule_names)
```

Check if any of the supplied rules have been set.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `rule_names` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.has_any_rules\(rule_names\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Number of rules. | `()` |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if any of the supplied rules have been set, `False` if none have. |

### has\_rule [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.has_rule "Permanent link")

```
has_rule(rule_name)
```

Check if a rule has been set.

### merge [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.merge "Permanent link")

```
merge()
```

Merge values from another Styles.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `other` [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.merge\(other\) "Permanent link") | `StylesBase` | A Styles object. | *required* |

### reset [¶](https://textual.textualize.io/api/types/#textual.types.RenderStyles.reset "Permanent link")

```
reset()
```

Reset the rules to initial state.

## UnusedParameter [¶](https://textual.textualize.io/api/types/#textual.types.UnusedParameter "Permanent link")

Helper type for a parameter that isn't specified in a method call.