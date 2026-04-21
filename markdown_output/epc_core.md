## Code Organization

The code is organized in three separate directories within the `src/`
directory: 1. `epc_core`: robot-agnostic code defining the core EPC
function and a few simple examples. 1. `pr2_arms`: Python code to
control the PR2 as well as perform kinematic computations using KDL. 1.
`cody_arms`: Python code to control Meka arms on the robot Cody in the
Healthcare Robotics Lab, Georgia Tech.

## Running on a PR2

To move the right arm to its home position (zero joint
angles):

```
$ roscd epc_core/src/epc_core
$ python epc.py
```


