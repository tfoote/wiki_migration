## Overview

This package consists of a Python driver and ROS node for
Arduino-compatible controllers. The Arduino must be connected to a PC or
SBC using either a USB port or an RF serial link (e.g. XBee).

\'\'\'Features\'\'\'

-   Direct support for the following sensors:
-   Ping sonar
-   Sharp infrared (GP2D12)
-   Onboard Pololu motor controller current
-   Phidgets Voltage sensor
-   Phidgets Current sensor (DC, 20A)

```{=html}
<!-- -->
```
-   Can also read data from generic analog and digital sensors

```{=html}
<!-- -->
```
-   Can control digital outputs (e.g. turn a switch or LED on and off)

```{=html}
<!-- -->
```
-   Support for PWM servos

```{=html}
<!-- -->
```
-   Configurable base controller if using the required hardware.

## Arduino Node

```clearsilver
node.0 {
name = arduino-node.py
desc = A ROS node for Arduino-compatible microcontrollers.  Sensors can be polled at independent rates (see sample config file at the end of this page.)  For example, main voltage could be polled at 1 Hz while a sonar sensor could be polled at 20 Hz.

sub {
  0.name = /cmd_vel
  0.type = geometry_msgs/Twist
  0.desc = Movement commands for the base controller.
}
pub {
  0.name = /odom
  0.type = nav_msgs/Odometry
  0.desc = Odometry messages from the base controller.

  1.name = ~sensor_state
  1.type = ros_arduino_msgs/SensorState
  1.desc = An array of sensor names and values.

  2.name = ~sensor/name
  2.type = sensor_msgs/Range, std_msgs/Bool, std_msgs/Float64, std_msgs/Int16
  2.desc = Each sensor value is published on its own topic under the "sensor" namespace with the appropriate type.  See sample config file below for examples.
}
srv {
  0.name = ~servo_write
  0.type = ros_arduino_msgs/ServoWrite
  0.desc = Set the target position of a servo with index 'id' to 'value' (in radians).  The 'id' to pin mapping is made in the Arduino firmware.

  1.name = ~servo_read
  1.type = ros_arduino_msgs/ServoRead
  1.desc = Get the last set position (in radians) from the servo with index 'id'.

  2.name = ~digital_set_direction
  2.type = ros_arduino_msgs/DigitalSetDirection
  2.desc = Sets a digital pin to INPUT (0) or OUTPUT (1)

  3.name = ~digital_write
  3.type = ros_arduino_msgs/DigitalWrite
  3.desc = Sets a digital pin either LOW (0) or HIGH (1)
 
}
param {
  0.name = ~port
  0.type = str
  0.desc = Serial port.
  0.default = /dev/ttyUSB0 -- some controllers use /dev/ttyACM0

  1.name = ~baud
  1.type = int
  1.desc = Baud rate for the serial connection.
  1.default = 57600

  2.name = ~timeout
  2.type = float
  2.desc = Timeout for serial port in seconds.
  2.default = 0.1

  3.name = ~rate
  3.type = int
  3.desc = Rate to run the main control loop.  Should be at least as fast as the faster sensor rate.
  3.default = 50

  4.name = ~sensorstate_rate
  4.type = int
  4.desc = Rate to publish the overall sensor array.  Note that individual sensors are published on their own topics and at their own rate.
  4.default = 10

  5.name = ~use_base_controller
  5.type = bool
  5.desc = Whether or not to use the base controller.
  5.default = False

  6.name = ~base_controller_rate
  6.type = int
  6.desc = Rate to publish odometry data.
  6.default = 10

  6a.name = ~base_frame (New in Hydro)
  6a.type = string
  6a.desc = Link to use as the base link when publishing odometry
  6a.default = base_link

  7.name = ~wheel_diameter
  7.type = float
  7.desc = Wheel diameter in meters.
  7.default = none

  8.name = ~wheel_track
  8.type = float
  8.desc = Wheel track in meters. (Distance between centers of drive wheels.)
  8.default = none

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

  14.name = ~Kp
  14.type = int
  14.desc = Proportial PID parameter.
  14.default = 20

  16.name = ~Kd
  16.type = int
  16.desc = Derivative PID parameter.
  16.default = 12

  17.name = ~Ki
  17.type = int
  17.desc = Integral PID parameter.
  17.default = 0

  18.name = ~Ko
  18.type = int
  18.desc = Output PID parameter.
  18.default = 50

  19.name = ~accel_limit
  19.type = float
  19.desc = Max acceleration when changing wheel speeds
  19.default = 0.1

  23.name = ~sensors
  23.type = dict
  23.desc = Dictionary of sensors attached to the Arduino.  (See the sample YAML config file below.)
  23.default = None

}
prov_tf {
  0.from = odom
  0.to   = base_link
  0.desc = Transform needed for navigation.
}
```

### Configuration

The Arduino node is configured using a YAML file specifying the required
parameters. A sample parameter file called \`arduino_params.yaml\` is
included in the config directory and is shown below. Make a copy of this
file(e.g. \`my_arduino_params.yaml\`) before editing. Note that many of
the parameters are commented out and must be set and un-commented before
you can use the node with your Arduino.

Current valid sensor types names (case-sensitive):

-   Ping
-   GP2D12
-   Analog (generic)
-   Digital (generic)
-   PololuMotorCurrent
-   PhidgetsVoltage
-   PhidgetsCurrent (20 amps, DC)

```
port: /dev/ttyUSB0
baud: 57600
timeout: 0.1

rate: 50
sensorstate_rate: 10

use_base_controller: False
base_controller_rate: 10

# === Robot drivetrain parameters
#wheel_diameter: 0.146
#wheel_track: 0.2969
#encoder_resolution: 8384 # from Pololu for 131:1 motors
#gear_reduction: 1.0
#motors_reversed: True

# === PID parameters
#Kp: 20
#Kd: 12
#Ki: 0
#Ko: 50
#accel_limit: 1.0

# === Sensor definitions.  Examples only - edit for your robot.
#     Sensor type can be one of the follow (case sensitive!):
#	  * Ping
#	  * GP2D12
#	  * Analog
#	  * Digital
#	  * PololuMotorCurrent
#	  * PhidgetsVoltage
#	  * PhidgetsCurrent (20 Amp, DC)

sensors: {
  #motor_current_left:   {pin: 0, type: PololuMotorCurrent, rate: 5},
  #motor_current_right:  {pin: 1, type: PololuMotorCurrent, rate: 5},
  #ir_front_center:      {pin: 2, type: GP2D12, rate: 10},
  #sonar_front_center:   {pin: 5, type: Ping, rate: 10},
  arduino_led:          {pin: 13, type: Digital, rate: 5, direction: output}
}
```

### Example Launch File

```
<launch>
   <node name="arduino" pkg="ros_arduino_python" type="arduino_node.py" output="screen">
      <rosparam file="$(find ros_arduino_python)/config/my_arduino_params.yaml" command="load" />
   </node>
</launch>
```

### Usage Notes

-   Be sure to put your robot on blocks before first trying the base
    controller

```{=html}
<!-- -->
```
-   If you mess up your parameters in a given session, just do a:\
    ```
rosparam delete /arduino
```

```{=html}
<!-- -->
```
-   The driver requires Python 2.6.5 or higher and PySerial 2.3 or
    higher. It has been tested on Ubuntu Linux 10.04 (Maveric) and 11.10
    (Oneric).

## Report a Bug

<https://github.com/hbrobotics/ros_arduino_bridge/issues>
