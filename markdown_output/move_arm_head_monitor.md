NOTE: This package is unreleased at this point, the documentation is for
Willow Garage internal use only.

## Overview

This package contains the \`move_arm_head_monitor\` node, which is
designed primarily for use by [move_arm](move_arm), enabling the
monitoring of a given arm during its motion. During the monitoring, the
head is continuously pointed at locations in space where the arm will be
in the future, allowing the detection of obstacles if a head-mounted
sensor is set up to provide data to the [collision map](collision_map).
On the PR2, this sensor is typically the stereo vision.

[Youtube](https://www.youtube.com/watch?v=l6u06j_VsXc)

### Note on Usage

Normally, you will not interact with \`move_arm_head_monitor\` directly.
It, along with \`move_arm\`, should be launched with the appropriate
remappings and parameters, and that\'s it (see Example Usage below). The
API details below are given as a reference.

### Node Instances

One instance of \`move_arm_head_monitor\` allows the monitoring of one
arm. The names required for the node to connect to the appropriate
services need to be remapped properly based on which arm is to be
monitored.

## ROS API

The \`move_arm_head_monitor\` node connects to ROS services for querying
arm state and calculating forward kinematics, and to the point head
action server. It provides two action servers, one to look at a target
location on a given link, and one to monitor a given link.

### ROS Parameters

The \`move_arm_head_monitor\` node does not take any parameters, as all
required information is passed in through the action goal at the start
of monitoring. It might be desirable to change this in the future.

### Required Services

The \`move_arm_head_monitor\` node requires two external services and
one action server. In a launch file, the names below should be remapped
to the appropriate service or action server, such as the ones
recommended.

```clearsilver
pub {
  no_header= True
  0.name= head_controller_actionserver
  0.type= pr2_controllers_msgs/PointHeadAction
  0.desc= The point head action server. On the PR2, typically /head_traj_controller/point_head_action
  1.name= trajectory_query_service
  1.type= pr2_controllers_msgs/QueryTrajectoryState
  1.desc= The trajectory query service for the arm this node is monitoring, used to get the joint positions in the future. On the PR2, typically /x_arm_controller/query_state
  2.name= forward_kinematics_service
  2.type= kinematics_msgs/GetPositionFK
  2.desc= The forward kinematics service for the arm this node is monitoring, used to calculate the coordinates of the monitored point in the future. On the PR2, typically /pr2_xxxx_arm_kinematics/get_fk
}
```

### Action API

Two action servers are provided. The first action can be used to look at
a target location on a given link at a certain time, without starting to
monitor. This is useful when we want to make sure the head is pointed at
the arm before motion starts (NOTE: this action could be removed and a
monitoring goal with a short time used instead). The second action
invokes the full monitoring capability. The URL links below don\'t seem
to work, for details on the structure of the goal messages please see
the action definitions in the move_arm_head_monitor package.

#### Action Subscribed Topics

```clearsilver
sub {
  no_header= True
  0.name= move_arm_head_monitor/look_action/goal
  0.type= move_arm_head_monitor/HeadLookGoal
  0.desc= A goal for `move_arm_head_monitor` which defines target link, target (x,y,z) location, etc.
  1.name= move_arm_head_monitor/monitor_action/goal
  1.type= move_arm_head_monitor/HeadMonitorGoal
  1.desc= A goal for `move_arm_head_monitor` which defines all relevant monitoring parameters, such as target link, target (x,y,z) location, monitoring frequency, etc. 

}
```

### Published Topics

```clearsilver
sub{
  no_header = True
  group.0{
    name = Visualization topics
    0.name = point_head_target_marker
    0.type = visualization_msgs/Marker
    0.desc = The monitored points where the head is pointed.
    }
}
```

## Example Usage

To use this node, it must be launched with the correct remappings, and
then \`move_arm\` needs to be launched also with the appropriate
remappings as well as the desired monitoring parameters. Below is an
example launch file that can be used to launch the
\`move_arm_head_monitor\` node for the right arm. The file
head_monitor_right_arm.launch in pr2_arm_navigation_actions (trunk)
contains this code.

### Launch Files

```
<launch>
  <node pkg="move_arm_head_monitor" type="move_arm_head_monitor" respawn="true" name="head_monitor_right_arm" output="screen">

    <remap from="head_controller_actionserver" to="head_traj_controller/point_head_action" />
    <remap from="trajectory_query_service" to="r_arm_controller/query_state" />
    <remap from="forward_kinematics_service" to="pr2_right_arm_kinematics/get_fk" />
  </node>
