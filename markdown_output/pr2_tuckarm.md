## Bring up the robot

As with all applications, you must first
[bring up your robot](pr2_apps#bringup).

## Launching

### Boxturtle

The tuck arm application is a Python script, \`tuckarms.py\`:
```
USAGE: tuck_arms.py [b | l | r]
```

For example, to tuck both arms: ```
rosrun pr2_tuckarm tuck_arms.py b
```

### C-turtle or newer versions

The tuck arm application is a Python script, \`tuck_arms.py\`:
```
USAGE: tuck_arms.py [-r <action>] [-l <action>]; <action> is '(t)uck' or '(u)ntuck'.
```

For example, to tuck both arms: ```
rosrun pr2_tuckarm tuck_arms.py -r t -l t
```

or to untuck the right arm only: ```
rosrun pr2_tuckarm tuck_arms.py --right untuck
```

If this runs properly, you will see the PR2 tuck each of its arms in
turn and see something like the following feedback in the terminal:

-   Waiting for controller manager to start
-   Tucking both left and right arm
