## Overview

Controller for executing joint-space trajectories on a group of joints.
Trajectories are specified as a set of waypoints to be reached at
specific time instants, which the controller attempts to execute as well
as the mechanism allows. Waypoints consist of positions, and optionally
velocities and accelerations.

### Trajectory representation

The controller is templated to work with multiple trajectory
representations. By default, a spline interpolator is provided, but
it\'s possible to support other representations. The spline interpolator
uses the following interpolation strategies depending on the waypoint
specification:

-   **Linear**: Only position is specified. Guarantees continuity at the
    position level. Discouraged because it yields trajectories with
    discontinuous velocities at the waypoints.

```{=html}
<!-- -->
```
-   **Cubic**: Position and velocity are specified. Guarantees
    continuity at the velocity level.

```{=html}
<!-- -->
```
-   **Quintic**: Position, velocity and acceleration are specified:
    Guarantees continuity at the acceleration level.

### Hardware interface type

The controller is templated to work with multiple hardware interface
types. Currently joints with **position**, **velocity** and **effort**
interfaces are supported. For position-controlled joints, desired
positions are simply forwarded to the joints; while for velocity
(effort) joints, the position+velocity trajectory following error is
mapped to velocity (effort) commands through a PID loop. Example
controller configurations can be found
[here](#Controller_configuration_examples).

Similarly to the trajectory representation case above, it\'s possible to
support new hardware interfaces, or alternative mappings to an already
supported interface (eg. a proxy controller for generating effort
commands).

### Other features

-   **Realtime-safe** implementation.
-   Proper handling of **wrapping** (continuous) joints.
-   **Robust to system clock changes:** Discontinuous system clock
    changes do not cause discontinuities in the execution of already
    queued trajectory segments.

## Sending trajectories

### Available interfaces

There are two mechanisms for sending trajectories to the controller: by
means of the **action interface** or the **topic interface**. Both use
the \<\<MsgLink(trajectory_msgs/JointTrajectory)\>\> message to specify
trajectories, and require specifying values for *all* the controller
joints (as opposed to only a subset) if allow_partial_joints_goal is not
set to True.

The primary way to send trajectories is through the **action
interface**, and should be favored when execution monitoring is desired.
Action goals allow to specify not only the trajectory to execute, but
also (optionally) path and goal tolerances. When no tolerances are
specified, the defaults given in the parameter server are used (see
[ROS API](#ROS_API) below). If tolerances are violated during trajectory
execution, the action goal is aborted and the client is notified.

**Important note** Even when a goal has been aborted, the controller
will still attempt to execute the trajectory as best as possible.

The **topic interface** is a fire-and-forget alternative. Use this
interface if you don\'t care about execution monitoring. The
controller\'s path and goal tolerance specification is *not* used in
this case, as there is no mechanism to notify the sender about tolerance
violations. Note that although some degree of monitoring is available
through the \`query_state\` service and \`state\` topic (see
[ROS API](#ROS_API) below), it is much more cumbersome to realize than
with the action interface.

### Preemption policy

Only one action goal can be active at any moment, or none if the topic
interface is used. Path and goal tolerances are checked *only* for the
trajectory segments of the active goal.

When an active action goal is preempted by another command coming from
either the action or the topic interface, the goal is canceled and the
client is notified.

Sending an **empty trajectory** message from the **topic interface**
(not the action interface) will stop the execution of all queued
trajectories and enter position hold mode. The
\`stop_trajectory_duration\` parameter controls the duration of the stop
motion.

### Trajectory replacement

Joint trajectory messages allow to specify the time at which a new
trajectory should start executing by means of the header timestamp,
where zero time (the default) means *\"start now\"*.

The arrival of a new trajectory command does *not necessarily* mean that
the controller will completely discard the currently running trajectory
and substitute it with the new one. Rather, the controller will take the
useful parts of both and combine them appropriately. Please refer to the
[ understanding trajectory replacement](/UnderstandingTrajectoryReplacement)
page for a detailed description of this behavior.

## ROS API

### Description

#### Action interface

The controller exposes a
[control_msgs::FollowJointTrajectoryAction](http://docs.ros.org/api/control_msgs/html/action/FollowJointTrajectory.html)
interface in the \`follow_joint_trajectory\` namespace of the
controller. See the action definition for more information on what to
send.

```clearsilver
pub {
  0.name=state
  0.type=control_msgs/JointTrajectoryControllerState
  0.desc= Current controller state.
}
sub {
  0.name= command
  0.type= trajectory_msgs/JointTrajectory
  0.desc= Trajectory to execute using the '''topic interface'''.
}
```

```clearsilver
srv{
  0.name= query_state
  0.type= control_msgs/QueryTrajectoryState
  0.desc= Query controller state at any future time.
}
``` ```clearsilver
param{
  0.name=joints
  0.type=string[]
  0.desc=The list of joints to control.
  1.name=constraints/goal_time
  1.type=double
  1.desc=If the timestamp of the goal trajectory point is t, then following the trajectory succeeds if it reaches the goal within t +/- goal_time, and aborts otherwise.
  1.default=0.0
  2.name=constraints/stopped_velocity_tolerance
  2.type=double
  2.desc=Velocity to be considered approximately equal to zero.
  2.default=0.01
  3.name=constraints/<joint>/goal
  3.type=double
  3.desc=Position tolerance for a particular joint to reach the goal.  When the joint is within goal_position +/- goal_tolerance, than the trajectory can succeed.
  3.default=0.0
  4.name=constraints/<joint>/trajectory
  4.type=double
  4.desc=Position tolerance for a particular joint throughout the trajectory. If the joint position ever falls outside trajectory_position +/- tolerance, then the trajectory aborts.
  4.default=0.0
  5.name=gains/<joint>
  5.type=associative array
  5.desc=Key value pairs specifying a PID controller. This is required by the effort and velocity interfaces. See examples [[#Controller_configuration_examples|here]].
  6.name=velocity_ff/<joint>
  6.type=double
  6.desc=Gain for a velocity feed-forward term added to the PID controller output. This is optional and is only used by the effort and velocity interfaces. See examples [[#Controller_configuration_examples|here]].
  6.default=0.0
  7.name=stop_trajectory_duration
  7.type=double
  7.desc=When starting the controller or canceling a trajectory, position hold mode is entered. This parameter specifies the time it takes to bring the current state (position and velocity) to a stop. Its value can be greater or equal than zero.
  7.default=0.0
  8.name=state_publish_rate
  8.type=double
  8.desc=Frequency (in Hz) at which the controller state is published.
  8.default=50
  9.name=action_monitor_rate
  9.type=double
  9.desc=Frequency (in Hz) at which the action goal status is monitored. This is an advanced parameter that should not require changing.
  9.default=20
  10.name=allow_partial_joints_goal
  10.type=bool
  10.desc=Enables sending JointTrajectory messages with a partial set of joints.
  10.default=False
}
```

### Controller configuration examples

#### Minimal description, position interface

```yaml
head_controller:
  type: "position_controllers/JointTrajectoryController"
  joints:
    - head_1_joint
    - head_2_joint
```

#### Minimal description, velocity interface

```yaml
head_controller:
  type: "velocity_controllers/JointTrajectoryController"
  joints:
    - head_1_joint
    - head_2_joint

  gains: # Required because we're controlling a velocity interface
    head_1_joint: {p: 100,  d: 1, i: 1, i_clamp: 1}
    head_2_joint: {p: 100,  d: 1, i: 1, i_clamp: 1}
```

#### Velocity FF, velocity interface

```yaml
head_controller:
  type: "velocity_controllers/JointTrajectoryController"
  joints:
    - head_1_joint
    - head_2_joint

  gains: # Required because we're controlling a velocity interface
    head_1_joint: {p: 10,  d: 1, i: 1, i_clamp: 1} # Smaller 'p' term, since ff term does most of the work
    head_2_joint: {p: 10,  d: 1, i: 1, i_clamp: 1} # Smaller 'p' term, since ff term does most of the work

  velocity_ff:
    head_1_joint: 1.0
    head_2_joint: 1.0
```

#### Minimal description, effort interface

```yaml
head_controller:
  type: "effort_controllers/JointTrajectoryController"
  joints:
    - head_1_joint
    - head_2_joint

  gains: # Required because we're controlling an effort interface
    head_1_joint: {p: 100,  d: 1, i: 1, i_clamp: 1}
    head_2_joint: {p: 100,  d: 1, i: 1, i_clamp: 1}
```

#### Complete description, effort interface

```yaml
head_controller:
  type: "effort_controllers/JointTrajectoryController"
  joints:
    - head_1_joint
    - head_2_joint

  constraints:
    goal_time: 0.5                   # Override default
    stopped_velocity_tolerance: 0.02 # Override default
    head_1_joint:
      trajectory: 0.05               # Not enforced if unspecified
      goal: 0.02                     # Not enforced if unspecified
    head_2_joint:
      goal: 0.01                     # Not enforced if unspecified

  gains: # Required because we're controlling an effort interface
    head_1_joint: {p: 100,  d: 1, i: 1, i_clamp: 1}
    head_2_joint: {p: 100,  d: 1, i: 1, i_clamp: 1}

  state_publish_rate:  25            # Override default
  action_monitor_rate: 30            # Override default
  stop_trajectory_duration: 0        # Override default
```
