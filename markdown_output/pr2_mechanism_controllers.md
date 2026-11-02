## Controllers

- [LaserTrajController](#laserscannertrajcontroller)
- [Pr2BaseController](#pr2basecontroller)
- [Pr2Odometry](#pr2odometry)
- [Pr2GripperController](#pr2grippercontroller)

## Stability

At the present time, the controllers in this stack are not intended for
direct use. The controllers should be used via their
[action](https://index.ros.org/p/actionlib) interfaces, e.g.,
[joint_trajectory_action](https://index.ros.org/p/joint_trajectory_action),
[pr2_gripper_action](https://index.ros.org/p/pr2_gripper_action),
[pr2_head_action](https://index.ros.org/p/pr2_head_action), and
[single_joint_position_action](https://index.ros.org/p/single_joint_position_action).
The [control_toolbox](https://index.ros.org/p/control_toolbox) library
is stable.

## LaserScannerTrajController

### Laser Scanner Trajectory Controller

#### Introduction

This controller allows you to send periodic/repeating command to the
tilting laser on the PR2

#### ROS API

###### Parameters

- `joint` (`string`, default: `Required`): The joint to control
- `gains/p` (`double`, default: `Required`): The position gain
- `gains/d` (`double`, default: `0.0`): The position derivative gain
- `gains/i` (`double`, default: `0.0`): The integral gain around
  position
- `gains/i_clamp` (`double`, default: `0.0`): The clamp of the integral
  gain
- `velocity_filter` (`Filter Chain`, default: `Required`): namespace
  defining a filter chain acting on the measured velocity. Refer to
  [Filter Chain](https://index.ros.org/p/filters) for more details
- `max_velocity` (`double`, default: `Required`): Maximum allowed
  velocity/rate for a trajectory that this controller generates (in
  rad/sec)
- `max_acceleration` (`double`, default: `Required`): Maximum allowed
  acceleration for a trajectory that this controller generates (in
  rad/sec\^2)

**Example Configuration:** 

```
laser_tilt_controller:
  type: LaserScannerTrajController
  joint: laser_tilt_mount_joint
  gains:
    p: 8.0
    i: 0.1
    d: 0.2
    i_clamp: 0.5
  velocity_filter:
    - name: low_pass
      type: TransferFunctionFilterDouble
      params:
        a: [1.0, -0.1]
        b: [0.9]
  max_velocity:    100
  max_acceleration: 30
```



###### Published Topics

- `<name>/laser_scanner_signal`
  ([pr2_msgs/msg/LaserScannerSignal](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/LaserScannerSignal.html)):
  The index of the last completed trajectory segment. Useful for
  aggregating laser scans

###### Subscribed Topics

- `<name>/set_periodic_cmd`
  ([pr2_msgs/msg/PeriodicCmd](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/PeriodicCmd.html)):
  Sets the periodic trajectory using periodic parameters like period,
  amplitude, and offset
- `<name>/set_traj_cmd`
  ([pr2_msgs/msg/LaserTrajCmd](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/LaserTrajCmd.html)):
  Sets the periodic trajectory by explicitly setting trajectory
  waypoints

###### Services

- `<name>/set_periodic_cmd`
  ([pr2_msgs/srv/SetPeriodicCmd](https://docs.ros.org/en/rolling/p/pr2_msgs/srv/SetPeriodicCmd.html)):
  Sets the periodic trajectory using periodic parameters (period,
  amplitude, and offset)
- `<name>/set_traj_cmd`
  ([pr2_msgs/srv/SetLaserTrajCmd](https://docs.ros.org/en/rolling/p/pr2_msgs/srv/SetLaserTrajCmd.html)):
  Sets the periodic trajectory by explicitly setting trajectory
  waypoints (position & time pairs)

#### Usage example



```
rosservice call laser_tilt_controller/set_periodic_cmd '{ command: { header: { stamp: 0 }, profile: "linear" , period: 3 , amplitude: 1 , offset: 0 }}'
```

## Pr2BaseController

### Base Velocity Controller

#### Introduction

This controller allows you to send velocity commands to the base.

**Status:** REVIEWED, NOT STABLE .

#### ROS API

###### Parameters

- `max_translational_velocity` (`double`, default: `1.0`): Maximum
  allowed translational velocity
- `max_rotational_velocity` (`double`, default: `2.0`): Maximum allowed
  rotational velocity
- `max_translational_acceleration/x` (`double`, default: `2.0`): Maximum
  allowed acceleration in X direction
- `max_translation_acceleration/y` (`double`, default: `2.0`): Maximum
  allowed acceleration in X direction
- `max_rotational_acceleration` (`double`, default: `2.0`): Maximum
  allowed yaw acceleration
- `kp_caster_steer` (`double`, default: `80.0`): The proportional gain
  on the caster steer velocity controller, vel_desired = kp_caster_steer
  \* caster_steer_error
- `timeout` (`double`, default: `0.3`): If time from last command heard
  > timeout, the controller will stop the robot.
- `state_publish_rate` (`double`, default: `1.0`): rate of state
  publishing events
- `caster_names` (`string`, default: `""`): The string names for all the
  caster link names on the robot separated by a space delimiter
- `wheel_radius_multiplier` (`double`, default: `1.0`): A correction
  multiplier for the radius of the wheels on the robot
- `caster_calibration_multiplier` (`double`, default: `1.0`): A
  correction multiplier for the reduction ratio for the caster rotation
  joint

**Example Configuration:** 

```
pr2_base_controller:
  caster_names: fr_caster_rotation_link fl_caster_rotation_link bl_caster_rotation_link br_caster_rotation_link

  type: Pr2BaseController

  caster_pid_gains: &caster_pid_gains
    p: 3.0
    d: 0.0
    i: 0.1
    i_clamp: 4.0
  wheel_pid_gains: &wheel_pid_gains
    p: 3.0
    d: 0.0
    i: 0.01
    i_clamp: 0.4

  fl_caster_l_wheel_joint:
   *wheel_pid_gains
  fl_caster_r_wheel_joint:
   *wheel_pid_gains
  fr_caster_l_wheel_joint:
   *wheel_pid_gains
  fr_caster_r_wheel_joint:
   *wheel_pid_gains
  bl_caster_l_wheel_joint:
   *wheel_pid_gains
  bl_caster_r_wheel_joint:
   *wheel_pid_gains
  br_caster_l_wheel_joint:
   *wheel_pid_gains
  br_caster_r_wheel_joint:
   *wheel_pid_gains

  fr_caster_rotation_joint:
   *caster_pid_gains
  fl_caster_rotation_joint:
   *caster_pid_gains
  bl_caster_rotation_joint:
   *caster_pid_gains
  br_caster_rotation_joint:
   *caster_pid_gains

  kp_caster_steer: 80.0
  timeout: 0.2
  max_translational_acceleration: 
   x: 2.0
   y: 2.0 
  max_rotational_acceleration: 2.0
  state_publish_rate: 0.25

  max_translational_velocity: 1.0 
  max_rotational_velocity: 2.0
```



###### Published Topics

- `<name>/state`
  ([pr2_mechanism_controllers/msg/BaseControllerState](https://docs.ros.org/en/rolling/p/pr2_mechanism_controllers/msg/BaseControllerState.html)):
  The state of the base controller

###### Subscribed Topics

- `<name>/command`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Input velocity command for the base (the reference point for this
  command is the origin of the base link which is in the middle of the
  base)

## Pr2Odometry

### PR2 Base Odometry

#### Introduction

This component computes odometry for the base.

**Status:** REVIEWED, NOT STABLE. .

#### ROS API

###### Parameters

- `odometer/initial_distance` (`double`, default: `0.0`): Initial value
  for the distance traveled by the robot (in m)
- `odometer/initial_angle` (`double`, default: `0.0`): Initial value for
  the total angular distance traveled by the robot (in radians)
- `odom/initial_x` (`double`, default: `0.0`): Initial X position of the
  robot in an odometric frame
- `odom/initial_y` (`double`, default: `0.0`): Initial Y position of the
  robot in an odometric frame
- `odom/initial_yaw` (`double`, default: `0.0`): Initial yaw position of
  the robot in an odometric frame
- `ils_max_iterations` (`int`, default: `3`): max number of iterations
  for iterative least squares
- `odom_frame` (`string`, default: `odom`): The odometric frame id
- `base_footprint_frame` (`string`, default: `base_footprint`): The id
  for a frame that is below the base link and coincident with the ground
- `base_link_frame` (`string`, default: `base_link`): the id of the base
  frame on the robot
- `x_stddev` (`double`, default: `0.002`): the standard deviation for
  odometry in X direction (higher values for this term implies odometry
  is doing worse)
- `y_stddev` (`double`, default: `0.002`): the standard deviation for
  odometry in Y direction (higher values for this term implies odometry
  is doing worse)
- `rotation_stddev` (`double`, default: `0.017`): the standard deviation
  for odometry in yaw (higher values for this term implies odometry is
  doing worse)
- `cov_xy` (`double`, default: `0.0`): the off-axis values in the
  covariance matrix
- `cov_xrotation` (`double`, default: `0.0`): the off-axis values in the
  covariance matrix
- `cov_yrotation` (`double`, default: `0.0`): the off-axis values in the
  covariance matrix
- `odom_publish_rate` (`double`, default: `100.0`): Odometry publish
  rate (Hz)
- `odometer_publish_rate` (`double`, default: `1.0`): Odometer publish
  rate (Hz)
- `state_publish_rate` (`double`, default: `1.0`): Odometry state
  publish rate (Hz)
- `wheel_radius_multiplier` (`double`, default: `1.0`): A correction
  multiplier for the radius of the wheels on the robot
- `caster_calibration_multiplier` (`double`, default: `1.0`): A
  correction multiplier for the reduction ratio for the caster rotation
  joint

**Example Configuration:** 

```
base_odometry:
  caster_names: fr_caster_rotation_link fl_caster_rotation_link bl_caster_rotation_link br_caster_rotation_link
  type: Pr2Odometry
  ils_max_iterations: 3
  odom_frame: odom
  base_footprint_frame: base_footprint
  base_link_frame: base_link
  x_stddev: 0.002
  y_stddev: 0.002
  rotation_stddev: 0.017
  cov_xy: 0.0
  cov_xrotation: 0.0
  cov_yrotation: 0.0
  verbose: false
  wheel_radius_multiplier: 1.0
  caster_calibration_multiplier: 1.0
  odom_publish_rate: 100.0
  state_publish_rate: 1.0
  odometer_publish_rate: 1.0
```



###### Published Topics

- `<name>/odom`
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)):
  Odometry is published on this topic in addition to being published
  directly to tf
- `<name>/odometer`
  ([pr2_mechanism_controllers/msg/Odometer](https://docs.ros.org/en/rolling/p/pr2_mechanism_controllers/msg/Odometer.html)):
  The odometer published on this topic contains the total translational
  and rotational distance traveled
- `/tf`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html)):
  Two transforms are published to tf, a constant transform from the
  base_footprint frame to the base_link frame and the transform from the
  odom frame to the base footprint frame.
- `<name>/state`
  ([pr2_mechanism_controllers/msg/BaseOdometryState](https://docs.ros.org/en/rolling/p/pr2_mechanism_controllers/msg/BaseOdometryState.html)):
  The odometry state contains information about wheel drive errors
  (difference in predicted and actual wheel speeds) and longitudinal
  slip errors (amount by which the wheels are predicted to be slipping
  sideways)

## Pr2GripperController

### Overview

The gripper controller provides an interface for sending position
setpoints limited by a maximum effort. You may want to connect a
[pr2_gripper_action](https://index.ros.org/p/pr2_gripper_action) to make
the gripper easier to command.

### ROS API

##### Parameters

- `joint` (`string`, default: `Required`): The joint to control
- `pid/p` (`double`, default: `Required`): The position gain for the
  controller
- `pid/i` (`double`, default: `0.0`): The integral gain on position
- `pid/i_clamp` (`double`, default: `0.0`): The clamp on the integral
  gain
- `pid/d` (`double`, default: `0.0`): The velocity gain of the
  controller

##### Subscribed Topics

- `command`
  ([pr2_controllers_msgs/msg/Pr2GripperCommand](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/Pr2GripperCommand.html)):
  Accepts set point commands

##### Published Topics

- `state`
  ([pr2_controllers_msgs/msg/JointControllerState](https://docs.ros.org/en/rolling/p/pr2_controllers_msgs/msg/JointControllerState.html)):
  Reports the current state of the controller.

### Example Configuration



```
r_gripper_controller:
  type: Pr2GripperController
  joint: r_gripper_joint
  pid:
    p: 1000.0
```
