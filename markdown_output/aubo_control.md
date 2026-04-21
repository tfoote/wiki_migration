## Overview

This package is part of the [aubo_robot](aubo_robot) program.

## Usage

Make sure have installed Peakcan driver, connect peackcan to aubo robot
i5.

To control the AUBO-i5 use USB-PCAN,run the joint_control node use the
following:



```
rosrun aubo_control joint_control_pcan
```



A teleop control panel to move the real robot,run



```
roslaunch aubo_description aubo_i5_rviz.launch
```



Choose PCAN bus interface, and select "Continuous move" mode.

Then we can control 6 joints with press button "+" and "-".

## Additional information

See also the relevant sections in the
[readme](https://github.com/auboliuxin/aubo_robot/blob/master/README.md)
on Github.
