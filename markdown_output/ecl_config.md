## Overview

Different platforms have minor differences in their implementations of
c/c++. The most obvious of these is integer representations (e.g.
16/32/64 bit types). This package uses cmake detection scripts to check
your platform's implementation and define some cross platform macros,
types and classes that facilitate easy handling of these fundamental
properties.

Major platform support includes posix/apple and mingw/msvc (partial).

## Compiling & Linking

Include the following at the top of any translation unit that utilises
the configuration definitions and tools.



```cplusplus
#include <ecl/config.hpp>

// Functions
using ecl::is_big_endian;
using ecl::is_char_signed;

// Types - refer to ecl/config/portable_types.hpp
using ecl::int8;
using ecl::uint8;
// ...
```



## Under the Hood

CMake can do the hard yards on most platforms/toolchains and autodetect
what variables and headers can be used - this works mostly for the main
platforms as outlined above. The result of this guesswork are a suite of
macros stored in the `ecl/config/ecl.hpp` header. All macros are
prefixed by an `ECL`, e.g. `ECL_IS_POSIX`.

When autodetection fails (you have a very embedded board, or your
toolchain has been patched together in a very non-standard way) there is
provision to manually supply details via the `ECL_IS_CUSTOM` macro.
Refer to the
[custom platform detection tutorial](ecl_config/Tutorials/Custom Platform Detection).

Note that other packages also do some platform detection to varying
degrees, e.g ecl_time_lite. The macros defined here are the most general
purpose macros only.

## Reference

### Macros



```
// Platform macros - automatically detected by the build.
- ECL_IS_POSIX || ECL_IS_WIN32 || ECL_IS_APPLE || ECL_IS_CUSTOM
- ECL_HAS_POSIX_THREADS || ECL_HAS_WIN32_THREADS
- ECL_SIZE_OF_CHAR
- ECL_SIZE_OF_SHORT
- ECL_SIZE_OF_INT
- ECL_SIZE_OF_LONG
- ECL_SIZE_OF_LONG_LONG
- ECL_SIZE_OF_FLOAT
- ECL_SIZE_OF_DOUBLE
- ECL_SIZE_OF_LONG_DOUBLE
- ECL_CHAR_IS_SIGNED || ECL_CHAR_IS_UNSIGNED
- ECL_HAS_SHARED_LIBS || ECL_HAS_STATIC_LIBS
// ECL Development macros
- ECL_DISABLE_EXCEPTIONS
- ECL_DONT_INLINE
- ECL_DEPRECATED
- ECL_PUBLIC || ECL_LOCAL
```



Note that you may predefine ECL_HAS_SHARED_LIBS or ECL_HAS_STATIC_LIBS
for your project if both are available and you want to force appropriate
behaviour for the target set you are linking against.

### Types

When you absolutely need to specify the bit-width type you need to use,
the following typedefs are defined by the ECL when the appropriate types
are available.



```
- ecl::int8,  ecl::uint8
- ecl::int16, ecl::uint16
- ecl::int32, ecl::uint32
- ecl::int64, ecl::uint64
- ecl::float32
- ecl::float64 
- ecl::float96 
- ecl::float128
```



### Platform Sniffers

Checking for *endianness*:



```
// The function operates like a macro, and a good compiler will compile
// out the if mechanism and leave behind the required section of code.
if ( ecl::is_big_endian() {
    // ...
}
```



To check if your default char type is signed, or otherwise, use the
following. Note that this only works for runtime checks. To do compile
time checks (for use in template parameters etc), there is the
ECL_CHAR_IS_SIGNED and ECL_CHAR_IS_UNSIGNED macros.



```cplusplus
if ( ecl::is_char_signed() {
   // ...
}
```


