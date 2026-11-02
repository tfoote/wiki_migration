## Nodes

### neato_laser_publisher

`neato_laser_publisher` ROS wrapper for the `xv11_laser_driver`
library also available in this package.

#### Published Topics

- `scan`
  ([sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html)):
  Scan data from the laser. Under normal conditions, contains 360 pings
  at 1 degree increments.

#### Parameters

- `~port` (`string`, default: `/dev/ttyUSB0`): The device path
- `~baud_rate` (`int`, default: `115200`): The baud rate to receive
  laser data. Should not be changed from 115200 unless the laser's baud
  rate is changed (by a firmware upgrade, for example).
- `~firmware_version` (`int`, default: `1`): The firmware version that
  attempts to interpret the byte format of the laser. There are two
  known firmwares right now. One is noted for sending all 360 pings in a
  structure. This is probably the older firmware and is "1" for this
  value. The other sends the pings 4 at a time. This is probably the
  newer firmware and is "2" for this value. There isn't a reliable
  way to get the firmware version from the laser right now, so you'll
  have to set this and check a visualization of the pings in order to
  see if the driver is correctly interpreting the laser bytes.
- `~frame_id` (`string`, default: `neato_laser`): The laser data frame.
  This frame should be at the optical center of the laser, with the
  x-axis along the zero degree ray, and the y-axis along the pi/2 degree
  ray.

## Library

### XV11 Laser Driver

`xv11_laser_driver` is a C++ library for reading the data from the
XV11's laser and packing that data into a
[sensor_msgs/msg/LaserScan](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/LaserScan.html).
As a standalone library, it has no ROS API.

## Tutorials

