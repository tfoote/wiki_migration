## Overview

This package reads a specified bitmap and send targets by replaying the
drawn movement.

It also receives an input topic and calculates the MSE for each cycle of
the bitmap plot. The MSE is output to ROS_INFO and published in the
topic **mse_out**.

For example, using this png file ![simple movement](attachment:test.png)
will send targets between the specified **min** and **max** values on a
(very) rough sinusoid. The black dot on each row represents the
percentage between **min** and **max**. The top of the graph is 100%
(=max), the bottom is 0% (=min).

## ROS interface

### How to run

The recommended way of using this package is: ```
rosrun sr_movements sr_movements /sr_movements/targets:=/sh_ffj3_mixed_position_velocity_controller/command /sr_movements/inputs:=/sh_ffj3_mixed_position_velocity_controller/state _image_path:="`rospack find sr_movements`/movements/test.png" _min:=.1 _max:=1.4 _publish_rate:=100 _repetition:=5 _nb_step:=1000 _msg_type:="sr"
```

### Topics published and subscribed

Publishes **/sr_movements/targets** with the targets values.

Publishes **/sr_movements/mse_out** with the calculated MSE values.

Subscribe to **/sr_movements/inputs** to receive the data to calculate
MSE.

### Parameters

where we:

-   remap the targets to the
    **/sh_ffj3_mixed_position_velocity_controller/command** topic
-   remap the inputs to the
    **/sh_ffj3_mixed_position_velocity_controller/state** topic
-   load the movement from the image **sr_movements/movements/test.png**
-   set the **min** to 0.0 and the **max** to 1.57
-   set the publish_rate to 100
-   set the number of **repetition** to 5
-   set the number of samples taken from the image (**_nb_step**) to
    1000
-   set the type of data (**_msg_type**) received from **inputs** to
    "sr" to indicate that it's sr_robot_msgs. (the other possible
    value being "pr2" to indicate that it's pr2_controllers_msgs

## Notes

If you have more than one point in the same row, the higher point will
be taken into account.

If there's a gap in your drawn line, then we'll continue publishing
the last value until we get to a new value.
