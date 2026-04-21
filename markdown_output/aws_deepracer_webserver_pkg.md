## Overview

The
[DeepRacer Web Server ROS package](https://github.com/aws-deepracer/aws-deepracer-webserver-pkg)
creates the webserver_publisher_node which is part of the core AWS
DeepRacer application and will be launched from the
[deepracer_launcher](https://github.com/aws-deepracer/aws-deepracer-launcher).
More details about the application and the components can be found
[here](https://github.com/aws-deepracer/aws-deepracer-launcher).

### License

The source code is released under
[Apache 2.0](https://aws.amazon.com/apache-2-0/).

### Supported ROS Distributions

-   Foxy

## Node Details



```clearsilver
name = webserver_publisher_node
sub {
  0{
   name = /deepracer_systems_pkg/software_update_pct
   type = msg/SoftwareUpdatePctMsg
   desc = Message with the latest software update percentage and status.
   }
}
pub {
  0{
   name = /webserver_pkg/calibration_drive
   type = msg/ServoCtrlMsg
   desc = Publish a message with raw pwm values for steering angle and throttle data sent to the servo package to calibrate the car.
   }
  1{
   name = /webserver_pkg/manual_drive
   type = msg/ServoCtrlMsg
   desc = Publish a message with steering angle and throttle data sent to the servo package to move the car.
   }
}

srv_called {
   1{
   name = /ctrl_pkg/vehicle_state
   type = srv/ActiveStateSrv
   desc = Client to the vehicle state service to deactivate the current vehicle state and prepare the new mode.
  }
  2{
   name = /ctrl_pkg/enable_state
   type = srv/EnableStateSrv
   desc = Client to the enable state service to activate and deactivate the current vehicle mode.
  }
  3{
   name = /ctrl_pkg/get_car_cal
   type = srv/GetCalibrationSrv
   desc = Client to the get calibration service to get the current calibration value for the steering or throttle.
   }
  4{
   name = /ctrl_pkg/set_car_cal
   type = srv/SetCalibrationSrv
   desc = Client to the set calibration service to set the current calibration value for the steering or throttle.
   }
  5{
   name = /device_info_pkg/get_device_info
   type = srv/GetDeviceInfoSrv
   desc = Client to the get device info service to get the hardware and software version of DeepRacer device and packages.
   }
  6{
   name = /i2c_pkg/battery_level
   type = srv/BatteryLevelSrv
   desc = Client to the battery level service to get the current vehicle battery level ranging from [0 to 11].
   }
  7{
   name = /sensor_fusion_pkg/sensor_data_status
   type = srv/SensorStatusCheckSrv
   desc = Client to the sensor data status service to get the sensor connection status for single camera/stereo camera and LiDAR.
   }
  8{
   name = /ctrl_pkg/set_led_state
   type = srv/SetLedCtrlSrv
   desc = Client to set car led service to set the tail light LED values.
   }
  9{
   name = /ctrl_pkg/get_led_state
   type = srv/GetLedCtrlSrv
   desc = Client to get car led service to get the tail light LED values.
   }
  10{
   name = /deepracer_systems_pkg/verify_model_ready
   type = srv/VerifyModelReadySrv
   desc = Client to verify model service to validate if the extraction and installation of the model was successful.
   }
   11{
   name = /sensor_fusion_pkg/configure_lidar
   type = srv/LidarConfigSrv
   desc = Client to configure lidar service to dynamically configure the preprocessing details for the LiDAR data before publishing as part of sensor message.
   }
   14{
   name = /deepracer_systems_pkg/console_model_action
   type = srv/ConsoleModelActionSrv
   desc = Client to the get otg link state service to get the current connection status of micro-USB cable to the DeepRacer device.
   }
   14{
   name = /deepracer_systems_pkg/console_model_action
   type = srv/ConsoleModelActionSrv
   desc = Client to the get otg link state service to get the current connection status of micro-USB cable to the DeepRacer device.
   }
   14{
   name = /deepracer_systems_pkg/console_model_action
   type = srv/ConsoleModelActionSrv
   desc = Client to trigger the upload/delete models action from device console.
   }
   14{
   name = /deepracer_systems_pkg/console_model_action
   type = srv/ConsoleModelActionSrv
   desc = Client to trigger the upload/delete models action from device console.
   }
   15{
   name = /deepracer_systems_pkg/software_update_check
   type = srv/SoftwareUpdateCheckSrv
   desc = Client to the software update check service to find out if there is a software update available for the aws-deepracer packages.
   }
   16{
   name = /deepracer_systems_pkg/begin_update
   type = srv/BeginSoftwareUpdateSrv
   desc = Client to the begin update service to trigger the update of the aws-deepracer debian packages to the latest software version available.
   }
   17{
   name = /deepracer_systems_pkg/software_update_state
   type = srv/SoftwareUpdateStateSrv
   desc = Client to software update state service to get the current software update state from the states [UPDATE_UNKNOWN, UP_TO_DATE, UPDATE_AVAILABLE, UPDATE_PENDING, UPDATE_IN_PROGRESS].
   }
   18{
   name = /ctrl_pkg/autonomous_throttle
   type = srv/NavThrottleSrv
   desc = Client to autonomous throttle service to set the scale value to multiply to the throttle during autonomous navigation.
   }
  19{
   name = /deepracer_systems_pkg/get_otg_link_state
   type = srv/OTGLinkStateSrv
   desc = Client to the get otg link state service to get the current connection status of micro-USB cable to the DeepRacer device.
   }
}
```


