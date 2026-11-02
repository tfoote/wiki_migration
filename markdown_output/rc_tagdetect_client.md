See <http://rc-visard.com> and <http://doc.rc-visard.com> for more
details.



```wiki
'''This package is not developed anymore'''. New clients are available in the
[[rc_reason_clients]] package.
```



## Overview

This node provides ROS service calls and parameters for the
[TagDetect](https://roboception.com/product/tag-detection/) module.

For detail description of the
[TagDetect](https://roboception.com/product/tag-detection/) module check
the
[rc_visard manual](https://doc.rc-visard.com/latest/en/tagdetect.html).

## Configuration

### Parameters

- `host`: The IP address or hostname of the rc_visard that should be
  used.

**Since version 2.7, the device ID can be used instead of the sensor's
IP address:**

- `device`: The ID of the device, i.e. Roboception rc_visard sensor.
  This can be either:
- serial number, e.g. `02912345`. 

```wiki
Preceed with a colon (`:02912345`) when passing this on the commandline or setting it via rosparam (see https://gSinceithub.com/ros/ros_comm/issues/1339). This is not neccessary when specifying it as a string in a launch file.
```


- user defined name must be unique among all reachable sensors. If no
  device or host is given, this parameter works if just one rc_visard is
  connected.

### Dynamic reconfigure parameters

- `use_cached_images`: Use most recently received image pair instead
  of waiting for a new pair.
- `forget_after_n_detections`: Number of detection runs after which to
  forget about a previous tag during tag re-identification.
- `max_corner_distance`: Maximum distance of corresponding tag corners
  in meters during tag re-identification.
- `quality`: Quality of tag detection (H, M or L).
- `detect_inverted_tags`: Detect tags with black and white exchanged.
- `publish_visualization`: Whether or not the
  [tf](https://index.ros.org/p/tf2) and markers should be published.

### Services

The following services are offered to follow the calibration routine:

- `detect`: Triggers single detection.
- `start_continuous_detection`: Starts continuous detection.
- `stop_continuous_detection`: Stops continuous detection.

## Launch

Using command line parameters: 

```bash
rosrun rc_tagdetect_client rc_april_node _host:=<sensor_ip>
rosrun rc_tagdetect_client rc_qr_node _host:=<sensor_ip>
```



**Since version 2.7:**



```bash
rosrun rc_tagdetect_client rc_april_node _device:=:<serial_number>
rosrun rc_tagdetect_client rc_qr_node _device:=:<serial_number>
```



## Report a Bug

## Acknowledgements

![ROSIN Logo\|height=60](https://raw.githubusercontent.com/rosin-project/press_kit/master/img/rosin_ack_logo_wide.png)

Supported by ROSIN - ROS-Industrial Quality-Assured Robot Software
Components.\
More information: [rosin-project.eu](http://rosin-project.eu/)\

  -- --------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------- --
     ![EU Flag\|height=45](https://raw.githubusercontent.com/rosin-project/press_kit/master/img/rosin_eu_flag.jpg)      <99%> This project has received funding from the European Union's Horizon 2020\   
                                                                                                                        research and innovation programme under grant agreement No. 732287.                 

  -- --------------------------------------------------------------------------------------------------------------- -- ----------------------------------------------------------------------------------- --
