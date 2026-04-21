## Introduction

This package provides a driver for the
[Thymio II](https://aseba.wikidot.com/en:thymio) robot using the
[asebaros](asebaros) package. This driver listens to velocity commands
and outputs odometry and `tf` data. In addition, we provide launch
files to do SLAM and path planning with [gmapping](gmapping) and
[navigation](navigation) stack, should an [Hokuyo sensor](hokuyo_node)
be taped on top of the Thymio, like in this picture:

![](attachment:thymio-hokuyo.jpg)

![](attachment:thymio-hokuyo-closeup.jpg)

## Usage

### Node: thymio_navigation_driver

This node interfaces the Thymio with ROS. It demands an
[asebaros](asebaros) node connected to the Thymio. Using asebaros, this
node will accept twist commands and publish odometry/tf.



```clearsilver
sub {
  0.name = /aseba/events/odometry
  0.type = asebaros/AsebaEvent
  0.desc = aseba odometry messages from the Thymio
  1.name = cmd_vel
  1.type = geometry_msgs/Twist
  1.desc = velocity commands from ROS
}
pub {
  0.name = /aseba/events/set_speed
  0.type = asebaros/AsebaEvent
  0.desc = aseba speed messages to the Thymio
  1.name = odom
  1.type = nav_msgs/Odometry
  1.desc = odometry to ROS
}
prov_tf {
  0.from = base_link
  0.to = odom
  0.desc = tf from odometry
```



### Node: joy_to_twist

This node transform a joystick command into a twist command to control
the speed of Thymio.



```clearsilver
sub {
  0.name = /joy
  0.type = sensor_msgs/Joy
  0.desc = joystick messages
}
pub {
  0.name = /cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = velocity commands
}
```



### Putting it all together

This driver provides a different launch files that together provide the
complete integration with [gmapping](gmapping) and the
[navigation stack](navigation), as you can see in this video:

[Youtube](https://www.youtube.com/watch?v=c6IToN1KJvk)

The file to launch is `aseba_slam_nav_viewer.launch`. For this launch
file to work, you must first connect the Hokuyo and then the Thymio, so
that the Hokuyo gets `/dev/ttyACM0` as device and the Thymio
`/dev/ttyACM1`. This also means that you should have no other
USB-serial device plugged in.
