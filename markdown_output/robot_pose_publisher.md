## About

The `robot_pose_publisher` package contains a ROS node that will
publish the transform between the `/base_link` frame and the `/map`
frame as a pose message. This information is useful if you are
interested in the robots position but do not want to stream the entire
TF tree to get this information. An example use case is for web widgets.

## Nodes



```clearsilver
node.0 {
  name = robot_pose_publisher
  desc = `robot_pose_publisher` publishes the transform between the `/base_link` frame and the `/map` frame.
  pub {
    0.name = robot_pose
    0.type = geometry_msgs/Pose
    0.desc = The current transform between the `/base_link` frame and the `/map` frame as a pose message.
  }
}
```



## Installation

### Startup

To run the node, ensure that a valid transform exists between the
`/base_link` frame and the `/map` frame (e.g., from a navigation
node), and run the following: 

```
rosrun robot_pose_publisher robot_pose_publisher
```



## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/robot_pose_publisher/issues).
Feel free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)

------------------------------------------------------------------------

  -- ------------------------------------------------- -- ---------- -- -------------------------- --
     <tablewidth="100%"> ![](attachment:wpi.png)      <:99%>      ![](attachment:rail.png)   
  -- ------------------------------------------------- -- ---------- -- -------------------------- --
