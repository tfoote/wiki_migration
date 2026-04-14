## leJOS ROS API

This package provides the leJOS ROS API. There is an alternate package -
nxt_lejos_lcp_proxy - which provides a very similar API and does not
need a responder running on the NXT, but this package is much faster,
and is recommended.

### Example

Even though the API description looks quite complicated, it\'s very easy
to configure the bindings. Here is an example configuration:
```
nxt_robot:
  - type: motor
    name: r_wheel_joint
    port: PORT_A
    desired_frequency: 20.0

  - type: motor
    name: l_wheel_joint
    port: PORT_B
    desired_frequency: 20.0

  - type: gyro
    name: gyro
    frame_id: gyro_link
    port: PORT_3
    offset: 0
    desired_frequency: 20.0

  - type: ultrasonic
    frame_id: ultrasonic_link
    name: ultrasonic_sensor
    port: PORT_2
    desired_frequency: 10.0

  - type: differential_pilot
    name: pilot
    port: PORT_AC
    desired_frequency: 10.0
    track_width: 16.0
    wheel_diameter: 5.6
    reverse: true
``` ```clearsilver
node.0 {
name=Motor
desc=leJOS ROS API for the NXT motor 
pub{
0.name= ~joint_state
0.type= sensor_msgs/JointState
0.desc= The current power, position, and velocity of the servo motors.
}
sub{
0.name= ~<name>
0.type= nxt_msgs/JointVelocity
0.desc= The joint velocity to apply at the joint
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "motor".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_A, PORT_B or PORT_C.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the actuator and sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
}
}
```

```clearsilver
node.0 {
name=Ultrasonic Sensor
desc=leJOS ROS API for the ultrasonic sensor
pub{
0.name= ~<name>
0.type= sensor_msgs/Range
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "ultrasonic".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_1, PORT_2, PORT_3, or PORT_4.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
4.name= ~nxt_robot/frame_id
4.default=None
4.type= string
4.desc= The frame that the sensor data is published in. 
}
}
```

```clearsilver
node.0 {
name=Touch Sensor
desc=leJOS ROS API for the touch sensor
pub{
0.name= ~<name>
0.type= nxt_msgs/Contact
0.desc= The state of the touch sensor (touching or not).
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "touch".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_1, PORT_2, PORT_3, or PORT_4.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
4.name= ~nxt_robot/frame_id
4.default=None
4.type= string
4.desc= The frame that the sensor data is published in. 
}
}
```

```clearsilver
node.0 {
name=Color Sensor
desc=leJOS ROS API for the color sensor
pub{
0.name= ~<name>
0.type= nxt_msgs/Color
0.desc= Color value measured from the color sensor.
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "color".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_1, PORT_2, PORT_3, or PORT_4.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
4.name= ~nxt_robot/frame_id
4.default=None
4.type= string
4.desc= The frame that the sensor data is published in. 
}
}
```

```clearsilver
node.0 {
name=Gyro Sensor
desc=leJOS ROS API for the gyro sensor
pub{
0.name= ~<name>
0.type= nxt_msgs/Gyro
0.desc= Rotation rate data from the gyro sensor.
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "gyro".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_1, PORT_2, PORT_3, or PORT_4.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
4.name= ~nxt_robot/frame_id
4.default=None
4.type= string
4.desc= The frame that the sensor data is published in. 
}
}
```

```clearsilver
node.0 {
name=Acceleration Sensor
desc=leJOS ROS API for the acceleration sensor
pub{
0.name= ~<name>
0.type= nxt_msgs/Accelerometer
0.desc= The three axis measured values form the accelerometer sensor.
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "accelerometer".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_1, PORT_2, PORT_3, or PORT_4.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
4.name= ~nxt_robot/frame_id
4.default=None
4.type= string
4.desc= The frame that the sensor data is published in. 
}
}
```

```clearsilver
node.0 {
name=Light Sensor
desc=leJOS ROS API for the light sensor
pub{
0.name= ~<name>
0.type= nxt_msgs/Intensity
0.desc= Intensity value measured from the light sensor.
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "light".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_1, PORT_2, PORT_3, or PORT_4.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
4.name= ~nxt_robot/frame_id
4.default=None
4.type= string
4.desc= The frame that the sensor data is published in. 
}
}
```

```clearsilver
node.0 {
name=Sound Sensor
desc=leJOS ROS API for the intensity sensor
pub{
0.name= ~<name>
0.type= nxt_lejos_msgs/Decibels
0.desc= Decibels measured from the sound sensor.
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "sound".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_1, PORT_2, PORT_3, or PORT_4.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
4.name= ~nxt_robot/frame_id
4.default=None
4.type= string
4.desc= The frame that the sensor data is published in. 
}
}
```

```clearsilver
node.0 {
name=Compass Sensor
desc=leJOS ROS API for the compass sensor
pub{
0.name= ~<name>
0.type= nxt_lejos_msgs/Compass
0.desc= Heading value measured from the compass sensor.
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "compass".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_1, PORT_2, PORT_3, or PORT_4.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
4.name= ~nxt_robot/frame_id
4.default=None
4.type= string
4.desc= The frame that the sensor data is published in. 
}
}
```

```clearsilver
node.0 {
name=Motor
desc=leJOS ROS API for the NXT motor 
pub{
0.name= ~joint_state
0.type= sensor_msgs/JointState
0.desc= The current power, position, and velocity of the servo motors.
}
sub{
0.name= ~<name>
0.type= nxt_msgs/JointVelocity
0.desc= The joint velocity to apply at the joint
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "motor".
1.name= ~nxt_robot/port
1.default=None
1.type= string
1.desc= This should be one of the brick ports: PORT_A, PORT_B or PORT_C.
2.name= ~nxt_robot/desired_frequency
2.default=None
2.type= double
2.desc= The desired update frequency for the actuator and sensor.
3.name= ~nxt_robot/name
3.default=None
3.type= string
3.desc= The topic name for the sensor data.   
}
}
```0
