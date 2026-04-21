## Overview

The arbotix_sensors package contains several sensor modules that add
additional layers of ROS interface onto the basic structure of
[arbotix_python](arbotix_python).

## Nodes



```clearsilver
name=ir_ranger.py
desc=Interface to a Sharp IR range finder. Automatically starts analog stream and publishes a range message derived from the raw stream.
pub {
  0.name = /ir_range
  0.type = sensor_msgs/Range
  0.desc = Output range information.
}
sub {
  0.name = /<name>
  0.type = arbotix_msgs/Analog
  0.desc = Raw analog stream to convert to range messages. 
}
srv_called {
  0.name = /arbotix/SetupAnalogIn
  0.type = arbotix_msgs/SetupChannel
  0.desc = Service to call to setup the raw analog stream for processing. Will use name, pin, and rate parameters defined below. 
}
param {
  0.name = ~name
  0.type = str
  0.desc = Name for raw analog reading topic.
  1.name = ~pin
  1.type = int
  1.desc = Analog IO pin to connect to.
  2.name = ~rate
  2.type = int
  2.desc = Rate to publish range message at.
  2.default = 10
  3.name = ~type
  3.type = str
  3.desc = Type of Sharp IR sensor being interfaced.
  3.default = GP2D12
}
```


