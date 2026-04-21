## ROS API

The sections below describe how to configure the NXT to ROS bindings.

### Example

Even though the API description looks quite complicated, it's very easy
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
    spread_angle: 0.2
    min_range: 0.01
    max_range: 2.5
    desired_frequency: 5.0
```

 

```clearsilver
node.0 {
name=Motor
desc=ROS API for the NXT motor 
pub{
0.name= ~joint_state
0.type= sensor_msgs/JointState
0.desc= The current effort, position, and velocity of the servo motors.
}
sub{
0.name= ~<name>
0.type= nxt_msgs/JointCommand
0.desc= The joint effort to apply at the joint
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



![\|width="200"](attachment:motor.jpg)



```clearsilver
node.0 {
name=Ultrasonic Sensor
desc=ROS API for the ultrasonic sensor
pub{
0.name= ~<name>
0.type= nxt_msgs/Range
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
5.name= ~spread_angle
5.type= double
5.desc= The angle that describes the cone shape of the ultrasonic beam.
6.name= ~min_range
6.type= double
6.desc= The minimum distance the ultrasonic sensor can measure (meters)
7.name= ~max_range
7.type= double
7.desc= The maximum distance the ultrasonic sensor can measure (meters)
}
}
```

 ![\|width="200"](attachment:ultrasonic.jpg)



```clearsilver
node.0 {
name=Touch Sensor
desc=ROS API for the touch sensor
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

 ![\|width="200"](attachment:touch.jpg)



```clearsilver
node.0 {
name=Color Sensor
desc=ROS API for the color sensor
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

 ![\|width="120"](attachment:color.jpg)



```clearsilver
node.0 {
name=Gyro Sensor
desc=ROS API for the gyro sensor
pub{
0.name= ~<name>
0.type= sensor_msgs/Imu
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

 ![\|width="200"](attachment:gyro.jpg)



```clearsilver
node.0 {
name=Accelerometer Sensor
desc=ROS API for the accelerometer sensor
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

 ![\|width="200"](attachment:accel.jpg)



```clearsilver
node.0 {
name=Intensity Sensor
desc=ROS API for the intensity sensor
pub{
0.name= ~<name>
0.type= nxt_msgs/Intensity
0.desc= Intensity value measured from the intensity sensor.
}
param {
0.name= ~nxt_robot/type
0.default= None
0.type= string
0.desc= The type should be set to "intensity".
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

 ![\|width="120"](attachment:color.jpg)
