## Nodes

```clearsilver
node.0 {
 name = neato_laser_publisher
 desc = `neato_laser_publisher` ROS wrapper for the `xv11_laser_driver` library also available in this package.
 pub{
  0.name= scan
  0.type= sensor_msgs/LaserScan
  0.desc= Scan data from the laser. Under normal conditions, contains 360 pings at 1 degree increments.
  }
 param {
  0.name = ~port
  0.default = /dev/ttyUSB0
  0.type = string
  0.desc = The device path
  1.name = ~baud_rate
  1.default = 115200
  1.type = int
  1.desc = The baud rate to receive laser data. Should not be changed from 115200 unless the laser's baud rate is changed (by a firmware upgrade, for example).
  2.name = ~firmware_version
  2.default = 1
  2.type = int
  2.desc = The firmware version that attempts to interpret the byte format of the laser.  There are two known firmwares right now.  One is noted for sending all 360 pings in a structure.  This is probably the older firmware and is "1" for this value.  The other sends the pings 4 at a time.  This is probably the newer firmware and is "2" for this value. There isn't a reliable way to get the firmware version from the laser right now, so you'll have to set this and check a visualization of the pings in order to see if the driver is correctly interpreting the laser bytes.
  3.name = ~frame_id
  3.default = neato_laser
  3.type = string
  3.desc = The laser data frame. This frame should be at the optical center of the laser, with the x-axis along the zero degree ray, and the y-axis along the pi/2 degree ray.
  }
```

## Library

### XV11 Laser Driver

`xv11_laser_driver` is a C++ library for reading the data from the
XV11's laser and packing that data into a
<<MsgLink(sensor_msgs/LaserScan)>>. As a standalone library, it has
no ROS API.
