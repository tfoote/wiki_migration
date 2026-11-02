## ROS API

The cob_sick_s300 package provides two
configurable nodes for operating with the scanners.

### cob_sick_s300

The `cob_sick_s300` node takes in
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages and send this directly to the hardware.

#### Published Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Publishes the single scan from a planar laser range-finder.
- `scan_standby`
  ([std_msgs/msg/Bool](https://docs.ros.org/en/rolling/p/std_msgs/msg/Bool.html)):
  Whether this scanner is in standby mode.
- `/diagnostics`
  ([diagnostic_msgs/msg/DiagnosticArray](https://docs.ros.org/en/rolling/p/diagnostic_msgs/msg/DiagnosticArray.html)):
  Publishes ROS diagnostics for this driver.

#### Parameters

- `port` (`string`, default: `"/dev/ttyUSB0"`): Device address of can
  module, e.g. /dev/ttyScan1\...
- `baud` (`int`, default: `500000`): Baudrate: for most setups 500000
- `scan_duration` (`int`, default: `0.025`): How long one actual scan
  takes (without the internal calibration procedure)
- `scan_cycle_time` (`int`, default: `0.040`): How long the one turn of
  the scan takes (usually 0.040 seconds)
- `inverted` (`boolean`, default: `false`): Wether the scanner is
  mounted upside down or not. NOTE: this flag turns the output of the
  scanner, so you don't need to turn the frame upside down.
- `scan_id` (`int`, default: `7`): Scan_id for Guest/Host-Setups. ID for
  Guest is 8, for Host 7, for regular setups always 7.
- `frame_id` (`string`, default: `"/base_laser_link"`): name of the link
  of the scanner in the robot_description
- `publish_frequency` (`int`, default: `12`): Frequency \[Hz\] of the
  published scan

### cob_scan_filter

The `cob_scan_filter` node takes
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)
messages and sends a filtered copy of it to the hardware.

#### Subscribed Topics

- `scan_in`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Receives the scan message.

#### Published Topics

- `scan_out`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Publishes the filtered scan message.

#### Parameters

- `scan_intervals` (`list of scan intervals`, default: `Required`):
  these intervals are included to the scan

## Usage/Examples

This package is not intended to be used directly, but with the
corresponding launch and yaml files from e.g.
[cob_bringup](https://index.ros.org/p/cob_bringup) in the
[cob_robots](https://index.ros.org/p/cob_robots) stack. For starting
use: 

```
roslaunch cob_bringup laser_front.launch
roslaunch cob_bringup laser_rear.launch
```

 For including in your overall launch file
use 

```
<include file="$(find cob_bringup)/components/laser_front.launch" />
<include file="$(find cob_bringup)/components/laser_rear.launch" />
```

 All hardware configuration is done in the
[cob_hardware_config](https://index.ros.org/p/cob_hardware_config)
package. A sample parameter file in
"cob_hardware_config/cob3-3/config/laser_front.yaml" could look like
this 

```
port: /dev/ttyScan1
baud: 500000
scan_duration: 0.025 #no info about that in SICK-docu, but 0.025 is believable and looks good in rviz
scan_cycle_time: 0.040 #SICK-docu says S300 scans every 40ms
inverted: true
scan_id: 7
frame_id: /base_laser_front_link
scan_intervals: [[-1.3526, 1.361357]] #[rad] these intervals are included to the scan
```
