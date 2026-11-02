## Documentation

### tracker.py

#### Subscribed Topics

- `people_tracker_measurements`
  ([people_msgs/msg/PositionMeasurementArray](https://docs.ros.org/en/rolling/p/people_msgs/msg/PositionMeasurementArray.html)):
  Positions of people

#### Published Topics

- `/people`
  ([people_msgs/msg/People](https://docs.ros.org/en/rolling/p/people_msgs/msg/People.html)):
  Positions and velocities of people
- `/visualization_marker`
  ([visualization_msgs/msg/Marker](https://docs.ros.org/en/rolling/p/visualization_msgs/msg/Marker.html)):
  Markers

#### Parameters

- `timeout` (`double`, default: `1.0`): Stop tracking velocities if no
  message for this many seconds

### static.py

Publishes a People message repeatedly, with one person at the
position/velocity specified by four command line arguments. (pos_x,
pos_y, vel_x, vel_y)

#### Published Topics

- `/people`
  ([people_msgs/msg/People](https://docs.ros.org/en/rolling/p/people_msgs/msg/People.html)):
  Positions and velocities of people
