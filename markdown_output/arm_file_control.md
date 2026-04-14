## Description

Provides three nodes to help with trouble shooting and data collection
for the learning from demonstration challenge

The first records data for given joint positions. Currently the node
records the arms wrist_roll_link. The desired file location can be
provided via the parameter server under the parameter
aaai_arm_file_recorder. The desired arm is also specified through the
parameter server aaai_arm_file_arm_desired.

This can be run using the following command:
` rosrun arm_file_control arm_listener.py `

The second takes a set of positions and moves the arm to the desired
position. It is assumed that the points are for the wrist_roll_link and
with the base frame set to the torso_lift_link frame. The file location
can be specified via the parameter server with the aaai_arm_file_reader
parameter. arm_file_teleop_reader.launch file can be used to set this as
long as you edit the file to point to the location of your data file.

This node can be run with the following command:
` rosrun arm_file_control arm_teleop_reader.py `

The third takes a set of waypoints and has the arm move to the desired
position. Once again, it is assumed that the points are for the
wrist_roll_link and with the base frame set to the torso_lift_link
frame. The file location can be specified via the parameter server with
the aaai_arm_file_reader parameter.

This node can be run with the following command:
` rosrun arm_file_control arm_reader.py `

An example file can be found in the scripts folder of the
arm_file_control package.

Troubleshooting: if you are running the arm_reader.py after running the
arm_teleop_reader.py and the arms are not moving you should use the
[pr2_controller_manager](pr2_controller_manager) to stop the r_cart and
l_cart controllers and start the r_arm_controller and l_arm_controller
controllers. The provided launch files allow you to avoid having to do
this.
