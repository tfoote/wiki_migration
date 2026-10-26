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
package does provide the [motorconf](#motorconf) command-line tool for
configuring these boards. In practice, this tool is used during robot
assembly, and should not be needed after initial bring-up of the robot.
**NOTE: improper use of this tool could lead to hardware damage,
`motorconf` usage is limited to system administrators only.**

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


