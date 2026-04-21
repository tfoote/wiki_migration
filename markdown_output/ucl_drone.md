## Overview

This package contains the implementation corresponding to the following
master theses:

-   Towards 3D Visual SLAM for an Autonomous Quadcopter Running on ROS.
    (A. Leclère, A. Jacques)
-   Suivi d'une cible mobile par des drones autonomes. (J. Gérardy, F.
    Schiltz)

Abstract 1 --- In a context where multi-copters gain in attractiveness
each day to solve novel challenges or replace older technologies, the
need for autonomous behaviour is being pointed out as a key feature for
unlocking lots of applications. This master thesis is conducted at UCL
for trying to understand the current challenges to unlock multi-copter
autonomy. We point out that the lack of robustness of all current
state-of-the-art implementations which are based only upon on-board
sensors, leads, as a common flaw, to a lack of accuracy of the pose
estimation. Indeed, for GPS-denied environments such as indoors, there
exist poor absolute references to build an accurate and robust belief of
the position and orientation of the drone. Unfortunately, indoor
situations need precisely the best pose estimation since they are
confined places not allowing too large errors while executing movement.
We propose an implementation of the direct keyframe-based visual SLAM
approach based on features detected in the images of the video-stream of
an embedded camera. We show that the results obtained on a real low cost
quadcopter, the AR.Drone 2.0, improve substantially the pose estimation,
notably by canceling the drift on sensor readings. However, this
technique presents strong limitations when confronted to untextured
environments, due to the lack of reference keypoints detected in the
images. To palliate this, we explore the state of the literature to
propose some promising advances to replace or enhance this approach,
such as replacing conventional cameras by RGB-D (Red Green Blue - Depth)
cameras or DVS (Dynamic Vision Sensors), or replacing computationally
costly software parts by a hardware implementation, or better fusing the
available sensors informations.

This is a video of an AR.Drone 2.0 executing a demonstration, using this
package:

[Youtube](https://www.youtube.com/watch?v=eWDQgP83RXs&feature=share)

Abstract 2 --- In this thesis, we describe a system that enables a
low-cost quadcopter coupled with a ground-based laptop and a router
navigate autonomously in previously unknown and GPS- denied
environments. The first drone searches for a moving target in a 3 by 3
meters room. when it finds it, it starts following it. When its battery
level becomes critical, it calls an other drone to replace him and it
goes back to its starting position.

This is a video of two AR.Drone 2.0 executing the mission, using this
package:

[Youtube](https://www.youtube.com/watch?v=IaHg9J8_VjA&feature=share)

## Quickstart

### Installation

It is advised to use "indigo" version of ROS.

1\. Install the
[ardrone_autonomy](http://github.com/AutonomyLab/ardrone_autonomy#installation)
package. To do this, follow intructions at
<http://ardrone-autonomy.readthedocs.io/en/latest/installation.html>

OpenCV 2.4.x and PCL (Point Cloud Library) are also needed. To install
them, follow the procedures on their respective official websites.

### Install ucl_drone package:



```
# cd into ros root dir
roscd

# clone repository
git clone git:https://github.com/Felicien93/ucl_drone.git

# compile in the root of ucl_drone package
catkin_make
```



## Set up the router

As several drones communicate during this mission, it is mandatory to
use a router and make the drones act as clients instead of hosts. The
model we used was the "TPlink « TL-WR841N »" but any model should do.

The first step is to collect the MAC addresses of the drone you will
use.



```
#Connect your computer to the drone's network

#Use telnet to access the drone network informations
telnet 192.168.1.1

#Display relevant informations
ifconfig ath0

#Note the drone's MAC address. You will need it later. It is written in the "HWaddr" field. MAC address example: 90:03:B7:2A:DF:11

#Set up your network card
sudo ifconfig eth0 192.168.1.253

#Type the IP address of your router in your internet navigator
192.168.1.254

#Connect on the page using the password and ID of the router

#Go in Network>Interfaces>Edit>LAN and define 192.168.1.254 in the ipv4address field.

#Go in Network>wifi and click add. Use the controller with "BGN" in his description.

#In "general setup" configure the essid fiel on "drone" and hide essid.

#Go back in Network>wifi and click "enable" next to the "drone" network

#Click on "edit". Go in Mac filter, chose "allow listed only" and add the MAC addresses of the drones you connected.

#In your files (not in navigator) go in src>ucl_drone>drone_preparation>Appareillage and add one file per drone. The file name should be the drone's network name (example: ardrone2_00217) and it should contain the IP address you want it to have (example: 192.168.1.5)
```



## Run



```
# Connect to the drones. Go in src>ucl_drone>drone_preparation>Appareillage
bash autoconfarparrot

# run the program
roslaunch ucl_drone two_simples_new.launch
```


