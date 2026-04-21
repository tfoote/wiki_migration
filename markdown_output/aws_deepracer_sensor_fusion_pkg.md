## Overview

The
[DeepRacer Sensor Fusion ROS package](https://github.com/aws-deepracer/aws-deepracer-sensor-fusion-pkg)
creates the sensor_fusion_node which is part of the core AWS DeepRacer
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
name = sensor_fusion_node
sub {
  0{
   name = /rplidar_ros/scan
   type = msg/LaserScan
   desc = This message holds the LiDAR data published by the rplidar_ros package.
   }
  1{
   name = /camera_pkg/video_mjpeg
   type = msg/CameraMsg
   desc = This message holds the single camera or two camera images from the connected cameras published by the camera_pkg.
   }
   2{
   name = /camera_pkg/display_mjpeg
   type = msg/Image
   desc = This message holds one camera image used for display in the UI published by the camera_pkg.
   }
}
pub {
    1{
    name = /sensor_fusion_pkg/overlay_msg
    type = msg/Image
    desc = Publisher to publish the overlay message with sector LiDAR information highlighting nearby obstacles overlayed over the camera image frame.   
    }
    2{
    name = /sensor_fusion_pkg/sensor_msg
    type = msg/EvoSensorMsg
    desc = Publisher that publishes combined sensor messages with camera data and LiDAR data.
    }
}
srv {
  1{
   name = sensor_data_status
   type = srv/SensorStatusCheckSrv
   desc = Service that is called to find out the data status of the cameras and the LiDAR sensors. Based on whether the single camera/stereo camera/LiDAR data is being read by the node, the corresponding sensor status are set.
  }
  2{
   name = configure_lidar
   type = srv/LidarConfigSrv
   desc = Service called to dynamically configure LiDAR processing information for each model. It allows to set the LiDAR preprocessing information like the maximum distance, minimum distance, number of sectors etc., which will be used to create the sensor message being published for running the inference for the particular model selected.
  }
}
```


