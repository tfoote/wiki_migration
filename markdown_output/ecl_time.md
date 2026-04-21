## Ecl Time vs Rostime

Many of the classes/methods in this package have many characteristics in
common with the [rostime](rostime) package - in fact they are almost
identical. It was made before ros came about and is kept in the ecl for
both legacy reasons and because it is still sometimes useful outside a
ros runtime environment (particularly when cross-compiling).

## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/time.hpp>

// The time classes
using ecl::Duration;
using ecl::MicroSleep;
using ecl::MilliSleep;
using ecl::NanoSleep;
using ecl::Sleep;
using ecl::Snooze;
using ecl::CpuWatch; // posix only
using ecl::StopWatch;
using ecl::TimeData;
using ecl::TimeStamp;
```

If outside ros, you will also need to link to *ecl_time*.

## Tutorials

-   [Timestamps and Durations](ecl_time/Tutorials/Timestamps and Durations)
    : timestamping and performing arithmetic on timestamps/durations.
-   [Sleep](ecl_time/Tutorials/Sleep) : classes that put the thread to
    sleep for fixed or periodic intervals.
-   [Stopwatch](ecl_time/Tutorials/Stopwatch) : devices to record the
    passing of time.
-   [Benchmarking](ecl_time/Tutorials/Benchmarking) : tools to assist
    benchmarking programs.

## Cross Platform Support

### Posix RT Timers

Posix timers record times as a pair : (seconds,nanoseconds), so they
have a very fine resolution, but it needs to remembered that the system
latency will still affect their results. For example, sleeping for 1
nanosecond wont work as you expect, since the system latency will
usually mean the command has to wait for the scheduler to grant it a
slice of the action (usually a wait of around 1ms on a linux desktop).
This latency is usually configured by the scheduler being used by the
kernel.

Returning to the pair, the first unit, seconds is usually of a system
defined type. This allows it to be extendable to a larger type in the
future if the system time requires a larger value. The latter is
measured with the long variable, which is more than sufficient to cater
for 1x10\^9 units.

### MacOSX Timers

MacOSX timers are mostly posix, however they are missing the extensions
provided by the librt library, e.g. `clock_gettime` and
`clock_nanosleep`. The real downside of this is that it is not
possible to use absolute time with the macosx posix timers (i.e.
periodic timers will drift).

There are another set of mac specific timers that will let you do this,
but it has not yet been implemented.

### Windows Timers

Not yet implemented.
