---
title: "Textual - textual.command"
source: "https://textual.textualize.io/api/command/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.command

This module contains classes for working with Textual's command palette.

See the guide on the [Command Palette](https://textual.textualize.io/guide/command_palette/) for full details.

## Hits [¶](https://textual.textualize.io/api/command/#textual.command.Hits "Permanent link")

```
Hits = AsyncIterator['DiscoveryHit | Hit']
```

Return type for the command provider's `search` method.

## ProviderSource [¶](https://textual.textualize.io/api/command/#textual.command.ProviderSource "Permanent link")

```
ProviderSource = "Iterable[type[Provider] | Callable[[], type[Provider]]]"
```

The type used to declare the providers for a CommandPalette.

## Command [¶](https://textual.textualize.io/api/command/#textual.command.Command "Permanent link")

```
Command(, , =None, =False)
```

Bases: `[Option](https://textual.textualize.io/widgets/option_list/#textual.widgets.option_list.Option " Option (textual.widgets.option_list.Option)")`

Class that holds a hit in the .

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `prompt` [¶](https://textual.textualize.io/api/command/#textual.command.Command\(prompt\) "Permanent link") | `VisualType` | The prompt for the option. | *required* |
| ### `hit` [¶](https://textual.textualize.io/api/command/#textual.command.Command\(hit\) "Permanent link") | `  \|  ` | The details of the hit associated with the option. | *required* |
| ### `id` [¶](https://textual.textualize.io/api/command/#textual.command.Command\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The optional ID for the option. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/api/command/#textual.command.Command\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | The initial enabled/disabled state. Enabled by default. | `False` |

### hit [¶](https://textual.textualize.io/api/command/#textual.command.Command.hit "Permanent link")

```
hit =
```

The details of the hit associated with the option.

## CommandInput [¶](https://textual.textualize.io/api/command/#textual.command.CommandInput "Permanent link")

```
CommandInput(
    value=None,
    placeholder="",
    highlighter=None,
    password=False,
    *,
    restrict=None,
    type="text",
    max_length=0,
    suggester=None,
    validators=None,
    validate_on=None,
    valid_empty=False,
    select_on_focus=True,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    tooltip=None
)
```

Bases: `[Input](https://textual.textualize.io/widgets/input/#textual.widgets.Input " Input (textual.widgets.Input)")`

The command palette input control.

## CommandList [¶](https://textual.textualize.io/api/command/#textual.command.CommandList "Permanent link")

```
CommandList(
    *content,
    name=None,
    id=None,
    classes=None,
    disabled=False,
    markup=True
)
```

Bases: `[OptionList](https://textual.textualize.io/widgets/option_list/#textual.widgets.OptionList " OptionList (textual.widgets.OptionList)")`

The command palette command list.

## CommandPalette [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette "Permanent link")

```
CommandPalette(
    =None,
    *,
    ="Search for commands…",
    name=None,
    id=None,
    classes=None
)
```

Bases: `[SystemModalScreen](https://textual.textualize.io/api/screen/#textual.screen.SystemModalScreen " SystemModalScreen (textual.screen.SystemModalScreen)")[None]`

The Textual command palette.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `providers` [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette\(providers\) "Permanent link") | ` \| None` | An optional list of providers to use. If None, the providers supplied in the App or Screen will be used. | `None` |
| ### `placeholder` [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette\(placeholder\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The placeholder text for the command palette. | `'Search for commands…'` |

### BINDINGS [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding(
        "ctrl+end, shift+end",
        "command_list('last')",
        "Go to bottom",
        show=False,
    ),
    Binding(
        "ctrl+home, shift+home",
        "command_list('first')",
        "Go to top",
        show=False,
    ),
    Binding(
        "down", "cursor_down", "Next command", show=False
    ),
    Binding("escape", "escape", "Exit the command palette"),
    Binding(
        "pagedown",
        "command_list('page_down')",
        "Next page",
        show=False,
    ),
    Binding(
        "pageup",
        "command_list('page_up')",
        "Previous page",
        show=False,
    ),
    Binding(
        "up",
        "command_list('cursor_up')",
        "Previous command",
        show=False,
    ),
]
```

| Key(s) | Description |
| --- | --- |
| ctrl+end, shift+end | Jump to the last available commands. |
| ctrl+home, shift+home | Jump to the first available commands. |
| down | Navigate down through the available commands. |
| escape | Exit the command palette. |
| pagedown | Navigate down a page through the available commands. |
| pageup | Navigate up a page through the available commands. |
| up | Navigate up through the available commands. |

### COMPONENT\_CLASSES [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {
    "command-palette--help-text",
    "command-palette--highlight",
}
```

