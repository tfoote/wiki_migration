## Purpose

The messages in `derived_object_msgs` are meant to represent, with as
much detail as possible, detected objects derived from sensor data. The
contents of this package is somewhat skewed toward autonomous automotive
vehicles but also contains generic messages such as Object.

## Provided Message Types

In order to provide as much detail as can be provided by most sensors
available today, the Object message contains:

-   A `detection_level` to indicate whether the object has only been
    "detected" or whether it is "tracked" (indicating more than one
    detection).
-   A
    [geometry_msgs/Pose](http://docs.ros.org/melodic/api/geometry_msgs/html/msg/Pose.html)
    to indicate the object's estimated position and orientation.
-   A
    [geometry_msgs/Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
    to represent the object's estimated linear and angular velocities.
-   A
    [geometry_msgs/Accel](http://docs.ros.org/api/geometry_msgs/html/msg/Accel.html)
    to indicate the object's estimated linear and angular
    accelerations.
-   A
    [geometry_msgs/Polygon](http://docs.ros.org/api/geometry_msgs/html/msg/Polygon.html)
    to precisely define the detected object's estimated outer edge
    profile.
-   A
    [shape_msgs/SolidPrimitive](http://docs.ros.org/api/shape_msgs/html/msg/SolidPrimitive.html)
    to represent a shape primitive which completely encompasses the
    object's outer bounds (mostly for visualization).
-   An object classification, if one has been determined by any of the
    detecting sensors.
-   A classification certainty.
-   A classification age.

In addition, other messages which represent real-world objects at a high
level include things like Lanes, Lane Models, and Closest In-Path
Vehicles.
