ros0xrobot node provides ROS interface for robot bases in 0x series
(pronounced as Ox). The ROS interface is supported by 0xRobotCpp library
from [Nex Robotics](http://www.nex-robotics.com/). Information from the
robot base, velocity and acceleration control, is implemented via a
ros0xrobot node, which publishes topics providing data received from the
robot\'s embedded controller by 0xRobotCpp library, and sets desired
velocity, acceleration and other commands in robot when new commands are
received from command topics.

## Installation and Getting Started

Instructions on installing ROS can be found
[here](http://wiki.ros.org/indigo/Installation/Ubuntu).

## Reporting bugs and making feature requests

Bugs and requests can be reported here: \<\<MailTo(support AT
nex-robotics DOT com)\>\>

## ros0xrobot node

```clearsilver
 name = ros0xrobot
 desc =  A simple node to communicate with 0x series robot from nex Robotics. Topics published by ros0xrobot node are available under topic named `ros0xrobot/topic`. The ros0xrobot node requires 0xRobotCpp library for establishing communication with robot base. The library is available in the '/lib' folder of source provided.

sub {
  0.name = cmd_vel
  0.type = geometry_msgs/Twist
  0.desc =  Receives new velocity commands. The received velocities will be updated and maintained by robot. There is no need to send the velocity repeatedly to maintain the velocity. If the robot is kept in timeout mode, then any valid communication/command needs to be sent to the robot before timeout to keep the robot moving.
}

pub {
  0.name = pose
  0.type = nav_msgs/Odometry
  0.desc = publishes odometry information (rate depends on the robot, normally 10Hz)
}

pub {
  1.name = sonar
  1.type = sensor_msgs/PointCloud
  1.desc = publishes sonar readings. Requires `enableSonar` parameter to be set to true.
}

pub {
  2.name = imu
  2.type = sensor_msgs/Imu
  2.desc = publishes imu readings. Requires `enableImu` parameter to be set to true.
}

param {
  0.name = ~port
  0.type = string
  0.desc = Serial port device the robot is is connected to. Set to /dev/ttyUSBx depending on port on which robot is connected.
  0.default = /dev/ttyUSB0
}

param {
  1.name = CountsPerRev
  1.type = int
  1.desc = Set counts per revolution of the robot. Refer hardware manual of robot for appropriate value.
  1.default = 3840
}

param {
  2.name = WheelDiameter
  2.type = float
  2.desc = Set wheel diameter of robot in mm.
  2.default = 100.0
}

param {
  3.name = AxelLength
  3.type = float
  3.desc = Set axle length in mm.
  3.default = 290.0
}

param {
  4.name = enableSonar
  4.type = bool
  4.desc = Enable or disable Sonar. This will cause the node to start publishing sonar messages when enabled.
  4.default = false
}

param {
  5.name = enableImu
  5.type = bool
  5.desc = Enable or disable IMU. This will cause the node to start publishing imu messages when enabled.
  5.default = false
}
```

### Running ros0xrobot node

\$rosrun ros0xrobot ros0xrobotNode
