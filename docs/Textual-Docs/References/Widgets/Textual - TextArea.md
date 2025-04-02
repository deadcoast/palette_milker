---
title: "Textual - TextArea"
source: "https://textual.textualize.io/widgets/text_area/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## TextArea¶

Tip

Added in version 0.38.0. Soft wrapping added in version 0.48.0.

A widget for editing text which may span multiple lines. Supports text selection, soft wrapping, optional syntax highlighting with tree-sitter and a variety of keybindings.

- Focusable
- Container

## Guide¶

### Code editing vs plain text editing¶

By default, the `TextArea` widget is a standard multi-line input box with soft-wrapping enabled.

If you're interested in editing code, you may wish to use the convenience constructor. This is a method which, by default, returns a new `TextArea` with soft-wrapping disabled, line numbers enabled, and the tab key behavior configured to insert `\t`.

### Syntax highlighting dependencies¶

To enable syntax highlighting, you'll need to install the `syntax` extra dependencies:

```
pip install "textual[syntax]"
```

```
poetry add "textual[syntax]"
```

This will install `tree-sitter` and `tree-sitter-languages`. These packages are distributed as binary wheels, so it may limit your applications ability to run in environments where these wheels are not available. After installing, you can set the reactive attribute on the `TextArea` to enable highlighting.

In this example we load some initial text into the `TextArea`, and set the language to `"python"` to enable syntax highlighting.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import TextArea

TEXT = """\
def hello(name):
    print("hello" + name)

def goodbye(name):
    print("goodbye" + name)
"""

class TextAreaExample(App):
    def compose(self) -> ComposeResult:
        yield TextArea.code_editor(TEXT, language="python")

app = TextAreaExample()
if __name__ == "__main__":
    app.run()
```

To update the content programmatically, set the property to a string value.

To update the parser used for syntax highlighting, set the reactive attribute:

```
# Set the language to Markdown
text_area.language = "markdown"
```

Note

More built-in languages will be added in the future. For now, you can [add your own](https://textual.textualize.io/widgets/text_area/#adding-support-for-custom-languages).

### Reading content from `TextArea`[¶](https://textual.textualize.io/widgets/text_area/#reading-content-from-textarea "Permanent link")

There are a number of ways to retrieve content from the `TextArea`:

- The property returns all content in the text area as a string.
- The property returns the text corresponding to the current selection.
- The method returns the text between two locations.

In all cases, when multiple lines of text are retrieved, the [document line separator](https://textual.textualize.io/widgets/text_area/#line-separators) will be used.

### Editing content inside `TextArea`[¶](https://textual.textualize.io/widgets/text_area/#editing-content-inside-textarea "Permanent link")

The content of the `TextArea` can be updated using the method. This method is the programmatic equivalent of selecting some text and then pasting.

Some other convenient methods are available, such as , , and .

Tip

The `TextArea.document.end` property returns the location at the end of the document, which might be convenient when editing programmatically.

### Working with the cursor¶

#### Moving the cursor¶

The cursor location is available via the property, which represents the location of the cursor as a tuple `(row_index, column_index)`. These indices are zero-based and represent the position of the cursor in the content. Writing a new value to `cursor_location` will immediately update the location of the cursor.

```
>>> text_area = TextArea()
>>> text_area.cursor_location
(0, 0)
>>> text_area.cursor_location = (0, 4)
>>> text_area.cursor_location
(0, 4)
```

`cursor_location` is a simple way to move the cursor programmatically, but it doesn't let us select text.

#### Selecting text¶

To select text, we can use the `selection` reactive attribute. Let's select the first two lines of text in a document by adding `text_area.selection = Selection(start=(0, 0), end=(2, 0))` to our code:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import TextArea
from textual.widgets.text_area import Selection

TEXT = """\
def hello(name):
    print("hello" + name)

def goodbye(name):
    print("goodbye" + name)
"""

class TextAreaSelection(App):
    def compose(self) -> ComposeResult:
        text_area = TextArea.code_editor(TEXT, language="python")
        text_area.selection = Selection(start=(0, 0), end=(2, 0))  
        yield text_area

app = TextAreaSelection()
if __name__ == "__main__":
    app.run()
```

1. Selects the first two lines of text.

Note that selections can happen in both directions, so `Selection((2, 0), (0, 0))` is also valid.

Tip

The `end` attribute of the `selection` is always equal to `TextArea.cursor_location`. In other words, the `cursor_location` attribute is simply a convenience for accessing `text_area.selection.end`.

There are a number of additional utility methods available for interacting with the cursor.

##### Location information¶

Many properties exist on `TextArea` which give information about the current cursor location. These properties begin with `cursor_at_`, and return booleans. For example, tells us if the cursor is at a start of line.

We can also check the location the cursor *would* arrive at if we were to move it. For example, returns the location the cursor would move to if it were to move right. A number of similar methods exist, with names like `get_cursor_*_location`.

##### Cursor movement methods¶

The method allows you to move the cursor to a new location while selecting text, or move the cursor and scroll to keep it centered.

```
# Move the cursor from its current location to row index 4,
# column index 8, while selecting all the text between.
text_area.move_cursor((4, 8), select=True)
```

The method offers a very similar interface, but moves the cursor relative to its current location.

##### Common selections¶

There are some methods available which make common selections easier:

- selects a line by index. Bound to F6 by default.
- selects all text. Bound to F7 by default.

### Themes¶

`TextArea` ships with some builtin themes, and you can easily add your own.

Themes give you control over the look and feel, including syntax highlighting, the cursor, selection, gutter, and more.

#### Default theme¶

The default `TextArea` theme is called `css`, which takes its values entirely from CSS. This means that the default appearance of the widget fits nicely into a standard Textual application, and looks right on both dark and light mode.

When using the `css` theme, you can make use of to style elements of the `TextArea`. For example, the CSS code `TextArea .text-area--cursor { background: green; }` will make the cursor `green`.

More complex applications such as code editors may want to use pre-defined themes such as `monokai`. This involves using a `TextAreaTheme` object, which we cover in detail below. This allows full customization of the `TextArea`, including syntax highlighting, at the code level.

#### Using builtin themes¶

The initial theme of the `TextArea` is determined by the `theme` parameter.

```
# Create a TextArea with the 'dracula' theme.
yield TextArea.code_editor("print(123)", language="python", theme="dracula")
```

You can check which themes are available using the property.

```
>>> text_area = TextArea()
>>> print(text_area.available_themes)
{'css', 'dracula', 'github_light', 'monokai', 'vscode_dark'}
```

After creating a `TextArea`, you can change the theme by setting the attribute to one of the available themes.

```
text_area.theme = "vscode_dark"
```

On setting this attribute the `TextArea` will immediately refresh to display the updated theme.

#### Custom themes¶

Note

Custom themes are only relevant for people who are looking to customize syntax highlighting. If you're only editing plain text, and wish to recolor aspects of the `TextArea`, you should use the .

Using custom (non-builtin) themes is a two-step process:

1. Create an instance of .
2. Register it using .

##### 1\. Creating a theme¶

Let's create a simple theme, `"my_cool_theme"`, which colors the cursor blue, and the cursor line yellow. Our theme will also syntax highlight strings as red, and comments as magenta.

```
from rich.style import Style
from textual.widgets.text_area import TextAreaTheme
# ...
my_theme = TextAreaTheme(
    # This name will be used to refer to the theme...
    name="my_cool_theme",
    # Basic styles such as background, cursor, selection, gutter, etc...
    cursor_style=Style(color="white", bgcolor="blue"),
    cursor_line_style=Style(bgcolor="yellow"),
    # \`syntax_styles\` is for syntax highlighting.
    # It maps tokens parsed from the document to Rich styles.
    syntax_styles={
        "string": Style(color="red"),
        "comment": Style(color="magenta"),
    }
)
```

Attributes like `cursor_style` and `cursor_line_style` apply general language-agnostic styling to the widget. If you choose not to supply a value for one of these attributes, it will be taken from the CSS component styles.

