## Overview

The Serializer package consists of a Python driver and ROS node for the
[Serializer microcontroller](http://www.roboticsconnection.com/p-16-serializer-robot-controller.aspx)
made by the Robotics Connection. The Serializer connects to a PC or SBC
using either a USB port or XBEE radios.

## Serializer Node

```clearsilver
node.0 {
name = serializer-node.py
desc = A ROS node for the Serializer microcontroller made by the Robotics Connection.

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
  1.type = serializer/SensorState
  1.desc = An array of sensor names and values.
}
srv {
  0.name = ~SetServo
  0.type = serializer/SetServo
  0.desc = Set the target position of servo on pin 'id' to 'value'.

  1.name = ~GetAnalog
  1.type = serializer/GetAnalog
  1.desc = Get the value from an analog sensor on pin 'id'.

  2.name = ~Voltage
  2.type = serializer/Voltage
  2.desc = Return the voltage on the Serializer's main terminals.

  3.name = ~Ping
  3.type = serializer/Ping
  3.desc = Query a Ping sonar sensor on digital pin 'id'.

  4.name = ~GP2D12
  4.type = serializer/GP2D12
  4.desc = Query a GP2D12 IR sensor on analog pin 'id'.

  5.name = ~PhidgetsTemperature
  5.type = serializer/PhidgetsTemperature
  5.desc = Query a Phidgets Temperature sensor on analog pin 'id'.

  6.name = ~PhidgetsVoltage
  6.type = serializer/PhidgetsVoltage
  6.desc = Query a Phidgets voltage sensor on analog pin 'id'.

  7.name = ~PhidgetsCurrent
  7.type = serializer/PhidgetsCurrent
  7.desc = Query a Phidgets current sensor on analog pin 'id'.

  8.name = ~Rotate
  8.type = serializer/Rotate
  8.desc = Rotate the robot base through 'angle' radians at 'velocity' rad/s.

  9.name = ~TravelDistance
  9.type = serializer/TravelDistance
  9.desc = Move the robot forward or backward through 'distance' meters at 'velocity' m/s.
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
  4.desc = Rate to poll sensors and publish data.
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
  13.desc = Whether or not to write the PID parameters to the Serializer firmware.
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

}
prov_tf {
  0.from = odom
  0.to   = base_link
  0.desc = Transform needed for navigation.
}
```

### Configuration

The recommended way to configure the Serializer node is to use a YAML
file specifying the required parameters. A sample parameter file called
`sample_params.yaml` is included in the distribution and is shown
below. Note that many of the parameters are commented out and must be
set and un-commented before you can use the node with your Serialzier:

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
analog: { voltage: {pin: 5, type: Voltage}, drive_current: {pin: 1, type: PhidgetsCurrent}, light_sensor: {pin: 2, type: Analog} }
#digital: { base_sonar: {pin: 5, type: Ping} }
```

### Example Launch File

```
<launch>
   <node name="serializer" pkg="serializer" type="serializer_node.py" output="screen">
   <rosparam file="$(find my_robot)/params/serializer_params.yaml" command="load" />
   </node>
</launch>
```

### Usage Notes

-   If you mess up your parameters in a given session, just do a:\
    ```
rosparam delete /serializer
```

```{=html}
<!-- -->
```
-   Try to keep the sensor and PID polling rates relatively low.
    Something around 10Hz seems ideal although you can try 15-20Hz.
    Higher rates can cause the Serializer to act sporadically.

```{=html}
<!-- -->
```
-   Most of the Serializer functions have been implemented though a few
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
    higher. It has been tested on Ubuntu Linux 10.04.

```{=html}
<!-- -->
```
-   Documentation for the Python Serializer library can be found at
    <http://www.pirobot.org/code/serializer.html>

```{=html}
<!-- -->
```
-   The official Serializer manual can be found at
    <http://www.roboticsconnection.com/multimedia/docs/Serializer_3.0_UserGuide.pdf>
