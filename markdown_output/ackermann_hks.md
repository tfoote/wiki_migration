HKS game controller tele-operation interface for driving a vehicle with
Ackermann steering under human control.

## ROS Nodes

```clearsilver
node.0 {
 name = hks_teleop
 desc = ROS node for issuing commands to a robot using Ackermann steering from using an HKS game controller. 
 pub {
  0.name= ackermann_cmd
  0.type= ackermann_msgs/AckermannDriveStamped
  0.desc= commands for a robot using Ackerman steering.
}
}
```

#### Example

Run the teleop script. ```
rosrun ackermann_qt hks_teleop
```

#### Usage

Plug the joystick into a USB 2.0 port. When first attached, four blue
LEDs will blink, and the joystick is not yet active. Press the PS
button, causing the blinking to stop, and the controller to connect.

![](attachment:HKS-controller.jpg)

Controls:

1\. Press \"PS\" button when controller first attached. 1. Use thumb
wheel to steer left or right. 1. Press blue \"X\" button to speed up. 1.
Press purple square button to slow down.
