## Requirements

-   PR2 Robot with gt-ros-pkg repository checked out
-   C-turtle
-   A properly setup
    [ \`laser_interface\`](http://www.ros.org/wiki/laser_interface#Setting_up_and_Running_the_Laser_Detector )
    package.

## Running

### Launching

To quickly get up and running run the following commands:
```
ssh pr2c1 #Replace with the address of your PR2's c1 computer.
roslaunch pr2_laser_follow_behavior follow_pointer.launch 2> /dev/null
```

Note that, by default, this launch script runs the map server with the
map for our building, HSI, so replace the appropriate part of the launch
script for better navigation in your facility. However, this is not
strictly necessary if you\'re not sending any navigation commands.

On another computer with a running X server launch the GUI with:
```
rosrun laser_interface user_interface_node.py
```

### User Interface

With the joystick, position the robot\'s head to point at the floor in
front of it. If you now activate the laser-mouse (make sure your cursor
is over the GUI\'s window) and point it in the field of view of the
robot it should move its head to look at your laser point. When
satisfied with the 3D location that the robot is looking at, double
click the laser-mouse to have the robot drive there. Note that double
clicking while the robot is executing the navigation command will cancel
it.

### Demo State Machine

The demo is governed by a state machine. At start up it launches in the
state \`turn\`, a mode where the robot\'s cameras can be guided by the
laser pointer. When you double click the laser-mouse, the robot will
transition into the state \`move\` and drive to the last seen 3D
location. On receipt of a cancel command (by double clicking) or
notification of success the state machine will transition to back to
\`turn\`.