The `syntax_styles` attribute of `TextAreaTheme` is used for syntax highlighting and depends on the `language` currently in use. For more details, see [syntax highlighting](https://textual.textualize.io/widgets/text_area/#syntax-highlighting).

If you wish to build on an existing theme, you can obtain a reference to it using the classmethod:

```
from textual.widgets.text_area import TextAreaTheme

monokai = TextAreaTheme.get_builtin_theme("monokai")
```

Our theme can now be registered with the `TextArea` instance.

```
text_area.register_theme(my_theme)
```

After registering a theme, it'll appear in the `available_themes`:

```
>>> print(text_area.available_themes)
{'dracula', 'github_light', 'monokai', 'vscode_dark', 'my_cool_theme'}
```

We can now switch to it:

```
text_area.theme = "my_cool_theme"
```

This immediately updates the appearance of the `TextArea`:

<!-- SVG content removed by SVG Remover -->

### Tab and Escape behavior¶

Pressing the Tab key will shift focus to the next widget in your application by default. This matches how other widgets work in Textual.

To have Tab insert a `\t` character, set the `tab_behavior` attribute to the string value `"indent"`. While in this mode, you can shift focus by pressing the Esc key.

### Indentation¶

The character(s) inserted when you press tab is controlled by setting the `indent_type` attribute to either `tabs` or `spaces`.

If `indent_type == "spaces"`, pressing Tab will insert up to `indent_width` spaces in order to align with the next tab stop.

### Undo and redo¶

`TextArea` offers `undo` and `redo` methods. By default, `undo` is bound to Ctrl+Z and `redo` to Ctrl+Y.

The `TextArea` uses a heuristic to place *checkpoints* after certain types of edit. When you call `undo`, all of the edits between now and the most recent checkpoint are reverted. You can manually add a checkpoint by calling the instance method.

The undo and redo history uses a stack-based system, where a single item on the stack represents a single checkpoint. In memory-constrained environments, you may wish to reduce the maximum number of checkpoints that can exist. You can do this by passing the `max_checkpoints` argument to the `TextArea` constructor.

### Read-only mode¶

`TextArea.read_only` is a boolean reactive attribute which, if `True`, will prevent users from modifying content in the `TextArea`.

While `read_only=True`, you can still modify the content programmatically.

While this mode is active, the `TextArea` receives the `-read-only` CSS class, which you can use to supply custom styles for read-only mode.

### Line separators¶

When content is loaded into `TextArea`, the content is scanned from beginning to end and the first occurrence of a line separator is recorded.

This separator will then be used when content is later read from the `TextArea` via the `text` property. The `TextArea` widget does not support exporting text which contains mixed line endings.

Similarly, newline characters pasted into the `TextArea` will be converted.

You can check the line separator of the current document by inspecting `TextArea.document.newline`:

```
>>> text_area = TextArea()
>>> text_area.document.newline
'\n'
```

### Line numbers¶

The gutter (column on the left containing line numbers) can be toggled by setting the `show_line_numbers` attribute to `True` or `False`.

Setting this attribute will immediately repaint the `TextArea` to reflect the new value.

You can also change the start line number (the topmost line number in the gutter) by setting the `line_number_start` reactive attribute.

### Extending `TextArea`[¶](https://textual.textualize.io/widgets/text_area/#extending-textarea "Permanent link")

Sometimes, you may wish to subclass `TextArea` to add some extra functionality. In this section, we'll briefly explore how we can extend the widget to achieve common goals.

#### Hooking into key presses¶

You may wish to hook into certain key presses to inject some functionality. This can be done by over-riding `_on_key` and adding the required functionality.

##### Example - closing parentheses automatically¶

Let's extend `TextArea` to add a feature which automatically closes parentheses and moves the cursor to a sensible location.

```
from textual import events
from textual.app import App, ComposeResult
from textual.widgets import TextArea

class ExtendedTextArea(TextArea):
    """A subclass of TextArea with parenthesis-closing functionality."""

    def _on_key(self, event: events.Key) -> None:
        if event.character == "(":
            self.insert("()")
            self.move_cursor_relative(columns=-1)
            event.prevent_default()

class TextAreaKeyPressHook(App):
    def compose(self) -> ComposeResult:
        yield ExtendedTextArea.code_editor(language="python")

app = TextAreaKeyPressHook()
if __name__ == "__main__":
    app.run()
```

This intercepts the key handler when `"("` is pressed, and inserts `"()"` instead. It then moves the cursor so that it lands between the open and closing parentheses.

Typing "`def hello(`" into the `TextArea` now results in the bracket automatically being closed:

<!-- SVG content removed by SVG Remover -->

### Advanced concepts¶

#### Syntax highlighting¶

Syntax highlighting inside the `TextArea` is powered by a library called [`tree-sitter`](https://tree-sitter.github.io/tree-sitter/).

Each time you update the document in a `TextArea`, an internal syntax tree is updated. This tree is frequently *queried* to find location ranges relevant to syntax highlighting. We give these ranges *names*, and ultimately map them to Rich styles inside `TextAreaTheme.syntax_styles`.

To illustrate how this works, lets look at how the "Monokai" `TextAreaTheme` highlights Markdown files.

When the `language` attribute is set to `"markdown"`, a highlight query similar to the one below is used (trimmed for brevity).

```
(heading_content) @heading
(link) @link
```

This highlight query maps `heading_content` nodes returned by the Markdown parser to the name `@heading`, and `link` nodes to the name `@link`.

Inside our `TextAreaTheme.syntax_styles` dict, we can map the name `@heading` to a Rich style. Here's a snippet from the "Monokai" theme which does just that:

```
TextAreaTheme(
    name="monokai",
    base_style=Style(color="#f8f8f2", bgcolor="#272822"),
    gutter_style=Style(color="#90908a", bgcolor="#272822"),
    # ...
    syntax_styles={
        # Colorise @heading and make them bold
        "heading": Style(color="#F92672", bold=True),
        # Colorise and underline @link
        "link": Style(color="#66D9EF", underline=True),
        # ...
    },
)
```

To understand which names can be mapped inside `syntax_styles`, we recommend looking at the existing themes and highlighting queries (`.scm` files) in the Textual repository.

Tip

You may also wish to take a look at the contents of `TextArea._highlights` on an active `TextArea` instance to see which highlights have been generated for the open document.

#### Adding support for custom languages¶

To add support for a language to a `TextArea`, use the method.

To register a language, we require two things:

1. A tree-sitter `Language` object which contains the grammar for the language.
2. A highlight query which is used for [syntax highlighting](https://textual.textualize.io/widgets/text_area/#syntax-highlighting).

##### Example - adding Java support¶

The easiest way to obtain a `Language` object is using the [`py-tree-sitter-languages`](https://github.com/grantjenks/py-tree-sitter-languages) package. Here's how we can use this package to obtain a reference to a `Language` object representing Java:

```
from tree_sitter_languages import get_language
java_language = get_language("java")
```

The exact version of the parser used when you call `get_language` can be checked via the [`repos.txt` file](https://github.com/grantjenks/py-tree-sitter-languages/blob/a6d4f7c903bf647be1bdcfa504df967d13e40427/repos.txt) in the version of `py-tree-sitter-languages` you're using. This file contains links to the GitHub repos and commit hashes of the tree-sitter parsers. In these repos you can often find pre-made highlight queries at `queries/highlights.scm`, and a file showing all the available node types which can be used in highlight queries at `src/node-types.json`.

Since we're adding support for Java, lets grab the Java highlight query from the repo by following these steps:

1. Open [`repos.txt` file](https://github.com/grantjenks/py-tree-sitter-languages/blob/a6d4f7c903bf647be1bdcfa504df967d13e40427/repos.txt) from the `py-tree-sitter-languages` repo.
2. Find the link corresponding to `tree-sitter-java` and go to the repo on GitHub (you may also need to go to the specific commit referenced in `repos.txt`).
3. Go to [`queries/highlights.scm`](https://github.com/tree-sitter/tree-sitter-java/blob/ac14b4b1884102839455d32543ab6d53ae089ab7/queries/highlights.scm) to see the example highlight query for Java.

Be sure to check the license in the repo to ensure it can be freely copied.

Warning

It's important to use a highlight query which is compatible with the parser in use, so pay attention to the commit hash when visiting the repo via `repos.txt`.

We now have our `Language` and our highlight query, so we can register Java as a language.

```
from pathlib import Path

from tree_sitter_languages import get_language

from textual.app import App, ComposeResult
from textual.widgets import TextArea

java_language = get_language("java")
java_highlight_query = (Path(__file__).parent / "java_highlights.scm").read_text()
java_code = """\
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
"""

class TextAreaCustomLanguage(App):
    def compose(self) -> ComposeResult:
        text_area = TextArea.code_editor(text=java_code)
        text_area.cursor_blink = False

        # Register the Java language and highlight query
        text_area.register_language("java", java_language, java_highlight_query)

        # Switch to Java
        text_area.language = "java"
        yield text_area

app = TextAreaCustomLanguage()
if __name__ == "__main__":
    app.run()
```

Running our app, we can see that the Java code is highlighted. We can freely edit the text, and the syntax highlighting will update immediately.

Recall that we map names (like `@heading`) from the tree-sitter highlight query to Rich style objects inside the `TextAreaTheme.syntax_styles` dictionary. If you notice some highlights are missing after registering a language, the issue may be:

1. The current `TextAreaTheme` doesn't contain a mapping for the name in the highlight query. Adding a new key-value pair to `syntax_styles` should resolve the issue.
2. The highlight query doesn't assign a name to the pattern you expect to be highlighted. In this case you'll need to update the highlight query to assign to the name.

Tip

The names assigned in tree-sitter highlight queries are often reused across multiple languages. For example, `@string` is used in many languages to highlight strings.

If you're building functionality on top of `TextArea`, it may be useful to inspect the `navigator` and `wrapped_document` attributes.

- `navigator` is a instance which can give us general information about the cursor's location within a document, as well as where the cursor will move to when certain actions are performed.
- `wrapped_document` is a instance which can be used to convert document locations to visual locations, taking wrapping into account. It also offers a variety of other convenience methods and properties.

A detailed view of these classes is out of scope, but do note that a lot of the functionality of `TextArea` exists within them, so inspecting them could be worthwhile.

## Reactive attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `language` | `str \| None` | `None` | The language to use for syntax highlighting. |
| `theme` | `str` | `"css"` | The theme to use. |
| `selection` | `Selection` | `Selection()` | The current selection. |
| `show_line_numbers` | `bool` | `False` | Show or hide line numbers. |
| `line_number_start` | `int` | `1` | The start line number in the gutter. |
| `indent_width` | `int` | `4` | The number of spaces to indent and width of tabs. |
| `match_cursor_bracket` | `bool` | `True` | Enable/disable highlighting matching brackets under cursor. |
| `cursor_blink` | `bool` | `True` | Enable/disable blinking of the cursor when the widget has focus. |
| `soft_wrap` | `bool` | `True` | Enable/disable soft wrapping. |
| `read_only` | `bool` | `False` | Enable/disable read-only mode. |

## Messages¶

## Bindings¶

The `TextArea` widget defines the following bindings:

| Key(s) | Description |
| --- | --- |
| up | Move the cursor up. |
| down | Move the cursor down. |
| left | Move the cursor left. |
| ctrl+left | Move the cursor to the start of the word. |
| ctrl+shift+left | Move the cursor to the start of the word and select. |
| right | Move the cursor right. |
| ctrl+right | Move the cursor to the end of the word. |
| ctrl+shift+right | Move the cursor to the end of the word and select. |
| home,ctrl+a | Move the cursor to the start of the line. |
| end,ctrl+e | Move the cursor to the end of the line. |
| shift+home | Move the cursor to the start of the line and select. |
| shift+end | Move the cursor to the end of the line and select. |
| pageup | Move the cursor one page up. |
| pagedown | Move the cursor one page down. |
| shift+up | Select while moving the cursor up. |
| shift+down | Select while moving the cursor down. |
| shift+left | Select while moving the cursor left. |
| shift+right | Select while moving the cursor right. |
| backspace | Delete character to the left of cursor. |
| ctrl+w | Delete from cursor to start of the word. |
| delete,ctrl+d | Delete character to the right of cursor. |
| ctrl+f | Delete from cursor to end of the word. |
| ctrl+shift+k | Delete the current line. |
| ctrl+u | Delete from cursor to the start of the line. |
| ctrl+k | Delete from cursor to the end of the line. |
| f6 | Select the current line. |
| f7 | Select all text in the document. |
| ctrl+z | Undo. |
| ctrl+y | Redo. |
| ctrl+x | Cut selection or line if no selection. |
| ctrl+c | Copy selection to clipboard. |
| ctrl+v | Paste from clipboard. |

## Component classes¶

The `TextArea` defines component classes that can style various aspects of the widget. Styles from the `theme` attribute take priority.

`TextArea` offers some component classes which can be used to style aspects of the widget.

Note that any attributes provided in the chosen `TextAreaTheme` will take priority here.

| Class | Description |
| --- | --- |
| `text-area--cursor` | Target the cursor. |
| `text-area--gutter` | Target the gutter (line number column). |
| `text-area--cursor-gutter` | Target the gutter area of the line the cursor is on. |
| `text-area--cursor-line` | Target the line the cursor is on. |
| `text-area--selection` | Target the current selection. |
| `text-area--matching-bracket` | Target matching brackets. |

## See also¶

- [`Input`](https://textual.textualize.io/widgets/input/#textual.widgets.Input " Input") - single-line text input widget
- \- theming the `TextArea`
- \- guides cursor movement
- \- manages wrapping the document
- \- manages the undo stack
- The tree-sitter documentation [website](https://tree-sitter.github.io/tree-sitter/).
- The tree-sitter Python bindings [repository](https://github.com/tree-sitter/py-tree-sitter).
- `py-tree-sitter-languages` [repository](https://github.com/grantjenks/py-tree-sitter-languages) (provides binary wheels for a large variety of tree-sitter languages).

## Additional notes¶

- To remove the outline effect when the `TextArea` is focused, you can set `border: none; padding: 0;` in your CSS.

---

Bases: `[ScrollView](https://textual.textualize.io/api/scroll_view/#textual.scroll_view.ScrollView " ScrollView (textual.scroll_view.ScrollView)")`

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `text` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The initial text to load into the TextArea. | `''` |
| ## `language` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(language\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The language to use. | `None` |
| ## `theme` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(theme\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The theme to use. | `'css'` |
| ## `soft_wrap` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(soft_wrap\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable soft wrapping. | `True` |
| ## `tab_behavior` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(tab_behavior\) "Permanent link") | `Literal['focus', 'indent']` | If 'focus', pressing tab will switch focus. If 'indent', pressing tab will insert a tab. | `'focus'` |
| ## `read_only` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(read_only\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable read-only mode. This prevents edits using the keyboard. | `False` |
| ## `show_line_numbers` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(show_line_numbers\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Show line numbers on the left edge. | `False` |
| ## `line_number_start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(line_number_start\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | What line number to start on. | `1` |
| ## `max_checkpoints` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(max_checkpoints\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The maximum number of undo history checkpoints to retain. | `50` |
| ## `name` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the `TextArea` widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget, used to refer to it from Textual CSS. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | One or more Textual CSS compatible class names separated by spaces. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the widget is disabled. | `False` |
|  | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | Optional tooltip. | `None` |

## BINDINGS [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.BINDINGS "Permanent link")

```
BINDINGS = [
    Binding("up", "cursor_up", "Cursor up", show=False),
    Binding(
        "down", "cursor_down", "Cursor down", show=False
    ),
    Binding(
        "left", "cursor_left", "Cursor left", show=False
    ),
    Binding(
        "right", "cursor_right", "Cursor right", show=False
    ),
    Binding(
        "ctrl+left",
        "cursor_word_left",
        "Cursor word left",
        show=False,
    ),
    Binding(
        "ctrl+right",
        "cursor_word_right",
        "Cursor word right",
        show=False,
    ),
    Binding(
        "home,ctrl+a",
        "cursor_line_start",
        "Cursor line start",
        show=False,
    ),
    Binding(
        "end,ctrl+e",
        "cursor_line_end",
        "Cursor line end",
        show=False,
    ),
    Binding(
        "pageup",
        "cursor_page_up",
        "Cursor page up",
        show=False,
    ),
    Binding(
        "pagedown",
        "cursor_page_down",
        "Cursor page down",
        show=False,
    ),
    Binding(
        "ctrl+shift+left",
        "cursor_word_left(True)",
        "Cursor left word select",
        show=False,
    ),
    Binding(
        "ctrl+shift+right",
        "cursor_word_right(True)",
        "Cursor right word select",
        show=False,
    ),
    Binding(
        "shift+home",
        "cursor_line_start(True)",
        "Cursor line start select",
        show=False,
    ),
    Binding(
        "shift+end",
        "cursor_line_end(True)",
        "Cursor line end select",
        show=False,
    ),
    Binding(
        "shift+up",
        "cursor_up(True)",
        "Cursor up select",
        show=False,
    ),
    Binding(
        "shift+down",
        "cursor_down(True)",
        "Cursor down select",
        show=False,
    ),
    Binding(
        "shift+left",
        "cursor_left(True)",
        "Cursor left select",
        show=False,
    ),
    Binding(
        "shift+right",
        "cursor_right(True)",
        "Cursor right select",
        show=False,
    ),
    Binding("f6", "select_line", "Select line", show=False),
    Binding("f7", "select_all", "Select all", show=False),
    Binding(
        "backspace",
        "delete_left",
        "Delete character left",
        show=False,
    ),
    Binding(
        "ctrl+w",
        "delete_word_left",
        "Delete left to start of word",
        show=False,
    ),
    Binding(
        "delete,ctrl+d",
        "delete_right",
        "Delete character right",
        show=False,
    ),
    Binding(
        "ctrl+f",
        "delete_word_right",
        "Delete right to start of word",
        show=False,
    ),
    Binding("ctrl+x", "cut", "Cut", show=False),
    Binding("ctrl+c", "copy", "Copy", show=False),
    Binding("ctrl+v", "paste", "Paste", show=False),
    Binding(
        "ctrl+u",
        "delete_to_start_of_line",
        "Delete to line start",
        show=False,
    ),
    Binding(
        "ctrl+k",
        "delete_to_end_of_line_or_delete_line",
        "Delete to line end",
        show=False,
    ),
    Binding(
        "ctrl+shift+k",
        "delete_line",
        "Delete line",
        show=False,
    ),
    Binding("ctrl+z", "undo", "Undo", show=False),
    Binding("ctrl+y", "redo", "Redo", show=False),
]
```

| Key(s) | Description |
| --- | --- |
| up | Move the cursor up. |
| down | Move the cursor down. |
| left | Move the cursor left. |
| ctrl+left | Move the cursor to the start of the word. |
| ctrl+shift+left | Move the cursor to the start of the word and select. |
| right | Move the cursor right. |
| ctrl+right | Move the cursor to the end of the word. |
| ctrl+shift+right | Move the cursor to the end of the word and select. |
| home,ctrl+a | Move the cursor to the start of the line. |
| end,ctrl+e | Move the cursor to the end of the line. |
| shift+home | Move the cursor to the start of the line and select. |
| shift+end | Move the cursor to the end of the line and select. |
| pageup | Move the cursor one page up. |
| pagedown | Move the cursor one page down. |
| shift+up | Select while moving the cursor up. |
| shift+down | Select while moving the cursor down. |
| shift+left | Select while moving the cursor left. |
| shift+right | Select while moving the cursor right. |
| backspace | Delete character to the left of cursor. |
| ctrl+w | Delete from cursor to start of the word. |
| delete,ctrl+d | Delete character to the right of cursor. |
| ctrl+f | Delete from cursor to end of the word. |
| ctrl+shift+k | Delete the current line. |
| ctrl+u | Delete from cursor to the start of the line. |
| ctrl+k | Delete from cursor to the end of the line. |
| f6 | Select the current line. |
| f7 | Select all text in the document. |
| ctrl+z | Undo. |
| ctrl+y | Redo. |
| ctrl+x | Cut selection or line if no selection. |
| ctrl+c | Copy selection to clipboard. |
| ctrl+v | Paste from clipboard. |

## COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {
    "text-area--cursor",
    "text-area--gutter",
    "text-area--cursor-gutter",
    "text-area--cursor-line",
    "text-area--selection",
    "text-area--matching-bracket",
}
```

`TextArea` offers some component classes which can be used to style aspects of the widget.

Note that any attributes provided in the chosen `TextAreaTheme` will take priority here.

| Class | Description |
| --- | --- |
| `text-area--cursor` | Target the cursor. |
| `text-area--gutter` | Target the gutter (line number column). |
| `text-area--cursor-gutter` | Target the gutter area of the line the cursor is on. |
| `text-area--cursor-line` | Target the line the cursor is on. |
| `text-area--selection` | Target the current selection. |
| `text-area--matching-bracket` | Target matching brackets. |

## available\_languages [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.available_languages "Permanent link")

```
available_languages
```

A set of the names of languages available to the `TextArea`.

The values in this set can be assigned to the `language` reactive attribute of `TextArea`.

The returned set contains the builtin languages installed with the syntax extras, plus those registered via the `register_language` method.

## available\_themes [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.available_themes "Permanent link")

```
available_themes
```

A list of the names of the themes available to the `TextArea`.

The values in this list can be assigned `theme` reactive attribute of `TextArea`.

You can retrieve the full specification for a theme by passing one of the strings from this list into `TextAreaTheme.get_by_name(theme_name: str)`.

Alternatively, you can directly retrieve a list of `TextAreaTheme` objects (which contain the full theme specification) by calling `TextAreaTheme.builtin_themes()`.

## cursor\_at\_end\_of\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cursor_at_end_of_line "Permanent link")

```
cursor_at_end_of_line
```

True if and only if the cursor is at the end of a row.

## cursor\_at\_end\_of\_text [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cursor_at_end_of_text "Permanent link")

```
cursor_at_end_of_text
```

True if and only if the cursor is at the very end of the document.

## cursor\_at\_first\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cursor_at_first_line "Permanent link")

```
cursor_at_first_line
```

True if and only if the cursor is on the first line.

## cursor\_at\_last\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cursor_at_last_line "Permanent link")

```
cursor_at_last_line
```

True if and only if the cursor is on the last line.

## cursor\_at\_start\_of\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cursor_at_start_of_line "Permanent link")

```
cursor_at_start_of_line
```

True if and only if the cursor is at column 0.

## cursor\_at\_start\_of\_text [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cursor_at_start_of_text "Permanent link")

```
cursor_at_start_of_text
```

True if and only if the cursor is at location (0, 0)

## cursor\_blink [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cursor_blink "Permanent link")

```
cursor_blink = reactive(True, init=False)
```

True if the cursor should blink.

## cursor\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cursor_location "Permanent link")

```
cursor_location
```

The current location of the cursor in the document.

This is a utility for accessing the `end` of `TextArea.selection`.

## cursor\_screen\_offset [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cursor_screen_offset "Permanent link")

```
cursor_screen_offset
```

The offset of the cursor relative to the screen.

## document [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.document "Permanent link")

```
document = ()
```

The document this widget is currently editing.

## gutter\_width [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.gutter_width "Permanent link")

```
gutter_width
```

The width of the gutter (the left column containing line numbers).

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The cell-width of the line number column. If `show_line_numbers` is `False` returns 0. |

## history [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.history "Permanent link")

```
history = (
    max_checkpoints=,
    checkpoint_timer=2.0,
    checkpoint_max_characters=100,
)
```

A stack (the end of the list is the top of the stack) for tracking edits.

## indent\_type [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.indent_type "Permanent link")

```
indent_type = 'spaces'
```

Whether to indent using tabs or spaces.

## indent\_width [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.indent_width "Permanent link")

```
indent_width = reactive(4, init=False)
```

The width of tabs or the multiple of spaces to align to on pressing the `tab` key.

If the document currently open contains tabs that are currently visible on screen, altering this value will immediately change the display width of the visible tabs.

## is\_syntax\_aware [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.is_syntax_aware "Permanent link")

```
is_syntax_aware
```

True if the TextArea is currently syntax aware - i.e. it's parsing document content.

## language [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.language "Permanent link")

```
language =
```

The language to use.

This must be set to a valid, non-None value for syntax highlighting to work.

If the value is a string, a built-in language parser will be used if available.

If you wish to use an unsupported language, you'll have to register it first using .

## line\_number\_start [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.line_number_start "Permanent link")

```
line_number_start = reactive(1, init=False)
```

The line number the first line should be.

## match\_cursor\_bracket [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.match_cursor_bracket "Permanent link")

```
match_cursor_bracket = reactive(True, init=False)
```

If the cursor is at a bracket, highlight the matching bracket (if found).

## matching\_bracket\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.matching_bracket_location "Permanent link")

```
matching_bracket_location
```

The location of the matching bracket, if there is one.

## navigator [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.navigator "Permanent link")

```
navigator = (wrapped_document)
```

Queried to determine where the cursor should move given a navigation action, accounting for wrapping etc.

## read\_only [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.read_only "Permanent link")

```
read_only = reactive(False)
```

True if the content is read-only.

Read-only means end users cannot insert, delete or replace content.

The document can still be edited programmatically via the API.

## selected\_text [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.selected_text "Permanent link")

```
selected_text
```

The text between the start and end points of the current selection.

## selection [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.selection "Permanent link")

```
selection = reactive(
    (), init=False, always_update=True
)
```

The selection start and end locations (zero-based line\_index, offset).

This represents the cursor location and the current selection.

The `Selection.end` always refers to the cursor location.

If no text is selected, then `Selection.end == Selection.start` is True.

The text selected in the document is available via the `TextArea.selected_text` property.

## show\_line\_numbers [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.show_line_numbers "Permanent link")

```
show_line_numbers = reactive(False, init=False)
```

True to show the line number column on the left edge, otherwise False.

Changing this value will immediately re-render the `TextArea`.

## soft\_wrap [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.soft_wrap "Permanent link")

```
soft_wrap = reactive(True, init=False)
```

True if text should soft wrap.

## text [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.text "Permanent link")

```
text
```

The entire text content of the document.

## theme [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.theme "Permanent link")

```
theme =
```

The name of the theme to use.

Themes must be registered using before they can be used.

Syntax highlighting is only possible when the `language` attribute is set.

## wrap\_width [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.wrap_width "Permanent link")

```
wrap_width
```

The width which gets used when the document wraps.

Accounts for gutter, scrollbars, etc.

## wrapped\_document [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.wrapped_document "Permanent link")

```
wrapped_document = (document)
```

The wrapped view of the document.

## Changed [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.Changed "Permanent link")

```
Changed(text_area)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.events.Message)")`

Posted when the content inside the TextArea changes.

Handle this message using the `on` decorator - `@on(TextArea.Changed)` or a method named `on_text_area_changed`.

### control [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.Changed.control "Permanent link")

```
control
```

The `TextArea` that sent this message.

### text\_area [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.Changed.text_area "Permanent link")

```
text_area
```

The `text_area` that sent this message.

## SelectionChanged [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.SelectionChanged "Permanent link")

```
SelectionChanged(selection, text_area)
```

Bases: `[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.events.Message)")`

Posted when the selection changes.

This includes when the cursor moves or when text is selected.

### selection [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.SelectionChanged.selection "Permanent link")

```
selection
```

The new selection.

### text\_area [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.SelectionChanged.text_area "Permanent link")

```
text_area
```

The `text_area` that sent this message.

## action\_copy [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_copy "Permanent link")

```
action_copy()
```

Copy selection to clipboard.

## action\_cursor\_down [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_down "Permanent link")

```
action_cursor_down(=False)
```

Move the cursor down one cell.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_down\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, select the text while moving. | `False` |

## action\_cursor\_left [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_left "Permanent link")

```
action_cursor_left(=False)
```

Move the cursor one location to the left.

If the cursor is at the left edge of the document, try to move it to the end of the previous line.

If text is selected, move the cursor to the start of the selection.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_left\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, select the text while moving. | `False` |

## action\_cursor\_line\_end [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_line_end "Permanent link")

```
action_cursor_line_end(select=False)
```

Move the cursor to the end of the line.

## action\_cursor\_line\_start [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_line_start "Permanent link")

```
action_cursor_line_start(select=False)
```

Move the cursor to the start of the line.

## action\_cursor\_page\_down [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_page_down "Permanent link")

```
action_cursor_page_down()
```

Move the cursor and scroll down one page.

## action\_cursor\_page\_up [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_page_up "Permanent link")

```
action_cursor_page_up()
```

Move the cursor and scroll up one page.

## action\_cursor\_right [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_right "Permanent link")

```
action_cursor_right(=False)
```

Move the cursor one location to the right.

If the cursor is at the end of a line, attempt to go to the start of the next line.

If text is selected, move the cursor to the end of the selection.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_right\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, select the text while moving. | `False` |

## action\_cursor\_up [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_up "Permanent link")

```
action_cursor_up(=False)
```

Move the cursor up one cell.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_up\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, select the text while moving. | `False` |

## action\_cursor\_word\_left [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_word_left "Permanent link")

```
action_cursor_word_left(=False)
```

Move the cursor left by a single word, skipping trailing whitespace.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `select` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_word_left\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether to select while moving the cursor. | `False` |

## action\_cursor\_word\_right [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cursor_word_right "Permanent link")

```
action_cursor_word_right(select=False)
```

Move the cursor right by a single word, skipping leading whitespace.

## action\_cut [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_cut "Permanent link")

```
action_cut()
```

Cut text (remove and copy to clipboard).

## action\_delete\_left [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_delete_left "Permanent link")

```
action_delete_left()
```

Deletes the character to the left of the cursor and updates the cursor location.

If there's a selection, then the selected range is deleted.

## action\_delete\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_delete_line "Permanent link")

```
action_delete_line()
```

Deletes the lines which intersect with the selection.

## action\_delete\_right [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_delete_right "Permanent link")

```
action_delete_right()
```

Deletes the character to the right of the cursor and keeps the cursor at the same location.

If there's a selection, then the selected range is deleted.

## action\_delete\_to\_end\_of\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_delete_to_end_of_line "Permanent link")

```
action_delete_to_end_of_line()
```

Deletes from the cursor location to the end of the line.

## action\_delete\_to\_end\_of\_line\_or\_delete\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_delete_to_end_of_line_or_delete_line "Permanent link")

```
action_delete_to_end_of_line_or_delete_line()
```

Deletes from the cursor location to the end of the line, or deletes the line.

The line will be deleted if the line is empty.

## action\_delete\_to\_start\_of\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_delete_to_start_of_line "Permanent link")

```
action_delete_to_start_of_line()
```

Deletes from the cursor location to the start of the line.

## action\_delete\_word\_left [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_delete_word_left "Permanent link")

```
action_delete_word_left()
```

Deletes the word to the left of the cursor and updates the cursor location.

## action\_delete\_word\_right [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_delete_word_right "Permanent link")

```
action_delete_word_right()
```

Deletes the word to the right of the cursor and keeps the cursor at the same location.

Note that the location that we delete to using this action is not the same as the location we move to when we move the cursor one word to the right. This action does not skip leading whitespace, whereas cursor movement does.

## action\_paste [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_paste "Permanent link")

```
action_paste()
```

Paste from local clipboard.

## action\_redo [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_redo "Permanent link")

```
action_redo()
```

Redo the most recently undone batch of edits.

## action\_select\_all [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_select_all "Permanent link")

```
action_select_all()
```

Select all the text in the document.

## action\_select\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_select_line "Permanent link")

```
action_select_line()
```

Select all the text on the current line.

## action\_undo [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.action_undo "Permanent link")

```
action_undo()
```

Undo the edits since the last checkpoint (the most recent batch of edits).

## cell\_width\_to\_column\_index [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cell_width_to_column_index "Permanent link")

```
cell_width_to_column_index(, )
```

Return the column that the cell width corresponds to on the given row.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `cell_width` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cell_width_to_column_index\(cell_width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The cell width to convert. | *required* |
| ### `row_index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.cell_width_to_column_index\(row_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the row to examine. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The column corresponding to the cell width on that row. |

## check\_consume\_key [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.check_consume_key "Permanent link")

```
check_consume_key(, =None)
```

Check if the widget may consume the given key.

As a textarea we are expecting to capture printable keys.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `key` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.check_consume_key\(key\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | A key identifier. | *required* |
| ### `character` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.check_consume_key\(character\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | A character associated with the key, or `None` if there isn't one. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | `True` if the widget may capture the key in it's `Key` message, or `False` if it won't. |

## clamp\_visitable [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.clamp_visitable "Permanent link")

```
clamp_visitable()
```

Clamp the given location to the nearest visitable location.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.clamp_visitable\(location\) "Permanent link") |  | The location to clamp. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The nearest location that we could conceivably navigate to using the cursor. |

## clear [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.clear "Permanent link")

```
clear()
```

Delete all text from the document.

Returns:

| Type | Description |
| --- | --- |
|  | An EditResult relating to the deletion of all content. |

## code\_editor [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor "Permanent link")

```
code_editor(
    ="",
    *,
    =None,
    ="monokai",
    =False,
    ="indent",
    read_only=False,
    =True,
    =1,
    max_checkpoints=50,
    =None,
    =None,
    =None,
    =False,
    =None
)
```

Construct a new `TextArea` with sensible defaults for editing code.

This instantiates a `TextArea` with line numbers enabled, soft wrapping disabled, "indent" tab behavior, and the "monokai" theme.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The initial text to load into the TextArea. | `''` |
| ### `language` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(language\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The language to use. | `None` |
| ### `theme` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(theme\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The theme to use. | `'monokai'` |
| ### `soft_wrap` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(soft_wrap\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable soft wrapping. | `False` |
| ### `tab_behavior` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(tab_behavior\) "Permanent link") | `Literal['focus', 'indent']` | If 'focus', pressing tab will switch focus. If 'indent', pressing tab will insert a tab. | `'indent'` |
| ### `show_line_numbers` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(show_line_numbers\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Show line numbers on the left edge. | `True` |
| ### `line_number_start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(line_number_start\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | What line number to start on. | `1` |
| ### `name` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the `TextArea` widget. | `None` |
| ### `id` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget, used to refer to it from Textual CSS. | `None` |
| ### `classes` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | One or more Textual CSS compatible class names separated by spaces. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.code_editor\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the widget is disabled. | `False` |
|  | `[RenderableType](https://rich.readthedocs.io/en/stable/reference/console.html#rich.console.RenderableType "rich.console.RenderableType") \| None` | Optional tooltip | `None` |

## delete [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.delete "Permanent link")

```
delete(, , *, =True)
```

Delete the text between two locations in the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.delete\(start\) "Permanent link") |  | The start location. | *required* |
| ### `end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.delete\(end\) "Permanent link") |  | The end location. | *required* |
| ### `maintain_selection_offset` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.delete\(maintain_selection_offset\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, the active Selection will be updated such that the same text is selected before and after the selection, if possible. Otherwise, the cursor will jump to the end point of the edit. | `True` |

Returns:

| Type | Description |
| --- | --- |
|  | An `EditResult` containing information about the edit. |

## edit [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.edit "Permanent link")

```
edit()
```

Perform an Edit.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `edit` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.edit\(edit\) "Permanent link") |  | The Edit to perform. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | Data relating to the edit that may be useful. The data returned |
|  | may be different depending on the edit performed. |

## find\_matching\_bracket [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.find_matching_bracket "Permanent link")

```
find_matching_bracket(, )
```

If the character is a bracket, find the matching bracket.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `bracket` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.find_matching_bracket\(bracket\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The character we're searching for the matching bracket of. | *required* |
| ### `search_from` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.find_matching_bracket\(search_from\) "Permanent link") |  | The location to start the search. | *required* |

Returns:

| Type | Description |
| --- | --- |
| ` \| None` | The `Location` of the matching bracket, or `None` if it's not found. |
| ` \| None` | If the character is not available for bracket matching, `None` is returned. |

## get\_column\_width [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_column_width "Permanent link")

```
get_column_width(, )
```

Get the cell offset of the column from the start of the row.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `row` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_column_width\(row\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The row index. | *required* |
| ### `column` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_column_width\(column\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The column index (codepoint offset from start of row). | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The cell width of the column relative to the start of the row. |

## get\_cursor\_down\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_cursor_down_location "Permanent link")

```
get_cursor_down_location()
```

Get the location the cursor will move to if it moves down.

Returns:

| Type | Description |
| --- | --- |
|  | The location the cursor will move to if it moves down. |

## get\_cursor\_left\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_cursor_left_location "Permanent link")

```
get_cursor_left_location()
```

Get the location the cursor will move to if it moves left.

Returns:

| Type | Description |
| --- | --- |
|  | The location of the cursor if it moves left. |

## get\_cursor\_line\_end\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_cursor_line_end_location "Permanent link")

```
get_cursor_line_end_location()
```

Get the location of the end of the current line.

Returns:

| Type | Description |
| --- | --- |
|  | The (row, column) location of the end of the cursors current line. |

## get\_cursor\_line\_start\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_cursor_line_start_location "Permanent link")

```
get_cursor_line_start_location(=False)
```

Get the location of the start of the current line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `smart_home` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_cursor_line_start_location\(smart_home\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, use "smart home key" behavior - go to the first non-whitespace character on the line, and if already there, go to offset 0. Smart home only works when wrapping is disabled. | `False` |

Returns:

| Type | Description |
| --- | --- |
|  | The (row, column) location of the start of the cursors current line. |

## get\_cursor\_right\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_cursor_right_location "Permanent link")

```
get_cursor_right_location()
```

Get the location the cursor will move to if it moves right.

Returns:

| Type | Description |
| --- | --- |
|  | the location the cursor will move to if it moves right. |

## get\_cursor\_up\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_cursor_up_location "Permanent link")

```
get_cursor_up_location()
```

Get the location the cursor will move to if it moves up.

Returns:

| Type | Description |
| --- | --- |
|  | The location the cursor will move to if it moves up. |

## get\_cursor\_word\_left\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_cursor_word_left_location "Permanent link")

```
get_cursor_word_left_location()
```

Get the location the cursor will jump to if it goes 1 word left.

Returns:

| Type | Description |
| --- | --- |
|  | The location the cursor will jump on "jump word left". |

## get\_cursor\_word\_right\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_cursor_word_right_location "Permanent link")

```
get_cursor_word_right_location()
```

Get the location the cursor will jump to if it goes 1 word right.

Returns:

| Type | Description |
| --- | --- |
|  | The location the cursor will jump on "jump word right". |

## get\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_line "Permanent link")

```
get_line()
```

Retrieve the line at the given line index.

You can stylize the Text object returned here to apply additional styling to TextArea content.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `line_index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_line\(line_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the line. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Text](https://rich.readthedocs.io/en/stable/reference/text.html#rich.text.Text "rich.text.Text")` | A `rich.Text` object containing the requested line. |

## get\_target\_document\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_target_document_location "Permanent link")

```
get_target_document_location()
```

Given a MouseEvent, return the row and column offset of the event in document-space.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `event` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_target_document_location\(event\) "Permanent link") | `[MouseEvent](https://textual.textualize.io/api/events/#textual.events.MouseEvent " MouseEvent (textual.events.MouseEvent)")` | The MouseEvent. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The location of the mouse event within the document. |

## get\_text\_range [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_text_range "Permanent link")

```
get_text_range(, )
```

Get the text between a start and end location.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_text_range\(start\) "Permanent link") |  | The start location. | *required* |
| ### `end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.get_text_range\(end\) "Permanent link") |  | The end location. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text between start and end. |

## insert [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.insert "Permanent link")

```
insert(
    , =None, *, =True
)
```

Insert text into the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.insert\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text to insert. | *required* |
| ### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.insert\(location\) "Permanent link") | ` \| None` | The location to insert text, or None to use the cursor location. | `None` |
| ### `maintain_selection_offset` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.insert\(maintain_selection_offset\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, the active Selection will be updated such that the same text is selected before and after the selection, if possible. Otherwise, the cursor will jump to the end point of the edit. | `True` |

Returns:

| Type | Description |
| --- | --- |
|  | An `EditResult` containing information about the edit. |

## load\_text [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.load_text "Permanent link")

```
load_text()
```

Load text into the TextArea.

This will replace the text currently in the TextArea and clear the edit history.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.load_text\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text to load into the TextArea. | *required* |

## move\_cursor [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor "Permanent link")

```
move_cursor(
    , =False, =False, =True
)
```

Move the cursor to a location.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor\(location\) "Permanent link") |  | The location to move the cursor to. | *required* |
| ### `select` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, select text between the old and new location. | `False` |
| ### `center` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor\(center\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, scroll such that the cursor is centered. | `False` |
| ### `record_width` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor\(record_width\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, record the cursor column cell width after navigating so that we jump back to the same width the next time we move to a row that is wide enough. | `True` |

## move\_cursor\_relative [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor_relative "Permanent link")

```
move_cursor_relative(
    =0,
    =0,
    =False,
    =False,
    =True,
)
```

Move the cursor relative to its current location in document-space.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `rows` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor_relative\(rows\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of rows to move down by (negative to move up) | `0` |
| ### `columns` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor_relative\(columns\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The number of columns to move right by (negative to move left) | `0` |
| ### `select` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor_relative\(select\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, select text between the old and new location. | `False` |
| ### `center` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor_relative\(center\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, scroll such that the cursor is centered. | `False` |
| ### `record_width` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.move_cursor_relative\(record_width\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, record the cursor column cell width after navigating so that we jump back to the same width the next time we move to a row that is wide enough. | `True` |

## record\_cursor\_width [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.record_cursor_width "Permanent link")

```
record_cursor_width()
```

Record the current cell width of the cursor.

This is used where we navigate up and down through rows. If we're in the middle of a row, and go down to a row with no content, then we go down to another row, we want our cursor to jump back to the same offset that we were originally at.

## redo [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.redo "Permanent link")

```
redo()
```

Redo the most recently undone batch of edits.

```
register_language(, , )
```

Register a language and corresponding highlight query.

Calling this method does not change the language of the `TextArea`. On switching to this language (via the `language` reactive attribute), syntax highlighting will be performed using the given highlight query.

If a string `name` is supplied for a builtin supported language, then this method will update the default highlight query for that language.

Registering a language only registers it to this instance of `TextArea`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The name of the language. | *required* |
|  | `'Language'` | A tree-sitter `Language` object. | *required* |
|  | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The highlight query to use for syntax highlighting this language. | *required* |

```
register_theme(theme)
```

Register a theme for use by the `TextArea`.

After registering a theme, you can set themes by assigning the theme name to the `TextArea.theme` reactive attribute. For example `text_area.theme = "my_custom_theme"` where `"my_custom_theme"` is the name of the theme you registered.

If you supply a theme with a name that already exists that theme will be overwritten.

## replace [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.replace "Permanent link")

```
replace(
    , , , *, =True
)
```

Replace text in the document with new text.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `insert` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.replace\(insert\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text to insert. | *required* |
| ### `start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.replace\(start\) "Permanent link") |  | The start location | *required* |
| ### `end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.replace\(end\) "Permanent link") |  | The end location. | *required* |
| ### `maintain_selection_offset` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.replace\(maintain_selection_offset\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, the active Selection will be updated such that the same text is selected before and after the selection, if possible. Otherwise, the cursor will jump to the end point of the edit. | `True` |

Returns:

| Type | Description |
| --- | --- |
|  | An `EditResult` containing information about the edit. |

## scroll\_cursor\_visible [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.scroll_cursor_visible "Permanent link")

```
scroll_cursor_visible(=False, =False)
```

Scroll the `TextArea` such that the cursor is visible on screen.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `center` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.scroll_cursor_visible\(center\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the cursor should be scrolled to the center. | `False` |
| ### `animate` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.scroll_cursor_visible\(animate\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if we should animate while scrolling. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | The offset that was scrolled to bring the cursor into view. |

## select\_all [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.select_all "Permanent link")

```
select_all()
```

Select all of the text in the `TextArea`.

## select\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.select_line "Permanent link")

```
select_line()
```

Select all the text in the specified line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.select_line\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the line to select (starting from 0). | *required* |

## undo [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.undo "Permanent link")

```
undo()
```

Undo the edits since the last checkpoint (the most recent batch of edits).

## update\_highlight\_query [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.update_highlight_query "Permanent link")

```
update_highlight_query(, )
```

Update the highlight query for an already registered language.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `name` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.update_highlight_query\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The name of the language. | *required* |
| ### `highlight_query` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets._text_area.TextArea.update_highlight_query\(highlight_query\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The highlight query to use for syntax highlighting this language. | *required* |

---

## BUILTIN\_LANGUAGES [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.BUILTIN_LANGUAGES "Permanent link")

```
BUILTIN_LANGUAGES = [
    "python",
    "markdown",
    "json",
    "toml",
    "yaml",
    "html",
    "css",
    "javascript",
    "rust",
    "go",
    "regex",
    "sql",
    "java",
    "bash",
    "xml",
]
```

Languages that are included in the `syntax` extras.

## Highlight [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Highlight "Permanent link")

```
Highlight = Tuple[StartColumn, EndColumn, HighlightName]
```

A tuple representing a syntax highlight within one line.

## Location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Location "Permanent link")

```
Location = Tuple[int, int]
```

A location (row, column) within the document. Indexing starts at 0.

## Document [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document "Permanent link")

```
Document(text)
```

Bases:

A document which can be opened in a TextArea.

### end [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.end "Permanent link")

```
end
```

Returns the location of the end of the document.

### line\_count [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.line_count "Permanent link")

```
line_count
```

Returns the number of lines in the document.

### lines [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.lines "Permanent link")

```
lines
```

Get the document as a list of strings, where each string represents a line.

Newline characters are not included in at the end of the strings.

The newline character used in this document can be found via the `Document.newline` property.

### newline [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.newline "Permanent link")

```
newline
```

Get the Newline used in this document (e.g. ' ', ' '. etc.)

### start [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.start "Permanent link")

```
start
```

Returns the location of the start of the document (0, 0).

### text [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.text "Permanent link")

```
text
```

Get the text from the document.

### get\_index\_from\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_index_from_location "Permanent link")

```
get_index_from_location()
```

Given a location, returns the index from the document's text.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_index_from_location\(location\) "Permanent link") |  | The location in the document. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The index in the document's text. |

### get\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_line "Permanent link")

```
get_line()
```

Returns the line with the given index from the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_line\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the line in the document. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The string representing the line. |

### get\_location\_from\_index [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_location_from_index "Permanent link")

```
get_location_from_index()
```

Given a codepoint index in the document's text, returns the corresponding location.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_location_from_index\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index in the document's text. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The corresponding location. |

Raises:

| Type | Description |
| --- | --- |
| `[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` | If the index is doesn't correspond to a location in the document. |

### get\_size [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_size "Permanent link")

```
get_size()
```

The Size of the document, taking into account the tab rendering width.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `tab_width` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_size\(tab_width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The width to use for tab indents. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | The size (width, height) of the document. |

### get\_text\_range [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_text_range "Permanent link")

```
get_text_range(, )
```

Get the text that falls between the start and end locations.

Returns the text between `start` and `end`, including the appropriate line separator character as specified by `Document._newline`. Note that `_newline` is set automatically to the first line separator character found in the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_text_range\(start\) "Permanent link") |  | The start location of the selection. | *required* |
| #### `end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.get_text_range\(end\) "Permanent link") |  | The end location of the selection. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text between start (inclusive) and end (exclusive). |

### replace\_range [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.replace_range "Permanent link")

```
replace_range(, , )
```

Replace text at the given range.

This is the only method by which a document may be updated.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.replace_range\(start\) "Permanent link") |  | A tuple (row, column) where the edit starts. | *required* |
| #### `end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.replace_range\(end\) "Permanent link") |  | A tuple (row, column) where the edit ends. | *required* |
| #### `text` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Document.replace_range\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text to insert between start and end. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The EditResult containing information about the completed replace operation. |

## DocumentBase [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase "Permanent link")

Bases: `[ABC](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")`

Describes the minimum functionality a Document implementation must provide in order to be used by the TextArea widget.

### end [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.end "Permanent link")

```
end
```

Returns the location of the end of the document.

### line\_count [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.line_count "Permanent link")

```
line_count
```

Returns the number of lines in the document.

### lines [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.lines "Permanent link")

```
lines
```

Get the lines of the document as a list of strings.

The strings should *not* include newline characters. The newline character used for the document can be retrieved via the newline property.

### newline [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.newline "Permanent link")

```
newline
```

Return the line separator used in the document.

### start [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.start "Permanent link")

```
start
```

Returns the location of the start of the document (0, 0).

### text [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.text "Permanent link")

```
text
```

The text from the document as a string.

### get\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.get_line "Permanent link")

```
get_line()
```

Returns the line with the given index from the document.

This is used in rendering lines, and will be called by the TextArea for each line that is rendered.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.get_line\(index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the line in the document. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The str instance representing the line. |

### get\_size [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.get_size "Permanent link")

```
get_size()
```

Get the size of the document.

The height is generally the number of lines, and the width is generally the maximum cell length of all the lines.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `indent_width` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.get_size\(indent_width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The width to use for tab characters. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Size](https://textual.textualize.io/api/geometry/#textual.geometry.Size " Size (textual.geometry.Size)")` | The Size of the document bounding box. |

### get\_text\_range [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.get_text_range "Permanent link")

```
get_text_range(, )
```

Get the text that falls between the start and end locations.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.get_text_range\(start\) "Permanent link") |  | The start location of the selection. | *required* |
| #### `end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.get_text_range\(end\) "Permanent link") |  | The end location of the selection. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text between start (inclusive) and end (exclusive). |

### query\_syntax\_tree [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.query_syntax_tree "Permanent link")

```
query_syntax_tree(, =None, =None)
```

Query the tree-sitter syntax tree.

The default implementation always returns an empty list.

To support querying in a subclass, this must be implemented.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `query` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.query_syntax_tree\(query\) "Permanent link") | `'Query'` | The tree-sitter Query to perform. | *required* |
| #### `start_point` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.query_syntax_tree\(start_point\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)] \| None` | The (row, column byte) to start the query at. | `None` |
| #### `end_point` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.query_syntax_tree\(end_point\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)] \| None` | The (row, column byte) to end the query at. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [list](https://docs.python.org/3/library/stdtypes.html#list)['Node']]` | A dict mapping captured node names to lists of Nodes with that name. |

### replace\_range [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.replace_range "Permanent link")

```
replace_range(, , )
```

Replace the text at the given range.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.replace_range\(start\) "Permanent link") |  | A tuple (row, column) where the edit starts. | *required* |
| #### `end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.replace_range\(end\) "Permanent link") |  | A tuple (row, column) where the edit ends. | *required* |
| #### `text` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentBase.replace_range\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text to insert between start and end. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The new end location after the edit is complete. |

## DocumentNavigator [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator "Permanent link")

```
DocumentNavigator()
```

Cursor navigation in the TextArea is "wrapping-aware".

Although the cursor location (the selection) is represented as a location in the raw document, when you actually *move* the cursor, it must take wrapping into account (otherwise things start to look really confusing to the user where wrapping is involved).

Your cursor visually moves through the wrapped version of the document, rather than the raw document. So, for example, pressing down on the keyboard may move your cursor to a position further along the current raw document line, rather than on to the next line in the raw document.

The DocumentNavigator class manages that behavior.

Given a cursor location in the unwrapped document, and a cursor movement action, this class can inform us of the destination the cursor will move to considering the current wrapping width and document content. It can also translate between document-space (a location/(row,col) in the raw document), and visual-space (x and y offsets) as the user will see them on screen after the document has been wrapped.

For this to work correctly, the wrapped\_document and document must be synchronised. This means that if you make an edit to the document, you *must* then update the wrapped document, and *then* you may query the document navigator.

Naming conventions:

A "location" refers to a location, in document-space (in the raw document). It is entirely unrelated to visually positioning. A location in a document can appear in any visual position, as it is influenced by scrolling, wrapping, gutter settings, and the cell width of characters to its left.

A "wrapped section" refers to a portion of the line accounting for wrapping. For example the line "ABCDEF" when wrapped at width 3 will result in 2 sections: "ABC" and "DEF". In this case, we call "ABC" is the first section/wrapped section.

A "wrap offset" is an integer representing the index at which wrapping occurs in a document-space line. This is a codepoint index, rather than a visual offset. In "ABCDEF" with wrapping at width 3, there is a single wrap offset of 3.

"Smart home" refers to a modification of the "home" key behavior. If smart home is enabled, the first non-whitespace character is considered to be the home location. If the cursor is currently at this position, then the normal home behavior applies. This is designed to make cursor movement more useful to end users.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `wrapped_document` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator\(wrapped_document\) "Permanent link") |  | The WrappedDocument to be used when making navigation decisions. | *required* |

### last\_x\_offset [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.last_x_offset "Permanent link")

```
last_x_offset = 0
```

Remembers the last x offset (cell width) the cursor was moved horizontally to, so that it can be restored on vertical movement where possible.

### clamp\_reachable [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.clamp_reachable "Permanent link")

```
clamp_reachable()
```

Given a location, return the nearest location that corresponds to a reachable location in the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.clamp_reachable\(location\) "Permanent link") |  | A location. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The nearest reachable location in the document. |

### get\_location\_above [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_above "Permanent link")

```
get_location_above()
```

Get the location visually aligned with the cell above the given location.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_above\(location\) "Permanent link") |  | The location to start from. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The cell above the given location. |

### get\_location\_at\_y\_offset [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_at_y_offset "Permanent link")

```
get_location_at_y_offset(, )
```

Apply a visual vertical offset to a location and check the resulting location.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_at_y_offset\(location\) "Permanent link") |  | The location to start from. | *required* |
| #### `vertical_offset` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_at_y_offset\(vertical_offset\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The vertical offset to move (negative=up, positive=down). | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The location after the offset has been applied. |

### get\_location\_below [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_below "Permanent link")

```
get_location_below()
```

Given a location in the raw document, return the raw document location corresponding to moving down in the wrapped representation of the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_below\(location\) "Permanent link") |  | The location in the raw document. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The location which is *visually* below the given location. |

### get\_location\_end [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_end "Permanent link")

```
get_location_end()
```

Get the location corresponding to the end of the current section.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_end\(location\) "Permanent link") |  | The current location. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The location corresponding to the end of the wrapped line. |

### get\_location\_home [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_home "Permanent link")

```
get_location_home(, =False)
```

Get the "home location" corresponding to the given location.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_home\(location\) "Permanent link") |  | The location to consider. | *required* |
| #### `smart_home` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_home\(smart_home\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Enable/disable 'smart home' behavior. | `False` |

Returns:

| Type | Description |
| --- | --- |
|  | The home location, relative to the given location. |

### get\_location\_left [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_left "Permanent link")

```
get_location_left()
```

Get the location to the left of the given location.

Note that if the given location is at the start of the line, then this will return the end of the preceding line, since that's where you would expect the cursor to move.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_left\(location\) "Permanent link") |  | The location to start from. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The location to the right. |

### get\_location\_right [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_right "Permanent link")

```
get_location_right()
```

Get the location to the right of the given location.

Note that if the given location is at the end of the line, then this will return the start of the following line, since that's where you would expect the cursor to move.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.get_location_right\(location\) "Permanent link") |  | The location to start from. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The location to the right. |

### is\_end\_of\_document [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_end_of_document "Permanent link")

```
is_end_of_document()
```

Check if a location is at the end of the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_end_of_document\(location\) "Permanent link") |  | The location to examine. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if and only if the cursor is at the end of the document. |

### is\_end\_of\_document\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_end_of_document_line "Permanent link")

```
is_end_of_document_line()
```

True if the location is at the end of a line in the document.

Note that the "end" of a line is equal to its length (one greater than the final index), since there is a space at the end of the line for the cursor to rest.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_end_of_document_line\(location\) "Permanent link") |  | The location to examine. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if and only if the document is at the end of a line in the document. |

