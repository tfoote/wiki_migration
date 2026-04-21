repository: <git://github.com/neobotix/neo_common>

this package contains a robot model of the mp 500.

## Usage/Example

### Launch a Simulation

To launch a simulation, you can type: 

```
export ROBOT=mp_500_2_1
 roslaunch neo_description_mp_500 mp_500_empty_world.launch
```



### Using the model as tf broadcaster

You can add this section to your launch file: 

```
<!--tf broadcaster-->
<param name="robot_description" command="$(find xacro)/xacro.py 
'$(find neo_description_mp_500)/ros/robot/mp_500.urdf.xacro'" />

<node pkg="robot_state_publisher" type="state_publisher"  
  name="robot_state_publisher" output="screen" >
   <param name="publish_frequency" type="double" value="50.0" />
</node>
```


