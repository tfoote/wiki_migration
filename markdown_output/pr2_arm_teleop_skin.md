This package contains two collision avoiding teleops. One teleop that
should be used with the controller in the
[reactive_trajectory_controller](reactive_trajectory_controller) and
another one that implements the collison avoidance routines on it's
own.

Both teleops are highly experimental! They do not guarantee 100% safety,
but almost 100%

To run the teleops you need a PS3 joystick. Information about using PS3
joysticks in ROS can be found here

<http://www.ros.org/wiki/ps3joy/Tutorials/PairingJoystickAndBluetoothDongle>,

here: [joy](joy), and here: [ps3joy](ps3joy)

## Running the standalone teleop

To run the standalone teleop you first have to run the collision
environment if you do not have any running.



```
roslaunch pr2_arm_teleop_skin teleop_environment.launch
```

 Now you are ready to launch the standalone
teleop:



```
roslaunch pr2_arm_teleop_skin teleop_standalone.launch
```

 To drive the robot around you have to press the
deadman button which is button 1 on the left side. To move the arms
around you have to press button 1 on the left side and button 1 on the
right side at the same time. If you want to change the orientation of
the gripper you have to press button 1 on the left side and button 1 and
2 on the right side.

## Running the teleop with the reactive trajectory controller

The other teleop does not have any collision avoidance routines they are
located in the
[reactive_tracjetory_controller](reactive_tracjetory_controller). You
first have to launch this controller, see documentation in
[reactive_trajectory_controller](reactive_trajectory_controller).

Then you can run teleop with



```
roslaunch pr2_arm_teleop_skin teleop.launch
```

 The usage is the same as with the standalone
teleop.

## Add obstacles with the proximity sensor

After you started your teleop you have a running environment server
either which teleop you ran. So you can use the proximity sensor to add
obstacles to that environment server.



```
roslaunch proximity_sensor_add_obstacles add_obstacles.launch
```

 However, you do not need to use the proximity
sensor to build your collision map, you can use whatever sensor (or
sensors) you want.
