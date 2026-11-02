## Supported Hardware

Currently only the following Willow Garage hardware is supported:

### WG005

These are the main motor controller boards used in the PR2. Each board
has the following features:

- 1 quadrature incremental encoder input
- 1 limit-switch input (with on-board latching of encoder position at
  time of rising and falling edges)
- 1 digital output, used as to synchronize camera exposures with the
  realtime loop
- Closed-loop current control for 1 brushed DC motor up to 3A

### WG006

This motor controller board is used in the gripper on the PR2. Each
board has the following features:

- Same as the WG005, but with a current limit of 0.5A
- Additional LED to be used for finding position of hand in camera
  images
- 3-axis accelerometer with 3khz update
- Support for 2 SPI ports (compatible with 22-element tactile sensors
  for fingertips)

### WG014

- 6-port EtherCAT hub

### WG021

- Support for driving LED projector at 30hz, synchronized with motion
  control and camera exposures

## ROS API

<a id="NodeApi"></a> 

```clearsilver
node.0 {
name=ethercat_hardware
desc=`ethercat_hardware` is a driver for the EtherCAT motor controller boards (MCBs).  The driver handles all initialization, communication, and diagnostic reporting for the MCBs.  The driver currently supports four board types (WG005, WG006, WG014, and WG021)

pub{
0.name= diagnostics
0.type= diagnostic_msgs/DiagnosticStatus
0.desc= Diagnostic status information.
1.name= accelerometer
1.type= pr2_msgs/AccelerometerState
1.desc= Accelerometer data from a WG006 board (gripper)
2.name= pressure
2.type= pr2_msgs/PressureState
2.desc= Fingertip pressure sensor data from a WG006 board (gripper)
3.name= motors_halted
3.type= std_msgs/Bool
3.desc= A boolean value indicating if the motors have been halted
}
}
```



## Command-line Tools

