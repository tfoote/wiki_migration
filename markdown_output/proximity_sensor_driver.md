The proximity_sensor_driver communicates over a SUB20 with the
controller box of the proximity sensor. The driver takes some arguments
that can be configured in the *sensor_config.yaml:*

**sensor_count** the number of patches that are in the proximity sensor
chain

**noise_threshold **Patches with a value in the range of this parameter
to init are considered as inactive

**static_threshold **Patches with a reading over the range of
noise_threshold but within static_threshold are considered as
(abs(init - reading) - noise_threshold) / static_threshold % active.

**dynamic_threshold **Not used yet

After you have configured the driver you can launch it with

```
roslaunch proximity_sensor_driver proximity_sensor_driver.launch
```
