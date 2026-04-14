## Documentation

This is a conversion package to convert tf2 data to eigen data
structures. These functions are templated.

### Supported datatypes

  -- -------------------------------------------------- -- ---------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     ROS message type                                      library datatype                            Transform function                                                                                                                                                                                                                          
     \<\<MsgLink(geometry_msgs/PointStamped)\>\>           \`tf2::Stamped\<Eigen::Vector3d\>\`         doTransform(const tf2::Stamped\<Eigen::Vector3d\>& t_in, tf2::Stamped\<Eigen::Vector3d\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/noetic/api/geometry_msgs/html/msg/TransformStamped.html)& transform)           
     \<\<MsgLink(geometry_msgs/QuaternionStamped)\>\>      \`tf2::Stamped\<Eigen::Quaterniond\>\`      doTransform(const tf2::Stamped\<Eigen::Quaterniond\>& t_in, tf2::Stamped\<Eigen::Quaterniond\>& t_out, const [geometry_msgs::QuaternionStamped](http://docs.ros.org/noetic/api/geometry_msgs/html/msg/QuaternionStamped.html)& transform)   
     \<\<MsgLink(geometry_msgs/TransformStamped)\>\>       \`tf2::Stamped\<Eigen::Isometry3d\>\`       doTransform(const tf2::Stamped\<Eigen::Isometry3d\>& t_in, tf2::Stamped\<Eigen::Isometry3d\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/noetic/api/geometry_msgs/html/msg/TransformStamped.html)& transform)       
     \<\<MsgLink(geometry_msgs/TransformStamped)\>\>       \`tf2::Stamped\<Eigen::Affine3d\>\`         doTransform(const tf2::Stamped\<Eigen::Affine3d\>& t_in, tf2::Stamped\<Eigen::Affine3d\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/noetic/api/geometry_msgs/html/msg/TransformStamped.html)& transform)           
     \<\<MsgLink(geometry_msgs/PoseStamped)\>\>            \`tf2::Stamped\<Eigen::Affine3d\>\`         doTransform(const tf2::Stamped\<Eigen::Affine3d\>& t_in, tf2::Stamped\<Eigen::Affine3d\>& t_out, const [geometry_msgs::TransformStamped](http://docs.ros.org/noetic/api/geometry_msgs/html/msg/TransformStamped.html)& transform)           
  -- -------------------------------------------------- -- ---------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

### How to use

Please see the
[ Code API documentation](http://docs.ros.org/noetic/api/tf2_eigen/html )
for use.