The `ethercat_hardware` package's primary purpose is to provide a
library for communicating with motor controller boards. However, the
package does provide the
[motorconf](#motorconf) command-line tool
for configuring these boards. In practice, this tool is used during
robot assembly, and should not be needed after initial bring-up of the
robot. **NOTE: improper use of this tool could lead to hardware damage,
`motorconf` usage is limited to system administrators only.**

<a id="motorconf"></a>

### motorconf

`motorconf` Display the current configuration of motor controller
boards, and allow boards to be programmed with new configuration
information.



```
Usage: ./motorconf [options]
 -i, --interface <i>    Use the network interface <i>
 -a, --actuators <file> Get the actuator definitions from file (default: actuators.conf)
 -d, --device <d>       Select the device to program
 -b, --board <b>        Set the expected board type (wg005, wg006, wg021)
 -p, --program          Program a motor control board
 -n, --name <n>         Set the name of the motor control board to <n>
 -m, --motor <m>        Set the configuration for motor <m>
 -h, --help             Print this message and exit
```



When running motorconf, you must specify the interface used to
communicate with the EtherCAT devices. Without any additional arguments,
`motorconf` will enumerate all of the EtherCAT devices it can find.



```
# ./motorconf -i ecat0

[DEBUG] 1263333387.377268000: Device #00: WG014 (0x67d616)
[DEBUG] 1263333387.419128000: Device #01: WG014 (0x67d616)
[DEBUG] 1263333387.462366000: Device #02: WG05 (0x67d60d) Firmware Revision 1.20, PCB Revision F.02, Serial #: 1399
[DEBUG] 1263333387.463359000:             Serial #: 01399
[DEBUG] 1263333387.465986000:             Name: br_caster_r_wheel_motor
[DEBUG] 1263333387.509329000: Device #03: WG05 (0x67d60d) Firmware Revision 1.20, PCB Revision F.02, Serial #: 1414
[DEBUG] 1263333387.510322000:             Serial #: 01414
[DEBUG] 1263333387.512832000:             Name: br_caster_l_wheel_motor
 .
 . 
 .
[DEBUG] 1263333388.293608000: Device #20: WG05 (0x67d60d) Firmware Revision 1.20, PCB Revision F.02, Serial #: 1695
[DEBUG] 1263333388.294604000:             Serial #: 01695
[DEBUG] 1263333388.297113000:             Name: laser_tilt_mount_motor
```



In order to program an unconfigured device, or re-program a device, you
must specify a name, motor type, and board type for this motor. If the
name given (using the `-n` option) matches one of the names in the
actuators configuration file (`actuators.conf`, by default), then the
motor type and board type will be selected automatically. The motor type
can be specified explicitly with the `-m` option, and the board type
can be specified with the `-b` option. A list of valid actuator names
and motor types can be found with the `-h` option. In addition to the
name, motor, and board types, `motorconf` needs to know which device
in the EtherCAT chain to program. The device number is specified with
the `-d` option. Finally, the `-p` option tells `motorconf` to
actually program the board. The following example programs device #2 to
be the `br_caster_r_wheel_motor`: 

```
./motorconf -i ecat0 -n br_caster_r_wheel_motor -d 2 -p
```



`motorconf` will respond with: 

```
[ INFO] 1263334127.577301000: Programming device 2, to be named: br_caster_r_wheel_motor
```



#### actuators.conf

actuators.conf is an XML file that specifies the motor parameters and
common motor names to be programmed into the motor controller boards.
The file consists of a single <configuration> section. The
<configuration> section contains two subsections: <motors> and
<actuators>.

The <motors> subsection contains a series of <motor> definitions.
Each motor requires a *name* attribute. The <motor> also requires
child elements <params> and <encoder>. The <params> element
contains the following attributes:

- Make
- Model
- Maximum current
- Speed constant
- Resistance
- Motor Torque Constant The <encoder> element contains the following
  attributes:
- Pulses per Revolution
- Reduction

For example, this element specifies the Maxon RE40 motor used in PR2's
elbow, shoulder and spine: 

```
<!-- Elbow, shoulder, spine -->
  <!-- http://pr.willowgarage.com/wiki/HardwareComponents/Motors?action=AttachFile&do=get&target=maxonRE40.pdf -->
  <motor name="148877">
    <params make="Maxon"
            model="148877"
            max_current="3.12"
            speed_constant="158"
            resistance="1.16"
            motor_torque_constant="0.0603" />
    <encoder pulses_per_revolution="1200" reduction="-1"/>
  </motor>
```



The <actuators> subsection contains a series of <actuator>
definitions. An <actuator> has the following attributes:

- Name
- Motor
- Board For example, the following <actuator> definition states that
  the *l_elbow_flex_motor* should be configured with the motor
  parameters specified in the previous example: 

```
<actuator name="l_elbow_flex_motor" motor="148877" board="wg005"/>
```

## Tutorials

- [Changing the packet timeout and number of process data retries for pr2_etherCAT](#changing-the-packet-timeout-and-number-of-process-data-retries-for-pr2_ethercat):
  Changing the packet timeout and retries for pr2_etherCAT
- [Setting up communication with a new EtherCAT device](#setting-up-communication-with-a-new-ethercat-device):
  Second part of tutorial. Shows how to setup process communication with
  new device.
- [Using the 3-axis accelerometer on the PR2 gripper](#using-the-3-axis-accelerometer-on-the-pr2-gripper):
  Introduction to the 3-axis accelerometer on the PR2 gripper
- [Writing a controller for the gripper accelerometer.](#writing-a-controller-for-the-gripper-accelerometer):
  Writing a real-time controller for the gripper accelerometer.
- [Integrating a new type of EtherCAT device with ROS.](#integrating-a-new-type-of-ethercat-device-with-ros):
  First part of tutorial. Provides minimal code needed to get
  pr2_etherCAT to recognize a new type of device.
- [Understanding the motor model](#understanding-the-motor-model):
  Understanding motor model checks, and motor trace.
- [Using Force/Torque sensor with WG035 and pr2_etherCAT](#using-forcetorque-sensor-with-wg035-and-pr2_ethercat):
  Using Force/Torque sensor with WG035 and pr2_etherCAT

## Troubleshooting

### Errors when using motorconf

#### Error: Unable to locate any slaves



```
root@prXX:/ros/ros-pkg/drivers/motor/ethercat_hardware# ./motorconf -i ecat0

 Unable to locate any slaves
```

 **Solution:** Check the following things:

- Are you on a machine connected MCBs? On most robots this is machine 1,
  prX1.

<!-- -->

- Is the interface up? In this example the interface is ecat0.
  

```
sudo ifconfig ecat0 up
```



#### Error: No default motor for this name



```
root@prXX:/ros/ros-pkg/drivers/motor/ethercat_hardware# ./motorconf -i ecat0 -p -n actuator_name -d 0

 [ INFO] 1236963380.428284000: Device #02: WG05 (0x67d60d) Firmware Revision 1.08, PCB Revision B.02
 [ INFO] 1236963380.429241000:             Serial #: 01070
 [ INFO] 1236963380.431508000:             Name: fr_caster_l_wheel_motor
 [ INFO] 1236963380.475175000: Device #03: WG05 (0x67d60d) Firmware Revision 1.08, PCB Revision B.02
 [ INFO] 1236963380.476185000:             Serial #: 01101
 [ INFO] 1236963380.478312000:             Name: fr_caster_r_wheel_motor
 [ INFO] 1236963380.522127000: Device #04: WG05 (0x67d60d) Firmware Revision 1.08, PCB Revision B.02
 [ INFO] 1236963380.523138000:             Serial #: 01025
 [ INFO] 1236963380.525259000:             Name: fr_caster_rotation_motor
 .
 .
 Usage: ./motorconf [options]
 -i, --interface <i>    Use the network interface <i>
 -a, --actuators <file> Get the actuator definitions from file (default: actuators.conf)
 -d, --device <d>       Select the device to program
 -b, --board <b>        Set the expected board type (wg005, wg006, wg021)
 -p, --program          Program a motor control board
 -n, --name <n>         Set the name of the motor control board to <n>
    Known actuator names:
      bl_caster_l_wheel_motor
      bl_caster_r_wheel_motor
      .
      .
 -m, --motor <m>        Set the configuration for motor <m>
    Legal motor values are:
      148877 - Maxon 148877
      222057 - Maxon 222057
      .
      .
 -h, --help    Print this message and exit
 Error: No default motor for this name
```



**Solution:**

- Check the spelling of the actuator name
- Is the actuator defined in actuators.conf?
- Did you mean to use an alternate actuators configuration file (-a
  option)?
- Explicitly specify a motor with the -m option

#### Error: There is no device at position #X



```
root@prXX:/ros/ros-pkg/drivers/motor/ethercat_hardware# ./motorconf -i ecat0 -p -n actuator_name -d X
 [ INFO] 1236963380.428284000: Device #02: WG05 (0x67d60d) Firmware Revision 1.08, PCB Revision B.02
 [ INFO] 1236963380.429241000:             Serial #: 01070
 [ INFO] 1236963380.431508000:             Name: fr_caster_l_wheel_motor
 [ INFO] 1236963380.475175000: Device #03: WG05 (0x67d60d) Firmware Revision 1.08, PCB Revision B.02
 [ INFO] 1236963380.476185000:             Serial #: 01101
 [ INFO] 1236963380.478312000:             Name: fr_caster_r_wheel_motor
 [ INFO] 1236963380.522127000: Device #04: WG05 (0x67d60d) Firmware Revision 1.08, PCB Revision B.02
 [ INFO] 1236963380.523138000:             Serial #: 01025
 [ INFO] 1236963380.525259000:             Name: fr_caster_rotation_motor
 .
 .
 [FATAL] 1236963689.398617000: There is no device at position #X
```



**Solution:**

- Did you give the correct device location?

#### Error: Returns without finding slaves



```
root@prXX:/ros/ros-pkg/drivers/motor/ethercat_hardware# ./motorconf -i ecat0 
 Filename: actuators.conf
 With:
 Socket created: socket id: 3
 Got interface: index: 0
 Packet round-trip timeout has been set to 20000 usecs.
```



**Solution:**

- Is the power board on? 

```
roscd pr2_power_board
  rosmake
  roslaunch gui_power2.launch
```

## Changing the packet timeout and number of process data retries for pr2_etherCAT

#### Timeout

An EtherCAT slave device never generates network traffic. The EtherCAT
master (computer) generates all packets, and slave device simply fills
in or pull out data from packets. As such, every packet sent by EtherCAT
master, should come back to the master, unless: 1. The packet data was
corrupted (CRC bad). The computer's network card will drop packet on
reception. 1. There is a broken device or a non-EtherCAT device plugged
into chain.

The EtherCAT slaves process the packets in hardware so the delay between
sending a packets and receiving packet should be very consistent. After
sending a packet, the Master should be able to wait a small timeout
before receiving the result. If the packet is not received after the
small timeout, then it must have been dropped.

Unfortunately, the Linux OS, and most Ethernet drivers is not hard
realtime. The amount of time a packet takes to get delivered back to a
user-space program can vary widely. This leads to the following
tradeoff:

- Setting the timeout to be too short causes user-space to believe that
  a packet is dropped when OS takes too long to deliverer (ie **late
  packet**).
- Setting timeout to be too long causes user-space program to wait too
  long and and messes up realtime loop.

In past, the timeout was set to 20 milliseconds, which lead to very few
**late packets** but, caused noticeable glitches in realtime
controllers.

With new releases, the timeout has been reduced to 1 millisecond. A
dropped packet should cause less glitching of realtime controllers.
Hopefully, a timeout of 1ms does not cause extra **late packets**.

##### Process data retries

When a packet containing process data (realtime data) times-out, the
EtherCAT master assumes the packet is lost and will retry sending
process data. For safety reasons, the EtherCAT master will halt motor
after the retries a certain amount of times. In the past the number of
retries was 5 and the timeout was 20ms. This meant that the master would
resend packet for 100ms before halting motors (5\*20ms = 100ms = 1/10th
second). With reduced timeout, 5 retries no longer make much sense.
Instead the retries is calculated based on the timeout so that the
master spends about 20ms retrying a packet transmission. So for a 1ms
timeout, the master will retry 20 times before halting motors.

##### Changing the timeout

The the new release of pr2_ethercat_drivers, it is possible to change
the default timeout by using a setting a rosparam. Before launching
pr2_etherCAT.



```
rosparam set /pr2_etherCAT/realtime_socket_timeout 20000
```



The above example sets the timeout to 20000 microseconds (20
milliseconds).

**NOTE:** Changing parameter after launching pr2_etherCAT **has no
effect**. Thus, setting parameter after using `sudo robot launch` will
not work.

Also note that timeout only takes effect after devices are initialized
and pr2_etherCAT starts running in realtime mode. If the timeout was set
to a value that was way too small (say 1usec). Then pr2_etherCAT should
start-up, but it would start dropping all/most packets after switching
to realtime mode.

### Changing the retries

The number of retries usually is calculated based on the timeout.
However, the number of retries can also be changed with a rosparam


```
rosparam set /pr2_etherCAT/max_pd_retries 5
```



#### Where to Set Parameter

For the PR2, set these parameters in the file `/etc/ros/robot.launch`.
This will change it for all users of your PR2.



```
<launch>
  <param name="pr2_etherCAT/max_pd_retries" value="5" />
  <param name="pr2_etherCAT/realtime_socket_timeout" value="20000" />

  <!-- Launch robot here-->
</launch>
```

## Setting up communication with a new EtherCAT device

The previous tutorial added initial support for a mythical analog device
with one 16bit analog input and one 16bit analog output. This tutorial
will setup process communication with the new device.

### Process Data Communication

Communication with the new EtherCAT device was already occurring in the
previous tutorial. The `EthercatHardware:::ethercatDiagnostics()`
function uses EtherCAT positional addressing to read communication error
counters. However, positional addressing has high overhead.

For reads and writes that need to constantly occur, logical addressing
uses much lower overhead. However, logical addressing uses special
hardware (FMMU and !SyncManagers) on each device. There is limited
amount FMMU and !SyncManager hardware. Also, !SyncManagers and FMMU must
be configured before logical addressing will work.

For the new device, both the 16bit analog input and 16bit analog output
are good candidates for logical addressing.

### SyncManagers and FMMU setup

In the previous tutorial left the `construct()` function setup zero
!SyncManagers and zero FMMUs. For communication to work correctly with
new device, two !SyncManagers and two FMMUs are needed. One !SyncManager
and one FMMU is used for getting the analog input status data. The other
!SyncManager and FMMU will be used for send the analog output data.

#### EtherCAT device details

Lets assume that the !EtherCAT slave device consists of two major parts.
EtherCAT ASIC and a microcontroller. A system diagram is shown below.

TODO : system diagram.

The microcontroller interfaces with a 16 bit ADC for its analog input.
It also interfaces with a 16bit DAC for its analog output. The
microcontroller also uses a SPI bus to communicate with the !EtherCAT
ASIC.

The EtherCAT ASIC is connected to two Ethernet PHYs.

#### Modify construct() function

## Using the 3-axis accelerometer on the PR2 gripper

### Introduction

The new revisions of the gripper motor control board (MCB) has a 3-axis
accelerometer. The accelerometer is the Bosch BMA150. It contain 10 bit
acceleration value data at at 3kHz sample rate. The full scale
acceleration range is configurable to +/-2g, +/-4g, or +/8g (g=gravity).

### Viewing Accelerometer Data

#### As ROS topic

The gripper accelerometer data is published on a ROS topic. Running:


```
rostopic echo /accelerometer/r_gripper_motor
```

 Should produce data like this:


```
header: 
  seq: 14740
  stamp: 
    secs: 1282083521
    nsecs: 167468635
  frame_id: r_gripper_motor_accelerometer_link
samples: 
  - 
    x: 7.3191796875
    y: -3.142265625
    z: 5.0966015625
  - 
    x: 7.3191796875
    y: -2.988984375
    z: 5.441484375
  - 
    x: 7.280859375
    y: -3.065625
    z: 5.4031640625
```



The accelerometer message is published by the realtime loop at 1kHz. The
accelerometer samples at 3kHz so the messages usually contain 3 samples.


```
rostopic hz /accelerometer/r_gripper_motor
```

 

```
average rate: 1000.191
```



**NOTE**: there is a known problem with the accelerometers going to an
error state where they seem to sample at rates far about 3kHz. If the
accelerometer topic always outputs messages 4 accelerometer samples then
the accelerometer is in this error state. See
[ Troubleshooting Gripper Accelerometer ](#troubleshootinggripperaccelerometer)
for more information.

#### With Controller

The accelerometer data can be accessed by with a controller plugin.
Currently the only way to change the accelerometer range and bandwidth
settings are with a controller.

An example controller has been written to get users started and show how
to change these settings. See
[ Controller for gripper accelerometer](#writing-a-controller-for-the-gripper-accelerometer)
for the example.

#### With diagnostics (pr2_dashboard)

In newer releases (C-turtle) the diagnostic topic provides information
on the accelerometer range and bandwidth settings are available in the
diagnostics. The best way to view the diagnostics data on a PR2 is
through pr2_dashboard.

![attachment:gripper-accelerometer-diagnostics.png](doc/gripper-accelerometer-diagnostics.png)

**NOTE:** Accelerometer data is towards bottom of gripper diagnostics
window.

### Accelerometer Settings

#### Range

As mentioned before the range of the accelerometer is configurable. The
accelerometer data is automatically scaled by the range value the data
was sampled with. Changing the range setting \*should not\* cause
inconstancies with the data.

Currently, the only way to change the current range of the accelerometer
you will need to write a controller plugin. Example code has been
provided to get users started that shows how to change these settings:
[ Controller for gripper accelerometer](#writing-a-controller-for-the-gripper-accelerometer).

#### Bandwidth

The accelerometer hardware has a averaging filter that can reduce the
bandwidth of the data. For proper operation the bandwidth should be set
to highest value (no filtering).

In future releases, they ability to changed the hardware bandwidth
setting may be removed. If signal with less high frequency content is
needed, use highest bandwidth setting and filter samples in software.

**NOTE:** On older software releases, the bandwidth mistakenly defaulted
to lowest value. On newer software releases the bandwidth setting
defaults to highest value. See
[ Troubleshooting Gripper Accelerometer ](#troubleshootinggripperaccelerometer)
for more information on this bug.

### Orientation

Below is a picture of the gripper and some information on orientation of
the accelerometer X,Y,and Z axis.

![attachment:gripper-accelerometer-directions.jpg](doc/gripper-accelerometer-directions.jpg)

**NOTE:** Use cover on top of gripper as orientation reference.

### Troubleshooting

See
[ Troubleshooting Gripper Accelerometer ](#troubleshootinggripperaccelerometer)

## Writing a controller for the gripper accelerometer.

### Introduction

**NOTE: THIS TUTORIAL HAS NOT YET BEEN TESTED AND MAY HAVE MINOR BUGS**

For a more detailed explanation of the steps seen here for writing a
real-time controller please refer to the excellent tutorial:
[Writing a Real-Time Joint Controller](https://index.ros.org/p/pr2_mechanism).

To understand this tutorial you should be familiar with the
documentation for a.
[pr2_hardware_interface](https://index.ros.org/p/pr2_hardware_interface),
which provides the low-level c++ interface we will be calling functions
from to communicate with the accelerometer. a.
[pr2_controller_interface](https://index.ros.org/p/pr2_controller_interface),
which provides the code interface, i.e. how your code will be called. a.
[pr2_controller_manager](https://index.ros.org/p/pr2_controller_manager),
which load/start/stops and generally administers the execution of
realtime code.

### Writing the code

![](http://www.ros.org/wiki/pr2_mechanism/Tutorials/Writing%20a%20realtime%20joint%20controller?action=AttachFile&do=get&target=controllers_1.png)

First, let's create a package where you'll build your controller. The
package needs to depend on the
[pr2_controller_interface](https://index.ros.org/p/pr2_controller_interface),
the
[pr2_hardware_interface](https://index.ros.org/p/pr2_hardware_interface)
and the [pluginlib](https://index.ros.org/p/pluginlib). The
[controller interface](https://index.ros.org/p/pr2_controller_interface)
package contains the base class for all controllers, the
[pr2_hardware_interface](https://index.ros.org/p/pr2_hardware_interface)
provides access to the C++ API for the accelerometer, and the
[pluginlib](https://index.ros.org/p/pluginlib) package allows us to add
our own controller as a plugin into the
[controller manager](https://index.ros.org/p/pr2_controller_manager)



```
$ roscd ros_pkg_tutorials
$ roscreate-pkg my_controller_pkg pr2_controller_interface pr2_hardware_interface pluginlib
$ roscd my_controller_pkg
```

 And let's already build all the dependencies
of our new package: 

```
$ rosmake
```



#### The code

Now, inside our new package, create the directory **include**, then
**include/my_controller_pkg**, fire up your editor, create a file called
**include/my_controller_pkg/my_controller_file.h** and copy paste the
following code into this file: 

```cplusplus
#include <pr2_controller_interface/controller.h>
#include <pr2_hardware_interface/hardware_interface.h>

namespace my_controller_ns{

class MyControllerClass: public pr2_controller_interface::Controller
{
private:
  pr2_hardware_interface::Accelerometer* accelerometer_handle_;
  double aX, aY, aZ;


public:
  virtual bool init(pr2_mechanism_model::RobotState *robot,
                   ros::NodeHandle &n);
  virtual void starting();
  virtual void update();
  virtual void stopping();
};
}
```



And also create a directory **src** and a file called
**src/my_controller_file.cpp**. Copy paste the following code into this
file: 

```cplusplus
#include "my_controller_pkg/my_controller_file.h"
#include <pluginlib/class_list_macros.h>

namespace my_controller_ns {


/// Controller initialization in non-realtime
bool MyControllerClass::init(pr2_mechanism_model::RobotState *robot,
                            ros::NodeHandle &n)
{
  /* get a handle to the hardware interface */
  pr2_hardware_interface::HardwareInterface* hardwareInterface = robot->model_->hw_;
  if(!hardwareInterface)
      ROS_ERROR("Something wrong with the hardware interface pointer!");

  /* get a handle to the left gripper accelerometer */
  accelerometer_handle_ = hardwareInterface->getAccelerometer("l_gripper_motor");
  if(!accelerometer_handle_)
      ROS_ERROR("Something wrong with getting accelerometer handle");

  // set to 1.5 kHz bandwidth (should be the default)                       
  accelerometer_handle_->command_.bandwidth_ = 6;

  // set to +/- 8g range (0=2g,1=4g)
  accelerometer_handle_->command_.range_ = 2;

  return true;
}


/// Controller startup in realtime
void MyControllerClass::starting()
{
}


/// Controller update loop in realtime
void MyControllerClass::update()
{
  // retrieve our accelerometer data
  // it is most likely that this loop below will run 3 times,
  // this is because the ROS controller_manager calls this
  // function at 1khz and data is buffered from the accelerometer
  // at 3khz. 
  std::vector<geometry_msgs::Vector3> threeAccs = accelerometer_handle_->state_.samples_;
  for( uint  i = 0; i < threeAccs.size(); i++ )
  {
    // here is where you would do anything that you want with
    // the measured acceleration data. This is a good place to
    // do any filtering or other such manipulation. Below we simply
    // overwrite global variables that act as storage containers.
    aX = threeAccs[i].x;
    aY = threeAccs[i].y;
    aZ = threeAccs[i].z;
  }

}


/// Controller stopping in realtime
void MyControllerClass::stopping()
{}
} // namespace
```



#### The code explained

- To make a realtime controller, we created a class which inherits from
  the
  [controller::Controller](http://www.ros.org/doc/api/pr2_controller_interface/html/classcontroller_1_1Controller.html)
  class in the
  [pr2_controller_interface](https://index.ros.org/p/pr2_controller_interface)
  package. Overload certain methods of this base class and Mechanism
  Control will call these methods when your controller changes state.
  You need to overload the `init`, `starting`, `update`, and
  `stopping` methods.
- The `init` method will get called in non-realtime when the
  controller is loaded.
- When the controller gets started, `starting` will get called once in
  realtime, right before the first call of `update`.
- While the controller is running `update` gets called periodically
  (1000 Hz) from the realtime loop.
- When the controller is stopped, `stopping` gets called once in
  realtime, right after the last `update` call.

For a detailed description of the methods in the base class, take a look
at the
[pr2_controller_interface package documentation](https://index.ros.org/p/pr2_controller_interface).

### Compiling the code

Now that we created the code, lets compile it first. Open the
**CMakeLists.txt** file, and add the following line on the bottom:



```
rosbuild_add_library(my_controller_lib src/my_controller_file.cpp)
```

 and, try to build your package:


```
$ make
```

 If everything went well, you should have a
library file called **(lib)my_controller_lib.so** in your **lib**
folder.

### Register your controller as a plugin

![](http://www.ros.org/wiki/pr2_mechanism/Tutorials/Writing%20a%20realtime%20joint%20controller?action=AttachFile&do=get&target=controllers_2.png)
The code, now compiled as a library, needs to run inside the realtime
process. This linking can occur in two ways: (a) automatically, as the
realtime process starts. When the process starts, it will search for and
load your library. Or (b) manually, while the process is running. You
can explicitly ask the process to load your library on the fly. For both
cases, however, the code needs to be earmarked as destined for the
realtime process, that is it needs to be registered as a plugin. Then
the
[pr2_controller_manager](https://index.ros.org/p/pr2_controller_manager)
can use the [pluginlib](https://index.ros.org/p/pluginlib) to administer
the linking, loading, and starting of the controller.

To make the controllers visible to the
[pr2_controller_manager](https://index.ros.org/p/pr2_controller_manager),
[pluginlib](https://index.ros.org/p/pluginlib), and the realtime
process, the package containing the controller must export it as a
loadable class. The first thing to do is to call the plugin registration
macro from your **src/my_controller_file.cpp** file. Add the following
lines to the bottom of this file: 

```
/// Register controller to pluginlib
PLUGINLIB_REGISTER_CLASS(MyControllerPlugin, 
                         my_controller_ns::MyControllerClass, 
                         pr2_controller_interface::Controller)
```

 and rebuild
your controller: 

```
$ make
```



Next, to export the controller, you must also depend on the
[pr2_controller_interface](https://index.ros.org/p/pr2_controller_interface)
and [pluginlib](https://index.ros.org/p/pluginlib) packages and
reference the plugin description file in the exports section. The
dependencies were automatically noted during the package creation in
Section 2, but you need to explicitly add the following export statement
to **manifest.xml** in the `<package> <\\package>` scope:


```XML
  <export>
    <pr2_controller_interface plugin="${prefix}/controller_plugins.xml" />
  </export>
```

 All together the **manifest.xml** will look
something like: 

```XML
<package>
  ...
  <depend package="pr2_controller_interface" />
  <depend package="pluginlib" />
  ...
  <export>
    <pr2_controller_interface plugin="${prefix}/controller_plugins.xml" />
  </export>
  ...
</package>
```

 Finally, you need to create the
plugin description file, which the manifest called
**controller_plugins.xml**. The format is described in the
[pluginlib](https://index.ros.org/p/pluginlib) documentation. For our
controller we need the following description in
**controller_plugins.xml**:



```XML
<library path="lib/libmy_controller_lib">
  <class name="MyControllerPlugin" 
         type="my_controller_ns::MyControllerClass"           
         base_class_type="pr2_controller_interface::Controller" />
</library>
```



Now, let's ensure that the controller is correctly configured as a
plugin and is visible to Mechanism Control. Check that the plugin
description file is visible to rospack:



```
$ rospack plugins --attrib=plugin pr2_controller_interface
```

 Your controller_plugins.xml file should be in
this list. If it's not, then you probably did not add
[pr2_controller_interface](https://index.ros.org/p/pr2_controller_interface)
as a dependency of your package.



```wiki
There's still no good way of checking that plugins are built without using `nm`.
https://code.ros.org/trac/ros-pkg/ticket/2822
```



Now you are ready to run your controller. If you need tips on doing that
refer to the real-time joint controller tutorial here:
[run your controller](https://index.ros.org/p/pr2_mechanism).

## Integrating a new type of EtherCAT device with ROS.

This tutorial shows the steps needed to integrate an new type of
EtherCAT device into and ethercat_hardware and pr2_etherCAT. This
tutorial integrates an imaginary EtherCAT device with one 16bit analog
input and one 16bit analog output. The imaginary EtherCAT device is
assumed to have a product ID of **1234567**.

### Getting ROS

The code for this tutorial was writen for the ROS **boxturtle** release.
The PR2 version of the release has the required packages for this
tutorial. There are a couples methods for obtaining ROS. The following
method was used when this tutorial was created:

#### SVN Checkout

These instructions were taken from
[ROS/Installation/Ubuntu/SVN](ROS/Installation/Ubuntu/SVN).


```
wget --no-check-certificate http://ros.org/rosinstall -O ~/rosinstall
chmod 755 ~/rosinstall
~/rosinstall ~/ros http://ros.org/rosinstalls/boxturtle_pr2.rosinstall
```



### Run pr2_etherCAT

To verify the new EtherCAT device is connected properly, run
pr2_etherCAT before writing any code. Go through
[ this tutorial](pr2_etherCAT/Tutorials/Running ) for instruction on
building and running pr2_etherCAT.

On startup, pr2_etherCAT will read the product ID, serial number, and
revision of all EtherCAT devices it detects. If pr2_etherCAT can not
read these values or does not see any devices, there may be something
wrong with the new device or cabling connecting it to the computer.

When pr2_etherCAT finds an EtherCAT device it does not recognize, it
will print an error message and quit. Below is the error message caused
by using the new EtherCAT device. 

```
[FATAL] [1272302813.320857903]: Unable to configure slave #0, product code: 1234567 (0x12D687), serial: 1004 (0x3EC), revision: 33685781 (0x2020115)
[FATAL] [1272302813.321324003]: Perhaps you should power-cycle the MCBs
[FATAL] [1272302814.321531811]: BREAKPOINT HIT
	file = /u/dking/wg_latest/stacks/pr2_ethercat_drivers/ethercat_hardware/src/ethercat_hardware.cpp
	line=190
```



The error message shows the unidentified device has a product code of
**1234567**

### Create ROS package

All the code to support the new device will be put in a new package.
Some steps must be taken for ROS to find a new package.

#### Create directory to hold new packages

First, create a directory to store new ROS packages in. This directory
could be put anywhere, but for this tutorial create the directory in
your home folder. 

```
cd $HOME
mkdir my_pkgs
```



#### Add directory to ROS package search path

Modify ROS setup script to look for packages inside of new directory.
**my_pkgs**. The setup script should be located at `$HOME/ros/setup.sh`.

Prepend the new directory path (`$HOME/my_pkgs`) to the the
**ROS_PACKAGE_PATH** variable in the ROS setup script.

This is what the line in `setup.sh` should look like after the changes:


```
export ROS_PACKAGE_PATH=$HOME/my_pkgs:$HOME/ros/stacks
```



Any previously open terminals will not have the new value for
**ROS_PACKAGE_PATH**. Re-source the setup script to get the new value.


```
source ~/ros/setup.sh
```



#### Create a new package

Create a new ROS package called **my_device_pkg** for the new device.
Create the package inside the **my_pkgs** directory. The new package
will need to be given have a couple of dependencies:

- roscpp
- ethercat_hardware

Run: 

```
cd $HOME/my_pkgs
roscreate-pkg my_device_pkg roscpp ethercat_hardware
```



#### Verify new package

Verify ROS can find the new package by running: 

```
rospack find my_device_pkg
```



The command should provide path to the new package. The path will
probably be something like: 

```
$HOME/my_pkgs/my_device_pkg
```



### Create header file for new device

A header file for the new device should be created inside the include
directory of the new package.



```
roscd my_device_pkg/include/my_device_pkg/
```



Create a header file called **my_device.h** with the following code.


```cplusplus
#ifndef MY_DEVICE_H
#define MY_DEVICE_H

#include <ethercat_hardware/ethercat_device.h>

class MyDevice : public EthercatDevice
{
public:
  void construct(EtherCAT_SlaveHandler *sh, int &start_address);
  int initialize(pr2_hardware_interface::HardwareInterface *, bool);
  void diagnostics(diagnostic_updater::DiagnosticStatusWrapper &d, unsigned char *);
  void packCommand(unsigned char *buffer, bool halt, bool reset);
  bool unpackState(unsigned char *this_buffer, unsigned char *prev_buffer);
 
  MyDevice();
  ~MyDevice();

protected:
  int counter_;
};

#endif /* MY_DEVICE_H */
```



#### Explanation of header file

All device types should be derived from !EthercatDevice class.

`EthercatDevice` defines a few virtual functions that `MyDevice` must
implement.

### Create source for new device

Create a source file in the source directory of the ethercat_hardware
package. 

```
roscd my_device_pkg/src
```



Copy the following code into a file called **my_device.cpp**


```cplusplus
#include <my_device_pkg/my_device.h>
#include <ros/console.h>
#include <sstream>
#include <iomanip>
using namespace std;

PLUGINLIB_REGISTER_CLASS(1234567, MyDevice, EthercatDevice);

MyDevice::MyDevice()
{
  counter_ = 0;  
}

void MyDevice::construct(EtherCAT_SlaveHandler *sh, int &start_address)
{
  EthercatDevice::construct(sh, start_address);
  sh->set_fmmu_config( new EtherCAT_FMMU_Config(0) );
  sh->set_pd_config( new EtherCAT_PD_Config(0) );
}

MyDevice::~MyDevice()
{
  delete sh_->get_fmmu_config();
  delete sh_->get_pd_config();
}

int MyDevice::initialize(pr2_hardware_interface::HardwareInterface *hw, bool allow_unprogrammed)
{
  ROS_WARN("Device #%02d: MyDevice (%d)", 
            sh_->get_ring_position(), sh_->get_product_code());
  return 0;
}

void MyDevice::diagnostics(diagnostic_updater::DiagnosticStatusWrapper &d, unsigned char *)
{
  stringstream name;
  name << "EtherCAT Device #" << setw(2) << setfill('0') 
       << sh_->get_ring_position() << " (MyDevice)";
  d.name = name.str();
  d.summary(d.OK, "OK");
  stringstream hwid;
  hwid << sh_->get_product_code() << "-" << sh_->get_serial();
  d.hardware_id = hwid.str();

  d.clear();
  d.addf("Position", "%02d", sh_->get_ring_position());
  d.addf("Product Code", "%d", sh_->get_product_code());
  d.addf("Serial Number", "%d", sh_->get_serial());
  d.addf("Revision", "%d", sh_->get_revision());
  d.addf("Counter", "%d", ++counter_);

  EthercatDevice::ethercatDiagnostics(d, 2);
}

void MyDevice::packCommand(unsigned char *buffer, bool halt, bool reset)
{
}

bool MyDevice::unpackState(unsigned char *this_buffer, unsigned char *prev_buffer)
{
  return true;
}
```



#### Explanation of source file

Classes for different type of devices are used as plugins. The plugins
class will register themselves and the devices they support when the
class is loaded. **PLUGINLIB_REGISTER_CLASS** is a macro that registers
the `MyDevice` class as child class plugin for `EthercatDevice`. For
each device, a setup function will try to match the device to a plugin
using its product code. The code snippet registers `MyDevice` as a
plugin for any device with the product code **1234567**. There is more
information on pluginlib available
[ here](https://index.ros.org/p/pluginlib).

`construct()` is supposed to configure the EtherCAT !SyncManagers and
Fieldbus Memory Mannegment Units (FMMU) for a given device. This
configuration is needed for proper communication with a device. Setting
up communication with an EtherCAT device is covered in the next
tutorial. For now, no !SyncManagers and no FMMUs are configured.

`initialize()` is called once communication with a device available. The
purpose of this function is to setup ROS communication channels, create
hardware interface for controllers and possibly collect more information
about the device. More code will be implemented in next part of
tutorial. For now, the function just print out some information about
the device.

Every EtherCAT device must provide diagnostics information. A
diagnostics message has a few required fields, but most of the
information is provided in the form of key-value pairs. The
`DiagnosticStatusWrapper` provides an easy way to create and append data
to a diagnostics message.

The **name** is one piece of required information for a diagnostics
message. The name that is provided for a particular device should be
unique and should not change while the program is running. In the code
snippet, the device position is used to make sure the device name is
unique even when there are multiple devices of the same type.

The device **summary** contains two pieces of information. The **level**
provides an easy way to identify devices that have problems. The
possible values for level are : `ERROR`, `WARN`, and `OK`. The
**summary** is a short description of the any problem that is occurring
on a device. When there are no issues with a device, the summary should
be **OK**.

The hardware ID should be unique identifier for a given piece of
hardware. A combination of product code and serial number works well for
this purpose.

In next chunk of code a few key-value pairs are added to the diagnostics
message. Both key and values are formatted as strings. Notice the
`counter` variable is increment every time the diagnostics function is
called.

The `EthercatDevice` base class collects information from the EtherCAT
device that is available on most EtherCAT ASICs. The call to
`ethercatDiagnostics` allows this information to be added to the
diagnostics message. The number **2** is the number of Ethernet/EBUS
ports the device has.

The last two functions handle communication to and from the device. They
will be covered in the next tutorial. Leave them empty for now.

### Build new package

Open **my_device_pkg/CMakeLists.txt** and add the following line to the
end of the file: 

```
rosbuild_add_library(my_device_plugin src/my_device.cpp)
```



Now to build the new package: 

```
rosmake my_device_pkg
```



Running above command will build a shared library called
**libmy_device_plugin.so**. This shared library should be located inside
the **lib** directory or **my_device_pkg**.

### Register plugin

**my_device_plugin.so** needs to register as a ethercat_device plugin.
Create ethercat_device_plugin.xml in the top level directory of
**my_device_pkg** and add the following: 

```
<library path="lib/libmy_device_plugin" >
  <class name="1234567" type="MyDevice" base_class_type="EthercatDevice">
    <description>
      MyDevice - Fake analog I/O device.
    </description>
  </class>
</library>
```



Also open **manifest.xml** and added the following between the
`<package>` and `</package>` tags. 

```
<export>
    <ethercat_hardware plugin="${prefix}/ethercat_device_plugin.xml" />
  </export>
```



Now verify that ROS knows that my_device_pkg contains a
ethercat_hardware plugin. 

```
rospack plugins --attrib=plugin ethercat_hardware
```



The command should find two packages that contain ethercat_device
plugins. 

```
my_device_pkg $HOME/my_pkgs/my_device_pkg/ethercat_device_plugin.xml
ethercat_hardware $HOME/ros/stacks/pr2_ethercat_drivers/ethercat_hardware/ethercat_device_plugin.xml
```



For more information on plugins, see
[pluginlib](https://index.ros.org/p/pluginlib)

### Run pr2_etherCAT

Run pr2_etherCAT. It should no longer quit right away. Instead, you
should see the output from the `ROS_WARN` statement in the
`initialize()` function: 

```
[ WARN] [1272314533.520699463]: Device #00: MyDevice (1234567)
```



Look at diagnostics with runtime_monitor. There should be diagnostics
for the new device. Look at the **Counter** field, its value should be
incrementing once a second. Also notice the extra diagnostic information
that is provided by `EthercatDevice::ethercatDiagnostics()`

![width=100%](doc/Screenshot-RuntimeMonitor-MyDevice-Part1.png)

## Understanding the motor model

### Introduction

All of the PR2 motor control board (MCB) drivers use an electrical model
brushed motors to detect problems. Using this electrical model, the
software can detected the following problems:

- major encoder problems
- unplugged or missing encoder
- motor short circuit
- motor open circuit
- misbehaving motor control board
- wrong motor

The model so it can NOT detect issues like:

- mechanical damage
- encoder drift
- encoder that that is only slightly damaged

### Electrical Model

The following model of an electrical motor is used:


```
voltage = current*resistance + Kv*velocity
```



The equation can be re-arranged to sum to zero: 

```
current*resistance + Kv*velocity - voltage = 0
```



For a ideal motor and ideal sensors the software could just make sure
above equation equals zero. 

```
error = current*resistance + Kv*velocity - voltage
if (error != 0)
{
  halt_motors()
}
```



Since all motors parameters and measurements have variation or noise,
the following check is used to detect a problem if motor:


```
error = abs(current*resistance + Kv*velocity - voltage)
filtered_error = IIR_filter(error)
if ( filtered_error > limit )
{
  halt_motors()
}
```



### Determining Problem

The motor model equation can be used to detect that is something is
wrong, but it can't determine what caused the problem. There are some
simple heuristics that the motor model uses to guess the cause. But
these heuristics don't always work.

#### Detection heuristic example

If the encoder because unplugged, the measured velocity would be zero.
So one possible hueristic would be to blame encoder if velocity was zero
when motor model error was detected : 

```
error = abs(current*resistance + Kv*velocity - voltage)
filtered_error = IIR_filter(error)
if ( filtered_error > limit )
{
  halt_motors()
  if (velocity == 0)
  {
    print("Encoder might be damaged");
  }
  else 
  {
    print("Problem with motor or encoder");
  } 
}
```



While the above code might work sometimes, their might be other reason
why the encoder might not be moving:

- The motor is mechanically being held in place.
- The motor is unplugged (and no outside forces are being applied)
- etc\...

Many times it is easier to detect motor problems using outside
information. If I manually move a joint I know the encoder velocity
should not be zero. Using this outside information I can better
determine the problem. Unfortunately, we don't always have physical
access to a robot.

### Motor Trace

Some motor problems only for short period of time. For instance, a loose
connector could disconnect motor for only short period of time because
due a certain movement that would be difficult to reproduce. The motor
model would report an error, but would not be able to determine what
caused error later. For this reason (and others) a motor "trace" is
published when motor halts due to error. The motor trace contains all
data of motor that occurred a second before an error was detected.

On the PR2 robot the motor trace is recorded along with diagnostics to a
bag file. By looking at the motor trace data it is sometimes possible to
determine what the problem with a motor might have been.

The [ mtrace_plot](mtrace_tools/Tutorials/MtracePlot ) tool can be used
to plot motor trace data.

## Using Force/Torque sensor with WG035 and pr2_etherCAT

### Introduction

An ATI Mini45 force/torque sensor can attached on the back side of the
PR2 gripper. The un-amplified analog signal from the sensor goes into a
WG035 PCB inside the gripper. The WG035 amplifies the analog signal and
converts it to a digital signal. The digital data is passed back to
computer through the EtherCAT bus.

### Requirements Overview

This is a quick overview of what is required to get force/torque data
from ATI Mini45.

#### Gripper MCB (WG006) Firmware

The gripper MCB needs to be running new 2.xx version of its firmware.
This firmware is not compatible with older ROS releases (Electric).

#### pr2_etherCAT and pr2_ethercat_drivers

The Force/Torque sensor and WG006 FW version 2.xx needs ROS Fuerte (or
newer). If using ROS Fuerte, pr2_mechanism version 1.6.1 or better is
required.

#### Hardware

The WG035 and F/T sensor needs to be installed on the PR2 gripper.

#### Configuration

Calibration parameters are needed to convert between sensor strain-gauge
readings and Force/Torque values.

#### OS and software

There is a configuration tool (pr2-ft-config) available for Ubuntu
Precise. To install it, do `apt-get update` and `apt-get install
pr2-ft`.

Make sure you also have the latest pr2-core-\* package for your ROS
distribution:

- pr2-core-fuerte 0.1.9 or newer
- pr2-core-groovy 0.1.4 or newer
- pr2-core-hydro 0.1.6 or newer

### Tutorial Start

#### Install the latest version of pr2-core-\* and pr2-ft

Update your local apt cache: 

```
sudo apt-get update
```



Install the configuration tool: 

```
sudo apt-get install pr2-ft
```



Install the latest version of pr2-core-\* (replace `<distro>` with
your ROS distro): 

```
sudo apt-get install pr2-core-<distro>
```



#### Configure your F/T sensors

Get the serial number from each of the F/T sensors on your robot. The
serial number is printed on a white label on the sensor.

The configuration tool will update the robot's launch files and URDF
with the correct information for your sensors.

If you have F/T sensors on both grippers, do (replace <left s/n> and
<right s/n> with the serial numbers of your sensors, <distro> with
groovy or hydro): 

```
sudo pr2-ft-config --left <left s/n> --right <right s/n> --distro <distro>
```



For example, if your left S/N was FT12000 and your right S/N was
FT12001, and your PR2 runs Hydro, you would do: 

```
sudo pr2-ft-config --left 12000 --right 12001 --distro hydro
```



You can also pass only the `\--left` or `\--right` options to the
configuration tool. For example, if you only have a F/T sensor on the
right gripper, and your PR2 runs Hydro, you would do:


```
sudo pr2-ft-config --right 12001 --distro hydro
```



If you pass no options to the configuration tool, it will reset your
configuration, removing the extra launch parameters and reverting to a
URDF without the F/T patches. 

```
sudo pr2-ft-config --distro hydro
```



#### Special instructions for Ubuntu Lucid

<<SeeSaw(toshow="Click here for instructions for Ubuntu Lucid",
tohide="Click to hide Lucid instructions")>>


```
{{#!wiki seesaw section

=== Getting Electric to work with F/T sensors ===
Skip this section if using ROS Fuerte.
<<SeeSaw(toshow="Click here for special instructions if you run Electric", tohide="click to hide")>>
{{{{#!wiki seesaw section

The gripper motor controller board (MCB) uses a newer version of firmware that is not supported by ROS electric.  When running electric with firmware version (2.xx), you will get the following error(s).
 {{{
[ERROR] [1352339845.318725911]: WG06 FW version 2 not supported 
[FATAL] [1352339845.318781493]: Unable to initialize slave #33, product code: 6805006, revision: 83886800, serial: 1097
```



There is a overlay of pr2_etherCAT drivers that should support gripper
FW 2.xx Copy the following to ft_electric.rosinstall. You can download
the file with this
[ link](http://www.ros.org/wiki/ethercat_hardware/Tutorials/UsingForceTorqueSensorWithWG035?action=AttachFile&do=get&target=ft_electric.rosinstall ).



```
- svn: {local-name: pr2_ethercat_drivers, uri: 'https://code.ros.org/svn/wg-ros-pkg/stacks/pr2_ethercat_drivers/branches/ft_electric'}
- hg: {local-name: pr2_robot, uri: 'https://kforge.ros.org/pr2robot/hg', version: electric-dev}
```



Use rosinstall to make overlay: 

```
rosinstall ~/ft_electric /opt/ros/electric ft_electric.rosinstall
```



Now source new rosinstall script and build overlay:


```
source ~/ft_electric/setup.bash
rosmake pr2_robot
```



}}}}

#### Update to pr2_mechanism 1.6.1 for ROS Fuerte

**NOTE:** version 1.6.1 of pr2_mechanism has the changes needed. Check
*CMakesLists.txt*: 

```
roscd pr2_mechanism
cat CMakeLists.txt | grep rosbuild
```



You should see: 

```
rosbuild_make_distribution(1.6.1)
```



If using pr2_mechanism 1.6.0 or earlier, update packages.


```
sudo apt-get update
sudo apt-get dist-upgrade
```



#### Patch URDF

F/T adapters add extra length and angular offset to gripper connection.
The extra length can be accounted for by adding an extra link in RDF.
However, the anglar displacment causes problems for PR2 inverse
kinematics, so an offset of 85 degrees is used with the wrist
transmission to cancel it out.

A new linke is also added to the URDF for the Force/Torque sensor. The
new frame does not use the axis convention used by the PR2 (X axis
forward), but instead used the vendor specified reference frame. In this
reference frame, the Z-axis points backwards towards wrist, and X and Y
axis are aligned to markings ("+X,+Y) on side of F/T sensor. The data
on the force torque topic is aligned to force torque reference frame.

Make a copy of URDF and patch it to add a force/torque link for and
angular offset for the wrist transmission. **NOTE:** At this time,
robot_uncalibrated_1.8.2.xml is the newest URDF availble, and may change
for a future release. 

```
cd /etc/ros/fuerte/urdf
cp robot_uncalibrated_1.8.2.xml robot_uncalibrated_1.8.2_ft.xml
```



The patch for adding a left F/T sensor can be downloaded here:
[ robot_urdf_left_ft.patch](http://www.ros.org/wiki/ethercat_hardware/Tutorials/UsingForceTorqueSensorWithWG035?action=AttachFile&do=get&target=robot_urdf_left_ft.patch ).

The patch for adding a right F/T sensor can be downloaded here:
[ robot_urdf_right_ft.patch](http://www.ros.org/wiki/ethercat_hardware/Tutorials/UsingForceTorqueSensorWithWG035?action=AttachFile&do=get&target=robot_urdf_right_ft.patch ).

Patch the URDF with left F/T sensor: 

```
patch -p1 robot_uncalibrated_1.8.2_ft.xml < robot_urdf_left_ft.patch
```



Change robot.xml to point to patched URDF: 

```
rm robot.xml
ln -s robot_uncalibrated_1.8.2_ft.xml robot.xml
```



#### Change robot.launch to enbable F/T sensor and load calibration parameters

Each Force/Torque sensor is calibrated at the factory to create a
parameter matrix that maps between sensor readings and force/torque
values. ROS parameters must be loaded before pr2_etherCAT is run, so the
parameters are available to the driver at start-up.

We've created repository with calibration parameters for all F/T
sensors. Checkout this repository with svn: 

```
svn co https://code.ros.org/svn/wg-ros-pkg/pr2_mods/pr2_force_torque_calibration
```



The calibration parameters are different for each Force/Torque sensor.
The parameter file is named after force/torque serial number. For
force/torque sensor with serial number **FT11214** the parameter file
with be named *ft11214_params.yaml*. Also, there is common set of
parameters used for the F/T amplifier board that is also needed
*wg035_revF_params.yaml*.

Create directory for storing force/torque calibration parameters


```
mkdir /etc/ros/sensors/ft
```



Copy parameters files in */etc/ros/sensors/ft* directory. Copy
*wg035_revF_params.yaml*, and *ftXXXXX_params.yaml* where XXXXX is
serial number of force/torque sensor: 

```
cp wg035_revF_params.yaml /etc/ros/sensors/ft
cp ftXXXXX_params.yaml /etc/ros/sensors/ft
```



Change */etc/ros/fuerte/robot.launch* to add something like following.
Change **ftXXXXX_params.yaml** to correct filename for F/T sensor
parameters. The following 

```
<!-- Left Force/Torque -->
    <group ns="/realtime_loop/l_gripper_motor/">
     <param name="enable_ft_sensor" value="True" type="bool"/>    
     <param name="enable_pressure_sensor" value="True" type="bool"/>
     <rosparam command="load" file="/etc/ros/sensors/ft/ftXXXXX_params.yaml"/>
     <rosparam command="load" file="/etc/ros/sensors/ft/wg035_revF_params.yaml"/>
   </group>
```




```
<!-- Right Force/Torque -->
   <group ns="/realtime_loop/r_gripper_motor/">
     <param name="enable_ft_sensor" value="True" type="bool"/>    
     <param name="enable_pressure_sensor" value="True" type="bool"/>
     <rosparam command="load" file="/etc/ros/sensors/ft/ftXXXXX_params.yaml"/>
     <rosparam command="load" file="/etc/ros/sensors/ft/wg035_revF_params.yaml"/>
   </group>
```



This is what *robot.launch* might look like after being modified:


```
<launch>

    <!-- Robot Description --> <param name="robot_description" textfile="/etc/ros/fuerte/urdf/robot.xml" />

    <!-- Robot Analyzer --> <rosparam command="load" file="$(find pr2_bringup)/config/pr2_analyzers.yaml" ns="diag_agg" />

    <!-- Robot bringup --> <include file="$(find pr2_bringup)/pr2.launch" />

    <!-- Web ui --> <include file="$(find webui)/webui.launch" />

    <!-- Left Force/Torque -->
    <group ns="/realtime_loop/l_gripper_motor/">
      <param name="enable_ft_sensor" value="True" type="bool"/>    
      <param name="enable_pressure_sensor" value="True" type="bool"/>
      <rosparam command="load" file="/etc/ros/sensors/ft/ft12345_params.yaml"/>
      <rosparam command="load" file="/etc/ros/sensors/ft/wg035_revF_params.yaml"/>
    </group>

    <rosparam file="/etc/ros/robot.yaml"/>

</launch>
```



Notice the parameter file uses a flag that will enable and disable the
F/T sensor functionality: 

```
<param name="enable_ft_sensor" value="True" type="bool"/>
```

 If not specified
this flag will default to **False** and the F/T sensor will not be used.

The parameter file also has a parameter to enable and disable the
pressure sensors: 

```
<param name="enable_pressure_sensor" value="False" type="bool"/>
```

 If not specified this flag
will default to **True**.

If the pressure sensors are not installed (or needed) they should be
disabled with the ROS parameter. The pressure sensors are slow and share
the SPI bus with F/T amplifier. When the pressure sensor data is read
(every 40ms), it will cause a small glitch in the sampling rate for the
F/T sensor.

}}}}}

#### Recalibate PR2 with new F/T sensors (optional)

Follow the directions here
[Calibrating the PR2](https://index.ros.org/p/pr2_calibration)

#### Getting ROS data

Depending on whether the force/torque sensor is installed on right or
left arm the ROS topic containing F/T data will differ. Use rostopic
list and grep to determine topic name: 

```
rostopic list | grep /ft
```



For a PR2, the topic will either be **/ft/r_gripper_motor** or
**/ft/l_gripper_motor**.

Try viewing the topic data. The topic type should be
**geometry_msgs/WrenchStamped** 

```
rostopic echo /ft/r_gripper_motor
```



The output should look something like: 

```
---
header: 
  seq: 84683
  stamp: 
    secs: 1332478266
    nsecs: 775333703
  frame_id: ''
wrench: 
  force: 
    x: 19.5828911521
    y: 13.7608014027
    z: -70.0375319214
  torque: 
    x: 0.064923969713
    y: -3.26302135565
    z: -0.873719285359
---
```



The F/T data is not zeroed and may have a large offset, typical values
are 10N for force values and ?? Nm for torque.

#### Diagnostics

The driver for the force/torque sensor outputs useful diagnostics
information. If the F/T sensor is damaged or a wire is unplugged, the
diagnostics will contain a warning. On ROS electric the Force/Torque
sensor data will most likely show up in "Other" category. In the
future, the sensor data may be placed in the "Sensors" category.

## Troubleshooting/GripperAccelerometer

### Low bandwidth setting

#### Description

Bandwidth is not set to very low value, causing data is being heavily
filtered. The lowest bandwidth setting is 25Hz, which causes heavy data
filtering. Values may seem to be constant when viewed with rostopic.

#### Diagnosis

On new C-turtle release, current bandwidth setting value can be viewed
with diagnostics. The best way to view diagnostics is with
pr2_dashboard.

On older systems, the bandwidth value is only available to controllers.
Older software also defaulted to lowest bandwidth setting.

#### Solution

Upgrade software. Also, there might be a controller that is changing
bandwidth value.

### Accelerometer interrupt stays asserted

#### Description

The accelerometer has been know to go into bad state where it always
interrupt stays asserted. The interrupt notifies controller that a new
sample is available. If interrupt stays asserted, the controller board
to constantly read from accelerometer data believing it has a new
sample.

#### Diagnosis

Gripper firmware only buffer 4 most recent samples. When data is viewed
with rostopic there is always 4 new samples instead of an average of 3.


```
header: 
  seq: 14080967
  stamp: 
    secs: 1282097599
    nsecs: 640504013
  frame_id: l_gripper_motor_accelerometer_link
samples: 
  - 
    x: -9.04359375
    y: -3.2572265625
    z: -0.843046875
  - 
    x: -9.04359375
    y: -3.2572265625
    z: -0.843046875
  - 
    x: -9.04359375
    y: -3.2572265625
    z: -0.843046875
  - 
    x: -9.04359375
    y: -3.2572265625
    z: -0.843046875
```



New diagnostics software will use the sample counter to monitor the
accelerometer sampling rate. When the issue occurs the sampling rate
will be around 40kHz. The diagnostics will produce the warning **Bad
accelerometer sampling frequency**.

#### Cause

Older software and firmware would allow invalid bandwidth setting that
would trigger this issue. Even with newer firmware and software, this
still sometimes occurs. This is still under investigation.

#### Solution

The current solution is to power-cycle to right/left arm with the
problematic gripper accelerometer. This can be easy be done through the
dashboard by selecting **Disable** then selecting **Enable**. The
software will need to be restarted after power-cycling.

### Accelerometer values don't change (much)

#### Description

When viewing or plotting accelerometer data there does not seem to much
high frequency content.

#### Cause

There's a couple possible causes for this

- Low bandwidth setting causing data to be heavily filtered.
- Accelerometer interrupt stays asserted. Effectively causing sample
  accelerometer data to be read many times.
