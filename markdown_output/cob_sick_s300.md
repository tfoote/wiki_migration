## ROS API

The [cob_sick_s300](cob_sick_s300) package provides two configurable
nodes for operating with the scanners. ```clearsilver
 name = cob_sick_s300
 desc = The `cob_sick_s300` node takes in <<MsgLink(sensor_msgs/LaserScan)>> messages and send this directly to the hardware.


pub{
 0.name = scan
 0.type = sensor_msgs/LaserScan
 0.desc = Publishes the single scan from a planar laser range-finder.
 1.name = scan_standby
 1.type = std_msgs/Bool
 1.desc = Whether this scanner is in standby mode.
 2.name = /diagnostics
 2.type = diagnostic_msgs/DiagnosticArray
 2.desc = Publishes ROS diagnostics for this driver.

}

param{
 0.name = port
 0.type = string
 0.default = "/dev/ttyUSB0"
 0.desc = Device address of can module, e.g. /dev/ttyScan1...
 1.name = baud
 1.type = int
 1.default = 500000
 1.desc = Baudrate: for most setups 500000
 2.name = scan_duration
 2.type = int
 2.default = 0.025
 2.desc = How long one actual scan takes (without the internal calibration procedure)
 3.name = scan_cycle_time
 3.type = int
 3.default = 0.040
 3.desc = How long the one turn of the scan takes (usually 0.040 seconds)
 4.name = inverted
 4.type = boolean
 4.default = false
 4.desc = Wether the scanner is mounted upside down or not. NOTE: this flag turns the output of the scanner, so you don't need to turn the frame upside down.
 5.name = scan_id
 5.type = int
 5.default = 7
 5.desc = Scan_id for Guest/Host-Setups. ID for Guest is 8, for Host 7, for regular setups always 7.
 6.name = frame_id
 6.type = string
 6.default = "/base_laser_link"
 6.desc = name of the link of the scanner in the robot_description
 7.name = publish_frequency
 7.type = int
 7.default = 12
 7.desc = Frequency [Hz] of the published scan
}
```

```clearsilver
 name = cob_scan_filter
 desc = The `cob_scan_filter` node takes <<MsgLink(sensor_msgs/LaserScan)>> messages and sends a filtered copy of it to the hardware.

pub{
 0.name = scan_out
 0.type = sensor_msgs/LaserScan
 0.desc = Publishes the filtered scan message.
}

sub{
 0.name = scan_in
 0.type = sensor_msgs/LaserScan
 0.desc = Receives the scan message.
}

param{
 0.name = scan_intervals
 0.type = list of scan intervals
 0.default = Required
 0.desc = these intervals are included to the scan
}
```

## Usage/Examples

This package is not intended to be used directly, but with the
corresponding launch and yaml files from e.g. [cob_bringup](cob_bringup)
in the [cob_robots](cob_robots) stack. For starting use:
```
roslaunch cob_bringup laser_front.launch
roslaunch cob_bringup laser_rear.launch
``` For including in your overall launch file use
```
<include file="$(find cob_bringup)/components/laser_front.launch" />
<include file="$(find cob_bringup)/components/laser_rear.launch" />
``` All hardware configuration is done in the
[cob_hardware_config](cob_hardware_config) package. A sample parameter
file in \"cob_hardware_config/cob3-3/config/laser_front.yaml\" could
look like this ```
port: /dev/ttyScan1
baud: 500000
scan_duration: 0.025 #no info about that in SICK-docu, but 0.025 is believable and looks good in rviz
scan_cycle_time: 0.040 #SICK-docu says S300 scans every 40ms
inverted: true
scan_id: 7
frame_id: /base_laser_front_link
scan_intervals: [[-1.3526, 1.361357]] #[rad] these intervals are included to the scan
```
