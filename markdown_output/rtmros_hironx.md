[Included page Industrial/Software_Status/Developmental not found](Included page Industrial/Software_Status/Developmental not found)

## Software component

[Included page rtmros_nextage/Tutorials/Install NEXTAGE OPEN software on your machine,,from=\"##begin_swcomponent_hironx_nxo\",to=\"##end_swcomponent_hironx_nxo\" not found](Included page rtmros_nextage/Tutorials/Install NEXTAGE OPEN software on your machine,,from="##begin_swcomponent_hironx_nxo",to="##end_swcomponent_hironx_nxo" not found)

### Note for Coordinate Frames for Hironx

Root of the frame tree is \`WAIST\` (instead of
[ROS standard](http://www.ros.org/reps/rep-0105.html#base-link)
\`base_link\`) due to the fact that originally this robot wasn\'t made
to work on \`ROS\`.

## Media coverage

ROS news related to \`Hiro\` twin-arm robot:

-   [Tecnalia wins the \"Factory of the Future\" award at European Manufacturing Awards 2012 with a robot programed in ROS](http://www.ros.org/news/2013/01/tecnalia-wins-the-factory-of-the-future-award-at-european-manufacturing-awards-2012-with-a-robot-pro.html)

## Installation, usage

Full-fledged user document incl. writing codes is found
[here](rtmros_nextage/Tutorials).

## FAQ

### Moveit and dynamic scenes with HiroNXO

```
Can moveit plan a path and then change it during execution because a new obstacle
 appeared in the path? There are `move_group.plan()` and `move_group.go()` for static
 scenes. Do I need other commands for dynamic scenes?
```

For MoveIt! related feature, HiroNXO does no customization. So follow
general \`MoveIt! way\`. MoveIt! has \"allow re-plan\" feature.
[This post](https://groups.google.com/d/msg/moveit-users/IuZKCxsCvJo/dn_HYJ4gKj8J)
might be of your interest.

### Controlling joint motors directly with \`Joint Trajectory Action Interface\`

```
At the moment I am working on the low level API, the joint trajectory action
 interface to control the robot. Is it true that the joint trajectory controller 
 directly control the joints (joint motors) of the robot? Because I thought that 
 the robot can only be accessed via CORBA and ROS does not know anything about CORBA.
```

Your observation is correct; NEXTAGE OPEN does not provide direct
controller access to the motor, from both ROS API and hrpsys API. This
question is heard multiple times but the root is in its hardware API
limitation that we, as the robot\'s opensource API maintainer, don\'t
have control over.

### Correct physical behavior of the simulator

```
Another question is, if the hrpsys simulator can also simulate the correct physical
 behavior when we control the joints directly (with Joint Trajectory Aciton). 
 Let’s say my controller parameters are chosen wrong.. Will the robot arm overshoot?
```

TBA
