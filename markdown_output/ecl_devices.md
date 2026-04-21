## Overview

Devices provide a c++ interface (usually on top of a lower level api
such as posix) for input-output manipulation.

It's pretty hard to find a library that treats devices in anything but
an ad-hoc way. There is no consistent interface. This attempts to bring
that to the subset of devices that control systems use. It also allows
hooking of streams to each and any of the devices. Also of interest,
there are a few very theoretical approaches to writing c++ devices
(sources, sinks, seekable, etc ..). The ecl's first version too was
along these lines, but ultimately for control systems, being practical
wins over syntactic correctness.

The devices here are kept as consistent and practical as possible
without sacrificing speed.

## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/devices.hpp>

// Device Classes
using ecl::OFile;
using ecl::SharedFile;
using ecl::Serial;
using ecl::OConsole; // Also IConsole, EConsole, but dont use directly, use console streams instead.
using ecl::String;   // Dont use directly, use StringStream instead.
using ecl::SocketClient; // Simple and does ipv4 only.
using ecl::SocketServer; // Simple and does ipv4 only.
```



If outside ros, you will also need to link against *ecl_devices*.

## Tutorials

-   [Introduction to Ecl Devices](ecl_devices/Tutorials/Introduction to Ecl Devices)

## Examples

-   `src/examples/serial_timeout.cpp` : shows off the low latency
    timeout code \[posix only\].

These are in [ecl_core_apps](ecl_core_apps).

-   `src/benchmarks/files.cpp`
-   `src/demos/socket_client.cpp`
-   `src/demos/socket_server.cpp`
-   `src/utils/hex.cpp` : simple utility for reading/writing hex
    across the serial cable.
-   `src/utils/serial.cpp` : simple serial testing utility.
