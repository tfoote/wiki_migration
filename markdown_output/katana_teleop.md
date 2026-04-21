## ROS API

This package provides the `katana_teleop_key` ROS node, which provides
a keyboard-based teleoperation for the Neuronics Katana 450 arm.

```clearsilver

node.0 {
name = katana_teleop_key
desc = This nodes provides keyboard-based teleoperation of a Neuronics Katana 450 arm.

param{
    0.name = increment
    0.type = double
    0.desc = gives the value by which the joint position will be altered, by default: 0.017453293 rad = 1 degree
    0.default = 0.017453293
    1.name = increment_stepsize
    1.type = double
    1.desc = gives the value by which the increment can be increased/decreased, by default: 0.017453293 rad = 1 degree
    1.default = 0.017453293
    2.name = increment_step_scaling
    2.type = double
    2.desc = gices the value by which the increment_stepsize can be scaled while in/decreasing the increment
    2.default = 1.0
  }
sub{
    0.name = joint_states
    0.type = sensor_msgs/JointState
    0.desc = The node subscribes to the joint_states topic and alters the joint state according to the keyboard input.
  }
}
```

#### Usage

-   Press 'ws' to increase/decrease the joint position about one
    increment
-   Press 'ad' to switch to the next/previous joint \* Press '0-5'
    to choose a joint/gripper
-   Press '+#' to alter the increment by a +1/-1 increment_step_size
    \* increment_step_scaling
-   Press ',.' to alter the scaling factor by -/+ 1.0
-   Press 'r' to return to the arm's initial pose
-   Press 'i' to display this manual and the current joint state
-   Press 'q' to shutdown the node (the arm will be reset to it's
    initial pose first)
-   NOTICE: this initial position might not be a proper resting pose to
    switch off the arm's power supply
