---
title: "Textual - Input"
source: "https://textual.textualize.io/widgets/input/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Input¶

A single-line text input widget.

- Focusable
- Container

## Examples¶

### A Simple Example¶

The example below shows how you might create a simple form using two `Input` widgets.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Input

class InputApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="First Name")
        yield Input(placeholder="Last Name")

if __name__ == "__main__":
    app = InputApp()
    app.run()
```

### Input Types¶

The `Input` widget supports a `type` parameter which will prevent the user from typing invalid characters. You can set `type` to any of the following values:

| input.type | Description |
| --- | --- |
| `"integer"` | Restricts input to integers. |
| `"number"` | Restricts input to a floating point number. |
| `"text"` | Allow all text (no restrictions). |

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Input

class InputApp(App):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="An integer", type="integer")
        yield Input(placeholder="A number", type="number")

if __name__ == "__main__":
    app = InputApp()
    app.run()
```

If you set `type` to something other than `"text"`, then the `Input` will apply the appropriate [validator](https://textual.textualize.io/widgets/input/#validating-input).

### Restricting Input¶

You can limit input to particular characters by supplying the `restrict` parameter, which should be a regular expression. The `Input` widget will prevent the addition of any characters that would cause the regex to no longer match. For instance, if you wanted to limit characters to binary you could set `restrict=r"[01]*"`.

Note

The `restrict` regular expression is applied to the full value and not just to the new character.

### Maximum Length¶

You can limit the length of the input by setting `max_length` to a value greater than zero. This will prevent the user from typing any more characters when the maximum has been reached.

### Validating Input¶

You can supply one or more *[validators](https://textual.textualize.io/api/validation/#textual.validation.Validator " Validator")* to the `Input` widget to validate the value.

All the supplied validators will run when the value changes, the `Input` is submitted, or focus moves *out* of the `Input`. The values `"changed"`, `"submitted"`, and `"blur"`, can be passed as an iterable to the `Input` parameter `validate_on` to request that validation occur only on the respective mesages. (See [`InputValidationOn`](https://textual.textualize.io/api/types/#textual.types.InputValidationOn " InputValidationOn") and .) For example, the code below creates an `Input` widget that only gets validated when the value is submitted explicitly:

```
input = Input(validate_on=["submitted"])
```

Validation is considered to have failed if *any* of the validators fail.

You can check whether the validation succeeded or failed inside an or handler by looking at the `validation_result` attribute on these events.

In the example below, we show how to combine multiple validators and update the UI to tell the user why validation failed. Click the tabs to see the output for validation failures and successes.

```
from textual import on
from textual.app import App, ComposeResult
from textual.validation import Function, Number, ValidationResult, Validator
from textual.widgets import Input, Label, Pretty

class InputApp(App):
    
    CSS = """
    Input.-valid {
        border: tall $success 60%;
    }
    Input.-valid:focus {
        border: tall $success;
    }
    Input {
        margin: 1 1;
    }
    Label {
        margin: 1 2;
    }
    Pretty {
        margin: 1 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Enter an even number between 1 and 100 that is also a palindrome.")
        yield Input(
            placeholder="Enter a number...",
            validators=[
                Number(minimum=1, maximum=100),  
                Function(is_even, "Value is not even."),  
                Palindrome(),  
            ],
        )
        yield Pretty([])

    @on(Input.Changed)
    def show_invalid_reasons(self, event: Input.Changed) -> None:
        # Updating the UI to show the reasons why validation failed
        if not event.validation_result.is_valid:  
            self.query_one(Pretty).update(event.validation_result.failure_descriptions)
        else:
            self.query_one(Pretty).update([])

def is_even(value: str) -> bool:
    try:
        return int(value) % 2 == 0
    except ValueError:
        return False

# A custom validator
class Palindrome(Validator):  
    def validate(self, value: str) -> ValidationResult:
        """Check a string is equal to its reverse."""
        if self.is_palindrome(value):
            return self.success()
        else:
            return self.failure("That's not a palindrome :/")

    @staticmethod
    def is_palindrome(value: str) -> bool:
        return value == value[::-1]

app = InputApp()

if __name__ == "__main__":
    app.run()
```

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

Textual offers several [built-in validators](https://textual.textualize.io/api/validation/#textual.validation " validation") for common requirements, but you can easily roll your own by extending [Validator](https://textual.textualize.io/api/validation/#textual.validation.Validator " Validator"), as seen for `Palindrome` in the example above.

#### Validate Empty¶

If you set `valid_empty=True` then empty values will bypass any validators, and empty values will be considered valid.

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `cursor_blink` | `bool` | `True` | True if cursor blinking is enabled. |
| `value` | `str` | `""` | The value currently in the text input. |
| `cursor_position` | `int` | `0` | The index of the cursor in the value string. |
| `placeholder` | `str` | `""` | The dimmed placeholder text to display when the input is empty. |
| `password` | `bool` | `False` | True if the input should be masked. |
| `restrict` | `str` | `None` | Optional regular expression to restrict input. |
| `type` | `str` | `"text"` | The type of the input. |
| `max_length` | `int` | `None` | Maximum length of the input value. |
| `valid_empty` | `bool` | `False` | Allow empty values to bypass validation. |

## Messages¶

## Bindings¶

The input widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| left | Move the cursor left. |
| shift+left | Move cursor left and select. |
| ctrl+left | Move the cursor one word to the left. |
| right | Move the cursor right or accept the completion suggestion. |
| ctrl+shift+left | Move cursor left a word and select. |
| shift+right | Move cursor right and select. |
| ctrl+right | Move the cursor one word to the right. |
| backspace | Delete the character to the left of the cursor. |
| ctrl+shift+right | Move cursor right a word and select. |
| home,ctrl+a | Go to the beginning of the input. |
| end,ctrl+e | Go to the end of the input. |
| shift+home | Select up to the input start. |
| shift+end | Select up to the input end. |
| delete,ctrl+d | Delete the character to the right of the cursor. |
| enter | Submit the current value of the input. |
| ctrl+w | Delete the word to the left of the cursor. |
| ctrl+u | Delete everything to the left of the cursor. |
| ctrl+f | Delete the word to the right of the cursor. |
| ctrl+k | Delete everything to the right of the cursor. |
| ctrl+x | Cut selected text. |
| ctrl+c | Copy selected text. |
| ctrl+v | Paste text from the clipboard. |

## Component Classes¶

The input widget provides the following component classes:

| Class | Description |
| --- | --- |
| `input--cursor` | Target the cursor. |
| `input--placeholder` | Target the placeholder text (when it exists). |
| `input--suggestion` | Target the auto-completion suggestion (when it exists). |
| `input--selection` | Target the selected text. |

## Additional Notes¶

- The spacing around the text content is due to border. To remove it, set `border: none;` in your CSS.

---

Bases: `[ScrollView](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView " ScrollView (textual.scroll_view.ScrollView)")`

A text input widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `value` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An optional default value for the input. | `None` |
| ## `placeholder` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(placeholder\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Optional placeholder text for the input. | `''` |
| ## `highlighter` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(highlighter\) "Permanent link") | `[Highlighter](https://rich.readthedocs.io/en/stable/reference/highlighter.html#rich.highlighter.Highlighter "rich.highlighter.Highlighter") \| None` | An optional highlighter for the input. | `None` |
| ## `password` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(password\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Flag to say if the field should obfuscate its content. | `False` |
| ## `restrict` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(restrict\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A regex to restrict character inputs. | `None` |
| ## `type` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(type\) "Permanent link") | `InputType` | The type of the input. | `'text'` |
| ## `max_length` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(max_length\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The maximum length of the input, or 0 for no maximum length. | `0` |
| ## `suggester` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(suggester\) "Permanent link") | `[Suggester](https://textual.textualize.io/api/suggester/#textual.suggester.Suggester " Suggester (textual.suggester.Suggester)") \| None` | [`Suggester`](https://textual.textualize.io/api/suggester/#textual.suggester.Suggester " Suggester") associated with this input instance. | `None` |
| ## `validators` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(validators\) "Permanent link") | `[Validator](https://textual.textualize.io/api/validation/#textual.validation.Validator " Validator (textual.validation.Validator)") \| [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[Validator](https://textual.textualize.io/api/validation/#textual.validation.Validator " Validator (textual.validation.Validator)")] \| None` | An iterable of validators that the Input value will be checked against. | `None` |
| ## `validate_on` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(validate_on\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[InputValidationOn](https://textual.textualize.io/api/types/#textual.types.InputValidationOn " InputValidationOn (textual.widgets._input.InputValidationOn)")] \| None` | Zero or more of the values "blur", "changed", and "submitted", which determine when to do input validation. The default is to do validation for all messages. | `None` |
| ## `valid_empty` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(valid_empty\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Empty values are valid. | `False` |
| ## `select_on_focus` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(select_on_focus\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to select all text on focus. | `True` |
| ## `name` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional name for the input widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional ID for the widget. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional initial classes for the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the input is disabled or not. | `False` |
|  | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | Optional tooltip. | `None` |

## BINDINGS [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding(
        "left",
        "cursor_left",
        "Move cursor left",
        show=False,
    ),
    Binding(
        "shift+left",
        "cursor_left(True)",
        "Move cursor left and select",
        show=False,
    ),
    Binding(
        "ctrl+left",
        "cursor_left_word",
        "Move cursor left a word",
        show=False,
    ),
    Binding(
        "ctrl+shift+left",
        "cursor_left_word(True)",
        "Move cursor left a word and select",
        show=False,
    ),
    Binding(
        "right",
        "cursor_right",
        "Move cursor right or accept the completion suggestion",
        show=False,
    ),
    Binding(
        "shift+right",
        "cursor_right(True)",
        "Move cursor right and select",
        show=False,
    ),
    Binding(
        "ctrl+right",
        "cursor_right_word",
        "Move cursor right a word",
        show=False,
    ),
    Binding(
        "ctrl+shift+right",
        "cursor_right_word(True)",
        "Move cursor right a word and select",
        show=False,
    ),
    Binding(
        "backspace",
        "delete_left",
        "Delete character left",
        show=False,
    ),
    Binding(
        "home,ctrl+a", "home", "Go to start", show=False
    ),
    Binding("end,ctrl+e", "end", "Go to end", show=False),
    Binding(
        "shift+home",
        "home(True)",
        "Select line start",
        show=False,
    ),
    Binding(
        "shift+end",
        "end(True)",
        "Select line end",
        show=False,
    ),
    Binding(
        "delete,ctrl+d",
        "delete_right",
        "Delete character right",
        show=False,
    ),
    Binding("enter", "submit", "Submit", show=False),
    Binding(
        "ctrl+w",
        "delete_left_word",
        "Delete left to start of word",
        show=False,
    ),
    Binding(
        "ctrl+u",
        "delete_left_all",
        "Delete all to the left",
        show=False,
    ),
    Binding(
        "ctrl+f",
        "delete_right_word",
        "Delete right to start of word",
        show=False,
    ),
    Binding(
        "ctrl+k",
        "delete_right_all",
        "Delete all to the right",
        show=False,
    ),
    Binding(
        "ctrl+x", "cut", "Cut selected text", show=False
    ),
    Binding(
        "ctrl+c", "copy", "Copy selected text", show=False
    ),
    Binding(
        "ctrl+v",
        "paste",
        "Paste text from the clipboard",
        show=False,
    ),
]
```

| Key(s) | Description |
| --- | --- |
| left | Move the cursor left. |
| shift+left | Move cursor left and select. |
| ctrl+left | Move the cursor one word to the left. |
| right | Move the cursor right or accept the completion suggestion. |
| ctrl+shift+left | Move cursor left a word and select. |
| shift+right | Move cursor right and select. |
| ctrl+right | Move the cursor one word to the right. |
| backspace | Delete the character to the left of the cursor. |
| ctrl+shift+right | Move cursor right a word and select. |
| home,ctrl+a | Go to the beginning of the input. |
| end,ctrl+e | Go to the end of the input. |
| shift+home | Select up to the input start. |
| shift+end | Select up to the input end. |
| delete,ctrl+d | Delete the character to the right of the cursor. |
| enter | Submit the current value of the input. |
| ctrl+w | Delete the word to the left of the cursor. |
| ctrl+u | Delete everything to the left of the cursor. |
| ctrl+f | Delete the word to the right of the cursor. |
| ctrl+k | Delete everything to the right of the cursor. |
| ctrl+x | Cut selected text. |
| ctrl+c | Copy selected text. |
| ctrl+v | Paste text from the clipboard. |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {
    "input--cursor",
    "input--placeholder",
    "input--suggestion",
    "input--selection",
}
```

| Class | Description |
| --- | --- |
| `input--cursor` | Target the cursor. |
| `input--placeholder` | Target the placeholder text (when it exists). |
| `input--suggestion` | Target the auto-completion suggestion (when it exists). |
| `input--selection` | Target the selected text. |

## content\_width [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.content_width "Permanent link")

```
content_width
```

The width of the content.

## cursor\_position [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.cursor_position "Permanent link")

```
cursor_position
```

The current position of the cursor, corresponding to the end of the selection.

## cursor\_screen\_offset [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.cursor_screen_offset "Permanent link")

```
cursor_screen_offset
```

The offset of the cursor of this input in screen-space. (x, y)/(column, row)

## is\_valid [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.is_valid "Permanent link")

```
is_valid
```

Check if the value has passed validation.

## max\_length [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.max_length "Permanent link")

```
max_length =
```

The maximum length of the input, in characters.

## restrict [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.restrict "Permanent link")

```
restrict =
```

A regular expression to limit changes in value.

## selected\_text [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.selected_text "Permanent link")

```
selected_text
```

The text between the start and end points of the current selection.

## selection [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.selection "Permanent link")

```
selection = reactive(cursor(0))
```

The currently selected range of text.

## suggester [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.suggester "Permanent link")

```
suggester =
```

The suggester used to provide completions as the user types.

## type [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.type "Permanent link")

```
type =
```

The type of the input.

## valid\_empty [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.valid_empty "Permanent link")

```
valid_empty = var(False)
```

Empty values should pass validation.

## validate\_on [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.validate_on "Permanent link")

```
validate_on = (
    _POSSIBLE_VALIDATE_ON_VALUES & set()
    if  is not None
    else _POSSIBLE_VALIDATE_ON_VALUES
)
```

Set with event names to do input validation on.

Validation can only be performed on blur, on input changes and on input submission.

Example

This creates an `Input` widget that only gets validated when the value is submitted explicitly:

```
input = Input(validate_on=["submitted"])
```

## Blurred [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Blurred "Permanent link")

```
Blurred(input, value, validation_result=None)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when the widget is blurred (loses focus).

Can be handled using `on_input_blurred` in a subclass of `Input` or in a parent widget in the DOM.

### control [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Blurred.control "Permanent link")

```
control
```

Alias for self.input.

### input [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Blurred.input "Permanent link")

```
input
```

The `Input` widget that was changed.

### validation\_result [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Blurred.validation_result "Permanent link")

```
validation_result = None
```

The result of validating the value (formed by combining the results from each validator), or None if validation was not performed (for example when no validators are specified in the `Input`s init)

### value [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Blurred.value "Permanent link")

```
value
```

The value that the input was changed to.

## Changed [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Changed "Permanent link")

```
Changed(input, value, validation_result=None)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when the value changes.

Can be handled using `on_input_changed` in a subclass of `Input` or in a parent widget in the DOM.

### control [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Changed.control "Permanent link")

```
control
```

Alias for self.input.

### input [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Changed.input "Permanent link")

```
input
```

The `Input` widget that was changed.

### validation\_result [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Changed.validation_result "Permanent link")

```
validation_result = None
```

The result of validating the value (formed by combining the results from each validator), or None if validation was not performed (for example when no validators are specified in the `Input`s init)

### value [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Changed.value "Permanent link")

```
value
```

The value that the input was changed to.

## Submitted [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Submitted "Permanent link")

```
Submitted(input, value, validation_result=None)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")`

Posted when the enter key is pressed within an `Input`.

Can be handled using `on_input_submitted` in a subclass of `Input` or in a parent widget in the DOM.

### control [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Submitted.control "Permanent link")

```
control
```

Alias for self.input.

### input [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Submitted.input "Permanent link")

```
input
```

The `Input` widget that is being submitted.

### validation\_result [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Submitted.validation_result "Permanent link")

```
validation_result = None
```

The result of validating the value on submission, formed by combining the results for each validator. This value will be None if no validation was performed, which will be the case if no validators are supplied to the corresponding `Input` widget.

### value [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Submitted.value "Permanent link")

```
value
```

The value of the `Input` being submitted.

## action\_copy [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_copy "Permanent link")

```
action_copy()
```

Copy the current selection to the clipboard.

## action\_cursor\_left [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_cursor_left "Permanent link")

```
action_cursor_left(=False)
```

Move the cursor one position to the left.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_cursor_left\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `True`, select the text to the left of the cursor. | `False` |

## action\_cursor\_left\_word [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_cursor_left_word "Permanent link")

```
action_cursor_left_word(=False)
```

Move the cursor left to the start of a word.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_cursor_left_word\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `True`, select the text between the old and new cursor positions. | `False` |

## action\_cursor\_right [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_cursor_right "Permanent link")

```
action_cursor_right(=False)
```

Accept an auto-completion or move the cursor one position to the right.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_cursor_right\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `True`, select the text to the right of the cursor. | `False` |

## action\_cursor\_right\_word [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_cursor_right_word "Permanent link")

```
action_cursor_right_word(=False)
```

Move the cursor right to the start of a word.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_cursor_right_word\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `True`, select the text between the old and new cursor positions. | `False` |

## action\_cut [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_cut "Permanent link")

```
action_cut()
```

Cut the current selection (copy to clipboard and remove from input).

## action\_delete\_left [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_delete_left "Permanent link")

```
action_delete_left()
```

Delete one character to the left of the current cursor position.

## action\_delete\_left\_all [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_delete_left_all "Permanent link")

```
action_delete_left_all()
```

Delete all characters to the left of the cursor position.

## action\_delete\_left\_word [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_delete_left_word "Permanent link")

```
action_delete_left_word()
```

Delete leftward of the cursor position to the start of a word.

## action\_delete\_right [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_delete_right "Permanent link")

```
action_delete_right()
```

Delete one character at the current cursor position.

## action\_delete\_right\_all [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_delete_right_all "Permanent link")

```
action_delete_right_all()
```

Delete the current character and all characters to the right of the cursor position.

## action\_delete\_right\_word [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_delete_right_word "Permanent link")

```
action_delete_right_word()
```

Delete the current character and all rightward to the start of the next word.

## action\_end [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_end "Permanent link")

```
action_end(=False)
```

Move the cursor to the end of the input.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_end\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `True`, select the text between the old and new cursor positions. | `False` |

## action\_home [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_home "Permanent link")

```
action_home(=False)
```

Move the cursor to the start of the input.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_home\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If `True`, select the text between the old and new cursor positions. | `False` |

## action\_paste [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_paste "Permanent link")

```
action_paste()
```

Paste from the local clipboard.

## action\_submit [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.action_submit "Permanent link")

```
action_submit()
```

Handle a submit action.

Normally triggered by the user pressing Enter. This may also run any validators.

## check\_consume\_key [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.check_consume_key "Permanent link")

```
check_consume_key(, )
```

Check if the widget may consume the given key.

As an input we are expecting to capture printable keys.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `key` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.check_consume_key\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A key identifier. | *required* |
| ### `character` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.check_consume_key\(character\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A character associated with the key, or `None` if there isn't one. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the widget may capture the key in it's `Key` message, or `False` if it won't. |

## clear [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.clear "Permanent link")

```
clear()
```

Clear the input.

## delete [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.delete "Permanent link")

```
delete(, )
```

Delete the text between the start and end locations.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `start` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.delete\(start\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Start index to delete (inclusive). | *required* |
| ### `end` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.delete\(end\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | End index to delete (inclusive). | *required* |

## delete\_selection [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.delete_selection "Permanent link")

```
delete_selection()
```

Delete the current selection.

## insert [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.insert "Permanent link")

```
insert(, )
```

Insert text at the given index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.insert\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Text to insert. | *required* |
| ### `index` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.insert\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Index to insert the text at (inclusive). | *required* |

## insert\_text\_at\_cursor [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.insert_text_at_cursor "Permanent link")

```
insert_text_at_cursor()
```

Insert new text at the cursor, move the cursor to the end of the new text.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.insert_text_at_cursor\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | New text to insert. | *required* |

## replace [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.replace "Permanent link")

```
replace(, , )
```

Replace the text between the start and end locations with the given text.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.replace\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Text to replace the existing text with. | *required* |
| ### `start` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.replace\(start\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | Start index to replace (inclusive). | *required* |
| ### `end` [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.replace\(end\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | End index to replace (inclusive). | *required* |

## restricted [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.restricted "Permanent link")

```
restricted()
```

Called when a character has been restricted.

The default behavior is to play the system bell. You may want to override this method if you want to disable the bell or do something else entirely.

## validate [¶](https://textual.textualize.io/widgets/input/#textual.widgets.Input.validate "Permanent link")

```
validate(value)
```

Run all the validators associated with this Input on the supplied value.

Runs all validators, combines the result into one. If any of the validators failed, the combined result will be a failure. If no validators are present, None will be returned. This also sets the `-invalid` CSS class on the Input if the validation fails, and sets the `-valid` CSS class on the Input if the validation succeeds.

Returns:

| Type | Description |
| --- | --- |
| `[ValidationResult](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult " ValidationResult (textual.validation.ValidationResult)") \| None` | A ValidationResult indicating whether *all* validators succeeded or not. That is, if *any* validator fails, the result will be an unsuccessful validation. |