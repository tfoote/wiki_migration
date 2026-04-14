## Overview

The
[DeepRacer Servo ROS package](https://github.com/aws-deepracer/aws-deepracer-servo-pkg)
creates the servo_node which is part of the core AWS DeepRacer
application and will be launched from the
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
name = servo_node
sub {
  0{
   name = /ctrl_pkg/servo_msg	
   type = msg/ServoCtrlMsg
   desc = This message holds the scaled throttle and angle values in the range of [-1, 1] that will be translated based on the calibration to raw PWM values.
   }
  1{
   name = /ctrl_pkg/raw_pwm
   type = msg/ServoCtrlMsg
   desc = This message holds the raw PWM throttle and angle values to be set on the motor and servo.
   }
}
srv {
  1{
   name = servo_gpio
   type = srv/ServoGPIOSrv
   desc = A service that is called enable/disable the servo GPIO pin.
  }
  2{
   name = set_calibration
   type = srv/SetCalibrationSrv
   desc = A service that is called to set the [min, mid, max, polarity] pwm values for the speed and steering calibration and store them in a file.
  }
  3{
   name = get_calibration
   type = srv/GetCalibrationSrv
   desc = A service that is called to get the [min, mid, max, polarity] pwm values for the speed and steering calibration from the saved file.
  }
  4{
   name = set_led_state
   type = srv/SetLedCtrlSrv
   desc = A service that is called to set the [red, green, blue] channel pwm values for the tail light LEDs and store them in a file.
  }
  5{
   name = get_led_state
   type = srv/GetLedCtrlSrv
   desc = A service that is called to get the [red, green, blue] channel pwm values for the tail light LEDs from the saved file.
  }
}
```
