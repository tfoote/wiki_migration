  -- ------------------------- -- -- -- ----------------------------- --
     [English](smach_viewer)            [简体中文](cn/smach_viewer)   
  -- ------------------------- -- -- -- ----------------------------- --

## Usage

```
rosrun smach_viewer smach_viewer.py
```

This will start the GUI. Once you have one or more state machines
running with an introspection server, they should show up in the GUI.

/!\\ Your state machine needs to run an introspection server to allow
the smach viewer to connect to it. See
[this tutorial](smach/Tutorials/Smach Viewer) for more details.

![\|width=100%](attachment:smach/smach_viewer.png)

## Documentation

### Graph view

The graph view shows all the states of the state machine, connected by
their outcomes. Each node represents a state (or sub state machine), and
each arc represents a state transition. When the outcome of the state is
the same as the outcome of the state machine, there is no arc drawn to
simplify the view. Clicking on \"show implicit\" will show all state
transitions.

![\|width=\"750\"](attachment:viewer1.png)

### View depth

The \"depth\" box allows you to expand or collapse sub state machines.
Depth 0 means you only show the top level state machine, depth 1 shows
the first level of sub state machines, etc. Level -1 show all levels.

![\|width=\"650\"](attachment:smach/Tutorials/Create a hierarchical state machine/sm_expanded.png)

### Tree view

It is also possible to show a state machine as a tree. This view makes
it clear that one state machine is a sub state machine of another state
machine.

![\|width=\"600\"](attachment:viewer2.png)
