## Use

The `turtlebot_teleop` package provides launch files for teleoperation
with different input devices.

For a keyboard teleoperation use: 

```
roslaunch turtlebot_teleop keyboard_teleop.launch
```



For a ps3 joystick use: 

```
roslaunch turtlebot_teleop ps3_teleop.launch
```



For a xbox360 joystick use: 

```
roslaunch turtlebot_teleop xbox360_teleop.launch
```



## Nodes



```clearsilver
node {
  0{
    name = Keyboard Teleop
    desc = The `turtlebot_teleop_key` provides a generic keyboard teleop node.

    pub{
      0{
        name= turtlebot_telop_keyboard/cmd_vel
        type= geometry_msgs/Twist
        desc= Outputs command velocity
      }
    }
    param {
      1{
        name= ~scale_linear
        type= double
        default= 0.5
        desc= The amount to scale the joystick input for the command velocity output.
      }
      2{
        name= ~scale_angular
        type= double
        default= 1.5
        desc=  The amount to scale the joystick input for the command velocity output.
      }
    }
  }
  1{
    name = PS3/XBox Teleop
    desc = The `turtlebot_teleop_joy` provides a generic joystick teleop node.

    pub{
      0{
        name= turtlebot_telop_joystick/cmd_vel
        type= geometry_msgs/Twist
        desc= Outputs command velocity
      } 
    }
    sub{
      0{
        name= joy
        type= sensor_msgs/Joy
        desc= Listens to a joystick commands
      }
    }
    param{
      1{
        name= ~scale_linear
        type= double
        default= 0.5
        desc= The amount to scale the joystick input for the command velocity output.
      }
      2{
        name= ~scale_angular
        type= double
        default= 1.5
        desc=  The amount to scale the joystick input for the command velocity output.
      }
      3{
        name= ~axis_deadman
        type= int
        default= 10
        desc= The joystick index to disables/enables the output cmd_vel message.
      }
      4{
        name= ~axis_linear
        type= int
        default= 1
        desc= The joystick button index to control linear speed
      }
      5{
        name= ~axis_angular
        type= int
        default= 0
        desc= The joystick button index to control angular speed
      }
    }
  }
}
```


