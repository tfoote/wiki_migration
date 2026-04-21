This package provides communication driver to control PWMs with
Erle-Brain

-   Maintainer status: developed
-   Maintainer: Erle Robotics <contact AT erlerobot DOT com>
-   Author: Alejandro Hernández Cordero <ahcorde AT erlerobot DOT com>
-   License:
-   Bug/feature tracker:
    <https://github.com/erlerobot/ros_erle_pwm/issues>
-   Source: git <https://github.com/erlerobot/ros_erle_pwm.git> (branch:
    master)

## Overview

This package provides communication driver to control PWMs with
Erle-Brain

## Nodes



```clearsilver
node.0 {
 name = ros_erle_pwm_main
 sub {
  0.name= /pwm/to
  0.type= ros-hydro-erle-pwm/pwm
  0.desc= .
 }
}
node.1 {
 name = ros_erle_pwm_writer
 pub {
  0.name= /pwm/to
  0.type= ros-hydro-erle-pwm/pwm
  0.desc= .
 }
}
```



## Using ros_erle_pwm

In this section we are going to explain how to use this package to
change the status of the PWMs

### ros_erle_pwm_main

Launch the subscriber: 

```
rosrun ros_erle_pwm ros_erle_pwm_main
```



You can publish the pwm value with one of the two examples:

### ros_erle_pwm_write.py

Usage in Python: 

```
rosrun ros_erle_pwm ros_erle_pwm.py PWM_1 PWM_2 PWM_3 PWM_4 PWM_5 PWM_6 PWM_7 PWM_8
```



### ros_erle_pwm_write

Usage in C++: 

```
rosrun ros_erle_pwm ros_erle_pwm PWM_1 PWM_2 PWM_3 PWM_4 PWM_5 PWM_6 PWM_7 PWM_8
```



### Example

If you want to change the values of the PWM execute:


```
rosrun ros_erle_pwm ros_erle_pwm_writer 900 800 850 400 200 400 100 756
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
