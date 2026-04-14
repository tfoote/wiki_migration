# Quadrotor Handler

![Quadrotor in V-REP\|width=200](attachment:quadrotor.PNG)

The quadrotor handler has mainly two functions:

-   Publish the state of the robot :
-   Quadrotor pose w.r.t. the world frame (linear position and angular
    position) as a
    [PoseStamped Message]( http://mirror.umd.edu/roswiki/doc/diamondback/api/geometry_msgs/html/msg/PoseStamped.html)
-   Quadrotor twist w.r.t the world frame (linear and angular velocity)
    as a
    [TwistStamped Message](http://mirror.umd.edu/roswiki/doc/diamondback/api/geometry_msgs/html/msg/TwistStamped.html)
-   Receive commands from ROS and apply them to the quadrotor:
-   We consider the first four fields of the effort vector from the
    message
    [ JointState](http://docs.ros.org/api/sensor_msgs/html/msg/JointState.html).
    The first three values will be the torques to apply in x,y and z (of
    the body frame) and the last one the thrust.
