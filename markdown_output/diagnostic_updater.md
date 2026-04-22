## Diagnostic Updater API

diagnostic_updater provides a variety of C++ utilities to assist in
integrating diagnostics with your software. Common updater tasks
include:

-   publishing the status of a sensor data topic on a device driver
-   reporting that a hardware device is closed
-   reporting an error when a value is out of bounds, e.g. temperature
    It also provides a Python API very similar to the C++ API

### Examples and Tutorials

A working example of a diagnostic_updater can be found in
[diagnostic_updater/src/example.cpp](http://www.ros.org/doc/api/diagnostic_updater/html/example_8cpp_source.html).
This example goes through some of the most common uses of an updater.

### API Stability

The documented C++ API is widely used and should be considered stable.

### diagnostic_updater::DiagnosticStatusWrapper

The
[diagnostic_updater::DiagnosticStatusWrapper](http://www.ros.org/doc/api/diagnostic_updater/html/classdiagnostic__updater_1_1DiagnosticStatusWrapper.html)
class eases the pain of filling out a
[diagnostic_msgs/msg/DiagnosticStatus](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticStatus.html)
message. It handles setting the summary, possibly with `printf`-type
formatting of the message field, and setting of key-value pairs with
type-conversion and formatting of the values. It also has facilities for
merging multiple
[diagnostic_msgs/msg/DiagnosticStatus](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticStatus.html)
messages without losing information in the status message.

### diagnostic_updater::Updater

The
[diagnostic_updater::Updater](http://www.ros.org/doc/api/diagnostic_updater/html/classdiagnostic__updater_1_1Updater.html)
class manages a set of diagnostic update functions, and their periodic
publication.

### diagnostic_updater::DiagnosedPublisher

Monitoring a topic's frequency, a common diagnostics feature, and the
validity of its timestamps can be done using pre-packaged diagnostic
update functions. A
[diagnostic_updater::DiagnosedPublisher](http://www.ros.org/doc/api/diagnostic_updater/html/classdiagnostic__updater_1_1DiagnosedPublisher.html)
wraps a Publisher and standard diagnostics that relate to it in a single
class.

Topics with expected frequency lower than 1 Hz are supported. However,
`DiagnosedPublisher` will report the
[diagnostic_updater::TimeStampStatus](https://docs.ros.org/en/api/diagnostic_updater/html/classdiagnostic__updater_1_1TimeStampStatus.html)
task in WARNING state for the periods when no message came. If you want
to work around this limitation and report the timestamp status as OK in
the empty periods, you have to manually create a task of type
[diagnostic_updater::SlowTimeStampStatus](https://docs.ros.org/en/api/diagnostic_updater/html/classdiagnostic__updater_1_1SlowTimeStampStatus.html)
and use it together with a
[diagnostic_updater::FrequencyStatus](https://docs.ros.org/en/api/diagnostic_updater/html/classdiagnostic__updater_1_1FrequencyStatus.html)
task instead of the `DiagnosedPublisher`.
