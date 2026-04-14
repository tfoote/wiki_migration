\<\<GitHubIssues(MarkNaeem/move_base_sequence)\>\>

## Overview

This is a ROS package that uses a ROS Action server to manage sending
multiple goals to the navigation stack (move base action server) on a
robot in order to achieve them one after another. The package handles
everything regarding the goals: receiving, storing, sending, error
handling\... etc.

A demo showing the package while running on turtlebot3:
[Youtube](https://www.youtube.com/watch?v=afTX3Mg4qq4)

Check:
[Readme file on GitHub](https://github.com/MarkNaeem/move_base_sequence/blob/main/README.md)

## Nodes

```clearsilver
node.0 {
  name=move_base_sequence
  desc= The main and only node in the package.This is where the action server runs.
  sub{
    0.name= wayposes
    0.type= geometry_msgs/PoseArray
    0.desc=  a visualization topic that shows the registered goals. It can also be sued to pass precalculated set of goals all at once by publishing on it..
    1.name= corner_pose
    1.type= geometry_msgs/Pose
    1.desc= the topic that is used to append new goals to the goals sequence.
  }
  pub{
    0.name= wayposes
    0.type= geometry_msgs/PoseArray
    0.desc=  a visualization topic that shows the registered goals. It can also be sued to pass precalculated set of goals all at once by publishing on it..
    1.name= path
    1.type= nav_msgs/Path
    1.desc= visualization topic that draws the path that connects goals together.
  }
``` note: A robot using move base sequence can have
two states: paused: paused state stops the move base server and stops
the sequence server so the robot stays at its place. operating:
operating state means that the sequence server will be sending goals and
waiting for move base response. In other words, the system will be fully
functioning until something causes state to change to paused (e.g. a
goal cancellation or abortion).

## Parameters

```clearsilver
param{
  no_header=True
  0.name = move_base_sequence/abortion_behaviour
  0.default = 'stop'
  0.type = Str
  0.desc = determines the behaviour of the robot should the move base server face any problems that cause goal abortion. Default is 'stop' but it can be set to 'continue' which will make the system ignore this goal and take the next one in the sequence. It takes 'continue' and 'stop' as strings.
  1.name = move_base_sequence/is_repeating
  1.default = True
  1.type = Bool
  1.desc =  determines whether the robot should be looping on the goals in an infinite loop which is the default value and set to be True, or it should only achieve them once, delete them, and wait for new goals, which is set by False.
}
``` \<\<MsgSrvDoc(move_base_sequence)\>\>
