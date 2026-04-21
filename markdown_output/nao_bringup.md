# Overview

nao_bringup contains launch and configuration files as a single-entry
point for nao. The launch files are starting all basic actuators and
sensor publishers in their robot specific configurations

# Dependencies

Before starting, please make sure you meet all the required dependencies
especially the packages [naoqi_driver](naoqi_driver),
[naoqi_bridge](naoqi_bridge) and [nao_description](nao_description). You
can either install the official releases via your package manager or
directly clone the necessary ros packages from github.

# Usage

To start the robot bringup, simply run: 

```
$ roslaunch nao_bringup nao_full.launch nao_ip:=<robot_ip> roscore_ip:=<roscore_ip>
```



The first parameter gives the IP of your robot. The second paramter, the
roscore IP, is the IP of the computer where the roscore is running. This
is necessary since there is no roscore running on the robot. So we have
to tell the robot where to find its roscore. The third parameter
network_interface specifies the network interface the bridge is
connected. By default, this is set to eth0. Changing this becomes
important to establish a correct network connection between robot and
computer, when you are connected via a different network device, such as
wlan0 or vpn0 etc. In case you are not certain which device to use,
verify with ifconfig and verify which network device has the correct IP.

This will start the robot's default configuration with the following
publisher:

-   joint_states
-   tf
-   top camera
-   bottom camera
-   left sonar
-   right sonar
-   microphone

Alternatively you can make use of the python SDK, which has to be
installed and correctly setup in your PYTHONPATH environment variable.
For more information on that, please refer to [nao](nao).


```
$ roslaunch nao_bringup nao_full_py.launch nao_ip:=<robot_ip> roscore_ip:=<roscore_ip>
```



Once this is successfully launched, you can simply open RVIZ. The
bringup package provides already a rviz-config file. Simply open this
configuration and you will see the robot model, tf, and the top camera.