### is\_end\_of\_wrapped\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_end_of_wrapped_line "Permanent link")

```
is_end_of_wrapped_line()
```

True if the location is at the end of a wrapped line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_end_of_wrapped_line\(location\) "Permanent link") |  | The location to examine. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if and only if the cursor is on the last wrapped section of *any* line. |

### is\_first\_document\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_first_document_line "Permanent link")

```
is_first_document_line()
```

Check if the given location is on the first line in the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_first_document_line\(location\) "Permanent link") |  | The location to examine. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if and only if the cursor is on the first line of the document. |

### is\_first\_wrapped\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_first_wrapped_line "Permanent link")

```
is_first_wrapped_line()
```

Check if the given location is on the first wrapped section of the first line in the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_first_wrapped_line\(location\) "Permanent link") |  | The location to examine. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if and only if the cursor is on the first wrapped section of the first line. |

### is\_last\_document\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_last_document_line "Permanent link")

```
is_last_document_line()
```

Check if the given location is on the last line of the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_last_document_line\(location\) "Permanent link") |  | The location to examine. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True when the location is on the last line of the document. |

### is\_last\_wrapped\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_last_wrapped_line "Permanent link")

```
is_last_wrapped_line()
```

Check if the given location is on the last wrapped section of the last line.

That is, the cursor is *visually* on the last rendered row.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_last_wrapped_line\(location\) "Permanent link") |  | The location to examine. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if and only if the cursor is on the last section of the last line. |

