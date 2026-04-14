This package provides communication driver to control the status led of
Erle-Brain

-   Maintainer status: developed
-   Maintainer: Erle Robotics \<contact AT erlerobot DOT com\>
-   Author: Alejandro Hernández Cordero \<ahcorde AT erlerobot DOT com\>
-   License:
-   Bug/feature tracker:
    <https://github.com/erlerobot/ros_erle_statusled/issues>
-   Source: git <https://github.com/erlerobot/ros_erle_statusled.git>
    (branch: master)

## Overview

This package provides communication driver to control the status led of
Erle-Brain

## Nodes

```clearsilver
node.0 {
 name = ros_erle_statusled_main
 sub {
  0.name= /statusled/to
  0.type= ros-hydro-erle-statusled/statusled
  0.desc= .
 }
}
node.1 {
 name = ros_erle_statusled_writer
 pub {
  0.name= /statusled/to
  0.type= ros-hydro-erle-statusled/statusled
  0.desc= .
 }
}
```

## Using ros_erle_statusled

### ros_erle_statusled_main

Launch the subscriber: ```
rosrun ros_erle_statusled ros_erle_statusled_main
```

You can Publish the led status with one of the two examples:

### ros_erle_statusled_write.py

Usage in Python: ```
rosrun ros_erle_statusled ros_erle_statusled_writer.py led_red led_blue
```

### ros_erle_statusled_write

Usage in C++: ```
rosrun ros_erle_statusled ros_erle_statusled_writer led_red led_blue
```

### Example

If you want to turn on the red led and turn off the blue led execute the
following line ```
rosrun ros_erle_statusled ros_erle_statusled_writer 1 0
```

### Configure your network

If you are working with two different machines, for example: Erle-Brain
and your laptop remember to configure ROS_MASTER_URI and ROS_IP. Maybe
could be interesting to put this lines in your bashrc.

Erle-Brain ```
export ROS_MASTER_URI=http://192.168.7.2:11311
export ROS_IP=192.168.7.2
```

Laptop or PC: ```
export ROS_MASTER_URI=http://192.168.7.2:11311
export ROS_IP=192.168.7.1
```

## Support forums and chats

Please ask your questions not related to bugs/feauture requests on:

-   Erle Robotics Forum: <http://forum.erlerobotics.com/>

We\'d like to keep the project bugtracker as free as possible, so please
contact via the above methods.

## Related Links

-   Erle Robotics: <http://erlerobotics.com/>
-   Erle-Brain: <https://erlerobotics.com/blog/product/erle-brain/>
