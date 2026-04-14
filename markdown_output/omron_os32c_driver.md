![\|align=right,width=240](attachment:os32c.jpg)

## Overview

This package provides a driver for the OMRON OS32C EtherNet/IP based
safety laser. You can learn more about this device on the
manufacturer\'s website:

<https://www.ia.omron.com/products/family/2717/>

The primary resource used in developing this driver was the
[OS32C with EtherNet/IP & Measurement Data Addendum](http://downloads.omron.ca/IAB/Products/Safety/Programmable%20safety%20system/Standalone%20safety%20controllers/OS32C/Z336/OS32C-DM_UsersManual_en_201404_Z336-E1-05.pdf).

## Nodes

```clearsilver
node.0 {
 name = omron_os32c_driver
 desc = Standalone driver node that publishes the laserscan with diagnostics information.
 pub {
  0.name = scan
  0.type = sensor_msgs/LaserScan
  0.desc = Scans output from the device at specified frequency.
 }
 param {
  0.name = ~host
  0.type = string
  0.desc = IP address to find device at.
  0.default = 192.168.1.1
  1.name = ~local_ip
  1.type = string
  1.desc = IP adress where the device sends its data to. Enables using multiple scanners at the same time when specifying different ~local_ip parameters.
  1.default = 0.0.0.0
  2.name = ~frame_id
  2.type = string
  2.desc = The header frame_id of the published laser scan message
  2.default = laser
  3.name = ~start_angle
  3.type = double
  3.desc = Start angle
  3.default = OS32C::ANGLE_MAX
  4.name = ~end_angle
  4.type = double
  4.desc = End angle
  4.default = OS32C::ANGLE_MIN
  5.name = ~frequency
  5.type = double
  5.desc = Poll frequency
  5.default = 12.856
  6.name = ~expected_frequency
  6.type = double
  6.desc = Expected frequency
  6.default = frequency
  7.name = ~frequency_tolerance
  7.type = double
  7.desc = Tolerance on frequency for diagnosed publisher
  7.default = 0.1
  8.name = ~timestamp_min_acceptable
  8.type = double
  8.desc = Min acceptable timestamp for diagnosed publisher
  8.default = -1
  9.name = ~timestamp_max_acceptable
  9.type = double
  9.desc = Max acceptable timestamp for diagnosed publisher
  9.default = -1
  10.name = ~reconnect_timeout
  10.type = double
  10.desc = How long before we try a reconnecting to the device
  10.default = 2.0
  11.name = ~publish_intensities
  11.type = bool
  11.desc = Whether the intensities are filled in the output scan msg
  11.default = false
 }
}
```
