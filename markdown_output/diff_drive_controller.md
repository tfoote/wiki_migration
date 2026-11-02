## Overview

Controller for differential drive wheel systems. Control is in the form
of a velocity command, that is split then sent on the two wheels of a
differential drive wheel base. Odometry is computed from the feedback
from the hardware, and published.

### Velocity commands

The controller works with a velocity twist from which it extracts the x
component of the linear velocity and the z component of the angular
velocity. Velocities on other components are ignored.

### Hardware interface type

The controller works with wheel joints through a **velocity** interface.

### Other features

- **Realtime-safe** implementation.
- Odometry publishing
- Task-space velocity, acceleration and jerk limits
- Automatic stop after command time-out

### Mathematical Background

![\|align="right"](https://upload.wikimedia.org/wikipedia/commons/2/28/Differential_Drive_Kinematics_of_a_Wheeled_Mobile_Robot.svg)

The illustration on the right shows a sketch of a
[differential drive wheeled robot](https://en.wikipedia.org/wiki/Differential_wheeled_robot).
In this sketch, the following notation applies.

- ![](https://latex.codecogs.com/svg.image?V) - linear velocity
  (Velocity Command, see chapter 1.1)
- ![](https://latex.codecogs.com/svg.image?\omega) - angular velocity by
  which the robot rotates (Velocity Command, see chapter 1.1)
- ![](https://latex.codecogs.com/svg.image?X) and
  ![](https://latex.codecogs.com/svg.image?Y) - global coordinate system
- {{<https://latex.codecogs.com/svg.image?X_%7BB%7D> }} and
  {{<https://latex.codecogs.com/svg.image?Y_%7BB%7D> }} - locale body
  coordinate system
- ![](https://latex.codecogs.com/svg.image?\varphi ) - angle of robot
  with respect to global coordinate system
- ![](https://latex.codecogs.com/svg.image?r) - radius of the wheels
- ![](https://latex.codecogs.com/svg.image?b) - width of the vehicle
- ![](https://latex.codecogs.com/svg.image?ICR)⁣ - instantaneous center
  of rotation
- {{<https://latex.codecogs.com/svg.image?v_%7BL%7D> }},
  {{<https://latex.codecogs.com/svg.image?v_%7BR%7D> }} - ground contact
  speed of left and right wheel
- {{[https://latex.codecogs.com/svg.image?\\omega_{L}](https://latex.codecogs.com/svg.image?\omega_%7BL%7D)
  }},
  {{[https://latex.codecogs.com/svg.image?\\omega_{R}](https://latex.codecogs.com/svg.image?\omega_%7BR%7D)
  }} - angular velocity of left and right wheel

Using the kinematic model (see
[here](https://en.wikipedia.org/wiki/Differential_wheeled_robot#Kinematics_of_Differential_Drive_Robots)),
the diff_drive_controller calculates the left
{{[https://latex.codecogs.com/svg.image?\\omega_{L}](https://latex.codecogs.com/svg.image?\omega_%7BL%7D)
}} and right angular velocity
{{[https://latex.codecogs.com/svg.image?\\omega_{R}](https://latex.codecogs.com/svg.image?\omega_%7BR%7D)
}} to:

{{[https://latex.codecogs.com/svg.image?\\omega_{L}&space;=&space;\\frac{V-\\omega&space;\\cdot&space;b/2](https://latex.codecogs.com/svg.image?\omega_%7BL%7D&space;=&space;\frac%7BV-\omega&space;\cdot&space;b/2)}{r}
}}

and

{{[https://latex.codecogs.com/svg.image?\\omega_{R}&space;=&space;&space;&space;\\frac{V+\\omega&space;\\cdot&space;b/2](https://latex.codecogs.com/svg.image?\omega_%7BR%7D&space;=&space;&space;&space;\frac%7BV+\omega&space;\cdot&space;b/2)}{r}
}}.

## Robots

  -- ---------------------------------------------------------- -- -------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------------------------------------------------------------------------- --
     [![REEM](doc/reem_boxes.jpg)](Robots/REEM)                    [PAL Robotics REEM](http://www.pal-robotics.com)      ![PMB2](doc/pmb2.jpg)                                                                                                                                     [PAL Robotics Mobile Base](http://www.pal-robotics.com)                     
     [![Husky](doc/Husky_Icon_-_Small.jpg)](Robots/Husky)          [Clearpath Robotics Husky](Robots/Husky)              [![Robots/Jackal](doc/Jackal_Icon.png)](Robots/Jackal)                                                                                                    [Clearpath Robotics Jackal](Robots/Jackal)                                  
     [![i-Cart mini](doc/icart_mini.png)](Robots/i-Cart mini)      [i-Cart mini](Robots/icart_mini)                      ![Remo\|width="150"](https://raw.githubusercontent.com/ros-mobile-robots/ros-mobile-robots.github.io/main/docs/resources/remo/remo_front_side.jpg)      [ros-mobile-robots/diffbot](https://github.com/ros-mobile-robots/diffbot)   
  -- ---------------------------------------------------------- -- -------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------------------------------------------------------------------------- --

## ROS API

### Description

The controller main input is a
[geometry_msgs::Twist](http://docs.ros.org/api/geometry_msgs/html/msg/Twist.html)
topic in the namespace of the controller.

#### Subscribed Topics

- `cmd_vel`
  ([geometry_msgs/msg/Twist](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/Twist.html)):
  Velocity command.

#### Published Topics

- `odom`
  ([nav_msgs/msg/Odometry](https://docs.ros.org/en/rolling/p/nav_msgs/msg/Odometry.html)):
  Odometry computed from the hardware feedback.
- `/tf`
  ([tf/msg/tfMessage](https://docs.ros.org/en/rolling/p/tf/msg/tfMessage.html)):
  Transform from odom to base_footprint
- `publish_cmd`
  ([geometry_msgs/msg/TwistStamped](https://docs.ros.org/en/rolling/p/geometry_msgs/msg/TwistStamped.html)):
  Available when "publish_cmd" parameter is set to True. It is the
  Twist after limiters have been applied on the controller input.

#### Parameters

- `left_wheel` (`string | string[...]`): Left wheel joint name or list
  of joint names
- `right_wheel` (`string | string[...]`): Right wheel joint name or list
  of joint names
- `pose_covariance_diagonal` (`double[6]`): Diagonal of the covariance
  matrix for odometry pose publishing
- `twist_covariance_diagonal` (`double[6]`): Diagonal of the covariance
  matrix for odometry twist publishing
- `publish_rate` (`double`, default: `50.0`): Frequency (in Hz) at which
  the odometry is published. Used for both tf and odom
- `wheel_separation_multiplier` (`double`, default: `1.0`): Multiplier
  applied to the wheel separation parameter. This is used to account for
  a difference between the robot model and a real robot.
- `wheel_radius_multiplier` (`double`, default: `1.0`): Multiplier
  applied to the wheel radius parameter. This is used to account for a
  difference between the robot model and a real robot.
- `cmd_vel_timeout` (`double`, default: `0.5`): Allowed period (in s)
  allowed between two successive velocity commands. After this delay, a
  zero speed command will be sent to the wheels.
- `base_frame_id` (`string`, default: `base_link`): Base frame_id, which
  is used to fill in the child_frame_id of the Odometry messages and TF.
- `linear/x/has_velocity_limits` (`bool`, default: `false`): Whether the
  controller should limit linear speed or not.
- `linear/x/max_velocity` (`double`): Maximum linear velocity (in m/s)
- `linear/x/min_velocity` (`double`): Minimum linear velocity (in m/s).
  Setting this to 0.0 will disable backwards motion. When unspecified,
  -max_velocity is used.
- `linear/x/has_acceleration_limits` (`bool`, default: `false`): Whether
  the controller should limit linear acceleration or not.
- `linear/x/max_acceleration` (`double`): Maximum linear acceleration
  (in m/s\^2)
- `linear/x/min_acceleration` (`double`): Minimum linear acceleration
  (in m/s\^2). When unspecified, -max_acceleration is used.
- `linear/x/has_jerk_limits` (`bool`, default: `false`): Whether the
  controller should limit linear jerk or not.
- `linear/x/max_jerk` (`double`): Maximum linear jerk (in m/s\^3).
- `angular/z/has_velocity_limits` (`bool`, default: `false`): Whether
  the controller should limit angular velocity or not.
- `angular/z/max_velocity` (`double`): Maximum angular velocity (in
  rad/s)
- `angular/z/min_velocity` (`double`): Minimum angular velocity (in
  rad/s). Setting this to 0.0 will disable counter-clockwise rotation.
  When unspecified, -max_velocity is used.
- `angular/z/has_acceleration_limits` (`bool`, default: `false`):
  Whether the controller should limit angular acceleration or not.
- `angular/z/max_acceleration` (`double`): Maximum angular acceleration
  (in rad/s\^2)
- `angular/z/min_acceleration` (`double`): Minimum angular acceleration
  (in rad/s\^2). When unspecified, -max_acceleration is used.
- `angular/z/has_jerk_limits` (`bool`, default: `false`): Whether the
  controller should limit angular jerk or not.
- `angular/z/max_jerk` (`double`): Maximum angular jerk (in m/s\^3).
- `enable_odom_tf` (`bool`, default: `true`): Publish to TF directly or
  not
- `wheel_separation` (`double`): The distance of the left and right
  wheel(s). The diff_drive_controller will attempt to read the value
  from the URDF if this parameter is not specified
- `wheel_radius` (`double`): Radius of the wheels. It is expected they
  all have the same size. The diff_drive_controller will attempt to read
  the value from the URDF if this parameter is not specified.
- `odom_frame_id` (`string`, default: `"/odom"`): Name of frame to
  publish odometry in.
- `publish_cmd` (`bool`, default: `False`): Publish the velocity command
  to be executed. It is to monitor the effect of limiters on the
  controller input.
- `allow_multiple_cmd_vel_publishers` (`bool`, default: `False`):
  Setting this to true will allow more than one publisher on the input
  topic, /cmd_vel. Setting this to false will cause the controller to
  brake if there is more than one publisher on /cmd_vel.
- `velocity_rolling_window_size` (`int`, default: `10`): The number of
  velocity samples to average together to compute the odometry
  twist.linear.x and twist.angular.z velocities

### Controller configuration examples

#### Minimal description



```yaml
mobile_base_controller:
  type: "diff_drive_controller/DiffDriveController"
  left_wheel: 'wheel_left_joint'
  right_wheel: 'wheel_right_joint'
  pose_covariance_diagonal: [0.001, 0.001, 1000000.0, 1000000.0, 1000000.0, 1000.0]
  twist_covariance_diagonal: [0.001, 0.001, 1000000.0, 1000000.0, 1000000.0, 1000.0]
```



#### Complete description



```yaml
mobile_base_controller:
  type        : "diff_drive_controller/DiffDriveController"
  left_wheel  : 'wheel_left_joint'
  right_wheel : 'wheel_right_joint'
  publish_rate: 50.0               # default: 50
  pose_covariance_diagonal : [0.001, 0.001, 1000000.0, 1000000.0, 1000000.0, 1000.0]
  twist_covariance_diagonal: [0.001, 0.001, 1000000.0, 1000000.0, 1000000.0, 1000.0]

  # Wheel separation and diameter. These are both optional.
  # diff_drive_controller will attempt to read either one or both from the
  # URDF if not specified as a parameter
  wheel_separation : 1.0
  wheel_radius : 0.3

  # Wheel separation and radius multipliers
  wheel_separation_multiplier: 1.0 # default: 1.0
  wheel_radius_multiplier    : 1.0 # default: 1.0

  # Velocity commands timeout [s], default 0.5
  cmd_vel_timeout: 0.25

  # Base frame_id
  base_frame_id: base_footprint #default: base_link

  # Velocity and acceleration limits
  # Whenever a min_* is unspecified, default to -max_*
  linear:
    x:
      has_velocity_limits    : true
      max_velocity           : 1.0  # m/s
      min_velocity           : -0.5 # m/s
      has_acceleration_limits: true
      max_acceleration       : 0.8  # m/s^2
      min_acceleration       : -0.4 # m/s^2
      has_jerk_limits        : true
      max_jerk               : 5.0  # m/s^3
  angular:
    z:
      has_velocity_limits    : true
      max_velocity           : 1.7  # rad/s
      has_acceleration_limits: true
      max_acceleration       : 1.5  # rad/s^2
      has_jerk_limits        : true
      max_jerk               : 2.5  # rad/s^3
```



#### Skid steer

The diff_drive_controller allows for skid steer driving with the
geometry_msgs/Twist command interface however it doesn't support direct
skid commands.

The current implementation allows you to register multiple wheels per
side and will average those wheel positions in its odometry
calculations. For more info read the code and
[issue](https://github.com/ros-controls/ros_controllers/issues/100).

Multiple wheels per side example from Jackal.



```yaml

jackal_velocity_controller:
  type: "diff_drive_controller/DiffDriveController"
  left_wheel: ['front_left_wheel', 'rear_left_wheel']
  right_wheel: ['front_right_wheel', 'rear_right_wheel']
  publish_rate: 50
  pose_covariance_diagonal: [0.001, 0.001, 1000000.0, 1000000.0, 1000000.0, 0.03]
  twist_covariance_diagonal: [0.001, 0.001, 0.001, 1000000.0, 1000000.0, 0.03]
  cmd_vel_timeout: 0.25

  # Odometry fused with IMU is published by robot_localization, so
  # no need to publish a TF based on encoders alone.
  enable_odom_tf: false

  # Wheel separation and radius multipliers
  wheel_separation_multiplier: 1.5 # default: 1.0
  wheel_radius_multiplier    : 1.0 # default: 1.0

  # Velocity and acceleration limits
  # Whenever a min_* is unspecified, default to -max_*
  linear:
    x:
      has_velocity_limits    : true
      max_velocity           : 2.0   # m/s
      has_acceleration_limits: true
      max_acceleration       : 20.0   # m/s^2
  angular:
    z:
      has_velocity_limits    : true
      max_velocity           : 4.0   # rad/s
      has_acceleration_limits: true
      max_acceleration       : 25.0   # rad/s^2
```



## Further reading

In addition to the robots addressed in chapter 2, tutorials for the
application of the `diff_drive_controller` should be briefly
mentioned.

A basic understanding of the implementation of `ros_control` and its
interaction with the `hardware_interface` is explained in
[this](https://slaterobotics.medium.com/how-to-implement-ros-control-on-a-custom-robot-748b52751f2e)
post.

An overview of the `diff_drive_controller` and its integration into
`ros_control` can be found in the
[DiffBot Base Package](https://ros-mobile-robots.com/packages/diffbot_base/)
tutorial.

A detailed description of the specific execution and application of the
`diff_drive_controller` can also be found in the
[DiffBot Base Package](https://ros-mobile-robots.com/packages/diffbot_base/low-level/).

In the Jackal Robot, the
[diff_drive_controller](https://github.com/jackal/jackal/tree/noetic-devel/jackal_control)
is also applied, and the control commands
({{[https://latex.codecogs.com/svg.image?\\omega_{L}](https://latex.codecogs.com/svg.image?\omega_%7BL%7D)
}} and
{{[https://latex.codecogs.com/svg.image?\\omega_{R}](https://latex.codecogs.com/svg.image?\omega_%7BR%7D)
}}) are being retrieved in the
[hardware_interface](https://github.com/jackal/jackal_robot/blob/noetic-devel/jackal_base/src/jackal_hardware.cpp#L49)
and forwarded to the corresponding drives.
