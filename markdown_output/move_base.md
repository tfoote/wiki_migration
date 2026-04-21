**NOTE: The \`move_base\` package lets you move a robot to desired
positions using the navigation stack. If you just want to drive the PR2
robot around in the odometry frame, you might be interested in this
tutorial:
[pr2_controllers/Tutorials/Using the base controller with odometry and transform information](pr2_controllers/Tutorials/Using the base controller with odometry and transform information).**

# ROS 2 succession

move_base is exclusively a ROS 1 package. It is succeeded by Navigation
2 in ROS 2.

-   [Comparison of move_base and Navigation 2](https://navigation.ros.org/about/ros1_comparison.html)
-   [Navigation 2 Documentation](https://navigation.ros.org/)
-   [Navigation 2 github repo](https://github.com/ros-planning/navigation2)

## Nodes

This package provides the \`move_base\` ROS Node which is a major
component of the [ navigation stack](navigation ). A detailed
description of this Node and its configuration options is found below.

### move_base

[ {{attachment:overview_tf_small.png}}](attachment:overview_tf.png )

The \`move_base\` node provides a ROS interface for configuring,
running, and interacting with the [ navigation stack](navigation ) on a
robot. A high-level view of the move_base node and its interaction with
other components is shown above. The blue vary based on the robot
platform, the gray are optional but are provided for all systems, and
the white nodes are required but also provided for all systems. For more
information on configuration of the \`move_base\` node, and the
navigation stack as a whole, please see the
[ navigation setup and configuration](navigation/Tutorials/RobotSetup )
tutorial.

#### Expected Robot Behavior

![](attachment:recovery_behaviors.png)

Running the \`move_base\` node on a robot that is properly configured
(please see [ navigation stack documentation](navigation ) for more
details) results in a robot that will attempt to achieve a goal pose
with its base to within a user-specified tolerance. In the absence of
dynamic obstacles, the move_base node will eventually get within this
tolerance of its goal or signal failure to the user. The \`move_base\`
node may optionally perform recovery behaviors when the robot perceives
itself as stuck. By default, the [move_base](move_base) node will take
the following actions to attempt to clear out space:

First, obstacles outside of a user-specified region will be cleared from
the robot\'s map. Next, if possible, the robot will perform an in-place
rotation to clear out space. If this too fails, the robot will more
aggressively clear its map, removing all obstacles outside of the
rectangular region in which it can rotate in place. This will be
followed by another in-place rotation. If all this fails, the robot will
consider its goal infeasible and notify the user that it has aborted.
These recovery behaviors can be configured using the
[ recovery_behaviors](#Parameters ) parameter, and disabled using the
[ recovery_behavior_enabled](#Parameters ) parameter.

#### Action API

The \`move_base\` node provides an implementation of the
\`SimpleActionServer\` (see [ actionlib documentation](actionlib )),
that takes in goals containing \`geometry_msgs/PoseStamped\` messages.
You can communicate with the \`move_base\` node over ROS directly, but
the recommended way to send goals to \`move_base\` if you care about
tracking their status is by using the \`SimpleActionClient\`. Please see
[ actionlib documentation](actionlib ) for more information.

##### Action Subscribed Topics

```clearsilver
sub {
  no_header= True
  0.name= move_base/goal
  0.type= move_base_msgs/MoveBaseActionGoal
  0.desc=A goal for `move_base` to pursue in the world. 
  1.name= move_base/cancel
  1.type= actionlib_msgs/GoalID
  1.desc= A request to cancel a specific goal.
}
```

##### Action Published Topics

```clearsilver
pub {
  no_header= True
  0.name= move_base/feedback
  0.type= move_base_msgs/MoveBaseActionFeedback
  0.desc= Feedback contains the current position of the base in the world.
  1.name= move_base/status
  1.type= actionlib_msgs/GoalStatusArray
  1.desc= Provides status information on the goals that are sent to the `move_base` action.
  2.name= move_base/result
  2.type= move_base_msgs/MoveBaseActionResult
  2.desc= Result is empty for the `move_base` action.
}
```

```clearsilver
pub {
  0.name= cmd_vel
  0.type=geometry_msgs/Twist 
  0.desc= A stream of velocity commands meant for execution by a mobile base. 
}
sub {
  0.name= move_base_simple/goal
  0.type= geometry_msgs/PoseStamped
  0.desc=  Provides a non-action interface to move_base for users that don't care about tracking the execution status of their goals.
}
srv{
  0.name= ~make_plan
  0.type= nav_msgs/GetPlan
  0.desc= Allows an external user to ask for a plan to a given pose from `move_base` without causing `move_base` to execute that plan.
  1.name= ~clear_unknown_space  
  1.type= std_srvs/Empty
  1.desc= Allows an external user to tell move_base to clear unknown space in the area directly around the robot. This is useful when move_base has its costmaps stopped for a long period of time and then started again in a new location in the environment. - '''Available in versions from 1.1.0-groovy'''
  2.name= ~clear_costmaps  
  2.type= std_srvs/Empty
  2.desc= Allows an external user to tell move_base to clear obstacles in the costmaps used by move_base. This could cause a robot to hit things and should be used with caution. - '''New in 1.3.1'''
}
param {
  0.name=~base_global_planner 
  0.default=`"navfn/NavfnROS"` '''For 1.1+ series'''
  0.type= string
  0.desc= The name of the plugin for the global planner to use with `move_base`, see [[pluginlib]] documentation for more details on plugins. This plugin must adhere to the `nav_core::BaseGlobalPlanner` interface specified in the [[nav_core]] package. ('''1.0 series default:''' `"NavfnROS"`)
  1.name= ~base_local_planner
  1.default=`"base_local_planner/TrajectoryPlannerROS"` '''For 1.1+ series'''
  1.type= string
  1.desc= The name of the plugin for the local planner to use with `move_base` see [[pluginlib]] documentation for more details on plugins. This plugin must adhere to the `nav_core::BaseLocalPlanner` interface specified in the [[nav_core]] package. ('''1.0 series default:''' `"TrajectoryPlannerROS"`)
  2.name= ~recovery_behaviors
  2.default = [{name: conservative_reset, type: clear_costmap_recovery/ClearCostmapRecovery}, {name: rotate_recovery, type: rotate_recovery/RotateRecovery}, {name: aggressive_reset, type: clear_costmap_recovery/ClearCostmapRecovery}] '''For 1.1+ series'''
  2.type = list
  2.desc = A list of recovery behavior plugins to use with `move_base`, see [[pluginlib]] documentation for more details on plugins. These behaviors will be run when `move_base` fails to find a valid plan in the order that they are specified. After each behavior completes, `move_base` will attempt to make a plan. If planning is successful, `move_base` will continue normal operation. Otherwise, the next recovery behavior in the list will be executed.  These plugins must adhere to the `nav_core::RecoveryBehavior` interface specified in the [[nav_core]] package. ('''1.0 series default:''' [{name: conservative_reset, type: !ClearCostmapRecovery}, {name: rotate_recovery, type: !RotateRecovery}, {name: aggressive_reset, type: !ClearCostmapRecovery}]). Note: For the default parameters, the aggressive_reset behavior will clear out to a distance of 4 * `~/local_costmap/circumscribed_radius`.
  3.name= ~controller_frequency
  3.default= 20.0
  3.type= double
  3.desc= The rate in Hz at which to run the control loop and send velocity commands to the base.
  4.name= ~planner_patience
  4.default= 5.0
  4.type= double
  4.desc=   How long the planner will wait in seconds in an attempt to find a valid plan before space-clearing operations are performed.
  5.name= ~controller_patience
  5.default= 15.0
  5.type= double
  5.desc= How long the controller will wait in seconds without receiving a valid control before space-clearing operations are performed.
  6.name= ~conservative_reset_dist
  6.default= 3.0
  6.type= double
  6.desc= The distance away from the robot in meters beyond which obstacles will be cleared from the [[costmap_2d | costmap]] when attempting to clear space in the map. Note, this parameter is only used when the default recovery behaviors are used for `move_base`.
  7.name= ~recovery_behavior_enabled
  7.default= `true`
  7.type= bool
  7.desc=  Whether or not to enable the `move_base` recovery behaviors to attempt to clear out space.
  8.name= ~clearing_rotation_allowed
  8.default= `true`
  8.type= bool
  8.desc= Determines whether or not the robot will attempt an in-place rotation when attempting to clear out space. Note: This parameter is only used when the default recovery behaviors are in use, meaning the user has not set the `recovery_behaviors` parameter to anything custom.
  9.name= ~shutdown_costmaps
  9.default= `false`
  9.type= bool
  9.desc= Determines whether or not to shutdown the costmaps of the node when `move_base` is in an inactive state
  10.name= ~oscillation_timeout
  10.default= 0.0
  10.type= double
  10.desc= How long in seconds to allow for oscillation before executing recovery behaviors. A value of 0.0 corresponds to an infinite timeout. '''New in navigation 1.3.1'''
  11.name= ~oscillation_distance
  11.default= 0.5
  11.type= double
  11.desc= How far in meters the robot must move to be considered not to be oscillating. Moving this far resets the timer counting up to the `~oscillation_timeout` '''New in navigation 1.3.1'''
  12.name= ~planner_frequency
  12.default= 0.0
  12.type= double
  12.desc= The rate in Hz at which to run the global planning loop. If the frequency is set to 0.0, the global planner will only run when a new goal is received or the local planner reports that its path is blocked. '''New in navigation 1.6.0'''
  13.name= ~max_planning_retries
  13.default= -1
  13.type= int32_t
  13.desc= How many times to allow for planning retries before executing recovery behaviors. A value of -1.0 corresponds to an infinite retries.
}
```

#### Component APIs

The \`move_base\` node contains components that have their own ROS APIs.
These components may vary based on the values of the
\`base_global_planner\`, \`base_local_planner\`, and
\`recovery_behaviors\` respectively. Links to the APIs for the default
components can be found below:

-   [costmap_2d](costmap_2d) - Documentation on the
    [costmap_2d](costmap_2d) package used in move_base
-   [nav_core](nav_core) - Documentation on the
    \`nav_core::BaseGlobalPlanner\` and \`nav_core::BaseLocalPlanner\`
    interfaces used by \`move_base\`.
-   [base_local_planner](base_local_planner) - Documentation on the
    [base_local_planner](base_local_planner) used in \`move_base\`
-   [navfn](navfn) - Documentation on the [navfn](navfn) global planner
    used in \`move_base\`
-   [clear_costmap_recovery](clear_costmap_recovery) - Documentation on
    the [clear_costmap_recovery](clear_costmap_recovery) recovery
    behavior used in \`move_base\`
-   [rotate_recovery](rotate_recovery) - Documentation on the
    [rotate_recovery](rotate_recovery) recovery behavior used in
    \`move_base\`

Class Diagram (partially & not strictly drawn) is available
[here](https://docs.google.com/drawings/d/1rKY4yxI0ibHqgQoLFZPuEayRp8Bs4FpRyaNKsMxqpX4/edit?usp=sharing).
