## About

The \`python_ethernet_rmp\` package contains the drivers for interfacing
to a Segway RMP via an Ethernet connection.

## Installation

To install the \`python_ethernet_rmp\` package, you can choose to either
install from source, or from the Ubuntu package:

### Source

To install from source, execute the following: ```shell
cd /path/to/your/catkin/workspace/src
git clone https://github.com/WPI-RAIL/python_ethernet_rmp.git
cd /path/to/your/catkin/workspace
catkin_make 
catkin_make install
```

### Ubuntu Package

To install the Ubuntu package, execute the following:
```
sudo apt-get install ros-indigo-python-ethernet-rmp
```

## system_defines.py

This file located in the package contains all of the system defines for
the RMP. This can gives max and min values for all of the parameters as
well as some system configuration option. Some of these defines are also
listed in the \'segway_msgs/RMPCommand\' message type used to set
parameters or sent commands to the RMP.

## Support

Please send bug reports to the
[GitHub Issue Tracker](https://github.com/WPI-RAIL/rovio/issues). Feel
free to contact me at any point with questions and comments.

-   [Russell Toris](Russell Toris)
-   <rctoris@wpi.edu>
-   [Academic Website](http://users.wpi.edu/~rctoris/)
