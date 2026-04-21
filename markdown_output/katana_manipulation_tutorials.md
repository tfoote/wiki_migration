## simple_pick_and_place_test

See [katana_driver](katana_driver).

## get_fk / get_ik

clone fixed version of arm_navigation (in the official Fuerte version,
the kinematics services don't work): ```
git clone -b fix_kinematics_services_fuerte https://github.com/uos/arm_navigation.git
rosmake arm_navigation    # for this to work, the directory you just cloned needs to be on the ROS_PACKAGE_PATH *before* /opt/ros/fuerte/...
```

launch prerequisites: ```
roslaunch kurtana_gazebo kurtana_gazebo.launch
roslaunch kurtana_arm_navigation kurtana_arm_navigation.launch
```

run tests: ```
rosrun katana_manipulation_tutorials get_fk
rosrun katana_manipulation_tutorials get_ik
```

alternatively, run get_fk from the command line:
```
rosservice call /kurtana_arm_kinematics/get_fk '{header: {frame_id: "katana_base_link"}, fk_link_names: ["katana_motor5_wrist_roll_link"], robot_state: {joint_state: {name: ["katana_motor1_pan_joint", "katana_motor2_lift_joint", "katana_motor3_lift_joint", "katana_motor4_lift_joint", "katana_motor5_wrist_roll_joint"], position: [0.0, 0.0, 0.0, 0.0, 0.0]}} }'
```
