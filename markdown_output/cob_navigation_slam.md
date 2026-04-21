## Overview

This package contains launch files for the [move_base](move_base) and
[gmapping](gmapping) nodes meant to be run in an application that
requires SLAM-based global navigation.

## Applications

-   **`launch/2dnav_ros_tr.launch`**: Starts global navigation with
    the trajectory rollout local planner and SLAM.
-   **`launch/2dnav_ros_dwa.launch`**: Starts global navigation with
    the DWA local planner and SLAM.
-   **`launch/2dnav_linear.launch`**: Starts global navigation with
    the simple linear navigation [cob_linear_nav](cob_linear_nav) and
    SLAM.

Furthermore it holds a launch file for the internal SLAM algorithm of
Fraunhofer IPA.

-   **`launch/2dnav_ipa.launch`**: Starts global navigation with the
    IPA navigation and SLAM algorithm.

## NOTE

When you run `2dnav_ros_tr.launch` or `2dnav_ros_dwa.launch`, the
robot might start with the **rotating recovery behaviour** after the
first goal has been sent to the 'move_base_simple/goal' topic. This is
probably due to the robot standing in mainly unknown space. Please make
sure, that this can happen without running into obstacles or persons.
