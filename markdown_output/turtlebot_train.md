## Hardware Requirements

You'll need a TurtleBot!
[Don't have one yet?](http://clearpathrobotics.com/turtlebot)

## Example

Use the launch file 

```
roslaunch turtlebot_train train.launch
```

 Make sure the robot starts
with a good amount of floor area in it's view so that it can properly
calibrate the floor plane.

(Edit; 12/8/2011) If `turtlebot` doesn't move even though it shows
the x-z distance of another turtlebot on commandline, you might want to
modify the `launch` file as following (probably due to
[this ticket](https://kforge.ros.org/turtlebot/trac/ticket/86)).


```
Before;    <param name="out_vel"               value="/turtlebot_node/cmd_vel" />
 After;     <param name="out_vel"               value="/cmd_vel" />
```


