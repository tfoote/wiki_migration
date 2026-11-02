## The Mia Hand

![height="740px"](doc/miahand1.png)

**Mia** is a robotic anthropomorphic end-effector, suitable in: flexible
manufacturing plants, social and/or humanoid collaborative robots,
bio-automation, ergonomics, prosthetics, human-machine interface
research, and wherever a gripper with hand-like features may become
handy. The three embedded motors allow to interact with the environment
and to grasp objects and tools using power, precision and lateral
grasps. Embedded force sensors allow to regulate the grasping force.
Embedded functions and a simple control interface based on RS-232 makes
integration seamless, saving you money and time. Being extremely
lightweight (500 g) but still powerful (up to 70 N grip force), Mia
offers the good balance between flexibility and performance. Designed
and engineered by Prensilia, Mia is made in Italy, and it has been
awarded with the
[Red Dot Design Award 2019](https://www.red-dot.org/project/mia-39819),
and obtained the honorable mention in
[The Plan Award 2019](https://www.theplan.it/award). For additional info
see [ Mia home page](https://www.prensilia.com/portfolio/mia/).

### Video

[Youtube](https://www.youtube.com/watch?v=hseGvpIE_uc&rel=0)
[Youtube](https://www.youtube.com/watch?v=YpLcr7J7g4E&rel=0)

## Repository

The **mia_hand_ros_pkgs**
[repository](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/)
contains packages for controlling the robotic hand in real and in Gazebo
simulated environment. This metapackage provides also URDF models of the
hand and launch files.

### Packages Overview

Our code is split into different packages:

- [mia_hand_msgs\|target="_blank"](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_msgs/):
  This package contains custom messages/services/actions for the Mia
  hand.
- [mia_hand_description\|target="_blank"](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_description/):
  This package provides the URDF models of the Mia hand. For further
  details please see the
  [README.md](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_description/README.md)
  file and the doxygen documentation
  ([doc ](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_description/doc/)
  ) stored in the package.
- [mia_hand_driver\|target="_blank"](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_driver/):
  This package contains the cpp driver library to communicate and
  control the real Mia hand. For further details please see the
  [README.md](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_driver/README.md)
  file and the doxygen documentation
  ([doc](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_driver/doc/)
  ) stored in the package.
- [mia_hand_ros_control\|target="_blank"](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_ros_control/):
  This package contains the hardware interface class that allows ROS
  controllers to send command to and receive joint states data from the
  Mia hand. This package contains also a list of pre-set ROS controllers
  that can be used to control the Mia hand in position or velocity. For
  further details please see the
  [README.md](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_ros_control/README.md)
  file and the doxygen documentation
  ([doc](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_ros_control/doc/)
  ) stored in the package.
- [mia_hand_gazebo\|target="_blank"](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_gazebo/):
  This package contains the hardware Sim interface class that allows to
  use the Mia hand within a Gazebo simulated environment. This package
  contains also a list of pre-set ROS controllers that can be used to
  control the simulated Mia hand in position or velocity. For further
  details please see the
  [README.md](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_gazebo/README.md)
  file and the doxygen documentation
  ([doc](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_gazebo/doc/)
  ) stored in the package.
- [mia_hand_moveit_config\|target="_blank"](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_moveit_config/):
  This package contains all the configuration files needed to make Mia
  hand work with MoveIt. However, if needed custom configuration files
  can be generated following the
  [MoveIt Setup Assistant tutorial](http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/setup_assistant/setup_assistant_tutorial.html).
- [mia_hand_bringup\|target="_blank"](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_bringup/):
  This package contains all the launch files to start the nodes of the
  Mia hand. For further details please see the
  [README.md](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/mia_hand_bringup/README.md)
  file stored in the package.

### Report a Bug

To report bug or issues please use
[ bitbucket repo](https://bitbucket.org/prensilia-ros/mia_hand_ros_pkgs/src/master/).

### Acknowledgments

The development of the **mia_hand_ros_pkgs repository** was supported by
by the European Commission under the Horizon 2020 framework program for
Research and Innovation within
[ the APRIL project](http://aprilproject.eu/) (multipurpose robotics for
mAniPulation of defoRmable materIaLs in manufacturing processes, number:
870142).

![width="300px"](doc/APRIL.png)
