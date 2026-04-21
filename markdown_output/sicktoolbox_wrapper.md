![](attachment:sicktoolbox/sick.JPG)

## Supported Hardware

This package should work with Sick LMS 2xx and Sick LD laser range
finders.

## API Stability

The ROS API of this node should be considered stable.

## Nodes



```clearsilver
node.0 {
name=sicklms
desc=`sicklms` is a ROS wrapper for the `lms_config` driver provided by the [[sicktoolbox]] package.
pub{
0.name= scan
0.type= sensor_msgs/LaserScan
0.desc= Scan data from the laser.
}
param {
0.name= ~use_rep_117
0.default= true
0.type= bool
0.desc= Whether or not to use REP 117 output parameters.  See http://ros.org/wiki/rep_117/migration for more information.  This parameter was default to false in Fuerte; the default was now true for Groovy.  This parameter was removed for the Hydromedusa release.
1.name= ~port
1.default=`/dev/lms200`
1.type= string
1.desc= The device path.
2.name= ~baud
2.default=38400
2.type= int
2.desc= The baud rate to receive laser data.
3.name= ~inverted
3.default=`false`
3.type= bool
3.desc= Inverts the sign convention for angles. I.e., swaps min_angle and max_angle, and inverts angle_increment in the <<MsgLink(sensor_msgs/LaserScan)>> message. See the message definition for details of the angle convention.
4.name= ~frame_id
4.default=`laser`
4.type= string
4.desc= The laser data frame. This frame should be at the optical center of the laser, with the x-axis along the zero degree ray, and the y-axis along the pi/2 degree ray. (If ~inverted is true then the y-axis is along the -pi/2 ray.)
5.name= ~angle
5.default=0
5.type= int
5.desc= The angular range of the scan. The default value of zero uses the range returned by the laser. (New in version 1.1.0)
6.name= ~resolution
6.default=0.0
6.type=double
6.desc= The angular resolution of the scan. The default value of zero uses the resolution returned by the laser. (New in version 1.1.0)
7.name= ~connect_delay
7.default=0.0
7.type=double
7.desc= How long to wait between opening the serial port and connecting to the laser.  This is specifically for the Pioneer, where opening the serial port turns on the power to the laser, so you need roughly a 30 second delay between these two events.
}
}
node.1 {
name=sickld
desc=`sickld` is a ROS wrapper for the `ld_config` driver provided by the [[sicktoolbox]] package.
pub{
0.name= scan
0.type= sensor_msgs/LaserScan
0.desc= Scan data from the laser.
}
param {
0.name= ~port
0.default=`49152`
0.type= int
0.desc= The device TCP port.
1.name= ~ipaddress
1.default=192.168.1.10
1.type= string
1.desc= Sick LD INet 4 address.
2.name= ~inverted
2.default=`false`
2.type= bool
2.desc= Inverts the sign convention for angles. I.e., swaps min_angle and max_angle, and inverts angle_increment in the <<MsgLink(sensor_msgs/LaserScan)>> message. See the message definition for details of the angle convention.
3.name= ~frame_id
3.default=`laser`
3.type= string
3.desc= The laser data frame. This frame should be at the optical center of the laser, with the x-axis along the zero degree ray, and the y-axis along the pi/2 degree ray. (If ~inverted is true then the y-axis is along the -pi/2 ray.)
4.name= ~timer_smoothing_factor
4.default=0.97
4.type= double
4.desc= The driver has an in-build complimentary filter to help get better timing information. The smoothing factor helps smooth the time stamps.
5.name= ~timer_error_threshold
5.default=0.5
5.type=double
5.desc= If the timestamp drifts by more than the error threshold, then the smoothed timestamps are reset.
6.name= ~resolution
6.default=1.0
6.type=double
6.desc= The angular resolution between scan points.
7.name= ~start_angle
7.default=0
7.type=double
7.desc= The angle to start scanning.
8.name= ~stop_angle
8.default=300
8.type=double
8.desc= The angle to stop scanning.
9.name= ~scan_rate
9.default=10
9.type=double
9.desc= The rate in Hz to scan.
}
}
```


