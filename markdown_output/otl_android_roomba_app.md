## Overview

This is App Chooser version of [otl_android_roomba](otl_android_roomba).
You may be able to use this app with your turtlebot.

[Youtube](https://www.youtube.com/watch?v=lWmGXgDEOPQ)

You can use this with [otl_roomba](otl_roomba) package.

## How to use on Turtlebot

cd to your working ROS directory. 

```
svn checkout https://otl-ros-pkg.googlecode.com/svn/trunk/otl_android
```

 Add below
into your mock_apps/turtlebot_apps.installed file.


```
- display: Tilt Teleop
   app: otl_android_roomba_app/roomba
```



Access to your robot by App Chooser of your Android device, and select
'Tilt Teleop'. Enjoy!

## Node Info



```clearsilver
name = Tilt Teleop (Android App)
desc = Publishes cmd_vel by tilting the device.
pub {
0.name = /cmd_vel
0.type = geometry_msgs/Twist
0.desc = Velocity of robot (roomba).  you can remap this by editting roomba.app file.
1.name = /roomba/clean
1.type = std_msgs/Bool
1.desc = start cleaning or stop.
2.name = /roomba/dock
2.type = std_msgs/Bool
2.desc = start docking to charge station of roomba
}
```



## .app file

You can adjust velocity by editting
otl_android_roomba_app/app/roomba.app file. Default setting is


```
app:
      base_control_topic: /cmd_vel
      linear_rate: 0.08
      angular_rate: 0.2
```

 linear_rate means velocity of linear.x,
angular_rate is for angular.z.
