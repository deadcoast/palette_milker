---
title: "Textual - Events and Messages"
source: "https://textual.textualize.io/guide/events/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Events and Messages¶

We've used event handler methods in many of the examples in this guide. This chapter explores [events](https://textual.textualize.io/events/) and messages (see below) in more detail.

## Messages¶

Events are a particular kind of *message* sent by Textual in response to input and other state changes. Events are reserved for use by Textual, but you can also create custom messages for the purpose of coordinating between widgets in your app.

More on that later, but for now keep in mind that events are also messages, and anything that is true of messages is true of events.

## Message Queue¶

Every [App](https://textual.textualize.io/api/app/#textual.app.App " App") and [Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget") object contains a *message queue*. You can think of a message queue as orders at a restaurant. The chef takes an order and makes the dish. Orders that arrive while the chef is cooking are placed in a line. When the chef has finished a dish they pick up the next order in the line.

Textual processes messages in the same way. Messages are picked off a queue and processed (cooked) by a handler method. This guarantees messages and events are processed even if your code can not handle them right away.

This processing of messages is done within an asyncio Task which is started when you mount the widget. The task monitors a queue for new messages and dispatches them to the appropriate handler when they arrive.

Tip

The FastAPI docs have an [excellent introduction](https://fastapi.tiangolo.com/async/) to Python async programming.

By way of an example, let's consider what happens if you were to type "Text" into a `Input` widget. When you hit the T key, Textual creates a [key](https://textual.textualize.io/api/events/#textual.events.Key " Key") event and sends it to the widget's message queue. Ditto for E, X, and T.

The widget's task will pick the first message from the queue (a key event for the T key) and call the `on_key` method with the event as the first argument. In other words it will call `Input.on_key(event)`, which updates the display to show the new letter.

<!-- SVG content removed by SVG Remover -->

When the `on_key` method returns, Textual will get the next event from the queue and repeat the process for the remaining keys. At some point the queue will be empty and the widget is said to be in an *idle* state.

Note

This example illustrates a point, but a typical app will be fast enough to have processed a key before the next event arrives. So it is unlikely you will have so many key events in the message queue.

<!-- SVG content removed by SVG Remover -->

## Default behaviors¶

You may be familiar with Python's [super](https://docs.python.org/3/library/functions.html#super) function to call a function defined in a base class. You will not have to use this in event handlers as Textual will automatically call handler methods defined in a widget's base class(es).

For instance, let's say we are building the classic game of Pong and we have written a `Paddle` widget which extends [Static](https://textual.textualize.io/widgets/static/#textual.widgets.Static " Static"). When a [Key](https://textual.textualize.io/api/events/#textual.events.Key " Key") event arrives, Textual calls `Paddle.on_key` (to respond to Up and Down keys), then `Static.on_key`, and finally `Widget.on_key`.

### Preventing default behaviors¶

If you don't want this behavior you can call [prevent\_default()](https://textual.textualize.io/api/message/#textual.message.Message.prevent_default " prevent_default") on the event object. This tells Textual not to call any more handlers on base classes.

Warning

You won't need `prevent_default` very often. Be sure to know what your base classes do before calling it, or you risk disabling some core features builtin to Textual.

## Bubbling¶

Messages have a `bubble` attribute. If this is set to `True` then events will be sent to a widget's parent after processing. Input events typically bubble so that a widget will have the opportunity to respond to input events if they aren't handled by their children.

The following diagram shows an (abbreviated) DOM for a UI with a container and two buttons. With the "No" button [focused](https://textual.textualize.io/guide/events/#), it will receive the key event first.

<!-- SVG content removed by SVG Remover -->

After Textual calls `Button.on_key` the event *bubbles* to the button's parent and will call `Container.on_key` (if it exists).

<!-- SVG content removed by SVG Remover -->

As before, the event bubbles to its parent (the App class).

<!-- SVG content removed by SVG Remover -->

The App class is always the root of the DOM, so there is nowhere for the event to bubble to.

### Stopping bubbling¶

Event handlers may stop this bubble behavior by calling the [stop()](https://textual.textualize.io/api/message/#textual.message.Message.stop " stop") method on the event or message. You might want to do this if a widget has responded to the event in an authoritative way. For instance when a text input widget responds to a key event it stops the bubbling so that the key doesn't also invoke a key binding.

## Custom messages¶

You can create custom messages for your application that may be used in the same way as events (recall that events are simply messages reserved for use by Textual).

The most common reason to do this is if you are building a custom widget and you need to inform a parent widget about a state change.

Let's look at an example which defines a custom message. The following example creates color buttons which—when clicked—send a custom message.

```
custom01.pyfrom textual.app import App, ComposeResult
from textual.color import Color
from textual.message import Message
from textual.widgets import Static

class ColorButton(Static):
    """A color button."""

    class Selected(Message):
        """Color selected message."""

        def __init__(self, color: Color) -> None:
            self.color = color
            super().__init__()

    def __init__(self, color: Color) -> None:
        self.color = color
        super().__init__()

    def on_mount(self) -> None:
        self.styles.margin = (1, 2)
        self.styles.content_align = ("center", "middle")
        self.styles.background = Color.parse("#ffffff33")
        self.styles.border = ("tall", self.color)

    def on_click(self) -> None:
        # The post_message method sends an event to be handled in the DOM
        self.post_message(self.Selected(self.color))

    def render(self) -> str:
        return str(self.color)

class ColorApp(App):
    def compose(self) -> ComposeResult:
        yield ColorButton(Color.parse("#008080"))
        yield ColorButton(Color.parse("#808000"))
        yield ColorButton(Color.parse("#E9967A"))
        yield ColorButton(Color.parse("#121212"))

    def on_color_button_selected(self, message: ColorButton.Selected) -> None:
        self.screen.styles.animate("background", message.color, duration=0.5)

if __name__ == "__main__":
    app = ColorApp()
    app.run()
```

<!-- SVG content removed by SVG Remover -->

Note the custom message class which extends [Message](https://textual.textualize.io/api/message/#textual.message.Message " Message"). The constructor stores a [color](https://textual.textualize.io/api/color/#textual.color.Color " Color") object which handler methods will be able to inspect.

The message class is defined within the widget class itself. This is not strictly required but recommended, for these reasons:

- It reduces the amount of imports. If you import `ColorButton`, you have access to the message class via `ColorButton.Selected`.
- It creates a namespace for the handler. So rather than `on_selected`, the handler name becomes `on_color_button_selected`. This makes it less likely that your chosen name will clash with another message.

### Sending messages¶

To send a message call the [post\_message()](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.post_message " post_message") method. This will place a message on the widget's message queue and run any message handlers.

It is common for widgets to send messages to themselves, and allow them to bubble. This is so a base class has an opportunity to handle the message. We do this in the example above, which means a subclass could add a `on_color_button_selected` if it wanted to handle the message itself.

## Preventing messages¶

You can *temporarily* disable posting of messages of a particular type by calling [prevent](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.prevent " prevent"), which returns a context manager (used with Python's `with` keyword). This is typically used when updating data in a child widget and you don't want to receive notifications that something has changed.

The following example will play the terminal bell as you type. It does this by handling [Input.Changed](https://textual.textualize.io/widgets/input/#textual.widgets.Input.Changed " Changed") and calling [bell()](https://textual.textualize.io/api/app/#textual.app.App.bell " bell"). There is a Clear button which sets the input's value to an empty string. This would normally also result in a `Input.Changed` event being sent (and the bell playing). Since we don't want the button to make a sound, the assignment to `value` is wrapped within a [prevent](https://textual.textualize.io/api/message_pump/#textual.message_pump.MessagePump.prevent " prevent") context manager.

Tip

In reality, playing the terminal bell as you type would be very irritating -- we don't recommend it!

```
prevent.pyfrom textual.app import App, ComposeResult
from textual.widgets import Button, Input

class PreventApp(App):
    """Demonstrates \`prevent\` context manager."""

    def compose(self) -> ComposeResult:
        yield Input()
        yield Button("Clear", id="clear")

    def on_button_pressed(self) -> None:
        """Clear the text input."""
        input = self.query_one(Input)
        with input.prevent(Input.Changed):  
            input.value = ""

    def on_input_changed(self) -> None:
        """Called as the user types."""
        self.bell()  

if __name__ == "__main__":
    app = PreventApp()
    app.run()
```

<!-- SVG content removed by SVG Remover -->

## Message handlers¶

Most of the logic in a Textual app will be written in message handlers. Let's explore handlers in more detail.

### Handler naming¶

Textual uses the following scheme to map messages classes on to a Python method.

- Start with `"on_"`.
- Add the message's namespace (if any) converted from CamelCase to snake\_case plus an underscore `"_"`.
- Add the name of the class converted from CamelCase to snake\_case.

<!-- SVG content removed by SVG Remover -->

Messages have a namespace if they are defined as a child class of a Widget. The namespace is the name of the parent class. For instance, the builtin `Input` class defines its `Changed` message as follows:

```
class Input(Widget):
    ...
    class Changed(Message):
        """Posted when the value changes."""
        ...
```

Because `Changed` is a *child* class of `Input`, its namespace will be "input" (and the handler name will be `on_input_changed`). This allows you to have similarly named events, without clashing event handler names.

Tip

If you are ever in doubt about what the handler name should be for a given event, print the `handler_name` class variable for your event class.

Here's how you would check the handler name for the `Input.Changed` event:

```
>>> from textual.widgets import Input
>>> Input.Changed.handler_name
'on_input_changed'
```

### On decorator¶

In addition to the naming convention, message handlers may be created with the [`on`](https://textual.textualize.io/api/logger/#textual.on " on") decorator, which turns a method into a handler for the given message or event.

For instance, the two methods declared below are equivalent:

```
@on(Button.Pressed)
def handle_button_pressed(self):
    ...

def on_button_pressed(self):
    ...
```

While this allows you to name your method handlers anything you want, the main advantage of the decorator approach over the naming convention is that you can specify *which* widget(s) you want to handle messages for.

Let's first explore where this can be useful. In the following example we have three buttons, each of which does something different; one plays the bell, one toggles dark mode, and the other quits the app.

```
on_decorator01.pyfrom textual.app import App, ComposeResult
from textual.widgets import Button

class OnDecoratorApp(App):
    CSS_PATH = "on_decorator.tcss"

    def compose(self) -> ComposeResult:
        """Three buttons."""
        yield Button("Bell", id="bell")
        yield Button("Toggle dark", classes="toggle dark")
        yield Button("Quit", id="quit")

    def on_button_pressed(self, event: Button.Pressed) -> None:  
        """Handle all button pressed events."""
        if event.button.id == "bell":
            self.bell()
        elif event.button.has_class("toggle", "dark"):
            self.theme = (
                "textual-dark" if self.theme == "textual-light" else "textual-light"
            )
        elif event.button.id == "quit":
            self.exit()

if __name__ == "__main__":
    app = OnDecoratorApp()
    app.run()
```

```
on_decorator.tcssScreen {
    align: center middle;
    layout: horizontal;
}

Button {
    margin: 2 4;
}
```

<!-- SVG content removed by SVG Remover -->

Note how the message handler has a chained `if` statement to match the action to the button. While this works just fine, it can be a little hard to follow when the number of buttons grows.

The `on` decorator takes a [CSS selector](https://textual.textualize.io/guide/CSS/#selectors) in addition to the event type which will be used to select which controls the handler should work with. We can use this to write a handler per control rather than manage them all in a single handler.

The following example uses the decorator approach to write individual message handlers for each of the three buttons:

```
on_decorator02.pyfrom textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button

class OnDecoratorApp(App):
    CSS_PATH = "on_decorator.tcss"

    def compose(self) -> ComposeResult:
        """Three buttons."""
        yield Button("Bell", id="bell")
        yield Button("Toggle dark", classes="toggle dark")
        yield Button("Quit", id="quit")

    @on(Button.Pressed, "#bell")  
    def play_bell(self):
        """Called when the bell button is pressed."""
        self.bell()

    @on(Button.Pressed, ".toggle.dark")  
    def toggle_dark(self):
        """Called when the 'toggle dark' button is pressed."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    @on(Button.Pressed, "#quit")  
    def quit(self):
        """Called when the quit button is pressed."""
        self.exit()

if __name__ == "__main__":
    app = OnDecoratorApp()
    app.run()
```

```
on_decorator.tcssScreen {
    align: center middle;
    layout: horizontal;
}

Button {
    margin: 2 4;
}
```

<!-- SVG content removed by SVG Remover -->

While there are a few more lines of code, it is clearer what will happen when you click any given button.

Note that the decorator requires that the message class has a `control` property which should return the widget associated with the message. Messages from builtin controls will have this attribute, but you may need to add a `control` property to any [custom messages](https://textual.textualize.io/guide/events/#custom-messages) you write.

Note

If multiple decorated handlers match the message, then they will *all* be called in the order they are defined.

The naming convention handler will be called *after* any decorated handlers.

#### Applying CSS selectors to arbitrary attributes¶

The `on` decorator also accepts selectors as keyword arguments that may be used to match other attributes in a Message, provided those attributes are in [`Message.ALLOW_SELECTOR_MATCH`](https://textual.textualize.io/api/message/#textual.message.Message.ALLOW_SELECTOR_MATCH " ALLOW_SELECTOR_MATCH").

The snippet below shows how to match the message [`TabbedContent.TabActivated`](https://textual.textualize.io/widgets/tabbed_content/#textual.widgets.TabbedContent.TabActivated " TabActivated") only when the tab with id `home` was activated:

```
@on(TabbedContent.TabActivated, pane="#home")
def home_tab(self) -> None:
    self.log("Switched back to home tab.")
    ...
```

### Handler arguments¶

Message handler methods can be written with or without a positional argument. If you add a positional argument, Textual will call the handler with the event object. The following handler (taken from `custom01.py` above) contains a `message` parameter. The body of the code makes use of the message to set a preset color.

```
def on_color_button_selected(self, message: ColorButton.Selected) -> None:
        self.screen.styles.animate("background", message.color, duration=0.5)
```

A similar handler can be written using the decorator `on`:

```
@on(ColorButton.Selected)
    def animate_background_color(self, message: ColorButton.Selected) -> None:
        self.screen.styles.animate("background", message.color, duration=0.5)
```

If the body of your handler doesn't require any information in the message you can omit it from the method signature. If we just want to play a bell noise when the button is clicked, we could write our handler like this:

```
def on_color_button_selected(self) -> None:
        self.app.bell()
```

This pattern is a convenience that saves writing out a parameter that may not be used.

### Async handlers¶

Message handlers may be coroutines. If you prefix your handlers with the `async` keyword, Textual will `await` them. This lets your handler use the `await` keyword for asynchronous APIs.

If your event handlers are coroutines it will allow multiple events to be processed concurrently, but bear in mind an individual widget (or app) will not be able to pick up a new message from its message queue until the handler has returned. This is rarely a problem in practice; as long as handlers return within a few milliseconds the UI will remain responsive. But slow handlers might make your app hard to use.

Info

To re-use the chef analogy, if an order comes in for beef wellington (which takes a while to cook), orders may start to pile up and customers may have to wait for their meal. The solution would be to have another chef work on the wellington while the first chef picks up new orders.

Network access is a common cause of slow handlers. If you try to retrieve a file from the internet, the message handler may take anything up to a few seconds to return, which would prevent the widget or app from updating during that time. The solution is to launch a new asyncio task to do the network task in the background.

Let's look at an example which looks up word definitions from an [api](https://dictionaryapi.dev/) as you type.

Note

You will need to install [httpx](https://www.python-httpx.org/) with `pip install httpx` to run this example.

```
dictionary.pyimport asyncio

try:
    import httpx
except ImportError:
    raise ImportError("Please install httpx with 'pip install httpx' ")

from rich.json import JSON

from textual.app import App, ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Input, Static

class DictionaryApp(App):
    """Searches a dictionary API as-you-type."""

    CSS_PATH = "dictionary.tcss"

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Search for a word")
        yield VerticalScroll(Static(id="results"), id="results-container")

    async def on_input_changed(self, message: Input.Changed) -> None:
        """A coroutine to handle a text changed message."""
        if message.value:
            # Look up the word in the background
            asyncio.create_task(self.lookup_word(message.value))
        else:
            # Clear the results
            self.query_one("#results", Static).update()

    async def lookup_word(self, word: str) -> None:
        """Looks up a word."""
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        async with httpx.AsyncClient() as client:
            results = (await client.get(url)).text

        if word == self.query_one(Input).value:
            self.query_one("#results", Static).update(JSON(results))

if __name__ == "__main__":
    app = DictionaryApp()
    app.run()
```

```
dictionary.tcssScreen {
    background: $panel;
}

Input {
    dock: top;
    width: 100%;
    height: 1;
    padding: 0 1;
    margin: 1 1 0 1;
}

#results {
    width: auto;
    min-height: 100%;
}

#results-container {
    background: $background 50%;
    overflow: auto;
    margin: 1 2;
    height: 100%;
}
```

<!-- SVG content removed by SVG Remover -->

Note the highlighted line in the above code which calls `asyncio.create_task` to run a coroutine in the background. Without this you would find typing into the text box to be unresponsive.