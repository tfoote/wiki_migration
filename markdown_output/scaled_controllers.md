This repository contains controllers and hardware interface for
\`ros_control\` that are leveraging an on-the-fly speed scaling
mechanism. For example, they are used by the
[ur_robot_driver](http://wiki.ros.org/ur_robot_driver).

For this, the following subpackages exist:

-   A \'\'\'speed_scaling_interface\'\'\' to read the value of the
    current speed scaling into controllers.
-   A \'\'\'speed_scaling_state_controller\'\'\' that publishes the
    current execution speed as reported by the robot to a topic
    interface. Values are floating points between 0 and 1.
-   A \'\'\'scaled_joint_trajectory_controller\'\'\' that is similar to
    the \'\'joint_trajectory_controller\'\', but it uses the speed
    scaling reported by the robot to reduce execution speed of the
    trajectory.
