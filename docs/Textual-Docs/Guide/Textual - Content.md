---
title: "Textual - Content"
source: "https://textual.textualize.io/guide/content/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Content¶

The *content* of widget (displayed within the widget's borders) is typically specified in a call to [`Static.update`](https://textual.textualize.io/widgets/static/#textual.widgets.Static.update " update") or returned from [`render()`](https://textual.textualize.io/api/widget/#textual.widget.Widget.render " render") in the case of [custom widgets](https://textual.textualize.io/guide/widgets/#custom-widgets).

There are a few ways for you to specify this content.

- Text — a string containing [markup](https://textual.textualize.io/guide/content/#markup).
- [Content](https://textual.textualize.io/guide/content/#content-class) objects — for more advanced control over output.
- Rich renderables — any object that may be printed with [Rich](https://rich.readthedocs.io/en/latest/).

In this chapter, we will cover all these methods.

## Markup¶

When building a custom widget you can embed color and style information in the string returned from the Widget's [`render()`](https://textual.textualize.io/api/widget/#textual.widget.Widget.render " render") method. Markup is specified as a string which contains Text enclosed in square brackets (`[]`) won't appear in the output, but will modify the style of the text that follows. This is known as *Textual markup*.

Before we explore Textual markup in detail, let's first demonstrate some of what it can do. In the following example, we have two widgets. The top has Textual markup enabled, while the bottom widget has Textual markup *disabled*.

Notice how the markup *tags* change the style in the first widget, but are left unaltered in the second:

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.widgets import Static

TEXT1 = """\
Hello, [bold $text on $primary]World[/]!

[@click=app.notify('Hello, World!')]Click me[/]
"""

TEXT2 = """\
Markup will [bold]not[/bold] be displayed.

Tags will be left in the output.

"""

class ContentApp(App):
    CSS = """
    Screen {
        Static {
            height: 1fr;
        }
        #text1 { background: $primary-muted; }
        #text2 { background: $error-muted; }
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(TEXT1, id="text1")
        yield Static(TEXT2, id="text2", markup=False)  

if __name__ == "__main__":
    app = ContentApp()
    app.run()
```

1. With `markup=False`, tags have no effect and left in the output.

### Playground¶

Textual comes with a markup playground where you can enter Textual markup and see the result's live. To launch the playground, run the following command:

```
python -m textual.markup
```

You can experiment with markup by entering it in to the textarea at the top of the terminal, and seeing the results in the lower pane:

<!-- SVG content removed by SVG Remover -->

You might find it helpful to try out some of the examples from this guide in the playground.

What are Variables?

You may have noticed the "Variables" tab. This allows you to experiment with [variable substitution](https://textual.textualize.io/guide/content/#markup-variables).

### Tags¶

There are two types of tag: an *opening* tag which starts a style change, and a *closing* tag which ends a style change. An opening tag looks like this:

```
[bold]
```

The second type of tag, known as a *closing* tag, is almost identical, but starts with a forward slash inside the first square bracket. A closing tag looks like this:

```
[/bold]
```

A closing tag marks the end of a style from the corresponding opening tag.

By wrapping text in an opening and closing tag, we can apply the style to just the characters we want. For example, the following makes just the first word in "Hello, World!" bold:

```
[bold]Hello[/bold], World!
```

Note how the tags change the style but are removed from the output:

<!-- SVG content removed by SVG Remover -->

You can use any number of tags. If tags overlap their styles are combined. For instance, the following combines the bold and italic styles:

```
[bold]Bold [italic]Bold and italic[/italic][/bold]
```

Here's the output:

<!-- SVG content removed by SVG Remover -->

#### Auto-closing tags¶

A closing tag without any style information (i.e. `[/]`) is an *auto-closing* tag. Auto-closing tags will close the last opened tag.

The following uses an auto-closing tag to end the bold style:

```
[bold]Hello[/], World!
```

This is equivalent to the following (but saves typing a few characters):

```
[bold]Hello[/bold], World!
```

Auto-closing tags recommended when it is clear which tag they are intended to close.

### Styles¶

Tags may contain any number of the following values:

| Style | Abbreviation | Description |
| --- | --- | --- |
| `bold` | `b` | **Bold text** |
| `dim` | `d` | Dim text (slightly transparent) |
| `italic` | `i` | *Italic text* |
| `underline` | `u` | Underlined text |
| `strike` | `s` | ~~Strikethrough text~~ |
| `reverse` | `r` | Reversed colors text (background swapped with foreground) |

These styles can be abbreviate to save typing. For example `[bold]` and `[b]` are equivalent.

Styles can also be combined within the same tag, so `[bold italic]` produces text that is both bold *and* italic.

#### Inverting styles¶

You can invert a style by preceding it with the word `not`. This is useful if you have text with a given style, but you temporarily want to disable it.

For instance, the following starts with `[bold]`, which would normally make the rest of the text bold. However, the `[not bold]` tag disables bold until the corresponding `[/not bold]` tag:

```
[bold]This is bold [not bold]This is not bold[/not bold] This is bold.
```

Here's what this markup will produce:

<!-- SVG content removed by SVG Remover -->

### Colors¶

Colors may specified in the same way as a CSS [<color>](https://textual.textualize.io/css_types/color). Here are a few examples:

```
[#ff0000]HTML hex style[/]
[rgba(0,255,0)]HTML RGB style[/]
```

You can also any of the [named colors](https://textual.textualize.io/css_types/color).

```
[chartreuse]This is a green color[/]
[sienna]This is a kind of yellow-brown.[/]
```

Colors may also include an *alpha* component, which makes the color fade in to the background. For instance, if we specify the color with `rgba(...)`, then we can add an alpha component between 0 and 1. An alpha of 0 is fully transparent (and therefore invisible). An alpha of 1 is fully opaque, and equivalent to a color without an alpha component. A value between 0 and 1 results in a faded color.

In the following example we have an alpha of 0.5, which will produce a color half way between the background and solid green:

```
[rgba(0, 255, 0, 0.5)]Faded green (and probably hard to read)[/]
```

Here's the output:

<!-- SVG content removed by SVG Remover -->

Warning

Be careful when using colors with an alpha component. Text that is blended too much with the background may become hard to read.

#### Auto colors¶

You can also specify a color as "auto", which is a special value that tells Textual to pick either white or black text -- whichever has the best contrast.

For example, the following will produce either white or black text (I haven't checked) on a sienna background:

```
[auto on sienna]This should be fairly readable.
```

#### Opacity¶

While you can set the opacity in the color itself by adding an alpha component to the color, you can also modify the alpha of the previous color with a percentage.

For example, the addition of `50%` will result in a color half way between the background and "red":

```
[red 50%]This is in faded red[/]
```

#### Background colors¶

Background colors may be specified by preceding a color with the world `on`. Here's an example:

```
[on #ff0000]Background is bright red.
```

Background colors may also have an alpha component (either in the color itself or with a percentage). This will result in a color that is blended with the widget's parent (or Screen).

Here's an example that tints the background with 20% red:

```
[on #ff0000 20%]The background has a red tint.[/]
```

Here's the output:

<!-- SVG content removed by SVG Remover -->

### CSS variables¶

You can also use CSS variables in markup, such as those specified in the [design](https://textual.textualize.io/guide/design/#base-colors) guide.

To use any of the theme colors, simple use the name of the color including the `$` at the first position. For example, this will display text in the *accent* color:

```
[$accent]Accent color[/]
```

You may also use a color variable in the background position. The following displays text in the 'warning' style on a muted 'warning' background for emphasis:

```
[$warning on $warning-muted]This is a warning![/]
```

Here's the result of that markup:

<!-- SVG content removed by SVG Remover -->

### Links¶

Styles may contain links which will create clickable links that launch your web browser, if supported by your terminal.

To create a link add `link=` followed by your link in quotes (single or double). For instance, the following create a clickable link:

```
[link="https://www.willmcgugan.com"]Visit my blog![/link]
```

This will produce the following output:

```js
Visit my blog!
```

### Actions¶

In addition to links, you can also markup content that runs [actions](https://textual.textualize.io/guide/actions/) when clicked. To do this create a style that starts with `@click=` and is followed by the action you wish to run.

For instance, the following will highlight the word "bell", which plays the terminal bell sound when click:

```
Play the [@click=app.bell]bell[/]
```

Here's what it looks like:

<!-- SVG content removed by SVG Remover -->

We've used an [auto-closing](https://textual.textualize.io/guide/content/#auto-closing-tags) to close the click action here. If you do need to close the tag explicitly, you can omit the action:

```
Play the [@click=app.bell]bell[/@click=]
```

Actions may be combined with other styles, so you could set the style of the clickable link:

```
Play the [on $success 30% @click=app.bell]bell[/]
```

Here's what that looks like:

<!-- SVG content removed by SVG Remover -->

## Content class¶

Under the hood, Textual will convert markup into a [Content](https://textual.textualize.io/api/content/#textual.content.Content " Content") instance. You can also return a Content object directly from `render()`. This can give you more flexibility beyond the markup.

To clarify, here's a render method that returns a string with markup:

```
class WelcomeWidget(Widget):
    def render(self) -> RenderResult:
        return "[b]Hello, World![/b]"
```

This is roughly the equivalent to the following code:

```
class WelcomeWidget(Widget):
    def render(self) -> RenderResult:
        return Content.from_markup("[b]Hello, World![/b]")
```

### Constructing content¶

The [Content](https://textual.textualize.io/api/content/#textual.content.Content " Content") class accepts a default string in it's constructor.

Here's an example:

```
Content("hello, World!")
```

Note that if you construct Content in this way, it *won't* process markup (any square brackets will be displayed literally).

If you want markup, you can create a `Content` with the [Content.from\_markup](https://textual.textualize.io/api/content/#textual.content.Content.from_markup " from_markup") alternative constructor:

```
Content.from_markup("hello, [bold]World[/bold]!")
```

### Styling content¶

You can add styles to content with the [stylize](https://textual.textualize.io/api/content/#textual.content.Content.stylize " stylize") or [stylize\_before](https://textual.textualize.io/api/content/#textual.content.Content.stylize " stylize") methods.

For instance, in the following code we create content with the text "Hello, World!" and style "World" to be bold:

```
content = Content("Hello, World!")
content = content.stylize(7, 12, "bold")
```

Note that `Content` is *immutable* and methods will return new instances rather than updating the current instance.

### Markup variables¶

You may be tempted to combine markup with Python's f-strings (or other string template system). Something along these lines:

```
class WelcomeWidget(Widget):
    def render(self) -> RenderResult:
        name = "Will"
        return f"Hello [bold]{name}[/bold]!"
```

While this is straightforward and intuitive, it can potentially break in subtle ways. If the 'name' variable contains square brackets, these may be interpreted as markup. For instance if the user entered their name at some point as "\[magenta italic\]Will" then your app will display those styles where you didn't intend them to be.

We can avoid this problem by relying on the [Content.from\_markup](https://textual.textualize.io/api/content/#textual.content.Content.from_markup " from_markup") method to insert the variables for us. If you supply variables as keyword arguments, these will be substituted in the markup using the same syntax as [string.Template](https://docs.python.org/3/library/string.html#template-strings). Any square brackets in the variables will be present in the output, but won't change the styles.

Here's how we can fix the previous example:

```
return Content.from_markup("hello [bold]$name[/bold]!", name=name)
```

You can experiment with this feature by entering a dictionary of variables in the variables text-area.

Here's what that looks like:

<!-- SVG content removed by SVG Remover -->

## Rich renderables¶

Textual supports Rich *renderables*, which means you can display any object that works with Rich, such as Rich's [Text](https://rich.readthedocs.io/en/latest/text.html) object.

The Content class is preferred for simple text, as it supports more of Textual's features. But you can display any of the objects in the [Rich library](https://github.com/Textualize/rich) (or ecosystem) within a widget.

Here's an example which displays its own code using Rich's [Syntax](https://rich.readthedocs.io/en/latest/syntax.html) object.

<!-- SVG content removed by SVG Remover -->

```
from rich.syntax import Syntax

from textual.app import App, ComposeResult, RenderResult
from textual.reactive import reactive
from textual.widget import Widget

class CodeView(Widget):
    """Widget to display Python code."""

    DEFAULT_CSS = """
    CodeView { height: auto; }
    """

    code = reactive("")

    def render(self) -> RenderResult:
        # Syntax is a Rich renderable that displays syntax highlighted code
        syntax = Syntax(self.code, "python", line_numbers=True, indent_guides=True)
        return syntax

class CodeApp(App):
    """App to demonstrate Rich renderables in Textual."""

    def compose(self) -> ComposeResult:
        with open(__file__) as self_file:
            code = self_file.read()
        code_view = CodeView()
        code_view.code = code
        yield code_view

if __name__ == "__main__":
    app = CodeApp()
    app.run()
```