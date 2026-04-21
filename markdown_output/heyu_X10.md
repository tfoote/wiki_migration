## Installation

You'll need a working copy of the heyu software installed at the
standard location (/usr/local/bin/heyu). Here's a good
[FAQ](http://www.grep-ros.net/x10/heyu-x10/heyu-x10-install/) on how to
install it.

Just download the code in the directory you want:


```
bzr branch lp:ros-heyu-x10
```



Then, you can edit your config_file_path (in
heyu_x10/heyu_X10/src/heyu_node.py) (this will be set as a parameter
some day).

Locate the full path to heyu_X10 ros package and add it to the code to
your ROS_PACKAGE_PATH (you should probably add this to your .bashrc)
e.g.: export ROS_PACKAGE_PATH=/path/to/code:\${ROS_PACKAGE_PATH}

Then build it: eventhough it's a python node, you need to generate the
services, etc\... 

```
rosmake heyu_X10
```



If you want to get the latest version, just run:


```
roscd heyu_X10 ; bzr pull lp:ros-heyu-x10
```



Do not forget to rebuild the update with: rosmake heyu_X10

## Getting Started

Start the roscore in a console: 

```
roscore &
```

 Then just start
the node: 

```
rosrun heyu_X10 heyu_node.py
```



If you want to start one of your appliances (replace True by False if
you want to stop it): 

```
rosservice call /heyu/back_porch/command True
```



If you want to check the status of your appliances:


```
rosservice call rosservice call /heyu/back_porch/state
```



You can of course replace bedroom_light by your other appliances. If you
want to get a list of the possible appliances, you can run:


```
rosservice list
```


