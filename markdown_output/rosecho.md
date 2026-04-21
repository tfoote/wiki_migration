## Introduction

Tianbot Rosecho (Tianecho)，a Chinese speech recognition sensor for
robots to hear the world.ROSECHO is based on iFlyTek IFLYOS system, the
AIUI development kit.
'''[Rosecho github repo](https://github.com/tianbot/rosecho)
**[中文语音交互模块使用手册](http://doc.tianbot.com/rosecho/) **

## Installation

You can skip these steps if you purchase ROSECHO with a ROS2GO system

### Install from debian package

To be released

### Install from source

Steps to install to catkin_ws. Tested for ROS kinetic and melodic.
```
cd ~/catkin_ws/src/
git clone https://github.com/tianbot/rosecho.git
cd ~/catkin_ws && catkin_make
```

### Usage Instructions

Make sure the power supply and usb connection are correct.

Start ROSECHO node Launch the ROSECHO. ```
roslaunch rosecho rosecho.launch
```

The default serial port is /dev/ttyUSB0, if serial open failed, pls
check the port used by ROSECHO If it is /dev/ttyUSB1, you can change the
launch file or launch use the command as follows
```
roslaunch rosecho rosecho.launch serial_port:=/dev/ttyUSB1
```

To enable wifi config, call the wifi_cfg service.
```
rosservice call /rosecho/wifi_cfg "ssid: 'tianbot' password: 'www.tianbot.com'"
``` You can use Tab to auto-complete the command
and then fill in the ssid and password.

check the automated sound recognition result ```
rosrun rosecho asr_echo.py
```

check the answer ```
rosrun rosecho answer_echo.py
```

send tts to rosecho/tts/goal ```
rostopic pub /rosecho/tts/goal rosecho/ttsActionGoal "header:
  seq: 0
  stamp:
    secs: 0
    nsecs: 0
  frame_id: ''
goal_id:
  stamp:
    secs: 0
    nsecs: 0
  id: ''
goal:
  text: '你好机器人'"
```

You can use Tab to auto-complete the command and then fill in the goal:
text: '你好机器人'

## Simple Demo

Voice command test in turtlebot stage ```
roslaunch rosecho rosecho.launch
roslaunch turtlebot_stage turtlebot_in_stage.launch
rosrun rosecho demo.py
```

## Nodes

```clearsilver
  name=rosecho
  desc=rosecho is the main function.
pub {
  0.name= /rosecho/answer
  0.type = std_msgs/String
  0.desc = The answer returned by iflyos.
  1.name = /rosecho/asr
  1.type = std_msgs/String
  1.desc = Speech recognized result.
  2.name = /rosecho/wakeup_pos
  2.type = std_msgs/Int16
  2.desc = Position of the speaker when wakeup.
  3.name= /rosecho/tts/feedback
  3.type = rosecho/ttsActionFeedback
  3.desc = Currently no output.
  4.name= /rosecho/tts/result 
  4.type = rosecho/ttsActionResult
  4.desc = Return success when finish TTS.
  5.name= /rosecho/tts/status 
  5.type = actionlib_msgs/GoalStatus
  5.desc = The ROSECHO tts status.
}

sub {
  0.name = /rosecho/tts/goal  
  0.type = rosecho/ttsActinoGoal
  0.desc = The ROSECHO tts status.
  1.name= /rosecho/tts/cancel   
  1.type = actionlib_msgs/GoalID
  1.desc = Cancel goal, interupt the current TTS action.
}

srv{
  0.name = /rosecho/disable  
  0.type = std_srvs/Empty
  0.desc = Disable the service.
  1.name = /rosecho/enable  
  1.type = std_srvs/Empty
  1.desc = Enable the service.
  2.name = /rosecho/sleep  
  2.type = std_srvs/Empty
  2.desc = Enter sleep mode if awaken.
  3.name = /rosecho/wakeup
  3.type = std_srvs/Empty
  3.desc = Manually wakeup.
  4.name = /rosecho/wifi_cfg
  4.type = rosecho/WifiCfg
  4.desc = Setup WIFI connection.
}
```

## License

The package is under BSD 3-Clause License
