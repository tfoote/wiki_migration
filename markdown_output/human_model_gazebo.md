This package provides human model as a detection target for
[Tsukuba Challenge (Japanese Page)](http://www.tsukubachallenge.jp/).

An example of using the packages can be seen in
[Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03).

## Usage

This script can delay the launch of a roslaunch file.

### Spawn it in launch file

example:

```
<launch>
  <param name="human_description1"
      command="$(find xacro)/xacro.py '$(find human_model_gazebo)/urdf/human.xacro'" />
  <node name="urdf_spawner_human1" pkg="gazebo_ros" type="spawn_model" respawn="false" output="screen"
	args="-urdf -model human1 -param human_description1 -x 7.2 -y 0.49 -z 0.34 -R 0 -P 0 -Y -3.05"/>
</launch>
```

Specify a point of spawning the model in Gazebo coordinate.

### View a human model

```
roslaunch human_model_gazebo view_human.launch
```

![human_model_gazebo1\|width=\"500\"](attachment:human_model_gazebo1.png)

![human_model_gazebo2\|width=\"500\"](attachment:human_model_gazebo2.png)
