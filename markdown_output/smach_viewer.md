  -- -------------------------------------- -- -- -- ----------------------------- --
     English            [简体中文](cn/smach_viewer)   
  -- -------------------------------------- -- -- -- ----------------------------- --

## Usage



```
rosrun smach_viewer smach_viewer.py
```



This will start the GUI. Once you have one or more state machines
running with an introspection server, they should show up in the GUI.

/!\\ Your state machine needs to run an introspection server to allow
the smach viewer to connect to it. See
[this tutorial](https://index.ros.org/p/smach) for more details.

![width=100%](doc/smach_viewer.png)

## Documentation

### Graph view

The graph view shows all the states of the state machine, connected by
their outcomes. Each node represents a state (or sub state machine), and
each arc represents a state transition. When the outcome of the state is
the same as the outcome of the state machine, there is no arc drawn to
simplify the view. Clicking on "show implicit" will show all state
transitions.

![width="750"](doc/viewer1.png)

### View depth

The "depth" box allows you to expand or collapse sub state machines.
Depth 0 means you only show the top level state machine, depth 1 shows
the first level of sub state machines, etc. Level -1 show all levels.

![width="650"](doc/sm_expanded.png)

### Tree view

It is also possible to show a state machine as a tree. This view makes
it clear that one state machine is a sub state machine of another state
machine.

![width="600"](doc/viewer2.png)

## Tutorials

- [Viewing State Machines (ROS)](https://index.ros.org/p/smach): This
  tutorial shows you how to use the smach viewer, a simple tool to
  monitor state machines and get introspection into the data flow
  between states.

## Troubleshooting

### Check ros master

Make sure the terminal you use to start the smach viewer is connected to
your ros master. To check, run: 

```
rostopic list
```

 and look for
topics of your state machine.

### Check instrospection server

Your state machine needs to run an introspection server to allow the
smach viewer to connect to it. A quick check is:


```
rostopic list | grep "smach/container_status"
```

 If nothing is found, your state machine is not
running an introspection server. See
[this tutorial](https://index.ros.org/p/smach) for more details on how
to run an introspection server.
