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



```clearsilver
param{
  0.name=joints
  0.type=string[]
  0.desc=The list of joints to control
  1.name=gains/<joint>/p
  1.type=double
  1.default=Required
  1.desc=The position gain for joint <joint>.  (There should be a `p` gain for every joint listed in the `joints` parameter)
  2.name=gains/<joint>/d
  2.type=double
  2.desc=The position derivative gain for joint <joint>
  2.default=0.0
  3.name=gains/<joint>/i
  3.type=double
  3.desc=The integral gain around position for joint <joint>
  3.default=0.0
  4.name=gains/<joint>/i_clamp
  4.type=double
  4.desc=The clamp of the integral gain for joint <joint>
  4.default=0.0
  5.name=gains/<joint>/mass
  5.type=double
  5.desc=The approximate inertia for joint <joint>
  5.default=0.0
  6.name=gains/<joint>/proxy/lambda
  6.type=double
  6.desc=Bandwidth of proxy reconvergence
  6.default=1.0
  7.name=gains/<joint>/proxy/acc_converge
  7.type=double
  7.desc=Acceleration of proxy reconvergence
  7.default=0.0
  8.name=gains/<joint>/proxy/vel_limit
  8.type=double
  8.desc=Velocity limit (enforced by the proxy)
  8.default=0.0
  9.name=gains/<joint>/proxy/effort_limit
  9.type=double
  9.desc=Acceleration limit (enforced by the proxy)
  9.default=0.0
  10.name=joint_trajectory_action_node/constraints/goal_time
  10.type=double
  10.desc=If the timestamp of the goal trajectory point is t, then following the trajectory succeeds if it reaches the goal within t +/- goal_time, and aborts otherwise.
  10.default=0.0
  11.name=joint_trajectory_action_node/constraints/<joint>/goal
  11.type=double
  11.desc=Position tolerance for a particular joint to reach the goal.  When the joint is within goal_position +/- goal_tolerance, than the trajectory can succeed.
  11.default=0.0
  12.name=joint_trajectory_action_node/constraints/<joint>/trajectory
  12.type=double
  12.desc=Position tolerance for a particular joint throughout the trajectory.  If the joint position every falls outside trajectory_position +/- tolerance, then the trajectory aborts.
  12.default=0.0
}
```



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



```clearsilver
param{
  0.name=joints
  0.type=string[]
  0.desc=The list of joints to control
  1.name=gains/<joint>/p
  1.type=double
  1.default=Required
  1.desc=The position gain for joint <joint>.  (There should be a `p` gain for every joint listed in the `joints` parameter)
  2.name=gains/<joint>/d
  2.type=double
  2.desc=The position derivative gain for joint <joint>
  2.default=0.0
  3.name=gains/<joint>/i
  3.type=double
  3.desc=The integral gain around position for joint <joint>
  3.default=0.0
  4.name=gains/<joint>/i_clamp
  4.type=double
  4.desc=The clamp of the integral gain for joint <joint>
  4.default=0.0
}
```



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





```clearsilver
pub{
  0.name=state
  0.type=pr2_controllers_msgs/JointTrajectoryControllerState
  0.desc=Current state of the controller, including the current and desired positions, velocities, and accelerations.
}
```





```clearsilver
sub{
  0.name=command
  0.type=trajectory_msgs/JointTrajectory
  0.desc=The trajectory to follow.  The absolute start time of the trajectory is given in header.stamp.  If positions, velocities, and accelerations are all specified, then the controller will interpolate using quintic splines.  If only positions and velocities are specified, it will use cubic splines.  If only positions are specified, it will interpolate linearly (though using this behavior is not recommended, as the trajectory will not be smooth).
}
```





```clearsilver
srv{
  0.name=query_state
  0.type=pr2_controllers_msgs/QueryTrajectoryState
  0.desc=The query_state service allows the user to inquire where the controller setpoint will be at a desired time.
}
```



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



```clearsilver
param {
  0.name=joint
  0.type=string
  0.default=Required
  0.desc=The joint to control
}
sub {
  0.name=command
  0.type=std_msgs/Float64
  0.desc=The effort to command
}
```



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



```clearsilver
param {
  0.name=joint
  0.type=string
  0.default=Required
  0.desc=The joint to control
  1.name=pid/p
  1.type=double
  1.default=Required
  1.desc=The proportional gain relating efforts to the error in velocity
  2.name=pid/d
  2.type=double
  2.default=0.0
  2.desc=Derivative gain
  3.name=pid/i
  3.type=double
  3.default=0.0
  3.desc=Integral gain
  4.name=pid/i_clamp
  4.type=double
  4.default=0.0
  4.desc=Bounds enforced on the integral windup
}
sub {
  0.name=command
  0.type=std_msgs/Float64
  0.desc=The velocity to command
}
```



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



```clearsilver
param {
  0.name=joint
  0.type=string
  0.default=Required
  0.desc=The joint to control
  1.name=pid/p
  1.type=double
  1.default=Required
  1.desc=The proportional gain relating efforts to the error in position
  2.name=pid/d
  2.type=double
  2.default=0.0
  2.desc=Derivative gain, relating efforts to velocity (derivative of position)
  3.name=pid/i
  3.type=double
  3.default=0.0
  3.desc=Integral gain
  4.name=pid/i_clamp
  4.type=double
  4.default=0.0
  4.desc=Bounds enforced on the integral windup
}
sub {
  0.name=command
  0.type=std_msgs/Float64
  0.desc=The position to command
}
```



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



