## Nodes

### explore

The explore node implements frontier based exploration. It actively
builds a map of its environment by visiting unknown areas.



```clearsilver
pub {
  0.name= visualization_marker
  0.type= visualization_msgs/Marker
  0.desc= Arrows that show current frontiers (blue) and currently selected frontier(green) 
  1.name= ~<name>/map
  1.type= nav_msgs/OccupancyGrid
  1.desc= Current map
}
srv{
  0.name= ~<name>/explore_map
  0.type= nav_msgs/GetMap
  0.desc= Allows an external user to ask for the current map
}
param {
  0.name= ~<name>/planner_frequency
  0.default= 1.0
  0.type= double
  0.desc= Frequency at which to update goals

  1.name= ~<name>/visualize
  1.default= true
  1.type= boolean
  1.desc= If true, explore will publish the current map and frontiers

  2.name= ~<name>/navfn/robot_base_frame
  2.default= "base_link"
  2.type= string
  2.desc= The frame of the robot base
}
```



#### Action API

The `explore` node implements a `SimpleActionClient` (see
[ actionlib documentation](actionlib )) that generates goals containing
`geometry_msgs/PoseStamped` messages.

##### Action Published Topics



```clearsilver
pub {
  no_header= True
  0.name= move_base/goal
  0.type= move_base_msgs/MoveBaseActionGoal
  0.desc= A goal to pursue in the world. 
}
```



#### Component Parameters

The `explore` node contains components that have their own ROS APIs
and parameters. These components are:

-   [costmap_2d](costmap_2d) - Parameters should be set under
    <name>/explore_costmap
-   [navfn](navfn) - Parameters should be set under
    <name>/explore_planner

#### Examples

See [explore_stage](explore_stage) for examples how to use the explore
node.
