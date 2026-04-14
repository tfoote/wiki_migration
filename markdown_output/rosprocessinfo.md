# ROS Process Info

A simple node to convert the Process Info of your node-process to a ROS
Topic.

## Installation

```
$ bzr branch lp:rosprocessinfo ~/ros/
$ export ROS_PACKAGE_PATH=~/ros/rosprocessinfo:$ROS_PACKAGE_PATH
$ rosmake rosprocessinfo
```

## Usage

Suppose you want to log the process information of nodes: /node/name1
/node/name2

```
$ rosrun rosprocessinfo /node/name1 /node/name2
```

This will should publish new topics with names
\"/node/name1/processinfo\", \"/node/name2/processinfo\".

```
$ rostopic list | grep processinfo
/node/name1/processinfo
/node/name2/processinfo
```

You are all set. You can use these topics in any way you want. To plot
them with rxplot use ```
$ rxplot /node/name1/processinfo/RSS:SIZE /node/name1/processinfo/CPU
```

To record them into bagfiles use: ```
$ rosbag record /node/name1/processinfo /node/name2/processinfo
```
