# Startup launch files for Romeo robot.

# Overview

romeo_bringup contains launch and configuration files required to bring
ROS interfaces for Romeo up into a running state. The launch files are
used to start all basic actuators and sensor publishers in their robot
specific configurations.

## Prerequirements

Install packages 

```
sudo apt-get install ros-indigo-romeo-robot ros-indigo-naoqi-driver
```



## Bring up Romeo

You can start Romeo either with a [C++](naoqi_driver) or
[Python](naoqi_driver_py) version. Thus, the romeo_bringup package
contains two launch files.

For starting the C++ version: 

```
roslaunch romeo_bringup romeo_full.launch nao_ip:=<robot_ip> roscore_ip:=<roscore_ip> [network_interface:=<eth0|wlan0|vpn0>]
```



Similar, the Python version: 

```
roslaunch romeo_bringup romeo_full_py.launch nao_ip:=<robot_ip> roscore_ip:=<roscore_ip>
```



As shown above, the launch files contain 3 parameters

1\. nao_ip : This is necessary for telling which robot to connect to. 2.
roscore_ip : Since there is no roscore running on the robot, we have to
tell it the IP of the roscore to use. 3. network_interface : By default,
we assume that your computer is connected via eth0. When you are
connected via WLAN or VPN, name the correct network interface here
(eth1, wlan0, vpn0 etc). ```This is only available in the C++
version```

See the [naoqi_driver](naoqi_driver) and
[naoqi_driver_py](naoqi_driver_py) for further details.
