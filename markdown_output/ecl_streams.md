## Overview

Streams provide a standardised c++ interface for connecting to ecl
input-output devices.

- *speed* : control cannot afford serious slowdowns for convenience.
- *extensible* : must be able to create new devices easily.
- *streams* : all devices should connect in a standardised way to
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

- [Input and Output Streams](#input-and-output-streams)
  : general usage notes for ecl io streams.
- [Logging Streams](#logging-streams)
  : low overhead logging streams.
- [Manipulators](#manipulators) :
  utilities for ecl streams.

## Input and Output Streams

### Overview

Ecl streams work on top of ecl io devices.

### Initialisation

Each stream-device pair can be instantiated via the generic TextStream
object and the underlying device opened via the `device()` member
method. For example,



```cplusplus
TextStream<OFile> stream;
stream.device().open("dude.txt",New);
```



The console device is a special case - it is automatically opened.

### Convenience Classes

The preferred method of instantiation is via the constructor in the
convenience classes. The convenience classes are specialised interfaces
that inherit from the appropriate `Textstream` type (dependant on the
template parameter). Examples, `SerialStream`, `OFileStream`. Rather
than calling `stream.device().open(\...)` directly, you can use their
constructors to instantiate the stream. They are also more convenient
than typing out template parameters continuously.



```cplusplus
OFileStream stream("dude.txt",New);
```



### Output Streams

Output streams function similarly to the familiar cout stream. The
primary advantage being that they can easily be attached to any standard
ecl io device. They can also be used with the
[ecl formatter](https://index.ros.org/p/ecl_formatters) classes.



```cplusplus
OFileStream ostream;
Format<double> format; format.width(5); format.precision(2);
double d = 1.0/3.0;
ostream << format(d);  // This will send 0.33 to the stream.
ostream.flush();
```



### Input Streams

There are three ways to utilise an input stream:

- reading element by element (separated by whitespace or newlines).
- reading raw characters (you must call enableRawCharReads()).
- reading line by line (not yet enabled).

The first method is similar to the familiar cin, it will take a string
and convert it to the requested type.



```cplusplus
IConsoleStream istream;
double d;
istream >> d;
```



The second method is sometimes useful when communicated with raw
character devices (e.g. a serial line). In this situation, you must
simply make use of the char input operator.



```cplusplus
SerialStream serial_stream;
char c;
if ( serial_stream.device().remaining() ) {
     serial_stream >> c;
}
```



The third method has not yet been implemented.

### Error Checking

Output streams can generate errors that are not so easily checked
compared with handling devices directly. To check for failure, ecl
streams use a mechanism similar to that of the standard cout stream.



```cplusplus
ostream << 32.1;
if ( ostream.fail() ) {
    std::cout << ostream.errorStatus().what() << std::endl;
}
```

## Logging Streams

### Overview

`LogStream` is a convenient, fast means to logging from multiple
threads with multiple customisable modes. They can also optionally
automatically insert header and timestamp information.

The `LogStream` class is now mostly irrelevant if you are using ros
logging, though they are sometimes a useful low overhead alternative
(don't need the sometimes difficult to compile apache libraries) for
logging, specially when cross compiling.

### Usage

Multiple modes are most conveniently utilised via customised enums. For
example:



```cplusplus
enum LogModes {
    Warning,
    Error,
    Debug,
};
```



Note that this is an advantage over alot of other loggers in that it
gives you the freedom to define your own error logging levels. Each mode
can then be associated inside the log stream with its own customised
header.



```cplusplus
LogStream log_stream("test.log")
log_stream.enableMode(Warning,"WARNING");
log_stream.enableMode(Error,"ERROR");
log_stream.enableMode(Debug,"DEBUG");
```



This process can be repeated from multiple threads each with its own
instance of the log stream attached to the single file. Using the log
stream is then done via the macros `LOG` and `FLUSH`



```cplusplus
LOG(log_stream, Warning) << "This is a log message from main().\n";
FLUSH(log_stream)
```



By default this will automatically add header and timestamp information.
You can manually disable these if you prefer.

## Manipulators

### Overview

Ecl manipulators are defined to enable some similar functionality to
c++'s cout manipulators for ecl's streams. However they extend the
concept to use class instantiations rather than functions. This provides
one important advantage over the former, these manipulators can retain
state. Given that they're also easy to customise, this opens up many
possibilities.

The default manipulators defined in the ecl export a few global
instantiations, namely

- `ecl::endl`
- `ecl::clrscr`

### Usage

Using manipulators follows the same pattern as for standard c++ style
cout manipulators.



```cplusplus
int main() {
    ecl::OConsoleStream ostream;
    ostream << ecl::clrscr;
    ostream << "Dude" << ecl::endl;
    return;
}
```



### Creating your own Manipulators

Any manipulator that you wish to define must inherit from this parent
class in the following manner:



```
include <ecl/streams/manipulators.hpp>

class MyManipulator : public ecl::Manipulator<MyManipulator> {
    template <typename OutputStream>
    void action (OutputStream& ostream) {
        // ...
    }
};
```

## Tutorials

- [Input and Output Streams](#input-and-output-streams):
  General usage notes for input-output streams.
- [Logging Streams](#logging-streams):
  \## the next tutorial description (optional)
- [Manipulators](#manipulators):
  Manipulators for ecl streams.
