## Overview

The \`move_slow_and_clear::MoveSlowAndClear\` is a simple recovery
behavior that clears information in the [ costmap](costmap_2d ) and then
limits the speed of the robot. Note, this recovery behavior is not truly
safe, the robot may hit things, it\'ll just happen at a user-specified
speed. Also, this recovery behavior is only compatible with local
planners that allow maximum speeds to be set via
[dynamic_reconfigure](dynamic_reconfigure) such as the
[dwa_local_planner](dwa_local_planner).

## MoveSlowAndClear

The \`move_slow_and_clear::MoveSlowAndClear\` object exposes its
functionality as a [ C++ ROS Wrapper](navigation/ROS_Wrappers ). It
operates within a ROS namespace (assumed to be **name** from here on)
specified on initialization. It adheres to the
\`nav_core::RecoveryBehavior\` interface found in the
[nav_core](nav_core) package.

### API Stability

-   The C++ API is stable.
-   The ROS API is stable.

### ROS Parameters

```clearsilver
param {
  no_header=True
  0.name = ~<name>/clearing_distance
  0.default = 0.5
  0.type = double 
  0.desc = The radius away from the robot in meters inside of which obstacles will be cleared.
  1.name = ~<name>/limited_trans_speed
  1.default = 0.25
  1.type = double 
  1.desc = The translational speed in meters/second the robot will be limited to while executing this recovery behavior.
  2.name = ~<name>/limited_rot_speed
  2.default = 0.25
  2.type = double 
  2.desc = The rotational speed in radians/second the robot will be limited to while executing this recovery behavior.
  3.name = ~<name>/limited_distance
  3.default = 0.3
  3.type = double 
  3.desc = The distance in meters the robot must move before the speed restrictions are lifted.
  4.name = ~<name>/planner_namespace
  4.default = "DWAPlannerROS"
  4.type = string
  4.desc = The name of the planner to reconfigure parameters on. Specifically the `max_trans_vel` and `max_rot_vel` parameters will be reconfigured within this namespace.
}
```

### C++ API

The C++ \`move_slow_and_clear::MoveSlowAndClear\` class adheres to the
\`nav_core::RecoveryBehavior\` interface found in the
[nav_core](nav_core) package. For detailed documentation, please see
[ MoveSlowAndClear Documentation](http://www.ros.org/doc/api/move_slow_and_clear/html/ ).

## Implementation

To use move_slow_and_clear, add the following lines in your move base
yaml file:

\`recovery_behaviors:\`

\` - name: \'move_slow_and_clear\'\`

\` type: \'move_slow_and_clear/MoveSlowAndClear\'\`
