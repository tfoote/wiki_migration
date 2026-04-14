# Overview

This package provides a publisher that interfaces with the yoctopuce
altimeter:
<http://www.yoctopuce.com/EN/products/usb-position-sensors/yocto-altimeter>.

To use, you must have the following dependencies: \`ros_cpp\`,
\`ros_py\`, \`std_msgs\`, \`nav_msgs\`, \`sensor_msgs\`.

# Sample Usage

To use this ROS package, you must install the C++ API from Yoctopuce.
Use the following link to download to your preferred location, and then
use the setup script to build.

<http://www.yoctopuce.com/EN/libraries.php>

Then, install this ROS package.

To make sure the yocto API is accessible during runtime:

`export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/yocto/cpp/api/Binaries/linux/64bits`

Then, to launch the node run:

`rosrun yoctopuce_altimeter yoctopuce_altimeter`

# Roadmap

Currently, this package only works with kinetic. If you are interested
in seeing support for other distros, please email the maintainer.

# Nodes

## yoctopuce_altimeter

### Published Topics

\`/yocto/raw\` Uses custom \`yocto_msg\` which publishes a header,
altitude, pressure, and temperature.

\`/yocto/odom\` Uses standard \`nav_msgs/odom\`. Edits the linear z
value.
