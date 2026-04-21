## Description

Driver for ROS to read the scan data from the device SICK S3000. This
driver is based on the original driver developed for Player/Stage by
Brian Gerkey, Kasper Stoy, Richard Vaughan, & Andrew Howard.

This driver controls the SICK S3000 safety laser scanner interpreting
its data output. The driver is very basic and assumes the S3000 has
already been configured to continuously output its measured data on the
RS422 data lines.

## Supported Hardware

This package should work with SICK S3000 safety laser scanners.

![SICK S3000\|width="250px"](attachment:SICK_S3000.jpg)

## Nodes

```clearsilver
node.0 {
 name = s3000_laser
 desc = S3000 laser driver.
 param {
  0.name= ~port
  0.type= string
  0.desc= Serial port.
  0.default= "/dev/ttyUSB0"
  1.name= ~frame_id
  1.type= string
  1.desc= Relative frame for the publication of the laser measures.
  1.default= "/laser"
  2.name= ~baud_rate
  2.type= int
  2.desc= Serial port baudrate (options: 9600, 19200, 38400, 115200, 500000).
  2.default= 500000
  3.name= ~serial_parity
  3.type= string
  3.desc= Serial port parity (options: "even", "odd", "none").
  3.default= "none"
  4.name= ~serial_datasize
  4.type= int
  4.desc= Character size mask for serial link (options: 5,6,7,8).
  4.default= 8
  5.name= ~range_min
  5.type= float
  5.desc= Min valid range (m) for S3000 data produced.
  5.default= 0m
  6.name= ~range_max
  6.type= float
  6.desc= Max valid range (m) for S3000 data.
  6.default= 40m
 }
 pub {
  0.name= s3000_laser/scan
  0.type= sensor_msgs/LaserScan
  0.desc= Scan data from the laser, containing either range data or reflector detections.
 }
}
```