```clearsilver
param{
  0.name=root_name
  0.type=string
  0.default=Required
  0.desc=The root link of the chain to control.
  1.name=tip_name
  1.type=string
  1.default=Required
  1.desc=The tip link (end effector) of the chain to control.
  2.name=cart_gain/trans/p
  2.type=double
  2.default=Required
  2.desc=Proportional gain for translation of the end effector.
  3.name=cart_gains/trans/d
  3.type=double
  3.default=Required
  3.desc=Derivative gain for translation of the end effector
  4.name=cart_gains/rot/p
  4.type=double
  4.default=Required
  4.desc=Proportional gain for rotation of the end effector
  5.name=cart_gains/rot/d
  5.type=double
  5.default=Required
  5.desc=Derivative gain for rotation of the end effector
  6.name=vel_saturation_trans
  6.type=double
  6.default=0.0
  6.desc=Velocity limit for translation (m/s).  Zero means not limited.
  7.name=vel_saturation_rot
  7.type=double
  7.default=0.0
  7.desc=Velocity limit for rotation (rad/s).  Zero means not limited.
  8.name=jacobian_inverse_damping
  8.type=double
  8.default=0.0
  8.desc=Damping term for taking the inverse of the Jacobian.
  9.name=joint_feedforward/<joint>
  9.type=double
  9.default=0.0
  9.desc=Feedforward term for the posture controller.
  10.name=saturation/<joint>
  10.type=double
  10.default=0.0
  10.desc=Maximum torque for the joint.
  11.name=k_posture
  11.type=double
  11.default=1.0
  11.desc=Gain on the posture control.
}
```



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





```clearsilver
pub{
  0.name=state
  0.type=robot_mechanism_controllers/JTCartesianControllerState
  0.desc=Current state of the controller
  1.name=state/x_desi
  1.type=geometry_msgs/PoseStamped
  1.desc=Current setpoint of the controller
}
```





```clearsilver
sub{
  0.name=command_pose
  0.type=geometry_msgs/PoseStamped
  0.desc=Tells the controller where to go.
  1.name=gains
  1.type=std_msgs/Float64MultiArray
  1.desc=New gains.  6 values replaces all the Kp terms (trans, trans, trans, rot, rot, rot).  12 Replaces the Kp and Kd terms.
  2.name=command_posture
  2.type=std_msgs/Float64MultiArray
  2.desc=New desired joint posture.  Should have the same size as the number of joints being controlled.
}
```

## CartesianWrenchController

### Cartesian Wrench Controller

#### Overview

The Cartesian Wrench Controller commands a desired wrench to a chain of
joints. The chain of joints is a set of joints that spans from some link
(the "root" link) to another link (the "tip" link). The wrenches are
applied at the origin of the tip link in the frame of the root link.

#### ROS API



```clearsilver
param {
  0.name=root_link
  0.type=string
  0.default=Required
  0.desc=The root link of the chain of joints
  1.name=tip_link
  1.type=string
  1.default=Required
  1.desc=The tip link of the chain of joints
}
sub {
  0.name=command
  0.type=geometry_msgs/Wrench
  0.desc=The wrench to command
}
```



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



```clearsilver
param {
  0.name=root_name
  0.type=string
  0.default=Required
  0.desc=The root link of the chain of joints
  1.name=tip_name
  1.type=string
  1.default=Required
  1.desc=The tip link of the chain of joints
  2.name=fb_trans/p
  2.type=double
  2.default=Required
  2.desc=Translational gain, relating force to velocity error
  3.name=fb_trans/d
  3.type=double
  3.default=0.0
  3.desc=Translational derivative gain
  4.name=fb_trans/i
  4.type=double
  4.default=0.0
  4.desc=Translational integral gain
  5.name=fb_trans/i_clamp
  5.type=double
  5.default=0.0
  5.desc=Bounds enforced on the translational integral windup
  6.name=fb_rot/p
  6.type=double
  6.default=Required
  6.desc=Rotational gain, relating end-effector torques to angular velocity error
  7.name=fb_rot/d
  7.type=double
  7.default=0.0
  7.desc=Rotational derivative gain
  8.name=fb_rot/i
  8.type=double
  8.default=0.0
  8.desc=Rotational integral gain
  9.name=fb_rot/i_clamp
  9.type=double
  9.default=0.0
  9.desc=Bounds enforced on the rotational integral windup

}
sub {
  0.name=command
  0.type=geometry_msgs/Twist
  0.desc=The twist to command
}
```



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



```clearsilver
param {
  0.name=root_name
  0.type=string
  0.default=Required
  0.desc=The root link of the chain of joints
  1.name=tip_name
  1.type=string
  1.default=Required
  1.desc=The tip link of the chain of joints
  2.name=fb_trans/p
  2.type=double
  2.default=Required
  2.desc=Translational gain, relating force to position error
  3.name=fb_trans/d
  3.type=double
  3.default=0.0
  3.desc=Translational derivative gain
  4.name=fb_trans/i
  4.type=double
  4.default=0.0
  4.desc=Translational integral gain
  5.name=fb_trans/i_clamp
  5.type=double
  5.default=0.0
  5.desc=Bounds enforced on the translational integral windup
  6.name=fb_rot/p
  6.type=double
  6.default=Required
  6.desc=Rotational gain, relating end-effector torques to orientation error
  7.name=fb_rot/d
  7.type=double
  7.default=0.0
  7.desc=Rotational derivative gain
  8.name=fb_rot/i
  8.type=double
  8.default=0.0
  8.desc=Rotational integral gain
  9.name=fb_rot/i_clamp
  9.type=double
  9.default=0.0
  9.desc=Bounds enforced on the rotational integral windup

}
sub {
  0.name=command
  0.type=geometry_msgs/Pose
  0.desc=The pose to command
}
```



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
