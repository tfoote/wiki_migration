## Overview

This is a light version of [ecl_sigslots](ecl_sigslots) and provides a
very ruthlessly simple signals and slots mechanisms useful for

-   very\* embedded development. Differences from
    [ecl_sigslots](ecl_sigslots):

```{=html}
<!-- -->
```
-   Not thread safe\...

This is a bit of a vague statement on its own. In essence, its usually
important to make sure your signals and slots finish processing any
currently executing slots before they self destruct. Most sigslot
implementations dont do this, [ecl_sigslots](ecl_sigslots) does, but
[ecl_sigslots_lite](ecl_sigslots_lite) does not. If you have a
monolothic program with a single thread, this probably doesn't matter,
but if not, then you must take care to ensure signals and slots close
appropriately.

-   No disconnects\...

Adding disconnect capability adds alot of complexity to the sigslots
implementation. Lite sigslots assume that signals and slots connections,
once fixed, stay until the signal goes out of scope.

-   No dynamic storage (no heap storage with malloc/new)\...

This is often verboten with various embedded compilers and introduces
alot of system overhead. Lite sigslots allocates memory up front and
will not permit overuse thereafter.

-   Self contained\...

While utilising things like standard error flag constructors (from
[ecl_errors](ecl_errors)) might be convenient, this package is and
likely will often be used standalone in a firmware project. As a result,
its designed with its own internal mechanisms (e.g. error class) so
it's source can be simply copied to a firmware project.

## Compiling & Linking

```cplusplus
#include <ecl/sigslots_lite.hpp>

// Signals
using ecl::lite::Signal;

// Functions
using ecl::lite::connect
using ecl::lite::global_slots_stored;
using ecl::lite::global_slots_capacity;
using ecl::lite::member_slots_stored;
using ecl::lite::member_slots_capacity;
```

## Examples

-   `src/examples/sigslots.cpp`