### is\_start\_of\_document [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_start_of_document "Permanent link")

```
is_start_of_document()
```

Check if a location is at the start of the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_start_of_document\(location\) "Permanent link") |  | The location to examine. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if and only if the cursor is at document location (0, 0) |

### is\_start\_of\_document\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_start_of_document_line "Permanent link")

```
is_start_of_document_line()
```

True when the location is at the start of the first document line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_start_of_document_line\(location\) "Permanent link") |  | The location to check. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the location is at column index 0. |

### is\_start\_of\_wrapped\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_start_of_wrapped_line "Permanent link")

```
is_start_of_wrapped_line()
```

True when the location is at the start of the first wrapped line.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.DocumentNavigator.is_start_of_wrapped_line\(location\) "Permanent link") |  | The location to check. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[bool](https://docs.python.org/3/library/functions.html#bool)` | True if the location is at column index 0. |

## Edit [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit "Permanent link")

```
Edit(
    text,
    from_location,
    to_location,
    maintain_selection_offset,
)
```

Implements the Undoable protocol to replace text at some range within a document.

### bottom [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.bottom "Permanent link")

```
bottom
```

The Location impacted by this edit that is nearest the end of the document.

### from\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.from_location "Permanent link")

```
from_location
```

The start location of the insert.

### maintain\_selection\_offset [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.maintain_selection_offset "Permanent link")

```
maintain_selection_offset
```

If True, the selection will maintain its offset to the replacement range.

### text [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.text "Permanent link")

```
text
```

The text to insert. An empty string is equivalent to deletion.

### to\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.to_location "Permanent link")

```
to_location
```

The end location of the insert

### top [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.top "Permanent link")

```
top
```

The Location impacted by this edit that is nearest the start of the document.

### after [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.after "Permanent link")

```
after()
```

Hook for running code after an Edit has been performed via `Edit.do` *and* side effects such as re-wrapping the document and refreshing the display have completed.

For example, we can't record cursor visual offset until we know where the cursor will land *after* wrapping has been performed, so we must wait until here to do it.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `text_area` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.after\(text_area\) "Permanent link") |  | The `TextArea` this operation was performed on. | *required* |

### do [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.do "Permanent link")

```
do(, =True)
```

Perform the edit operation.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `text_area` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.do\(text_area\) "Permanent link") |  | The `TextArea` to perform the edit on. | *required* |
| #### `record_selection` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.do\(record_selection\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | If True, record the current selection in the TextArea so that it may be restored if this Edit is undone in the future. | `True` |