</launch>
```

Below is an example of how the above launch file can be used to launch
the \`move_arm\` node properly. Note the remaps for
**head_monitor_action** and **head_look_action** and the various params
with with the prefix **head_monitor\_**

```
<launch>
  <include file="$(find pr2_arm_navigation_actions)/launch/head_monitor_right_arm.launch"/>

  <node pkg="move_arm" type="move_arm_simple_action" output="screen" name="move_right_arm">

    <remap from="robot_description" to="robot_description" />
    <remap from="joint_state" to="joint_states" />
    <remap from="arm_ik" to="pr2_right_arm_kinematics/get_constraint_aware_ik" />
    <remap from="arm_fk" to="pr2_right_arm_kinematics/get_fk" />
    <remap from="filter_trajectory" to="chomp_planner_longrange/filter_trajectory_with_constraints" />

    <remap from="get_trajectory_validity" to="environment_server/get_trajectory_validity" />
    <remap from="get_environment_safety" to="environment_server/get_environment_safety" />
    <remap from="get_execution_safety" to="environment_server/get_execution_safety" />
    <remap from="get_joints_in_group" to="environment_server/get_joints_in_group" />
    <remap from="get_robot_state" to="environment_server/get_robot_state" />
    <remap from="get_state_validity" to="environment_server/get_state_validity" />

    <remap from="head_monitor_action" to="head_monitor_right_arm/monitor_action" />
    <remap from="head_look_action" to="head_monitor_right_arm/look_action" />

    <param name="group" type="string" value="right_arm" />
    <param name="ik_allowed_time" type="double" value="2.0" />
    <param name="trajectory_filter_allowed_time" type="double" value="2.0" />
    <param name="group" type="string" value="right_arm" />
    <param name="controller_action_name" type="string" value="/r_arm_controller/joint_trajectory_action" />

    <param name="head_monitor_link" type="string" value="r_forearm_roll_link" />
    <param name="head_monitor_link_x" type="double" value="0.10" />
    <param name="head_monitor_time_offset" type="double" value="3.0" />
    <param name="head_monitor_max_frequency" type="double" value="3.0" />

    <param name="pause_allowed_time" type="double" value="30000.0" />

  </node>
</launch>
```

### move_arm params

The following params can be given to \`move_arm\` to control the
monitoring process:

```clearsilver
param {
  1.name= ~head_monitor_link
  1.default= ""
  1.type= string
  1.desc= The link to monitor. If empty string, no monitoring will be performed.
  2.name= ~head_monitor_link_x
  2.default= 0.0
  2.type= double
  2.desc= The x offset of the point to monitor in the coordinate frame of the link to monitor.
  3.name= ~head_monitor_link_y
  3.default= 0.0
  3.type= double
  3.desc= The y offset of the point to monitor in the coordinate frame of the link to monitor.
  4.name= ~head_monitor_link_z
  4.default= 0.0
  4.type= double
  4.desc= The z offset of the point to monitor in the coordinate frame of the link to monitor.
  5.name= ~head_monitor_max_frequency
  5.default= 2.0
  5.type= double
  5.desc= The frequency in Hz that the `move_arm_head_monitor` node tries to maintain for updating the head look position. As the system load increases, the maximum frequency that can be maintained decreases.
  6.name= ~head_monitor_time_offset
  6.default= 1.0
  6.type= double
  6.desc= The number of seconds to look into the future for determining where to point the head.
}
```
