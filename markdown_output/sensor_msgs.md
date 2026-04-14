\<\<MsgSrvDoc(sensor_msgs)\>\>

A number of these messages have ROS [stacks](Stacks) dedicated to
manipulating them.

-   More information on how to use the
    \<\<MsgLink(sensor_msgs/LaserScan)\>\> message can be found in the
    [laser_pipeline](laser_pipeline) stack.
-   More information on how to use the
    \<\<MsgLink(sensor_msgs/Image)\>\> and
    \<\<MsgLink(sensor_msgs/CameraInfo)\>\> messages can be found in the
    [image_pipeline](image_pipeline) stack.
-   The \<\<MsgLink(sensor_msgs/JointState)\>\> message is published by
    [joint_state_controller](joint_state_controller), and received by
    [robot_state_publisher](robot_state_publisher) (which combines the
    joint information with [urdf](urdf) to publish a robot\'s [tf](tf)
    tree).
-   The [sensor_filters](sensor_filters) package provides easy-to-setup
    nodes and nodelets for running [filters](filters) on the sensor
    data.
