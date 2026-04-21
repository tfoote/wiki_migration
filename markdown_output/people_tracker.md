[cyphy_people_mapping](cyphy_people_mapping):[people_tracker](people_tracker)/[trajectory_clustering](trajectory_clustering)/[map_creation](map_creation)

## Getting started

In order to use the people tracker you must have installed a version of
OpenNI/Nite that supports the load/save user calibration facility.
Follow the instructions on [cyphy_people_mapping](cyphy_people_mapping)
to install the latest version of OpenNI for your distro.

## Video

[Youtube](https://www.youtube.com/watch?v=t_EZsFHOmsA)

## Compiling People Tracker

You'll need to point the compiler at the location of OPEN_NI_UNSTABLE
and OPEN_NITE_UNSTABLE on your system. Change the corresponding lines in
the CMakeLists.txt file. eg



```
set(OPEN_NI_UNSTABLE "/home/your_name/kinect/openni/" CACHE STRING "Location of Unstable OpenNI")
set(OPEN_NITE_UNSTABLE "/home/your_name/kinect/nite/" CACHE STRING "Location of Unstable NITE")
```



## Running the node



```
rosrun people_tracker tracker
```



Stand about 1-2 metres in front of the kinect so that it can see your
whole body. There is no need to pose, the default calibration file is
for a person 5'10" in height so as long as you are roughly this size
you will be detected.

### Node Description

#### Subscribed Topics

None. This node wraps the OpenNI skeleton tracker so communicates
directly to the kinect.



```clearsilver
pub {
  0.name = robotsound
  0.type = sound_play/SoundRequest
  0.desc = Audio feedback when the robot tracks/loses users
}

pub {
  1.name = cmd_vel
  1.type = geometry_msgs/Twist
  1.desc = Velocity commands to get the robot to follow currently tracked user
}

pub {
  2.name = person_track
  2.type = geometry_msgs/PointStamped
  2.desc = xyz offset of the tracked person's torso from the base_link
}
```


