## Hardware Requirements

To use this package you need either a real Care-O-bot or you can use a
simulated one.

## ROS API

The [cob_2dnav](cob_2dnav) package uses the ROS [navigation](navigation)
stack to navigate with the robot.

## Usage/Examples

Building all packages needed for cob_2dnav 

```
rosdep install cob_2dnav
rosmake cob_2dnav
```



Make sure you started either a real robot or a simulated one using
[cob_bringup](cob_bringup).

Start the 2D navigation with 

```
roslaunch cob_2dnav 2dnav.launch
```



### Using rviz to localize the robot and send goals to the navigation

Please localize the robot and send some navigation goals following the
[rviz navigation stack tutorial](navigation/Tutorials/Using rviz with the Navigation Stack).

### Using the Care-O-bot dashboard

If the robot is localized you can use the [cob_dashboard](cob_dashboard)
to send navigation goals.

### Sending goals from code

A tutorial on sending goals to the [navigation](navigation) stack with
code can be found [ here](navigation/Tutorials/SendingSimpleGoals ).
