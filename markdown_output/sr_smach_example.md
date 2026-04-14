## Overview

This uses the [smach](smach) package to implement a small demo using a
State Machine. The demo is simply a succession of simple movements (e.g.
beckon with a finger, show your muscles, etc\...), with a state for
checking if we\'re getting to the targets or not between each of the
different positions.

You can see the state machine below:
![Demo using SMACH\|width=100%](attachment:sr_smach.png)

## Running the Demo

To start it, just run: ```
$ roslaunch sr_smach_example sr_smach.launch
```

It will start the demo as well as the
[state machine visualizer](smach_viewer).
