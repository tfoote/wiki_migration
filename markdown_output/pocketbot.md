## App Summary

PocketBot for Ros is an Android application and ROS node. It provides
both controls for a ROS enabled robot and social interactions. In
addition the app uses WebRTC for telepresence.

<http://pocketbot.io>

[Youtube](https://www.youtube.com/watch?v=IwLGbz-uRno)

## Installation

-   From the
    [Play Store\|target=\"\_blank\"](http://play.google.com/store/apps/details?id=com.tesseractmobile.pocketbot)

This app has been tested with ROS indigo, kinetic and lunar. On Ubuntu
14.04, 16.04, 17.04 and HypriotOS on the Rapberry Pi 3.

## ROS API

```clearsilver
name = pocketbot_ABCD
desc = The node name is randomly generated so that multiple PocketBots may connect at the same time.
pub{
  0.name = pocketbot/emotion
  0.type = std_msgs/String
  0.desc = Emotional state of the robot. (JOY, ACCEPTED, AWARE, ANGER, SADNESS, REJECTED, SURPRISED, FEAR)

  1.name = pocketbot/speech
  1.type = std_msgs/String
  1.desc = When the PocketBot app recognizes speech it is output on this topic as a String the app normally send this to the AI service

  2.name = pocketbot/ai_speech_out
  2.type = std_msgs/String
  2.desc = AI services response, the app will normally speak this text when in face mode

  3.name = pocketbot/imu
  3.type = sensor_msgs/Imu
  3.desc = The current orientation of the Android device

  4.name = pocketbot/face
  4.type = geometry_msgs/Twist
  4.desc = Position of foremost recognized face

  5.name = pocketbot/cmd_vel
  5.type = geometry_msgs/Twist
  5.desc = Output from onscreen joysticks in PocketBot app's control screen. Right joystick outputs linear x and angular z. Left joystick outputs angular y and angular x.

  6.name = pocketbot/fix
  6.type = sensor_msgs/NavSatFix
  6.desc = Current position of robot in latitude and longitude as measured by Android device, position_covariance[0] is the accuracy in meters

  7.name = pocketbot/waypoint
  7.type = sensor_msgs/NavSatFix
  7.desc = Updated when a new way point is added using PocketBot's navigation interface

  8.name = pocketbot/heading
  8.type = std_msgs/Float32
  8.desc = Heading in degrees 0-360 of direction device is facing (front camera)
}
```
