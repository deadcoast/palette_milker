---
title: "Textual - DOM Queries"
source: "https://textual.textualize.io/guide/queries/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## DOM Queries¶

In the [CSS chapter](https://textual.textualize.io/guide/CSS/) we introduced the [DOM](https://textual.textualize.io/guide/CSS/#the-dom) which is how Textual apps keep track of widgets. We saw how you can apply styles to the DOM with CSS [selectors](https://textual.textualize.io/guide/CSS/#selectors).

Selectors are a very useful idea and can do more than apply styles. We can also find widgets in Python code with selectors, and make updates to widgets in a simple expressive way. Let's look at how!

Tip

See the [Textual Query Sandbox](https://github.com/davep/textual-query-sandbox/) project for an interactive way of experimenting with DOM queries.

## Query one¶

The [query\_one](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query_one " query_one") method is used to retrieve a single widget that matches a selector or a type.

Let's say we have a widget with an ID of `send` and we want to get a reference to it in our app. We could do this with the following line of code:

```
send_button = self.query_one("#send")
```

This will retrieve the first widget discovered with an ID of `send`. If there are no matching widgets, Textual will raise a [NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches") exception.

You can also add a second parameter for the expected type, which will ensure that you get the type you are expecting.

```
send_button = self.query_one("#send", Button)
```

If the matched widget is *not* a button (i.e. if `isinstance(widget, Button)` equals `False`), Textual will raise a [WrongType](https://textual.textualize.io/api/query/#textual.css.query.WrongType " WrongType") exception.

Tip

The second parameter allows type-checkers like MyPy to know the exact return type. Without it, MyPy would only know the result of `query_one` is a Widget (the base class).

You can also specify a widget type in place of a selector, which will return a widget of that type. For instance, the following would return a `Button` instance (assuming there is a single Button).

```
my_button = self.query_one(Button)
```

`query_one` searches the DOM *below* the widget it is called on, so if you call `query_one` on a widget, it will only find widgets that are descendants of that widget.

If you wish to search the entire DOM, you should call `query_one` on the `App` or `Screen` instance.

```
# Search the entire Screen for a widget with an ID of "send-email"
self.screen.query_one("#send-email")
```

## Making queries¶

Apps and widgets also have a [query](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query " query") method which finds (or queries) widgets. This method returns a [DOMQuery](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery " DOMQuery") object which is a list-like container of widgets.

If you call `query` with no arguments, you will get back a `DOMQuery` containing all widgets. This method is *recursive*, meaning it will also return child widgets (as many levels as required).

Here's how you might iterate over all the widgets in your app:

```
for widget in self.query():
    print(widget)
```

Called on the `app`, this will retrieve all widgets in the app. If you call the same method on a widget, it will return the children of that widget.

Note

All the query and related methods work on both App and Widget sub-classes.

### Query selectors¶

You can call `query` with a CSS selector. Let's look a few examples:

If we want to find all the button widgets, we could do something like the following:

```
for button in self.query("Button"):
    print(button)
```

Any selector that works in CSS will work with the `query` method. For instance, if we want to find all the disabled buttons in a Dialog widget, we could do this:

```
for button in self.query("Dialog Button.disabled"):
    print(button)
```

Info

The selector `Dialog Button.disabled` says find all the `Button` with a CSS class of `disabled` that are a child of a `Dialog` widget.

### Results¶

Query objects have a [results](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.results " results") method which is an alternative way of iterating over widgets. If you supply a type (i.e. a Widget class) then this method will generate only objects of that type.

The following example queries for widgets with the `disabled` CSS class and iterates over just the Button objects.

```
for button in self.query(".disabled").results(Button):
    print(button)
```

Tip

This method allows type-checkers like MyPy to know the exact type of the object in the loop. Without it, MyPy would only know that `button` is a `Widget` (the base class).

## Query objects¶

We've seen that the [query](https://textual.textualize.io/api/dom_node/#textual.dom.DOMNode.query " query") method returns a [DOMQuery](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery " DOMQuery") object you can iterate over in a for loop. Query objects behave like Python lists and support all of the same operations (such as `query[0]`, `len(query)` ,`reverse(query)` etc). They also have a number of other methods to simplify retrieving and modifying widgets.

## First and last¶

The [first](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.first " first") and [last](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.last " last") methods return the first or last matching widget from the selector, respectively.

Here's how we might find the *last* button in an app:

```
last_button = self.query("Button").last()
```

If there are no buttons, Textual will raise a [NoMatches](https://textual.textualize.io/api/query/#textual.css.query.NoMatches " NoMatches") exception. Otherwise it will return a button widget.

Both `first()` and `last()` accept an `expect_type` argument that should be the class of the widget you are expecting. Let's say we want to get the last widget with class `.disabled`, and we want to check it really is a button. We could do this:

```
disabled_button = self.query(".disabled").last(Button)
```

The query selects all widgets with a `disabled` CSS class. The `last` method gets the last disabled widget and checks it is a `Button` and not any other kind of widget.

If the last widget is *not* a button, Textual will raise a [WrongType](https://textual.textualize.io/api/query/#textual.css.query.WrongType " WrongType") exception.

Tip

Specifying the expected type allows type-checkers like MyPy to know the exact return type.

## Filter¶

Query objects have a [filter](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.filter " filter") method which further refines a query. This method will return a new query object with widgets that match both the original query *and* the new selector.

Let's say we have a query which gets all the buttons in an app, and we want a new query object with just the disabled buttons. We could write something like this:

```
# Get all the Buttons
buttons_query = self.query("Button")
# Buttons with 'disabled' CSS class
disabled_buttons = buttons_query.filter(".disabled")
```

Iterating over `disabled_buttons` will give us all the disabled buttons.

## Exclude¶

Query objects have an [exclude](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.exclude " exclude") method which is the logical opposite of [filter](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.filter " filter"). The `exclude` method removes any widgets from the query object which match a selector.

Here's how we could get all the buttons which *don't* have the `disabled` class set.

```
# Get all the Buttons
buttons_query = self.query("Button")
# Remove all the Buttons with the 'disabled' CSS class
enabled_buttons = buttons_query.exclude(".disabled")
```

## Loop-free operations¶

Once you have a query object, you can loop over it to call methods on the matched widgets. Query objects also support a number of methods which make an update to every matched widget without an explicit loop.

For instance, let's say we want to disable all buttons in an app. We could do this by calling [add\_class()](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.add_class " add_class") on a query object.

```
self.query("Button").add_class("disabled")
```

This single line is equivalent to the following:

```
for widget in self.query("Button"):
    widget.add_class("disabled")
```

Here are the other loop-free methods on query objects:

- [add\_class](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.add_class " add_class") Adds a CSS class (or classes) to matched widgets.
- [blur](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.focus " focus") Blurs (removes focus) from matching widgets.
- [focus](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.focus " focus") Focuses the first matching widgets.
- [refresh](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.refresh " refresh") Refreshes matched widgets.
- [remove\_class](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.remove_class " remove_class") Removes a CSS class (or classes) from matched widgets.
- [remove](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.remove " remove") Removes matched widgets from the DOM.
- [set\_class](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set_class " set_class") Sets a CSS class (or classes) on matched widgets.
- [set](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.set " set") Sets common attributes on a widget.
- [toggle\_class](https://textual.textualize.io/api/query/#textual.css.query.DOMQuery.toggle_class " toggle_class") Sets a CSS class (or classes) if it is not set, or removes the class (or classes) if they are set on the matched widgets.