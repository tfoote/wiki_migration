## Overview

[86Hexapod](http://www.thingiverse.com/thing:964149) is a open-source,
3D-printed hexapod robot to demonstrate the application of the
[86ME](https://github.com/Sayter99/86ME) (86Duino Motion Editor).
86Hexapod has 12 DOF and employs the low-cost
[TowerPro](http://www.towerpro.com.tw/) SG90 servos as its actuators.
With 86Duino Zero/One as its controller, you can easily edit
86Hexapod's motion and automatically generate its control program using
86ME.

[Youtube](https://www.youtube.com/watch?v=tW_QmSS2TaY)

## Connect to ROS

### Wired

The controller of 86Hexapod is [86Duino](http://www.86duino.com).
86Duino can connect to ROS by
[rosserial_Arduino](http://wiki.ros.org/rosserial_arduino) with a usb
cable.

### Wireless

For the wireless solution, users can adopt the
[rosserial for 86Duino](https://github.com/Sayter99/rosserial) with
ESP8266. First, generate ros_lib by rosserial_86duino and use it as
rosserial_arduino in
[86Duino IDE](http://www.86duino.com/?page_id=8918). Then, check the
connection of ESP8266 and 86Duino works by AT commands. Finally, we can
write a program to connect 86Duino to ROS. An example:


```
#include <ros.h>
#include <std_msgs/String.h>

ros::NodeHandle nh;

std_msgs::String msg;
ros::Publisher chatter("chatter", &msg);

void setup()
{
  //(HardwareSerial, Baudrate). Depends on settings of ESP8266
  nh.getHardware()->setESP8266(Serial1, 115200);
  // connect to an AP
  nh.getHardware()->setWiFi("ssid", "password");
  // "IP<:PORT>". Default port number is 11411
  nh.initNode("192.168.4.175");
  nh.advertise(chatter);
}

void loop()
{
  chatter.publish( &msg );
  nh.spinOnce();
  delay(100);
}
```



#### Demo Video

By this work, we can connect multiple 86Duinos to ROS through wifi. Here
is a demonstration to controll two 86Hexapods by a ROS topic
"chatter".

[Youtube](https://www.youtube.com/watch?v=yWgQdA1mVpQ)
