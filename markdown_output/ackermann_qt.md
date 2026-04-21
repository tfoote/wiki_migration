Qt tele-operation interface for driving a vehicle with Ackermann
steering under human control.

## ROS Nodes



```clearsilver
node.0 {
 name = qteleop
 desc = ROS node for issuing commands to a robot using Ackermann steering from a Qt window. 
 pub {
  0.name= ackermann_cmd
  0.type= ackermann_msgs/AckermannDriveStamped
  0.desc= commands for a robot using Ackerman steering.
}
}
```



#### Example

Run the teleop script. 

```
rosrun ackermann_qt qteleop
```


