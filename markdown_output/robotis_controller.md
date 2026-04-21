*ROS Software Maintainer: [ROBOTIS](http://wiki.ros.org/ROBOTIS)*

## ROBOTIS e-Manual

-   [ROBOTIS e-Manual for ROBOTIS Controller](http://emanual.robotis.com/docs/en/software/robotis_framework_packages/#robotis_controller)

## ROS API



```clearsilver
node.0 {
name=robotis_controller

pub{
  0{
    name= /robotis/goal_joint_states
    type= sensor_msgs/JointState
    desc= The message publishes goal joint status value for each joint.
   }
  1{
    name= /robotis/present_joint_states
    type= sensor_msgs/JointState
    desc= The message publishes present joint status value read from each joint.
   }
  2{
    name= /robotis/present_joint_ctrl_modules
    type= robotis_controller_msgs/JointCtrlModule
    desc= The message publishes current status of motion module that controls each joint.
   }
}

sub{
  0{
    name= /robotis/write_control_table
    type= robotis_controller_msgs/WriteControlTable
    desc= The message can write multiple item values to a specific joint by using Sync Write.
   }
  1{
    name= /robotis/sync_write_item
    type= robotis_controller_msgs/SyncWriteItem
    desc= The message can write a specific item value to multiple joints by using Sync Write.
   }
  2{
    name= /robotis/set_joint_ctrl_modules
    type= robotis_controller_msgs/JointCtrlModule
    desc= The message can configure motion modules that controls specific joints.
   }
  3{
    name= /robotis/enable_ctrl_module
    type= std_msgs/String
    desc= This message assigns a specific motion module that manages specific joints to a motion control module.
   }
  4{
    name= /robotis/set_control_mode
    type= std_msgs/String
    desc= The message sets the control mode of `robotis_controller` to ether `DIRECT_CONTROL_MODE` or `MOTION_MODULE_MODE`.
   }
  5{
    name= /robotis/set_joint_states
    type= sensor_msgs/JointState
    desc= This message includes status data for each joint. The data in this message is transmitted to each joint to control the joint.
   }
  6{
    name= /[gazebo_robot_name]/joint_states
    type= sensor_msgs/JointState
    desc= This message includes status data for each joint from gazebo. When gazebo mode is enabled, the data in this message is transmitted to each joint to control the joint.
   }
}

srv{
  0{
    name= /robotis/get_present_joint_ctrl_modules
    type= robotis_controller_msgs/GetJointModule
    desc= The service to get the configuration of motion module that controls each joint.
   }
  1{
    name= /robotis/set_present_joint_ctrl_modules
    type= robotis_controller_msgs/SetJointModule
    desc= The service to set the configuration of motion module that controls each joint.
   }
  2{
    name= /robotis/set_present_ctrl_modules
    type= robotis_controller_msgs/SetModule
    desc= The service to set the configuration of motion module that controls all joints.
   }
}
```


