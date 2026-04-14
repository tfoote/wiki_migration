This package provides communication driver to control ubleds through
Erle-Brain

-   Maintainer status: developed
-   Maintainer: Erle Robotics \<contact AT erlerobot DOT com\>
-   Author: Iñigo Muguruza \<inigo AT erlerobot DOT com\>
-   License:
-   Bug/feature tracker:
    <https://github.com/erlerobot/ros_erle_ubled/issues>
-   Source: git <https://github.com/erlerobot/ros_erle_ubled.git>
    (branch: master)

## Overview

This package provides communication driver to control ubleds through
Erle-Brain

## Nodes

```clearsilver
node.0 {
 name = ros_erle_ubled_main
 sub {
  0.name= /ubled/to
  0.type= ros-hydro-erle-ubled/init_number_leds
  0.desc= .
  1.name= /ubled/to
  1.type= ros-hydro-erle-ubled/reset_pattern
  1.desc= .
  2.name= /ubled/to
  2.type= ros-hydro-erle-ubled/single_led_preset_pattern
  2.desc= .
 }
}
node.1 {
 name = ros_erle_ubled_writer
 pub {
  0.name= /ubled/to
  0.type= ros-hydro-erle-ubled/init_number_leds
  0.desc= .
  1.name= /ubled/to
  1.type= ros-hydro-erle-ubled/reset_pattern
  1.desc= .
  2.name= /ubled/to
  2.type= ros-hydro-erle-ubled/single_led_preset_pattern
  2.desc= .
 }
}
```

## Using ros_erle_ubled

### ros_erle_ubled_main

Launch the subscriber: ```
rosrun ros_erle_ubled ros_erle_ubled_main
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

-   Erle Robotics: <https://erlerobotics.com>
-   Erle-Brain: <https://erlerobotics.com/blog/product/erle-brain/>
