

## Tutorials

- [Running PR2 Counterbalance Check](#running-pr2-counterbalance-check):
  Shows how to run the counterbalance adjustment test on the PR2.

## Running PR2 Counterbalance Check

### Overview

Over time, the counterbalance on your PR2 will go out of adjustment. It
is important to tune the counterbalance periodically. The counterbalance
is adjusted by tuning the secondary spring, and the arm gimbal shaft.

The PR2 counterbalance adjustment tool allows you to estimate the
counterbalance adjustment required to return the arm to the minimum
torque state.

**Note:** Complete instructions for adjusting the PR2 counterbalance are
available at support.willowgarage.com. These instructions are for
running adjustment check program only. Do not proceed without
understanding the procedures at support.willowgarage.com. Adjusting the
counterbalance is a risky activity and can cause harm to you and the
PR2.

### Running the CB Check Tool

To run the counterbalance check tool, you will need to launch the robot.
The CB check tool is released against **cturtle** only, so start the
robot with cturtle.

After the robot starts up, verify that all the joints are calibrated.
Start up the joystick, and drive the spine up to the maximum height.


```
roslaunch pr2_teleop teleop_joystick.launch
```



#### Pre-start Checklist

Before you check the CB adjustment, make sure you have completed these
steps:

- Spine is **UP**
- Both arms of robot have 5' of clear space
- Shoulder pan joints are separated by 90 degrees, arms can't collide
- Foam covers installed on arms
- Robot WAN port is plugged in (for display tool)

**Note:** Failure to complete these steps may cause damage to the PR2 or
personal injury.

#### Launching the Adjustment Controller

To launch the adjustment controller, you will have to load a launch file
that holds the arms in place, and runs a check command on the arms.



```
roslaunch pr2_counterbalance_check counterbalance_test_[left|right].launch
```



The arm controllers should take 1-2 minutes each to gather data on the
arms. During this test, they will shake the arms to break static
friction. This is normal, do not abort the test for shaking.

#### Getting CB Adjustment

While the counterbalance test is still running but after the arm has
stopped moving, use the `cb_check.py` tool in
`pr2_counterbalance_check` to get the proper adjustment,



```
rosrun pr2_counterbalance_check cb_check.py `rospack find pr2_counterbalance_check`/cb_data/counterbalance_model.dat
```



This tool will use training data to analyze the PR2 counterbalance and
recommend an adjustment. The output of the tool will look like this:


```
Calculated counterbalance adjustment:
        Secondary Spring: 3.0 (CCW)
        Arm Gimbal Shaft: 0.4 (CCW)
Make sure to follow proper adjustment procedures if you choose to make an adjustment.
```



For the above, you would turn the secondary spring 3.0 turns CCW
(counter-clockwise) and the arm gimbal shaft 0.4 turns CCW.

You can check the recommended tolerance using the `-t` option.


```
$ rosrun pr2_counterbalance_check cb_check.py -t
Recommended CB tolerances for secondary spring, arm gimbal shaft
	Secondary spring: +/-2.0
	Arm Gimbal Shaft: +/-0.8
If your recommended adjustment is less than this many turns, do not adjust your CB
```



**Note:** Choosing to adjust your PR2 counterbalance is your decision.
The tolerances are only recommendations.

##### Training Data

In order to recommend an adjustment, the `cb_check.py` tool needs
*training data*. The recommended data is in
`pr2_counterbalance_check/cb_data`. If you have an non-standard arm
configuration, you can record your own training data with
`pr2_counterbalance_check/training/counterbalance_training.py`.
Instructions to do this are in the usage of that node.

Recording training data is for advanced users only. Do not attempt to
record training data.

### Checking Counterbalance Post-Adjustment

In most cases, the adjustment tool will recommend an adjustment that is
correct in one try. You should always recheck the counterbalance to make
sure that the adjustment tool did not malfunction. Follow the above
instructions to re-run the adjustment tool after you have adjusted the
counterbalance.
