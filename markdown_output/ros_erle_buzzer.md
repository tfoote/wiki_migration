This package provides communication driver to control the buzzer of
Erle-Brain

-   Maintainer status: developed
-   Maintainer: Erle Robotics <contact AT erlerobot DOT com>
-   Author: Alejandro Hernández Cordero <ahcorde AT erlerobot DOT com>
-   License:
-   Bug/feature tracker:
    <https://github.com/erlerobot/ros_erle_buzzer/issues>
-   Source: git <https://github.com/erlerobot/ros_erle_buzzer.git>
    (branch: master)

## Overview

This package provides communication driver to control the buzzer of
Erle-Brain

## Nodes



```clearsilver
node.0 {
 name = ros_erle_buzzer_main
 sub {
  0.name= /buzzer/to
  0.type= ros-hydro-erle-buzzer/buzzer
  0.desc= .
 }
}
node.1 {
 name = ros_erle_buzzer_writer
 pub {
  0.name= /buzzer/to
  0.type= ros-hydro-erle-buzzer/buzzer
  0.desc= .
 }
}
```



## Using ros_erle_buzzer

### ros_erle_buzzer_main

Launch the subscriber: 

```
rosrun ros_erle_buzzer ros_erle_buzzer_main
```



You can Publish the led status with one of the two examples:

### ros_erle_buzzer_write.py

Usage in Python: 

```
rosrun ros_erle_buzzer ros_erle_buzzer_writer.py tune
```



### ros_erle_buzzer_write

Usage in C++: 

```
rosrun ros_erle_buzzer ros_erle_buzzer_writer tune
```



### Example

If you want to play one of the eleven different tones execute:


```
rosrun ros_erle_buzzer ros_erle_buzzer_writer 1
```



### Configure your network

If you are working with two different machines, for example: Erle-Brain
and your laptop remember to configure ROS_MASTER_URI and ROS_IP. Maybe
could be interesting to put this lines in your bashrc.

Erle-Brain 

```
export ROS_MASTER_URI=http://192.168.7.2:11311
export ROS_IP=192.168.7.2
```



Laptop or PC: 

```
export ROS_MASTER_URI=http://192.168.7.2:11311
export ROS_IP=192.168.7.1
```



## Support forums and chats

Please ask your questions not related to bugs/feauture requests on:

-   Erle Robotics Forum: <http://forum.erlerobotics.com/>

We'd like to keep the project bugtracker as free as possible, so please
contact via the above methods.

## Related Links

-   Erle Robotics: <https://erlerobotics.com>
-   Erle-Brain: <https://erlerobotics.com/blog/product/erle-brain/>
