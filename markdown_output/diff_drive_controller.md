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

  -- -------------------------------------------------------------------------------- -- -------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------------------------------------------------------------------------- --
     [![REEM\|width="100"](attachment:reem_boxes.jpg)](Robots/REEM)                    [PAL Robotics REEM](http://www.pal-robotics.com)      ![PMB2\|width="150"](attachment:pmb2.jpg)                                                                                                               [PAL Robotics Mobile Base](http://www.pal-robotics.com)                     
     [![Husky](attachment:Husky Icon - Small.jpg)](Robots/Husky)                         [Clearpath Robotics Husky](Robots/Husky)              [![Robots/Jackal](attachment:Jackal Icon.png)](Robots/Jackal)                                                                                             [Clearpath Robotics Jackal](Robots/Jackal)                                  
     [![i-Cart mini\|width="150"](attachment:icart_mini.png)](Robots/i-Cart mini)      [i-Cart mini](Robots/icart_mini)                      ![Remo\|width="150"](https://raw.githubusercontent.com/ros-mobile-robots/ros-mobile-robots.github.io/main/docs/resources/remo/remo_front_side.jpg)      [ros-mobile-robots/diffbot](https://github.com/ros-mobile-robots/diffbot)   
  -- -------------------------------------------------------------------------------- -- -------------------------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------ -- --------------------------------------------------------------------------- --

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
```

 

```clearsilver
pub {
  0.name= odom
  0.type= nav_msgs/Odometry
  0.desc= Odometry computed from the hardware feedback.

  1.name= /tf
  1.type= tf/tfMessage
  1.desc= Transform from odom to base_footprint

  2.name= publish_cmd
  2.type= geometry_msgs/TwistStamped
  2.desc= Available when "publish_cmd" parameter is set to True. It is the Twist after limiters have been applied on the controller input.
}
```




```clearsilver
param{
  0.name=left_wheel
  0.type=string | string[...]
  0.desc=Left wheel joint name or list of joint names
  1.name=right_wheel
  1.type=string | string[...]
  1.desc=Right wheel joint name or list of joint names
  2.name=pose_covariance_diagonal
  2.type=double[6]
  2.desc=Diagonal of the covariance matrix for odometry pose publishing
  3.name=twist_covariance_diagonal
  3.type=double[6]
  3.desc=Diagonal of the covariance matrix for odometry twist publishing
  4.name=publish_rate
  4.type=double
  4.desc=Frequency (in Hz) at which the odometry is published. Used for both tf and odom
  4.default=50.0
  5.name=wheel_separation_multiplier
  5.type=double
  5.desc=Multiplier applied to the wheel separation parameter. This is used to account for a difference between the robot model and a real robot.
  5.default=1.0
  6.name=wheel_radius_multiplier
  6.type=double
  6.desc=Multiplier applied to the wheel radius parameter. This is used to account for a difference between the robot model and a real robot.
  6.default=1.0
  7.name=cmd_vel_timeout
  7.type=double
  7.desc=Allowed period (in s) allowed between two successive velocity commands. After this delay, a zero speed command will be sent to the wheels.
  7.default=0.5
  8.name=base_frame_id
  8.type=string
  8.desc=Base frame_id, which is used to fill in the child_frame_id of the Odometry messages and TF.
  8.default=base_link
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
 25.name=enable_odom_tf
 25.type=bool
 25.desc= Publish to TF directly or not
 25.default=true
 26.name=wheel_separation
 26.type=double
 26.desc=The distance of the left and right wheel(s). The diff_drive_controller will attempt to read the value from the URDF if this parameter is not specified
 27.name=wheel_radius
 27.type=double
 27.desc=Radius of the wheels. It is expected they all have the same size. The diff_drive_controller will attempt to read the value from the URDF if this parameter is not specified.
 28.name=odom_frame_id
 28.type=string
 28.desc=Name of frame to publish odometry in.
 28.default="/odom"
 29.name=publish_cmd
 29.type=bool
 29.desc=Publish the velocity command to be executed. It is to monitor the effect of limiters on the controller input.
 29.default=False
 30.name=allow_multiple_cmd_vel_publishers
 30.type=bool
 30.desc=Setting this to true will allow more than one publisher on the input topic, ~/cmd_vel.  Setting this to false will cause the controller to brake if there is more than one publisher on ~/cmd_vel.
 30.default=False
 31.name=velocity_rolling_window_size
 31.type=int
 31.desc=The number of velocity samples to average together to compute the odometry twist.linear.x and twist.angular.z velocities
 31.default=10
}
```



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
