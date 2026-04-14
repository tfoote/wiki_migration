## Overview

The
[DeepRacer Control ROS package](https://github.com/aws-deepracer/aws-deepracer-ctrl-pkg)
creates the ctrl_node which is part of the core AWS DeepRacer
application which is launched from the
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
name = ctrl_node
sub {
  0{
   name = /deepracer_navigation_pkg/auto_drive
   type = msg/ServoCtrlMsg
   desc = Message with scaled steering angle and throttle data as per action space values sent to the servo package to move the car in autonomous mode.
   }
  1{
   name = /webserver_pkg/calibration_drive
   type = msg/ServoCtrlMsg
   desc = Message with raw pwm values for steering angle and throttle data sent to the servo package to calibrate the car in calibration mode.
   }
  2{
   name = /webserver_pkg/manual_drive
   type = msg/ServoCtrlMsg
   desc = Message with steering angle and throttle data sent to the servo package to move the car in manual mode.
   }
}
pub {
  0{
   name = /ctrl_pkg/raw_pwm
   type = msg/ServoCtrlMsg
   desc = Publisher to send a message with raw pwm values for steering angle and throttle data sent to the servo package to calibrate the car.
   }
  1{
   name = /ctrl_pkg/servo_msg
   type = msg/ServoCtrlMsg
   desc = Publisher to send a message with steering angle and throttle data sent to the servo package to move the car.
   }
}

srv {
  1{
   name = vehicle_state
   type = srv/ActiveStateSrv
   desc = Service that is called to set the vehicle mode by deactivating the current vehicle state and set the new mode.
  }
  2{
   name = enable_state
   type = srv/EnableStateSrv
   desc = Service that is called to activate and deactivate the current vehicle mode.
  }
  3{
   name = get_car_cal
   type = srv/GetCalibrationSrv
   desc = Service that is called to get the current calibration PWM values [min, mid, max, polarity] for the steering or throttle.
   }
  4{
   name = set_car_cal
   type = srv/SetCalibrationSrv
   desc = Service that is called to set the calibration PWM values  [min, mid, max, polarity] for the steering or throttle.
   }
  5{
   name = set_car_led
   type = srv/SetLedCtrlSrv
   desc = Service that is called to set the tail light LED [red, green, blue] channel PWM values.
   }
  6{
   name = get_car_led
   type = srv/GetLedCtrlSrv
   desc = Service that is called to get the tail light LED [red, green, blue] channel PWM values.
   }
  7{
   name = model_state
   type = srv/ModelStateSrv
   desc = Service that is called to execute the load model services in background thread.
   }
  8{
   name = autonomous_throttle
   type = srv/NavThrottleSrv
   desc = Service that is called to set the scale value to multiply to the throttle during autonomous navigation.
   }
  9{
   name = is_model_loading
   type = srv/GetModelLoadingStatusSrv
   desc = Service that is called to know if there is load model operation going on right now on the device in autonomous mode.
   }
}

srv_called {
   1{
   name = /model_optimizer_pkg/model_optimizer_server
   type = srv/ModelOptimizeSrv
   desc = Client to the model optimizer service that is called to trigger the model optimizing script for the current model selected in autonomous mode.
  }
  2{
   name = /inference_pkg/load_model
   type = srv/LoadModelSrv
   desc = Client to the load model service from the inference package that is called to set the preprocessing and inference task details in autonomous mode.
  }
  3{
   name = /inference_pkg/inference_state
   type = srv/InferenceStateSrv
   desc = Client to service that is called to enable/disable inference function on the stream of sensor messages in autonomous mode.
   }
  4{
   name = /servo_pkg/servo_gpio
   type = srv/ServoGPIOSrv
   desc = Client ot service that is called to enable/disable the servo GPIO to allow setting the PWM values on the servo and motor.
   }
  5{
   name = /servo_pkg/set_calibration
   type = srv/SetCalibrationSrv
   desc = Client to set the calibration value for the steering or throttle in calibration mode.
   }
  6{
   name = /servo_pkg/get_calibration
   type = srv/GetCalibrationSrv
   desc = Client to get the current calibration value for the steering or throttle in calibration mode.
   }
  7{
   name = /servo_pkg/get_led_state
   type = srv/GetLedCtrlSrv
   desc = Client to get car led service to get the tail light LED channel PWM values in calibration mode.
   }
  8{
   name = /servo_pkg/set_led_state
   type = srv/SetLedCtrlSrv
   desc = Client to set car led service to set the tail light LED channel PWM values in calibration mode.
   }
  9{
   name = /deepracer_navigation_pkg/navigation_throttle
   type = srv/NavThrottleSrv
   desc = Client to service that is called set the scale value for the navigation throttle in autonomous mode to control the speed of the device.
   }
  10{
   name = /deepracer_navigation_pkg/load_action_space
   type = srv/LoadModelSrv
   desc = Client to load action space service that is called to set the action space for the model in deepracer_navigation_node to be used while mapping the inference results to the action values in autonomous mode.
  }
}
```
