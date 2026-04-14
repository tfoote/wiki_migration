## Usage

```
rosrun smach_recovery_viewer smach_viewer.py
```

This will start the GUI and help visualize the transitions in the state
machine much like in the original SMACH package. The GUI also shows you
the ORACLE state which controls failure recovery.

/!\\ Your state machine needs to run an introspection server to allow
the smach recovery viewer to connect to it. See
[this tutorial](recovery_tutorials) for more details.

![\|width=100%](attachment:oracle_sm.png)

## Documentation

The functionality provided in the smach_recovery_viewer is similar to
the [\|smach_viewer](smach_viewer). It also provides the added
functionality of viewing the oracle transitions and current transition
matrices along with failure rates.

/!\\ State Machines written for RECOVERY SMACH will not work with the
regular SMACH VIEWER you need to use the SMACH RECOVERY VIEWER. However
state machines written for regular SMACH can be used with the RECOVERY
SMACH VIEWER if the proper packages are imported
