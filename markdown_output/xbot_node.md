## 简介

xbot_node功能包为[xbot_driver](xbot_driver)提供ROS API。

## ROS API



```clearsilver
name = XbotNodelet
 sub{
    0.name = /commands/motor_disable
    0.type = std_msgs/Bool
    0.desc = 是/否禁用机器人电机控制，默认为false。当消息为true时,机器人将无法进行移动控制（处于“急停”状态）。
    1.name = /commands/velocity
    1.type = geometry_msgs/TwistConstPtr
    1.desc = TODO；
    2.name = /commands/yaw_platform
    2.type = std_msgs/Int8
    2.desc = 机器人云台水平运动控制，msg为偏航角角度信息，单位为度。
    3.name = /commands/pitch_platform
    3.type = std_msgs/Int8
    3.desc = 机器人云台俯仰运动控制，msg为俯仰角角度信息，单位为度，范围为-60°～+30°。
    4.name = /commands/sound_enable
    4.type = std_msgs/Bool
    4.desc = 是/否启用声音设备，默认为true。
    5.name = /commands/led
    5.type = std_msgs/Int8
    5.desc = TODO
    6.name = /commands/lift
    6.type = std_msgs/Int8
    6.desc = TODO
    7.name = /commands/reset_odometry
    7.type = std_msgs/EmptyConstPtr
    7.desc = 重置里程计信息，且机器人的位置和速度清零。
 }
 pub {
   0.name = /joint_states
   0.type = sensor_msgs/JointState
   0.desc = 从此话题可以获取xbot机器人轮子关节的位置和速度信息。 
   1.name = /sensors/core
   1.type = xbot_msgs/CoreSensor
   1.desc = TODO
   2.name = /sensors/extra
   2.type = xbot_msgs/ExtraSensor
   2.desc = TODO
   3.name = /sensors/yaw_platform_degree
   3.type = std_msgs/Int8
   3.desc = 水平云台当前的偏转角度信息，单位度。
   4.name = /sensors/pitch_platform_degree
   4.type = std_msgs/Int8
   4.desc = 竖直云台当前的俯仰角度信息，单位度。
   5.name = /sensors/motor_disabled
   5.type = std_msgs/Bool
   5.desc = 从此话题获取机器人的电机禁用信息。
   6.name = /sensors/sound_enabled
   6.type = std_msgs/Bool
   6.desc = 从此话题获取机器人的声音设备启用信息。
   7.name = /sensors/battery
   7.type = xbot_msgs/Battery
   7.desc = 从此话题获取机器人的电量信息。
   8.name = /sensors/echo
   8.type = xbot_msgs/Echo
   8.desc = 从此话题获取超声传感器信息。
   9.name = /sensors/infrared
   9.type = xbot_msgs/InfraRed
   9.desc = 从此话题获取红外传感器信息。
   10.name = /sensors/imu_data
   10.type = sensor_msgs/Imu
   10.desc = 从此话题获取IMU传感器信息。
   11.name = /sensors/raw_imu_data
   11.type = xbot_msgs/RawImu
   11.desc = 从此话题获取IMU传感器信息。
   12.name = /xbot/state
   12.type = xbot_msgs/XbotState
   12.desc = TODO


   
 }
 srv {
    0.name = /commands/velocity
    0.type = geometry_msgs/TwistConstPtr
    0.desc = Call this service to play the audio file of the specified path or convert text to voice playback.
    1.name = /xbot/chat
    1.type = xbot_talker/chat
    1.desc = Call this service to start voice conversation with the robot.
  }
param {
  0.name = ~base_path
  0.type = string
  0.default = `"$(find xbot_talker)"`
  0.desc =  Home directory of voice interactive configuration files and audio files.Please use the default value.
}
```


