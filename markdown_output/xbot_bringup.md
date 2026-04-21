## 简介

xbot_bringup功能包提供启动xbot机器人所有功能的launch文件脚本。

## Launch 文件

### xbot.launch

xbot.launch文件可以将Xbot单独运行起来，所驱动起来的传感器包括机器人电机控制器、电机码盘、超声波传感器、红外传感器、电压电流检测器等。


```
roslaunch xbot_bringup xbot.launch
```



### rplidar.launch

rplidar.launch文件可以单独启动激光雷达传感器的驱动。


```
roslaunch xbot_bringup rplidar.launch
```



### realsense.launch

驱动 Intel Realsence 深度摄像头。 

```
roslaunch xbot_bringup realsense.launch
```



### xbot-u.launch

xbot-u.launch文件包含了上述三个文件，并同时启动了人脸识别、语音交互等功能。


```
roslaunch xbot_bringup xbot-u.launch
```


