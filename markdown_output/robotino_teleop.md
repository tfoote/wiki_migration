## Overview

The robotino_teleop package implements two nodes which allow Robotino to
be controlled remotely using a joystick or a keyboard.

## ROS Nodes



```clearsilver
node.0 {
  name = joystick_teleop_node
  desc = Control Robotino using a joystick
  pub {
    0.name= cmd_vel
    0.type= geometry_msgs/Twist
    0.desc= Velocities to drive/rotate Robotino
  }
  param {
    0.name= axis_linear_x
    0.default= 1
    0.type= int
    0.desc= Linear X Axis
    1.name= axis_linear_y
    1.default= 0
    1.type= int
    1.desc= Linear Y Axis
    2.name= axis_angular
    2.default= 2
    2.type= int
    2.desc= Angular Axis
    3.name= scale_linear
    3.default= 0.1
    3.type= double
    3.desc= Scale for the translational values
    4.name= scale_angular
    4.default= 0.2
    4.type= double
    4.desc= Scale for the rotational values
  }
}
```



#### Joystick note

**Please note** that depending on your joystick, you might have to
modify the axes parameters in the launch file for it to work.

#### Usage



```
roslaunch robotino_teleop joystick_teleop.launch
```





```clearsilver
node.0 {
  name = keyboard_teleop_node
  desc = Control Robotino using a keyboard
  pub {
    0.name= cmd_vel
    0.type= geometry_msgs/Twist
    0.desc= Velocities to drive/rotate Robotino
  }
  param {
    0.name= scale_linear
    0.default= 1.0
    0.type= double
    0.desc= Scale for the translational values
    1.name= scale_angular
    1.default= 1.0
    1.type= double
    1.desc= Scale for the rotational values
  }
}
```



#### Usage

Run the following command and use the W,A,S & D keys for translational
motion and keys Q and E for rotational motion. Use the SPACEBAR to stop.


```
roslaunch robotino_teleop keyboard_teleop.launch
```