- [Connecting the XV-11 Laser to USB](#connecting-the-xv-11-laser-to-usb):
  This tutorial will show you how to remove the XV-11 vacuum cleaner's
  built in laser and connect it as a stand alone laser scanner through
  USB.
- [Running the XV-11 Laser Node](#running-the-xv-11-laser-node):
  This tutorial will walk you through installing and running the XV-11
  Laser Node so that you get laser scans in rviz.
- [The Underlying XV-11 Protocol Explained](#the-underlying-xv-11-protocol-explained):
  This tutorial will walk you through one entire message sent from the
  XV-11 laser and will tell you exactly what gets output from the unit.
  This is an advanced tutorial for those interested in the raw data
  formatting. This is for the older firmware only.

## Connecting the XV-11 Laser to USB

- **Note:** This tutorial requires voiding your Neato XV-11's warranty
  and removing the laser from the robot. Your robot will not work
  without this laser present. For using the robot inside ROS, please
  see: [The Neato Robot Stack](neato_robot).
- **Description:** This tutorial will show you how to remove the XV-11
  vacuum cleaner's built in laser and connect it as a stand alone laser
  scanner through USB.
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Running the XV-11 Node](#running-the-xv-11-laser-node)

So you want to use the XV-11 laser without gluing the vacuum robot to
the top of your iRobot Create? This tutorial will show you how to remove
the laser and connect it using an FTDI serial to USB adapter while also
drawing power for the motor from USB as well.

### Removing the Laser from the Robot

!RobotShop.com has created a nice video explaining how to disassemble
the XV-11. You can stop following this walkthrough when you can remove
the four screws holding the laser in place. The approximate timestamp is
2:15.

[Youtube](https://www.youtube.com/watch?v=G8G72NAppKY)

Before you disconnect the wires, be sure you are statically grounded and
in a cat-free zone. You should now have the laser unit removed. It
should look like the following:

![width="50%"](doc/BewareCats.jpg) ![width="50%"](doc/LaserOnly.jpg)

### Understanding the Connections

The four wire plug is a 3.3V serial connection. The red wire requires
+3.3V and the black wire is ground. The Orange is "TX" or transmits
from the laser. The Brown is "RX" and receives for the laser, but does
not appear to be used since the laser begins outputting data as soon as
the motor is spinning at the appropriate speed. The electronics inside
the laser require approximately 120mA peak to operate.

  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <#cce0ff>**Note:** Brown is actually labeled "TX" and Orange is labeled "RX" on the PCB inside the laser. My best guess is that these are written in the Neato XV-11 frame instead of the laser frame, such that RX on the laser PCB goes to RX on the Neato's onboard computer.   
  -- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

![width="100%"](doc/DataConnector.jpg)

The two wire plug connects directly to the motor. The motor is typically
powered by 12V pulses at 25% duty cycle. This works out to a constant
potential of +3.0V from the red wire to ground. The motor requires
approximately 100mA peak at 3V to operate.

![width="100%"](doc/MotorConnector.jpg)

### An Example Connection to USB

Now that we know the connections that need to be made, we can set up the
unit so that it is entirely powered and interfaced to through USB.

**Parts List:**

- XV-11 Laser Unit
- Sparkfun FTDI Basic Breakout - 3.3V.
  <http://www.sparkfun.com/products/9873>
- A 3.0V Regulator
  <http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name=BA30BC0T-ND>
- A sacrificial USB mini cable.
- Connecting wire

We used a Sparkfun FTDI Basic Breakout 3.3V as our USB to serial
converter. This allows the laser to show up as a /dev/ttyUSB\* device
and be mapped using the FTDI udev rules. Unfortunately, this board does
not create enough power to run the electronics.

![width="100%"](doc/FTDIBasic.jpg)

You will need a 3.0V regulator for this project. 3.3V will spin the
motor too fast and the unit will not output data. We actually used the
[REG104FA-3](http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name=REG104FA-3TR-ND),
but I do not recommend this part as the surface mount pins are fragile,
easily broken, and this part has unnecessary features. The part listed
above should be fine for this project, but does require filter
capacitors.

Once you have gathered all of your pieces, you will need to carefully
remove the outer layer from your USB cable. Once you have the inner four
wires exposed, you need to tap into the +5V and Ground to create the
following connections:

![width="100%"](doc/RegulatorConnection.png)

  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
     <#cce0ff>**Note:** We have left off the diode to protect the laser from the inductive motor creating large spikes of voltage. You may want to use one to guarantee safety of your laser.   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

In this diagram, you can see that we've powered the laser from 3.0V
instead of 3.3V. This has worked fine in our application. Remember that
the motor needs 3.0V instead of 3.3V or it will spin too fast.

The RX pin of the FTDI adapter will be connected to the **Orange** wire.
The Brown wire does not appear to be necessary or used, and can be
ignored.

Once you have everything connected, be careful of shorting and test it
out. It may be a good idea to run this from a bench power supply before
plugging it into a computer.

Once you have verified that everything is working, you should have
something that looks like this and you can move on to the
[next tutorial](#running-the-xv-11-laser-node)!

![width="100%"](doc/FinalConnections.jpg)

### Additional USB Connection Option

[XV Lidar Controller by GetSurreal](http://www.getsurreal.com/product/xv-lidar-controller-v1-2)

![width="40%"](doc/XV_Lidar_Controller_v1.2.jpg)
![width="60%"](doc/XV_Lidar_Controller_with_Laser.jpg)

## Running the XV-11 Laser Node

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Connecting the XV-11 Laser to USB](#connecting-the-xv-11-laser-to-usb),
  [ROS Tutorials](ROS/Tutorials).
- **Description:** This tutorial will walk you through installing and
  running the XV-11 Laser Node so that you get laser scans in rviz.
- **Keywords:** xv11 xv-11 neato laser rviz udev ftdi
- **Tutorial Level:** BEGINNER

### Install the Driver

#### Install the Driver via apt-get

You can install the xv_11_laser_driver via command line:



```
$ sudo apt-get install ros-<distro>-xv-11-laser-driver
```

 Replace the <distro> with the ros distro you
installed. e.g. indigo, jade or kinetic

#### Build Driver from Source

Hydro and later releases of this driver use the catkin build system.
Groovy and earlier use rosbuild. Select the build system based on your
ros version.



```
{#!wiki buildsystem catkin
It is assumed you have created and initialized a catkin workspace as described in the "Create a ROS Workspace" section of [[ROS/Tutorials/InstallingandConfiguringROSEnvironment | this tutorial]]

Clone the source code from github and build it. Source the workspace environment.
{{{
cd catkin_ws/src
git clone https://github.com/rohbotics/xv_11_laser_driver.git
cd ..
catkin_make
source devel/setup.bash
```

 }}}} 

```
{#!wiki buildsystem rosbuild

We assume you have ros-cturtle-base and rosinstall installed.
 1. Install git (if you don't already have it installed). For example, on Ubuntu use
 {{{
sudo apt-get install git-core
```

 1. Use rosinstall
to get the code (replace "groovy" with "fuerte" or any earlier
distribution you're using) 

```
rosinstall ~/cwru-ros-pkg /opt/ros/groovy 'http://www.ros.org/wiki/xv_11_laser_driver/Tutorials/Running%20the%20XV-11%20Node?action=AttachFile&do=get&target=cwru-ros-pkg.rosinstall'
```

 1. Add cwru-ros-pkg
to your environment 

```
. ~/cwru-ros-pkg/setup.sh
```



1\. Build the driver 

```
rosmake --rosdep-install xv_11_laser_driver
```



If the above fails, try 

```
rosmake xv_11_laser_driver
rosdep install xv_11_laser_driver
```

 }}}}

