## Documentation



```clearsilver
name = tracker.py
desc = 
sub { 
  0.name = people_tracker_measurements
  0.type = people_msgs/PositionMeasurementArray
  0.desc = Positions of people
}
pub {
  0.name = /people
  0.type = people_msgs/People
  0.desc = Positions and velocities of people
  1.name = /visualization_marker
  1.type = visualization_msgs/Marker
  1.desc = Markers
}
param { 
  0.name = timeout
  0.type = double
  0.desc = Stop tracking velocities if no message for this many seconds
  0.default = 1.0
}
```





```clearsilver
name = static.py
desc = Publishes a People message repeatedly, with one person at the position/velocity specified by four command line arguments. (pos_x, pos_y, vel_x, vel_y)
pub {
  0.name = /people
  0.type = people_msgs/People
  0.desc = Positions and velocities of people
}
```
