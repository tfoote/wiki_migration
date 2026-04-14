The package provides:

-   map of the Bosch RTC facility
-   launch file for starting up the pr2_navigation stack
-   launch file for starting up the action server which enables sending
    the robot to different poses in the map frame

# Usage:

Start up the pr2_navigation stack:

```
roslaunch ds_pr2_2dnav drink_demo.launch
``` Start up the action server:

```
roslaunch ds_pr2_2dnav move_robot.launch
``` Definition of the action:

```
#goal definition
geometry_msgs/PoseStamped pose
---
#result definition
bool success
---
#feedback
``` Send the robot to the arbitrary pose:

```
rosrun ds_pr2_2dnav move_robot_client x y z qx qy qz qw
```
