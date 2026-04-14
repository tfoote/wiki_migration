## Documentation

This is a conversion package to convert tf2 data to bullet data
structures. These functions are templated.

### Supported datatypes

  -- -------------------------------------------------------------------------------------------------------------- -- --------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ROS message type                                                                                                  supported datatype             Function to apply transform                                                                                                                                                                                               
     [geometry_msgs::PointStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/PointStamped.html)              tf2::Stamped\<btVector3\>      doTransform(const tf2::Stamped\<btVector3\>& t_in, tf2::Stamped\<btVector3\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TransformStamped.html)& transform)       
     [geometry_msgs::TransformStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TransformStamped.html)      btTransform                    doTransform(const tf2::Stamped\<btTransform\>& t_in, tf2::Stamped\<btTransform\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TransformStamped.html)& transform)   
  -- -------------------------------------------------------------------------------------------------------------- -- --------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

### How to use

Please see the
[ Code API documentation](http://docs.ros.org/jade/api/tf2_bullet/html )
for use.
