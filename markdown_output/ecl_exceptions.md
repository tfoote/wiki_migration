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

- Standard exceptions
- Data throwing exceptions
- Debug only exceptions
- Assert style exceptions
- Exception rethrowing

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

- [Ecl Exception Handling](#ecl-exception-handling)

## Examples

- `src/examples/exceptions.cpp` : coverage style test for exceptions.
- `src/examples/exception_tracer.cpp` : getting a backtrace via
  exceptions, posix style.

## Benchmarks

These are in [ecl_core_apps](https://index.ros.org/p/ecl_core_apps).

- `/src/benchmarks/exceptions.cpp` : benchmarks the latencies for
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

## Ecl Exception Handling

### Exception Types

#### Standard Exceptions

`ecl::StandardException` fulfills the general exception type used by
the ecl. Note we're just using one class for most exceptions -
typically c++ encourages throwing different classes of exceptions for
different error types, and we'll probably upgrade to that sometime.
Until now though, this has proved conveniently practical and we haven't
found any good reason to make things more complicated yet.

Anywhere you wish to throw an `ecl::StandardException`, throw it by
supplying the exception constructor some important information at the
point of failure (maybe naive!? if so, please enlighten!).

- `LOC`, the code location macro stamp defined in
  [ecl_errors](https://index.ros.org/p/ecl_errors).
- One of the `ErrorFlag` enum values defined in
  [ecl_errors](http://docs.ros.org/indigo/api/ecl_errors/html/flags_8hpp.html).
- Optionally an extra string customised to provide further detail.



```cplusplus
void f(int i) throw(StandardException) {
    if ( i > 5 ) { 
        throw StandardException(LOC,InvalidInputError,"The maximum input is 5.");
    }   
}
```



Typical output from this will be of the form:



```
Location : /mnt/froody/work/code/cpp/projects/ecl/modules/core/src/tests/exceptions.cpp:154
         : /mnt/froody/work/code/cpp/projects/ecl/modules/core/src/tests/exceptions.cpp:151
Flag     : There was a configuration error.
Detail   : Intentionally throwing in debug mode.
```



If you wish to manually catch and handle them, then you can implement a
handler as follows.



```cplusplus
try {
    f(6);
} catch ( StandardException &e) {
    cout << e.what() << endl;
    if ( e.flag() == ConfigurationError ) {
        // handle the error here.
    }
}
```



Note the use of the flag handler within the if statement.

#### DataExceptions

Another variant is the data exception which allows an additional data
object to be bundled with the exception. This is a templatised class.
Note, if you're going to output the error message, the data object
needs to be streamable to the standard output (if not, you will get a
compile time error).



```cplusplus

try {
    throw DataException<int>(LOC, ConfigurationError,"Throwing a data exception with an int.", 7);
} catch ( DataException<int> &e ) {
    std::cout << "Data: " << e.data() << std::endl;
    std::cout << e.what() << std::endl;
}
```



### Rethrowing Exceptions

You can also rethrow a StandardException, useful if you want to track
the source of the exception as it goes back up the program heirarchy.
This is done by passing the old exception to the constructor call of a
new throw.



```cplusplus
void f(int i) throw(StandardException) {
    if ( i > 5 ) {
        throw StandardException(LOC,InvalidInputError,"The maximum input is 5.");
    }
}

int main() {
    try {
        f(6);
    } catch (StandardException &e) {
        cout << e.what() << endl;
        throw StandardException(LOC,e);  // Rethrow with a new LOC
    }
}
```



### Disabling Exceptions

#### Disabling All Exceptions

Exceptions in any of the ecl libraries can be compiled out by simply
passing the `-DECL_DISABLE_EXCEPTIONS` to cmake when compiling the ecl
libraries (not your program!). If building in ros you can set this
variable in `\$ROS_ROOT/rosconfig.cmake`. Note that this variable is
picked up by ecl_config where it sets a macro that is used throughout by
the ecl libraries.

When you disable ecl exceptions, all ecl classes are designed in such a
way so that they can gracefully fall back to a lower form of error
handling.

#### Debug Only Exceptions

Exceptions can also be enabled exclusively for debug mode (so long as
`NDEBUG` is not defined) with the `debug_throw` and
`debug_throw_decl` macros. When `NDEBUG` is defined, the throw will
automatically disappear from the program code.



```cplusplus
void f(int i) ecl_debug_throw_decl(StandardException) {
    if ( i > 5 ) {
        ecl_debug_throw( StandardException(LOC,InvalidInputError,"The maximum input is 5.") );
    }
}
```



Catching can be done with the usual try-catch blocks, but if you want to
pre-process this code away as well, you can use the debug_try and
debug_catch macros.



```cplusplus
ecl_try {
    std::cout << "Try" << std::endl;
    ecl_throw(ecl::StandardException(LOC,ecl::OpenError));
} ecl_catch(ecl::StandardException &e) {
    std::cout << "Catch" << std::endl;
}
```



### Assertive Exceptions

In addition, you may use the `assert_throw` and `assert_throw_decl`
macros (a mechanism similar to the run_time_assert function in
[ecl_errors](https://index.ros.org/p/ecl_errors)) as follows:



```cplusplus
void f(int i) ecl_assert_throw_decl(StandardException) {
    ecl_assert_throw( i <= 5, StandardException(LOC,InvalidInputError,"The maximum input is 5.") );
}
```

## Tutorials

- [Ecl Exception Handling](#ecl-exception-handling):
  Introduction to the usage of exceptions in the ecl.
