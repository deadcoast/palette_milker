---
title: "Textual - Hide"
source: "https://textual.textualize.io/events/hide/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Hide

Bases: `[Event](https://textual.textualize.io/api/events/#textual.events.Event " Event (textual.events.Event)")`

Sent when a widget has been hidden.

- Bubbles
- Verbose

Sent when any of the following conditions apply:

- The widget is removed from the DOM.
- The widget is no longer displayed because it has been scrolled or clipped from the terminal or its container.
- The widget has its `display` attribute set to `False`.
- The widget's `display` style is set to `"none"`.