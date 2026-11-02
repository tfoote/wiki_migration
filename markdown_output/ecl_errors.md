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
[ecl_exceptions](https://index.ros.org/p/ecl_exceptions).

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

- [Debug Modes](#debug-modes-in-the-ecl) -
  toggling debug/release mode functionality.
- [Error Handling](#error-handling-in-the-ecl) -
  simple macros and error flags for error handling at the lowest level.
- [Assertions](#assertions-in-the-ecl) -
  run-time and cmopile-time asserts and aborts.

## Debug Modes in the Ecl

### Debug Mode

To compile in **debug mode**, do not define either `NDEBUG` or
`ECL_NDEBUG`. e.g.



```
g++ -lecl_devices -o hello hello.cpp
```



This will enable alot of error handling within ecl components
themselves. For example
[ecl_containers](https://index.ros.org/p/ecl_containers) will do alot of
range checking, [ecl_devices](https://index.ros.org/p/ecl_devices) will
test for errors on every read/write.

### Release Mode

Define either `NDEBUG` or `ECL_NDEBUG`. e.g.



```
g++ -DNDEBUG -lecl_devices -o hello hello.cpp
```



This will disable alot of the aforementioned error handling - especially
those inside fast control blocks. If you want to do error handling in
these blocks, check the return values for each function manually.

### Inside Ros

In ros, the `NDEBUG` macro is automatically added by the cmake build
system when choosing to build in `Release` mode.

## Error Handling in the ECL

### Macros

ecl_errors defines a macro, `LOC`, is a
means of picking up the current file and line number of the point at
which it is processed. Example code further below.

### Error Flags

A set of flags is provided through the enumeration `ecl::ErrorFlag`.
These, when coupled with the `ecl::Error` (error handler) class and
`LOC` macro provide a convenient means of quickly identifying errors
produced by the ecl libraries regardless of the platform that is used.



```cplusplus
ecl::Error void f(const int &i) const {
    if ( i == 3 ) { 
        return ecl::Error(ecl::NoError);
    } else {
        return ecl::Error(ecl::OutOfRangeError);
    }   

int main() {
    ecl::Error error = f(5);
    if ( error.flag() != NoError() ) {
        error.print(LOC);
    }
    // output is ~ 'my_main.cpp : 11 - Out of range error.'
    return 0;
}
```



The `ecl::Error` class can be extended to customise the error
messages - refer to
[ecl_time_lite](https://index.ros.org/p/ecl_time_lite) and the
`ecl::TimeError` class for an example.

## Assertions in the Ecl

### Run-Time Assert/Abort

These functions, because they are coupled with fallback macros for
debug/ndebug modes, are the only functions in the ecl not namespaced
inside the ecl namespace. Rather they are prefixed with ecl_.

The `ecl_run_time_assert` macro/function is a tool for conditional
testing. It is governed by the presence of the `NDEBUG` macro. If
`NDEBUG` is absent (either in your code or c-flagged by the compiler
(`-DNDEBUG`) then run_time_assert will equate to a macro that defers
to a null function pointer. This is the fastest means of bypassing
debugged code.

If `NDEBUG` is defined, then `ecl_run_time_assert` will act as a
conditional test via a function. If the test fails, it will output some
data (that you have passed to the function) before finally aborting.



```cplusplus
int i = 3;
int j = 2;
ecl_run_time_assert(i < j, LOC, "Illegal context, need i < j");
```



The `ecl_runtime_abort` macro/function works similarly except that it
does no conditional test and it is not negated by the presence of
`NDEBUG`.

#### Compile-Time Assert

There is also a macro which works as a compile time equivalent of
`ecl_run_time_assert()`. This macro is useful for checking template
parameters mostly. When passed a logical condition which fails, an
eye-catching COMPILE_TIME_FAILURE is reported in the compile log.



```cplusplus
ecl_compile_time_assert( 1 > 3 )
```



Corresponding failure is reported in a format similar to the example
output shown below:



```cplusplus
test.cpp:47: error: invalid application of ‘sizeof’ to incomplete type ‘COMPILE_TIME_FAILURE<false>’
```

## Tutorials

- [Assertions in the Ecl](#assertions-in-the-ecl):
  how to utilise ecl's run-time and compile-time asserts/aborts.
- [Debug Modes in the Ecl](#debug-modes-in-the-ecl):
  Toggling debug/ndebug mode for the ecl.
- [Error Handling in the ECL](#error-handling-in-the-ecl):
  Shows how the ecl does error handling at the simplest level, with
  macros and flags.
