## Description

This package will launch a Gazebo world with the AAAI LfD task
environment and a PR2 in the simulation. The environment and a PR2 will
be launched by using the following command: ```
roslaunch aaai_lfd_simulator simulation_world.launch
```
This launchfile sets two parameters which are necessary in the
simulation to make the PR2 grasp and pick up items:
```
<param name="r_gripper_controller/gripper_action_node/stall_velocity_threshold" value="0.01" type="double"/>
<param name="l_gripper_controller/gripper_action_node/stall_velocity_threshold" value="0.01" type="double"/>
```

Furthermore it contains a node to move the torso of the PR2 up to the
necessary position for the task. This node can be launched by using the
following instruction: ```
roslaunch aaai_lfd_simulator torso_up.launch
``` note: this node will be
launched automatically when following the instructions for using the
[aaai_lfd_demo](aaai_lfd_demo) in simulation.
