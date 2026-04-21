## Overview

This package is still under development. The goal is to generate a
friction compensation map for each joint of Shadow Robot's Dexterous
Hand.

The friction compensation map is composed of two different maps: one for
when the joint is going forward and the other one for when it's going
backward. Those two maps are different because the tendon path is
different for those 2 movements.

A friction map contains an interpolated piecewise linear function
representing the force necessary to move a joint at a given position,
for the whole range of the joint.

To compute those maps, we save the force applied by the motor and the
joint position while we move the joint through it's whole range at a
very slow and constant speed. We then generate the best piecewise linear
function to represent this data. We repeat while moving the joint in the
other direction.

## How to run the Friction Compensation Algorithm

Simply run: 

```
$ rosrun sr_friction_compensation sr_friction_compensation.py /sr_friction_compensation/FFJ3:=/sh_ffj3_effort_controller/command _sign:=1 _nb_repetition=3
```



The following parameters can be specified:

-   **joint_name**: the name of the joint for which you want to record
    the map (default to FFJ3)
-   **sign** 1 or -1, make sure that when you start the node, the finger
    goes toward the minimum of its range (default to -1)
-   **nb_repetition**: the number of time each map is recorded. The
    bigger the number, the more data you'll have (default to 2)
-   **min**: the minimum of the range (default to 0)
-   **max**: the maximum of the range (default to 1.55)

The result is a plot saved to the current directory. The file is:
**friction_compensation_ffj3.png** (ffj3 is replaced by the joint you
ran the friction compensation on).

## Results

Here is an example of the result you'd get (the 2 maps are displayed on
the same plot).

![forward and backward friction compensation maps](attachment:friction_compensation_FFJ3.png)
