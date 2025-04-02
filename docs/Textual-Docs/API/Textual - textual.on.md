---
title: "Textual - textual.on"
source: "https://textual.textualize.io/api/on/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## On¶

Decorator to declare that the method is a message handler.

The decorator accepts an optional CSS selector that will be matched against a widget exposed by a `control` property on the message.

Example
```
# Handle the press of buttons with ID "#quit".
@on(Button.Pressed, "#quit")
def quit_button(self) -> None:
    self.app.quit()
```

Keyword arguments can be used to match additional selectors for attributes listed in [`ALLOW_SELECTOR_MATCH`](https://textual.textualize.io/api/message/#textual.message.Message.ALLOW_SELECTOR_MATCH " ALLOW_SELECTOR_MATCH").

Example
```
# Handle the activation of the tab "#home" within the \`TabbedContent\` "#tabs".
@on(TabbedContent.TabActivated, "#tabs", pane="#home")
def switch_to_home(self) -> None:
    self.log("Switching back to the home tab.")
    ...
```

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `message_type` [¶](https://textual.textualize.io/api/on/#textual.on\(message_type\) "Permanent link") | `[type](https://docs.python.org/3/library/functions.html#type)[[Message](https://textual.textualize.io/api/message/#textual.message.Message " Message (textual.message.Message)")]` | The message type (i.e. the class). | *required* |
| ## `selector` [¶](https://textual.textualize.io/api/on/#textual.on\(selector\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | An optional [selector](https://textual.textualize.io/guide/CSS#selectors). If supplied, the handler will only be called if `selector` matches the widget from the `control` attribute of the message. | `None` |
| ## `**kwargs` [¶](https://textual.textualize.io/api/on/#textual.on\(**kwargs\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str)` | Additional selectors for other attributes of the message. | `{}` |