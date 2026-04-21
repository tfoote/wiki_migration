# Startup launch files for SoftBank's pepper robot.

## Prerequirements

Install packages ```
sudo apt-get install ros-indigo-pepper-robot ros-indigo-pepper-meshes
```

## Bring up Pepper

You can start Pepper either with a [C++](naoqi_driver) or
[Python](naoqi_driver_py) version. The pepper_bringup package thus
contains two launch files.

For starting the C++ version: ```
roslaunch pepper_bringup pepper_full.launch nao_ip:=<robot_ip> roscore_ip:=<roscore_ip> [network_interface:=<eth0|wlan0|vpn0>]
```

Similar, the Python version: ```
roslaunch pepper_bringup pepper_full_py.launch nao_ip:=<robot_ip> roscore_ip:=<roscore_ip>
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

## Visualize your robot

When you have launched your robot correctly, you see a similar picture
in RVIZ:

![Pepper with rviz\|width=750](http://1.bp.blogspot.com/-v-UpYPMWd3M/VMj9lj3oTrI/AAAAAAAAWL8/Tkk_kK5CWa8/s1600/pepper_rviz.png)

## Tutorial

-   [OTL's blog post (Japanese)](http://ros-robot.blogspot.jp/2015/01/pepper-is-here.html)
    for the detail.
