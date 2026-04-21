## Documentation

The `urdfdom_py` package provides the `urdf_parser_py` Python module
providing both functions to parse an URDF model from a file or the
parameter server and Python classes mapping the URDF information to a
Python structure.

The `display_urdf` script allows the user to display the parsing
result. It can be used either with a path to an URDF file (i.e. `rosrun
urdf_parser_py display_urdf /tmp/robot.urdf`) or without any argument.
In this case, it connects to the parameter server to retrieve the robot
configuration.



```shell
# Display the PR-2 model.
rosrun urdf_parser_py display_urdf `rospack find pr2_mechanism_model`/pr2.urdf
```



### History

This package comes from the following prior packages: [urdfpy](urdfpy),
[urdf_python](urdf_python), [urdf_parser_python](urdf_parser_python),
and [robot_model_py](robot_model_py).

[urdf_parser_py](urdf_parser_py) presently has its own package page,
which redirects here.

## Python API

Here is a brief example showing the different ways to load/parse a URDF
model.



```python

# Load the urdf_parser_py manifest, you use your own package
# name on the condition but in this case, you need to depend on
# urdf_parser_py.
import roslib; roslib.load_manifest('urdfdom_py')
import rospy

# Import the module

from urdf_parser_py.urdf import URDF

# 1. Parse a string containing the robot description in URDF.
# Pro: no need to have a roscore running.
# Cons: n/a
# Note: it is rare to receive the robot model as a string.
robot = URDF.from_xml_string("<robot name='myrobot'></robot>")

# - OR -

# 2. Load the module from a file.
# Pro: no need to have a roscore running.
# Cons: using hardcoded file location is not portable.
robot = URDF.from_xml_file()

# - OR -

# 3. Load the module from the parameter server.
# Pro: automatic, no arguments are needed, consistent
#      with other ROS nodes.
# Cons: need roscore to be running and the parameter to
#      to be set beforehand (through a roslaunch file for
#      instance).
robot = URDF.from_parameter_server()

# Print the robot
print(robot)
```

 Once you have retrieved the `robot` object,
please consult the package Python API to know how to browse the
structure.
