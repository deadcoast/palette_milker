---
title: "Textual - Getting started"
source: "https://textual.textualize.io/getting_started/"
author:
  - "[[Textual Documentation]]"
published:
created: 2025-03-28
description: "Textual is a TUI framework for Python, inspired by modern web development."
tags:
  - "clippings"
  - "textual"
---
## Getting started

All you need to get started building Textual apps.

## Requirements¶

Textual requires Python 3.8 or later (if you have a choice, pick the most recent Python). Textual runs on Linux, macOS, Windows and probably any OS where Python also runs.

Your platform

### Linux (all distros)[¶](https://textual.textualize.io/getting_started/#linux-all-distros "Permanent link")

All Linux distros come with a terminal emulator that can run Textual apps.

### macOS[¶](https://textual.textualize.io/getting_started/#macos "Permanent link")

The default terminal app is limited to 256 colors. We recommend installing a newer terminal such as [iterm2](https://iterm2.com/), [Ghostty](https://ghostty.org/), [Kitty](https://sw.kovidgoyal.net/kitty/), or [WezTerm](https://wezfurlong.org/wezterm/).

### Windows[¶](https://textual.textualize.io/getting_started/#windows "Permanent link")

The new [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-gb&gl=GB) runs Textual apps beautifully.

## Installation¶

Here's how to install Textual.

### From PyPI¶

You can install Textual via PyPI, with the following command:

```
pip install textual
```

If you plan on developing Textual apps, you should also install textual developer tools:

```
pip install textual-dev
```

If you would like to enable syntax highlighting in the [TextArea](https://textual.textualize.io/widgets/text_area/) widget, you should specify the "syntax" extras when you install Textual:

```
pip install "textual[syntax]"
```

### From conda-forge¶

Textual is also available on [conda-forge](https://conda-forge.org/). The preferred package manager for conda-forge is currently [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html):

```
micromamba install -c conda-forge textual
```

And for the textual developer tools:

```
micromamba install -c conda-forge textual-dev
```

### Textual CLI¶

If you installed the developer tools you should have access to the `textual` command. There are a number of sub-commands available which will aid you in building Textual apps. Run the following for a list of the available commands:

```
textual --help
```

See [devtools](https://textual.textualize.io/guide/devtools/) for more about the `textual` command.

## Demo¶

Once you have Textual installed, run the following to get an impression of what it can do:

```
python -m textual
```

## Examples¶

The Textual repository comes with a number of example apps. To try out the examples, first clone the Textual repository:

```
git clone https://github.com/Textualize/textual.git
```

```
git clone git@github.com:Textualize/textual.git
```

```
gh repo clone Textualize/textual
```

With the repository cloned, navigate to the `/examples/` directory where you will find a number of Python files you can run from the command line:

```
cd textual/examples/
python code_browser.py ../
```

### Widget examples¶

In addition to the example apps, you can also find the code listings used to generate the screenshots in these docs in the `docs/examples` directory.

## Need help?¶

See the [help](https://textual.textualize.io/help/) page for how to get help with Textual, or to report bugs.