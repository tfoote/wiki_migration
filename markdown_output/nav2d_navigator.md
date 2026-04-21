## General usage

The `navigator` is a ROS node that implements a path planner for
navigation and is supposed to be used in conjunction with the
'operator' node. Beside this, the whole functionality is provided by
the RobotNavigator class, which is exported by this package and can be
used from within other nodes as well.

Interaction with the Navigator is implemented using the
[actionlib](actionlib) interface. This allows other nodes (e.g. some
high level mission control) to start actions like goal navigation or
exploration, monitor the progress and eventually cancel an action in
progress. The following four actions are available:

-   MoveToPosition2D
-   !StartMapping
-   !StartExploration
-   Localize

## Example

See the [Navigator Tutorial](nav2d/Tutorials/RobotNavigator) for an
example how to setup the Navigator in Stage with a given map of the
environment.

## ROS Interface

```clearsilver
node {
  0.name=navigator
  0.desc=The `navigator` takes a map and the robot's position in this map to generate a path to a goal point and send motion commands to the `operator`.
  sub{
    0.name= scan
    0.type= sensor_msgs/LaserScan
    0.desc= Laser scans to update local costmap.
    1.name= tf
    1.type= tf/tfMessage
    1.desc= Transforms.
  }
  pub{
    0.name= cmd
    0.type= nav2d_operator/cmd
    0.desc= Motion command to the Operator.
    1.name= ~plan
    1.type= nav_msgs/GridCells
    2.name= ~markers
    2.type= visualization_msgs/Marker
    2.desc= Used to show current target. (Useful during exploration)
  }
  param {
    0.name= robot_id
    0.default=1
    0.type= int
    0.desc= Unique ID among robots in a Team.
    1.name= map_frame
    1.default= "map"
    1.type= string
    1.desc= TF frame of the map.
    2.name= robot_frame
    2.default= "robot"
    2.type= string
    2.desc= TF frame of the robot.
   11.name= map_service
   11.default= "get_map"
   11.type= string
   11.desc= Name of the service to get the map from. The Navigator will always query for a map using this service and not listen to a map topic.
    3.name= ~robot_radius
    3.default=0.3
    3.type= double
    3.desc= Radius of the robot, should be large enough so that the robot can turn in place anytime. (meter)
    4.name= ~map_inflation_radius
    4.default= 1.0
    4.type= double
    4.desc= Radius to increase cell costs around obstacles in the map. MUST be larger then robot_radius! (meter)
    5.name= ~navigation_goal_distance
    5.default= 1.0
    5.type= double
    5.desc= Stop navigation when distance to target is smaller then this value. Can be overitten by the MoveToPosition2D-!ActionGoal. (meter)
    6.name= ~navigation_goal_angle
    6.default= 1.0
    6.type= double
    6.desc= Tolerance when turning to target direction upon reaching the goal. When set to 0, ignore target heading. Can be overitten by the MoveToPosition2D-!ActionGoal. (radians)
    7.name= ~navigation_homing_distance
    7.default= 3.0
    7.type= double
    7.desc= Turn off obstacle avoidance (Operator drive_mode = 1) when distance to target is smaller then this value. Required to reach targets near obstacles. (meter)
   12.name= ~exploration_strategy
   12.default= "!NearestFrontierPlanner"
   12.type= string
   12.desc= Select the exploration module to load. Currently available are "!NearestFrontierPlanner", "!MultiWavefrontPlanner" and "!MinPosPlanner". The different strategies might have additional parameters.
    8.name= ~exploration_goal_distance
    8.default= 3.0
    8.type= double
    8.desc= Start checking for a new goal when distance to target is smaller then this value during exploration mode. (meter)
    9.name= ~min_replanning_period
    9.default= 3.0
    9.type= double
    9.desc= Replan period during navigation and exploration. (seconds)
   10.name= ~max_replanning_period
   10.default= 1.0
   10.type= double
   10.desc= Minimum time between replanning cycles, used during exploration only. (seconds)

}
```

```clearsilver
node{
  1.name=set_goal_client
  1.desc= Send a goal to the navigator via action interface.
  sub{
    0.name= goal
    0.type= geometry_msgs/PoseStamped
    0.desc= Goal pose to be reached.
  }
}
```

```clearsilver
node{
  2.name=get_map_client
  2.desc= Initialize mapping (drive forward and turn) via action interface.
  srv{
    0.name= StartMapping
    0.type= nav2d_navigator/SendCommand
    0.desc= Has to be called with param "3" for historic reasons.
  }
}
```

```clearsilver
node{
  3.name=explore_client
  3.desc= Start exploration via action interface.
  srv{
    0.name= StartExploration
    0.type= nav2d_navigator/SendCommand
    0.desc= Has to be called with param "2" for historic reasons.
  }
}
```
