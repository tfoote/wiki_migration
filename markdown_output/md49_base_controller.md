ROS Package for the serial dual motor driver board MD49, designed for
use with two EMG49 motors

\<\<GitHubIssues(scheik/md49_base_controller)\>\>

## Documentation

```clearsilver
name = The md49_base_controller node
desc = Subscribes to /cmd_vel and publishes to topics /md49_data and /md49_encoders
sub {
  0.name = /cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = subscribes this topic
}
pub {
  0.name = /md49_data
  0.type = md49_messages/md49_data
  0.desc = Contains the set parameters and data from MD49, like mode, acceleration, current_left, current_right...
  1.name = /md49_encoders
  1.type = md49_messages/md49_encoders
  1.desc = Encodervalues, read from MD49
}
param_set {
  0.name = ~serialport/name
  0.type = std::string
  0.desc = Used serialport, to which MD49 is connected
  0.default = /dev/ttyS0
  1.name = ~serialport/bps
  1.type = int
  1.desc = Used baudrate for serialport, to which MD49 is connected
  1.default = 38400
  2.name = ~md49/mode
  2.type = int
  2.desc = Mode, with which MD49 initiated
  2.default = 0
  3.name = ~md49/acceleration
  3.type = int
  3.desc = Acceleration, with which MD49 initiated
  3.default = 5
  4.name = ~md49/regulator
  4.type = boolean
  4.desc = Regulator mode, with which MD49 initiated
  4.default = true
  5.name = ~md49/timeout
  5.type = boolean
  5.desc = Timeout mode, with which MD49 initiated
  5.default = true
  6.name = ~md49/speed_l
  6.type = int
  6.desc = Speed for left drive, with which MD49 initiated
  6.default = 128
  7.name = ~md49/speed_r
  7.type = int
  7.desc = Speed for right drive, with which MD49 initiated
  7.default = 128
}
```
