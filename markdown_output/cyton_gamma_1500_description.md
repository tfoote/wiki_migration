This package contains the URDF description file for the Robai Cyton
Gamma 1500 robot manipulator.

# Installation

You can use git clone to install the package.

```
cd <your_catkin_ws>/src
git clone https://github.com/GertKanter/cyton_gamma_1500_description.git
cd ..
catkin_make
```

Building it with *catkin_make* will allow using *roslaunch* and *find*
later.

# Usage

You can view the model in RViz and move the joints manually (if you have
joint_state_publisher, robot_state_publisher and rviz installed).

```
roslaunch cyton_gamma_1500_description cyton_gamma_1500.launch
```

# Screenshot

[![URDF in RViz\|width=600](attachment:cyton_gamma_1500.png)](attachment:cyton_gamma_1500.png)
