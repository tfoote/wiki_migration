## Documentation

This package allows to convert ros messages to tf2 messages and to
retrieve data from ros messages.

### Supported Conversions

  -- ---------------------------------------------------------------------------------------------------------------- -- --------------------------------- --
     ros message type                                                                                                    tf2 datatype                      
     [geometry_msgs::Quaternion](http://docs.ros.org/jade/api/geometry_msgs/html/msg/Quaternion.html)                    tf2::Quaternion                   
     [geometry_msgs::QuaternionStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/QuaternionStamped.html)      tf2::Stamped\<tf2::Quaternion\>   
     [geometry_msgs::Transform](http://docs.ros.org/jade/api/geometry_msgs/html/msg/Transform.html)                      tf2::Transform                    
     [geometry_msgs::Pose](http://docs.ros.org/jade/api/geometry_msgs/html/msg/Pose.html)                                tf2::Transform                    
  -- ---------------------------------------------------------------------------------------------------------------- -- --------------------------------- --

### Supported Data Extractions

Timestamps and frame IDs can be extracted from the following
geometry_msgs

-   [Vector3Stamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/Vector3Stamped.html)
-   [PointStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/PointStamped.html)
-   [PoseStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/PoseStamped.html)
-   [QuaternionStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/QuaternionStamped.html)
-   [TransformStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TransformStamped.html)

### How to use

Please see the Code API documentation (top right of this page) for use.
