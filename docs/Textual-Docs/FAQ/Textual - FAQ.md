---
title: "Textual - FAQ"
source: "https://textual.textualize.io/FAQ/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Frequently Asked Questions¶

Welcome to the Textual FAQ. Here we try and answer any question that comes up frequently. If you can't find what you are looking for here, see our other [help](https://textual.textualize.io/help/) channels.

## Does Textual support images?¶

Textual doesn't have built-in support for images yet, but it is on the [Roadmap](https://textual.textualize.io/roadmap/).

See also the [rich-pixels](https://github.com/darrenburns/rich-pixels) project for a Rich renderable for images that works with Textual.

---

## How can I fix ImportError cannot import name ComposeResult from textual.app ?¶

You likely have an older version of Textual. You can install the latest version by adding the `-U` switch which will force pip to upgrade.

The following should do it:

```
pip install textual-dev -U
```

---

## How can I select and copy text in a Textual app?¶

Running a Textual app puts your terminal in to *application mode* which disables clicking and dragging to select text. Most terminal emulators offer a modifier key which you can hold while you click and drag to restore the behavior you may expect from the command line. The exact modifier key depends on the terminal and platform you are running on.

- **iTerm** Hold the OPTION key.
- **Gnome Terminal** Hold the SHIFT key.
- **Windows Terminal** Hold the SHIFT key.

Refer to the documentation for your terminal emulator, if it is not listed above.

---

## How can I set a translucent app background?¶

Some terminal emulators have a translucent background feature which allows the desktop underneath to be partially visible.

This feature is unlikely to work with Textual, as the translucency effect requires the use of ANSI background colors, which Textual doesn't use. Textual uses 16.7 million colors where available which enables consistent colors across all platforms and additional effects which aren't possible with ANSI colors.

For more information on ANSI colors in Textual, see [Why no ANSI Themes?](https://textual.textualize.io/FAQ/#why-doesnt-textual-support-ansi-themes).

---

## How do I center a widget in a screen?¶

Tip

See [*How To Center Things*](https://textual.textualize.io/how-to/center-things/) in the Textual documentation for a more comprehensive answer to this question.

To center a widget within a container use [`align`](https://textual.textualize.io/styles/align/). But remember that `align` works on the *children* of a container, it isn't something you use on the child you want centered.

For example, here's an app that shows a `Button` in the middle of a `Screen`:

```
from textual.app import App, ComposeResult
from textual.widgets import Button

class ButtonApp(App):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("PUSH ME!")

if __name__ == "__main__":
    ButtonApp().run()
```

If you use the above on multiple widgets, you'll find they appear to "left-align" in the center of the screen, like this:

```
+-----+
|     |
+-----+

+---------+
|         |
+---------+

+---------------+
|               |
+---------------+
```

If you want them more like this:

```
+-----+
     |     |
     +-----+

   +---------+
   |         |
   +---------+

+---------------+
|               |
+---------------+
```

The best approach is to wrap each widget in a [`Center` container](https://textual.textualize.io/api/containers/#textual.containers.Center) that individually centers it. For example:

```
from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Button

class ButtonApp(App):

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Center(Button("PUSH ME!"))
        yield Center(Button("AND ME!"))
        yield Center(Button("ALSO PLEASE PUSH ME!"))
        yield Center(Button("HEY ME ALSO!!"))

if __name__ == "__main__":
    ButtonApp().run()
```

---

## How do I fix WorkerDeclarationError?¶

Textual version 0.31.0 requires that you set `thread=True` on the `@work` decorator if you want to run a threaded worker.

If you want a threaded worker, you would declare it in the following way:

```
@work(thread=True)
def run_in_background():
    ...
```

If you *don't* want a threaded worker, you should make your work function `async`:

```
@work()
async def run_in_background():
    ...
```

This change was made because it was too easy to accidentally create a threaded worker, which may produce unexpected results.

---

## How do I pass arguments to an app?¶

When creating your `App` class, override `__init__` as you would when inheriting normally. For example:

```
from textual.app import App, ComposeResult
from textual.widgets import Static

class Greetings(App[None]):

    def __init__(self, greeting: str="Hello", to_greet: str="World") -> None:
        self.greeting = greeting
        self.to_greet = to_greet
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Static(f"{self.greeting}, {self.to_greet}")
```

Then the app can be run, passing in various arguments; for example:

```
# Running with default arguments.
Greetings().run()

# Running with a keyword argument.
Greetings(to_greet="davep").run()

# Running with both positional arguments.
Greetings("Well hello", "there").run()
```

---

## No widget called TextLog¶

The `TextLog` widget was renamed to `RichLog` in Textual 0.32.0. You will need to replace all references to `TextLog` in your code, with `RichLog`. Most IDEs will have a search and replace function which will help you do this.

Here's how you should import RichLog:

```
from textual.widgets import RichLog
```

---

## Why do some key combinations never make it to my app?¶

Textual can only ever support key combinations that are passed on by your terminal application. Which keys get passed on can differ from terminal to terminal, and from operating system to operating system.

Because of this it's best to stick to key combinations that are known to be universally-supported; these include the likes of:

- Letters
- Numbers
- Numbered function keys (especially F1 through F10)
- Space
- Return
- Arrow, home, end and page keys
- Control
- Shift

When [creating bindings for your application](https://textual.textualize.io/guide/input/#bindings) we recommend picking keys and key combinations from the above.

Keys that aren't normally passed through by terminals include Cmd and Option on macOS, and the Windows key on Windows.

If you need to test what [key combinations](https://textual.textualize.io/guide/input/#keyboard-input) work in different environments you can try them out with `textual keys`.

---

## Why doesn't Textual look good on macOS?¶

You may find that the default macOS Terminal.app doesn't render Textual apps (and likely other TUIs) very well, particularly when it comes to box characters. For instance, you may find it displays misaligned blocks and lines like this:

![Screenshot 2023-06-19 at 10 43 02](https://github.com/Textualize/textual/assets/554369/e61f3876-3dd1-4ac8-b380-22922c89c7d6)

You can (mostly) fix this by opening settings -> profiles > Text tab, and changing the font settings. We have found that Menlo Regular font, with a character spacing of 1 and line spacing of 0.805 produces reasonable results. If you want to use another font, you may have to tweak the line spacing until you get good results.

![Screenshot 2023-06-19 at 10 44 00](https://github.com/Textualize/textual/assets/554369/0a052a93-b1fd-4327-9d33-d954b51a9ad2)

With these changes, Textual apps render more as intended:

![Screenshot 2023-06-19 at 10 43 23](https://github.com/Textualize/textual/assets/554369/a0c4aa05-c509-4ac1-b0b8-e68ce4433f70)

Even with this *fix*, Terminal.app has a few limitations. It is limited to 256 colors, and can be a little slow compared to more modern alternatives. Fortunately there are a number of free terminal emulators for macOS which produces high quality results.

We recommend any of the following terminals:

- [iTerm2](https://iterm2.com/)
- [Kitty](https://sw.kovidgoyal.net/kitty/)
- [WezTerm](https://wezfurlong.org/wezterm/)

### Terminal.app colors¶

![Screenshot 2023-06-19 at 11 00 12](https://github.com/Textualize/textual/assets/554369/e0555d23-e141-4069-b318-f3965c880208)

### iTerm2 colors¶

![Screenshot 2023-06-19 at 11 00 25](https://github.com/Textualize/textual/assets/554369/9a8cde57-5121-49a7-a2e0-5f6fc871b7a6)

---

## Why doesn't Textual support ANSI themes?¶

Textual will not generate escape sequences for the 16 themeable *ANSI* colors.

This is an intentional design decision we took for for the following reasons:

- Not everyone has a carefully chosen ANSI color theme. Color combinations which may look fine on your system, may be unreadable on another machine. There is very little an app author or Textual can do to resolve this. Asking users to simply pick a better theme is not a good solution, since not all users will know how.
- ANSI colors can't be manipulated in the way Textual can do with other colors. Textual can blend colors and produce light and dark shades from an original color, which is used to create more readable text and user interfaces. Color blending will also be used to power future accessibility features.

Textual has a design system which guarantees apps will be readable on all platforms and terminals, and produces better results than ANSI colors.

There is currently a light and dark version of the design system, but more are planned. It will also be possible for users to customize the source colors on a per-app or per-system basis. This means that in the future you will be able to modify the core colors to blend in with your chosen terminal theme.

Changed in version 0.80.0

Textual added an `ansi_color` boolean to App. If you set this to `True`, then Textual will not attempt to convert ANSI colors. Note that you will lose transparency effects if you enable this setting.

---

## Why doesn't the `DataTable` scroll programmatically?[¶](https://textual.textualize.io/FAQ/#why-doesnt-the-datatable-scroll-programmatically "Permanent link")

If scrolling in your `DataTable` is *apparently* broken, it may be because your `DataTable` is using the default value of `height: auto`. This means that the table will be sized to fit its rows without scrolling, which may cause the *container* (typically the screen) to scroll. If you would like the table itself to scroll, set the height to something other than `auto`, like `100%`.

Note

As of Textual v0.31.0 the `max-height` of a `DataTable` is set to `100%`, this will mean that the above is no longer the default experience.

---

Generated by [FAQtory](https://github.com/willmcgugan/faqtory)