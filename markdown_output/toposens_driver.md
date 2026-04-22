## Overview

This package functions as a device driver for a Toposens 3D ultrasonic
sensor. It can be used to setup a serial connection to the sensor, parse
the received data string and publish it as a
[toposens_msgs/msg/TsScan](https://docs.ros.org/en/rolling/p/toposens_msgs/msg/TsScan.html).

## ROS Nodes



```clearsilver
name = ts_driver_node
desc = translates the raw datastream of a Toposens 3D ultrasonic sensor into messages of type <<MsgLink(toposens_msgs/TsScan)>>
pub {
  0.name = ts_scans
  0.type = toposens_msgs/TsScan
  0.desc = The messages are published with the same rate the data is received through the serial port.
}
param {

  0.name = ~port
  0.type = std_msgs/String
  0.desc = terminal ID that the sensor is connected to (e.g. ttyUSB0)
  1.name = ~frame_id
  1.type = std_msgs/String
  1.desc = frame ID in which the data is published
  2.name = ~echo_rejection_threshold
  2.type = int
  2.desc = minimum amplitude for an echo to be considered valid (sent to sensor)
  3.name = ~noise_indicator_threshold
  3.type = int
  3.desc = normalized noise level on ADC signals to mark processed points as noisy (sent to sensor)
  4.name = ~num_pulses
  4.type = int
  4.desc = number of ultrasonic pulses emitted in every transmission cycle (sent to sensor)
  5.name = ~peak_detection_window
  5.type = int
  5.desc = kernel size applied on ADC signals for peak detection (sent to sensor)
  6.name = ~external_temperature
  6.type = double
  6.desc = temperature value used to calibrate speed-of-sound (only used if use_external_temperature == true) (sent to sensor)
  7.name = ~use_external_temperature
  7.type = bool
  7.desc = if true uses external_temperature to calibrate speed-of-sound, otherwise uses value provided by on-board temperature sensor
```

 Most of the parameters are used by the sensors
firmware and are therefore sent to the sensor via the serial port. For a
more detailed description of these parameters see
[this tutorial](toposens/Tutorials/Getting Started with the TS3).
