repository: <git://github.com/neobotix/neo_common>

this package contains a robot model of the mpo 700.

## Usage/Example

### Launch a Simulation

To launch a simulation, you can type: 

```
export ROBOT=mpo_700_3_5
 roslaunch neo_description_mpo_700 mpo_700_empty_world.launch
```



### Using the model as tf broadcaster

You can add this section to your launch file: 

```
<param name="robot_description" command="$(find xacro)/xacro.py 
'$(find neo_description_mpo_700)/urdf/robot.urdf.xacro'" />

<node pkg="robot_state_publisher" type="state_publisher" name="robot_state_publisher"/>
```


