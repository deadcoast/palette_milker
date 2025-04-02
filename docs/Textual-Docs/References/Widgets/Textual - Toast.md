---
title: "Textual - Toast"
source: "https://textual.textualize.io/widgets/toast/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Toast¶

Added in version 0.30.0

A widget which displays a notification message.

- Focusable
- Container

Note that `Toast` isn't designed to be used directly in your applications, but it is instead used by [`notify`](https://textual.textualize.io/api/app/#textual.app.App.notify " notify") to display a message when using Textual's built-in notification system.

## Styling¶

You can customize the style of Toasts by targeting the `Toast` [CSS type](https://textual.textualize.io/guide/CSS/#type-selector). For example:

```
Toast {
    padding: 3;
}
```

If you wish to change the location of Toasts, it is possible by targeting the `ToastRack` CSS type. For example:

```
ToastRack {
        align: right top;
}
```

The three severity levels also have corresponding [classes](https://textual.textualize.io/guide/CSS/#class-name-selector), allowing you to target the different styles of notification. They are:

- `-information`
- `-warning`
- `-error`

If you wish to tailor the notifications for your application you can add rules to your CSS like this:

```
Toast.-information {
    /* Styling here. */
}

Toast.-warning {
    /* Styling here. */
}

Toast.-error {
    /* Styling here. */
}
```

You can customize just the title wih the `toast--title` class. The following would make the title italic for an information toast:

```
Toast.-information .toast--title {
    text-style: italic;
}
```

## Example¶

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App

class ToastApp(App[None]):
    def on_mount(self) -> None:
        # Show an information notification.
        self.notify("It's an older code, sir, but it checks out.")

        # Show a warning. Note that Textual's notification system allows
        # for the use of Rich console markup.
        self.notify(
            "Now witness the firepower of this fully "
            "[b]ARMED[/b] and [i][b]OPERATIONAL[/b][/i] battle station!",
            title="Possible trap detected",
            severity="warning",
        )

        # Show an error. Set a longer timeout so it's noticed.
        self.notify("It's a trap!", severity="error", timeout=10)

        # Show an information notification, but without any sort of title.
        self.notify("It's against my programming to impersonate a deity.", title="")

if __name__ == "__main__":
    ToastApp().run()
```

## Reactive Attributes¶

This widget has no reactive attributes.

## Messages¶

This widget posts no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

The toast widget provides the following component classes:

| Class | Description |
| --- | --- |
| `toast--title` | Targets the title of the toast. |

---

## textual.widgets.\_toast.Toast [¶](https://textual.textualize.io/widgets/toast/#textual.widgets._toast.Toast "Permanent link")

```
Toast()
```

Bases: `[Static](https://textual.textualize.io/widgets/static/#textual.widgets.Static " Static (textual.widgets._static.Static)")`

A widget for displaying short-lived notifications.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `notification` [¶](https://textual.textualize.io/widgets/toast/#textual.widgets._toast.Toast\(notification\) "Permanent link") | `Notification` | The notification to show in the toast. | *required* |

### COMPONENT\_CLASSES [¶](https://textual.textualize.io/widgets/toast/#textual.widgets._toast.Toast.COMPONENT_CLASSES "Permanent link")

```
COMPONENT_CLASSES = {'toast--title'}
```

| Class | Description |
| --- | --- |
| `toast--title` | Targets the title of the toast. |