Returns:

| Type | Description |
| --- | --- |
|  | An `EditResult` containing information about the replace operation. |

### undo [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.undo "Permanent link")

```
undo()
```

Undo the edit operation.

Looks at the data stored in the edit, and performs the inverse operation of `Edit.do`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `text_area` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Edit.undo\(text_area\) "Permanent link") |  | The `TextArea` to undo the insert operation on. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | An `EditResult` containing information about the replace operation. |

## EditHistory [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditHistory "Permanent link")

```
EditHistory(
    max_checkpoints,
    checkpoint_timer,
    checkpoint_max_characters,
)
```

Manages batching/checkpointing of Edits into groups that can be undone/redone in the TextArea.

### checkpoint\_max\_characters [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditHistory.checkpoint_max_characters "Permanent link")

```
checkpoint_max_characters
```

Maximum number of characters that can appear in a batch before a new batch is formed.

### checkpoint\_timer [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditHistory.checkpoint_timer "Permanent link")

```
checkpoint_timer
```

Maximum number of seconds since last edit until a new batch is created.

### redo\_stack [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditHistory.redo_stack "Permanent link")

```
redo_stack
```

A copy of the redo stack, with references to the original Edits.

### undo\_stack [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditHistory.undo_stack "Permanent link")

