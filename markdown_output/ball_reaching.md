## Description

![\|width=760](attachment:control-graph.png) The control graph (picture
above) is created by python script "reach_ball.py". This script is
parsed by the interperter embedded in the control framework SoT running
on HRP-2 control CPU.

Script "hueblob.py" listen to tf and publishes in topic
'/wide/blobs/rose/transform_base_link' the position of the ball in the
frame of the robot waist. Note that the position of the ball in the
camera reference frame is computed by package [hueblob](hueblob).

"watch_zone.py" implements an [actionlib](actionlib) server that
tracks the position of the ball and returns when the distance between
the ball and the target is less than the tolerance distance.

"supervisor.py" send a request to watch_zone server and triggers the
motion when the client returns.

## Running the motion on HRP-2 14

**Prerequisite**: the robot is calibrated.

ssh on hrp2014v and run 

```sh
roslaunch hrp2_bringup cameras.launch
```

 ssh on hrp2014v and run


```sh
roslaunch hrp2_bringup openhrp_bridge.launch
rosservice call restart_controller
```

 switch relay on, ssh on hrp2014v and run


```sh
rosservice call switch_servo True all
rosservice call start_dynamic_graph
```

 then put the robot down. ssh -Y on hrp2014v and
run 

```sh
roslaunch ball_reaching robot.launch
```

 Then take the ping ball and move it in
front of the robot. When the ball reaches the target position (specified
in supervisor.py script) in the waist coordinate frame, up to 5 cm, the
robot grabs the ball and moves back to rest position.
