## Supported Hardware

This controller will only work with the Crust Crawler Smart Arm with
Dual Gripper Claw.\
[AX-12 Smart Arm](http://www.crustcrawler.com/products/smartarm/index.php?prod=12)\
[AX-18 Smart Arm](http://www.crustcrawler.com/products/AX-18F%20Smart%20Robotic%20Arm)\
[AX-12/AX-18 Dual Gripper](http://www.crustcrawler.com/products/dualgripper/index.php).

This controller also requires a USB2Dynamixel adapter and a power
supply. We recommend the SMPS2Dynamixel adapter with the Bioloid Kit
power supply.\
[USB2Dynamixel](http://www.trossenrobotics.com/robotis-bioloid-usb2dynamixel.aspx)\
[SMPS2Dynamixel](http://www.trossenrobotics.com/store/p/5886-SMPS2Dynamixel-Adapter.aspx)\
[CM-5 Power Supply](http://www.trossenrobotics.com/bioloid-smps-cm-5.aspx)

## ROS API



```clearsilver
node.0 {
name= smart_arm.yaml
desc=The smart_arm.yaml configuration file contains all the parameters needed by [[dynamixel_controllers]] package's controller_manager node. The launch files provided will place the yaml file on the param server and load a smart_arm_controller by sending a list of joint controllers to the controller_spawner script. The smart_arm will run in the controller_manager node and you can specify angle positions for each joint on the smart arm. Depending on the value in the update_rate parameter, the smart_arm node will publish each joint's current state as well. Each controller type from the yaml file will create Publisher/Subscriber topics with the controller name (see [[dynamixel_controllers]] package documentation for description of available parameters).

pub{
0.name= shoulder_pan_controller/state
0.type= dynamixel_msgs/JointState
0.desc= Joint state data from shoulder_pan joint servo.

1.name= shoulder_pitch_controller/state
1.type= dynamixel_msgs/JointState
1.desc= Joint state data from shoulder_pitch joint servos.

2.name= elbow_flex_controller/state
2.type= dynamixel_msgs/JointState
2.desc= Joint state data from elbow_flex joint servos.

3.name= wrist_roll_controller/state
3.type= dynamixel_msgs/JointState
3.desc= Joint state data from wrist_roll joint servo.

4.name= right_finger_controller/state
4.type= dynamixel_msgs/JointState
4.desc= Joint state data from right_finger joint servo.

5.name= left_finger_controller/state
5.type= dynamixel_msgs/JointState
5.desc= Joint state data from left_finger joint servo.
}

sub{
0.name= shoulder_pan_controller/command
0.type= std_msgs/Float64
0.desc= Subscribes to this topic for new commands. A command tells the shoulder_pan_joint to go to the specified angle in radians.

1.name= shoulder_pitch_controller/command
1.type= std_msgs/Float64
1.desc= Subscribes to this topic for new commands. A command tells the shoulder_pitch_joint to go to the specified angle in radians.

2.name= elbow_flex_controller/command
2.type= std_msgs/Float64
2.desc= Subscribes to this topic for new commands. A command tells the elbow_flex_joint to go to the specified angle in radians.

3.name= wrist_roll_controller/command
3.type= std_msgs/Float64
3.desc= Subscribes to this topic for new commands. A command tells the wrist_roll_joint to go to the specified angle in radians.

4.name= right_finger_controller/command
4.type= std_msgs/Float64
4.desc= Subscribes to this topic for new commands. A command tells the right_finger_joint to go to the specified angle in radians.

5.name= left_finger_controller/command
5.type= std_msgs/Float64
5.desc= Subscribes to this topic for new commands. A command tells the left_finger_joint to go to the specified angle in radians.

6.name= motor_states
6.type= dynamixel_msgs/MotorStateList
6.desc= Subscribes to this topic to get the raw servo feedback from the low-level driver. Uses this information to create the joint states that get published to the arm_controller/joint_move topic.
}
```


