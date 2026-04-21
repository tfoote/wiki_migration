## Overview

Signals and slots provide a means for intra-process communication. The
classes here let you have a many-to-many relationship (unlike most event
callback techniques), and also templatise the data transfer to allow the
coder to customise the event data that is communicated from signal to
slot. It also implements a few conditional (event) related classes.

-   [Background](ecl_sigslots/Background) - non-essential historical
    notes.
-   [Comparisons](ecl_sigslots/Comparisons) - ecl_sigslots vs nodelets
    vs ecto.

## Features

-   *Lightweight* - implements only the necessary features for practical
    usage.
-   *Fully typesafe* - signal-slot pairs *must* have the same type,
    loaded functions must also agree.
-   *Convenient slot loading* - global/static and member functions can
    be loaded with the same api.
-   *Naming* - can use posix style names to identify and perform
    convenient connections/disconnections.
-   *Thread safe* - slots can disconnect/self-destruct without worrying
    about segfaulting across threads.

## Definitions

### Signals

Anywhere that triggers an event requiring a callback to be executed can
be implemented with a signal. These can be placed anywhere in your code
and can be connected to one or many slots.

### Slots

Anywhere that a callback function is required can be implemented with a
slot. These can be placed anywhere in your code and are initialised with
either a static (global) function, or a member function. Once
initialised, they can be hooked up to a signal.

### Message Data

The signal-slot pairs developed here only ever accept one template
argument representing the data to be transmitted from signal to slot. It
would be easy to extend this to more (aka SigSlot/Boost) but I have yet
to find a need for it - if you wish multiple arguments, simply wrap up
your data in a single struct/class. Conceptually, this makes the code
more readable anyway.

The data class itself could be as simple as an error id or as
complicated as the current state in a fsm. Note that both signal and
slot must use the same type.

## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/sigslots.hpp>

// The types
using ecl::Signal;
using ecl::Slots;
```

You will also need to link to *ecl_sigslots*.

## Tutorials

-   [Introduction to Sigslots](ecl_sigslots/Tutorials/Introduction to Sigslots) -
    creating, connecting and triggering signals and slots.
-   [Relaying Signals](ecl_sigslots/Tutorials/Relaying Signals) -
    relaying data from one signaller to the next.
-   [Debugging Sigslots](ecl_sigslots/Tutorials/Debugging Sigslots) -
    tools to help debug sigslots problems.

## Examples

-   [src/examples/sigslots.cpp](http://ros.org/doc/groovy/api/ecl_sigslots/html/examples_2sigslots_8cpp_source.html)
-   [src/examples/sigslots_manager.cpp](http://ros.org/doc/groovy/api/ecl_sigslots/html/sigslots__manager_8cpp_source.html)
