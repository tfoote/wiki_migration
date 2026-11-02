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



```clearsilver
param{
  0.name=joint
  0.type=string
  0.desc=The joint to control
  0.default=Required
  1.name=gains/p
  1.type=double
  1.desc=The position gain
  1.default=Required
  2.name=gains/d
  2.type=double
  2.desc=The position derivative gain
  2.default=0.0
  3.name=gains/i
  3.type=double
  3.desc=The integral gain around position
  3.default=0.0
  4.name=gains/i_clamp
  4.type=double
  4.desc=The clamp of the integral gain
  4.default=0.0
  5.name=velocity_filter
  5.type=Filter Chain
  5.desc=namespace defining a filter chain acting on the measured velocity. Refer to [[filters#Filter_Chain|Filter Chain]] for more details
  5.default=Required
  6.name=max_velocity
  6.type=double
  6.desc=Maximum allowed velocity/rate for a trajectory that this controller generates (in rad/sec)
  6.default=Required
  7.name=max_acceleration
  7.type=double
  7.desc=Maximum allowed acceleration for a trajectory that this controller generates (in rad/sec^2)
  7.default=Required

}
```



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





```clearsilver
pub{
  0.name=<name>/laser_scanner_signal
  0.type=pr2_msgs/LaserScannerSignal
  0.desc=The index of the last completed trajectory segment. Useful for aggregating laser scans
}
```





```clearsilver
sub{
  0.name=<name>/set_periodic_cmd
  0.type=pr2_msgs/PeriodicCmd
  0.desc=Sets the periodic trajectory using periodic parameters like period, amplitude, and offset
  1.name=<name>/set_traj_cmd
  1.type=pr2_msgs/LaserTrajCmd
  1.desc=Sets the periodic trajectory by explicitly setting trajectory waypoints
}
```





```clearsilver
srv{
  0.name=<name>/set_periodic_cmd
  0.type=pr2_msgs/SetPeriodicCmd
  0.desc=Sets the periodic trajectory using periodic parameters (period, amplitude, and offset)
  1.name=<name>/set_traj_cmd
  1.type=pr2_msgs/SetLaserTrajCmd
  1.desc=Sets the periodic trajectory by explicitly setting trajectory waypoints (position & time pairs)
}
```



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



```clearsilver
param{
  0.name=max_translational_velocity
  0.type=double
  0.desc=Maximum allowed translational velocity
  0.default=1.0
  1.name=max_rotational_velocity
  1.type=double
  1.desc=Maximum allowed rotational velocity 
  1.default=2.0
  2.name=max_translational_acceleration/x
  2.type=double
  2.desc=Maximum allowed acceleration in X direction 
  2.default=2.0
  3.name=max_translation_acceleration/y
  3.type=double
  3.desc=Maximum allowed acceleration in X direction 
  3.default=2.0
  5.name=max_rotational_acceleration
  5.type=double
  5.desc=Maximum allowed yaw acceleration
  5.default=2.0
 
  12.name=kp_caster_steer
  12.type=double
  12.desc=The proportional gain on the caster steer velocity controller, vel_desired = kp_caster_steer * caster_steer_error
  12.default=80.0
  14.name=timeout
  14.type=double
  14.desc=If time from last command heard > timeout, the controller will stop the robot.
  14.default=0.3
  16.name=state_publish_rate
  16.type=double
  16.desc=rate of state publishing events
  16.default=1.0
  18.name=caster_names
  18.type=string
  18.desc=The string names for all the caster link names on the robot separated by a space delimiter
  18.default=""
  20.name=wheel_radius_multiplier
  20.type=double
  20.desc=A correction multiplier for the radius of the wheels on the robot
  20.default=1.0
  21.name=caster_calibration_multiplier
  21.type=double
  21.desc=A correction multiplier for the reduction ratio for the caster rotation joint
  21.default=1.0
}
```



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





```clearsilver
pub{
  0.name=<name>/state
  0.type=pr2_mechanism_controllers/BaseControllerState
  0.desc=The state of the base controller
}
```





```clearsilver
sub{
  1.name=<name>/command
  1.type=geometry_msgs/Twist
  1.desc=Input velocity command for the base (the reference point for this command is the origin of the base link which is in the middle of the base)

}
```

## Pr2Odometry

### PR2 Base Odometry

#### Introduction

This component computes odometry for the base.

**Status:** REVIEWED, NOT STABLE. .

#### ROS API