### Setup udev for FTDI devices

  -- -------------------------------------------------------------------------------------------------------------------------------------------------- --
     <#cce0ff>**Note:** This is an optional step. You only need to complete it if you'd like your XV-11 laser to have a constant device identifier   
  -- -------------------------------------------------------------------------------------------------------------------------------------------------- --

Add the following to a new rule file in /etc/udev/rules.d. For example,
as `root`:



```
# echo 'SUBSYSTEMS=="usb", KERNEL=="ttyUSB[0-9]*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", SYMLINK+="sensors/ftdi_%s{serial}"' > /etc/udev/rules.d/52-ftdi.rules
```

 This will create devices in
/dev/sensors/ftdi_\* where \* is the serial number in a particular FTDI
USB-Serial chip's EEPROM. This will allow you to refer to the device
accurately even if you plug multiple /dev/ttyUSB\* devices in in
different orders.

### Startup the XV11 driver

In successive terminals that have had the cwru-ros-pkg environment setup
in them:

1\. Startup roscore 

```
roscore
```



1\. Startup the driver with the appropriate device path (I'm using
/dev/ttyUSB0 which assumes you didn't setup the udev rules and the
XV-11 laser was the first ttyUSB device you plugged into your computer)


```
rosrun xv_11_laser_driver neato_laser_publisher _port:=/dev/ttyUSB0
```



If you have a newer version of the Neato laser you need to start the
XV11 driver with the _firmware_version option:

. 

```
rosrun xv_11_laser_driver neato_laser_publisher _port:=/dev/ttyUSB0 _firmware_version:=2
```



The driver should now be running.

View the scan data using the following instructions, and if it doesn't
look right, try the other way of starting the driver.

### View the data in RVIZ

{} {} Have fun playing with your XV-11 Laser!

## The Underlying XV-11 Protocol Explained

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Running the XV-11 Node](#running-the-xv-11-laser-node).
- **Description:** This tutorial will walk you through one entire
  message sent from the XV-11 laser and will tell you exactly what gets
  output from the unit. This is an advanced tutorial for those
  interested in the raw data formatting. This is for the older firmware
  only.
- **Tutorial Level:** ADVANCED

An entire message consists of 1446 bytes. The format consists of:

- 4 header bytes
- 2 "speed" bytes
- 360 points \* 4 bytes = 1440 point bytes

### Header Format

The four header bytes are:



```
0xC0 0x00 0xA5 0x5A
```



Once these four bytes have been received in this order (0x5A followed by
0xA5, etc), you can be sure that this is the beginning of a new round of
pings.

### Speed Bytes

The next two bytes correspond to the rotational speed of the unit. It
appears that this is the approximate time between each ping \* 1e8. This
number is certainly used by the Neato to PID the motor speed. In our
experimentation, PIDing at such a slow rate (5Hz) did not produce
significant advantages, so we have dropped the required hardware and
software to do this.



```
0xD1 0xAA
```



This number is the two bytes combined as a uint16. The ideal value for
this is probably 1.0 second / (360 pings \* 5 Hz) \* 10\^8 = 55555. In
practice, I've seen values around 53674 in our unit. If the speed is
not close to this target number, due to friction or an obstacle blocking
rotation, the laser will not output meaningful pings.

### Ping Bytes

The next set of bytes consists of 4 bytes per ping for each of 360
pings. The pings start at 0 degrees and then rotate positively,
consistent with ROS frame.



```
0x00 0x06 0x10 0x87
```



The first two byte set (the 2 least significant 0x10 and 0x87) consists
of status bits (0 and 0) and the distance in millimeters (4231) the
laser returned.

The first status bit has appeared to be no return due to max range or no
reflectivity. This would appear in situations where an object has
absorbed the laser or the camera cannot find enough area to make a range
determination. A return of 0 is normal and a return of 1 seems to be the
max reading.

The second status bit has appeared to be that an object is too close.
Since the laser works by calculating laser area and intensity to provide
a distance estimate, this bit seems to indicate that the laser return is
at the edge of the camera as it kicks in at around 0.6m or less. A
return of 0 is normal and a return of 1 seems to be the close obstacle
condition.

The rest of the bits are then the return in millimeters, and the
approximate range of the laser appears to be from around 60mm through
5000mm.

The next two bytes we have used as the intensity values return with each
ping (in the example at 4.2m, only a value of 6 is returned). We have
confirmed that these generally go down with range and up with
reflectivity increases (off of a whiteboard, for instance). This value
is almost certainly brightness off the camera or the area of the laser
return on the camera. Most likely, it is a sum of brightness over the
area determined to be the laser return.
