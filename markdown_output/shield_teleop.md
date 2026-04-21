**Maintainer:** Mirza A. Shah\
**Author:** Mirza A. Shah\
**URL:** <https://github.com/mirzashah/shield_teleop>\
**License:** BSD\

## Overview

**shield_teleop** is an application for the nVidia SHIELD handheld
gaming console. As the SHIELD is a 100% pure Android device,
shield_teleop is an Android app. When the app starts running, it will
begin publish [sensor_msgs/Joy](sensor_msgs/Joy) that mimic the messages
produced by [ps3_teleop](ps3_teleop) on Ubuntu. The app all displays a
video stream using [image_transport](image_transport)'s compressed
image messages.

## ROS API



```clearsilver
name = shield_teleop
desc = ROS interface for shield_teleop
sub {
  0.name = /usb_cam/image_raw/compressed
  0.type = sensor_msgs/CompressedImage
  0.desc = Any valid image_transport video stream which will be displayed in the main view
}
pub {
  0.name = /joy
  0.type = sensor_msgs/Joy
  0.desc = Continuously publishes joystick messages representing SHIELD joystick state. Mimics PS3 controller.
}
```



## Building

shield_teleop utilizes [rosjava](rosjava) and the complimentary
[android_core](android_core) packages in its implementation and requires
them as a build dependency.

### Command Line



```
source ~/rosjava/devel/setup.bash
 mkdir -p ~/shield_teleop_ws/src
 cd ~/shield_teleop_ws/src
 catkin_create_android_repo
 git clone https://github.com/mirzashah/shield_teleop
 cd ~/shield_teleop
 catkin_make
```



### Android Studio

1\. Open Android Studio 1. Import project 1. Select
/shield_teleop_ws/src 1. Select "shield_teleop" in dropdown menu 1.
Hit "Play" button, this will build and attempt to upload to either
device or emulator

## Running

1\. On your device select "ROS SHIELD Teleop" from applications. 1. On
startup, you'll be prompted for a ROS master, choose the one that's
running on the robot. 1. You should be now publishing to topic /joy. 1.
Run either pr2_joystick_teleop or turtlebot_joystick.