```
undo_stack
```

A copy of the undo stack, with references to the original Edits.

### checkpoint [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditHistory.checkpoint "Permanent link")

```
checkpoint()
```

Ensure the next recorded edit starts a new batch.

### clear [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditHistory.clear "Permanent link")

```
clear()
```

Completely clear the history.

### record [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditHistory.record "Permanent link")

```
record()
```

Record an Edit so that it may be undone and redone.

Determines whether to batch the Edit with previous Edits, or create a new batch/checkpoint.

This method must be called exactly once per edit, in chronological order.

A new batch/checkpoint is created when:

- The undo stack is empty.
- The checkpoint timer expires.
- The maximum number of characters permitted in a checkpoint is reached.
- A redo is performed (we should not add new edits to a batch that has been redone).
- The programmer has requested a new batch via a call to `force_new_batch`.
- e.g. the TextArea widget may call this method in some circumstances.
- Clicking to move the cursor elsewhere in the document should create a new batch.
- Movement of the cursor via a keyboard action that is NOT an edit.
- Blurring the TextArea creates a new checkpoint.
- The current edit involves a deletion/replacement and the previous edit did not.
- The current edit is a pure insertion and the previous edit was not.
- The edit involves insertion or deletion of one or more newline characters.
- An edit which inserts more than a single character (a paste) gets an isolated batch.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `edit` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditHistory.record\(edit\) "Permanent link") |  | The edit to record. | *required* |