| Class | Description |
| --- | --- |
| `command-palette--help-text` | Targets the help text of a matched command. |
| `command-palette--highlight` | Targets the highlights of a matched command. |

### run\_on\_select [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.run_on_select "Permanent link")

```
run_on_select = True
```

A flag to say if a command should be run when selected by the user.

If `True` then when a user hits `Enter` on a command match in the result list, or if they click on one with the mouse, the command will be selected and run. If set to `False` the input will be filled with the command and then `Enter` should be pressed on the keyboard or the 'go' button should be pressed.

### Closed [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.Closed "Permanent link")

```
Closed(option_selected)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted to App when the command palette is closed.

#### option\_selected [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.Closed.option_selected "Permanent link")

```
option_selected
```

True if an option was selected, False if the palette was closed without selecting an option.

### Opened [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.Opened "Permanent link")

```
Opened()
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted to App when the command palette is opened.

### OptionHighlighted [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.OptionHighlighted "Permanent link")

```
OptionHighlighted(highlighted_event)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted to App when an option is highlighted in the command palette.

#### highlighted\_event [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.OptionHighlighted.highlighted_event "Permanent link")

```
highlighted_event
```

The option highlighted event from the OptionList within the command palette.

### is\_open [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.is_open "Permanent link")

```
is_open()
```

Is a command palette current open?

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `app` [¶](https://textual.textualize.io/api/command/#textual.command.CommandPalette.is_open\(app\) "Permanent link") | `[App](https://textual.textualize.io/api/app/#textual.app.App " App (textual.app.App)")[[object](https://docs.python.org/3/library/functions.html#object)]` | The app to test. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if a command palette is currently open, `False` if not. |

## DiscoveryHit [¶](https://textual.textualize.io/api/command/#textual.command.DiscoveryHit "Permanent link")

```
DiscoveryHit(display, command, text=None, help=None)
```

Holds the details of a single command search hit.

### command [¶](https://textual.textualize.io/api/command/#textual.command.DiscoveryHit.command "Permanent link")

```
command
```

The function to call when the command is chosen.

### display [¶](https://textual.textualize.io/api/command/#textual.command.DiscoveryHit.display "Permanent link")

```
display
```

A string or Rich renderable representation of the hit.

### help [¶](https://textual.textualize.io/api/command/#textual.command.DiscoveryHit.help "Permanent link")

```
help = None
```

Optional help text for the command.

### prompt [¶](https://textual.textualize.io/api/command/#textual.command.DiscoveryHit.prompt "Permanent link")

```
prompt
```

The prompt to use when displaying the discovery hit in the command palette.

### score [¶](https://textual.textualize.io/api/command/#textual.command.DiscoveryHit.score "Permanent link")

```
score
```

A discovery hit always has a score of 0.

The order in which discovery hits are displayed is determined by the order in which they are yielded by the Provider. It's up to the developer to yield DiscoveryHits in the .

### text [¶](https://textual.textualize.io/api/command/#textual.command.DiscoveryHit.text "Permanent link")

```
text = None
```

The command text associated with the hit, as plain text.

If `display` is not simple text, this attribute should be provided by the object.

## Hit [¶](https://textual.textualize.io/api/command/#textual.command.Hit "Permanent link")

```
Hit(score, match_display, command, text=None, help=None)
```

Holds the details of a single command search hit.

### command [¶](https://textual.textualize.io/api/command/#textual.command.Hit.command "Permanent link")

```
command
```

The function to call when the command is chosen.

### help [¶](https://textual.textualize.io/api/command/#textual.command.Hit.help "Permanent link")

```
help = None
```

Optional help text for the command.

### match\_display [¶](https://textual.textualize.io/api/command/#textual.command.Hit.match_display "Permanent link")

```
match_display
```

A string or Rich renderable representation of the hit.

### prompt [¶](https://textual.textualize.io/api/command/#textual.command.Hit.prompt "Permanent link")

```
prompt
```

The prompt to use when displaying the hit in the command palette.

### score [¶](https://textual.textualize.io/api/command/#textual.command.Hit.score "Permanent link")

```
score
```

The score of the command hit.

The value should be between 0 (no match) and 1 (complete match).

### text [¶](https://textual.textualize.io/api/command/#textual.command.Hit.text "Permanent link")

```
text = None
```

The command text associated with the hit, as plain text.

If `match_display` is not simple text, this attribute should be provided by the object.

## Matcher [¶](https://textual.textualize.io/api/command/#textual.command.Matcher "Permanent link")

```
Matcher(, *, =None, =False)
```

A fuzzy matcher.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `query` [¶](https://textual.textualize.io/api/command/#textual.command.Matcher\(query\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A query as typed in by the user. | *required* |
| ### `match_style` [¶](https://textual.textualize.io/api/command/#textual.command.Matcher\(match_style\) "Permanent link") | `[Style](https://textual.textualize.io/api/style/#textual.style.Style " Style (textual.visual.Style)") \| None` | The style to use to highlight matched portions of a string. | `None` |
| ### `case_sensitive` [¶](https://textual.textualize.io/api/command/#textual.command.Matcher\(case_sensitive\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Should matching be case sensitive? | `False` |

### case\_sensitive [¶](https://textual.textualize.io/api/command/#textual.command.Matcher.case_sensitive "Permanent link")

```
case_sensitive
```

Is this matcher case sensitive?

### match\_style [¶](https://textual.textualize.io/api/command/#textual.command.Matcher.match_style "Permanent link")

```
match_style
```

The style that will be used to highlight hits in the matched text.

### query [¶](https://textual.textualize.io/api/command/#textual.command.Matcher.query "Permanent link")

```
query
```

The query string to look for.

### highlight [¶](https://textual.textualize.io/api/command/#textual.command.Matcher.highlight "Permanent link")

```
highlight()
```

Highlight the candidate with the fuzzy match.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `candidate` [¶](https://textual.textualize.io/api/command/#textual.command.Matcher.highlight\(candidate\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The candidate string to match against the query. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Content](https://textual.textualize.io/api/content/#textual.content.Content " Content (textual.content.Content)")` | A \[rich.text.Text\]\[`Text`\] object with highlighted matches. |

### match [¶](https://textual.textualize.io/api/command/#textual.command.Matcher.match "Permanent link")

```
match()
```

Match the candidate against the query.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `candidate` [¶](https://textual.textualize.io/api/command/#textual.command.Matcher.match\(candidate\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Candidate string to match against the query. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[float](https://docs.python.org/3/library/functions.html#float)` | Strength of the match from 0 to 1. |

## Provider [¶](https://textual.textualize.io/api/command/#textual.command.Provider "Permanent link")

```
Provider(, match_style=None)
```

Bases: `[ABC](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")`

Base class for command palette command providers.

To create new command provider, inherit from this class and implement .

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `screen` [¶](https://textual.textualize.io/api/command/#textual.command.Provider\(screen\) "Permanent link") | `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]` | A reference to the active screen. | *required* |

### app [¶](https://textual.textualize.io/api/command/#textual.command.Provider.app "Permanent link")

```
app
```

A reference to the application.

### focused [¶](https://textual.textualize.io/api/command/#textual.command.Provider.focused "Permanent link")

```
focused
```

The currently-focused widget in the currently-active screen in the application.

If no widget has focus this will be `None`.

### match\_style [¶](https://textual.textualize.io/api/command/#textual.command.Provider.match_style "Permanent link")

```
match_style
```

The preferred style to use when highlighting matching portions of the .

### screen [¶](https://textual.textualize.io/api/command/#textual.command.Provider.screen "Permanent link")

```
screen
```

The currently-active screen in the application.

### discover [¶](https://textual.textualize.io/api/command/#textual.command.Provider.discover "Permanent link")

```
discover()
```

A default collection of hits for the provider.

Yields:

| Type | Description |
| --- | --- |
|  | Instances of . |

Note

This is different from in that it should yield that should be shown by default (before user input).

It is permitted to *not* implement this method.

### matcher [¶](https://textual.textualize.io/api/command/#textual.command.Provider.matcher "Permanent link")

```
matcher(, =False)
```

Create a [fuzzy matcher](https://textual.textualize.io/api/fuzzy_matcher/#textual.fuzzy.Matcher " Matcher") for the given user input.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `user_input` [¶](https://textual.textualize.io/api/command/#textual.command.Provider.matcher\(user_input\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text that the user has input. | *required* |
| #### `case_sensitive` [¶](https://textual.textualize.io/api/command/#textual.command.Provider.matcher\(case_sensitive\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Should matching be case sensitive? | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[Matcher](https://textual.textualize.io/api/fuzzy_matcher/#textual.fuzzy.Matcher " Matcher (textual.fuzzy.Matcher)")` | A [fuzzy matcher](https://textual.textualize.io/api/fuzzy_matcher/#textual.fuzzy.Matcher " Matcher") object for matching against candidate hits. |

### search [¶](https://textual.textualize.io/api/command/#textual.command.Provider.search "Permanent link")

```
search()
```

A request to search for commands relevant to the given query.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `query` [¶](https://textual.textualize.io/api/command/#textual.command.Provider.search\(query\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The user input to be matched. | *required* |

Yields:

| Type | Description |
| --- | --- |
|  | Instances of . |

### shutdown [¶](https://textual.textualize.io/api/command/#textual.command.Provider.shutdown "Permanent link")

```
shutdown()
```

Called when the Provider is shutdown.

Use this method to perform an cleanup, if required.

### startup [¶](https://textual.textualize.io/api/command/#textual.command.Provider.startup "Permanent link")

```
startup()
```

Called after the Provider is initialized, but before any calls to `search`.

## SearchIcon [¶](https://textual.textualize.io/api/command/#textual.command.SearchIcon "Permanent link")

```
SearchIcon(
    content="",
    *,
    expand=False,
    shrink=False,
    markup=True,
    name=None,
    id=None,
    classes=None,
    disabled=False
)
```

Bases: `[Static](https://textual.textualize.io/widgets/static/#textual.widgets.Static " Static (textual.widgets.Static)")`

Widget for displaying a search icon before the command input.

### icon [¶](https://textual.textualize.io/api/command/#textual.command.SearchIcon.icon "Permanent link")

```
icon = var('🔎')
```

The icon to display.

## SimpleCommand [¶](https://textual.textualize.io/api/command/#textual.command.SimpleCommand "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

A simple command.

### callback [¶](https://textual.textualize.io/api/command/#textual.command.SimpleCommand.callback "Permanent link")

```
callback
```

The callback to invoke when the command is selected.

### help\_text [¶](https://textual.textualize.io/api/command/#textual.command.SimpleCommand.help_text "Permanent link")

```
help_text = None
```

The description of the command.

### name [¶](https://textual.textualize.io/api/command/#textual.command.SimpleCommand.name "Permanent link")

```
name
```

The name of the command.

## SimpleProvider [¶](https://textual.textualize.io/api/command/#textual.command.SimpleProvider "Permanent link")

```
SimpleProvider(screen, commands)
```

Bases:

A simple provider which the caller can pass commands to.

### discover [¶](https://textual.textualize.io/api/command/#textual.command.SimpleProvider.discover "Permanent link")

```
discover()
```

Handle a request for the discovery commands for this provider.

Yields:

| Type | Description |
| --- | --- |
|  | Commands that can be discovered. |