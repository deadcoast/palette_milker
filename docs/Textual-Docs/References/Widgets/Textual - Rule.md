---
title: "Textual - Rule"
source: "https://textual.textualize.io/widgets/rule/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Rule¶

A rule widget to separate content, similar to a `<hr>` HTML tag.

- Focusable
- Container

## Examples¶

### Horizontal Rule¶

The default orientation of a rule is horizontal.

The example below shows horizontal rules with all the available line styles.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Label, Rule

class HorizontalRulesApp(App):
    CSS_PATH = "horizontal_rules.tcss"

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("solid (default)")
            yield Rule()
            yield Label("heavy")
            yield Rule(line_style="heavy")
            yield Label("thick")
            yield Rule(line_style="thick")
            yield Label("dashed")
            yield Rule(line_style="dashed")
            yield Label("double")
            yield Rule(line_style="double")
            yield Label("ascii")
            yield Rule(line_style="ascii")

if __name__ == "__main__":
    app = HorizontalRulesApp()
    app.run()
```

```
Screen {
    align: center middle;
}

Vertical {
    height: auto;
    width: 80%;
}

Label {
    width: 100%;
    text-align: center;
}
```

### Vertical Rule¶

The example below shows vertical rules with all the available line styles.

<!-- SVG content removed by SVG Remover -->

```
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Label, Rule

class VerticalRulesApp(App):
    CSS_PATH = "vertical_rules.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Label("solid")
            yield Rule(orientation="vertical")
            yield Label("heavy")
            yield Rule(orientation="vertical", line_style="heavy")
            yield Label("thick")
            yield Rule(orientation="vertical", line_style="thick")
            yield Label("dashed")
            yield Rule(orientation="vertical", line_style="dashed")
            yield Label("double")
            yield Rule(orientation="vertical", line_style="double")
            yield Label("ascii")
            yield Rule(orientation="vertical", line_style="ascii")

if __name__ == "__main__":
    app = VerticalRulesApp()
    app.run()
```

```
Screen {
    align: center middle;
}

Horizontal {
    width: auto;
    height: 80%;
}

Label {
    width: 6;
    height: 100%;
    text-align: center;
}
```

## Reactive Attributes¶

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `orientation` | `RuleOrientation` | `"horizontal"` | The orientation of the rule. |
| `line_style` | `LineStyle` | `"solid"` | The line style of the rule. |

## Messages¶

This widget sends no messages.

## Bindings¶

This widget has no bindings.

## Component Classes¶

This widget has no component classes.

---

Bases: `[Widget](https://textual.textualize.io/api/widget/#textual.widget.Widget " Widget (textual.widget.Widget)")`

A rule widget to separate content, similar to a `<hr>` HTML tag.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ## `orientation` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule\(orientation\) "Permanent link") |  | The orientation of the rule. | `'horizontal'` |
| ## `line_style` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule\(line_style\) "Permanent link") |  | The line style of the rule. | `'solid'` |
| ## `name` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ## `id` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ## `classes` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the widget. | `None` |
| ## `disabled` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

## line\_style [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.line_style "Permanent link")

```
line_style =
```

The line style of the rule.

## orientation [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.orientation "Permanent link")

```
orientation =
```

The orientation of the rule.

## horizontal [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.horizontal "Permanent link")

```
horizontal(
    ="solid",
    =None,
    =None,
    =None,
    =False,
)
```

Utility constructor for creating a horizontal rule.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `line_style` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.horizontal\(line_style\) "Permanent link") |  | The line style of the rule. | `'solid'` |
| ### `name` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.horizontal\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ### `id` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.horizontal\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.horizontal\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the widget. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.horizontal\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

Returns:

| Type | Description |
| --- | --- |
|  | A rule widget with horizontal orientation. |

## vertical [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.vertical "Permanent link")

```
vertical(
    ="solid",
    =None,
    =None,
    =None,
    =False,
)
```

Utility constructor for creating a vertical rule.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| ### `line_style` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.vertical\(line_style\) "Permanent link") |  | The line style of the rule. | `'solid'` |
| ### `name` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.vertical\(name\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The name of the widget. | `None` |
| ### `id` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.vertical\(id\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The ID of the widget in the DOM. | `None` |
| ### `classes` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.vertical\(classes\) "Permanent link") | `[str](https://docs.python.org/3/library/stdtypes.html#str) \| None` | The CSS classes of the widget. | `None` |
| ### `disabled` [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.Rule.vertical\(disabled\) "Permanent link") | `[bool](https://docs.python.org/3/library/functions.html#bool)` | Whether the widget is disabled or not. | `False` |

Returns:

| Type | Description |
| --- | --- |
|  | A rule widget with vertical orientation. |

## textual.widgets.rule [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.rule "Permanent link")

### LineStyle [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.rule.LineStyle "Permanent link")

```
LineStyle = Literal[
    "ascii",
    "blank",
    "dashed",
    "double",
    "heavy",
    "hidden",
    "none",
    "solid",
    "thick",
]
```

The valid line styles of the rule widget.

### RuleOrientation [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.rule.RuleOrientation "Permanent link")

```
RuleOrientation = Literal['horizontal', 'vertical']
```

The valid orientations of the rule widget.

### InvalidLineStyle [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.rule.InvalidLineStyle "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Exception raised for an invalid rule line style.

### InvalidRuleOrientation [¶](https://textual.textualize.io/widgets/rule/#textual.widgets.rule.InvalidRuleOrientation "Permanent link")

Bases: `[Exception](https://docs.python.org/3/library/exceptions.html#Exception)`

Exception raised for an invalid rule orientation.