## EditResult [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditResult "Permanent link")

```
EditResult(end_location, replaced_text)
```

Contains information about an edit that has occurred.

### end\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditResult.end_location "Permanent link")

```
end_location
```

The new end Location after the edit is complete.

### replaced\_text [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.EditResult.replaced_text "Permanent link")

```
replaced_text
```

The text that was replaced.

## LanguageDoesNotExist [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.LanguageDoesNotExist "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when the user tries to use a language which does not exist. This means a language which is not builtin, or has not been registered.

## Selection [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Selection "Permanent link")

Bases: `[NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")`

A range of characters within a document from a start point to the end point. The location of the cursor is always considered to be the `end` point of the selection. The selection is inclusive of the minimum point and exclusive of the maximum point.

### end [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Selection.end "Permanent link")

```
end = (0, 0)
```

The end location of the selection.

If you were to click and drag a selection inside a text-editor, this is where you *finished* dragging.

### is\_empty [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Selection.is_empty "Permanent link")

```
is_empty
```

Return True if the selection has 0 width, i.e. it's just a cursor.

### start [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Selection.start "Permanent link")

```
start = (0, 0)
```

The start location of the selection.

If you were to click and drag a selection inside a text-editor, this is where you *started* dragging.

### cursor [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Selection.cursor "Permanent link")

```
cursor()
```

Create a Selection with the same start and end point - a "cursor".

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.Selection.cursor\(location\) "Permanent link") |  | The location to create the zero-width Selection. | *required* |

## SyntaxAwareDocument [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument "Permanent link")

```
SyntaxAwareDocument(, )
```

Bases:

A subclass of Document which also maintains a tree-sitter syntax tree when the document is edited.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `text` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The initial text contained in the document. | *required* |
| ### `language` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument\(language\) "Permanent link") | `Language` | The tree-sitter language to use. | *required* |

### language [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.language "Permanent link")

```
language =
```

The tree-sitter Language.

### get\_line [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.get_line "Permanent link")

```
get_line(index)
```

