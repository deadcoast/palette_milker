---
title: "Textual - MaskedInput"
source: "https://textual.textualize.io/widgets/masked_input/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## MaskedInput¶

Added in version 0.80.0

A masked input derived from `Input`, allowing to restrict user input and give visual aid via a simple template mask, which also acts as an implicit *[validator](https://textual.textualize.io/api/validation/#textual.validation.Validator " Validator")*.

- Focusable
- Container

## Example¶

The example below shows a masked input to ease entering a credit card number.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Label, MaskedInput

class MaskedInputApp(App):
    
    CSS = """
    MaskedInput.-valid {
        border: tall $success 60%;
    }
    MaskedInput.-valid:focus {
        border: tall $success;
    }
    MaskedInput {
        margin: 1 1;
    }
    Label {
        margin: 1 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Enter a valid credit card number.")
        yield MaskedInput(
            template="9999-9999-9999-9999;0",  
        )

app = MaskedInputApp()

if __name__ == "__main__":
    app.run()
```

1. Textual offers default styling for the `-invalid` CSS class (a red border), which is automatically applied to the `MaskedInput` when validation fails. We can also provide custom styling for the `-valid` class, as seen here. In this case, we add a green border around the `MaskedInput` to indicate successful validation.
2. This example shows how to define a template mask for a credit card number, which requires 16 digits in groups of 4.

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `template` | `str` | `""` | The template mask string. |

### The template string format¶

A `MaskedInput` template length defines the maximum length of the input value. Each character of the mask defines a regular expression used to restrict what the user can insert in the corresponding position, and whether the presence of the character in the user input is required for the `MaskedInput` value to be considered valid, according to the following table:

| Mask character | Regular expression | Required? |
| --- | --- | --- |
| `A` | `[A-Za-z]` | Yes |
| `a` | `[A-Za-z]` | No |
| `N` | `[A-Za-z0-9]` | Yes |
| `n` | `[A-Za-z0-9]` | No |
| `X` | `[^ ]` | Yes |
| `x` | `[^ ]` | No |
| `9` | `[0-9]` | Yes |
| `0` | `[0-9]` | No |
| `D` | `[1-9]` | Yes |
| `d` | `[1-9]` | No |
| `#` | `[0-9+\-]` | No |
| `H` | `[A-Fa-f0-9]` | Yes |
| `h` | `[A-Fa-f0-9]` | No |
| `B` | `[0-1]` | Yes |
| `b` | `[0-1]` | No |

There are some special characters that can be used to control automatic case conversion during user input: `>` converts all subsequent user input to uppercase; `<` to lowercase; `!` disables automatic case conversion. Any other character that appears in the template mask is assumed to be a separator, which is a character that is automatically inserted when user reaches its position. All mask characters can be escaped by placing `\` in front of them, allowing any character to be used as separator. The mask can be terminated by `;c`, where `c` is any character you want to be used as placeholder character. The `placeholder` parameter inherited by `Input` can be used to override this allowing finer grain tuning of the placeholder string.

## Messages¶

- [MaskedInput.Changed](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Changed " Changed")
- [MaskedInput.Submitted](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Submitted " Submitted")

## Bindings¶

The masked input widget defines the following bindings:

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

The masked input widget provides the following component classes:

| Class | Description |
| --- | --- |
| `input--cursor` | Target the cursor. |
| `input--placeholder` | Target the placeholder text (when it exists). |
| `input--suggestion` | Target the auto-completion suggestion (when it exists). |
| `input--selection` | Target the selected text. |

---

Bases: `[Input](https://textual.textualize.io/widgets/input/#textual.widgets.Input " Input (textual.widgets._input.Input)")`

A masked text input widget.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `template` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(template\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Template string. | *required* |
| ## `value` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An optional default value for the input. | `None` |
| ## `placeholder` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(placeholder\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Optional placeholder text for the input. | `''` |
| ## `validators` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(validators\) "Permanent link") | `[Validator](https://textual.textualize.io/api/validation/#textual.validation.Validator " Validator (textual.validation.Validator)") \| [Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[[Validator](https://textual.textualize.io/api/validation/#textual.validation.Validator " Validator (textual.validation.Validator)")] \| None` | An iterable of validators that the MaskedInput value will be checked against. | `None` |
| ## `validate_on` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(validate_on\) "Permanent link") | `[Iterable](https://docs.python.org/3/library/typing.html#typing.Iterable "typing.Iterable")[InputValidationOn] \| None` | Zero or more of the values "blur", "changed", and "submitted", which determine when to do input validation. The default is to do validation for all messages. | `None` |
| ## `valid_empty` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(valid_empty\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Empty values are valid. | `False` |
| ## `name` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional name for the masked input widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional ID for the widget. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | Optional initial classes for the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the input is disabled or not. | `False` |
|  | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | Optional tooltip. | `None` |

## template [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.template "Permanent link")

```
template =
```

Input template mask currently in use.

## action\_cursor\_left [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_cursor_left "Permanent link")

```
action_cursor_left()
```

Move the cursor one position to the left; separators are skipped.

## action\_cursor\_left\_word [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_cursor_left_word "Permanent link")

```
action_cursor_left_word()
```

Move the cursor left next to the previous separator. If no previous separator is found, moves the cursor to the start of the input.

## action\_cursor\_right [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_cursor_right "Permanent link")

```
action_cursor_right()
```

Move the cursor one position to the right; separators are skipped.

## action\_cursor\_right\_word [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_cursor_right_word "Permanent link")

```
action_cursor_right_word()
```

Move the cursor right next to the next separator. If no next separator is found, moves the cursor to the end of the input.

## action\_delete\_left [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_delete_left "Permanent link")

```
action_delete_left()
```

Delete one character to the left of the current cursor position.

## action\_delete\_left\_all [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_delete_left_all "Permanent link")

```
action_delete_left_all()
```

Delete all characters to the left of the cursor position.

## action\_delete\_left\_word [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_delete_left_word "Permanent link")

```
action_delete_left_word()
```

Delete leftward of the cursor position to the previous separator or the start of the input.

## action\_delete\_right [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_delete_right "Permanent link")

```
action_delete_right()
```

Delete one character at the current cursor position.

## action\_delete\_right\_word [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_delete_right_word "Permanent link")

```
action_delete_right_word()
```

Delete the current character and all rightward to next separator or the end of the input.

## action\_home [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.action_home "Permanent link")

```
action_home()
```

Move the cursor to the start of the input.

## clear [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.clear "Permanent link")

```
clear()
```

Clear the masked input.

## insert\_text\_at\_cursor [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.insert_text_at_cursor "Permanent link")

```
insert_text_at_cursor()
```

Insert new text at the cursor, move the cursor to the end of the new text.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.insert_text_at_cursor\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | New text to insert. | *required* |

## validate [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.validate "Permanent link")

```
validate(value)
```

Run all the validators associated with this MaskedInput on the supplied value.

Same as `Input.validate()` but also validates against template which acts as an additional implicit validator.

Returns:

| Type | Description |
| --- | --- |
| `[ValidationResult](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult " ValidationResult (textual.validation.ValidationResult)") \| None` | A ValidationResult indicating whether *all* validators succeeded or not. That is, if *any* validator fails, the result will be an unsuccessful validation. |

## validate\_value [¶](https://textual.textualize.io/widgets/masked_input/#textual.widgets.MaskedInput.validate_value "Permanent link")

```
validate_value(value)
```

Validates value against template.