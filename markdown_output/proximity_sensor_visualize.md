The proximity_sensor_visualize package contains a node that visualizes
the proximity sensor in rviz. It shows a circle and a normal as an arrow
for each patch. The arrow is blue gets whiter the stronger the value of
the patch differs from the init value. After abs(value) >= init +
noise_threshold + static_threshold is true, the patch is 100% active and
the color of the circle turns from green into red.

To run the visualization you first have to start the driver

```
roslaunch proximity_sensor_driver proximity_sensor_driver.launch
``` Then you have to start the tf node for the
proximity sensor

```
roslaunch proximity_sensor_tf tf.launch
``` Now you are ready to run the visualization with

```
rosrun proximity_sensor_visualize visualize_patches
``` For those who do not want to run this manually,
the package provides a little launch file that contains all three steps
in one. You can run it via

```
roslaunch proximity_sensor_visualize proximity_sensor_bringup.launch
``` This is meant to be the standard way of
starting the proximity sensor when you have calibrated it correctly
