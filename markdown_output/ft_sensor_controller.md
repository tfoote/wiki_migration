## Package Summary

The ft_sensor_controller shows how to access the force/torque data
provided by netft_ethercat_hardware plugin. This controller transforms
the measured x-,y- and z-force to the \'gripper_tool_frame\' and shows
how to compensate for the inertial forces from the gripper using the
(filtered) gripper accelerations. Note that the controller assumes a
constant horizontal pose of the gripper!

## Usage

First compile the controller:

. ```
rosmake ft_sensor_controller
```

Next, be sure to run pr2_etherCAT with netft plugin. Use directions
[here](netft_ethercat_hardware/Tutorials/UsingNetFTPluginWithPR2EtherCAT).
Now you should see \'\'ft_sensor_controller/ForceInterfacePlugin\'\' in
the list when doing:

. ```
rosrun pr2_controller_manager pr2_controller_manager list-types
```

If that is the case, you can use the \'\'FT_controller.launch\'\' script
which loads the parameters and spawns the controller:

. ```
roslaunch ft_sensor_controller FT_controller.launch
```

Try viewing controller output

. ```
rxplot /FT_reader/forces/Fx_sensor:Fx_sensor_comp /FT_reader/forces/Fy_sensor:Fy_sensor_comp /FT_reader/forces/Fz_sensor:Fz_sensor_comp
```
