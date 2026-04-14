## Preparing the TurtleBot

Before running the follower, make sure your !TurtleBot is setup:

1\. The !TurtleBot laptop must be powered on. 1. The iRobot Create must
be powered on. 1. The !TurtleBot must be placed away from walls and
objects that could confuse the follower. 1. The !TurtleBot must not be
running any other ros programs.

## Use

To start the follower, open an SSH terminal on the !TurtleBot laptop,
and run the following command:

```
roslaunch turtlebot_follower follower.launch
```

The follower should now be running. To initiate following, walk in front
of the !TurtleBot. Then, slowly walk away from the !TurtleBot. The robot
should move forward. Moving close to the !TurtleBot will cause it to
back away. Moving slowly to the left or right will cause the !TurtleBot
to turn. To stop the robot from following, walk quickly away from the
robot.

To get more details about running !TurtleBot follower, please take a
look to the
[TurtleBot follower tutorial](turtlebot_follower/Tutorials/Demo)
