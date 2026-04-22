## Documentation

Set of tools for mobile robot navigation with depth sensor, for example
Microsoft Kinect.

### Packages

-   [laserscan_kinect](laserscan_kinect) - Converts a depth image coded
    with uint16 to laser scan 2D
    ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)).
-   [cliff_detector](cliff_detector) - Detects negative objects like a
    cliff or downstairs.
-   [depth_sensor_pose](depth_sensor_pose) - Detects ground plane in
    depth image and estimates height and tilt angle of depth sensor.
-   [nav_layer_from_points](nav_layer_from_points) - Creates navigation
    costmap layer based on received points coordinates in robot frame.
-   [depth_nav_msgs](depth_nav_msgs) - Defines specific messages for
    other packages.

## Report a Bug
