<https://github.com/WuNL/laser_to_cloud.git>

## Overview

dlut_move_base is a package associated with control and movement of the
robot "SmartROB" our lab developed independently. The serial_com node is
a base controller node.It must run on a computer attached directly to
the motor controller by serial port.And the sick_key node is used to get
the command from the keyboard.

## Usage

Node "serial_com" can be started by running: ```shell
rosrun dlut_move_base serial_com
```

Node "sick_key" can be started by running: ```shell
rosrun dlut_move_base sick_key
```

## Nodes

```clearsilver
node.0 {
name = serial_com
desc = The serial_com node is a base controller node.It must run on a computer attached directly to the motor controller by serial port.

sub {
0{
name = cmd_velocity
type = dlut_move_base/Velocity
desc = the command to control the robot.
}
1{
name = cmd_twist
type = dlut_move_base/Twist
desc = the command to control the robot.
}
}
pub {
0{
name = robot_velocity
type = dlut_move_base/Twist
desc = the velocity from the robot.
}
1{
name = odom
type = nav_msgs/Odometry
desc = Get the odometry value.
}
}
param {
0.name = Port
0.type = int
0.desc = The serial port number.
0.default = 2
1.name = BaudRate
1.type = int
1.desc = The baud rate of the serial port.
1.default = 9600
}
}

node.1 {
name = sick_key
desc = The sick_key node is used to get the command from the keyboard. 

pub {
0.name = is_run
0.type = std_msgs/Bool
0.desc = Publish the message to tell the motor to rotate or not.
1.name = is_run_pch
1.type = std_msgs/Bool
1.desc = Publish the message whether the holder begin to rotate or not.
2.name = cmd_velocity
2.type = dlut_move_base/Velocity
2.desc = Publish the command to the topic to control the robot.
}

param {
0.name = scale_angular
0.type = double
0.desc = the weight of the angular velocity's increment.
0.default = 0.1
1.name = scale_linear
1.type = double
1.desc = the weight of the linear velocity's increment.
1.default = 0.1
```

## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.