```clearsilver
param{
  0.name=odometer/initial_distance
  0.type=double
  0.desc=Initial value for the distance traveled by the robot (in m)
  0.default=0.0
  1.name=odometer/initial_angle
  1.type=double
  1.desc=Initial value for the total angular distance traveled by the robot (in radians)
  1.default=0.0
  2.name=odom/initial_x
  2.type=double
  2.desc=Initial X position of the robot in an odometric frame 
  2.default=0.0
  3.name=odom/initial_y
  3.type=double
  3.desc=Initial Y position of the robot in an odometric frame
  3.default=0.0
  4.name=odom/initial_yaw
  4.type=double
  4.desc=Initial yaw position of the robot in an odometric frame 
  4.default=0.0
  6.name=ils_max_iterations
  6.type=int
  6.desc=max number of iterations for iterative least squares
  6.default=3
  7.name=odom_frame
  7.type=string
  7.desc=The odometric frame id
  7.default=odom
  8.name=base_footprint_frame
  8.type=string
  8.desc=The id for a frame that is below the base link and coincident with the ground
  8.default=base_footprint

  9.name=base_link_frame
  9.type=string
  9.desc=the id of the base frame on the robot 
  9.default=base_link

  11.name=x_stddev
  11.type=double
  11.desc=the standard deviation for odometry in X direction (higher values for this term implies odometry is doing worse)
  11.default=0.002

  12.name=y_stddev
  12.type=double
  12.desc=the standard deviation for odometry in Y direction (higher values for this term implies odometry is doing worse)
  12.default=0.002
  13.name=rotation_stddev
  13.type=double
  13.desc=the standard deviation for odometry in yaw (higher values for this term implies odometry is doing worse)
  13.default=0.017
  14.name=cov_xy
  14.type=double
  14.desc=the off-axis values in the covariance matrix
  14.default=0.0
  15.name=cov_xrotation
  15.type=double
  15.desc=the off-axis values in the covariance matrix
  15.default=0.0
  16.name=cov_yrotation
  16.type=double
  16.desc=the off-axis values in the covariance matrix
  16.default=0.0

  17.name=odom_publish_rate
  17.type=double
  17.desc=Odometry publish rate (Hz)
  17.default=100.0
  18.name=odometer_publish_rate
  18.type=double
  18.desc=Odometer publish rate (Hz)
  18.default=1.0
  19.name=state_publish_rate
  19.type=double
  19.desc=Odometry state publish rate (Hz)
  19.default=1.0

  20.name=wheel_radius_multiplier
  20.type=double
  20.desc=A correction multiplier for the radius of the wheels on the robot
  20.default=1.0
  21.name=caster_calibration_multiplier
  21.type=double
  21.desc=A correction multiplier for the reduction ratio for the caster rotation joint
  21.default=1.0
}
```



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





```clearsilver
pub{
  0.name=<name>/odom
  0.type=nav_msgs/Odometry
  0.desc=Odometry is published on this topic in addition to being published directly to tf
  1.name=<name>/odometer
  1.type=pr2_mechanism_controllers/Odometer
  1.desc=The odometer published on this topic contains the total translational and rotational distance traveled
  2.name=/tf
  2.type=tf/tfMessage
  2.desc=Two transforms are published to tf, a constant transform from the base_footprint frame to the base_link frame and the transform from the odom frame to the base footprint frame.
  3.name=<name>/state
  3.type=pr2_mechanism_controllers/BaseOdometryState
  3.desc=The odometry state contains information about wheel drive errors (difference in predicted and actual wheel speeds) and longitudinal slip errors (amount by which the wheels are predicted to be slipping sideways)

}
```

## Pr2GripperController

### Overview

The gripper controller provides an interface for sending position
setpoints limited by a maximum effort. You may want to connect a
[pr2_gripper_action](https://index.ros.org/p/pr2_gripper_action) to make
the gripper easier to command.

### ROS API



```clearsilver
param {
  0.name=joint
  0.type=string
  0.default=Required
  0.desc=The joint to control
  1.name=pid/p
  1.type=double
  1.default=Required
  1.desc=The position gain for the controller
  2.name=pid/i
  2.type=double
  2.default=0.0
  2.desc=The integral gain on position
  3.name=pid/i_clamp
  3.type=double
  3.default=0.0
  3.desc=The clamp on the integral gain
  4.name=pid/d
  4.type=double
  4.default=0.0
  4.desc=The velocity gain of the controller
}
```





```clearsilver
pub {
  0.name=state
  0.type=pr2_controllers_msgs/JointControllerState
  0.desc=Reports the current state of the controller.
}
sub {
  0.name=command
  0.type=pr2_controllers_msgs/Pr2GripperCommand
  0.desc=Accepts set point commands
}
```



### Example Configuration



```
r_gripper_controller:
  type: Pr2GripperController
  joint: r_gripper_joint
  pid:
    p: 1000.0
```
