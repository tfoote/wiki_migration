## Overview

The
[DeepRacer Inference ROS package](https://github.com/aws-deepracer/aws-deepracer-inference-pkg)
creates the inference_node which is part of the core AWS DeepRacer
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
name = inference_node
sub {
  1{
   name = /sensor_fusion_pkg/sensor_msg
   type = msg/EvoSensorMsg
   desc = Message with the combined sensor data. Contains single camera/two camera images and LiDAR distance data.
  }
}
pub {
  1{
   name = /inference_pkg/rl_results
   type = msg/InferResultsArray
   desc = Publish a message with the reinforcement learning inference results with class probabilities for the state input passed through the current model that is selected in the device console.
  }
}
srv {
  1{
   name = load_model
   type = srv/LoadModelSrv
   desc = Service that is responsible for setting pre-processing algorithm and inference task for the specific type of model loaded.
  }
  2{
   name = inference_state
   type = srv/InferenceStateSrv
   desc = Service that is responsible for starting and stopping inference tasks.
  }
}
```
