## Description

This package contains yaml files and launch files for the laser, camera
and arm of the Wubble robot. All motor ids and angles (in motor ticks)
are specific to the hardware on the Wubble robot. If you are using the
Wubble robot, you should not have to re-configure any of the parameters
in yaml files in this package. All yaml files are used by
[ax12_controller_core](ax12_controller_core) package's
controller_manager.py to setup topics and services which can be used to
control motors. The launch files provided will place the appropriate
yaml file on the param server and load the correct controller(s).

## Supported Hardware

All controllers created by these yaml files are specific to our Wubble
Robot and they assume Dynamixel AX12+ servos.\
[AX-12 Robot Servo](http://www.trossenrobotics.com/dynamixel-ax-12-robot-actuator.aspx)

## ROS API

```clearsilver
node.0 {
name= arm.yaml
desc= The Wubble arm.yaml configuration file contains all the parameters needed by [[ax12_controller_core]] package's controller_manager.py. For complete Publisher/Subscriber and Parameter information please see [[smart_arm_controller]] documentation.
}

node.1 {
name= head_pan_tilt.yaml
desc= Two Dynamixel AX-12+ servos (pan and tilt joints) can be controlled with a pan and tilt angle in (float) radians.
pub{
0.name= head_pan_tilt_controller/state
0.type= ua_controller_msgs/JointStateList
0.desc= Joint state data from the AX-12+ servos.
}
sub{
0.name= head_pan_controller/command
0.type= std_msgs/Float64
0.desc= Subscribes to this topic for new commands. A command tells the head_pan_joint to go to the specified angle in radians.
1.name= head_tilt_controller/command
1.type= std_msgs/Float64
1.desc= Subscribes to this topic for new commands. A command tells the head_tilt_joint to go to the specified angle in radians.
2.name= motor_states
2.type= ax12_driver_core/MotorStateList
2.desc= Subscribes to this topic to get the raw servo feedback from the low-level driver. 
}
}

node.2 {
name= laser_tilt.yaml
desc= One Dynamixel AX-12+ servo creates this joint and it can be controlled with a tilt angle in (float) radians, and the number of cycles.
pub{
0.name= laser_tilt_controller/state
0.type= ua_controller_msgs/JointStateList
0.desc= Joint state data from the AX-12+ servos.
}
sub{
0.name= laser_tilt_controller/command
0.type= std_msgs/Float64
0.desc= Subscribes to this topic for new commands. A command tells the laser_tilt_joint to go to the specified angle in radians.
1.name= motor_states
1.type= ax12_driver_core/MotorStateList
1.desc= Subscribes to this topic to get the raw servo feedback from the low-level driver. 

}
}
```
