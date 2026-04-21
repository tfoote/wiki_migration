## Overview

dlut_motor_hokuyo is a package associated with control of the robot
"SmartROB" our lab developed independently.

The node named dlut_motor_hokuyo is used for sending control command of
hokuyo motor to the serial port.

## Usage

Node "dlut_motor_hokuyo" can be started by running:


```shell
rosrun dlut_motor_hokuyo dlut_motor_hokuyo
```



## Nodes



```clearsilver
node.0 {
name = dlut_motor_hokuyo
desc = The dlut_motor_hokuyo node is a base controller node.It must run on a computer attached directly to the motor controller by serial port.

sub {
0{
name = is_run
type = std_msgs/Bool
desc = Whether the motor under hokuyo is running or not.
}
}
pub {
0{
name = motor_param
type = dlut_motor_hokuyo/motor
desc = Punlish the param of motor.
}
}
param {
0.name = baudrate_
0.type = int
0.desc = The baud rate of the serial port.
0.default = 19200
1.name = port_
1.type = int
1.desc = The serial port number.
1.default = 1
}
}
```



## Bug Reports & Feature Requests

We appreciate the time and effort spent submitting bug reports.
