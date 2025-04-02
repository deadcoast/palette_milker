---
title: "Textual - Design a Layout"
source: "https://textual.textualize.io/how-to/design-a-layout/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Design a Layout¶

This article discusses an approach you can take when designing the layout for your applications.

Textual's layout system is flexible enough to accommodate just about any application design you could conceive of, but it may be hard to know where to start. We will go through a few tips which will help you get over the initial hurdle of designing an application layout.

## Tip 1. Make a sketch¶

The initial design of your application is best done with a sketch. You could use a drawing package such as [Excalidraw](https://excalidraw.com/) for your sketch, but pen and paper is equally as good.

Start by drawing a rectangle to represent a blank terminal, then draw a rectangle for each element in your application. Annotate each of the rectangles with the content they will contain, and note wether they will scroll (and in what direction).

For the purposes of this article we are going to design a layout for a Twitter or Mastodon client, which will have a header / footer and a number of columns.

Note

The approach we are discussing here is applicable even if the app you want to build looks nothing like our sketch!

Here's our sketch:

<!-- SVG content removed by SVG Remover -->

It's rough, but it's all we need.

Try in Textual-web

## Tip 2. Work outside in¶

Like a sculpture with a block of marble, it is best to work from the outside towards the center. If your design has fixed elements (like a header, footer, or sidebar), start with those first.

In our sketch we have a header and footer. Since these are the outermost widgets, we will begin by adding them.

Tip

Textual has builtin [Header](https://textual.textualize.io/widgets/header/) and [Footer](https://textual.textualize.io/widgets/footer/) widgets which you could use in a real application.

The following example defines an [app](https://textual.textualize.io/guide/app/), a [screen](https://textual.textualize.io/guide/screens/), and our header and footer widgets. Since we're starting from scratch and don't have any functionality for our widgets, we are going to use the [Placeholder](https://textual.textualize.io/widgets/placeholder/#textual.widgets.Placeholder " Placeholder") widget to help us visualize our design.

In a real app, we would replace these placeholders with more useful content.

```
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder

class Header(Placeholder):  
    pass

class Footer(Placeholder):  
    pass

class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")  
        yield Footer(id="Footer")  

class LayoutApp(App):
    def on_mount(self) -> None:
        self.push_screen(TweetScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()
```

<!-- SVG content removed by SVG Remover -->

## Tip 3. Apply docks¶

This app works, but the header and footer don't behave as expected. We want both of these widgets to be fixed to an edge of the screen and limited in height. In Textual this is known as *docking* which you can apply with the [dock](https://textual.textualize.io/styles/dock/) rule.

We will dock the header and footer to the top and bottom edges of the screen respectively, by adding a little [CSS](https://textual.textualize.io/guide/CSS/) to the widget classes:

```
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """

class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer(id="Footer")

class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(TweetScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()
```

<!-- SVG content removed by SVG Remover -->

The `DEFAULT_CSS` class variable is used to set CSS directly in Python code. We could define these in an external CSS file, but writing the CSS inline like this can be convenient if it isn't too complex.

When you dock a widget, it reduces the available area for other widgets. This means that Textual will automatically compensate for the 6 additional lines reserved for the header and footer.

## Tip 4. Use FR Units for flexible things¶

After we've added the header and footer, we want the remaining space to be used for the main interface, which will contain the columns in the sketch. This area is flexible (will change according to the size of the terminal), so how do we ensure that it takes up precisely the space needed?

The simplest way is to use [fr](https://textual.textualize.io/css_types/scalar/#fraction) units. By setting both the width and height to `1fr`, we are telling Textual to divide the space equally amongst the remaining widgets. There is only a single widget, so that widget will fill all of the remaining space.

Let's make that change.

```
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """

class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class ColumnsContainer(Placeholder):
    DEFAULT_CSS = """
    ColumnsContainer {
        width: 1fr;
        height: 1fr;
        border: solid white;
    }
    """  

class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer(id="Footer")
        yield ColumnsContainer(id="Columns")

class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(TweetScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()
```

<!-- SVG content removed by SVG Remover -->

As you can see, the central Columns area will resize with the terminal window.

## Tip 5. Use containers¶

Before we add content to the Columns area, we have an opportunity to simplify. Rather than extend `Placeholder` for our `ColumnsContainer` widget, we can use one of the builtin *containers*. A container is simply a widget designed to *contain* other widgets. Containers are styled with `fr` units to fill the remaining space so we won't need to add any more CSS.

Let's replace the `ColumnsContainer` class in the previous example with a `HorizontalScroll` container, which also adds an automatic horizontal scrollbar.

```
from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll
from textual.screen import Screen
from textual.widgets import Placeholder

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """

class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer(id="Footer")
        yield HorizontalScroll()  

class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(TweetScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()
```

<!-- SVG content removed by SVG Remover -->

The container will appear as blank space until we add some widgets to it.

Let's add the columns to the `HorizontalScroll`. A column is itself a container which will have a vertical scrollbar, so we will define our `Column` by subclassing `VerticalScroll`. In a real app, these columns will likely be added dynamically from some kind of configuration, but let's add 4 to visualize the layout.

We will also define a `Tweet` placeholder and add a few to each column.

```
from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """

class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class Tweet(Placeholder):
    pass

class Column(VerticalScroll):
    def compose(self) -> ComposeResult:
        for tweet_no in range(1, 20):
            yield Tweet(id=f"Tweet{tweet_no}")

class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer(id="Footer")
        with HorizontalScroll():
            yield Column()
            yield Column()
            yield Column()
            yield Column()

class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(TweetScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()
```

<!-- SVG content removed by SVG Remover -->

Note from the output that each `Column` takes a quarter of the screen width. This happens because `Column` extends a container which has a width of `1fr`.

It makes more sense for a column in a Twitter / Mastodon client to use a fixed width. Let's set the width of the columns to 32.

We also want to reduce the height of each "tweet". In the real app, you might set the height to "auto" so it fits the content, but lets set it to 5 lines for now.

Here's the final example and a reminder of the sketch.

```
from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll, VerticalScroll
from textual.screen import Screen
from textual.widgets import Placeholder

class Header(Placeholder):
    DEFAULT_CSS = """
    Header {
        height: 3;
        dock: top;
    }
    """

class Footer(Placeholder):
    DEFAULT_CSS = """
    Footer {
        height: 3;
        dock: bottom;
    }
    """

class Tweet(Placeholder):
    DEFAULT_CSS = """
    Tweet {
        height: 5;
        width: 1fr;
        border: tall $background;
    }
    """

class Column(VerticalScroll):
    DEFAULT_CSS = """
    Column {
        height: 1fr;
        width: 32;
        margin: 0 2;
    }
    """

    def compose(self) -> ComposeResult:
        for tweet_no in range(1, 20):
            yield Tweet(id=f"Tweet{tweet_no}")

class TweetScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id="Header")
        yield Footer(id="Footer")
        with HorizontalScroll():
            yield Column()
            yield Column()
            yield Column()
            yield Column()

class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(TweetScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()
```

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

A layout like this is a great starting point. In a real app, you would start replacing each of the placeholders with [builtin](https://textual.textualize.io/widget_gallery/) or [custom](https://textual.textualize.io/guide/widgets/) widgets.

## Summary¶

Layout is the first thing you will tackle when building a Textual app. The following tips will help you get started.

1. Make a sketch (pen and paper is fine).
2. Work outside in. Start with the entire space of the terminal, add the outermost content first.
3. Dock fixed widgets. If the content doesn't move or scroll, you probably want to *dock* it.
4. Make use of `fr` for flexible space within layouts.
5. Use containers to contain other widgets, particularly if they scroll!

---

If you need further help, we are here to [help](https://textual.textualize.io/help/).