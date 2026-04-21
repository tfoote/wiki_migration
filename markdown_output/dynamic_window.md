This node is a robot controlled based on the Dynamic Window Approach
described in \"Fox, D.; Burgard, W.; Thrun, S., \"The dynamic window
approach to collision avoidance\" Robotics and Automation Magazine, IEEE
, vol.4, no.1, pp.23-33, Mar 1997\".

It differs from the original approach in that the best speed are found
by random sampling the search space instead of using a fixed step
incremental search. This allows the controller to run at a specific
frequency while still guaranteeing a good solution.

## Input

-   *odom*: the robot [nav_msgs/Odometry](odometry) message.
-   *base_scan*: the laser
    [sensor_msgs/laserscan](sensor_msgs/laserscan) message.
-   *cmd_vel_dwc*: the desired linear/rotational speed as a
    [geometry_msgs/twists](geometry_msgs/twists) message.
-   *base_link*: the robot base frame of referece.

## Output

-   *cmd_vel_dwc*: the node publishes the linear/rotational speeds as
    [geometry_msgs/twists](geometry_msgs/twists) messages.
-   *debug_point_cloud*: if enabled, the node publishes
    [sensor_msgs/Pointcloud](sensor_msgs/Pointcloud) messages
    corresponding to the laser scan.

## Parameters

-   *alpha, beta, gamma*: the importance weights given to heading,
    clearance and speed. See the original paper for the mathematical
    meaning of this parameters.
-   *vmax: *the maximum linear velocity of the robot.
-   *vpmax, vpbrake*: maximum linear acceleration and brake (reverse
    acceleration) of the robot.
-   *wmin, wmax*: minimum and maximum rotational velocities of the
    robot.
-   *wpmin, wpmax*: minimum and maximum rotational accelerations of the
    robot
-   *tcmax*: for how long (in seconds) should the controller search for
    an optimal value.It is the inverse of the frequency at which the
    controller should run.
-   *laser_max*: any laser reading below this value is not considered.
-   *robot_radius*: this is the radius of the circle that approximates
    the robot base.
-   *publish_pcl*; if the pointcloud showing the laser will be
    published.

## Code Stability

This code is stable. Although I cannot guarantee the absence of bugs,
I\'ve used it for several years with different robot platform and it
always proved reliable. Please feel free to send any comment and/or bug
report to lorenzo.riano (at) gmail.com.
