## Overview

This package contains nodes to enable the use of Toposens ECHO ONE
sensor within ROS. Data will be published as
\<\<MsgLink(toposens_msgs/TsScan)\>\>.

## ROS Nodes

```clearsilver
name = toposens_echo_driver_node
desc = Communicates with the Toposens Sensor Library and publishes ECHO ONE point clouds as <<MsgLink(toposens_msgs/TsScan)>>.
pub {
  0.name = ts_scans
  0.type = toposens_msgs/TsScan
  0.desc = Point cloud with additional header information and XYZIC points (x, y, z, intensity, confidence).
}
param {

  0.name = ~com_interface
  0.type = std_msgs/String
  0.desc = whether to use CAN or UART connection for ECHO ONE
  1.name = ~can_device
  1.type = std_msgs/String
  1.desc = CAN interface to use
  2.name = ~uart_device
  2.type = std_msgs/String
  2.desc = UART port to use
  3.name = ~loop_rate
  3.type = double
  3.desc = Spin rate of the ros node (for single shot mode)
  4.name = ~scans_topic
  4.type = std_msgs/String
  4.desc = Topic to publish point cloud to.
  5.name = ~sensor_mode
  5.type = std_msgs/String
  5.desc = Run the sensor in single-shot or continuous mode (options: [single_shot, continuous]).
  6.name = ~frame_id
  6.type = std_msgs/String
  6.desc = Base frame ID in which the data is published.
  7.name = ~target_frame
  7.type = std_msgs/String
  7.desc = Point cloud will be published with this prefix (e.g. `toposens_` + sensor ID)
  8.name = ~wait_for_transform
  8.type = double
  8.desc = Wait until transforms are available.
  9.name = ~drop_single_sensor_transform_id
  9.type = bool
  9.desc = When using single sensor the ID can be omitted in the published transform between sensor-frame and `toposens-base-link`
 10.name = ~respawn
 10.type = bool
 10.desc = Restart node again if it crashes.
 11.name = ~write_cfg_to_sensor
 11.type = bool
 11.desc = Configure the sensor at startup with values from the parameter yaml file.
 12.name = ~transducer/volume
 12.type = int
 12.desc = Transducer amplitude (percentage)
 13.name = ~transducer/num_pulses
 13.type = int
 13.desc = Electrical pulses that the piezo transmitter is stimulated with in every transmission cycle.
 14.name = ~transducer/transducer_noise_threshold
 14.type = double
 14.desc = Threshold to filter noise during signal processing on sensor.
 15.name = ~transducer/transducer_noise_ratio
 15.type = int
 15.desc = Deprecated filter on sensor to determine echo quality. Set to 100 to disable.
 16.name = ~signal_processing/temperature
 16.type = double
 16.desc = Environment temperature used for speed of sound calculations.
 17.name = ~sensor/slp_dur_pulses
 17.type = double
 17.desc = Adds sleep after each measurement in ROS node. [experimental]
 18.name = ~sensor/near_field_enabled
 18.type = bool
 18.desc = Activate the sensor's near field detection. [experimental]
 19.name = ~sensor/near_field_threshold_phase_deviations
 19.type = double
 19.desc = Parameter for near field detection. [experimental]
 20.name = ~sensor/noise_threshold
 20.type = int
 20.desc = Mark frames as noisy based on sensor noise level. [experimental]
 21.name = ~sensor/enable_auto_gain
 21.type = bool
 21.desc = Dynamically adjust signal amplification to avoid clipping or too quiet echoes.
}
```

```clearsilver
name = request_adc_dump
desc = Service to request adc dump from sensor.
param {
  0.name = sensor_id
  0.type = std_msgs/String
  0.desc = ID of the sensor to request the dump from.
  1.name = file_path
  1.type = std_msgs/String
  1.desc = File path to save the ADC dump to.
}
```
