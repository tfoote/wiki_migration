## Overview

This provides a portable set of time functions that are especially
useful for porting other code or being wrapped by higher level c++
classes. Code has been divided broadly via a set of cmake probes into
the following groups:



```cplusplus
- ECL_HAS_WIN_TIMERS
- ECL_HAS_MACH_TIMERS - apple operating systems.
- ECL_HAS_RT_TIMERS
- ECL_HAS_POSIX_TIMERS - the fallback posix functions when -lrt is not available.
```



## Compiling & Linking



```cplusplus
#include <ecl/time_lite.hpp>

// The portable time functions.
using ecl::time_lite::sleep;
using ecl::time_lite::sleep_until;
using ecl::time_lite::epoch_time;

// Platform specific function (requires linking to -lrt).
using ecl::time_lite::cpu_time;
```



If outside ros, you will also need to link to `ecl_time_lite`.

## Usage

### Time Functions

The function epoch_time is often not exactly epoch time (i.e. secs from
1970), but dependant on your platform. Nonetheless, it always provides a
relative timer measuring in sec/nsecs. Note that the time is only
guaranteed to be monotonic (i.e. it won't jump) if cmake has defined
the `ECL_HAS_CLOCK_MONOTONIC` macro.

The function cpu_time which is the amount of time that the process has
actually spent executing on the cpu. This is sometimes useful for
benchmarking tests.

### Error Handling

Use with the TimeError (an extension of [ecl_errors](ecl_errors)'s
Error handler) that provides time function specific verbose error
messages.



```cplusplus
ecl::TimeStructure duration;
duration.tv_sec = 1;
duration.tv_nsec = 300000000;
ecl::TimeError error = ecl::sleep(duration);
if ( error.flag() != ecl::NoError) {
     std::cout << error.what() << std::endl;
     // do something
}
```



### Macros

The cmake detection scripts configure the header
`ecl/time_lite/config.hpp` with many macros that describe your
platform and also your time implementation in detail (particularly with
posix, there are alot of levels and optionally available api). These are
mostly for internal purposes, but may be useful to the user.



```cplusplus
#ifdef ECL_HAS_CPUTIME
  ecl::TimeStructure time;
  ecl::TimeError error = ecl::cpu_time(time);
  if ( error.flag() == ecl::NoError) {
    // benchmarking code result printout
  }
#endif
```



## Examples

-   `src/examples/time_functions`