Return the string representing the line, not including new line characters.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `line_index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.get_line\(line_index\) "Permanent link") |  | The index of the line. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The string representing the line. |

### prepare\_query [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.prepare_query "Permanent link")

```
prepare_query()
```

Prepare a tree-sitter tree query.

Queries should be prepared once, then reused.

To execute a query, call `query_syntax_tree`.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `query` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.prepare_query\(query\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The string query to prepare. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `Query \| None` | The prepared query. |

### query\_syntax\_tree [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.query_syntax_tree "Permanent link")

```
query_syntax_tree(, =None, =None)
```

Query the tree-sitter syntax tree.

The default implementation always returns an empty list.

To support querying in a subclass, this must be implemented.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `query` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.query_syntax_tree\(query\) "Permanent link") | `Query` | The tree-sitter Query to perform. | *required* |
| #### `start_point` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.query_syntax_tree\(start_point\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)] \| None` | The (row, column byte) to start the query at. | `None` |
| #### `end_point` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.query_syntax_tree\(end_point\) "Permanent link") | `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)] \| None` | The (row, column byte) to end the query at. | `None` |

Returns:

| Type | Description |
| --- | --- |
| `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [list](https://docs.python.org/3/library/stdtypes.html#list)['Node']]` | A tuple containing the nodes and text captured by the query. |

### replace\_range [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.replace_range "Permanent link")

```
replace_range(, , )
```

Replace text at the given range.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.replace_range\(start\) "Permanent link") |  | A tuple (row, column) where the edit starts. | *required* |
| #### `end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.replace_range\(end\) "Permanent link") |  | A tuple (row, column) where the edit ends. | *required* |
| #### `text` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.SyntaxAwareDocument.replace_range\(text\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The text to insert between start and end. | *required* |

Returns:

| Type | Description |
| --- | --- |
|  | The new end location after the edit is complete. |

## TextAreaTheme [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme "Permanent link")

```
TextAreaTheme(
    name,
    base_style=None,
    gutter_style=None,
    cursor_style=None,
    cursor_line_style=None,
    cursor_line_gutter_style=None,
    bracket_matching_style=None,
    selection_style=None,
    syntax_styles=dict(),
)
```

A theme for the `TextArea` widget.

Allows theming the general widget (gutter, selections, cursor, and so on) and mapping of tree-sitter tokens to Rich styles.

For example, consider the following snippet from the `markdown.scm` highlight query file. We've assigned the `heading_content` token type to the name `heading`.

```
(heading_content) @heading
```

Now, we can map this `heading` name to a Rich style, and it will be styled as such in the `TextArea`, assuming a parser which returns a `heading_content` node is used (as will be the case when language="markdown").

```
TextAreaTheme('my_theme', syntax_styles={'heading': Style(color='cyan', bold=True)})
```

We can register this theme with our `TextArea` using the method, and headings in our markdown files will be styled bold cyan.

### base\_style [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.base_style "Permanent link")

```
base_style = None
```

The background style of the text area. If `None` the parent style will be used.

### bracket\_matching\_style [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.bracket_matching_style "Permanent link")

```
bracket_matching_style = None
```

The style to apply to matching brackets. If `None`, a legible Style will be generated.

### cursor\_line\_gutter\_style [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.cursor_line_gutter_style "Permanent link")

```
cursor_line_gutter_style = None
```

The style to apply to the gutter of the line the cursor is on. If `None`, a legible Style will be generated.

### cursor\_line\_style [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.cursor_line_style "Permanent link")

```
cursor_line_style = None
```

The style to apply to the line the cursor is on.

### cursor\_style [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.cursor_style "Permanent link")

```
cursor_style = None
```

The style of the cursor. If `None`, a legible Style will be generated.

### gutter\_style [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.gutter_style "Permanent link")

```
gutter_style = None
```

The style of the gutter. If `None`, a legible Style will be generated.

### name [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.name "Permanent link")

```
name
```

The name of the theme.

### selection\_style [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.selection_style "Permanent link")

```
selection_style = None
```

The style of the selection. If `None` a default selection Style will be generated.

### syntax\_styles [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.syntax_styles "Permanent link")

```
syntax_styles = field(default_factory=dict)
```

The mapping of tree-sitter names from the `highlight_query` to Rich styles.

### apply\_css [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.apply_css "Permanent link")

```
apply_css()
```

Apply CSS rules from a TextArea to be used for fallback styling.

If any attributes in the theme aren't supplied, they'll be filled with the appropriate base CSS (e.g. color, background, etc.) and component CSS (e.g. text-area--cursor) from the supplied TextArea.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `text_area` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.apply_css\(text_area\) "Permanent link") |  | The TextArea instance to retrieve fallback styling from. | *required* |

### builtin\_themes [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.builtin_themes "Permanent link")

```
builtin_themes()
```

Get a list of all builtin TextAreaThemes.

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[]` | A list of all builtin TextAreaThemes. |

### get\_builtin\_theme [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.get_builtin_theme "Permanent link")

```
get_builtin_theme()
```

Get a `TextAreaTheme` by name.

Given a `theme_name`, return the corresponding `TextAreaTheme` object.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `theme_name` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.get_builtin_theme\(theme_name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The name of the theme. | *required* |

Returns:

| Type | Description |
| --- | --- |
| ` \| None` | The `TextAreaTheme` corresponding to the name or `None` if the theme isn't found. |

### get\_highlight [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.get_highlight "Permanent link")

```
get_highlight()
```

Return the Rich style corresponding to the name defined in the tree-sitter highlight query for the current theme.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `name` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.TextAreaTheme.get_highlight\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | The name of the highlight. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Style](https://rich.readthedocs.io/en/stable/reference/style.html#rich.style.Style "rich.style.Style") \| None` | The `Style` to use for this highlight, or `None` if no style. |

## ThemeDoesNotExist [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.ThemeDoesNotExist "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Raised when the user tries to use a theme which does not exist. This means a theme which is not builtin, or has not been registered.

## WrappedDocument [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument "Permanent link")

```
WrappedDocument(, =0, =4)
```

A view into a Document which wraps the document at a certain width and can be queried to retrieve lines from the *wrapped* version of the document.

Allows for incremental updates, ensuring that we only re-wrap ranges of the document that were influenced by edits.

By default, a WrappedDocument is wrapped with width=0 (no wrapping). To wrap the document, use the wrap() method.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `document` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument\(document\) "Permanent link") |  | The document to wrap. | *required* |
| ### `width` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The width to wrap at. | `0` |
| ### `tab_width` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument\(tab_width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The maximum width to consider for tab characters. | `4` |

### document [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.document "Permanent link")

```
document =
```

The document wrapping is performed on.

### height [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.height "Permanent link")

```
height
```

The height of the wrapped document.

### lines [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.lines "Permanent link")

```
lines
```

The lines of the wrapped version of the Document.

Each index in the returned list represents a line index in the raw document. The list\[str\] at each index is the content of the raw document line split into multiple lines via wrapping.

Note that this is expensive to compute and is not cached.

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]]` | A list of lines from the wrapped version of the document. |

### wrapped [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.wrapped "Permanent link")

```
wrapped
```

True if the content is wrapped. This is not the same as wrapping being "enabled". For example, an empty document can have wrapping enabled, but no wrapping has actually occurred.

In other words, this is True if the length of any line in the document is greater than the available width.

### get\_offsets [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_offsets "Permanent link")

```
get_offsets()
```

Given a line index, get the offsets within that line where wrapping should occur for the current document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `line_index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_offsets\(line_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the line within the document. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` | When `line_index` is out of bounds. |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[int](https://docs.python.org/3/library/functions.html#int)]` | The offsets within the line where wrapping should occur. |

### get\_sections [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_sections "Permanent link")

```
get_sections()
```

Return the sections for the given line index.

When wrapping is enabled, a single line in the document can visually span multiple lines. The list returned represents that visually (each string in the list represents a single section (y-offset) after wrapping happens).

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `line_index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_sections\(line_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the line to get sections for. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]` | The wrapped line as a list of strings. |

### get\_tab\_widths [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_tab_widths "Permanent link")

```
get_tab_widths()
```

Return a list of the tab widths for the given line index.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `line_index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_tab_widths\(line_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the line in the document. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[list](https://docs.python.org/3/library/stdtypes.html#list)[[int](https://docs.python.org/3/library/functions.html#int)]` | An ordered list of the expanded width of the tabs in the line. |

### get\_target\_document\_column [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_target_document_column "Permanent link")

```
get_target_document_column(, , )
```

Given a line index and the offsets within the wrapped version of that line, return the corresponding column index in the raw document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `line_index` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_target_document_column\(line_index\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The index of the line in the document. | *required* |
| #### `x_offset` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_target_document_column\(x_offset\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The x-offset within the wrapped line. | *required* |
| #### `y_offset` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.get_target_document_column\(y_offset\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The y-offset within the wrapped line (supports negative indexing). | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[int](https://docs.python.org/3/library/functions.html#int)` | The column index corresponding to the line index and y offset. |

### location\_to\_offset [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.location_to_offset "Permanent link")

```
location_to_offset()
```

Convert a location in the document to an offset within the wrapped/visual display of the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `location` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.location_to_offset\(location\) "Permanent link") |  | The location in the document. | *required* |

Returns:

| Type | Description |
| --- | --- |
| `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | The Offset in the document's visual display corresponding to the given location. |

### offset\_to\_location [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.offset_to_location "Permanent link")

```
offset_to_location()
```

Given an offset within the wrapped/visual display of the document, return the corresponding location in the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `offset` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.offset_to_location\(offset\) "Permanent link") | `[Offset](https://textual.textualize.io/api/geometry/#textual.geometry.Offset " Offset (textual.geometry.Offset)")` | The y-offset within the document. | *required* |

Raises:

| Type | Description |
| --- | --- |
| `[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` | When the given offset does not correspond to a line in the document. |

Returns:

| Type | Description |
| --- | --- |
|  | The Location in the document corresponding to the given offset. |

### wrap [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.wrap "Permanent link")

```
wrap(, =None)
```

Wrap and cache all lines in the document.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `width` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.wrap\(width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int)` | The width to wrap at. 0 for no wrapping. | *required* |
| #### `tab_width` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.wrap\(tab_width\) "Permanent link") | `[int](https://docs.python.org/3/library/functions.html#int) \| None` | The maximum width to consider for tab characters. If None, reuse the tab width. | `None` |

### wrap\_range [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.wrap_range "Permanent link")

```
wrap_range(, , )
```

Incrementally recompute wrapping based on a performed edit.

This must be called *after* the source document has been edited.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| #### `start` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.wrap_range\(start\) "Permanent link") |  | The start location of the edit that was performed in document-space. | *required* |
| #### `old_end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.wrap_range\(old_end\) "Permanent link") |  | The old end location of the edit in document-space. | *required* |
| #### `new_end` [¶](https://textual.textualize.io/widgets/text_area/#textual.widgets.text_area.WrappedDocument.wrap_range\(new_end\) "Permanent link") |  | The new end location of the edit in document-space. | *required* |