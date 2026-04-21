The ROS interface to the extremum seeking control algorithms uses the
following topics:

-   `esc_in` (`esc_ros/StateValue`) State-value input to control
    algorithm
-   `obj_val` (`std_msgs/Float32`) Value input to control algorithm
-   `vel_ref` (`std_msgs/Float32MultiArray`) Velocity reference
-   `pos_ref` (`std_msgs/Float32MultiArray`) Position reference
-   `monitor_out` (`esc_ros/Monitors`) Internal monitor variables
