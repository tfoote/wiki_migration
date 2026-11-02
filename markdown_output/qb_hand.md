

## Tutorials

- [ROS Packages Installation](#ros-packages-installation):
  Install the last qb SoftHand Research and qb SoftHand2 Research
  related ROS packages

## ROS Packages Installation

```
{#!wiki version kinetic_and_newer

== Requirements ==
If you have never set it up, you probably need to add your linux user to the `dialout` group to grant right access to the serial port resources. To do so, just open a terminal and execute the following command:
{{{
sudo gpasswd -a <user_name> dialout
```

 where you need to replace the `<user_name>`
with your current linux username.

*Note: Don't forget to logout or reboot.*

### Ubuntu Packages

If you prefer to leave your catkin workspace as it is, you can simply
install all the ROS packages from the Ubuntu official repositories:



```
sudo apt update
sudo apt install ros-$ROS_DISTRO-qb-hand
```



### Sources



```wiki
Since you are interested in the ROS interfaces for our devices, it is assumed that you are familiar at least with the very basics of the ROS environment. If not, it might be useful to spend some of your time with [[ROS/Tutorials|ROS]] and [[catkin/Tutorials|catkin]] tutorials. After that, don't forget to come back here and start having fun with our Nodes.
```



Install the packages for a ROS user is straightforward. Nonetheless the
following are the detailed steps which should be easy to understand even
for ROS beginners:

1\. Clone both the `qb_device` and `qb_hand` packages to your Catkin
Workspace, e.g. `/catkin_ws`: 

```
cd `~/catkin_ws/src`
git clone --recurse-submodules --branch production-$ROS_DISTRO https://bitbucket.org/qbrobotics/qbdevice-ros.git
git clone --branch production-$ROS_DISTRO https://bitbucket.org/qbrobotics/qbhand-ros.git
```



1\. Compile the packages using `catkin`: 

```
cd `~/catkin_ws`
catkin_make
```


**Note:** depending on your ROS installation, you may need some extra
packages to properly compile the code. Please, be sure that you have
already installed at least `ros-\$ROS_DISTRO-ros-controllers`,
`ros-\$ROS_DISTRO-transmission-interface`,
`ros-\$ROS_DISTRO-joint-limits-interface`,
`ros-\$ROS_DISTRO-combined-robot-hw`, and their dependencies (*e.g.
use `sudo apt install <ros-pkg>`*).

1\. If you were not familiar with ROS you should be happy now:
everything is done! Nonetheless, if you encounter some troubles during
the compilation, feel free to ask for support on
[our Bitbucket](https://bitbucket.org/account/user/qbrobotics/projects/ROS).

### Device Setup

Connect a *[qb SoftHand Research ](Robots/qbhand)* or a
*[qb SoftHand2 Research](Robots/qbhand)* to your system is basically a
matter of plugging in a USB cable. Nonetheless, **read carefully** the
product manual to understand all the requirements and advices about
either single-device or chained configurations.

}}}}
