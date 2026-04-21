## Overview

sr_utilities contains a merger for the joint_states. It is a simple and
non optimal merger:

-   subscribe to two joint_states topics
-   when a message is received on one of those topics, wait until
    another message is received on the second topic.
-   when both messages are received, publish the merged message to the
    output topic.

Please note that the robot_state_publisher should soon implement this
feature (with a cleaner implementation), as stated by Wim in the
[mailing list](http://ros-users.122217.n3.nabble.com/merging-different-joint-states-td2289189.html).

## ROS API

### Input Topics

The node subscribes to the two topics to merge:
**/srh/position/joint_states** and **/sr_arm/position/joint_states**.
These are hard coded for the time being.

### Output Topics

Publishes the merged joint state messages to **/position/joint_states**.
