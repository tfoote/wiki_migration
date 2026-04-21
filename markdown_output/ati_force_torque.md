The ati_force_torque package provides a ROS interface for an ATI
force/torque sensor that is connected over CAN-bus. Most important
features of this package are:

1\. 2 ROS Nodes one for configuration and one for reading of sensor. 1.
Implemenation of
[hardware_interface::ForceTorqueSensorHandle](http://docs.ros.org/hydro/api/hardware_interface/html/c++/classhardware__interface_1_1ForceTorqueSensorHandle.html)
for using sensor in [ros_control](ros_control). 1. Sampling the sensor
on ca. 800 Hz and downsample to desied freqency 1. Automatic calibration
of sensor upon start. 1. Definition of static calibration offsets. 1.
Integration of filters: ThresholdFilter, LowPassFilter, MovingMeanFilter
and GravityCompensation.

This package is builds upon the original
[cob_forcetorque](http://wiki.ros.org/action/fullsearch/cob_forcetorque?action=fullsearch&context=180&value=linkto:"cob_forcetorque")
written in 2011 and not updated since than.For can interfacing the CAN
devices [cob_generic_can](cob_generic_can) pakcage is used.

## Installing the package

To use this package you should have
[ROS up and running](ROS/Tutorials/InstallingandConfiguringROSEnvironment).
To install the package clone the
[git repository](https://github.com/iirob/ati_force_torque) into *src*
folder of your workspace.

**Note**: Current version of the package depends on
[iirob_filters](https://github.com/iirob/iirob_filters) package for
filtering capabilities. To install this package clone the
[git repository](https://github.com/iirob/iirob_filters) into *src*
folder of your workspace

## Starting the nodes

There are few launch files provided to start the sensor, configure it of
get data from it.

config.launch - starts configuration node for sensor and uses
configuration from can_ati_config.yaml.

driver.launch - start sensor node on socket or chardev interface loading
the sensor description and starting the state publisher.

driver_socket.launch and driver_chardev.launch - start the node loading
the corresponding configuration.

## Nodes

```clearsilver
name = ati_force_torque_config
desc = Changes configuration data of the sensor like baudrate and base-id.
srv {
  0.name = SetBaudRate
  0.type = std_srvs/Trigger
  0.desc = Sets baudrate to the sensor from 'future_baudrate' parameter.
  1.name = SetBaseIdentifier
  1.type = std_srvs/Trigger
  1.desc = Sets base identifier of the sensor from 'future_base_id' parameter.
  2.name = Reset
  2.type = std_srvs/Trigger
  2.desc = Resets the sensor calling the reset function of sensors electronics.
}
param {
  0.name = ~CAN/type
  0.type = UInt
  0.desc = Type of used CAN Interface. Possible values are 1-5 for further details check cob_generic_can package.
  0.default = -1
  1.name = ~CAN/path
  1.type = String
  1.desc = Path to the CAN device. If you are using char device value is e.g. '/dev/canXX' or if you are using socket device value is e.g. 'can0'.
  1.default = ""
  2.name = ~CAN/baudrate
  2.type = HEX-Number
  2.desc = Baudrate of used CAN Interface. Possible values are 0x0-0xD. For further details check cob_generic_can package.
  2.default = -1
  3.name = ~FTS/base_identifier
  3.type = HEX-Number
  3.desc = Base identifier of sensor. For more details see sensor manual.
  3.default = -1
  4.name = ~FTS/future_baudrate
  4.type = UInt
  4.desc = Baudrate value on which you want to set up the sensor. For meaning of this value see sensor manual.
  4.default = 7
  5.name = ~FTS/future_base_id
  5.type = HEX-Number
  5.desc = Base identifier on which you want to set up the sensor. For meaning of this value see sensor manual.
  5.default = 7
}
``` ```clearsilver
name = ati_force_torque_node
desc = ROS-Node for reading sensor data. Data can be filtered and transformed automatically. The same description is valid for sensor handle used in ros_control.
sub {
  0.name = ~gravity_compensated
  0.type = geometry_msgs/WrenchStamped
  0.desc = Publish output of GravityCompensation filter (if enabled with parameter)
  1.name = ~low_pass
  1.type = geometry_msgs/WrenchStamped
  1.desc = Publish output of LowPass filter (if enabled with parameter)
  2.name = ~sensor_data
  2.type = geometry_msgs/WrenchStamped
  2.desc = Publish output of the sensor (if enabled with parameter)
  3.name = ~threshold_filtered
  3.type = geometry_msgs/WrenchStamped
  3.desc = Publish output of the Threshold filter (if enabled with parameter)
  4.name = ~transformed_data
  4.type = geometry_msgs/WrenchStamped
  4.desc = Publish output of the transformed and filtered sensor data (if enabled with parameter)
}
srv {
  0.name = Init
  0.type = std_srvs/Trigger
  0.desc = Initalised communication with the sensor and after that data are constantly published.
  1.name = Calibrate
  1.type = std_srvs/Trigger
  1.desc = Start automatic calibration procedure.
  2.name = DetermineCoordinateSystem
  2.type = std_srvs/Trigger
  2.desc = Start procedure for calculating current directio of the force. This is usefull to empirically determine transformation of the sensor in respect to sensor reference frame.
  3.name = GetTemperature
  3.type = ati_force_torque/DiagnosticVoltages
  3.desc = Return diagnostic voltages from the sensor electronics. For further detail see sensor manual.
  4.name = Recalibrate
  4.type = std_srvs/Trigger
  4.desc = Recalibrates the sensor in respect to the tool mounted on the sensor tool link.
}
param {
  0.name = ~CAN/type
  0.type = UInt
  0.desc = Type of used CAN Interface. Possible values are 1-5 for further details check cob_generic_can package.
  0.default = -1
  1.name = ~CAN/path
  1.type = String
  1.desc = Path to the CAN device. If you are using char device value is e.g. '/dev/canXX' or if you are using socket device value is e.g. 'can0'.
  1.default = ""
  2.name = ~CAN/baudrate
  2.type = HEX-Number
  2.desc = Baudrate of used CAN Interface. Possible values are 0x0-0xD. For further details check cob_generic_can package.
  2.default = -1
  3.name = ~FTS/base_identifier
  3.type = HEX-Number
  3.desc = Base identifier of sensor. For more details see sensor manual.
  3.default = -1
  4.name = ~FTS/auto_init
  4.type = Bool
  4.desc = Auto-initialisation of the sensor.
  4.default = False
  5.name = ~Node/ft_pub_freq
  5.type = Double
  5.desc = Publishing frequency of sensor data
  5.default = 100
  6.name = ~Node/ft_pull_freq
  6.type = Double
  6.desc = Frequency of pulling sensor data (currently maximal achieved value is ca. 800 Hz)
  6.default = 100
  7.name = ~Node/sensor_frame
  7.type = String
  7.desc = Sensor measurement frame (usually: "fts_reference_link")
  7.default = "fts_reference_link"
  8.name = ~Node/transform_frame
  8.type = String
  8.desc = Frame in which output data should be transoformed.
  8.default = "fts_base_link"
  9.name = ~Calibration/n_measurements
  9.type = Int
  9.desc = Number of measurements for automatic calibration.
  8.default = 20
  10.name = ~Calibration/T_between_meas
  10.type = Int
  10.desc = Number of micro-second to sleep between mesaurements during automatic calibration.
  10.default = 10000
  11.name = ~Calibration/static
  11.type = Bool
  11.desc = If true static calibration is used.
  11.default = False
  12.name = ~Calibration/offset_fx
  12.type = Double
  12.desc = Force offset in X-axis (static calibration).
  12.default = 0
  13.name = ~Calibration/offset_fy
  13.type = Double
  13.desc = Force offset in Y-axis (static calibration).
  13.default = 0
  14.name = ~Calibration/offset_fz
  14.type = Double
  14.desc = Force offset in Z-axis (static calibration).
  14.default = 0
  15.name = ~Calibration/offset_mx
  15.type = Double
  15.desc = Torque offset in X-axis (static calibration).
  15.default = 0
  16.name = ~Calibration/offset_my
  16.type = Double
  16.desc = Torque offset in Y-axis (static calibration).
  16.default = 0
  17.name = ~Calibration/offset_mz
  17.type = Double
  17.desc = Torque offset in Z-axis (static calibration).
  17.default = 0
  18.name = ~CoordinateSystemCal/n_measurements
  18.type = Int
  18.desc = Number of measurements for automatic calculation of coordinate system transformation.
  18.default = 20
  19.name = ~CoordinateSystemCal/T_between_meas
  19.type = Int
  19.desc = Number of micro-second to sleep between mesaurements during automatic calculation of coordinate system transformation.
  19.default = 10000
  20.name = ~CoordinateSystemCal/push_direction
  20.type = Int
  20.desc = Positive or negative force direction for automatic calculation of coordinate systems.
  20.default = 0
  21.name = ~Publish/gravity_compensated
  21.type = Bool
  21.desc = Publish output data from GravityCompensation filter.
  21.default = False
  22.name = ~Publish/low_pass
  22.type = Bool
  22.desc = Publish output data from LowPass filter.
  22.default = False
  23.name = ~Publish/sensor_data
  23.type = Bool
  23.desc = Publish output of the sensor.
  23.default = False
  24.name = ~Publish/threshold_filtered
  24.type = Bool
  24.desc = Publish output data from Threshold filter.
  24.default = False
  25.name = ~Publish/transformed_data
  25.type = Bool
  25.desc = Publish transformed data.
  25.default = False
}
```

There are few other paramters used for parametrisation of filters.
Please check sensor_configuration.yaml to see them.

## Issues

<<GitHubIssues(iirob/ati_force_torque)>>
