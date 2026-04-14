```wiki
'''Deprecated'''
You may want to check out the more up-to-date [[flir_ptu_driver]]
```

```clearsilver
name = PTU46
desc = Runs the Directed Perception PTU46
sub {
  0.name = ~cmd
  0.type = sensor_msgs/JointState
  0.desc = Desired position
}
pub {
  0.name = ~state
  0.type = sensor_msgs/JointState
  0.desc = Current pan/tilt position
}
param {
  0.name = ~hz
  0.type = Integer
  0.desc = Polling frequency
  0.default = 10
  1.name = ~port
  1.type = String
  1.desc = Filename for connection
  1.default = /dev/ttyUSB1
  2.name = ~baud
  2.type = Integer
  2.desc = Baud Rate
  2.default = 9600
  
}
param_set {
  0.name = ~min_tilt, ~max_tilt, ~min_pan, ~max_pan
  0.type = Float
  0.desc = Position limits in Radians
  1.name = ~min_tilt_speed, ~max_tilt_speed, ~min_pan_speed, ~max_pan_speed
  1.type = Float
  1.desc = Speed limits in Radians/second
  2.name = ~tilt_step, ~pan_step
  2.type = Float
  2.desc = Smallest possible movement

}
```
