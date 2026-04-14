## ROS API

```clearsilver
node.0 {
  name = kurt_base
  sub {
    0.name = rot_vel
    0.type = geometry_msgs/Twist
    0.desc = Commands a desired rotational velocity to the rotation unit.
    1.name = cmd_vel
    1.type = geometry_msgs/Twist
    1.desc = Commands a desired velocity to the Kurt base.
  }
  pub {
    0.name = joint_states
    0.type = sensor_msgs/JointState
    0.desc = Publishes the joint states of the wheels and the rotation unit.
    1.name = odom
    1.type = nav_msgs/Odometry
    1.desc = Publishes the wheel odometry.
    3.name = imu
    3.type = sensor_msgs/Imu
    3.desc = Publishes the IMU data.
    4.name = range
    4.type = sensor_msgs/Range
    4.desc = Publishes ultrasound and infrared range sensor data.
  }
  param {
    0.name = ~wheel_perimeter
    0.type = float
    0.default = 0.379
    0.desc = Wheel perimeter in m (required only for odometry; default is for kurt2_indoor).

    1.name = ~axis_length
    1.type = float
    1.default = 0.28
    1.desc = Length of axis in m (required only for odometry; default is for kurt2_indoor). Axis is the one which holds the tick counters (front/back?).

    2.name = ~turning_adaptation
    2.type = float
    2.default = 0.69
    2.desc = Factor that describes the portion of theoretical angular motion vs. actual angular motion. If the front and back wheels had no friction, this factor would be almost 1.0; however the lateral friction of the front and back wheels makes the middle wheels slip when the robot is turning, leading to this reduction in actual angular motion. Default is for kurt2_indoor.

    3.name = ~ticks_per_turn_of_wheel
    3.type = int
    3.default = 21950
    3.desc = Number of encoder ticks per complete turn of wheel. Default is for both kurt_indoor and kurt_outdoor; kurt_fast has 5120.

    4.name = ~use_rotunit
    4.type = bool
    4.default = false
    4.desc = Do we control the rotation unit?

    5.name = ~x_stddev
    5.type = float
    5.default = 0.002
    5.desc = x standard deviation to be put in Odometry message

    6.name = ~rotation_stddev
    6.type = float
    6.default = 0.017
    6.desc = theta standard deviation to be put in Odometry message

    7.name = ~cov_xy
    7.type = float
    7.default = 0.0
    7.desc = xy covariance to be put in Odometry message

    8.name = ~cov_xrotation
    8.type = float
    8.default = 0.0
    8.desc = x rotation covariance to be put in Odometry message

    9.name = ~cov_yrotation
    9.type = float
    9.default = 0.0
    9.desc = y rotation covariance to be put in Odometry message

    10.name = ~feedforward_turn
    10.type = float
    10.default = 0.35
    10.desc = PID parameter; unit: [m/s] (only evaluated if `~speedtable` is set)

    11.name = ~ki
    11.type = float
    11.default = 3.4
    11.desc = PID parameter (only evaluated if `~speedtable` is set)

    12.name = ~kp
    12.type = float
    12.default = 0.4
    12.desc = PID parameter (only evaluated if `~speedtable` is set)

    13.name = ~publish_tf
    13.type = bool
    13.default = true
    13.desc = Publish TF transform from `odom` to `base_link`?

    14.name = tf_prefix
    14.type = string
    14.default = ' '
    14.desc = The TF prefix to use

    15.name = ~rotunit_speed
    15.type = int
    15.default = M_PI/6.0
    15.desc = The initial rotational speed to send to the rotation unit on startup in rad/sec.

    16.name = ~speedtable
    16.type = string
    16.default = required
    16.desc = File name of speed table. If set, micro controller is disabled and software PID controller is enabled.
  }
}
```
