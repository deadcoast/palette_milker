---
title: "Textual - textual.suggester"
source: "https://textual.textualize.io/api/suggester/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.suggester

Contains the `Suggester` class, used by the [Input](https://textual.textualize.io/widgets/input) widget.

## SuggestFromList [¶](https://textual.textualize.io/api/suggester/#textual.suggester.SuggestFromList "Permanent link")

```
SuggestFromList(, *, =True)
```

Bases:

Give completion suggestions based on a fixed list of options.

Example
```
countries = ["England", "Scotland", "Portugal", "Spain", "France"]

class MyApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(suggester=SuggestFromList(countries, case_sensitive=False))
```

If the user types P inside the input widget, a completion suggestion for `"Portugal"` appears.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `suggestions` [¶](https://textual.textualize.io/api/suggester/#textual.suggester.SuggestFromList\(suggestions\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[str](https://docs.python.org/3/library/stdtypes.html#str)]` | Valid suggestions sorted by decreasing priority. | *required* |
| ### `case_sensitive` [¶](https://textual.textualize.io/api/suggester/#textual.suggester.SuggestFromList\(case_sensitive\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether suggestions are computed in a case sensitive manner or not. The values provided in the argument `suggestions` represent the canonical representation of the completions and they will be suggested with that same casing. | `True` |

### get\_suggestion [¶](https://textual.textualize.io/api/suggester/#textual.suggester.SuggestFromList.get_suggestion "Permanent link")

```
get_suggestion()
```

Gets a completion from the given possibilities.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `value` [¶](https://textual.textualize.io/api/suggester/#textual.suggester.SuggestFromList.get_suggestion\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The current value. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A valid completion suggestion or `None`. |

## Suggester [¶](https://textual.textualize.io/api/suggester/#textual.suggester.Suggester "Permanent link")

```
Suggester(*, =True, =False)
```

Bases: `[ABC](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")`

Defines how widgets generate completion suggestions.

To define a custom suggester, subclass `Suggester` and implement the async method `get_suggestion`. See for an example.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `use_cache` [¶](https://textual.textualize.io/api/suggester/#textual.suggester.Suggester\(use_cache\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to cache suggestion results. | `True` |
| ### `case_sensitive` [¶](https://textual.textualize.io/api/suggester/#textual.suggester.Suggester\(case_sensitive\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether suggestions are case sensitive or not. If they are not, incoming values are casefolded before generating the suggestion. | `False` |

### cache [¶](https://textual.textualize.io/api/suggester/#textual.suggester.Suggester.cache "Permanent link")

```
cache = LRUCache(1024) if  else None
```

Suggestion cache, if used.

### get\_suggestion [¶](https://textual.textualize.io/api/suggester/#textual.suggester.Suggester.get_suggestion "Permanent link")

```
get_suggestion()
```

Try to get a completion suggestion for the given input value.

Custom suggesters should implement this method.

Note

The value argument will be casefolded if `self.case_sensitive` is `False`.

Note

If your implementation is not deterministic, you may need to disable caching.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `value` [¶](https://textual.textualize.io/api/suggester/#textual.suggester.Suggester.get_suggestion\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The current value of the requester widget. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A valid suggestion or `None`. |

## SuggestionReady [¶](https://textual.textualize.io/api/suggester/#textual.suggester.SuggestionReady "Permanent link")

```
SuggestionReady(value, suggestion)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Sent when a completion suggestion is ready.

### suggestion [¶](https://textual.textualize.io/api/suggester/#textual.suggester.SuggestionReady.suggestion "Permanent link")

```
suggestion
```

The string suggestion.

### value [¶](https://textual.textualize.io/api/suggester/#textual.suggester.SuggestionReady.value "Permanent link")

```
value
```

The value to which the suggestion is for.