## Overview

This package provides a ROS interface for the DJI onboard SDK and
enables the users to take full control of supported platforms (DJI M100,
M600, M210, or drones equipped with A3/N3 flight controllers) using ROS
messages and services.

This package depends on DJI SDK core library, which can be found
[here](https://github.com/dji-sdk/Onboard-SDK).

The latest releases 3.4 and 3.5 introduce support for Matrice 210 and
210 RTK. Developers will now have access to previously unavailable data
such as stereo camera feeds (front-facing and downward-facing), FPV
camera stream, and main gimbaled camera stream through USB. M210 Users
will need to upgrade to the latest firmware (1.1.0410) to work with
Onboard SDK and to download the latest DJI Assistant 2 (1.1.8) for
simulation.

```wiki
'''ATTENTION:'''

Since version 3.3, the `dji_sdk` ROS package starts to follow the [[http://www.ros.org/reps/rep-0103.html|REP103]] convention on coordinate frame and units for the telemetry data. In the header of most of the telemetry data such as imu and attitude, the `frame_id` is either `"body_FLU"` or `ground_ENU`, to make it explicit. The flight control signals subscribed by the `dji_sdk` node are also supposed to be `FLU` for body frame or `ENU` for ground frame. The gimbal related data is currently NOT fully following the convention yet.
```

## Nodes

```clearsilver
node.0{
name = dji_sdk
desc = The main wrapper node for DJI Onboard SDK
pub {
  0.name = /dji_sdk/acceleration_ground_fused
  0.type = geometry_msgs/Vector3Stamped
  0.desc = Fused acceleration with respect to East-North-Up (ENU) ground frame, published at 100 Hz. '''This topic is unavailable on M100. Use imu topic for raw acceleration.'''
 
  1.name = /dji_sdk/angular_velocity_fused
  1.type = geometry_msgs/Vector3Stamped
  1.desc = Fused angular rate (p,q,r) around Forward-Left-Up (FLU) body frame, published at 100 Hz. '''This topic is unavailable on M100. Use imu topic for raw rate.'''
 
  2.name = /dji_sdk/attitude
  2.type = geometry_msgs/QuaternionStamped
  2.desc = Vehicle attitude represented as quaternion for the rotation from FLU body frame to ENU ground frame, published at 100 Hz.
  
  3.name = /dji_sdk/battery_state
  3.type = sensor_msgs/BatteryState
  3.desc = Report the current battery voltage at 10 Hz
 
  4.name = /dji_sdk/display_mode
  4.type = std_msgs/UInt8
  4.desc = Display mode is the detailed status of the drone. All supported status are listed in dji_sdk.h. Published at 50 Hz. '''This topic is unavailable on M100'''.

  5.name = /dji_sdk/flight_status
  5.type = std_msgs/UInt8
  5.desc = Simple status of the vehicle published at 50 Hz, detailed status are listed in dji_sdk.h. Note that status for M100 and A3/N3 are different.

  6.name = /dji_sdk/from_mobile_data
  6.type = std_msgs/UInt8[]
  6.desc = Data received from mobile device to the vehicle.

  7.name = /dji_sdk/gimbal_angle
  7.type = geometry_msgs/Vector3Stamped
  7.desc = Current gimbal joint angles, published at 50 Hz. If no gimbal present, default publishes all zeros.

  8.name = /dji_sdk/gps_health
  8.type = std_msgs/UInt8
  8.desc = GPS signal health is between 0 and 5, 5 is the best condition. Use gps_position for control only if gps_health >= 3. Published at 50 Hz.

  9.name = /dji_sdk/gps_position
  9.type = sensor_msgs/NavSatFix
  9.desc = Fused global position of the vehicle in latitude, longitude and altitude(m). Position in WGS 84 reference ellipsoid, published at 50 Hz. If no gps present, default publishes longitude and latitude equal zeros.

  10.name = /dji_sdk/imu
  10.type = sensor_msgs/Imu
  10.desc = IMU data including raw gyro reading in FLU body frame, raw accelerometer reading in FLU body frame, and attitude estimation, published at '''100 Hz for M100, and 400 Hz for other platforms'''. Note that raw accelerometer reading will give a Z direction 9.8 m/s^2^ when the drone is put on a level ground statically.

  11.name = /dji_sdk/rc
  11.type = sensor_msgs/Joy
  11.desc<<EOM 
Reading of the 6 channels of the remote controller, published at 50 Hz.

 ||<rowbgcolor="#FFFFE0"> ''' sensor_msgs/Joy ''' || description (LB2, M100) || description (SBUS) || Range (LB2) || Range (SBUS) || Range (M100) ||
 ||<rowbgcolor="#e6f3ff">axes[0]|| Roll Channel|| Channel A || -1 to +1|| -1 to +1|| -1 to +1||
 ||<rowbgcolor="#e6f3ff">axes[1]|| Pitch Channel || Channel E || -1 to +1 || -1 to +1|| -1 to +1||
 ||<rowbgcolor="#e6f3ff">axes[2]|| Yaw Channel|| Channel R || -1 to +1 || -1 to +1|| -1 to +1||
 ||<rowbgcolor="#e6f3ff">axes[3]|| Throttle Channel|| Channel T || -1 to +1 || -1 to +1|| -1 to +1||
 ||<rowbgcolor="#e6f3ff">axes[4]|| Mode switch || Channel U ||-10000, 0, 10000 ||-10000, 0, 10000 || -8000, 0, 8000||
 ||<rowbgcolor="#e6f3ff">axes[5]|| Landing gear (H) switch || Channel Gear || -5000, -10000|| -10000, 10000 || -4545, -10000||
 ||<rowbgcolor="#FFFFE0"> '''Known bug''' ||||||||||<(>For SBUS controllers, the gear output depend on the channel mapping. Please refer to DJI Assistant 2 Remote controller settings.||
 
EOM

  12.name = /dji_sdk/velocity
  12.type = geometry_msgs/Vector3Stamped
  12.desc = Velocity in ENU ground frame, published at 50 Hz. The velocity is valid only when gps_health >= 3.

  13.name = /dji_sdk/height_above_takeoff
  13.type = std_msgs/Float32
  13.desc = Height above takeoff location. '''It is only valid after drone is armed, when the flight controller has a reference altitude set'''.

  14.name = /dji_sdk/trigger_time
  14.type = sensor_msgs/TimeReference
  14.desc = The time at which a hardware sync pulse is generated by the flight controller. '''This topic is unavailable on M100.'''

  15.name = /dji_sdk/local_position
  15.type = geometry_msgs/PointStamped
  15.desc = Local position in Cartesian ENU frame, of which the origin is set by the user by calling the /dji_sdk/set_local_pos_ref service. Note that the local position is calculated from GPS position, so '''good GPS health is needed''' for the local position to be useful.

  16.name = /dji_sdk/rtk_position
  16.type = sensor_msgs/NavSatFix
  16.desc = RTK position published at 10hz '''Only available when RTK present'''

  17.name = /dji_sdk/rtk_velocity
  17.type = geometry_msgs/Vector3
  17.desc = Velocty measure by RTK published at 10hz'''Only available when RTK present'''

  18.name = /dji_sdk/rtk_yaw
  18.type = std_msgs/Int16
  18.desc = The azimuth measured by RTK published at 10hz'''Only available when RTK present'''

  19.name = /dji_sdk/rtk_info_position
  19.type = std_msgs/UInt8
  19.desc = The type of RTK positioning, indicating different solutions for calculating the position published at 10hz. '''Only available when RTK present'''

  20.name = /dji_sdk/rtk_info_yaw
  20.type = std_msgs/UInt8
  20.desc = The type of RTK orientation, indicating different solutions for calculating the orientation published at 10hz. '''Only available when RTK present'''

  21.name = /dji_sdk/stereo_240p_front_left_images
  21.type = sensor_msgs/Image
  21.desc = stereo image from the front-left camera of M210 in 240x320 resolution

  22.name = /dji_sdk/stereo_240p_front_right_images
  22.type = sensor_msgs/Image
  22.desc = stereo image from the front-right camera of M210 in 240x320 resolution

  23.name = /dji_sdk/stereo_240p_down_front_images
  23.type = sensor_msgs/Image
  23.desc = stereo image from the down-front camera of M210 in 240x320 resolution

  24.name = /dji_sdk/stereo_240p_down_back_images
  24.type = sensor_msgs/Image
  24.desc = stereo image from the down-back camera of M210 in 240x320 resolution

  25.name = /dji_sdk/stereo_240p_front_depth_images
  25.type = sensor_msgs/Image
  25.desc = stereo disparity map from the front-facing camera of M210 in 240x320 resolution

  26.name = /dji_sdk/stereo_vga_front_left_images
  26.type = sensor_msgs/Image
  26.desc = stereo image from the front-left camera of M210 in 640x480 resolution

  27.name = /dji_sdk/stereo_vga_front_right_images
  27.type = sensor_msgs/Image
  27.desc = stereo image from the front-right camera of M210 in 640x480 resolution

  28.name = /dji_sdk/fpv_camera_images
  28.type = sensor_msgs/Image
  28.desc = RGB image from the FPV camera of M210 in 608x448 resolution

  29.name = /dji_sdk/main_camera_images
  29.type = sensor_msgs/Image
  29.desc = RGB image from the main camera of M210. Resolution can be set in DJI Go App
}
}

sub {
 group.0{
  name = 1. Flight Control Topics

  desc << EOM

The user send flight control setpoints to the drone by publishing one of the following topics, which are subscribed by the dji_sdk node. All the fight control topics has message type sensor_msg/Joy. 

Among the flight control topics, the dji_sdk/flight_control_setpoint_generic is the most general one and requires the user to provide the control '''flag''' which dictates how the inputs are interpreted by the flight controller, while the rest are wrappers for the convenience of users and don't need the flag. All supported flags are listed in dji_sdk.h .

EOM

  0.name = /dji_sdk/flight_control_setpoint_generic
  0.type = sensor_msgs/Joy
  0.desc = General setpoint where axes[0] to axes[3] stores set-point data for the 2 horizontal channels, the vertical channel, and the yaw channel, respectively. The meaning of the set-point data will be interpreted based on the control flag which is stored in axes[4].

  1.name = /dji_sdk/flight_control_setpoint_ENUposition_yaw
  1.type = sensor_msgs/Joy
  1.desc = Command the X, Y '''position offset''', Z position (height) and yaw angle in ENU ground frame.
  
  2.name = /dji_sdk/flight_control_setpoint_ENUvelocity_yawrate
  2.type = sensor_msgs/Joy
  2.desc = Command the X, Y, Z velocity in ENU ground frame and yaw rate.

  3.name = /dji_sdk/flight_control_setpoint_rollpitch_yawrate_zposition
  3.type = sensor_msgs/Joy
  3.desc = Command the roll pitch angle, height, and yaw rate.
 }

 group.1{
  name = 2. Gimbal Control
  desc = The subscribers that takes the input for Gimbal arm controls.
  0.name = /dji_sdk/gimbal_angle_cmd
  0.type = dji_sdk/Gimbal
  0.desc = Gimbal control command: Controls the Gimbal roll pitch and yaw angles (unit: 0.1 deg). mode: 0 - incremental control, the angle reference is the current Gimbal location. 1 - absolute control, the angle reference is related to configuration in DJI Go App.
  
  1.name = /dji_sdk/gimbal_speed_cmd
  1.type = geometry_msgs/Vector3Stamped
  1.desc << EOM
Gimbal speed command: Controls the Gimbal rate of change for roll pitch and yaw angles (unit: 0.1 deg/sec).
EOM
 }
}
srv {
  0.name = /dji_sdk/activation
  0.type = dji_sdk/Activation
  0.desc << EOM
  The service to activate the drone with app ID and key pair. The activation arguments should be specified in launch files.
  Usage:
   ||<rowbgcolor="#f2f2f2">Response||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--invalid action||
EOM 

  1.name = /dji_sdk/camera_action
  1.type = dji_sdk/CameraAction
  1.desc << EOM
  Take photo or video via service, return true if successful.
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||||
   ||<#FFFFE0>Uint8 Camera_action||<#e6f3ff>0--Shoot Photo||<#e6f3ff>1--Start video taking||<#e6f3ff>2--Stop video taking||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--invalid action||
EOM 

  2.name = /dji_sdk/drone_arm_control
  2.type = dji_sdk/DroneArmControl
  2.desc << EOM
  Enable or disable vehicle's arm motors.
  Usage: 
   ||<rowbgcolor="#f2f2f2">Request||||||
   ||<#FFFFE0>uint8 arm||<#e6f3ff>1--enable vehicle arm motor||<#e6f3ff>else: disable arm motor||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--invalid action||
EOM 

  3.name = /dji_sdk/drone_task_control
  3.type = dji_sdk/DroneTaskControl
  3.desc << EOM
  Execute takeoff, landing or go home.
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||||
   ||<#FFFFE0>uint8 task||<#e6f3ff>4--takeoff||<#e6f3ff>6--landing||<#e6f3ff>1--gohome||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM

  5.name = /dji_sdk/mfio_config
  5.type = dji_sdk/MFIOConfig
  5.desc << EOM
  Config Multi-function IO. '''This service is unavailable on M100'''
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||||||||
   ||<#FFFFE0>uint8 mode||<#e6f3ff>0--PWM_OUT||<#e6f3ff>1--PWM_IN||<#e6f3ff>2--GPIO_OUT||<#e6f3ff>3--GPIO_IN||<#e6f3ff>4--ADC||
   ||<#FFFFE0>uint8 channel||<#e6f3ff>0-7||
   ||<#FFFFE0>uint32 init_on_time_us||
   ||<#FFFFE0>uint16 pwm_freq||
EOM 

  6.name = /dji_sdk/mfio_set_value
  6.type = dji_sdk/MFIOSetValue
  6.desc << EOM
  Set MFIO value. '''This service is unavailable on M100'''
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||
   ||<#FFFFE0>uint8 channel||<#e6f3ff>0-7||
   ||<#FFFFE0>uint32 init_on_time_us||
EOM 

  7.name = /dji_sdk/mission_hotpoint_action
  7.type = dji_sdk/MissionHpAction
  7.desc << EOM
  Service that start/stop/pause/resume the hotpoint mission.
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||||||
   ||<#FFFFE0>uint8 action||<#e6f3ff>0--start||<#e6f3ff>1--stop||<#e6f3ff>2--pause||<#e6f3ff>3--resume||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  8.name = /dji_sdk/mission_hotpoint_getInfo
  8.type = dji_sdk/MissionHpGetInfo
  8.desc << EOM
  Return the hotpoint tasks info. Use rosmsg show dji_sdk/MissionHotpointTask for more detail
  Usage:
   ||<rowbgcolor="#f2f2f2">Response||
   ||<#FFFFE0>MissionHotpointTask hotpoint_task||
EOM 

  9.name = /dji_sdk/mission_hotpoint_resetYaw
  9.type = dji_sdk/MissionHpResetYaw
  9.desc << EOM
  Resets the Yaw position of the vehicle
  Usage:
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  10.name = /dji_sdk/mission_hotpoint_updateRadius
  10.type = dji_sdk/MissionHpUpdateRadius
  10.desc << EOM
  Update the radius of the hot point mission
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||
   ||<#FFFFE0>float32 radius||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  11.name = /dji_sdk/mission_hotpoint_updateYawRate
  11.type = dji_sdk/MissionHpUpdateYawRate
  11.desc << EOM
  Update the rate of change for Yaw and the direction of the change.
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||
   ||<#FFFFE0>float32 yaw_rate||
   ||<#FFFFE0>uint8 direction||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  12.name = /dji_sdk/mission_hotpoint_upload
  12.type = dji_sdk/MissionHpUpload
  12.desc << EOM
  Upload a set of hotpoint tasks to the vehicle. Use rosmsg show dji_sdk/MissionHotpointTask for more detail
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||
   ||||<#FFFFE0>MissionHotpointTask hotpoint_task||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  13.name = /dji_sdk/mission_waypoint_action
  13.type = dji_sdk/MissionWpAction
  13.desc << EOM
  Start/stop/pause/resume waypoint action.
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||||||
   ||<#FFFFE0>uint8 action||<#e6f3ff>0--start||<#e6f3ff>1--stop||<#e6f3ff>2--pause||<#e6f3ff>3--resume||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  14.name = /dji_sdk/mission_waypoint_getInfo
  14.type = dji_sdk/MissionWpGetInfo
  14.desc << EOM
  Get the current waypoint tasks. Use rosmsg show dji_sdk/MissionWaypointTask for more detail
  Usage:
   ||<rowbgcolor="#f2f2f2">Response||
   ||<#FFFFE0>MissionWaypointTask waypoint_task||
EOM 

  15.name = /dji_sdk/mission_waypoint_getSpeed
  15.type = dji_sdk/MissionWpGetSpeed
  15.desc << EOM
  Return the waypoint velocity
  Usage:
   ||<rowbgcolor="#f2f2f2">Response||
   ||<#FFFFE0>float32 speed||
EOM 

  16.name = /dji_sdk/mission_waypoint_setSpeed
  16.type = dji_sdk/MissionWpSetSpeed
  16.desc << EOM
  Set the waypoint velocity.
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||
   ||<#FFFFE0>float32 speed||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  17.name = /dji_sdk/mission_waypoint_upload
  17.type = dji_sdk/MissionWpUpload
  17.desc << EOM
  Upload a new waypoint task, return true if succeed. Use rosmsg show dji_sdk/MissionWaypointTask for more detail
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||
   ||<#FFFFE0>MissionWaypointTask waypoint_task||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  18.name = /dji_sdk/sdk_control_authority
  18.type = dji_sdk/SDKControlAuthority
  18.desc << EOM
  request/release the control authority
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||
   ||<#FFFFE0>uint8 control_enable||<#e6f3ff>1--request control||<#e6f3ff>0--release control||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  19.name = /dji_sdk/send_data_to_mobile
  19.type = dji_sdk/SendMobileData
  19.desc << EOM
  Send data to the mobile side. The length of the data is upper-limited to 100.
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||
   ||<#FFFFE0>uint8[] data||<#e6f3ff>length(data) <= 100||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  20.name = /dji_sdk/set_hardsyc
  20.type = dji_sdk/SetHardSync
  20.desc << EOM
  Set Hard Sync. '''This service is unavailable on M100'''
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||
   ||<#FFFFE0>uint32 frequency||<#e6f3ff>frequency in Hz||
   ||<#FFFFE0>uint16 tag||||<#e6f3ff>the tag is to distinguish between different call||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  21.name = /dji_sdk/query_drone_version
  21.type = dji_sdk/QueryDroneVersion
  21.desc = Query drone firmware version. Available version list can be found in dji_sdk.h

  22.name = /dji_sdk/set_local_pos_ref
  22.type = dji_sdk/SetLocalPosRef
  22.desc = Set the origin of the local position to be the current GPS coordinate. Fail if GPS health is low (<=3).

  23.name = /dji_sdk/stereo_240p_subscription
  23.type = dji_sdk/Stereo240pSubscription
  23.desc << EOM
  subscribe to stereo images from the front-facing and down-facing cameras of M210 in 240x320 resolution. If '''unsubscribe_240p''' is 1, service will unsubscribe no matter what. '''This service is only available on M210.'''
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||
   ||<#FFFFE0>uint8 front_right_240p||<#e6f3ff>1--subscribe||<#e6f3ff>0--no behavior||
   ||<#FFFFE0>uint8 front_left_240p||<#e6f3ff>1--subscribe||<#e6f3ff>0--no behavior||
   ||<#FFFFE0>uint8 down_front_240p||<#e6f3ff>1--subscribe||<#e6f3ff>0--no behavior||
   ||<#FFFFE0>uint8 down_back_240p||<#e6f3ff>1--subscribe||<#e6f3ff>0--no behavior||
   ||<#FFFFE0>uint8 unsubscribe_240p||<#e6f3ff>1--unsubscribe||<#e6f3ff>0--no behavior||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  24.name = /dji_sdk/stereo_depth_subscription
  24.type = dji_sdk/StereoDepthSubscription
  24.desc << EOM
  subscribe to stereo disparity map from the front-facing camera of M210 in 240x320 resolution. If '''unsubscribe_240p''' is 1, service will unsubscribe no matter what. '''This service is only available on M210.'''
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||
   ||<#FFFFE0>uint8 front_depth_240p||<#e6f3ff>1--subscribe||<#e6f3ff>0--no behavior||
   ||<#FFFFE0>uint8 unsubscribe_240p||<#e6f3ff>1--unsubscribe||<#e6f3ff>0--no behavior||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  25.name = /dji_sdk/stereo_vga_subscription
  25.type = dji_sdk/StereoVGASubscription
  25.desc << EOM
  subscribe to stereo images from the front-facing camera of M210 in 640x480 resolution. If '''unsubscribe_vga''' is 1, service will unsubscribe no matter what. '''This service is only available on M210.'''
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||
   ||<#FFFFE0>uint8 vga_freq||<#e6f3ff>0--20Hz||<#e6f3ff>1--10Hz||
   ||<#FFFFE0>uint8 front_vga||<#e6f3ff>1--subscribe||<#e6f3ff>0--no behavior||
   ||<#FFFFE0>uint8 unsubscribe_vga||<#e6f3ff>1--unsubscribe||<#e6f3ff>0--no behavior||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 

  26.name = /dji_sdk/setup_camera_stream
  26.type = dji_sdk/SetupCameraStream
  26.desc << EOM
  subscribe to FPV and/or main camera images. '''This service is only available on M210.'''
  Usage:
   ||<rowbgcolor="#f2f2f2">Request||||||
   ||<#FFFFE0>uint8 cameraType||<#e6f3ff>0--FPV camera||<#e6f3ff>1--main camera||
   ||<#FFFFE0>uint8 start||<#e6f3ff>1--start||<#e6f3ff>0--stop||
   ||<rowbgcolor="#f2f2f2">Response||||||
   ||<#FFFFE0>bool result||<#e6f3ff>true--succeed||<#e6f3ff>false--failed||
EOM 
}
param {
  0.name = ~/dji_sdk/app_id
  0.type = int
  0.desc <<EOM
You must register as a developer with DJI and create an onboard SDK application ID and Key pair. Please go to https://developer.dji.com/register/ to complete registration.
EOM

  1.name = ~/dji_sdk/baud_rate
  1.type = int
  1.desc = Baud rate should be set to match that is displayed in DJI Assistant 2 SDK settings. '''For M100, 230400 should be set on both DJI Assistant 2, and in launch file. For A3/N3, 921600 should be used.'''
  1.default = 921600

  2.name = ~/dji_sdk/enc_key
  2.type = string
  2.desc = You must register as a developer with DJI and create an onboard SDK application ID and Key pair. Please go to https://developer.dji.com/register/ to complete registration.
  2.default = Enter your enc key here

  3.name = ~/dji_sdk/serial_name
  3.type = string
  3.desc = The serial port name that the USB is connected with. Candidates can be /dev/ttyUSBx, /dev/ttyTHSx, etc.
  3.default = /dev/ttyUSB0

  4.name = ~/dji_sdk/use_broadcast
  4.tpye = bool
  4.desc = Choose to use subscription (supported only on A3/N3) or broadcast method (supported by both M100 and A3/N3) for accessing telemetry data. 
  4.default = false

}
}
}
```

#### Details on flight control setpoint

All the above flight control topics take setpoint values of the X, Y, Z,
and Yaw channels in axes\[0\]-axes\[3\]. In addition, the
/dji_sdk/flight_control_setpoint_generic topic requires a control
**flag** as axes\[4\] of the input. The control flag is an UInt8
variable that dictates how the inputs are interpreted by the flight
controller. It is the bitwise OR of 5 separate flags defined as enums in
dji_sdk.h, including Horizontal, Vertical, Yaw, Coordinate Frame, and
the Breaking Mode.

  -- --------------------------------------- -- ------------------------------- -- ------------- -- ----------------------- --
     \<rowbgcolor=\"#FFFFE0\"\> Horizontal      description                        reference        limit                   
     \<rowbgcolor=\"#e6f3ff\"\>0x00             Command roll and pitch angle       Ground/Body      0.611 rad (35 degree)   
     \<rowbgcolor=\"#e6f3ff\"\>0x40             Command horizontal velocities      Ground/Body      30 m/s                  
     \<rowbgcolor=\"#e6f3ff\"\>0x80             Command position offsets           Ground/Body      N/A                     
     \<rowbgcolor=\"#e6f3ff\"\>0xC0             Command angular rates              Ground/Body      5&frasl;6&pi; rad/s     
  -- --------------------------------------- -- ------------------------------- -- ------------- -- ----------------------- --

  -- ------------------------------------- -- ---------------------------- -- ----------- -- ------------- --
     \<rowbgcolor=\"#FFFFE0\"\> Vertical      description                     reference      limit         
     \<rowbgcolor=\"#e6f3ff\"\>0x00           Command the vertical speed      Ground         -5 to 5 m/s   
     \<rowbgcolor=\"#e6f3ff\"\>0x10           Command altitude                Ground         0 to 120 m    
     \<rowbgcolor=\"#e6f3ff\"\>0x20           Command thrust                  Body           0% to 100%    
  -- ------------------------------------- -- ---------------------------- -- ----------- -- ------------- --

  -- -------------------------------- -- ------------------- -- ----------- -- --------------------- --
     \<rowbgcolor=\"#FFFFE0\"\> Yaw      description            reference      limit                 
     \<rowbgcolor=\"#e6f3ff\"\>0x00      Command yaw angle      Ground         -&pi; to &pi;         
     \<rowbgcolor=\"#e6f3ff\"\>0x08      Command yaw rate       Ground         5&frasl;6&pi; rad/s   
  -- -------------------------------- -- ------------------- -- ----------- -- --------------------- --

  -- --------------------------------------- -- ---------------------------------------- --
     \<rowbgcolor=\"#FFFFE0\"\> Coordinate      description                              
     \<rowbgcolor=\"#e6f3ff\"\>0x00             Horizontal command is ground_ENU frame   
     \<rowbgcolor=\"#e6f3ff\"\>0x02             Horizontal command is body_FLU frame     
  -- --------------------------------------- -- ---------------------------------------- --

  -- ----------------------------------------- -- ------------------------------------------------------------- --
     \<rowbgcolor=\"#FFFFE0\"\> Active Break      description                                                   
     \<rowbgcolor=\"#e6f3ff\"\>0x00               No active break                                               
     \<rowbgcolor=\"#e6f3ff\"\>0x01               Actively break to hold position after stop sending setpoint   
  -- ----------------------------------------- -- ------------------------------------------------------------- --
