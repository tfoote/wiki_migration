## Overview

This tutorial package provides a `turtle_tf_broadcaster` and
`turtle_tf_listener` for teaching the basic concepts of tf. The
default demo will cause turtle2 to follow turtle1, the
[tf tutorials](tf/Tutorials) extend this demo.

## Running the Tutorial Code

To run the default example, start by getting the required dependencies
and making the package.



```
$ rosdep install turtle_tf
$ rosmake turtle_tf
```



Then in `roslaunch` the demo: 

```
$ roscd turtle_tf
$ roslaunch launch/turtle_tf_demo.launch
```



You will see the turtlesim start with two turtles.

. ![](attachment:tf/Tutorials/Introduction to tf/turtle_tf_start.png)

Once the turtlesim is started you can drive the center turtle around in
the turtlesim using the keyboard arrow keys, **select the roslaunch
terminal window** so that your keystrokes will be captured to drive the
turtle.

. ![](attachment:tf/Tutorials/Introduction to tf/turtle_tf_drive.png)

As you can see that one turtle will continuously move to follow the
turtle you are driving around.
