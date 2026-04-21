## ROS API



```clearsilver

node.0 {
name=single_miniq_node
desc=`single_miniq_node` is a driver for a single LSE miniQ robot. It subscribes to velocity commands and publishes the robot's odometry and gas sensor data.
sub{
0.name= cmd_vel
0.type= geometry_msgs/Twist
0.desc= Velocity commands to the robot.
}
pub{
0.name= odom
0.type= nav_msgs/Odometry
0.desc= Odometry readings from the robot.
1.name= nose
1.type= lse_sensor_msgs/Nostril
1.desc= Gas sensor data from the LSE miniQ e2v MiSC 5524.
}
param {
0.name= port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The serial port where the LSE miniQ can be found.
1.name= baudrate
1.default= 57600
1.type= int
1.desc= The serial port baud rate.
}
}

node.1 {
name=multi_miniq_node
desc=`multi_miniq_node` is a driver for multiple LSE miniQ robots. It subscribes to velocity commands and publishes each robot's odometry and gas sensor data. Each topic is pushed down into its own namespaces, by prefixing the topics with `robot_<i>/` , e.g., `robot_0/cmd_vel` etc.
sub{
0.name= cmd_vel
0.type= geometry_msgs/Twist
0.desc= Velocity commands to the robot.
}
pub{
0.name= odom
0.type= nav_msgs/Odometry
0.desc= Odometry readings from the robot.
1.name= nose
1.type= lse_sensor_msgs/Nostril
1.desc= Gas sensor data from the LSE miniQ e2v MiSC 5524.
}
param {
0.name= port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The serial port where the LSE miniQ can be found.
1.name= baudrate
1.default= 57600
1.type= int
1.desc= The serial port baud rate.
2.name= /list_of_ids
2.type= list
2.desc= If no list of ids is provided the driver will scan the XBee network for existing LSE miniQ robots.
}
}

node.2 {
name=miniq_pid_server
desc=`miniq_pid_server` is a node for making online calibrations of the LSE miniQ PID velocity controllers. The LSE miniQ has two PID velocity controllers for each wheel, one to start the motor and another for regular operation. To learn how to use this node check [[lse_miniq_robot/Tutorials/Calibrate the  PID velocity controllers|this tutorial]].
param {
0.name= port
0.default= /dev/ttyUSB0
0.type= string
0.desc= The serial port where the LSE miniQ can be found.
1.name= baudrate
1.default= 57600
1.type= int
1.desc= The serial port baud rate.
}
}

node.3 {
name=setup_miniq
desc=`setup_miniq` is a node for downloading settings into the EEPROM of a LSE miniQ robot. This can be done using an XBee connection with a single LSE miniQ, however it is safer to do so using a USB cable. This node should be used in a launch file containing the settings of the robot. To learn how to use this node check [[lse_miniq_robot/Tutorials/Load settings to the LSE miniQ EEPROM|this tutorial]].
param {
0.name= starting_l_kp
0.default= 350
0.type= int
0.desc= The Kp gain for the left wheel starting PID velocity controller.
1.name= starting_l_ki
1.default= 80
1.type= int
1.desc= The Ki gain for the left wheel starting PID velocity controller.
2.name= starting_l_kd
2.default= 0
2.type= int
2.desc= The Kd gain for the left wheel starting PID velocity controller.
3.name= running_l_kp
3.default= 150
3.type= int
3.desc= The Kp gain for the left wheel running PID velocity controller.
4.name= running_l_ki
4.default= 20
4.type= int
4.desc= The Ki gain for the left wheel running PID velocity controller.
5.name= running_l_kd
5.default= 2
5.type= int
5.desc= The Kd gain for the left wheel running PID velocity controller.
6.name= starting_r_kp
6.default= 350
6.type= int
6.desc= The Kp gain for the right wheel starting PID velocity controller.
7.name= starting_r_ki
7.default= 80
7.type= int
7.desc= The Ki gain for the right wheel starting PID velocity controller.
8.name= starting_r_kd
8.default= 0
8.type= int
8.desc= The Kd gain for the right wheel starting PID velocity controller.
9.name= running_r_kp
9.default= 150
9.type= int
9.desc= The Kp gain for the right wheel running PID velocity controller.
10.name= running_r_ki
10.default= 20
10.type= int
10.desc= The Ki gain for the right wheel running PID velocity controller.
11.name= running_r_kd
11.default= 2
11.type= int
11.desc= The Kd gain for the right wheel running PID velocity controller.
12.name= battery_type
12.default= 0
12.type= int
12.desc= The batteries being used in the LSE miniQ (0=1x 18650, 1=4x AA).
13.name= mode
13.default= 0
13.type= int
13.desc= The communication mode used by the LSE miniQ (0=Serial, 1=XBee API). The XBee API mode is not yet implemented. It is possible to force a LSE miniQ to enter the Serial mode by pressing the KEY3 button on startup.
14.name= odometry_d
14.default= 0.0
14.type= double
14.desc= Odometry correction coefficient for the distance travelled.
15.name= odometry_yaw
15.default= 0.0
15.type= double
15.desc= Odometry correction coefficient for the angle.
16.name= gas_a
16.default= 0.0
16.type= double
16.desc= Gas sensor calibration coefficient a.
17.name= gas_b
17.default= 0.0
17.type= double
17.desc= Gas sensor calibration coefficient b.
18.name= timeout
18.default= 0.0
18.type= double
18.desc= Time it takes for the robot to stop if no messages arrive, 0.0 means the robot never stops.
19.name= port
19.default= /dev/ttyUSB0
19.type= string
19.desc= The serial port where the LSE miniQ can be found.
20.name= baudrate
20.default= 57600
20.type= int
20.desc= The serial port baud rate.
}
}
```



## Tutorials

All the LSE miniQ tutorials can be found on the
[lse_miniq_robot](lse_miniq_robot) stack.
