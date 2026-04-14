## The TraxBot Robot

The TraxBot is a tracked mobile robotic platform developed in the Mobile
Robotics Laboratory ([MRL](http://paloma.isr.uc.pt/mrl/)) at the
Institute of Systems and Robotics ([ISR](http://isr.uc.pt/)) in the
University of Coimbra, which has a differential drive system built upon
the Traxster II Robot educational Kit extended with substantial
components and improvements. The light and robust aluminum chassis is
equipped with 2 DC gearhead motors on the front wheels, with quadrature
wheel encoders. A flat acrylic structure was added on top of the
platform to support a 10" notebook and the three ultrasonic range
sonars, as presented.

![](attachment:traxbot.jpg)

The Traxbot is a low-cost robot based on open source tools,
incorporating an
[Arduino Uno](http://arduino.cc/en/Main/ArduinoBoardUno) board as the
control unit together with the [OMNI-3MD](http://botnroll.com/omni3md/)
motor driver, which are placed inside the robot chassis. Following this
philosopy, the next step was, of course, to add ROS support. The battery
pack is placed under the TraxBot and it also includes an Arduino
compatible Xbee Shield which enables an easy-to-use Zigbee-based
communication interface, enabling easy data exchange between multiple
robots or between the robot and a remote unit when no Network
infra-structure (i.e., WiFi) exists.

### Sensors

The TraxBot is equipped with the following sensors:

-   3 Ultrasonic Range Finders
    [Maxbotix MB1300](http://www.maxbotix.com/products/MB1300.htm);

### Actuators

The TraxBot has the following actuators:

-   Left and right wheel motors;
-   RGB lights.

### Processing

Hybrid processing system:

-   [Arduino Uno](http://arduino.cc/en/Main/ArduinoBoardUno) with ATmega
    328p;
-   ASUS eeePC 1001PXD.

### Communication

Hybrid communication system:

-   ZigBee;
-   Wi-Fi 802.11 b/g/n.

## ROS API

```clearsilver

node.0 {
name=traxbot_driverTest
desc=`traxbot_driverTest` is a ROS driver for the custom mobile robot TraxBot.
sub{
0.name= moveMotors
0.type= geometry_msgs/Point32
0.desc= Velocity commands to the robot.
}
pub{
0.name= odometry
0.type= nav_msgs/Odometry
0.desc= Odometry data from the robot.
1.name= batteryPower
1.type= std_msgs/Float32
1.desc= Battery info from robot.
2.name= sonar_traxbot_front
2.type= std_msgs/Float32
2.desc= Range data from the front sonar.
3.name= sonar_traxbot_left
3.type= std_msgs/Float32
3.desc= Range data from the left sonar.
4.name= sonar_traxbot_right
4.type= std_msgs/Float32
4.desc= Range data from the right sonar.
5.name= encoderRead1
5.type= std_msgs/Int16
5.desc= Data from encoder in motor 1 in pulses.
6.name= encoderRead2
6.type= std_msgs/Int16
6.desc= Data from encoder in motor 2 in pulses.
7.name= driverFirmware
7.type= std_msgs/Float32
7.desc= Firmware version of motor driver OMNI-3MD.

}
}

node.1 {
name=traxbot_stageSimulation
desc=`traxbot_stageSimulation` is a ROS alghoritm for perform simulatons with virtual TraxBot.
sub{
0.name= base_scan
0.type= sensor_msgs/LaserScan
0.desc= Data from virtual range laser.
1.name= odom
1.type= nav_msgs/Odometry
1.desc= Odometry data from the virtual TraxBot.

}
pub{
0.name= cmd_vel
0.type= geometry_msgs/Twist
0.desc= Velocity commands to the virtual TraxBot.
}
}
```

## Tutorials

Coming soon\...
