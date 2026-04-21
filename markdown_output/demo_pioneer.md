# Introduction

This package contains a set of nodes that can be used to run visual
servoing demonstrations on a real Pioneer P-3DX mobile robot equipped
with a camera. These nodes illustrate the usage of
[vision_visp](vision_visp) stack; especially
[visp_auto_tracker](visp_auto_tracker) for the tracking of the target,
and [visp](visp) usage in order to implement a position based visual
servoing.

Two demonstrations are provided:

-   The camera is rigidly fixed in front of the Pioneer
-   The camera is mounted on a PT-head fixed in front of the Pioneer

[Youtube](https://www.youtube.com/watch?v=n3UmgCXw5lY)

If you don't have a real Pioneer under the hand, it is also possible to
use this stack on a simulated Pioneer robot. To this end you may use the
[vrep_ros_plugin](vrep_ros_plugin) stack and follow the
[tutorial](http://wiki.ros.org/vrep_ros_bridge/Tutorials/Pioneer%203D-X%20controlling%20its%20pose%20via%20a%20visual%20servoing%20law).

# Requested material

This package was used with the following materials:

-   [Pioneer P3-DX](http://www.mobilerobots.com/ResearchRobots/PioneerP3DX.aspx)
    mobile robot
-   [Logitec wireless F710 gamepad](http://gaming.logitech.com/en-us/product/f710-wireless-gamepad)
    to tele operate the robot
-   A firewire camera. We use an
    [Allied Pike F-032C](http://www.alliedvisiontec.com/us/products/cameras/firewire/pike.html)
    with a 4.2mm lens, but any other camera can be used.

Optional material:

-   A [Biclops PT](http://traclabs.com/products/biclops-pt/) head.

# Installation

## Install ROS and create a catkin workspace



```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
cd ~/catkin_ws
catkin_make
```



## Bring the source



```
cd ~/catkin_ws/src
```



Get [rosaria](rosaria) stack that allows to control a real Pioneer robot


```
git clone https://github.com/amor-ros-pkg/rosaria.git (master branch)
```



Get [demo_pioneer](demo_pioneer) stack that does the visual servoing


```
git clone https://github.com/lagadic/demo_pioneer.git (master branch)
```



## Install dependencies



```
source ~/catkin_ws/devel/setup.bash
rosdep update
rosdep install rosaria
rosdep install demo_pioneer
```



## Build the source



```
cd ~/catkin_ws
catkin_make -DCMAKE_BUILD_TYPE=Release --pkg rosaria
catkin_make -DCMAKE_BUILD_TYPE=Release --pkg demo_pioneer
```



# Usage

## Test first pioneer tele operation from gamepad

Check if you have the read/write rights in /dev/ttyUSB0. If not



```
sudo chmod a+rw /dev/ttyUSB0
```

 or even better edit
'/etc/udev/rules.d/51-local.rules' and add the following line:



```
KERNEL=="ttyUSB*", MODE="0666"
```



First check if the Pioneer can be tele operated



```
source ~/catkin_ws/devel/setup.bash
roslaunch demo_pioneer pioneer-teleop.launch
```



On the gamepad, select the XInput interface mode. This can be done by
sliding the a switch on the side of the gamepad to the position marked
"X".

Once done, push "left or right button trigger" to wake the gamepad
driver and then use the "right mini stick" to move the robot.

## Start the visual servoing demo on the Pioneer

Then start the demo with a real Pioneer robot using:



```
source ~/catkin_ws/devel/setup.bash
roslaunch demo_pioneer demo-visual-servo-pioneer.launch
```



This will open a windows name "visp_auto_tracker debug display" that
shows the images provided by the camera. Present the target available
[here](https://github.com/downloads/lagadic/visp_auto_tracker/template-qr-code.pdf)
in front of the camera. It should be detected automatically. Once
detected, on the gamepad push "left or right button trigger" to apply
the visual servo command to the robot. As long as one of these two
buttons are pressed, the command applied to the robot is the one that
comes from the visual servoing node. If you release the button, the
robot stops moving. You can then move it with the "right mini stick".

# Known issues

## Missing pattern.wrl file

With some old releases of visp_auto_tracker installed with rosdep you
may encounter the following issue:



```
cd ~/catkin_ws/src
```

0

The fix consists in copying visp_auto_tracker/models folder in the
folder where visp_auto_tracker node was installed by using:


```
cd ~/catkin_ws/src
```

1
