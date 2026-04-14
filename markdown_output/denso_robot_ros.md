```html
<div style="position: relative; margin-top: -1%;">
 <ul>
   <li><a href="http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform"><img src="https://img.shields.io/badge/support%20level-consortium%20%26%20vendor-green.png"/></a></li>
 </ul>
</div>
```

## Overview

[denso_robot_ros](https://github.com/DENSORobot/denso_robot_ros.git)
contains packages that provide nodes for communication with DENSO
Industrial robot controllers (RC8/RC8A and RC9).

The robot controller models are as follows.

　・[RC8 controller](https://www.denso-wave.com/en/robot/product/controller/rc8.html)

　・[RC8A controller](https://www.denso-wave.com/en/robot/product/controller/rc8a.html)

　・[RC9 controller](https://www.denso-wave.com/en/robot/product/controller/rc9.html)

The robot models are as follows.

　・[4-Axis (SCARA) robots](http://www.denso-wave.com/en/robot/product/four/index.html)

　・[5-and 6-Axis robots](http://www.denso-wave.com/en/robot/product/five-six/index.html)

　・[Collaborative robots](https://www.denso-wave.com/en/robot/product/collabo/)(not
[OSS type](http://wiki.ros.org/denso_cobotta_ros))

It provides an URDF model for VS060 and an associated [MoveIt](moveit)
configuration package as a standard component. To control other robot
types, see the [ROSConverter](denso_robot_ros/ROSConverter) page for
creating the URDF model and the associated [MoveIt](moveit)
configuration package.

## Installation

The packages in the main repository have been released into ROS Indigo
on Ubuntu, making installation through \`apt-get\` or synaptic possible.
Other Linux distributions will have to build from source.

To install all released Indigo packages, run the following on the
command line: ```
sudo apt-get install ros-$ROS_DISTRO-denso-robot-ros
```

## Tutorials

See the [Tutorials](denso_robot_ros/Tutorials) page for an overview of
the available tutorials.

## Report a Bug

\<\<GitHubIssues(DENSORobot/denso_robot_ros)\>\>
