## Documentation

This is a conversion package to convert tf2 data to KDL data structures.
These functions are templated.

### Supported datatypes

  -- -------------------------------------------------------------------------------------------------------------- -- ----------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ROS message type                                                                                                  Library datatype                 Transform function                                                                                                                                                                                                        
     [geometry_msgs::PointStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/PointStamped.html)              tf2::Stamped\<KDL::Vector\>      doTransform(const tf2::Stamped\<KDL::Vector\>& t_in, tf2::Stamped\<KDL::Vector\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TransformStamped.html)& transform)   
     [geometry_msgs::TransformStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TransformStamped.html)      KDL::Frame                                                                                                                                                                                                                                                 
     [geometry_msgs::PoseStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/PoseStamped.html)                tf2::Stamped\<KDL::Frame\>       doTransform(const tf2::Stamped\<KDL::Frame\>& t_in, tf2::Stamped\<KDL::Frame\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TransformStamped.html)& transform)     
     [geometry_msgs::TwistStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TwistStamped.html)              tf2::Stamped\<KDL::Twist\>       doTransform(const tf2::Stamped\<KDL::Twist\>& t_in, tf2::Stamped\<KDL::Twist\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TransformStamped.html)& transform)     
     [geometry_msgs::WrenchStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/WrenchStamped.html)            tf2::Stamped\<KDL::Wrench\>      doTransform(const tf2::Stamped\<KDL::Wrench\>& t_in, tf2::Stamped\<KDL::Wrench\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/jade/api/geometry_msgs/html/msg/TransformStamped.html)& transform)   
  -- -------------------------------------------------------------------------------------------------------------- -- ----------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

### How to use

Please see the
[ Code API documentation](http://docs.ros.org/jade/api/tf2_kdl/html )
for use.
