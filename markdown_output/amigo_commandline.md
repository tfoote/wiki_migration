# Under Construction

This package has not been released yet, but will be soon.

# Package Summary

This package contains a command-line tool used for easy user control of
the joints of AMIGO.

# Functional Description

This tool translates terminal input with desired joint positions into
[ JointState messages](std_msgs ). These are subsequently published for
the controllers on the reference topic corresponding to the value of
CONTROLLER. Additional documentation of the C++ files can be found as
doxygen at **INSERT LINK HERE**

# Use

To set a reference a controller, type: 

```
$rosrun amigo_commandline set_reference <part name> {<joint1position>, <joint2position>, ... }
```

 For
example, to set a reference for the base type: 

```
$rosrun amigo_commandline set_reference base <x velocity> <y velocity> <angular velocity>
```


and for the left arm: 

```
$rosrun amigo_commandline set_reference left_arm 0 1 0 1.2 0.4 0 -0.5
```



The controllers for left_arm and right_arm expect seven joints,
left_gripper and right_gripper expect two joints, the spindle expects
one joint and head expects two joints.

The limits and initial position of each joint are given in the following
tables:

  -- ---------------------- -- ---------------------- -- ----------------- -- ----------------- --
     **Arms**                  **Initial position**      **Lower limit**      **Upper limit**   
     shoulder_yaw_joint        0                         -1.57                0                 
     shoulder_pitch_joint      -0.4                      -1.57                1.57              
     shoulder_roll_joint       0                         -1.57                1.57              
     elbow_pitch_joint         1.2                       0                    2.23              
     elbow_roll_joint          0                         -1.83                1.83              
     wrist_pitch_joint         0.8                       -0.95                0.95              
     wrist_yaw_joint           0                         -0.61                0.61              
  -- ---------------------- -- ---------------------- -- ----------------- -- ----------------- --

  -- ----------------- -- ---------------------- -- ----------------- -- ----------------- --
     **Head**             **Initial position**      **Lower limit**      **Upper limit**   
     neck_pan_joint       0                         -1.58                1.58              
     neck_tilt_joint      0                         -1.58                1.58              
  -- ----------------- -- ---------------------- -- ----------------- -- ----------------- --

  -- --------------- -- ---------------------- -- ----------------- -- ----------------- --
     **Grippers**       **Initial position**      **Lower limit**      **Upper limit**   
     finger1_joint      0                         -0.3                 0.25              
     finger2_joint      0                         -0.25                0.3               
  -- --------------- -- ---------------------- -- ----------------- -- ----------------- --

  -- --------------- -- ---------------------- -- ----------------- -- ----------------- --
     **Spindle**        **Initial position**      **Lower limit**      **Upper limit**   
     spindle_joint      0.35                      0                    0.5               
  -- --------------- -- ---------------------- -- ----------------- -- ----------------- --

Be mindfull that the left and right versions of joints might behave
differently (opposite) if set to the same position. Additional
information on all of these joints can be found in the yaml files in
[ amigo_controller_configuration_gazebo](amigo_controller_configuration_gazebo )
