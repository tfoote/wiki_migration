repository: <git://github.com/neobotix/neo_common>

this package contains a robot model of the mpo 500.

## Usage/Example

### Launch a Simulation

To launch a simulation, you can type: ```
export ROBOT=mpo_500_1_0
 roslaunch neo_description_mpo_500 mpo_500_empty_world.launch
```

### Using the model as tf broadcaster

You can add this section to your launch file: ```
<!--tf broadcaster-->
<param name="robot_description" command="$(find xacro)/xacro.py 
'$(find neo_description_mpo_500)/ros/robot/mpo_500.urdf.xacro'" />

<node pkg="robot_state_publisher" type="state_publisher" name="robot_state_publisher" output="screen" >
      <param name="publish_frequency" type="double" value="100.0" />
</node>
```
