---
title: "Textual - Animation"
source: "https://textual.textualize.io/guide/animation/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Animation¶

This chapter discusses how to use Textual's animation system to create visual effects such as movement, blending, and fading.

## Animating styles¶

Textual's animator can change an attribute from one value to another in fixed increments over a period of time. You can apply animations to [styles](https://textual.textualize.io/guide/styles/) such as `offset` to move widgets around the screen, and `opacity` to create fading effects.

Apps and widgets both have an [animate](https://textual.textualize.io/api/app/#textual.app.App.animate " animate") method which will animate properties on those objects. Additionally, `styles` objects have an identical `animate` method which will animate styles.

Let's look at an example of how we can animate the opacity of a widget to make it fade out. The following example app contains a single `Static` widget which is immediately animated to an opacity of `0.0` (making it invisible) over a duration of two seconds.

```
from textual.app import App, ComposeResult
from textual.widgets import Static

class AnimationApp(App):
    def compose(self) -> ComposeResult:
        self.box = Static("Hello, World!")
        self.box.styles.background = "red"
        self.box.styles.color = "black"
        self.box.styles.padding = (1, 2)
        yield self.box

    def on_mount(self):
        self.box.styles.animate("opacity", value=0.0, duration=2.0)

if __name__ == "__main__":
    app = AnimationApp()
    app.run()
```

The animator updates the value of the `opacity` attribute on the `styles` object in small increments over two seconds. Here's how the widget will change as time progresses:

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

<!-- SVG content removed by SVG Remover -->

## Duration and Speed¶

When requesting an animation you can specify a *duration* or *speed*. The duration is how long the animation should take in seconds. The speed is how many units a value should change in one second. For instance, if you animate a value at 0 to 10 with a speed of 2, it will complete in 5 seconds.

## Easing functions¶

The easing function determines the journey a value takes on its way to the target value. It could move at a constant pace, or it might start off slow then accelerate towards its final value. Textual supports a number of [easing functions](https://easings.net/).

<!-- SVG content removed by SVG Remover -->

Run the following from the command prompt to preview them.

```
textual easing
```

You can specify which easing method to use via the `easing` parameter on the `animate` method. The default easing method is `"in_out_cubic"` which accelerates and then decelerates to produce a pleasing organic motion.

Note

The `textual easing` preview requires the `textual-dev` package to be installed (using `pip install textual-dev`).

## Completion callbacks¶

You can pass a callable to the animator via the `on_complete` parameter. Textual will run the callable when the animation has completed.

## Delaying animations¶

You can delay the start of an animation with the `delay` parameter of the `animate` method. This parameter accepts a `float` value representing the number of seconds to delay the animation by. For example, `self.box.styles.animate("opacity", value=0.0, duration=2.0, delay=5.0)` delays the start of the animation by five seconds, meaning the animation will start after 5 seconds and complete 2 seconds after that.