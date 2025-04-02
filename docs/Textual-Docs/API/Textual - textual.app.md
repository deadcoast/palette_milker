---
title: "Textual - textual.app"
source: "https://textual.textualize.io/api/app/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.app

Here you will find the class, which is the base class for Textual apps.

See [app basics](https://textual.textualize.io/guide/app) for how to build Textual apps.

## AutopilotCallbackType [¶](https://textual.textualize.io/api/app/#textual.app.AutopilotCallbackType "Permanent link")

```
AutopilotCallbackType = (
    "Callable[[Pilot[object]], Coroutine[Any, Any, None]]"
)
```

Signature for valid callbacks that can be used to control apps.

## CommandCallback [¶](https://textual.textualize.io/api/app/#textual.app.CommandCallback "Permanent link")

```
CommandCallback = (
    "Callable[[], Awaitable[Any]] | Callable[[], Any]"
)
```

Signature for callbacks used in

## RenderResult [¶](https://textual.textualize.io/api/app/#textual.app.RenderResult "Permanent link")

```
RenderResult = 'RenderableType | Visual | SupportsVisual'
```

Result of Widget.render()

## ScreenType [¶](https://textual.textualize.io/api/app/#textual.app.ScreenType "Permanent link")

```
ScreenType = TypeVar('ScreenType', bound=Screen)
```

Type var for a Screen, used in .

## ActionError [¶](https://textual.textualize.io/api/app/#textual.app.ActionError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Base class for exceptions relating to actions.

## ActiveModeError [¶](https://textual.textualize.io/api/app/#textual.app.ActiveModeError "Permanent link")

Bases:

Raised when attempting to remove the currently active mode.

## App [¶](https://textual.textualize.io/api/app/#textual.app.App "Permanent link")

```
App(
    =None,
    =None,
    =False,
    =False,
)
```

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[ReturnType]`, `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")`

The base class for Textual Applications.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `driver_class` [¶](https://textual.textualize.io/api/app/#textual.app.App\(driver_class\) "Permanent link") | `[Type](https://docs.python.org/3/library/typing.html#typing.Type "typing.Type")[Driver] \| None` | Driver class or `None` to auto-detect. This will be used by some Textual tools. | `None` |
| ### `css_path` [¶](https://textual.textualize.io/api/app/#textual.app.App\(css_path\) "Permanent link") | `[CSSPathType](https://textual.textualize.io/api/types/#textual.types.CSSPathType " CSSPathType (textual._path.CSSPathType)") \| None` | Path to CSS or `None` to use the `CSS_PATH` class variable. To load multiple CSS files, pass a list of strings or paths which will be loaded in order. | `None` |
| ### `watch_css` [¶](https://textual.textualize.io/api/app/#textual.app.App\(watch_css\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Reload CSS if the files changed. This is set automatically if you are using `textual run` with the `dev` switch. | `False` |
| ### `ansi_color` [¶](https://textual.textualize.io/api/app/#textual.app.App\(ansi_color\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Allow ANSI colors if `True`, or convert ANSI colors to to RGB if `False`. | `False` |

Raises:

| Type | Description |
| --- | --- |
| `CssPathError` | When the supplied CSS path(s) are an unexpected type. |

### ALLOW\_IN\_MAXIMIZED\_VIEW [¶](https://textual.textualize.io/api/app/#textual.app.App.ALLOW_IN_MAXIMIZED_VIEW "Permanent link")

```
ALLOW_IN_MAXIMIZED_VIEW = 'Footer'
```

The default value of [Screen.ALLOW\_IN\_MAXIMIZED\_VIEW](https://textual.textualize.io/api/screen/#textual.screen.Screen.ALLOW_IN_MAXIMIZED_VIEW " ALLOW_IN_MAXIMIZED_VIEW").

### ALLOW\_SELECT [¶](https://textual.textualize.io/api/app/#textual.app.App.ALLOW_SELECT "Permanent link")

```
ALLOW_SELECT = True
```

A switch to toggle arbitrary text selection for the app.

Note that this doesn't apply to Input and TextArea which have builtin support for selection.

### AUTO\_FOCUS [¶](https://textual.textualize.io/api/app/#textual.app.App.AUTO_FOCUS "Permanent link")

```
AUTO_FOCUS = '*'
```

A selector to determine what to focus automatically when a screen is activated.

The widget focused is the first that matches the given [CSS selector](https://textual.textualize.io/guide/queries/#query-selectors). Setting to `None` or `""` disables auto focus.

### BINDINGS [¶](https://textual.textualize.io/api/app/#textual.app.App.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding(
        "ctrl+q",
        "quit",
        "Quit",
        tooltip="Quit the app and return to the command prompt.",
        show=False,
        priority=True,
    ),
    Binding("ctrl+c", "help_quit", show=False, system=True),
]
```

The default key bindings.

### BINDING\_GROUP\_TITLE [¶](https://textual.textualize.io/api/app/#textual.app.App.BINDING_GROUP_TITLE "Permanent link")

```
BINDING_GROUP_TITLE = None
```

Set to text to show in the key panel.

### CLICK\_CHAIN\_TIME\_THRESHOLD [¶](https://textual.textualize.io/api/app/#textual.app.App.CLICK_CHAIN_TIME_THRESHOLD "Permanent link")

```
CLICK_CHAIN_TIME_THRESHOLD = 0.5
```

The maximum number of seconds between clicks to upgrade a single click to a double click, a double click to a triple click, etc.

### CLOSE\_TIMEOUT [¶](https://textual.textualize.io/api/app/#textual.app.App.CLOSE_TIMEOUT "Permanent link")

```
CLOSE_TIMEOUT = 5.0
```

Timeout waiting for widget's to close, or `None` for no timeout.

### COMMANDS [¶](https://textual.textualize.io/api/app/#textual.app.App.COMMANDS "Permanent link")

```
COMMANDS = {}
```

Command providers used by the [command palette](https://textual.textualize.io/guide/command_palette).

Should be a set of [command.Provider](https://textual.textualize.io/api/command/#textual.command.Provider " Provider") classes.

### COMMAND\_PALETTE\_BINDING [¶](https://textual.textualize.io/api/app/#textual.app.App.COMMAND_PALETTE_BINDING "Permanent link")

```
COMMAND_PALETTE_BINDING = 'ctrl+p'
```

The key that launches the command palette (if enabled by ).

### COMMAND\_PALETTE\_DISPLAY [¶](https://textual.textualize.io/api/app/#textual.app.App.COMMAND_PALETTE_DISPLAY "Permanent link")

```
COMMAND_PALETTE_DISPLAY = None
```

How the command palette key should be displayed in the footer (or `None` for default).

### CSS [¶](https://textual.textualize.io/api/app/#textual.app.App.CSS "Permanent link")

```
CSS = ''
```

Inline CSS, useful for quick scripts. This is loaded after CSS\_PATH, and therefore takes priority in the event of a specificity clash.

### CSS\_PATH [¶](https://textual.textualize.io/api/app/#textual.app.App.CSS_PATH "Permanent link")

```
CSS_PATH = None
```

File paths to load CSS from.

### DEFAULT\_MODE [¶](https://textual.textualize.io/api/app/#textual.app.App.DEFAULT_MODE "Permanent link")

```
DEFAULT_MODE = '_default'
```

Name of the default mode.

### ENABLE\_COMMAND\_PALETTE [¶](https://textual.textualize.io/api/app/#textual.app.App.ENABLE_COMMAND_PALETTE "Permanent link")

```
ENABLE_COMMAND_PALETTE = True
```

Should the [command palette](https://textual.textualize.io/api/command/#textual.command.CommandPalette " CommandPalette") be enabled for the application?

### ESCAPE\_TO\_MINIMIZE [¶](https://textual.textualize.io/api/app/#textual.app.App.ESCAPE_TO_MINIMIZE "Permanent link")

```
ESCAPE_TO_MINIMIZE = True
```

Use escape key to minimize widgets (potentially overriding bindings).

This is the default value, used if the active screen's `ESCAPE_TO_MINIMIZE` is not changed from `None`.

### INLINE\_PADDING [¶](https://textual.textualize.io/api/app/#textual.app.App.INLINE_PADDING "Permanent link")

```
INLINE_PADDING = 1
```

Number of blank lines above an inline app.

### MODES [¶](https://textual.textualize.io/api/app/#textual.app.App.MODES "Permanent link")

```
MODES = {}
```

Modes associated with the app and their base screens.

The base screen is the screen at the bottom of the mode stack. You can think of it as the default screen for that stack. The base screens can be names of screens listed in , [`Screen`](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen") instances, or callables that return screens.

Example
```
class HelpScreen(Screen[None]):
    ...

class MainAppScreen(Screen[None]):
    ...

class MyApp(App[None]):
    MODES = {
        "default": "main",
        "help": HelpScreen,
    }

    SCREENS = {
        "main": MainAppScreen,
    }

    ...
```

### NOTIFICATION\_TIMEOUT [¶](https://textual.textualize.io/api/app/#textual.app.App.NOTIFICATION_TIMEOUT "Permanent link")

```
NOTIFICATION_TIMEOUT = 5
```

Default number of seconds to show notifications before removing them.

### SCREENS [¶](https://textual.textualize.io/api/app/#textual.app.App.SCREENS "Permanent link")

```
SCREENS = {}
```

Screens associated with the app for the lifetime of the app.

### SUB\_TITLE [¶](https://textual.textualize.io/api/app/#textual.app.App.SUB_TITLE "Permanent link")

```
SUB_TITLE = None
```

A class variable to set the default sub-title for the application.

To update the sub-title while the app is running, you can set the attribute. See also [the `Screen.SUB_TITLE` attribute](https://textual.textualize.io/api/screen/#textual.screen.Screen.SUB_TITLE " SUB_TITLE").

### SUSPENDED\_SCREEN\_CLASS [¶](https://textual.textualize.io/api/app/#textual.app.App.SUSPENDED_SCREEN_CLASS "Permanent link")

```
SUSPENDED_SCREEN_CLASS = ''
```

Class to apply to suspended screens, or empty string for no class.

### TITLE [¶](https://textual.textualize.io/api/app/#textual.app.App.TITLE "Permanent link")

```
TITLE = None
```

A class variable to set the *default* title for the application.

To update the title while the app is running, you can set the attribute. See also [the `Screen.TITLE` attribute](https://textual.textualize.io/api/screen/#textual.screen.Screen.TITLE " TITLE").

```
TOOLTIP_DELAY = 0.5
```

The time in seconds after which a tooltip gets displayed.

### active\_bindings [¶](https://textual.textualize.io/api/app/#textual.app.App.active_bindings "Permanent link")

```
active_bindings
```

Get currently active bindings.

If no widget is focused, then app-level bindings are returned. If a widget is focused, then any bindings present in the active screen and app are merged and returned.

This property may be used to inspect current bindings.

Returns:

| Type | Description |
| --- | --- |
| `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [ActiveBinding](https://textual.textualize.io/api/binding/#textual.binding.ActiveBinding " ActiveBinding (textual.screen.ActiveBinding)")]` | A dict that maps keys on to binding information. |

### animation\_level [¶](https://textual.textualize.io/api/app/#textual.app.App.animation_level "Permanent link")

```
animation_level = TEXTUAL_ANIMATIONS
```

Determines what type of animations the app will display.

See [`textual.constants.TEXTUAL_ANIMATIONS`](https://textual.textualize.io/api/constants/#textual.constants.TEXTUAL_ANIMATIONS " TEXTUAL_ANIMATIONS").

### animator [¶](https://textual.textualize.io/api/app/#textual.app.App.animator "Permanent link")

```
animator
```

The animator object.

### ansi\_color [¶](https://textual.textualize.io/api/app/#textual.app.App.ansi_color "Permanent link")

```
ansi_color = Reactive(False)
```

Allow ANSI colors in UI?

### ansi\_theme [¶](https://textual.textualize.io/api/app/#textual.app.App.ansi_theme "Permanent link")

```
ansi_theme
```

The ANSI TerminalTheme currently being used.

Defines how colors defined as ANSI (e.g. `magenta`) inside Rich renderables are mapped to hex codes.

### ansi\_theme\_dark [¶](https://textual.textualize.io/api/app/#textual.app.App.ansi_theme_dark "Permanent link")

```
ansi_theme_dark = Reactive(MONOKAI, init=False)
```

Maps ANSI colors to hex colors using a Rich TerminalTheme object while using a dark theme.

### ansi\_theme\_light [¶](https://textual.textualize.io/api/app/#textual.app.App.ansi_theme_light "Permanent link")

```
ansi_theme_light = Reactive(ALABASTER, init=False)
```

Maps ANSI colors to hex colors using a Rich TerminalTheme object while using a light theme.

### app\_focus [¶](https://textual.textualize.io/api/app/#textual.app.App.app_focus "Permanent link")

```
app_focus = Reactive(True, compute=False)
```

Indicates if the app has focus.

When run in the terminal, the app always has focus. When run in the web, the app will get focus when the terminal widget has focus.

### app\_resume\_signal [¶](https://textual.textualize.io/api/app/#textual.app.App.app_resume_signal "Permanent link")

```
app_resume_signal = Signal(self, 'app-resume')
```

The signal that is published when the app is resumed after a suspend.

When the app is resumed after a call this signal will be [published](https://textual.textualize.io/api/signal/#textual.signal.Signal.publish " publish"); [subscribe](https://textual.textualize.io/api/signal/#textual.signal.Signal.subscribe " subscribe") to this signal to perform work after the app has resumed.

### app\_suspend\_signal [¶](https://textual.textualize.io/api/app/#textual.app.App.app_suspend_signal "Permanent link")

```
app_suspend_signal = Signal(self, 'app-suspend')
```

The signal that is published when the app is suspended.

When is called this signal will be [published](https://textual.textualize.io/api/signal/#textual.signal.Signal.publish " publish"); [subscribe](https://textual.textualize.io/api/signal/#textual.signal.Signal.subscribe " subscribe") to this signal to perform work before the suspension takes place.

### available\_themes [¶](https://textual.textualize.io/api/app/#textual.app.App.available_themes "Permanent link")

```
available_themes
```

All available themes (all built-in themes plus any that have been registered).

A dictionary mapping theme names to Theme instances.

### children [¶](https://textual.textualize.io/api/app/#textual.app.App.children "Permanent link")

```
children
```

A view onto the app's immediate children.

This attribute exists on all widgets. In the case of the App, it will only ever contain a single child, which will be the currently active screen.

Returns:

| Type | Description |
| --- | --- |
| `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")['Widget']` | A sequence of widgets. |

### clipboard [¶](https://textual.textualize.io/api/app/#textual.app.App.clipboard "Permanent link")

```
clipboard
```

The value of the local clipboard.

Note, that this only contains text copied in the app, and not text copied from elsewhere in the OS.

### current\_mode [¶](https://textual.textualize.io/api/app/#textual.app.App.current_mode "Permanent link")

```
current_mode
```

The name of the currently active mode.

### cursor\_position [¶](https://textual.textualize.io/api/app/#textual.app.App.cursor_position "Permanent link")

```
cursor_position = Offset(0, 0)
```

The position of the terminal cursor in screen-space.

This can be set by widgets and is useful for controlling the positioning of OS IME and emoji popup menus.

### debug [¶](https://textual.textualize.io/api/app/#textual.app.App.debug "Permanent link")

```
debug
```

Is debug mode enabled?

### default\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.default_screen "Permanent link")

```
default_screen
```

The default screen instance.

### escape\_to\_minimize [¶](https://textual.textualize.io/api/app/#textual.app.App.escape_to_minimize "Permanent link")

```
escape_to_minimize
```

Use the escape key to minimize?

When a widget is [maximized](https://textual.textualize.io/api/screen/#textual.screen.Screen.maximize " maximize"), this boolean determines if the `escape` key will minimize the widget (potentially overriding any bindings).

The default logic is to use the screen's `ESCAPE_TO_MINIMIZE` classvar if it is set to `True` or `False`. If the classvar on the screen is *not* set (and left as `None`), then the app's `ESCAPE_TO_MINIMIZE` is used.

### focused [¶](https://textual.textualize.io/api/app/#textual.app.App.focused "Permanent link")

```
focused
```

The widget that is focused on the currently active screen, or `None`.

Focused widgets receive keyboard input.

Returns:

| Type | Description |
| --- | --- |
| `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | The currently focused widget, or `None` if nothing is focused. |

### is\_attached [¶](https://textual.textualize.io/api/app/#textual.app.App.is_attached "Permanent link")

```
is_attached
```

Is this node linked to the app through the DOM?

### is\_dom\_root [¶](https://textual.textualize.io/api/app/#textual.app.App.is_dom_root "Permanent link")

```
is_dom_root
```

Is this a root node (i.e. the App)?

### is\_headless [¶](https://textual.textualize.io/api/app/#textual.app.App.is_headless "Permanent link")

```
is_headless
```

Is the app running in 'headless' mode?

Headless mode is used when running tests with .

### is\_inline [¶](https://textual.textualize.io/api/app/#textual.app.App.is_inline "Permanent link")

```
is_inline
```

Is the app running in 'inline' mode?

### is\_web [¶](https://textual.textualize.io/api/app/#textual.app.App.is_web "Permanent link")

```
is_web
```

Is the app running in 'web' mode via a browser?

### log [¶](https://textual.textualize.io/api/app/#textual.app.App.log "Permanent link")

```
log
```

The textual logger.

Example
```
self.log("Hello, World!")
self.log(self.tree)
```

Returns:

| Type | Description |
| --- | --- |
| `[Logger](https://textual.textualize.io/api/logger/#textual.Logger " Logger (textual.Logger)")` | A Textual logger. |

### return\_code [¶](https://textual.textualize.io/api/app/#textual.app.App.return_code "Permanent link")

```
return_code
```

The return code with which the app exited.

Non-zero codes indicate errors. A value of 1 means the app exited with a fatal error. If the app hasn't exited yet, this will be `None`.

Example

The return code can be used to exit the process via `sys.exit`.

```
my_app.run()
sys.exit(my_app.return_code)
```

### return\_value [¶](https://textual.textualize.io/api/app/#textual.app.App.return_value "Permanent link")

```
return_value
```

The return value of the app, or `None` if it has not yet been set.

The return value is set when calling .

### screen [¶](https://textual.textualize.io/api/app/#textual.app.App.screen "Permanent link")

```
screen
```

The current active screen.

Returns:

| Type | Description |
| --- | --- |
| `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")[[object](https://docs.python.org/3/library/functions.html#object)]` | The currently active (visible) screen. |

Raises:

| Type | Description |
| --- | --- |
|  | If there are no screens on the stack. |

### screen\_stack [¶](https://textual.textualize.io/api/app/#textual.app.App.screen_stack "Permanent link")

```
screen_stack
```

A snapshot of the current screen stack.

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]]` | A snapshot of the current state of the screen stack. |

### scroll\_sensitivity\_x [¶](https://textual.textualize.io/api/app/#textual.app.App.scroll_sensitivity_x "Permanent link")

```
scroll_sensitivity_x = 4.0
```

Number of columns to scroll in the X direction with wheel or trackpad.

### scroll\_sensitivity\_y [¶](https://textual.textualize.io/api/app/#textual.app.App.scroll_sensitivity_y "Permanent link")

```
scroll_sensitivity_y = 2.0
```

Number of lines to scroll in the Y direction with wheel or trackpad.

### size [¶](https://textual.textualize.io/api/app/#textual.app.App.size "Permanent link")

```
size
```

The size of the terminal.

Returns:

| Type | Description |
| --- | --- |
| `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | Size of the terminal. |

### sub\_title [¶](https://textual.textualize.io/api/app/#textual.app.App.sub_title "Permanent link")

```
sub_title = SUB_TITLE if SUB_TITLE is not None else ''
```

The sub-title for the application.

The initial value for `sub_title` will be set to the `SUB_TITLE` class variable if it exists, or an empty string if it doesn't.

Sub-titles are typically used to show the high-level state of the app, such as the current mode, or path to the file being worked on.

Assign a new value to this attribute to change the sub-title. The new value is always converted to string.

### supports\_smooth\_scrolling [¶](https://textual.textualize.io/api/app/#textual.app.App.supports_smooth_scrolling "Permanent link")

```
supports_smooth_scrolling = False
```

Does the terminal support smooth scrolling?

### theme [¶](https://textual.textualize.io/api/app/#textual.app.App.theme "Permanent link")

```
theme = Reactive(DEFAULT_THEME)
```

The name of the currently active theme.

### theme\_changed\_signal [¶](https://textual.textualize.io/api/app/#textual.app.App.theme_changed_signal "Permanent link")

```
theme_changed_signal = Signal(self, 'theme-changed')
```

Signal that is published when the App's theme is changed.

Subscribers will receive the new theme object as an argument to the callback.

### theme\_variables [¶](https://textual.textualize.io/api/app/#textual.app.App.theme_variables "Permanent link")

```
theme_variables = {}
```

Variables generated from the current theme.

### title [¶](https://textual.textualize.io/api/app/#textual.app.App.title "Permanent link")

```
title = TITLE if TITLE is not None else f'{__name__}'
```

The title for the application.

The initial value for `title` will be set to the `TITLE` class variable if it exists, or the name of the app if it doesn't.

Assign a new value to this attribute to change the title. The new value is always converted to string.

### use\_command\_palette [¶](https://textual.textualize.io/api/app/#textual.app.App.use_command_palette "Permanent link")

```
use_command_palette = ENABLE_COMMAND_PALETTE
```

A flag to say if the application should use the command palette.

If set to `False` any call to will be ignored.

### workers [¶](https://textual.textualize.io/api/app/#textual.app.App.workers "Permanent link")

```
workers
```

The [worker](https://textual.textualize.io/guide/workers/) manager.

Returns:

| Type | Description |
| --- | --- |
| `[WorkerManager](https://textual.textualize.io/api/worker_manager/#textual.worker_manager.WorkerManager " WorkerManager (textual.worker_manager.WorkerManager)")` | An object to manage workers. |

### action\_add\_class [¶](https://textual.textualize.io/api/app/#textual.app.App.action_add_class "Permanent link")

```
action_add_class(, )
```

An [action](https://textual.textualize.io/guide/actions) to add a CSS class to the selected widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_add_class\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Selects the widget to add the class to. | *required* |
| #### `class_name` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_add_class\(class_name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The class to add to the selected widget. | *required* |

### action\_back [¶](https://textual.textualize.io/api/app/#textual.app.App.action_back "Permanent link")

```
action_back()
```

An [action](https://textual.textualize.io/guide/actions) to go back to the previous screen (pop the current screen).

Note

If there is no screen to go back to, this is a non-operation (in other words it's safe to call even if there are no other screens on the stack.)

### action\_bell [¶](https://textual.textualize.io/api/app/#textual.app.App.action_bell "Permanent link")

```
action_bell()
```

An [action](https://textual.textualize.io/guide/actions) to play the terminal 'bell'.

### action\_change\_theme [¶](https://textual.textualize.io/api/app/#textual.app.App.action_change_theme "Permanent link")

```
action_change_theme()
```

An [action](https://textual.textualize.io/guide/actions) to change the current theme.

### action\_command\_palette [¶](https://textual.textualize.io/api/app/#textual.app.App.action_command_palette "Permanent link")

```
action_command_palette()
```

Show the Textual command palette.

### action\_focus [¶](https://textual.textualize.io/api/app/#textual.app.App.action_focus "Permanent link")

```
action_focus()
```

An [action](https://textual.textualize.io/guide/actions) to focus the given widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget_id` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_focus\(widget_id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | ID of widget to focus. | *required* |

### action\_focus\_next [¶](https://textual.textualize.io/api/app/#textual.app.App.action_focus_next "Permanent link")

```
action_focus_next()
```

An [action](https://textual.textualize.io/guide/actions) to focus the next widget.

### action\_focus\_previous [¶](https://textual.textualize.io/api/app/#textual.app.App.action_focus_previous "Permanent link")

```
action_focus_previous()
```

An [action](https://textual.textualize.io/guide/actions) to focus the previous widget.

### action\_help\_quit [¶](https://textual.textualize.io/api/app/#textual.app.App.action_help_quit "Permanent link")

```
action_help_quit()
```

Bound to ctrl+C to alert the user that it no longer quits.

### action\_hide\_help\_panel [¶](https://textual.textualize.io/api/app/#textual.app.App.action_hide_help_panel "Permanent link")

```
action_hide_help_panel()
```

Hide the keys panel (if present).

### action\_notify [¶](https://textual.textualize.io/api/app/#textual.app.App.action_notify "Permanent link")

```
action_notify(message, title='', severity='information')
```

Show a notification.

### action\_pop\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.action_pop_screen "Permanent link")

```
action_pop_screen()
```

An [action](https://textual.textualize.io/guide/actions) to remove the topmost screen and makes the new topmost screen active.

### action\_push\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.action_push_screen "Permanent link")

```
action_push_screen()
```

An [action](https://textual.textualize.io/guide/actions) to push a new screen on to the stack and make it active.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_push_screen\(screen\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of the screen. | *required* |

### action\_quit [¶](https://textual.textualize.io/api/app/#textual.app.App.action_quit "Permanent link")

```
action_quit()
```

An [action](https://textual.textualize.io/guide/actions) to quit the app as soon as possible.

### action\_remove\_class [¶](https://textual.textualize.io/api/app/#textual.app.App.action_remove_class "Permanent link")

```
action_remove_class(, )
```

An [action](https://textual.textualize.io/guide/actions) to remove a CSS class from the selected widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_remove_class\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Selects the widget to remove the class from. | *required* |
| #### `class_name` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_remove_class\(class_name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The class to remove from the selected widget. | *required* |

### action\_screenshot [¶](https://textual.textualize.io/api/app/#textual.app.App.action_screenshot "Permanent link")

```
action_screenshot(=None, =None)
```

This [action](https://textual.textualize.io/guide/actions) will save an SVG file containing the current contents of the screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `filename` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_screenshot\(filename\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Filename of screenshot, or None to auto-generate. | `None` |
| #### `path` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_screenshot\(path\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Path to directory. Defaults to the user's Downloads directory. | `None` |

### action\_show\_help\_panel [¶](https://textual.textualize.io/api/app/#textual.app.App.action_show_help_panel "Permanent link")

```
action_show_help_panel()
```

Show the keys panel.

### action\_simulate\_key [¶](https://textual.textualize.io/api/app/#textual.app.App.action_simulate_key "Permanent link")

```
action_simulate_key()
```

An [action](https://textual.textualize.io/guide/actions) to simulate a key press.

This will invoke the same actions as if the user had pressed the key.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_simulate_key\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The key to process. | *required* |

### action\_suspend\_process [¶](https://textual.textualize.io/api/app/#textual.app.App.action_suspend_process "Permanent link")

```
action_suspend_process()
```

Suspend the process into the background.

Note

On Unix and Unix-like systems a `SIGTSTP` is sent to the application's process. Currently on Windows and when running under Textual Web this is a non-operation.

### action\_switch\_mode [¶](https://textual.textualize.io/api/app/#textual.app.App.action_switch_mode "Permanent link")

```
action_switch_mode(mode)
```

An [action](https://textual.textualize.io/guide/actions) that switches to the given mode.

### action\_switch\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.action_switch_screen "Permanent link")

```
action_switch_screen()
```

An [action](https://textual.textualize.io/guide/actions) to switch screens.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_switch_screen\(screen\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of the screen. | *required* |

### action\_toggle\_class [¶](https://textual.textualize.io/api/app/#textual.app.App.action_toggle_class "Permanent link")

```
action_toggle_class(, )
```

An [action](https://textual.textualize.io/guide/actions) to toggle a CSS class on the selected widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `selector` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_toggle_class\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Selects the widget to toggle the class on. | *required* |
| #### `class_name` [¶](https://textual.textualize.io/api/app/#textual.app.App.action_toggle_class\(class_name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The class to toggle on the selected widget. | *required* |

### action\_toggle\_dark [¶](https://textual.textualize.io/api/app/#textual.app.App.action_toggle_dark "Permanent link")

```
action_toggle_dark()
```

An [action](https://textual.textualize.io/guide/actions) to toggle the theme between textual-light and textual-dark. This is offered as a convenience to simplify backwards compatibility with previous versions of Textual which only had light mode and dark mode.

### add\_mode [¶](https://textual.textualize.io/api/app/#textual.app.App.add_mode "Permanent link")

```
add_mode(, )
```

Adds a mode and its corresponding base screen to the app.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `mode` [¶](https://textual.textualize.io/api/app/#textual.app.App.add_mode\(mode\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The new mode. | *required* |
| #### `base_screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.add_mode\(base_screen\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[], [Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")]` | The base screen associated with the given mode. | *required* |

Raises:

| Type | Description |
| --- | --- |
|  | If the name of the mode is not valid/duplicated. |

### animate [¶](https://textual.textualize.io/api/app/#textual.app.App.animate "Permanent link")

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

See the guide for how to use the [animation](https://textual.textualize.io/guide/animation) system.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `attribute` [¶](https://textual.textualize.io/api/app/#textual.app.App.animate\(attribute\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of the attribute to animate. | *required* |
| #### `value` [¶](https://textual.textualize.io/api/app/#textual.app.App.animate\(value\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| [Animatable](https://textual.textualize.io/api/types/#textual.types.Animatable " Animatable (textual._animator.Animatable)")` | The value to animate to. | *required* |
| #### `final_value` [¶](https://textual.textualize.io/api/app/#textual.app.App.animate\(final_value\) "Permanent link") | `[object](https://docs.python.org/3/library/functions.html#object)` | The final value of the animation. | `...` |
| #### `duration` [¶](https://textual.textualize.io/api/app/#textual.app.App.animate\(duration\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The duration (in seconds) of the animation. | `None` |
| #### `speed` [¶](https://textual.textualize.io/api/app/#textual.app.App.animate\(speed\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The speed of the animation. | `None` |
| #### `delay` [¶](https://textual.textualize.io/api/app/#textual.app.App.animate\(delay\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float)` | A delay (in seconds) before the animation starts. | `0.0` |
| #### `easing` [¶](https://textual.textualize.io/api/app/#textual.app.App.animate\(easing\) "Permanent link") | `[EasingFunction](https://textual.textualize.io/api/types/#textual.types.EasingFunction " EasingFunction (textual._animator.EasingFunction)") \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | An easing method. | `DEFAULT_EASING` |
| #### `on_complete` [¶](https://textual.textualize.io/api/app/#textual.app.App.animate\(on_complete\) "Permanent link") | `[CallbackType](https://textual.textualize.io/api/types/#textual.types.CallbackType " CallbackType (textual.messages.CallbackType)") \| None` | A callable to invoke when the animation is finished. | `None` |
| #### `level` [¶](https://textual.textualize.io/api/app/#textual.app.App.animate\(level\) "Permanent link") | `[AnimationLevel](https://textual.textualize.io/api/types/#textual.types.AnimationLevel " AnimationLevel (textual._types.AnimationLevel)")` | Minimum level required for the animation to take place (inclusive). | `'full'` |

### batch\_update [¶](https://textual.textualize.io/api/app/#textual.app.App.batch_update "Permanent link")

```
batch_update()
```

A context manager to suspend all repaints until the end of the batch.

### begin\_capture\_print [¶](https://textual.textualize.io/api/app/#textual.app.App.begin_capture_print "Permanent link")

```
begin_capture_print(, =True, =True)
```

Capture content that is printed (or written to stdout / stderr).

If printing is captured, the `target` will be sent an [events.Print](https://textual.textualize.io/api/events/#textual.events.Print " Print") message.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `target` [¶](https://textual.textualize.io/api/app/#textual.app.App.begin_capture_print\(target\) "Permanent link") | `[MessageTarget](https://textual.textualize.io/api/types/#textual.types.MessageTarget " MessageTarget (textual._types.MessageTarget)")` | The widget where print content will be sent. | *required* |
| #### `stdout` [¶](https://textual.textualize.io/api/app/#textual.app.App.begin_capture_print\(stdout\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Capture stdout. | `True` |
| #### `stderr` [¶](https://textual.textualize.io/api/app/#textual.app.App.begin_capture_print\(stderr\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Capture stderr. | `True` |

### bell [¶](https://textual.textualize.io/api/app/#textual.app.App.bell "Permanent link")

```
bell()
```

Play the console 'bell'.

For terminals that support a bell, this typically makes a notification or error sound. Some terminals may make no sound or display a visual bell indicator, depending on configuration.

### bind [¶](https://textual.textualize.io/api/app/#textual.app.App.bind "Permanent link")

```
bind(
    ,
    ,
    *,
    ="",
    =True,
    =None
)
```

Bind a key to an action.

Warning

This method may be private or removed in a future version of Textual. See [dynamic actions](https://textual.textualize.io/guide/actions#dynamic-actions) for a more flexible alternative to updating bindings.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `keys` [¶](https://textual.textualize.io/api/app/#textual.app.App.bind\(keys\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A comma separated list of keys, i.e. | *required* |
| #### `action` [¶](https://textual.textualize.io/api/app/#textual.app.App.bind\(action\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Action to bind to. | *required* |
| #### `description` [¶](https://textual.textualize.io/api/app/#textual.app.App.bind\(description\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Short description of action. | `''` |
| #### `show` [¶](https://textual.textualize.io/api/app/#textual.app.App.bind\(show\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Show key in UI. | `True` |
| #### `key_display` [¶](https://textual.textualize.io/api/app/#textual.app.App.bind\(key_display\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Replacement text for key, or None to use default. | `None` |

### call\_from\_thread [¶](https://textual.textualize.io/api/app/#textual.app.App.call_from_thread "Permanent link")

```
call_from_thread(, *, **)
```

Run a callable from another thread, and return the result.

Like asyncio apps in general, Textual apps are not thread-safe. If you call methods or set attributes on Textual objects from a thread, you may get unpredictable results.

This method will ensure that your code runs within the correct context.

Tip

Consider using [post\_message](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.post_message " post_message") which is also thread-safe.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `callback` [¶](https://textual.textualize.io/api/app/#textual.app.App.call_from_thread\(callback\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[..., CallThreadReturnType \| [Awaitable](https://docs.python.org/3/library/typing.html#typing.Awaitable "typing.Awaitable")[CallThreadReturnType]]` | A callable to run. | *required* |
| #### `*args` [¶](https://textual.textualize.io/api/app/#textual.app.App.call_from_thread\(*args\) "Permanent link") | `[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | Arguments to the callback. | `()` |
| #### `**kwargs` [¶](https://textual.textualize.io/api/app/#textual.app.App.call_from_thread\(**kwargs\) "Permanent link") | `[Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | Keyword arguments for the callback. | `{}` |

Raises:

| Type | Description |
| --- | --- |
| `[RuntimeError](https://docs.python.org/3/library/exceptions.html#RuntimeError)` | If the app isn't running or if this method is called from the same thread where the app is running. |

Returns:

| Type | Description |
| --- | --- |
| `CallThreadReturnType` | The result of the callback. |

### capture\_mouse [¶](https://textual.textualize.io/api/app/#textual.app.App.capture_mouse "Permanent link")

```
capture_mouse()
```

Send all mouse events to the given widget or disable mouse capture.

Normally mouse events are sent to the widget directly under the pointer. Capturing the mouse allows a widget to receive mouse events even when the pointer is over another widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/app/#textual.app.App.capture_mouse\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | Widget to capture mouse events, or `None` to end mouse capture. | *required* |

### clear\_notifications [¶](https://textual.textualize.io/api/app/#textual.app.App.clear_notifications "Permanent link")

```
clear_notifications()
```

Clear all the current notifications.

### compose [¶](https://textual.textualize.io/api/app/#textual.app.App.compose "Permanent link")

```
compose()
```

Yield child widgets for a container.

This method should be implemented in a subclass.

### copy\_to\_clipboard [¶](https://textual.textualize.io/api/app/#textual.app.App.copy_to_clipboard "Permanent link")

```
copy_to_clipboard()
```

Copy text to the clipboard.

Note

This does not work on macOS Terminal, but will work on most other terminals.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `text` [¶](https://textual.textualize.io/api/app/#textual.app.App.copy_to_clipboard\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Text you wish to copy to the clipboard. | *required* |

### deliver\_binary [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_binary "Permanent link")

```
deliver_binary(
    ,
    *,
    =None,
    =None,
    ="download",
    =None,
    =None
)
```

Deliver a binary file to the end-user of the application.

If an IO object is supplied, it will be closed by this method and *must not be used* after it is supplied to this method.

If running in a terminal, this will save the file to the user's downloads directory.

If running via a web browser, this will initiate a download via a single-use URL.

This operation runs in a thread when running on web, so this method returning does not indicate that the file has been delivered.

After the file has been delivered, a `DeliveryComplete` message will be posted to this `App`, which contains the `delivery_key` returned by this method. By handling this message, you can add custom logic to your application that fires only after the file has been delivered.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `path_or_file` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_binary\(path_or_file\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") \| [BinaryIO](https://docs.python.org/3/library/typing.html#typing.BinaryIO "typing.BinaryIO")` | The path or file-like object to save. | *required* |
| #### `save_directory` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_binary\(save_directory\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") \| None` | The directory to save the file to. If None, the default "downloads" directory will be used. This argument is ignored when running via the web. | `None` |
| #### `save_filename` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_binary\(save_filename\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The filename to save the file to. If None, the following logic applies to generate the filename: - If `path_or_file` is a file-like object, the filename will be taken from the `name` attribute if available. - If `path_or_file` is a path, the filename will be taken from the path. - If a filename is not available, a filename will be generated using the App's title and the current date and time. | `None` |
| #### `open_method` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_binary\(open_method\) "Permanent link") | `Literal['browser', 'download']` | The method to use to open the file. "browser" will open the file in the web browser, "download" will initiate a download. Note that this can sometimes be impacted by the browser's settings. | `'download'` |
| #### `mime_type` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_binary\(mime_type\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The MIME type of the file or None to guess based on file extension. If no MIME type is supplied and we cannot guess the MIME type, from the file extension, the MIME type will be set to "application/octet-stream". | `None` |
| #### `name` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_binary\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A user-defined named which will be returned in [`DeliveryComplete`](https://textual.textualize.io/api/events/#textual.events.DeliveryComplete " DeliveryComplete") and [`DeliveryComplete`](https://textual.textualize.io/api/events/#textual.events.DeliveryComplete " DeliveryComplete"). | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The delivery key that uniquely identifies the file delivery. |

### deliver\_screenshot [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_screenshot "Permanent link")

```
deliver_screenshot(
    =None, =None, =None
)
```

Deliver a screenshot of the app.

This with save the screenshot when running locally, or serve it when the app is running in a web browser.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `filename` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_screenshot\(filename\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Filename of SVG screenshot, or None to auto-generate a filename with the date and time. | `None` |
| #### `path` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_screenshot\(path\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Path to directory for output when saving locally (not used when app is running in the browser). Defaults to current working directory. | `None` |
| #### `time_format` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_screenshot\(time_format\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Date and time format to use if filename is None. Defaults to a format like ISO 8601 with some reserved characters replaced with underscores. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The delivery key that uniquely identifies the file delivery. |

### deliver\_text [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_text "Permanent link")

```
deliver_text(
    ,
    *,
    =None,
    =None,
    open_method="download",
    =None,
    =None,
    =None
)
```

Deliver a text file to the end-user of the application.

If a TextIO object is supplied, it will be closed by this method and *must not be used* after this method is called.

If running in a terminal, this will save the file to the user's downloads directory.

If running via a web browser, this will initiate a download via a single-use URL.

After the file has been delivered, a `DeliveryComplete` message will be posted to this `App`, which contains the `delivery_key` returned by this method. By handling this message, you can add custom logic to your application that fires only after the file has been delivered.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `path_or_file` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_text\(path_or_file\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") \| [TextIO](https://docs.python.org/3/library/typing.html#typing.TextIO "typing.TextIO")` | The path or file-like object to save. | *required* |
| #### `save_directory` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_text\(save_directory\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") \| None` | The directory to save the file to. | `None` |
| #### `save_filename` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_text\(save_filename\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The filename to save the file to. If `path_or_file` is a file-like object, the filename will be generated from the `name` attribute if available. If `path_or_file` is a path the filename will be generated from the path. | `None` |
| #### `encoding` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_text\(encoding\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The encoding to use when saving the file. If `None`, the encoding will be determined by supplied file-like object (if possible). If this is not possible, 'utf-8' will be used. | `None` |
| #### `mime_type` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_text\(mime_type\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The MIME type of the file or None to guess based on file extension. If no MIME type is supplied and we cannot guess the MIME type, from the file extension, the MIME type will be set to "text/plain". | `None` |
| #### `name` [¶](https://textual.textualize.io/api/app/#textual.app.App.deliver_text\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A user-defined named which will be returned in [`DeliveryComplete`](https://textual.textualize.io/api/events/#textual.events.DeliveryComplete " DeliveryComplete") and [`DeliveryComplete`](https://textual.textualize.io/api/events/#textual.events.DeliveryComplete " DeliveryComplete"). | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The delivery key that uniquely identifies the file delivery. |

### end\_capture\_print [¶](https://textual.textualize.io/api/app/#textual.app.App.end_capture_print "Permanent link")

```
end_capture_print()
```

End capturing of prints.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `target` [¶](https://textual.textualize.io/api/app/#textual.app.App.end_capture_print\(target\) "Permanent link") | `[MessageTarget](https://textual.textualize.io/api/types/#textual.types.MessageTarget " MessageTarget (textual._types.MessageTarget)")` | The widget that was capturing prints. | *required* |

### exit [¶](https://textual.textualize.io/api/app/#textual.app.App.exit "Permanent link")

```
exit(=None, =0, =None)
```

Exit the app, and return the supplied result.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `result` [¶](https://textual.textualize.io/api/app/#textual.app.App.exit\(result\) "Permanent link") | `ReturnType \| None` | Return value. | `None` |
| #### `return_code` [¶](https://textual.textualize.io/api/app/#textual.app.App.exit\(return_code\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The return code. Use non-zero values for error codes. | `0` |
| #### `message` [¶](https://textual.textualize.io/api/app/#textual.app.App.exit\(message\) "Permanent link") | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | Optional message to display on exit. | `None` |

### export\_screenshot [¶](https://textual.textualize.io/api/app/#textual.app.App.export_screenshot "Permanent link")

```
export_screenshot(*, =None, =False)
```

Export an SVG screenshot of the current screen.

See also which writes the screenshot to a file.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `title` [¶](https://textual.textualize.io/api/app/#textual.app.App.export_screenshot\(title\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The title of the exported screenshot or None to use app title. | `None` |
| #### `simplify` [¶](https://textual.textualize.io/api/app/#textual.app.App.export_screenshot\(simplify\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Simplify the segments by combining contiguous segments with the same style. | `False` |

### get\_child\_by\_id [¶](https://textual.textualize.io/api/app/#textual.app.App.get_child_by_id "Permanent link")

```
get_child_by_id(: str) -> Widget
```
```
get_child_by_id(
    : str, : type[ExpectType]
) -> ExpectType
```

```
get_child_by_id(, =None)
```

Get the first child (immediate descendant) of this DOMNode with the given ID.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `id` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_child_by_id\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID of the node to search for. | *required* |
| #### `expect_type` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_child_by_id\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[ExpectType] \| None` | Require the object be of the supplied type, or use `None` to apply no type restriction. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `ExpectType \| [Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | The first child of this node with the specified ID. |

Raises:

| Type | Description |
| --- | --- |
| `[NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches (textual.css.query.NoMatches)")` | If no children could be found for this ID. |
| `[WrongType](https://textual.textualize.io/api/query/#textual.css.query.WrongType " WrongType (textual.css.query.WrongType)")` | If the wrong type was found. |

### get\_child\_by\_type [¶](https://textual.textualize.io/api/app/#textual.app.App.get_child_by_type "Permanent link")

```
get_child_by_type()
```

Get a child of a give type.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `expect_type` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_child_by_type\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[ExpectType]` | The type of the expected child. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches (textual.css.query.NoMatches)")` | If no valid child is found. |

Returns:

| Type | Description |
| --- | --- |
| `ExpectType` | A widget. |

### get\_css\_variables [¶](https://textual.textualize.io/api/app/#textual.app.App.get_css_variables "Permanent link")

```
get_css_variables()
```

Get a mapping of variables used to pre-populate CSS.

May be implemented in a subclass to add new CSS variables.

Returns:

| Type | Description |
| --- | --- |
| `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]` | A mapping of variable name to value. |

### get\_default\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.get_default_screen "Permanent link")

```
get_default_screen()
```

Get the default screen.

This is called when the App is first composed. The returned screen instance will be the first screen on the stack.

Implement this method if you would like to use a custom Screen as the default screen.

Returns:

| Type | Description |
| --- | --- |
| `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")` | A screen instance. |

### get\_driver\_class [¶](https://textual.textualize.io/api/app/#textual.app.App.get_driver_class "Permanent link")

```
get_driver_class()
```

Get a driver class for this platform.

This method is called by the constructor, and unlikely to be required when building a Textual app.

Returns:

| Type | Description |
| --- | --- |
| `[Type](https://docs.python.org/3/library/typing.html#typing.Type "typing.Type")[Driver]` | A Driver class which manages input and display. |

### get\_key\_display [¶](https://textual.textualize.io/api/app/#textual.app.App.get_key_display "Permanent link")

```
get_key_display()
```

Format a bound key for display in footer / key panel etc.

Note

You can implement this in a subclass if you want to change how keys are displayed in your app.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `binding` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_key_display\(binding\) "Permanent link") | `[Binding](https://textual.textualize.io/api/binding/#textual.binding.Binding " Binding (textual.binding.Binding)")` | A Binding. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A string used to represent the key. |

```
get_loading_widget()
```

Get a widget to be used as a loading indicator.

Extend this method if you want to display the loading state a little differently.

Returns:

| Type | Description |
| --- | --- |
| `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A widget to display a loading state. |

### get\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.get_screen "Permanent link")

```
get_screen(: ) ->
```
```
get_screen(: str) -> Screen
```
```
get_screen(
    : str,
    : Type[] | None = None,
) ->
```
```
get_screen(
    : ,
    : Type[] | None = None,
) ->
```

```
get_screen(, =None)
```

Get an installed screen.

Example
```
my_screen = self.get_screen("settings", MyScreen)
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_screen\(screen\) "Permanent link") | `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)") \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | Either a Screen object or screen name (the `name` argument when installed). | *required* |
| #### `screen_class` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_screen\(screen_class\) "Permanent link") | `[Type](https://docs.python.org/3/library/typing.html#typing.Type "typing.Type")[[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")] \| None` | Class of expected screen, or `None` for any screen class. | `None` |

Raises:

| Type | Description |
| --- | --- |
| `[KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)` | If the named screen doesn't exist. |

Returns:

| Type | Description |
| --- | --- |
| `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")` | A screen instance. |

### get\_system\_commands [¶](https://textual.textualize.io/api/app/#textual.app.App.get_system_commands "Permanent link")

```
get_system_commands()
```

A generator of system commands used in the command palette.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_system_commands\(screen\) "Permanent link") | `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")` | The screen where the command palette was invoked from. | *required* |

Implement this method in your App subclass if you want to add custom commands. Here is an example:

```
def get_system_commands(self, screen: Screen) -> Iterable[SystemCommand]:
    yield from super().get_system_commands(screen)
    yield SystemCommand("Bell", "Ring the bell", self.bell)
```

Note

Requires that [`SystemCommandsProvider`](https://textual.textualize.io/api/system_commands_source/#textual.system_commands.SystemCommandsProvider " SystemCommandsProvider") is in `App.COMMANDS` class variable.

Yields:

| Type | Description |
| --- | --- |
| `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[]` | instances. |

### get\_theme [¶](https://textual.textualize.io/api/app/#textual.app.App.get_theme "Permanent link")

```
get_theme()
```

Get a theme by name.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `theme_name` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_theme\(theme_name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The name of the theme to get. May also be a comma separated list of names, to pick the first available theme. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Theme \| None` | A Theme instance and None if the theme doesn't exist. |

### get\_theme\_variable\_defaults [¶](https://textual.textualize.io/api/app/#textual.app.App.get_theme_variable_defaults "Permanent link")

```
get_theme_variable_defaults()
```

Get the default values for the `variables` used in a theme.

If the currently specified theme doesn't define a value for a variable, the value specified here will be used as a fallback.

If a variable is referenced in CSS but does not appear either here or in the theme, the CSS will fail to parse on startup.

This method allows applications to define their own variables, beyond those offered by Textual, which can then be overridden by a Theme.

Returns:

| Type | Description |
| --- | --- |
| `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]` | A mapping of variable name (e.g. "my-button-background-color") to value. |
| `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]` | Values can be any valid CSS value, e.g. "red 50%", "auto 90%", |
| `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]` | "#ff0000", "rgb(255, 0, 0)", etc. |

### get\_widget\_at [¶](https://textual.textualize.io/api/app/#textual.app.App.get_widget_at "Permanent link")

```
get_widget_at(, )
```

Get the widget under the given coordinates.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `x` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_widget_at\(x\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | X coordinate. | *required* |
| #### `y` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_widget_at\(y\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Y coordinate. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)"), [Region](https://textual.textualize.io/api/geometry/#textual.geometry.Region " Region (textual.geometry.Region)")]` | The widget and the widget's screen region. |

### get\_widget\_by\_id [¶](https://textual.textualize.io/api/app/#textual.app.App.get_widget_by_id "Permanent link")

```
get_widget_by_id(: str) -> Widget
```
```
get_widget_by_id(
    : str, : type[ExpectType]
) -> ExpectType
```

```
get_widget_by_id(, =None)
```

Get the first descendant widget with the given ID.

Performs a breadth-first search rooted at the current screen. It will not return the Screen if that matches the ID. To get the screen, use `self.screen`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `id` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_widget_by_id\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The ID to search for in the subtree | *required* |
| #### `expect_type` [¶](https://textual.textualize.io/api/app/#textual.app.App.get_widget_by_id\(expect_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[ExpectType] \| None` | Require the object be of the supplied type, or None for any type. Defaults to None. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `ExpectType \| [Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | The first descendant encountered with this ID. |

Raises:

| Type | Description |
| --- | --- |
| `[NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches (textual.css.query.NoMatches)")` | if no children could be found for this ID |
| `[WrongType](https://textual.textualize.io/api/query/#textual.css.query.WrongType " WrongType (textual.css.query.WrongType)")` | if the wrong type was found. |

### handle\_bindings\_clash [¶](https://textual.textualize.io/api/app/#textual.app.App.handle_bindings_clash "Permanent link")

```
handle_bindings_clash(, )
```

Handle a clash between bindings.

Bindings clashes are likely due to users setting conflicting keys via their keymap.

This method is intended to be overridden by subclasses.

Textual will call this each time a clash is encountered - which may be on each keypress if a clashing widget is focused or is in the bindings chain.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `clashed_bindings` [¶](https://textual.textualize.io/api/app/#textual.app.App.handle_bindings_clash\(clashed_bindings\) "Permanent link") | `[set](https://docs.python.org/3/library/stdtypes.html#set)[[Binding](https://textual.textualize.io/api/binding/#textual.binding.Binding " Binding (textual.binding.Binding)")]` | The bindings that are clashing. | *required* |
| #### `node` [¶](https://textual.textualize.io/api/app/#textual.app.App.handle_bindings_clash\(node\) "Permanent link") | `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)")` | The node that has the clashing bindings. | *required* |

### install\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.install_screen "Permanent link")

```
install_screen(, )
```

Install a screen.

Installing a screen prevents Textual from destroying it when it is no longer on the screen stack. Note that you don't need to install a screen to use it. See or to make a new screen current.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.install_screen\(screen\) "Permanent link") | `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")` | Screen to install. | *required* |
| #### `name` [¶](https://textual.textualize.io/api/app/#textual.app.App.install_screen\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Unique name to identify the screen. | *required* |

Raises:

| Type | Description |
| --- | --- |
|  | If the screen can't be installed. |

Returns:

| Type | Description |
| --- | --- |
| `None` | An awaitable that awaits the mounting of the screen and its children. |

### is\_mounted [¶](https://textual.textualize.io/api/app/#textual.app.App.is_mounted "Permanent link")

```
is_mounted()
```

Check if a widget is mounted.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/app/#textual.app.App.is_mounted\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | A widget. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True of the widget is mounted. |

### is\_screen\_installed [¶](https://textual.textualize.io/api/app/#textual.app.App.is_screen_installed "Permanent link")

```
is_screen_installed()
```

Check if a given screen has been installed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.is_screen_installed\(screen\) "Permanent link") | `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)") \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | Either a Screen object or screen name (the `name` argument when installed). | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the screen is currently installed, |

### mount [¶](https://textual.textualize.io/api/app/#textual.app.App.mount "Permanent link")

```
mount(*, =None, =None)
```

Mount the given widgets relative to the app's screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*widgets` [¶](https://textual.textualize.io/api/app/#textual.app.App.mount\(*widgets\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")` | The widget(s) to mount. | `()` |
| #### `before` [¶](https://textual.textualize.io/api/app/#textual.app.App.mount\(before\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| [Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | Optional location to mount before. An `int` is the index of the child to mount before, a `str` is a `query_one` query to find the widget to mount before. | `None` |
| #### `after` [¶](https://textual.textualize.io/api/app/#textual.app.App.mount\(after\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| [Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | Optional location to mount after. An `int` is the index of the child to mount after, a `str` is a `query_one` query to find the widget to mount after. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitMount](https://textual.textualize.io/api/widget/#textual.widget.AwaitMount " AwaitMount (textual.widget.AwaitMount)")` | An awaitable object that waits for widgets to be mounted. |

Raises:

| Type | Description |
| --- | --- |
| `[MountError](https://textual.textualize.io/api/widget/#textual.widget.MountError " MountError (textual.widget.MountError)")` | If there is a problem with the mount request. |

Note

Only one of `before` or `after` can be provided. If both are provided a `MountError` will be raised.

### mount\_all [¶](https://textual.textualize.io/api/app/#textual.app.App.mount_all "Permanent link")

```
mount_all(, *, =None, =None)
```

Mount widgets from an iterable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widgets` [¶](https://textual.textualize.io/api/app/#textual.app.App.mount_all\(widgets\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")]` | An iterable of widgets. | *required* |
| #### `before` [¶](https://textual.textualize.io/api/app/#textual.app.App.mount_all\(before\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| [Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | Optional location to mount before. An `int` is the index of the child to mount before, a `str` is a `query_one` query to find the widget to mount before. | `None` |
| #### `after` [¶](https://textual.textualize.io/api/app/#textual.app.App.mount_all\(after\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| [str](https://docs.python.org/3/library/stdtypes.html#str) \| [Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | Optional location to mount after. An `int` is the index of the child to mount after, a `str` is a `query_one` query to find the widget to mount after. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitMount](https://textual.textualize.io/api/widget/#textual.widget.AwaitMount " AwaitMount (textual.widget.AwaitMount)")` | An awaitable object that waits for widgets to be mounted. |

Raises:

| Type | Description |
| --- | --- |
| `[MountError](https://textual.textualize.io/api/widget/#textual.widget.MountError " MountError (textual.widget.MountError)")` | If there is a problem with the mount request. |

Note

Only one of `before` or `after` can be provided. If both are provided a `MountError` will be raised.

### notify [¶](https://textual.textualize.io/api/app/#textual.app.App.notify "Permanent link")

```
notify(
    ,
    *,
    ="",
    ="information",
    =None
)
```

Create a notification.

Tip

This method is thread-safe.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `message` [¶](https://textual.textualize.io/api/app/#textual.app.App.notify\(message\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The message for the notification. | *required* |
| #### `title` [¶](https://textual.textualize.io/api/app/#textual.app.App.notify\(title\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The title for the notification. | `''` |
| #### `severity` [¶](https://textual.textualize.io/api/app/#textual.app.App.notify\(severity\) "Permanent link") | `SeverityLevel` | The severity of the notification. | `'information'` |
| #### `timeout` [¶](https://textual.textualize.io/api/app/#textual.app.App.notify\(timeout\) "Permanent link") | `[float](https://docs.python.org/3/library/functions.html#float) \| None` | The timeout (in seconds) for the notification, or `None` for default. | `None` |

The `notify` method is used to create an application-wide notification, shown in a [`Toast`](https://textual.textualize.io/widgets/toast/#textual.widgets._toast.Toast " Toast"), normally originating in the bottom right corner of the display.

Notifications can have the following severity levels:

- `information`
- `warning`
- `error`

The default is `information`.

Example
```
# Show an information notification.
self.notify("It's an older code, sir, but it checks out.")

# Show a warning. Note that Textual's notification system allows
# for the use of Rich console markup.
self.notify(
    "Now witness the firepower of this fully "
    "[b]ARMED[/b] and [i][b]OPERATIONAL[/b][/i] battle station!",
    title="Possible trap detected",
    severity="warning",
)

# Show an error. Set a longer timeout so it's noticed.
self.notify("It's a trap!", severity="error", timeout=10)

# Show an information notification, but without any sort of title.
self.notify("It's against my programming to impersonate a deity.", title="")
```

### open\_url [¶](https://textual.textualize.io/api/app/#textual.app.App.open_url "Permanent link")

```
open_url(, *, =True)
```

Open a URL in the default web browser.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `url` [¶](https://textual.textualize.io/api/app/#textual.app.App.open_url\(url\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The URL to open. | *required* |
| #### `new_tab` [¶](https://textual.textualize.io/api/app/#textual.app.App.open_url\(new_tab\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to open the URL in a new tab. | `True` |

### panic [¶](https://textual.textualize.io/api/app/#textual.app.App.panic "Permanent link")

```
panic(*)
```

Exits the app and display error message(s).

Used in response to unexpected errors. For a more graceful exit, see the method.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `*renderables` [¶](https://textual.textualize.io/api/app/#textual.app.App.panic\(*renderables\) "Permanent link") | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType")` | Text or Rich renderable(s) to display on exit. | `()` |

### pop\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.pop_screen "Permanent link")

```
pop_screen()
```

Pop the current [screen](https://textual.textualize.io/guide/screens) from the stack, and switch to the previous screen.

Returns:

| Type | Description |
| --- | --- |
| `[AwaitComplete](https://textual.textualize.io/api/await_complete/#textual.await_complete.AwaitComplete " AwaitComplete (textual.await_complete.AwaitComplete)")` | The screen that was replaced. |

### post\_display\_hook [¶](https://textual.textualize.io/api/app/#textual.app.App.post_display_hook "Permanent link")

```
post_display_hook()
```

Called immediately after a display is done. Used in tests.

### push\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.push_screen "Permanent link")

```
push_screen(
    : Screen[ScreenResultType] | str,
    : (
        ScreenResultCallbackType[ScreenResultType] | None
    ) = None,
    : Literal[False] = False,
) -> AwaitMount
```
```
push_screen(
    : Screen[ScreenResultType] | str,
    : (
        ScreenResultCallbackType[ScreenResultType] | None
    ) = None,
    : Literal[True] = True,
) -> Future[ScreenResultType]
```

```
push_screen(, =None, =False)
```

Push a new [screen](https://textual.textualize.io/guide/screens) on the screen stack, making it the current screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.push_screen\(screen\) "Permanent link") | `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")[[ScreenResultType](https://textual.textualize.io/api/screen/#textual.screen.ScreenResultType " ScreenResultType (textual.screen.ScreenResultType)")] \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | A Screen instance or the name of an installed screen. | *required* |
| #### `callback` [¶](https://textual.textualize.io/api/app/#textual.app.App.push_screen\(callback\) "Permanent link") | `[ScreenResultCallbackType](https://textual.textualize.io/api/screen/#textual.screen.ScreenResultCallbackType " ScreenResultCallbackType (textual.screen.ScreenResultCallbackType)")[[ScreenResultType](https://textual.textualize.io/api/screen/#textual.screen.ScreenResultType " ScreenResultType (textual.screen.ScreenResultType)")] \| None` | An optional callback function that will be called if the screen is [dismissed](https://textual.textualize.io/api/screen/#textual.screen.Screen.dismiss " dismiss") with a result. | `None` |
| #### `wait_for_dismiss` [¶](https://textual.textualize.io/api/app/#textual.app.App.push_screen\(wait_for_dismiss\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `True`, awaiting this method will return the dismiss value from the screen. When set to `False`, awaiting this method will wait for the screen to be mounted. Note that `wait_for_dismiss` should only be set to `True` when running in a worker. | `False` |

Raises:

| Type | Description |
| --- | --- |
| `[NoActiveWorker](https://textual.textualize.io/api/worker/#textual.worker.NoActiveWorker " NoActiveWorker (textual.worker.NoActiveWorker)")` | If using `wait_for_dismiss` outside of a worker. |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitMount](https://textual.textualize.io/api/widget/#textual.widget.AwaitMount " AwaitMount (textual.widget.AwaitMount)") \| [Future](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")[[ScreenResultType](https://textual.textualize.io/api/screen/#textual.screen.ScreenResultType " ScreenResultType (textual.screen.ScreenResultType)")]` | An optional awaitable that awaits the mounting of the screen and its children, or an asyncio Future to await the result of the screen. |

### push\_screen\_wait [¶](https://textual.textualize.io/api/app/#textual.app.App.push_screen_wait "Permanent link")

```
push_screen_wait(
    : Screen[ScreenResultType],
) -> ScreenResultType
```
```
push_screen_wait(: str) -> Any
```

```
push_screen_wait()
```

Push a screen and wait for the result (received from [`Screen.dismiss`](https://textual.textualize.io/api/screen/#textual.screen.Screen.dismiss " dismiss")).

Note that this method may only be called when running in a worker.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.push_screen_wait\(screen\) "Permanent link") | `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)")[[ScreenResultType](https://textual.textualize.io/api/screen/#textual.screen.ScreenResultType " ScreenResultType (textual.screen.ScreenResultType)")] \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | A screen or the name of an installed screen. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[ScreenResultType](https://textual.textualize.io/api/screen/#textual.screen.ScreenResultType " ScreenResultType (textual.screen.ScreenResultType)") \| [Any](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` | The screen's result. |

### recompose [¶](https://textual.textualize.io/api/app/#textual.app.App.recompose "Permanent link")

```
recompose()
```

Recompose the widget.

Recomposing will remove children and call `self.compose` again to remount.

### refresh [¶](https://textual.textualize.io/api/app/#textual.app.App.refresh "Permanent link")

```
refresh(*, =True, =False, =False)
```

Refresh the entire screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `repaint` [¶](https://textual.textualize.io/api/app/#textual.app.App.refresh\(repaint\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Repaint the widget (will call render() again). | `True` |
| #### `layout` [¶](https://textual.textualize.io/api/app/#textual.app.App.refresh\(layout\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Also layout widgets in the view. | `False` |
| #### `recompose` [¶](https://textual.textualize.io/api/app/#textual.app.App.refresh\(recompose\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Re-compose the widget (will remove and re-mount children). | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Self` | The `App` instance. |

### refresh\_css [¶](https://textual.textualize.io/api/app/#textual.app.App.refresh_css "Permanent link")

```
refresh_css(=True)
```

Refresh CSS.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `animate` [¶](https://textual.textualize.io/api/app/#textual.app.App.refresh_css\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Also execute CSS animations. | `True` |

```
register_theme()
```

Register a theme with the app.

If the theme already exists, it will be overridden.

After registering a theme, you can activate it by setting the `App.theme` attribute. To retrieve a registered theme, use the `App.get_theme` method.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  | `Theme` | The theme to register. | *required* |

### remove\_mode [¶](https://textual.textualize.io/api/app/#textual.app.App.remove_mode "Permanent link")

```
remove_mode()
```

Removes a mode from the app.

Screens that are running in the stack of that mode are scheduled for pruning.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `mode` [¶](https://textual.textualize.io/api/app/#textual.app.App.remove_mode\(mode\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The mode to remove. It can't be the active mode. | *required* |

Raises:

| Type | Description |
| --- | --- |
|  | If trying to remove the active mode. |
|  | If trying to remove an unknown mode. |

### render [¶](https://textual.textualize.io/api/app/#textual.app.App.render "Permanent link")

```
render()
```

Render method, inherited from widget, to render the screen's background.

May be overridden to customize background visuals.

### run [¶](https://textual.textualize.io/api/app/#textual.app.App.run "Permanent link")

```
run(
    *,
    =False,
    =False,
    =False,
    =True,
    =None,
    =None
)
```

Run the app.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `headless` [¶](https://textual.textualize.io/api/app/#textual.app.App.run\(headless\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Run in headless mode (no output). | `False` |
| #### `inline` [¶](https://textual.textualize.io/api/app/#textual.app.App.run\(inline\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Run the app inline (under the prompt). | `False` |
| #### `inline_no_clear` [¶](https://textual.textualize.io/api/app/#textual.app.App.run\(inline_no_clear\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Don't clear the app output when exiting an inline app. | `False` |
| #### `mouse` [¶](https://textual.textualize.io/api/app/#textual.app.App.run\(mouse\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable mouse support. | `True` |
| #### `size` [¶](https://textual.textualize.io/api/app/#textual.app.App.run\(size\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)] \| None` | Force terminal size to `(WIDTH, HEIGHT)`, or None to auto-detect. | `None` |
| #### `auto_pilot` [¶](https://textual.textualize.io/api/app/#textual.app.App.run\(auto_pilot\) "Permanent link") | ` \| None` | An auto pilot coroutine. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `ReturnType \| None` | App return value. |

### run\_action [¶](https://textual.textualize.io/api/app/#textual.app.App.run_action "Permanent link")

```
run_action(, =None)
```

Perform an [action](https://textual.textualize.io/guide/actions).

Actions are typically associated with key bindings, where you wouldn't need to call this method manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `action` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_action\(action\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| [ActionParseResult](https://textual.textualize.io/api/types/#textual.types.ActionParseResult " ActionParseResult (textual.actions.ActionParseResult)")` | Action encoded in a string. | *required* |
| #### `default_namespace` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_action\(default_namespace\) "Permanent link") | `[DOMNode](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode " DOMNode (textual.dom.DOMNode)") \| None` | Namespace to use if not provided in the action, or None to use app. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the event has been handled. |

### run\_async [¶](https://textual.textualize.io/api/app/#textual.app.App.run_async "Permanent link")

```
run_async(
    *,
    =False,
    =False,
    =False,
    =True,
    =None,
    =None
)
```

Run the app asynchronously.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `headless` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_async\(headless\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Run in headless mode (no output). | `False` |
| #### `inline` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_async\(inline\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Run the app inline (under the prompt). | `False` |
| #### `inline_no_clear` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_async\(inline_no_clear\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Don't clear the app output when exiting an inline app. | `False` |
| #### `mouse` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_async\(mouse\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable mouse support. | `True` |
| #### `size` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_async\(size\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)] \| None` | Force terminal size to `(WIDTH, HEIGHT)`, or None to auto-detect. | `None` |
| #### `auto_pilot` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_async\(auto_pilot\) "Permanent link") | ` \| None` | An autopilot coroutine. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `ReturnType \| None` | App return value. |

### run\_test [¶](https://textual.textualize.io/api/app/#textual.app.App.run_test "Permanent link")

```
run_test(
    *,
    =True,
    =(80, 24),
    =False,
    =False,
    =None
)
```

An asynchronous context manager for testing apps.

Tip

See the guide for [testing](https://textual.textualize.io/guide/testing) Textual apps.

Use this to run your app in "headless" mode (no output) and drive the app via a [Pilot](https://textual.textualize.io/api/pilot/#textual.pilot.Pilot " Pilot") object.

Example:

```
\`\`\`python
async with app.run_test() as pilot:
    await pilot.click("#Button.ok")
    assert ...
\`\`\`
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `headless` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_test\(headless\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Run in headless mode (no output or input). | `True` |
| #### `size` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_test\(size\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)] \| None` | Force terminal size to `(WIDTH, HEIGHT)`, or None to auto-detect. | `(80, 24)` |
|  | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable tooltips when testing. | `False` |
| #### `notifications` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_test\(notifications\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable notifications when testing. | `False` |
| #### `message_hook` [¶](https://textual.textualize.io/api/app/#textual.app.App.run_test\(message_hook\) "Permanent link") | `[Callable](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")], None] \| None` | An optional callback that will be called each time any message arrives at any message pump in the app. | `None` |

### save\_screenshot [¶](https://textual.textualize.io/api/app/#textual.app.App.save_screenshot "Permanent link")

```
save_screenshot(=None, =None, =None)
```

Save an SVG screenshot of the current screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `filename` [¶](https://textual.textualize.io/api/app/#textual.app.App.save_screenshot\(filename\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Filename of SVG screenshot, or None to auto-generate a filename with the date and time. | `None` |
| #### `path` [¶](https://textual.textualize.io/api/app/#textual.app.App.save_screenshot\(path\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Path to directory for output. Defaults to current working directory. | `None` |
| #### `time_format` [¶](https://textual.textualize.io/api/app/#textual.app.App.save_screenshot\(time_format\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Date and time format to use if filename is None. Defaults to a format like ISO 8601 with some reserved characters replaced with underscores. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Filename of screenshot. |

### search\_commands [¶](https://textual.textualize.io/api/app/#textual.app.App.search_commands "Permanent link")

```
search_commands(
    , ="Search for commands…"
)
```

Show a list of commands in the app.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `commands` [¶](https://textual.textualize.io/api/app/#textual.app.App.search_commands\(commands\) "Permanent link") | `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")[CommandListItem]` | A list of SimpleCommand instances. | *required* |
| #### `placeholder` [¶](https://textual.textualize.io/api/app/#textual.app.App.search_commands\(placeholder\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Placeholder text for the search field. | `'Search for commands…'` |

Returns:

| Name | Type | Description |
| --- | --- | --- |
| `AwaitMount` | `[AwaitMount](https://textual.textualize.io/api/widget/#textual.widget.AwaitMount " AwaitMount (textual.widget.AwaitMount)")` | An awaitable that resolves when the commands are shown. |

### search\_themes [¶](https://textual.textualize.io/api/app/#textual.app.App.search_themes "Permanent link")

```
search_themes()
```

Show a fuzzy search command palette containing all registered themes.

Selecting a theme in the list will change the app's theme.

### set\_focus [¶](https://textual.textualize.io/api/app/#textual.app.App.set_focus "Permanent link")

```
set_focus(, =True)
```

Focus (or unfocus) a widget. A focused widget will receive key events first.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `widget` [¶](https://textual.textualize.io/api/app/#textual.app.App.set_focus\(widget\) "Permanent link") | `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)") \| None` | Widget to focus. | *required* |
| #### `scroll_visible` [¶](https://textual.textualize.io/api/app/#textual.app.App.set_focus\(scroll_visible\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Scroll widget into view. | `True` |

### set\_keymap [¶](https://textual.textualize.io/api/app/#textual.app.App.set_keymap "Permanent link")

```
set_keymap()
```

Set the keymap, a mapping of binding IDs to key strings.

Bindings in the keymap are used to override default key bindings, i.e. those defined in `BINDINGS` class variables.

Bindings with IDs that are present in the keymap will have their key string replaced with the value from the keymap.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `keymap` [¶](https://textual.textualize.io/api/app/#textual.app.App.set_keymap\(keymap\) "Permanent link") | `[Keymap](https://textual.textualize.io/api/binding/#textual.binding.Keymap " Keymap (textual.binding.Keymap)")` | A mapping of binding IDs to key strings. | *required* |

### simulate\_key [¶](https://textual.textualize.io/api/app/#textual.app.App.simulate_key "Permanent link")

```
simulate_key()
```

Simulate a key press.

This will perform the same action as if the user had pressed the key.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `key` [¶](https://textual.textualize.io/api/app/#textual.app.App.simulate_key\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Key to simulate. May also be the name of a key, e.g. "space". | *required* |

### stop\_animation [¶](https://textual.textualize.io/api/app/#textual.app.App.stop_animation "Permanent link")

```
stop_animation(, =True)
```

Stop an animation on an attribute.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `attribute` [¶](https://textual.textualize.io/api/app/#textual.app.App.stop_animation\(attribute\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Name of the attribute whose animation should be stopped. | *required* |
| #### `complete` [¶](https://textual.textualize.io/api/app/#textual.app.App.stop_animation\(complete\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Should the animation be set to its final value? | `True` |

Note

If there is no animation scheduled or running, this is a no-op.

### suspend [¶](https://textual.textualize.io/api/app/#textual.app.App.suspend "Permanent link")

```
suspend()
```

A context manager that temporarily suspends the app.

While inside the `with` block, the app will stop reading input and emitting output. Other applications will have full control of the terminal, configured as it was before the app started running. When the `with` block ends, the application will start reading input and emitting output again.

Example
```
with self.suspend():
    os.system("emacs -nw")
```

Raises:

| Type | Description |
| --- | --- |
|  | If the environment doesn't support suspending. |

Note

Suspending the application is currently only supported on Unix-like operating systems and Microsoft Windows. Suspending is not supported in Textual Web.

### switch\_mode [¶](https://textual.textualize.io/api/app/#textual.app.App.switch_mode "Permanent link")

```
switch_mode()
```

Switch to a given mode.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `mode` [¶](https://textual.textualize.io/api/app/#textual.app.App.switch_mode\(mode\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The mode to switch to. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[AwaitMount](https://textual.textualize.io/api/widget/#textual.widget.AwaitMount " AwaitMount (textual.widget.AwaitMount)")` | An optionally awaitable object which waits for the screen associated with the mode to be mounted. |

Raises:

| Type | Description |
| --- | --- |
|  | If trying to switch to an unknown mode. |

### switch\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.switch_screen "Permanent link")

```
switch_screen()
```

Switch to another [screen](https://textual.textualize.io/guide/screens) by replacing the top of the screen stack with a new screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.switch_screen\(screen\) "Permanent link") | `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)") \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | Either a Screen object or screen name (the `name` argument when installed). | *required* |

### uninstall\_screen [¶](https://textual.textualize.io/api/app/#textual.app.App.uninstall_screen "Permanent link")

```
uninstall_screen()
```

Uninstall a screen.

If the screen was not previously installed, then this method is a null-op. Uninstalling a screen allows Textual to delete it when it is popped or switched. Note that uninstalling a screen is only required if you have previously installed it with . Textual will also uninstall screens automatically on exit.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `screen` [¶](https://textual.textualize.io/api/app/#textual.app.App.uninstall_screen\(screen\) "Permanent link") | `[Screen](https://textual.textualize.io/api/screen/#textual.screen.Screen " Screen (textual.screen.Screen)") \| [str](https://docs.python.org/3/library/stdtypes.html#str)` | The screen to uninstall or the name of an installed screen. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the screen that was uninstalled, or None if no screen was uninstalled. |

```
unregister_theme()
```

Unregister a theme with the app.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The name of the theme to unregister. | *required* |

### update\_keymap [¶](https://textual.textualize.io/api/app/#textual.app.App.update_keymap "Permanent link")

```
update_keymap()
```

Update the App's keymap, merging with `keymap`.

If a Binding ID exists in both the App's keymap and the `keymap` argument, the `keymap` argument takes precedence.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `keymap` [¶](https://textual.textualize.io/api/app/#textual.app.App.update_keymap\(keymap\) "Permanent link") | `[Keymap](https://textual.textualize.io/api/binding/#textual.binding.Keymap " Keymap (textual.binding.Keymap)")` | A mapping of binding IDs to key strings. | *required* |

### update\_styles [¶](https://textual.textualize.io/api/app/#textual.app.App.update_styles "Permanent link")

```
update_styles(node)
```

Immediately update the styles of this node and all descendant nodes.

Should be called whenever CSS classes / pseudo classes change. For example, when you hover over a button, the :hover pseudo class will be added, and this method is called to apply the corresponding :hover styles.

### validate\_sub\_title [¶](https://textual.textualize.io/api/app/#textual.app.App.validate_sub_title "Permanent link")

```
validate_sub_title(sub_title)
```

Make sure the subtitle is set to a string.

### validate\_title [¶](https://textual.textualize.io/api/app/#textual.app.App.validate_title "Permanent link")

```
validate_title(title)
```

Make sure the title is set to a string.

## AppError [¶](https://textual.textualize.io/api/app/#textual.app.AppError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Base class for general App related exceptions.

## InvalidModeError [¶](https://textual.textualize.io/api/app/#textual.app.InvalidModeError "Permanent link")

Bases:

Raised if there is an issue with a mode name.

## InvalidThemeError [¶](https://textual.textualize.io/api/app/#textual.app.InvalidThemeError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when an invalid theme is set.

## ModeError [¶](https://textual.textualize.io/api/app/#textual.app.ModeError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Base class for exceptions related to modes.

## ScreenError [¶](https://textual.textualize.io/api/app/#textual.app.ScreenError "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Base class for exceptions that relate to screens.

## ScreenStackError [¶](https://textual.textualize.io/api/app/#textual.app.ScreenStackError "Permanent link")

Bases:

Raised when trying to manipulate the screen stack incorrectly.

## SuspendNotSupported [¶](https://textual.textualize.io/api/app/#textual.app.SuspendNotSupported "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised if suspending the application is not supported.

This exception is raised if is called while the application is running in an environment where this isn't supported.

## SystemCommand [¶](https://textual.textualize.io/api/app/#textual.app.SystemCommand "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

Defines a system command used in the command palette (yielded from ).

### callback [¶](https://textual.textualize.io/api/app/#textual.app.SystemCommand.callback "Permanent link")

```
callback
```

A callback to invoke when the command is selected.

### discover [¶](https://textual.textualize.io/api/app/#textual.app.SystemCommand.discover "Permanent link")

```
discover = True
```

Should the command show when the search is empty?

### help [¶](https://textual.textualize.io/api/app/#textual.app.SystemCommand.help "Permanent link")

```
help
```

Additional help text, shown under the title.

### title [¶](https://textual.textualize.io/api/app/#textual.app.SystemCommand.title "Permanent link")

```
title
```

The title of the command (used in search).

## UnknownModeError [¶](https://textual.textualize.io/api/app/#textual.app.UnknownModeError "Permanent link")

Bases:

Raised when attempting to use a mode that is not known.

## get\_system\_commands\_provider [¶](https://textual.textualize.io/api/app/#textual.app.get_system_commands_provider "Permanent link")

```
get_system_commands_provider()
```

Callable to lazy load the system commands.

Returns:

| Type | Description |
| --- | --- |
| `[type](https://docs.python.org/3/library/functions.html#type)[[SystemCommandsProvider](https://textual.textualize.io/api/system_commands_source/#textual.system_commands.SystemCommandsProvider " SystemCommandsProvider (textual.system_commands.SystemCommandsProvider)")]` | System commands class. |