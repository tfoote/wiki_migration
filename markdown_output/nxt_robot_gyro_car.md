![\|width=100%](attachment:quick_start.png)

## Running the robot

After building the robot, make sure the sensors and servos are connected
as listed in the robot.yaml file.
<<GetCode(<http://nxt.foote-ros-pkg.googlecode.com/hg/nxt_robots/nxt_robot_gyro_car/robot.yaml,#!python>)>>

Now you can start your base robot: 

```
roslaunch nxt_robot_gyro_car robot.launch
```



To make sure everything is running fine, look at your node graph:


```
rxgraph
```


![\|width=100%](attachment:rxgraph_nxt_robot.png)

Now try driving it around with [nxt_teleop](nxt_teleop).
