The proximity_sensor_fake_data contains a node that produces some random
proximity sensor data. This can be useful for debugging purposes. It
provides also the callback for the reinitialization service. The
callback does nothing but printing out that it has been called.

The launch file loads the *sensor_config.yaml *configuration file into
the ROS environment.

To produce some random proximity sensor data you have to run

```
roslaunch proximity_sensor_fake_data fake_sensor_data.launch
```
