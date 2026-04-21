## Overview

The range_sensor_layer is a plugin for the !LayeredCostmap in
[costmap_2d](costmap_2d), that uses the
<<MsgLink(sensor_msgs/Range)>> message. It is intended for use with
sonar and infrared data.

The Range messages are integrated into the costmap by using a
probabilistic model.

Cells with a probability higher than the mark_threshold are marked as
lethal obstacles in the master costmap. Cells with a probability lower
than the clear_threshold are marked as free space in the master costmap.

## API

```clearsilver
sub {
  0.name = "topics"
  0.type = sensor_msgs/Range
  0.desc = ranged sensor data
}
param {
  0.name = ns
  0.type = string
  0.default = ""
  0.desc = Namespace that is prepended to all topic names
  1.name = topics
  1.type = Array of strings
  1.default = ['/sonar']
  1.desc = List of Range topics to subscribe to
  2.name = no_readings_timeout
  2.type = double
  2.default = 0.0
  2.desc = If zero, this parameter has no effect. Otherwise if the layer does not receive sensor data for this amount of time, the layer will warn the user and the layer will be marked as not current.
  3.name = clear_threshold
  3.type = double
  3.default = .2
  3.desc = Cells with a probability lower than the clear_threshold are marked as free space in the master costmap.
  4.name = mark_threshold
  4.type = double
  4.default = .8
  4.desc = Cells with a probability higher than the mark_threshold are marked as lethal obstacles in the master costmap.
  5.name = clear_on_max_reading
  5.type = bool
  5.default = false
  5.desc = Whether to clear the sensor readings on max. range
}
```

## Usage

This layer can be used by adding the following values to the plugins
parameter in your costmap.

```
- {name: sonar,   type: "range_sensor_layer::RangeSensorLayer"}
```
