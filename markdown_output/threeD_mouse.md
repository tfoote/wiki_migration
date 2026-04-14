A simple ROS interface to the 3DConnexion 3D mouse.

## Overview

This node is a ROS wrapper around the
[spacenav library](http://spacenav.sourceforge.net). Refer to their
website to install the library on your computer first.

You can then compile the node by running: ```
$ rosmake threeD_mouse
```

## ROS API

### Published Topics

-   \'\'\'/three_d_mouse/pose topic\'\'\': The node publishes
    [geometry_msgs](geometry_msgs)/poseStamped messages to this topic.

### Parameters

-   \'\'\'publish_frequency\'\'\': You can change the rate at which the
    mouse publishes data. Default is 20Hz.

## Changing Modes

It can be operated in three different modes:

-   \'\'\'translation\'\'\' only
-   \'\'\'rotation\'\'\' only
-   or \'\'\'both\'\'\'

You can change between those modes by pressing the 2 buttons of the
mouse. The button of the left changes between \'\'\'translation\'\'\'
and \'\'\'rotation\'\'\' mode, while the one on the right changes
between \'\'\'both\'\'\' and \'\'\'translation\'\'\' or
\'\'\'rotation\'\'\'. A ROS_INFO message is printed when you change
modes.
