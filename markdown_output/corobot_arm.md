## Supported Hardware

This package can be used when your [CoroBot](Robots/Corobot) has any of
the optional arm. It provides some launch files for each possible arm to
launch all the necessary nodes and configuration, as it is different for
every arm. If you want to teleoperate the robot the only thing you need
to do is select the arm you have in the corobot_ros_gui.launch file in
the corobot_teleop package.

## ROS API



```clearsilver
node.0 {
name=corobot_arm
desc=`corobot_arm` is a driver for arm movements. This driver was designed to control the movement of a Corobot's arm.
pub{
0.name= setPositionServo
0.type= corobot_msgs/ServoPosition
0.desc= give an order of angle position for a specific servo motor.
1.name= phidgetServo_setType
1.type= corobot_msgs/ServoType
1.desc= Give the type of servo motor for a specific servo connected to the Phidget.
}
sub{
0.name= armPosition
0.type= corobot_msgs/MoveArm
0.desc= command to move a servo of the arm
}
param{
0.name= dynamixels
0.type= XmlRpcValue
0.default= 0
0.desc= Configuration of all the servos of the arm. Given in yalm file
1.name= controller_type
1.default= 0
1.type= String
1.desc= type of servo controller board: arbotix, ssc32 or phidget. Given in yalm file.
}

}
```


