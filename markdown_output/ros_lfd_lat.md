# Package Description

This project provides a ROS stack for teaching a robot through averaging
trajectories. This project is based on the bachelor-thesis of Heiko
Posenauer and his program Leatra.

Maintainer: Benjamin Reiner reinerbe@hs-weingarten.de University of
Applied Sciences
Ravensburg-Weingarten[Institute for Artificial Intelligence](http://iki.hs-weingarten.de/)

# Installation

Repository: <https://bitbucket.org/BennyRe/ros-lfd-lat/overview>

This package requires ROS Fuerte. Other ROS distributions are not
tested. Eigen should be installed properly (located in
/usr/local/include). First install the Katana Stack and all its required
dependencies. Install Orocos KDL with sudo apt-get install
ros-fuerte-orocos-kinematics-dynamics (some more dependencies could
occur) Now check out this repository and rosmake the ros_lfd_lat
package. If he can't find any packages while making, please install
them. rosmake the fake_or package, if you need it.

If you want to use the Katana 300 copy the katana package from this
repository into your katana_driver directory and overwrite the original
one. Then rosmake it.

# Running

If you have the Katana connencted over a RS-232-to-USB adapter, then you
migth want to run sudo setRightsTty.sh to create a symlink from ttyUSB0
to ttyS0. Start the Katana with roslaunch katana katana.launch rosrun
fake or fake or server.py To learn a task: rosrun ros lfd lat lat
learner To reproduce a task: rosrun ros lfd lat lat reproducer
\[trajectory name\] The trajectroy name is optional. If you don't define
one the programm asks you about one. Both programs will ask you to do
something if they want you to do something.
