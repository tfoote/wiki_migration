## Overview

The
[DeepRacer Navigation ROS package](https://github.com/aws-deepracer/aws-deepracer-navigation-pkg)
creates the deepracer_navigation_node which is part of the core AWS
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
name = deepracer_navigation_node
sub {
  0{
   name = /inference_pkg/rl_results
   type = msg/InferResultsArray
   desc = This message holds the reinforcement learning inference results for the state input passed through the current model that is selected in the device console.
   }
}
pub {
  0{
   name = /deepracer_navigation_pkg/auto_drive
   type = msg/ServoCtrlMsg
   desc = Publish a message with steering angle and throttle data sent to the servo package to move the car.
   }
}

srv {
  1{
   name = action_space_service
   type = srv/LoadModelSrv
   desc = A service that is called when a new model is loaded and helps set the action space to be considered while mapping the inference results
  }
  2{
   name = throttle_service
   type = srv/NavThrottleSrv
   desc = A service that is called to dynamically set the scale value to multiply to the throttle in autonomous mode for each action.
  }
  
}
```


