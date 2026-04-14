## Overview

This package is intended to contain a collection of simulated radar
sensor plugins for different Ainstein products. All radar plugins are
based on the existing laser
[RayPlugin](https://osrf-distributions.s3.amazonaws.com/gazebo/api/dev/classgazebo_1_1RayPlugin.html)
with additional processing to convert laser range detections to radar
targets and publish them as
\<\<MsgLink(ainstein_radar_msgs/RadarTargetArray)\>\> messages.

While the `libgazebo_radar_sensor_plugin.so` shared library (plugin) is
intended to be generic enough to simulate any Ainstein radar, it
currently only is valid for 1d radars (a vertical scan dimension could
be added and used to fill the elevation angle data), does not support
target speed (this might be able to be computed numerically from
successive scans) and the SNR is filled from the returned ray intensity
(this has not really been tested and may be a bad idea).

## Install Instructions

Once the package has been built (as normal in the catkin workspace),
copy the folder(s) inside the `models/` directory to somewhere on your
`GAZEBO_MODEL_PATH`, eg. `~/.gazebo/models` which can be added to your
model path (if it isn\'t already) by adding this to your `.bashrc`:

`export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/.gazebo/models`

Also, make sure that `~/catkin_ws/devel/lib/` is on your
`GAZEBO_PLUGIN_PATH` as this is where the shared library will be built.
To do this, add the following to your `.bashrc`:

`export GAZEBO_PLUGIN_PATH=$GAZEBO_PLUGIN_PATH:~/catkin_ws/devel/lib`

To test that the sensor is able to be loaded correctly in Gazebo (before
adding it to another model), use the provided test.launch file to
attempt to start Gazebo with the radar sensor. If you see an error about
not finding the .so file, check your `GAZEBO_PLUGIN_PATH`.
