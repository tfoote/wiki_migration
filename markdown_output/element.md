## Overview

The Element package consists of a Python driver and ROS node for the
[Element microcontroller](http://www.cmrobot.com/#!element) made by
cmRobot. The Element connects to a PC or SBC using either a USB port,
XBEE radios or TTL.

![float\|align="right"](attachment:element.png)

**Features**

-   Direct support for a wide variety of commonly used sensors including
    sonar (Ping, MaxEZ, SRF04, SRF05, SRF08, SRF10), infrared (Sharp
    GP2D12), temperature, current, and voltage (Phidgets), speech
    (Devantech SP03), compass (Devantech CMPS03), as well as generic
    digital and analog sensors.
-   Onboard PID controller and dual H-Bridges for driving a differential
    drive robot.
-   Support for attaching up to six hobby servos.

## Element Node

```clearsilver
node.0 {
name = element-node.py
desc = A ROS node for the Element microcontroller made by cmRobot.  Uses a multi-threaded queue so that each sensor can be polled at its own rate (see sample config file at the end of this page.)  For example, main voltage could be polled at 1 Hz while a sonar sensor could be polled at 10 Hz.

sub {
  0.name = /cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Movement commands for the base controller.
}
pub {
  0.name = /odom
  0.type = nav_msgs/Odometry
  0.desc = Odometry messages from the base controller.
  1.name = ~sensors
  1.type = element/SensorState
  1.desc = An array of sensor names and values.
  2.name = ~sensor/sensor_name
  2.type = sensor_msgs/Range, std_msgs/Bool, std_msgs/Float64, std_msgs/Int16
  2.desc = Each sensor value is published on its own topic under the "sensor" namespace with the appropriate type.  See sample config file below for examples.
}
srv {
  0.name = ~SetServo
  0.type = element/SetServo
  0.desc = Set the target position of servo on pin 'id' to 'value'.

  1.name = ~GetAnalog
  1.type = element/GetAnalog
  1.desc = Get the value from an analog sensor on pin 'id'.

  2.name = ~Voltage
  2.type = element/Voltage
  2.desc = Return the voltage on the Element's main terminals.

  3.name = ~Ping
  3.type = element/Ping
  3.desc = Query a Ping sonar sensor on digital pin 'id'.

  4.name = ~GP2D12
  4.type = element/GP2D12
  4.desc = Query a GP2D12 IR sensor on analog pin 'id'.

  5.name = ~PhidgetsTemperature
  5.type = element/PhidgetsTemperature
  5.desc = Query a Phidgets Temperature sensor on analog pin 'id'.

  6.name = ~PhidgetsVoltage
  6.type = element/PhidgetsVoltage
  6.desc = Query a Phidgets voltage sensor on analog pin 'id'.

  7.name = ~PhidgetsCurrent
  7.type = element/PhidgetsCurrent
  7.desc = Query a Phidgets current sensor on analog pin 'id'.

  8.name = ~Rotate
  8.type = element/Rotate
  8.desc = Rotate the robot base through 'angle' radians at 'velocity' rad/s.

  9.name = ~TravelDistance
  9.type = element/TravelDistance
  9.desc = Move the robot forward or backward through 'distance' meters at 'velocity' m/s.

  10.name = ~Speak
  10.type = element/SP03
  10.desc = Use the SP03 text-to-speech chip to speak a phrase given as a string
}
param {
  0.name = ~port
  0.type = str
  0.desc = Serial port.
  0.default = /dev/ttyUSB0

  1.name = ~baud
  1.type = int
  1.desc = Baud rate.
  1.default = 19200

  2.name = ~timeout
  2.type = float
  2.desc = Timeout for serial port in seconds.
  2.default = 0.5

  3.name = ~publish_sensors
  3.type = bool
  3.desc = Whether or not to automatically publish sensor data.
  3.default = False

  4.name = ~sensor_rate
  4.type = int
  4.desc = Rate to publish the overall sensor array.  Note that individual sensors are published on their own topics and at their own rate.
  4.default = 10

  5.name = ~use_base_controller
  5.type = bool
  5.desc = Whether or not to use the PID base controller.
  5.default = False

  6.name = ~units
  6.type = int
  6.desc = Measurement units to use: 0 = metric, 1 = English, 2 = raw.  For use with ROS, it is recommended to always leave this set to 0 for metric. 
  6.default = 0

  7.name = ~wheel_diameter
  7.type = float
  7.desc = Wheel diameter in meters.
  7.default = none

  8.name = ~wheel_track
  8.type = float
  8.desc = Wheel track in meters.
  8.default = none

  9.name = ~encoder_type
  9.type = int
  9.desc = Encoder type: 0 = single, 1 = quadrature
  9.default = 1

  10.name = ~encoder_resolution
  10.type = int
  10.desc = Encoder ticks per wheel revolution.
  10.default = none

  11.name = ~gear_reduction
  11.type = float
  11.desc = External gear reduction.
  11.default = 1.0

  12.name = ~motors_reversed
  12.type = bool
  12.desc = Reverse the sense of wheel rotation.
  12.default = False

  13.name = ~init_pid
  13.type = bool
  13.desc = Whether or not to write the PID parameters to the Element firmware.
  13.default = False

  14.name = ~VPID_P
  14.type = int
  14.desc = Velocity Proportial PID parameter.
  14.default = none

  15.name = ~VPID_I
  15.type = int
  15.desc = Velocity Integral PID parameter.
  15.default = none

  16.name = ~VPID_D
  16.type = int
  16.desc = Velocity Derivative PID parameter.
  16.default = none

  17.name = ~VPID_L
  17.type = int
  17.desc = Velocity Loop PID parameter.
  17.default = none

  18.name = ~DPID_P
  18.type = int
  18.desc = Distance Proportial PID parameter.
  18.default = none

  19.name = ~DPID_I
  19.type = int
  19.desc = Distance Integral PID parameter.
  19.default = none

  20.name = ~DPID_D
  20.type = int
  20.desc = Distance Derivative PID parameter.
  20.default = none

  21.name = ~DPID_L
  21.type = int
  21.desc = Distance Loop PID parameter.
  21.default = none

  22.name = ~base_controller_rate
  22.type = int
  22.desc = Rate to publish odometry information.
  22.default = 10

  23.name = ~analog
  23.type = dict
  23.desc = Dictionary of analog sensors
  23.default = None

  24.name = ~digital
  24.type = dict
  24.desc = Dictionary of digital sensors
  24.default = None

  25.name = ~maxez1
  25.type = dict
  25.desc = Dictionary of MaxEZ1 sensors
  25.default = None

}
prov_tf {
  0.from = odom
  0.to   = base_link
  0.desc = Transform needed for navigation.
}
```

### Configuration

The Element node is configured using a YAML file specifying the required
parameters. A sample parameter file called `element_params.yaml` is
included in the distribution in the config directory and is shown below.
Note that many of the parameters are commented out and must be set and
un-commented before you can use the node with your Element.

Current valid sensor types names (case-sensitive):

-   Ping
-   GP2D12
-   MaxEZ1
-   Analog (generic)
-   Digital (generic)
-   Voltage (main board voltage reported on internal analog pin 5)
-   PhidgetsVoltage
-   PhidgetsCurrent
-   PhidgetsTemperature

```
port: /dev/ttyUSB0
baud: 19200
timeout: 1
sensor_rate: 10
#use_base_controller: True
#base_controller_rate: 10
#wheel_diameter: <fill in and uncomment for your robot>
#wheel_track: <fill in and uncomment for your robot>
#encoder_type: 1
#encoder_resolution: <fill in and uncomment for your robot>
#gear_reduction: <fill in and uncomment for your robot>
#motors_reversed: False
#init_pid: True
#units: 0
#VPID_P: <fill in and uncomment for your robot>
#VPID_I: <fill in and uncomment for your robot>
#VPID_D: <fill in and uncomment for your robot>
#VPID_L: <fill in and uncomment for your robot>
#DPID_P: <fill in and uncomment for your robot>
#DPID_I: <fill in and uncomment for your robot>
#DPID_D: <fill in and uncomment for your robot>
#DPID_A: <fill in and uncomment for your robot>
#DPID_B: <fill in and uncomment for your robot>

publish_sensors: True

# Examples only - change accordingly for your robot.
analog: { voltage: {pin: 5, type: Voltage, rate: 1}, drive_current: {pin: 1, type: PhidgetsCurrent, rate: 1}, light_sensor: {pin: 2, type: Analog, rate: 10} }
#digital: { base_sonar: {pin: 5, type: Ping, rate: 1} }
```

### Example Launch File

```
<launch>
   <node name="element" pkg="element" type="element_node.py" output="screen">
   <rosparam file="$(find my_robot)/config/element_params.yaml" command="load" />
   </node>
</launch>
```

### Usage Notes

-   If you mess up your parameters in a given session, just do a:\
    ```
rosparam delete /element
```

```{=html}
<!-- -->
```
-   Try to keep the sensor and PID polling rates relatively low.
    Something around 10Hz seems ideal although you can try 15-20Hz.

```{=html}
<!-- -->
```
-   Most of the Element functions have been implemented though a few
    have not been tested since I don't currently have some of the
    supported sensors. The functions that have NOT been tested are:

```{=html}
<!-- -->
```
-   step (used with a bipolar stepper motor)
-   sweep (also used with a bipolar stepper motor)
-   srf04, srf08 and srf10 (used with a Devantech SRF04, SRF08 and SRF10
    sonar sensors)
-   tpa81 (used with the Devantech TPA81 thermopile sensor)

```{=html}
<!-- -->
```
-   The driver requires Python 2.6.5 or higher and PySerial 2.3 or
    higher. It has been tested on Ubuntu Linux 10.04 (Maveric) and 11.10
    (Oneric).

```{=html}
<!-- -->
```
-   The official Element manual can be found at
    <http://www.cmrobot.com/#!element/vstc8=downloads>
