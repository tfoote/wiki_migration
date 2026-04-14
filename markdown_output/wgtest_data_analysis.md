## Overview

This package is meant to allow users to analyze WG hardware testing
data. It is meant for internal WG use only. It will not work unless you
have access to the WG Inventory system.

In order to use these tools, you\'ll need to
[install ROS](ROS/Installation) (use the \"pr2all\" install). You\'ll
also need to have the \`wgtest_data_analysis\` package in your
ROS_PACKAGE_PATH.

## Control Chart / Parameter Review

In order to review (or request a change) of a testing parameter, you\'ll
need data to show that the parameter should be changed.

To make a [control chart](http://en.wikipedia.org/wiki/Control_chart)
for test parameters, follow these instructions:

```
rosrun wgtest_data_analysis make_control_chart.py -u USER
``` Enter your username for the WG Inventory
System, it will prompt for your password.

The available tests will display like this: ```
Available tests:
	0: 2966-2 (ID: 48)
	1: 4204-2 (ID: 50)
	2: 4204-l (ID: 49)
	3: 4204-r (ID: 51)
	4: caster-burn (ID: 32)
	5: caster-motor-test (ID: 46)
	6: caster-post (ID: 33)
	7: caster-test (ID: 31)
	8: ctr350-test (ID: 38)
	9: elbow-motor-test (ID: 36)
	10: forearm-roll-test (ID: 13)
	11: gripper-burn (ID: 2)
	12: gripper-motor-test (ID: 35)
	13: gripper-post-test (ID: 3)
	14: gripper-test (ID: 1)
	15: gripper-tip-test (ID: 44)
	16: head-burn (ID: 16)
	17: head-pan-motor-test (ID: 22)
	18: head-post-test (ID: 17)
	19: head-projector-test (ID: 18)
	20: head-test (ID: 15)
	21: head-tilt-motor-test (ID: 11)
	22: hokuyo_test (ID: 37)
        ....
```
Enter the index of the test. In this case, select \`20\` for the
\`head-test\`.

```
Subtests for head-test
	0. Tilt Hysteresis (ID: 24)
	1. Head Checkout (ID: 22)
	2. Pan Hysteresis (ID: 23)
	3. Pan Hysteresis Post-Drop (ID: 99)
	4. Head Drop Test (ID: 98)
	5. Tilt Hysteresis Post-Drop (ID: 100)
Select subtest to examine. Enter index (0, 1, ...):
```

Select the subtest you want to examine, in this case \`0\` for \`Tilt
Hysteresis\`.

Finally, select which measurement you want to plot:
```
Subtest measurements:
	0: Intercept_Negative
	1: Intercept_Positive
	2: Max_Range
	3: Min_Range
	4: Negative_Velocity_Avg
	5: Negative_Velocity_RMS
	6: Negative_Velocity_SD
	7: Positive_Velocity_Avg
	8: Positive_Velocity_RMS
	9: Positive_Velocity_SD
	10: Slope_Negative
	11: Slope_Positive
Select measurement to plot (enter index):
``` Entering \`2\` for \`Max_Range\`, we can make a
plot, or export a CSV.

### Request a Parameter Change

After examining the data, you can request a change to the existing qual
parameters.

Open a ticket
[here](https://code.ros.org/trac/wg-ros-pkg/newticket?component=hardware+test).

Ticket must include:

-   Test name / ID
-   Subtest name
-   Parameter name
-   Requested parameter values
-   CSV of parameter data.

### Troubleshooting

If the plot or CSV has almost no data, select a different parameter. For
example, instead of \"Positive_Effort_Average\", select
\"Positive_Effort_Avg\".

## Determining Test Sequences

To determine if a part is fully tested, you can run the
\`check_tested.py\` script.

```
watts@ckb:/wg/stor5_home4/watts$ rosrun  wgtest_data_analysis  check_tested.py -u USER -d -r 680421301037
Enter your password to the Willow Garage Inventory system
Password: 
All tests complete: False

Test sequence (completed and passed):
	wrist-test (ID: 39) on 03/16/2010 10:01
	wrist-dummy (ID: 40) on 03/18/2010 11:19

Required sequence:
	wrist-test (ID: 39)
	wrist-dummy (ID: 40)
	wrist-burn (ID: 41)
	wrist-dummy (ID: 40)
	wrist-post (ID: 42)
``` Enter the component\'s serial number (ex:
\"680421301037\" above).

Note: For any burn in tests completed before 9/15/2010, the completion
will not be in the log.

## Writing Custom Utilities

```python

#!/usr/bin/env python

import roslib; roslib.load_manifest('wgtest_data_analysis')

from wg_invent_client import Invent
import wgtest_data_analysis.wgtest_accessors as wgtest_access

# Return the percentage of time a subtest has passed
def percent_passed(results):
    count = 0
    passed = 0
    for k, v in results.iteritems():
        if v[0].lower() == 'pass':
            passed += 1
        count += 1

    return passed / count

if __name__ == '__main__':
    # Initialize WG Invent Client
    iv = Invent(sys.argv[1], sys.argv[2])
    
    if not iv.login():
        print >> sys.stderr, "Unable to login to Invent. Try again."
        sys.exit(1)

    percents = {}
    
    for i in range(1, 200):
        # Get subtest result histories
        results =  wgtest_access.get_subtest_results(iv, str(i))

        if not results:
            print >> sys.stderr, "Unable to find results for subtest %d" % i
            break
            
        percents[i] = percent_passed(results)
```
