## Overview

**rosconsole_bridge** is a package used in conjunction with
[console_bridge](console_bridge) and [rosconsole](rosconsole) for
connecting [console_bridge](console_bridge)-based logging to
[rosconsole](rosconsole)-based logging.

## Usage

If you have an application or library that is utilizing
[console_bridge](console_bridge) for logging, the logging information
will be written to stdout. Applications/libraries that utilize
[rosconsole](rosconsole) do not follow this behavior, but rather write
their output to both stdout (depending on log level) as well as the ROS
topic /rosout.

If you have a console_bridge application or library, you can have its
output be written to /rosout by simply having your package depend on
rosconsole_bridge. Additionally, a call to REGISTER_ROSCONOLE_BRIDGE has
to be added to the ROS node. (See
<https://github.com/ros/rosconsole_bridge/issues/12>).

## See Also

-   [rosconsole](rosconsole)
-   [console_bridge](console_bridge)
