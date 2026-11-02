## Overview

This package contains the code that runs in realtime to move the
mechanisms on the robot. These controllers are not specific to
mechanisms on the PR2 and may be useful on other robots.

- [Joint Trajectory Action Controller](#jointtrajectoryactioncontroller)
  for moving a set of joints along a joint space trajectory.
- [Joint Spline Trajectory Controller](#jointsplinetrajectorycontroller)
  for moving a set of joints along a joint space trajectory
  *(deprecated, use the Joint Trajectory Action Controller instead)*.
- [Joint Effort Controller](#jointeffortcontroller)
  for commanding an effort (force or torque) to a single joint.
- [Joint Velocity Controller](#jointvelocitycontroller)
  for commanding velocities to a single joint.
- [Joint Position Controller](#jointpositioncontroller)
  for commanding positions to a single joint.
- [JT Cartesian Controller](#jtcartesian-controller)
  for commanding poses (cartesian positions) to the end effector, with
  redundancy control.
- [Cartesian Wrench Controller](#cartesianwrenchcontroller)
  for commanding wrenches (cartesian forces and torques) to a chain of
  joints.
- [Cartesian Twist Controller](#cartesiantwistcontroller)
  for commanding twists (cartesian velocities) to a chain of joints.
- [Cartesian Pose Controller](#cartesianposecontroller)
  for commanding poses (cartesian positions) to a chain of joints.

## Stability

The controllers in this package should not be used directly. The
controllers should instead by used via their
[action](https://index.ros.org/p/actionlib) interfaces, e.g.,
[joint_trajectory_action](https://index.ros.org/p/joint_trajectory_action),
[pr2_gripper_action](https://index.ros.org/p/pr2_gripper_action),
[pr2_head_action](https://index.ros.org/p/pr2_head_action), and
[single_joint_position_action](https://index.ros.org/p/single_joint_position_action).

## JointTrajectoryActionController

### Joint Trajectory Action Controller

#### Overview

The Joint Trajectory Action Controller executes joint-space trajectories
on a set of joints. It takes, as a command, a message specifying the
desired position and velocity of each joint at every point in time, and
executes this command as well as the mechanism allows.

The Joint Trajectory Action Controller takes the trajectory points and
interpolates between them using splines. If you've specified
accelerations, it will use quintic splines, otherwise if you've
specified velocities, it will use cubic splines. (If you specify neither
accelerations nor velocities it will interpolate between the positions
linearly, however specifying only positions is discouraged, as the
linear interpolation will lead to discontinuities in the followed
trajectory).

#### ROS API

###### Parameters

- `joints` (`string[]`): The list of joints to control
- `gains/<joint>/p` (`double`, default: `Required`): The position gain
  for joint <joint>. (There should be a `p` gain for every joint
  listed in the `joints` parameter)
- `gains/<joint>/d` (`double`, default: `0.0`): The position derivative
  gain for joint <joint>
- `gains/<joint>/i` (`double`, default: `0.0`): The integral gain around
  position for joint <joint>
- `gains/<joint>/i_clamp` (`double`, default: `0.0`): The clamp of the
  integral gain for joint <joint>
- `gains/<joint>/mass` (`double`, default: `0.0`): The approximate
  inertia for joint <joint>
- `gains/<joint>/proxy/lambda` (`double`, default: `1.0`): Bandwidth of
  proxy reconvergence
- `gains/<joint>/proxy/acc_converge` (`double`, default: `0.0`):
  Acceleration of proxy reconvergence
- `gains/<joint>/proxy/vel_limit` (`double`, default: `0.0`): Velocity
  limit (enforced by the proxy)
- `gains/<joint>/proxy/effort_limit` (`double`, default: `0.0`):
  Acceleration limit (enforced by the proxy)
- `joint_trajectory_action_node/constraints/goal_time` (`double`,
  default: `0.0`): If the timestamp of the goal trajectory point is t,
  then following the trajectory succeeds if it reaches the goal within t
  +/- goal_time, and aborts otherwise.
- `joint_trajectory_action_node/constraints/<joint>/goal` (`double`,
  default: `0.0`): Position tolerance for a particular joint to reach
  the goal. When the joint is within goal_position +/- goal_tolerance,
  than the trajectory can succeed.
- `joint_trajectory_action_node/constraints/<joint>/trajectory`
  (`double`, default: `0.0`): Position tolerance for a particular joint
  throughout the trajectory. If the joint position every falls outside
  trajectory_position +/- tolerance, then the trajectory aborts.

Example configuration (from
[pr2_controller_configuration](https://index.ros.org/p/pr2_controller_configuration)/pr2_arm_controllers.yaml):



```yaml
r_arm_controller:
  type: "robot_mechanism_controllers/JointTrajectoryActionController"
  joints:
    - r_shoulder_pan_joint
    - r_shoulder_lift_joint
    - r_upper_arm_roll_joint
    - r_elbow_flex_joint
    - r_forearm_roll_joint
    - r_wrist_flex_joint
    - r_wrist_roll_joint
  gains:
    r_shoulder_pan_joint:
      p: 2400.0
      d: 18.0
      i: 800.0
      i_clamp: 4.0
      mass: 3.3
      proxy:
        lambda: 3.0
        acc_converge: 1.5
        vel_limit: 2.088
        effort_limit: 11.8
    r_shoulder_lift_joint:
      p: 1200.0
      d: 10.0
      i: 700.0
      i_clamp: 4.0
      mass: 2.0
      proxy:
        lambda: 3.0
        acc_converge: 1.5
        vel_limit: 2.082
        effort_limit: 8.0
    r_upper_arm_roll_joint: {p: 1000.0, d: 6.0, i: 600.0, i_clamp: 4.0}
    r_elbow_flex_joint: {p: 700.0, d: 4.0, i: 450, i_clamp: 4.0}
    r_forearm_roll_joint: {p: 300.0, d: 6.0, i: 300, i_clamp: 2.0}
    r_wrist_flex_joint: {p: 300.0, d: 4.0, i: 300, i_clamp: 2.0}
    r_wrist_roll_joint: {p: 300.0, d: 4.0, i: 300, i_clamp: 2.0}
  joint_trajectory_action_node:
    joints:
      - r_shoulder_pan_joint
      - r_shoulder_lift_joint
      - r_upper_arm_roll_joint
      - r_elbow_flex_joint
      - r_forearm_roll_joint
      - r_wrist_flex_joint
      - r_wrist_roll_joint
    constraints:
      goal_time: 0.6
      r_shoulder_pan_joint:
        goal: 0.02
      r_shoulder_lift_joint:
        goal: 0.02
      r_upper_arm_roll_joint:
        goal: 0.02
      r_elbow_flex_joint:
        goal: 0.02
      r_forearm_roll_joint:
        goal: 0.02
      r_wrist_flex_joint:
        goal: 0.02
      r_wrist_roll_joint:
        goal: 0.02
```



##### Sending trajectories

The primary way to send trajectories to the Joint Trajectory Action
Controller is by connecting to the
`control_msgs::FollowJointTrajectoryAction` on the
`follow_joint_trajectory` topic. The action goal specifies the
trajectory, and (optional) tolerances, which override the tolerances
given on the parameter server. See the action definition for more
information on what to send.

#### Advanced behaviors

##### Trajectory Replacement

![width=100%, height=30%](doc/trajectory_replacement.svg)

The controller provides an interface that allows you to interrupt only
part of the running trajectory.

When you send the controller a new
[trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)
message, it will splice the trajectory in at the time given in the
message header (t\*). At t\*, the controller will switch from the
previous trajectory to following the new trajectory. It is the user's
responsibility to ensure that the trajectories fit together by making
sure the positions and velocities are continuous at t\*. The
`query_state` service call helps by informing the user what the
positions and velocities of the current trajectory will be at a given
time.

##### Partial Execution

There are two ways of preventing trajectories from executing to the end.
Sending an empty trajectory will preempt the current trajectory,
however, this practice has a serious problem: if the node that sends the
"abort" message goes down, then the trajectory cannot be aborted.
Since the node sending the abort message is likely the node enforcing
the safety of the system, this means that the trajectory is being
executed without any safety constraints.

The solution is to send only the "cleared" parts of the trajectory to
the controller. The controllers will execute what it receives, but if
you stop sending it the rest of the trajectory, then it will stop the
mechanism. The commanding node sends small chunks of the trajectory,
possibly only 50ms into the future, after checking that these chunks are
"safe" to execute.

## JointSplineTrajectoryController

### Joint Spline Trajectory Controller

  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <#ff6666> **This controller is deprecated. Use the [Joint Trajectory Action Controller](#jointtrajectoryactioncontroller) instead**   
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

#### Overview

The Joint Spline Trajectory Controller executes joint-space trajectories
on a set of joints. It takes, as a command, a message specifying the
desired position and velocity of each joint at every point in time, and
executes this command as well as the mechanism allows.

The Joint Spline Trajectory Controller takes the trajectory points and
interpolates between them using splines. If you've specified
accelerations, it will use quintic splines, otherwise if you've
specified velocities, it will use cubic splines. (If you specify neither
accelerations nor velocities it will interpolate between the positions
linearly, however specifying only positions is discouraged, as the
linear interpolation will lead to discontinuities in the followed
trajectory).

#### ROS API

###### Parameters

- `joints` (`string[]`): The list of joints to control
- `gains/<joint>/p` (`double`, default: `Required`): The position gain
  for joint <joint>. (There should be a `p` gain for every joint
  listed in the `joints` parameter)
- `gains/<joint>/d` (`double`, default: `0.0`): The position derivative
  gain for joint <joint>
- `gains/<joint>/i` (`double`, default: `0.0`): The integral gain around
  position for joint <joint>
- `gains/<joint>/i_clamp` (`double`, default: `0.0`): The clamp of the
  integral gain for joint <joint>

Example configuration (from
[pr2_controller_configuration](https://index.ros.org/p/pr2_controller_configuration)/pr2_arm_controllers.yaml):



```yaml
r_arm_controller:
  type: JointSplineTrajectoryController
  joints:
    - r_shoulder_pan_joint
    - r_shoulder_lift_joint
    - r_upper_arm_roll_joint
    - r_elbow_flex_joint
    - r_forearm_roll_joint
    - r_wrist_flex_joint
    - r_wrist_roll_joint
  gains:
    r_shoulder_pan_joint: {p: 140.0, d: 30.0}
    r_shoulder_lift_joint: {p: 170.0, d: 30.0}
    r_upper_arm_roll_joint: {p: 300.0, d: 7.0}
    r_elbow_flex_joint: {p: 100.0, d: 5.0}
    r_forearm_roll_joint: {p: 300.0, d: 20.0}
    r_wrist_flex_joint: {p: 200.0, d: 8.0}
    r_wrist_roll_joint: {p: 200.0, d: 8.0}
```



###### Published Topics

- `state`
  ([pr2_controllers_msgs/msg/JointTrajectoryControllerState](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointTrajectoryControllerState.html)):
  Current state of the controller, including the current and desired
  positions, velocities, and accelerations.

###### Subscribed Topics

- `command`
  ([trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)):
  The trajectory to follow. The absolute start time of the trajectory is
  given in header.stamp. If positions, velocities, and accelerations are
  all specified, then the controller will interpolate using quintic
  splines. If only positions and velocities are specified, it will use
  cubic splines. If only positions are specified, it will interpolate
  linearly (though using this behavior is not recommended, as the
  trajectory will not be smooth).

###### Services

- `query_state`
  ([pr2_controllers_msgs/srv/QueryTrajectoryState](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/srv/QueryTrajectoryState.html)):
  The query_state service allows the user to inquire where the
  controller setpoint will be at a desired time.

#### Advanced behaviors

##### Trajectory Replacement

![width=100%, height=30%](doc/robot_mechanism_controllers_JointSplineTrajectoryController_trajectory_replacement.svg)

The controller provides an interface that allows you to interrupt only
part of the running trajectory.

When you send the controller a new
[trajectory_msgs/msg/JointTrajectory](https://docs.ros.org/en/rolling/p/trajectory_msgs/msg/JointTrajectory.html)
message, it will splice the trajectory in at the time given in the
message header (t\*). At t\*, the controller will switch from the
previous trajectory to following the new trajectory. It is the user's
responsiblity to ensure that the trajectories fit together by making
sure the positions and velocities are continuous at t\*. The
`query_state` service call helps by informing the user what the
positions and velocities of the current trajectory will be at a given
time.

##### Partial Excecution

There are two ways of preventing trajectories from executing to the end.
Sending an empty trajectory will preempt the current trajectory,
however, this practice has a serious problem: if the node that sends the
"abort" message goes down, then the trajectory cannot be aborted.
Since the node sending the abort message is likely the node enforcing
the safety of the system, this means that the trajectory is being
executed without any safety constraints.

The solution is to send only the "cleared" parts of the trajectory to
the controller. The controllers will execute what it receives, but if
you stop sending it the rest of the trajectory, then it will stop the
mechanism. The commanding node sends small chunks of the trajectory,
possibly only 50ms into the future, after checking that these chunks are
"safe" to execute.

## JointEffortController

### Joint Effort Controller

#### Overview

The Joint Effort Controller commands a desired effort (force/torque) to
the joint.

#### ROS API

###### Subscribed Topics

- `command`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  The effort to command

###### Parameters

- `joint` (`string`, default: `Required`): The joint to control

Example configuration:



```yaml
elbow_flex_effort_controller:
  type: JointEffortController
  joint: r_elbow_flex_joint
```

## JointVelocityController

### Joint Velocity Controller

#### Overview

The Joint Velocity Controller commands a desired velocity to the joint.
The velocity is controlled using PID control to specify the effort to
the joint. When started, the controller will command a velocity of zero.

The commands from the velocity controller will be subject to the
[safety limits](https://index.ros.org/p/pr2_controller_manager) of the
robot, so the velocity will not be achieved near the joint limits.

#### ROS API

###### Subscribed Topics

- `command`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  The velocity to command

###### Parameters

- `joint` (`string`, default: `Required`): The joint to control
- `pid/p` (`double`, default: `Required`): The proportional gain
  relating efforts to the error in velocity
- `pid/d` (`double`, default: `0.0`): Derivative gain
- `pid/i` (`double`, default: `0.0`): Integral gain
- `pid/i_clamp` (`double`, default: `0.0`): Bounds enforced on the
  integral windup

Example configuration:



```yaml
elbow_flex_velocity_controller:
  type: JointVelocityController
  joint: r_elbow_flex_joint
  pid:
    p: 5.0
    i: 20.0
    i_clamp: 100.0
```

## JointPositionController

### Joint Position Controller

#### Overview

The Joint Position Controller commands a desired position to the joint.
The position is controlled using PID control to specify the effort to
the joint. When started, the controller will command to the current
position.

The commands from the position controller will be constrained by the
[safety limits](https://index.ros.org/p/pr2_controller_manager) of the
robot, so position commands near the joint limits may not be achieved.

#### ROS API

###### Subscribed Topics

- `command`
  ([std_msgs/msg/Float64](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64.html)):
  The position to command

###### Parameters

- `joint` (`string`, default: `Required`): The joint to control
- `pid/p` (`double`, default: `Required`): The proportional gain
  relating efforts to the error in position
- `pid/d` (`double`, default: `0.0`): Derivative gain, relating efforts
  to velocity (derivative of position)
- `pid/i` (`double`, default: `0.0`): Integral gain
- `pid/i_clamp` (`double`, default: `0.0`): Bounds enforced on the
  integral windup

Example configuration:



```yaml
elbow_flex_position_controller:
  type: JointPositionController
  joint: r_elbow_flex_joint
  pid:
    p: 100.0
    d: 10.0
```

## JTCartesian Controller

### JT Cartesian Controller

#### Overview

The JT Cartesian Controller controls the pose of the end effector using
a Jacobian-transpose based controller, with redundancy control.

It's loosely based off the acceleration control scheme in
[Nakanishi, Comparative Experiements on Task Space Control](http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.79.5914),
with a diagonal approximation of the mass matrix, and the Jacobian
derivatives set to zero. These simplifications have worked well in
practice when controlling the PR2.

#### ROS API

###### Parameters

- `root_name` (`string`, default: `Required`): The root link of the
  chain to control.
- `tip_name` (`string`, default: `Required`): The tip link (end
  effector) of the chain to control.
- `cart_gain/trans/p` (`double`, default: `Required`): Proportional gain
  for translation of the end effector.
- `cart_gains/trans/d` (`double`, default: `Required`): Derivative gain
  for translation of the end effector
- `cart_gains/rot/p` (`double`, default: `Required`): Proportional gain
  for rotation of the end effector
- `cart_gains/rot/d` (`double`, default: `Required`): Derivative gain
  for rotation of the end effector
- `vel_saturation_trans` (`double`, default: `0.0`): Velocity limit for
  translation (m/s). Zero means not limited.
- `vel_saturation_rot` (`double`, default: `0.0`): Velocity limit for
  rotation (rad/s). Zero means not limited.
- `jacobian_inverse_damping` (`double`, default: `0.0`): Damping term
  for taking the inverse of the Jacobian.
- `joint_feedforward/<joint>` (`double`, default: `0.0`): Feedforward
  term for the posture controller.
- `saturation/<joint>` (`double`, default: `0.0`): Maximum torque for
  the joint.
- `k_posture` (`double`, default: `1.0`): Gain on the posture control.

Example configuration (from
[pr2_controller_configuration](https://index.ros.org/p/pr2_controller_configuration)/pr2_jt_controllers.yaml):



```yaml
r_cart:
  type: robot_mechanism_controllers/JTCartesianController
  root_name: torso_lift_link
  tip_name: r_gripper_tool_frame
  k_posture: 25.0
  jacobian_inverse_damping: 0.01
  pose_command_filter: 0.01
  cart_gains:
    trans:
      p: 800.0
      d: 15.0
    rot:
      p: 80.0
      d: 1.2
  joint_feedforward:
    r_shoulder_pan_joint: 3.33
    r_shoulder_lift_joint: 1.16
    r_upper_arm_roll_joint: 0.1
    r_elbow_flex_joint: 0.25
    r_forearm_roll_joint: 0.133
    r_wrist_flex_joint: 0.0727
    r_wrist_roll_joint: 0.0727
  joint_max_effort:
    r_shoulder_pan_joint: 11.88
    r_shoulder_lift_joint: 11.64
    r_upper_arm_roll_joint: 6.143
    r_elbow_flex_joint: 6.804
    r_forearm_roll_joint: 8.376
    r_wrist_flex_joint: 5.568
    r_wrist_roll_joint: 5.568

  vel_saturation_trans: 2.0
  vel_saturation_rot: 4.0
```



###### Published Topics

- `state`
  ([robot_mechanism_controllers/msg/JTCartesianControllerState](https://docs.ros.org/en/rolling/p/robot_mechanism_controllers/msg/JTCartesianControllerState.html)):
  Current state of the controller
- `state/x_desi`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Current setpoint of the controller

###### Subscribed Topics

- `command_pose`
  ([geometry_msgs/msg/PoseStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/PoseStamped.html)):
  Tells the controller where to go.
- `gains`
  ([std_msgs/msg/Float64MultiArray](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64MultiArray.html)):
  New gains. 6 values replaces all the Kp terms (trans, trans, trans,
  rot, rot, rot). 12 Replaces the Kp and Kd terms.
- `command_posture`
  ([std_msgs/msg/Float64MultiArray](https://docs.ros.org/en/rolling/p/std_msgs/msg/Float64MultiArray.html)):
  New desired joint posture. Should have the same size as the number of
  joints being controlled.

## CartesianWrenchController

### Cartesian Wrench Controller

#### Overview

The Cartesian Wrench Controller commands a desired wrench to a chain of
joints. The chain of joints is a set of joints that spans from some link
(the "root" link) to another link (the "tip" link). The wrenches are
applied at the origin of the tip link in the frame of the root link.

#### ROS API

###### Subscribed Topics

- `command`
  ([geometry_msgs/msg/Wrench](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Wrench.html)):
  The wrench to command

###### Parameters

- `root_link` (`string`, default: `Required`): The root link of the
  chain of joints
- `tip_link` (`string`, default: `Required`): The tip link of the chain
  of joints

Example configuration:



```yaml
r_arm_cartesian_wrench_controller:
  type: CartesianWrenchController
  root_name: torso_lift_link
  tip_name: r_wrist_roll_link
```

## CartesianTwistController

### Cartesian Twist Controller

#### Overview

The Cartesian Twist Controller commands a desired twist to a chain of
joints. The chain of joints is a set of joints that spans from some link
(the "root" link) to another link (the "tip" link). The twists are
applied at the origin of the tip link in the frame of the root link, and
are controlled by PID controllers. Translational and rotational gains
are set separately.

#### ROS API

###### Subscribed Topics

- `command`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  The twist to command

###### Parameters

- `root_name` (`string`, default: `Required`): The root link of the
  chain of joints
- `tip_name` (`string`, default: `Required`): The tip link of the chain
  of joints
- `fb_trans/p` (`double`, default: `Required`): Translational gain,
  relating force to velocity error
- `fb_trans/d` (`double`, default: `0.0`): Translational derivative gain
- `fb_trans/i` (`double`, default: `0.0`): Translational integral gain
- `fb_trans/i_clamp` (`double`, default: `0.0`): Bounds enforced on the
  translational integral windup
- `fb_rot/p` (`double`, default: `Required`): Rotational gain, relating
  end-effector torques to angular velocity error
- `fb_rot/d` (`double`, default: `0.0`): Rotational derivative gain
- `fb_rot/i` (`double`, default: `0.0`): Rotational integral gain
- `fb_rot/i_clamp` (`double`, default: `0.0`): Bounds enforced on the
  rotational integral windup

#### Example configuration



```yaml
r_arm_cartesian_twist_controller:
  type: CartesianTwistController
  root_name: torso_lift_link
  tip_name: r_wrist_roll_link
  fb_trans:
    p: 20.0
    i: 0.5
    d: 0.0
    i_clamp: 1.0
  fb_rot:
    p: 0.5
    i: 0.1
    d: 0.0
    i_clamp: 0.2
```

## CartesianPoseController

### Cartesian Pose Controller

#### Overview

The Cartesian Pose Controller commands a desired pose to a chain of
joints. The chain of joints is a set of joints that spans from some link
(the "root" link) to another link (the "tip" link). The poses are
applied at the origin of the tip link in the frame of the root link, and
are controlled by PID controllers. Translational and rotational gains
are set separately.

#### ROS API

###### Subscribed Topics

- `command`
  ([geometry_msgs/msg/Pose](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Pose.html)):
  The pose to command

###### Parameters

- `root_name` (`string`, default: `Required`): The root link of the
  chain of joints
- `tip_name` (`string`, default: `Required`): The tip link of the chain
  of joints
- `fb_trans/p` (`double`, default: `Required`): Translational gain,
  relating force to position error
- `fb_trans/d` (`double`, default: `0.0`): Translational derivative gain
- `fb_trans/i` (`double`, default: `0.0`): Translational integral gain
- `fb_trans/i_clamp` (`double`, default: `0.0`): Bounds enforced on the
  translational integral windup
- `fb_rot/p` (`double`, default: `Required`): Rotational gain, relating
  end-effector torques to orientation error
- `fb_rot/d` (`double`, default: `0.0`): Rotational derivative gain
- `fb_rot/i` (`double`, default: `0.0`): Rotational integral gain
- `fb_rot/i_clamp` (`double`, default: `0.0`): Bounds enforced on the
  rotational integral windup

#### Example configuration



```yaml
r_arm_cartesian_pose_controller:
  type: CartesianPoseController
  root_name: torso_lift_link
  tip_name: r_wrist_roll_link
  fb_trans:
    p: 20.0
    i: 0.5
    d: 0.0
    i_clamp: 1.0
  fb_rot:
    p: 0.5
    i: 0.1
    d: 0.0
    i_clamp: 0.2
```
