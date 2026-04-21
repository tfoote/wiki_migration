## Overview

Streams provide a standardised c++ interface for connecting to ecl
input-output devices.

-   *speed* : control cannot afford serious slowdowns for convenience.
-   *extensible* : must be able to create new devices easily.
-   *streams* : all devices should connect in a standardised way to
    streams.

## Other Streaming Libraries

Finding a library with a standard/extensible interface that works across
devices and implements streaming operators is like trying to find the
pot at the bottom of the rainbow.

## Compiling & Linking

Include the following at the top of any translation unit:

```cplusplus
#include <ecl/streams.hpp>

// Templatised all purpose stream
using ecl::TextStream;

// Convenience stream handles
using ecl::IConsoleStream;
using ecl::OConsoleStream;
using ecl::EConsoleStream;
using ecl::OFileStream;
using ecl::SerialStream;
using ecl::SharedFileStream;
using ecl::SocketClientStream;
using ecl::SocketServerStream;
using ecl::StringStream;

// Special customised streams
using ecl::LogStream;

// Stream manipulators
using ecl::endl;
using ecl::clrscr;
```

If outside ros, you will also need to link to *ecl_streams*.

## Tutorials

-   [Input and Output Streams](ecl_streams/Tutorials/Input and Output Streams)
    : general usage notes for ecl io streams.
-   [Logging Streams](ecl_streams/Tutorials/Logging Streams) : low
    overhead logging streams.
-   [Manipulators](ecl_streams/Tutorials/Manipulators) : utilities for
    ecl streams.
