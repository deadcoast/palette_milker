---
title: "Textual - textual.validation"
source: "https://textual.textualize.io/api/validation/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## textual.validation

This module provides a number of classes for validating input.

See [Validating Input](https://textual.textualize.io/widgets/input/#validating-input) for details.

## Failure [¶](https://textual.textualize.io/api/validation/#textual.validation.Failure "Permanent link")

```
Failure(validator, value=None, description=None)
```

Information about a validation failure.

### description [¶](https://textual.textualize.io/api/validation/#textual.validation.Failure.description "Permanent link")

```
description = None
```

An optional override for describing this failure. Takes precedence over any messages set in the Validator.

### validator [¶](https://textual.textualize.io/api/validation/#textual.validation.Failure.validator "Permanent link")

```
validator
```

The Validator which produced the failure.

### value [¶](https://textual.textualize.io/api/validation/#textual.validation.Failure.value "Permanent link")

```
value = None
```

The value which resulted in validation failing.

## Function [¶](https://textual.textualize.io/api/validation/#textual.validation.Function "Permanent link")

```
Function(function, failure_description=None)
```

Bases:

A flexible validator which allows you to provide custom validation logic.

### function [¶](https://textual.textualize.io/api/validation/#textual.validation.Function.function "Permanent link")

```
function = function
```

Function which takes the value to validate and returns True if valid, and False otherwise.

### ReturnedFalse [¶](https://textual.textualize.io/api/validation/#textual.validation.Function.ReturnedFalse "Permanent link")

```
ReturnedFalse(validator, value=None, description=None)
```

Bases:

Indicates validation failed because the supplied function returned False.

### describe\_failure [¶](https://textual.textualize.io/api/validation/#textual.validation.Function.describe_failure "Permanent link")

```
describe_failure()
```

Describes why the validator failed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `failure` [¶](https://textual.textualize.io/api/validation/#textual.validation.Function.describe_failure\(failure\) "Permanent link") |  | Information about why the validation failed. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A string description of the failure. |

### validate [¶](https://textual.textualize.io/api/validation/#textual.validation.Function.validate "Permanent link")

```
validate()
```

Validate that the supplied function returns True.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `value` [¶](https://textual.textualize.io/api/validation/#textual.validation.Function.validate\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The value to pass into the supplied function. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A ValidationResult indicating success if the function returned True, and failure if the function return False. |

## Integer [¶](https://textual.textualize.io/api/validation/#textual.validation.Integer "Permanent link")

```
Integer(
    minimum=None, maximum=None, failure_description=None
)
```

Bases:

Validator which ensures the value is an integer which falls within a range.

### NotAnInteger [¶](https://textual.textualize.io/api/validation/#textual.validation.Integer.NotAnInteger "Permanent link")

```
NotAnInteger(validator, value=None, description=None)
```

Bases:

Indicates a failure due to the value not being a valid integer.

### describe\_failure [¶](https://textual.textualize.io/api/validation/#textual.validation.Integer.describe_failure "Permanent link")

```
describe_failure()
```

Describes why the validator failed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `failure` [¶](https://textual.textualize.io/api/validation/#textual.validation.Integer.describe_failure\(failure\) "Permanent link") |  | Information about why the validation failed. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A string description of the failure. |

### validate [¶](https://textual.textualize.io/api/validation/#textual.validation.Integer.validate "Permanent link")

```
validate()
```

Ensure that `value` is an integer, optionally within a range.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `value` [¶](https://textual.textualize.io/api/validation/#textual.validation.Integer.validate\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The value to validate. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The result of the validation. |

## Length [¶](https://textual.textualize.io/api/validation/#textual.validation.Length "Permanent link")

```
Length(
    minimum=None, maximum=None, failure_description=None
)
```

Bases:

Validate that a string is within a range (inclusive).

### maximum [¶](https://textual.textualize.io/api/validation/#textual.validation.Length.maximum "Permanent link")

```
maximum = maximum
```

The inclusive maximum length of the value, or None if unbounded.

### minimum [¶](https://textual.textualize.io/api/validation/#textual.validation.Length.minimum "Permanent link")

```
minimum = minimum
```

The inclusive minimum length of the value, or None if unbounded.

### Incorrect [¶](https://textual.textualize.io/api/validation/#textual.validation.Length.Incorrect "Permanent link")

```
Incorrect(validator, value=None, description=None)
```

Bases:

Indicates a failure due to the length of the value being outside the range.

### describe\_failure [¶](https://textual.textualize.io/api/validation/#textual.validation.Length.describe_failure "Permanent link")

```
describe_failure()
```

Describes why the validator failed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `failure` [¶](https://textual.textualize.io/api/validation/#textual.validation.Length.describe_failure\(failure\) "Permanent link") |  | Information about why the validation failed. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A string description of the failure. |

### validate [¶](https://textual.textualize.io/api/validation/#textual.validation.Length.validate "Permanent link")

```
validate()
```

Ensure that value falls within the maximum and minimum length constraints.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `value` [¶](https://textual.textualize.io/api/validation/#textual.validation.Length.validate\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The value to validate. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The result of the validation. |

## Number [¶](https://textual.textualize.io/api/validation/#textual.validation.Number "Permanent link")

```
Number(
    minimum=None, maximum=None, failure_description=None
)
```

Bases:

Validator that ensures the value is a number, with an optional range check.

### maximum [¶](https://textual.textualize.io/api/validation/#textual.validation.Number.maximum "Permanent link")

```
maximum = maximum
```

The maximum value of the number, inclusive. If `None`, the maximum is unbounded.

### minimum [¶](https://textual.textualize.io/api/validation/#textual.validation.Number.minimum "Permanent link")

```
minimum = minimum
```

The minimum value of the number, inclusive. If `None`, the minimum is unbounded.

### NotANumber [¶](https://textual.textualize.io/api/validation/#textual.validation.Number.NotANumber "Permanent link")

```
NotANumber(validator, value=None, description=None)
```

Bases:

Indicates a failure due to the value not being a valid number (decimal/integer, inc. scientific notation)

### NotInRange [¶](https://textual.textualize.io/api/validation/#textual.validation.Number.NotInRange "Permanent link")

```
NotInRange(validator, value=None, description=None)
```

Bases:

Indicates a failure due to the number not being within the range \[minimum, maximum\].

### describe\_failure [¶](https://textual.textualize.io/api/validation/#textual.validation.Number.describe_failure "Permanent link")

```
describe_failure()
```

Describes why the validator failed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `failure` [¶](https://textual.textualize.io/api/validation/#textual.validation.Number.describe_failure\(failure\) "Permanent link") |  | Information about why the validation failed. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A string description of the failure. |

### validate [¶](https://textual.textualize.io/api/validation/#textual.validation.Number.validate "Permanent link")

```
validate()
```

Ensure that `value` is a valid number, optionally within a range.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `value` [¶](https://textual.textualize.io/api/validation/#textual.validation.Number.validate\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The value to validate. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The result of the validation. |

## Regex [¶](https://textual.textualize.io/api/validation/#textual.validation.Regex "Permanent link")

```
Regex(regex, flags=0, failure_description=None)
```

Bases:

A validator that checks the value matches a regex (via `re.fullmatch`).

### flags [¶](https://textual.textualize.io/api/validation/#textual.validation.Regex.flags "Permanent link")

```
flags = flags
```

The flags to pass to `re.fullmatch`.

### regex [¶](https://textual.textualize.io/api/validation/#textual.validation.Regex.regex "Permanent link")

```
regex = regex
```

The regex which we'll validate is matched by the value.

### NoResults [¶](https://textual.textualize.io/api/validation/#textual.validation.Regex.NoResults "Permanent link")

```
NoResults(validator, value=None, description=None)
```

Bases:

Indicates validation failed because the regex could not be found within the value string.

### describe\_failure [¶](https://textual.textualize.io/api/validation/#textual.validation.Regex.describe_failure "Permanent link")

```
describe_failure()
```

Describes why the validator failed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `failure` [¶](https://textual.textualize.io/api/validation/#textual.validation.Regex.describe_failure\(failure\) "Permanent link") |  | Information about why the validation failed. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A string description of the failure. |

### validate [¶](https://textual.textualize.io/api/validation/#textual.validation.Regex.validate "Permanent link")

```
validate()
```

Ensure that the value matches the regex.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `value` [¶](https://textual.textualize.io/api/validation/#textual.validation.Regex.validate\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The value that should match the regex. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The result of the validation. |

## URL [¶](https://textual.textualize.io/api/validation/#textual.validation.URL "Permanent link")

```
URL(failure_description=None)
```

Bases:

Validator that checks if a URL is valid (ensuring a scheme is present).

### InvalidURL [¶](https://textual.textualize.io/api/validation/#textual.validation.URL.InvalidURL "Permanent link")

```
InvalidURL(validator, value=None, description=None)
```

Bases:

Indicates that the URL is not valid.

### describe\_failure [¶](https://textual.textualize.io/api/validation/#textual.validation.URL.describe_failure "Permanent link")

```
describe_failure()
```

Describes why the validator failed.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `failure` [¶](https://textual.textualize.io/api/validation/#textual.validation.URL.describe_failure\(failure\) "Permanent link") |  | Information about why the validation failed. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A string description of the failure. |

### validate [¶](https://textual.textualize.io/api/validation/#textual.validation.URL.validate "Permanent link")

```
validate()
```

Validates that `value` is a valid URL (contains a scheme).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `value` [¶](https://textual.textualize.io/api/validation/#textual.validation.URL.validate\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The value to validate. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The result of the validation. |

## ValidationResult [¶](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult "Permanent link")

```
ValidationResult(failures=list())
```

The result of calling a `Validator.validate` method.

### failure\_descriptions [¶](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult.failure_descriptions "Permanent link")

```
failure_descriptions
```

Utility for extracting failure descriptions as strings.

Useful if you don't care about the additional metadata included in the `Failure` objects.

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]` | A list of the string descriptions explaining the failing validations. |

### failures [¶](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult.failures "Permanent link")

```
failures = field(default_factory=list)
```

A list of reasons why the value was invalid. Empty if valid=True

### is\_valid [¶](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult.is_valid "Permanent link")

```
is_valid
```

True if the validation was successful.

### failure [¶](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult.failure "Permanent link")

```
failure()
```

Construct a failure ValidationResult.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `failures` [¶](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult.failure\(failures\) "Permanent link") | `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")[]` | The failures. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | A failure ValidationResult. |

### merge [¶](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult.merge "Permanent link")

```
merge()
```

Merge multiple ValidationResult objects into one.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `results` [¶](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult.merge\(results\) "Permanent link") | `[Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")['ValidationResult']` | List of ValidationResult objects to merge. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `'ValidationResult'` | Merged ValidationResult object. |

### success [¶](https://textual.textualize.io/api/validation/#textual.validation.ValidationResult.success "Permanent link")

```
success()
```

Construct a successful ValidationResult.

Returns:

| Type | Description |
| --- | --- |
|  | A successful ValidationResult. |

## Validator [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator "Permanent link")

```
Validator(failure_description=None)
```

Bases: `[ABC](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")`

Base class for the validation of string values.

Commonly used in conjunction with the `Input` widget, which accepts a list of validators via its constructor. This validation framework can also be used to validate any 'stringly-typed' values (for example raw command line input from `sys.args`).

To implement your own `Validator`, subclass this class.

Example
```
def is_palindrome(value: str) -> bool:
    """Check has string has the same code points left to right, as right to left."""
    return value == value[::-1]

class Palindrome(Validator):
    def validate(self, value: str) -> ValidationResult:
        if is_palindrome(value):
            return self.success()
        else:
            return self.failure("Not a palindrome!")
```

### failure\_description [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.failure_description "Permanent link")

```
failure_description = failure_description
```

A description of why the validation failed.

The description (intended to be user-facing) to attached to the Failure if the validation fails. This failure description is ultimately accessible at the time of validation failure via the `Input.Changed` or `Input.Submitted` event, and you can access it on your message handler (a method called, for example, `on_input_changed` or a method decorated with `@on(Input.Changed)`.

### describe\_failure [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.describe_failure "Permanent link")

```
describe_failure()
```

Return a string description of the Failure.

Used to provide a more fine-grained description of the failure. A Validator could fail for multiple reasons, so this method could be used to provide a different reason for different types of failure.

Warning

This method is only called if no other description has been supplied. If you supply a description inside a call to `self.failure(description="...")`, or pass a description into the constructor of the validator, those will take priority, and this method won't be called.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `failure` [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.describe_failure\(failure\) "Permanent link") |  | Information about why the validation failed. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A string description of the failure. |

### failure [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.failure "Permanent link")

```
failure(=None, =None, =None)
```

Shorthand for signaling validation failure.

Return `self.failure(...)` from to indicated that validation *failed*.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `description` [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.failure\(description\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The failure description that will be used. When used in conjunction with the Input widget, this is the description that will ultimately be available inside the handler for `Input.Changed`. If not supplied, the `failure_description` from the `Validator` will be used. If that is not supplied either, then the `describe_failure` method on `Validator` will be called. | `None` |
| #### `value` [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.failure\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The value that was considered invalid. This is optional, and only needs to be supplied if required in your `Input.Changed` handler. | `None` |
| #### `failures` [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.failure\(failures\) "Permanent link") | ` \| [Sequence](https://docs.python.org/3/library/typing.html#typing.Sequence "typing.Sequence")[] \| None` | The reasons the validator failed. If not supplied, a generic `Failure` will be included in the ValidationResult returned from this function. | `None` |

Returns:

| Type | Description |
| --- | --- |
|  | A ValidationResult representing failed validation, and containing the metadata supplied to this function. |

### success [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.success "Permanent link")

```
success()
```

Shorthand for `ValidationResult(True)`.

Return `self.success()` from to indicated that validation *succeeded*.

Returns:

| Type | Description |
| --- | --- |
|  | A ValidationResult indicating validation succeeded. |

### validate [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.validate "Permanent link")

```
validate()
```

Validate the value and return a ValidationResult describing the outcome of the validation.

Implement this method when defining custom validators.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `value` [¶](https://textual.textualize.io/api/validation/#textual.validation.Validator.validate\(value\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The value to validate. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The result of the validation (\[`self.success()`\]\[textual.validation.Validator.success) or \[`self.failure(...)`\]\[textual.validation.Validator.failure\]). |