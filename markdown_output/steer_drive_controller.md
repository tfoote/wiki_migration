An example of using the packages can be seen in
[Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03).

## Overview

Controller for wheel systems with steering mechanism. Control is in the
form of a velocity command, that is split then sent on the single rear
wheel and the single front steer of a steering drive wheel base.
Odometry is computed from the feedback from the hardware, and published.

### Velocity commands

The controller works with a velocity twist from which it extracts the x
component of the linear velocity and the z component of the angular
velocity. Velocities on other components are ignored.

### Hardware interface type

The controller inherits **multi_interface_controller** to work with
wheel joints through a **velocity** interface for a linear wheel and a
**position** interface for a front steer wheel, which is the the most
basic configuration for the steer driving mechanism.

### Converting controller's interfaces to actual controller's interfaces

If you want [rviz](rviz) to show states of robot's actual joint
interfaces' [tf](tf) through
[joint_state_controller](joint_state_controller) and
[robot_state_publisher](robot_state_publisher), you need to convert the
two interfaces of `steer_drive_controller` to your robot's specific
ones via
[RobotHW](https://github.com/ros-controls/ros_control/wiki/hardware_interface)
or RobotHWSim (generally used for [GAZEBO](http://gazebosim.org/)). This
is because the controller only update it's basic interfaces mentioned
in the previous section.

### Other features

-   **Realtime-safe** implementation.
-   Odometry publishing
-   Task-space velocity, acceleration and jerk limits
-   Automatic stop after command time-out

## Robots

  -- ----------------------------------------------------------------------------------------- -- ----------------------------------------- --
     [![CIR-KIT-Unit03\|width="100"](attachment:cirkit_unit03.jpg)](Robots/CIR-KIT-Unit03)      [CIR-KIT-Unit03](Robots/CIR-KIT-Unit03)   
  -- ----------------------------------------------------------------------------------------- -- ----------------------------------------- --

## ROS API

### Description

The controller main input is a
[geometry_msgs::Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
topic in the namespace of the controller.

```clearsilver
sub {
  0.name= cmd_vel
  0.type= geometry_msgs/Twist
  0.desc= Velocity command.
}
``` ```clearsilver
pub {
  0.name= odom
  0.type= nav_msgs/Odometry
  0.desc= Odometry computed from the hardware feedback.

  1.name= /tf
  1.type= tf/tfMessage
  1.desc= Transform from odom to base_footprint
}
```

#### Joint Parameters

```clearsilver
param{
  no_header=True
  0.name=rear_wheel
  0.type=string
  0.desc=Rear wheel joint name
  1.name=front_steer
  1.type=string
  1.desc=Front steer joint name
}
```

#### Coveriance Parameters

```clearsilver
param{
  no_header=True
  2.name=pose_covariance_diagonal
  2.type=double[6]
  2.desc=Diagonal of the covariance matrix for odometry pose publishing
  3.name=twist_covariance_diagonal
  3.type=double[6]
  3.desc=Diagonal of the covariance matrix for odometry twist publishing
}
```

#### Time Related Parameters

```clearsilver
param{
  no_header=True
  4.name=publish_rate
  4.type=double
  4.desc=Frequency (in Hz) at which the odometry is published. Used for both tf and odom
  4.default=50.0
  7.name=cmd_vel_timeout
  7.type=double
  7.desc=Allowed period (in s) allowed between two successive velocity commands. After this delay, a zero speed command will be sent to the wheels.
  7.default=0.5
}
```

#### TF Related Parameters

```clearsilver
param{
  no_header=True
  8.name=base_frame_id
  8.type=string
  8.desc=Base frame_id, which is used to fill in the child_frame_id of the Odometry messages and TF.
  8.default=base_link
  9.name=odom_frame_id
  9.type=string
  9.desc=Odometry frame_id
  9.default=odom
 25.name=enable_odom_tf
 25.type=bool
 25.desc= Publish to TF directly or not
 25.default=true
}
```

#### Multiplier Parameters

```clearsilver
param{
  no_header=True
  5.name=wheel_separation_h_multiplier
  5.type=double
  5.desc=Multiplier applied to the wheel separation parameter. This is used to account for a difference between the robot model and a real robot (e.g. odometry tuning).
  5.default=1.0
  6.name=wheel_radius_multiplier
  6.type=double
  6.desc=Multiplier applied to the wheel radius parameter. This is used to account for a difference between the robot model and a real robot (e.g. odometry tuning).
  6.default=1.0
 28.name=steer_pos_multiplier
 28.type=double
 28.desc=Steer position angle multipliers for fine tuning.
 28.default=1.0
}
```

#### Limmiter Parameters

```clearsilver
param{
  no_header=True
  9.name=linear/x/has_velocity_limits
  9.type=bool
  9.desc=Whether the controller should limit linear speed or not.
  9.default=false
 10.name=linear/x/max_velocity
 10.type=double
 10.desc=Maximum linear velocity (in m/s)
 11.name=linear/x/min_velocity
 11.type=double
 11.desc=Minimum linear velocity (in m/s). Setting this to 0.0 will disable backwards motion. When unspecified, -max_velocity is used.
 12.name=linear/x/has_acceleration_limits
 12.type=bool
 12.desc=Whether the controller should limit linear acceleration or not.
 12.default=false
 13.name=linear/x/max_acceleration
 13.type=double
 13.desc=Maximum linear acceleration (in m/s^2)
 14.name=linear/x/min_acceleration
 14.type=double
 14.desc=Minimum linear acceleration (in m/s^2). When unspecified, -max_acceleration is used.
 15.name=linear/x/has_jerk_limits
 15.type=bool
 15.desc=Whether the controller should limit linear jerk or not.
 15.default=false
 16.desc=Maximum linear jerk (in m/s^3).
 16.name=linear/x/max_jerk
 16.type=double
 17.name=angular/z/has_velocity_limits
 17.type=bool
 17.desc=Whether the controller should limit angular velocity or not.
 17.default=false
 18.name=angular/z/max_velocity
 18.type=double
 18.desc=Maximum angular velocity (in rad/s)
 19.name=angular/z/min_velocity
 19.type=double
 19.desc=Minimum angular velocity (in rad/s). Setting this to 0.0 will disable counter-clockwise rotation. When unspecified, -max_velocity is used.
 20.name=angular/z/has_acceleration_limits
 20.type=bool
 20.desc=Whether the controller should limit angular acceleration or not.
 20.default=false
 21.name=angular/z/max_acceleration
 21.type=double
 21.desc=Maximum angular acceleration (in rad/s^2)
 22.name=angular/z/min_acceleration
 22.type=double
 22.desc=Minimum angular acceleration (in rad/s^2). When unspecified, -max_acceleration is used.
 23.name=angular/z/has_jerk_limits
 23.type=bool
 23.desc=Whether the controller should limit angular jerk or not.
 23.default=false
 24.desc=Maximum angular jerk (in m/s^3).
 24.name=angular/z/max_jerk
 24.type=double
}
```

#### Calibration Parameters

```clearsilver
param{
 no_header=True
 26.name=wheel_separation_h
 26.type=double
 26.desc=The distance of the rear wheel and the front wheel. The diff_drive_controller will attempt to read the value from the URDF if this parameter is not specified.
 27.name=wheel_radius
 27.type=double
 27.desc=Radius of the wheels. It is expected they all have the same size. The diff_drive_controller will attempt to read the value from the URDF if this parameter is not specified.
}
```

### Controller configuration examples

#### Minimal description

```yaml
mobile_base_controller:
  type: "steer_drive_controller/SteerDriveController"
  rear_wheel: 'rear_wheel_joint'
  front_steer: 'front_steer_joint'
  pose_covariance_diagonal: [0.001, 0.001, 1000000.0, 1000000.0, 1000000.0, 1000.0]
  twist_covariance_diagonal: [0.001, 0.001, 1000000.0, 1000000.0, 1000000.0, 1000.0]
```

#### Complete description

```clearsilver
pub {
  0.name= odom
  0.type= nav_msgs/Odometry
  0.desc= Odometry computed from the hardware feedback.

  1.name= /tf
  1.type= tf/tfMessage
  1.desc= Transform from odom to base_footprint
}
```0

### RobotHW

An example for usage of `steer_drive_controller` with
[RobotHW](https://github.com/ros-controls/ros_control/wiki/hardware_interface)
can be grabbed from [Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03).

### RobotHWSim for GAZEBO

We developped a general RobotHWSim plugin for usage of
[GAZEBO](http://gazebosim.org/). You can get the plugin from
[steer_bot_hardware_gazebo](steer_bot_hardware_gazebo) and also see an
example of application on
[Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03).

### Recovery Behavior

We also provide a recovery behavior plugin of [move_base](move_base)
specifically desigined for steer mechanism base robots in
[stepback_and_steerturn_recovery](stepback_and_steerturn_recovery). Feel
free to see [Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03) to learn how
to use it.
