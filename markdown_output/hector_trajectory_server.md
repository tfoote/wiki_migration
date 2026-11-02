## Documentation

This package provides a node that saves [tf](https://index.ros.org/p/tf)
based trajectory data given a target and and source frame. The
trajectory is saved internally as a
[nav_msgs/msg/Path](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Path.html)
and can be obtained using a service or topic. Internally, a
tf::Transformlistener listens to [tf](https://index.ros.org/p/tf),
performs the necessary transformations and pushes resulting poses to the
saved trajectory. The update and publish rates can be modified by
parameters as described below.

## ROS API

<a id="NodeApi"></a>



```clearsilver
node.0 {
name=hector_trajectory_server
desc=`hector_trajectory_server` is a node that saves trajectory data and makes it available using the ROS API described below.

sub{
0.name= syscommand
0.type= std_msgs/String
0.desc= System command. If the string equals "reset" the saved trajectory is cleared.
}
pub{
0.name=trajectory
0.type= nav_msgs/Path
0.desc= Get the traveled trajectory from this latched topic.
}
 srv {
   0{
    name = trajectory
    type = hector_nav_msgs/GetRobotTrajectory
    desc = Call this service to get the traveled trajectory.
    }
  }
param{
    0.name = ~target_frame_name
    0.type = string
    0.default = `"map"`
    0.desc = The name of the [[tf]] target frame 
    1.name = ~source_frame_name
    1.type = string
    1.default = `"base_link"`
    1.desc = The name of the [[tf]] source frame
    2.name = ~trajectory_update_rate
    2.type = double
    2.default = 4.0
    2.desc = The update rate [hz] for the saved trajectory
    3.name = ~trajectory_publish_rate
    3.type = double
    3.default = 0.25
    3.desc = The publish rate [hz] for the trajectory published on the "trajectory" topic.


}
}
}
```
