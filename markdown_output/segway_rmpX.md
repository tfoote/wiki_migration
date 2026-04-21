![](attachment:rmps.png)

## Supported Hardware

This package provides support for the RMP50, RMP100, and RMP200 Segway
mobile bases. For RMP400 support: [segway_rmp400](segway_rmp400)
**Coming Soon**.

## API Stability

The ROS API of this driver should be considered experimental.

## Theory of Operation

The segway_rmp_node will allow you connect to and control your Segway
RMP series mobile robot platform. On startup the node will announce how
it is trying to connect to the Segway RMP with a message similar to
this:

```
Connecting to Segway RMP via serial on serial port: /dev/ttyUSB0
``` or ```
Connecting to Segway RMP via usb identified by the device serial number: 00000056
```

If the node is unsuccessful in connecting to the Segway RMP or at any
point looses connection to the Segway RMP, it will report the error and
try to connect again in 5 seconds. The node is designed this way to make
it more robust to temporary E-Stopping of the vehicle.

This package supports two main ways to communicate with the Segway RMP,
both happen via the USB cable coming out of the Segway RMP. The
difference between communication methods is based on the driver you use
in the operating system. FTDI supplies two kind of drivers for this kind
of device, VCP and D2XX. The VCP (Virtual COM Port) driver allows the
device to show up as a normal serial port in the OS. The D2XX driver
allows you to directly communicate to the Segway RMP using the USB
protocol. In Linux the default driver is the VCP, and in fact you have
to disable the VCP driver for **all** FTDI devices on the system in
order to use the D2XX to communicate with the Segway RMP. This is the
main reason both VCP and D2XX (usb) support is supported in this
package.

## ROS API

```clearsilver
node.0 {
name=segway_rmp_node
desc=`segway_rmp_node` is a driver for the RMP50, RMP100, and RMP200 series of Segway's Robotic Mobile Platforms.  Currently these drivers only support using the mobile bases in "Tractor" mode (with a caster).  Support for "Balance" mode with these robots is unsupported because the maintainer cannot test the driver.  If you would like to volunteer to test code that would allow for balance mode, [[mailto:wjwwood@gmail.com|email me]].

pub{
0.name= segway_status
0.type= segway_rmpX/SegwayStatusStamped
0.desc= Data from the segway.
1.name= odom
1.type= geometry_msgs/Odometry
1.desc= Integrated Odometry of the mobile base.
}
sub {
0.name= cmd_vel
0.type= geometry_msgs/Twist
0.desc= This is the canonical method for commanding mobile bases in ROS.  The two components of this msg used by the segway_rmp_node are the linear/x and angular/z velocities in meters/second and radians/second respectively.  
}
param {
group.0 {
name= Common Parameters
desc= These parameters always apply, no matter what interface you are using to communicate with the Segway RMP.
0.name= interface_type
0.default= serial
0.type= string
0.desc= This allows you to indicate which interface you would like to use for communicating with the Segway RMP.  The default value is 'serial' (VCP), but you may also put 'usb' to interface via the ftd2xx library.
1.name= motor_timeout
1.default= 0.5
1.type= double
1.desc= This allows you set a timeout on the movement of the Segway RMP.  If a cmd_vel is not received every 'motor_timeout' seconds, then the Segway RMP is stopped.
2.name= frame_id
2.default= base_link
2.type= string
2.desc= This is the frame_id used when publishing the odometry msg.
3.name= invert_linear_vel_cmds
3.default= false
3.type= bool
3.desc= If this is true then all incoming cmd_vel's will have their linear (x) components inverted.
4.name= invert_angular_vel_cmds
4.default= false
4.type= bool
4.desc= If this is true then all incoming cmd_vel's will have their angualr (z) components inverted.
5.name= boadcast_tf
5.default= true
5.type= bool
5.desc= If true then the node will provide the odom -> 'frame_id' transform.
6.name= rmp_type
6.default= 200/400
6.type= string
6.desc= This allows you to specify the model of RMP you are using.  The possible values here are '200/400' and '50/100'.
7.name= linear_pos_accel_limit
7.default= 0.0
7.type= double
7.desc= Software controlled maximum possible positive linear acceleration (m/s^2). A value of 0.0 implies no limit.
8.name= linear_neg_accel_limit
8.default= 0.0
8.type= double
8.desc= Software controlled maximum possible negative linear acceleration (m/s^2). A value of 0.0 implies no limit.
9.name= angular_pos_accel_limit
9.default= 0.0
9.type= double
9.desc= Software controlled maximum possible positive angular acceleration(degrees/s^2). A value of 0.0 implies no limit.
10.name= angular_neg_accel_limit
10.default= 0.0
10.type= double
10.desc= Software controlled maximum possible negative angular acceleration (degrees/s^2). A value of 0.0 implies no limit.
}
group.1 {
name= Serial Interface Parameters
desc= These parameters only apply if you are using the VCP interface for communicating with the Segway RMP. (You put 'serial' for the 'interface_type' parameter.)
0.name= serial_port
0.default=/dev/ttyUSB0
0.type= string
0.desc= This is the serial port name to which the node will try to connect.
}
group.2 {
name= USB Interface Parameters
desc= These parameters only apply if you are using the USB interface for communicating with the Segway RMP. (You put 'serial' for the 'interface_type' parameter.) There are three ways to select which USB device you want to connect to: index, serial number, or description.
0.name= usb_selector
0.default= index
0.type= string
0.desc= This allows you to specify a method for describing the USB device you want to connect to the Segway RMP through.  Possible options are 'index', 'serial_number', and 'description'.
1.name= usb_index
1.default= 0
1.type= int
1.desc= Device index to use when connecting through USB. Only used if the 'usb_selector' parameter is set to 'index'.
2.name= usb_serial_number
2.default= 00000000
2.type= string
2.desc= USB device serial number to use when connecting through USB. Only used if the 'usb_selector' parameter is set to 'serial_number'.  It is a string because there _must_ be eight numbers to make a serial number.  Example: '00000056' (this is my segway rmp200's serial)
3.name= usb_description
3.default= Robotic Mobile Platform
3.type= string
3.desc= USB description to use when connecting through USB. Only used if the 'usb_selector' parameter is set to 'description'.
}
}
}
```
