## Overview

This package contains the code for controlling the rb1_base with a
joystick. The package has the following folders:

\- \'\'\'config:\'\'\' In this folder you will find the different config
files available for the different possible joysticks

\- \'\'\'launch:\'\'\' In this folder you will find the launch file to
execute the node

\- \'\'\'src:\'\'\' In this folder you will find the source code

## Usage

In order to launch the [joy](joy) node along with the personalized
rb1_base joystick: ```
roslaunch rb1_base_pad rb1_base_pad.launch pad_model:=ps4
```

This command will launch the mentioned joy node, in order to have a ROS
driver for joysticks, it will publish msgs of type sensor_msgs/Joy.
Besides, it will launch the rb1_base_pad for the joystick specified in
the argument.
