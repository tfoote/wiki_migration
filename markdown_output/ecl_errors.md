## Overview

The usual C++ means is to use exceptions, however in embedded systems,
exceptions are often unavailable or are too resource-heavy. This library
provides a simpler alternative, combining error flags, macros and an
error handler class to provide convenient disposal of errors across
multiple platforms for the ecl. It also provides simple runtime and
compile time asserts and aborts.

For a general overview on how ecl handles debugging, see
[Debugging and Error Handling in the Ecl](http://snorriheim.dnsdojo.com/redmine/wiki/ecl/Ecl_debugging).

For higher level exception handling of errors, refer to
[ecl_exceptions](ecl_exceptions).

## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/errors.hpp>

// The error interfaces
using ecl_compile_time_assert;
using ecl_run_time_assert;
using ecl_run_time_abort;

// Error type enumerations
using ecl::NoError;
using ecl::ConfigurationError;
using ecl::UnknownError;
//...
    
// Error Handler
using ecl::Error;
```



If outside ros, you will also need to link to `ecl_errors`.

## Usage

-   [Debug Modes](ecl_errors/Tutorials/Debug Modes in the Ecl) -
    toggling debug/release mode functionality.
-   [Error Handling](ecl_errors/Tutorials/Error Handling in the Ecl) -
    simple macros and error flags for error handling at the lowest
    level.
-   [Assertions](ecl_errors/Tutorials/Assertions in the Ecl) - run-time
    and cmopile-time asserts and aborts.
