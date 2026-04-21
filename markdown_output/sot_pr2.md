This package can be used to control the PR-2 using dynamic-graph both in
simulation and on the robot.

## Running the simulation with PR2 in Gazebo

1\. Edit the `sot_pr2.yaml` to add your own Python path. A cleaner way
should be implemented to replace this temporary mechanism. In this file
you can also switch between position/force control.

2\. Run the following commands:



```shell
# Launch gazebo simulation.
roslaunch gazebo_worlds empty_world.launch
# Spawn a PR-2 robot in gazebo.
roslaunch pr2_gazebo pr2.launch
# Load and start the sot_pr2 controller.
roslaunch sot_pr2 sot_pr2.launch

# List available controllers
# You should see sot_pr2/SotPr2Plugin in the list. If this is not the case,
# the plug-in cannot be found (did you compile sot_pr2 package? is it in your
# ROS_PACKAGE_PATH?).
rosrun pr2_controller_manager pr2_controller_manager list-types

# Manage the controller using the remote client.
rosrun dynamic_graph_bridge run_command
```


