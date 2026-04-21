## Overview

Exceptions are usually avoided in control programs in favour of c style
error handling (return values) because the stack winding/unwinding is
too costly an overhead for control/embedded programs. However there are
some instances where it is useful.

### RAII

Constructors cannot usually provide a means to return with detailed
information when something goes wrong - however they can with
exceptions. This is especially useful for raii (resource acquisition is
initialisation) classes where a class is completely initialised and
enabled in the constructor. Since speed is not usually of the essence in
program configuration and setup (particularly in control programs where
only the control loop needs to be fast) many classes can take advantage
of exception handling in their constructors in this phase of the
program.

### Debugging

Another is to provide a path back up the program heirarchy to ascertain
where bugs really occurred. Often a macro-function will only give you
the point of failure, which is usually in a library object somewhere -
it doesn't let you retrieve where your program caused the failure
higher up. Throwing, rethrowing and catching exceptions, in debug mode,
can do this.

However, again, be careful of using exceptions in areas of your code
which need to be fast. The stack winding *will* slow your program down.

### Provides

-   Standard exceptions
-   Data throwing exceptions
-   Debug only exceptions
-   Assert style exceptions
-   Exception rethrowing

## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/exceptions.hpp>

// The exception classes
using ecl::StandardException;
using ecl::DataException;

// Error flags (from ecl_errors)
using ecl::ConfigurationError;
using ecl::InvalidInputError;
// ...
```



If outside ros, you will also need to link to *ecl_exceptions*.

## Tutorials

-   [Ecl Exception Handling](ecl_exceptions/Tutorials/Ecl Exception Handling)

## Examples

-   `src/examples/exceptions.cpp` : coverage style test for
    exceptions.
-   `src/examples/exception_tracer.cpp` : getting a backtrace via
    exceptions, posix style.

## Benchmarks

These are in [ecl_core_apps](ecl_core_apps).

-   `/src/benchmarks/exceptions.cpp` : benchmarks the latencies for
    exception handling.

## Errata

The use of exceptions here doesn't exactly conform to the c++ 'ideal'
for exception handling in a library. For that you should derive from the
std exception classes, particularly runtime_error and logic_error and
have a single class for each type of error (we've bundled all the ecl
standard errors into two classes here - Standard and Data). However I
can't seem to find a really good reason at this point in time to
circumvent the convenient practicality of ecl_exceptions. I think this
is because the purpose of this library is to present a standard set of
error types across platforms, no need to keep making new exception
classes for every new class, package or platform implementation in the
ecl.

The only reason that might motivate a change in policy is if the ecl is
used in very heirarchical programs which require floating different
exception types to different levels depending on their type (e.g. you
might want to catch an *is_busy* error early and recover, whilst letting
a *configuration_error* float to the top).
