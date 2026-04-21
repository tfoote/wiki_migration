## Overview

This package provides definitions and methods that enable simple
colouring for output on the console without having to remember all the
specific keycodes that shells use.

## Colour Definitions

The current list of supported colour definitions:

-   ``Regular``: black, red, green, yellow, blue, magenta, cyan,
    white,
-   ``Bold``: bold, bold_black, bold_red, bold_green, bold_yellow,
    bold_blue, bold_magenta, bold_cyan, bold_white

## Usage

** Freeform Style **

Simply intersperse colour definitions throughout your printing
statements, e.g.

```highlight
   import rocon_console.console as console
   print(console.cyan + "    Name" + console.reset + ": " + console.yellow + "Dude" + console.reset)
```

** Logging Style **

```highlight
   import rocon_console.console as console
   logdebug("the ingredients of beer are interesting, but not important to the consumer")
   loginfo("the name of a beer is useful information")
   logwarn("this is a lite beer")
   logerror("this is a budweiser")
   logfatal("this is mereley a cider")
```
