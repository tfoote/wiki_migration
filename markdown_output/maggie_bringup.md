\`maggie_bringup\` is a package that collects together the scripts,
[roslaunch](roslaunch) files, and dependencies that are required to
bring the social robot [Maggie](Robots/Maggie) into a running state.

## HOW TO: Running the complete system

For running all the system is necessary the file
\`maggie_start.launch\`. This launch file contains all nodes to run the
complete [Maggie](Robots/Maggie) robot.

### Example

In a terminal window, start all the process:

```
$ roslaunch maggie_bringup maggie_start.launch
```

## HOW TO: Test a specific functionality

For running the basic of the robot is necessary the file
\`maggie_start_basic.launch\`. This launch file contains all nodes to
run the complete [Maggie](Robots/Maggie) robot.

### Example

-   In a terminal window, start the basic process:

```
$ roslaunch maggie_bringup maggie_start_basic.launch
```

-   In a new terminal window, start the process to be tested.

## HOW TO: Activate the robot

Initially, the robot is in EMERGENCY state. To active the robot, you
need to follow next steps:

1\. Launch at least the basic for the robot, it means,
\`maggie_start_basic.launch\`. 2. Set the robot to STOP state by
touching the head. 3. Press the two buttons bellow on the emergency
remote. Now, the robot is able to move its neck and arms. 4. If you want
to move the base of the robot, it is necessary to set the robot to
ACTIVE state. 5. Touch the shoulders of the robot at the same time. Now,
the robot is able to move around the world.

## Troubleshooting

-   \'\'\'Cannot be found a device.\'\'\'
-   Be sure the robot has the udev rules installed.

```
$ ls -la /etc/udev/rules.d | grep maggie
```

-   If not, install by:

```
$ rosrun maggie_bringup install.sh
```
