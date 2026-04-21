Each pr2 gripper is equipped with two pressure-sensitive fingertips.
Each pressure comprises 22 pressure sensing elements: one on the back, 6
around the edges and a 3x5 array on the front. \`fingertip_pressure\`
provides nodes to facilitate the visualization and interpretation of the
fingertip pressure sensor data.

## Stability

This package has not been reviewed so the API documented below should be
considered unstable. Also, this package has not been user-tested, so
there may be usability issues with the nodes.

## ROS API

Overview of how the nodes interact with the robot sensor stream:
[ {{attachment:overview.gif}}](attachment:overview.gif )

**Note**: All nodes assume that \`\<gripper_motor_name\>\` is either
\`r_gripper_motor\` or \`l_gripper_motor\`.

```clearsilver
node.0 {
name=sensor_info
desc=Publishes sensor geometry, tf frame and unit scaling information.
pub{
 0.name= /pressure/<gripper_motor_name>_info
 0.type= fingertip_pressure/PressureInfo
 0.desc= For each sensor, the tf frame is specified, and for each pressure sensing element, a scaling factor to Newtons, and rectangular geometry approximation are provided.
}
}
node.1 {
name=view_fingertip_pressure
desc=RX visualization panel to show the fingertip pressure information. Allows conversion to N or kPa units and zero-offset removal.
sub{
 0.name= board
 0.type= pr2_msgs/PressureState
 0.desc= Raw data from the pressure sensor. If board is not remapped, it will be automatically remapped to pressure/r_gripper_motor. (For versions prior to and including 1.0.3, the source was always pressure/r_gripper_motor.)
 1.name= <board>_info
 1.type= fingertip_pressure/PressureInfo
 1.desc= Sensor calibration, geometry and tf frame.
}
}
``` Example of \`view_fingertip_pressure\` GUI:

[ {{attachment:fingertip_sensors_panel.png}}](attachment:fingertip_sensors_panel.png)
```clearsilver
node.2 {
name=sphere_viz
desc=Provide visualization markers of the fingertip pressure data.
sub{
 0.name= /pressure/<gripper_motor_name>
 0.type= pr2_msgs/PressureState
 0.desc= Raw data from the pressure sensor
 1.name= /pressure/<gripper_motor_name>_info
 1.type= fingertip_pressure/PressureInfo
 1.desc= Sensor calibration, geometry and tf frame.
}
pub{
 0.name= "/visualization_marker"
 0.type= visualization_msgs/Marker
 0.desc= Graphical objects to be displayed.
}
}
node.3 {
name=rectangle_viz
desc=Provide visualization markers of the fingertip pressure data.  A more limited form of `sphere_viz` that allows the geometry of the sensor output to be checked.
sub{
 0.name= /pressure/<gripper_motor_name>
 0.type= pr2_msgs/PressureState
 0.desc= Raw data from the pressure sensor
 1.name= /pressure/<gripper_motor_name>_info
 1.type= fingertip_pressure/PressureInfo
 1.desc= Sensor calibration, geometry and tf frame.
}
pub{
 0.name= "/visualization_marker"
 0.type= visualization_msgs/Marker
 0.desc= Graphical objects to be displayed.
}
}
node.4 {
name=sim_sensor
desc=Allows the fingertip_pressure package to be tested without actual hardware by providing a raw sensor data feed.
pub{
 0.name= /pressure/<gripper_motor_name>
 0.type= pr2_msgs/PressureState
 0.desc= Simulated pressure sensor data.
}
}
```

### Launch files

\`launch/fingertip_demo.launch\` is a standalone demo of the package\'s
capabilities. It runs all the package\'s nodes, and rviz (to view the
visualization markers). This should demonstrate all the packages
capabilities.

Example: ```
$ roslaunch launch/fingertip_demo.launch
``` and in a separate shell:
```
$ roscd pr2_gazebo
$ roslaunch pr2_empty.launch
```
