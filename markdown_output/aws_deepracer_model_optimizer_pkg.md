## Overview

The
[DeepRacer Model Optimizer ROS package](https://github.com/aws-deepracer/aws-deepracer-model-optimizer-pkg)
creates the model_optimizer_node which is part of the core AWS DeepRacer
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
name = model_optimizer_node
srv {
  1{
   name = model_optimizer_server
   type = srv/ModelOptimizeSrv
   desc = Service that is called to launch the Intel OpenVino model optimizer script for the specific model with appropriate model and platform specific parameters set.
  }
}
```
