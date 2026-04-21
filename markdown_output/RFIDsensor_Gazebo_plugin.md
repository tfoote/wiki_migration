EOL distros:

  -- --------------------- -- -- -- --------------------------- --
     <#00FF00> Melodic            <#00FF00> (./) Released   
  -- --------------------- -- -- -- --------------------------- --

Interface for using ROS with the Gazebo simulator.

-   Maintainer status: developed
-   Maintainer\\Support: Abdussalam Alajami
    <Abdussalam.alajami@upf.edu>
-   Developers from UBICALAB, Pompeu Fabra Universitat: Abdussalam
    Alajami <Abdussalam.alajami@upf.edu>, Guillem Moreno
    <guillem.moreno01@estudiant.upf.edu>, Dr.Rafael Pous
    <rafael.pous@upf.edu>.
-   Source: git
    <https://github.com/Abdu-lybot/RFID_Sensor_Plugin_gazebo.git>
    (branch: master \--> Tested on turtlebot, branch uav_tested \-->
    tested with iris drone).

# RFID System Gazebo Plugin

**RFID System Gazebo Plugin** A design of a ROS Gazebo RFID system
plugin that enables the simulation of the RFID readers-antennas mounted
on robots reading RFID tags in the environment. The plugin is based on a
model based on probability of detection which simulates the behavior of
the complete RFID system, comprised of readers, antennas, and tags, in
the Gazebo simulation platform. It consists of a set of ROS packages
that provide the necessary interfaces to simulate the functionality of
an RFID antenna and an RFID tag in the Gazebo 3D rigid body simulator
for robots. It integrates with ROS using ROS messages, services, and
transforms.

These plugins are designed to be able to adapt and be used with any
robot simulated in the gazebo by including the models and plugins
adequately in the robot SDF/Xacro file.

This page will provide you with the necessary steps to run the plugin on
your system. ```wiki
'''IMPORTANT:''' Please install dependencies required for gazebo 9 and iris drone for the simulation to be able to work.
```

## RFID Antenna Sensor Gazebo Plugin

### Overview

The first plugin/package (RFID_antenna_plugin): Simulates the behavior
of an RFID reader/antenna. The plugin is a ros package that can be
simply compiled using catkin_make or catkin build. In real life, RFID
antennas perform two very important functions. First, they transmit
power to the RFID tags to activate them. Second, they receive data back
from the activated tags. A single antenna can activate and receive data
from multiple tags simultaneously.

Similarly, in simulation, the antenna/reader **diptera_antenna** plugin
will be able to detect tags using a probability model considering in a
simplified manner the effect of the environment on the detection of the
tag. The telecommunication parameters that govern the probability of
detection are:

### Params

```wiki
'''NOTE:''' These parameters could be changed in the SDF/Xacro file while adding the plugin.
```

-   `<Antenna_name>`: A parameter that sets the name of the antenna.
-   `<tag_name>`: A parameter that sets the name of the tag.
-   `<detected_tag_name>`: A parameter that sets the name of the
    detected tag.
-   `<detected_tag_colour>`: A parameter that sets the color of the
    detected tag.
-   `<Antenna_id>`: A parameter that gives the antenna a unique id. This
    parameter is able the reuse the same plugin by adding multiple
    antennas in the simulation Each antenna with a different id will
    function independently from the others.

```{=html}
<!-- -->
```
-   `<azimuth_beamwidth>`: Beamwidth is the angle from which the
    majority of the antenna's power, as illustrated on the radiation
    pattern's main lobe radiates. It may be measured in the horizontal
    or vertical planes and is the distance between two points where the
    power is less than half of the maximum.
    ![](https://raw.githubusercontent.com/abdu-bot/AdvanDiptera_VIO/master/rfid-antennas-beamwidth-directivity-1.png)
    This parameter represents the azimuth beam-width of the antenna.
-   `<elevation_beamwidth>`: This parameter represents the elevation
    beam-width of the antenna.
-   `<rzero>`: R0 is a parameter that represents the distance at which
    the probability distribution function = 0.5.
-   `<tag_yellow_sdf_path>`: A parameter that sets the SDF model path of
    the yellow tags to be spawned.
-   `<tag_red_sdf_path>`: A parameter that sets the SDF model path of
    the red tags to be spawned.
-   `<tag_blue_sdf_path>`: A parameter that sets the SDF model path of
    the blue tags to be spawned.
-   `<tag_purple_sdf_path>`: A parameter that sets the SDF model path of
    the purple tags to be spawned.

### TF

In order for the plugin to work the antenna frame and relative pose in
ROS must be set correctly in the **gazebo_to_ros_tf** package launch
file. ```highlight
<launch>

 	<node pkg="gazebo_to_ros_tf"
              name="world_to_ros"
              type="world_to_ros.py" output="screen">
  	</node>
	<node pkg="tf"
		type="static_transform_publisher"
		name="map_to_odom_publisher"
		args="0 0 0 0 0 0 map odom_sim 100" />
	<node pkg="tf"
		type="static_transform_publisher"
		name="base_link_to_antenna_publisher"
		args="0.12 0 -0.11 0 0 0 base_link_sim antenna_1 100" />
```

However, if you would like to use more then one RFID antenna/reader
attached to the same robot an example would be like this:

```highlight
<launch>

 	<node pkg="gazebo_to_ros_tf"
              name="world_to_ros"
              type="world_to_ros.py" output="screen">
  	</node>
	<node pkg="tf"
		type="static_transform_publisher"
		name="map1_to_odom_publisher"
		args="0 0 0 0 0 0 map odom_sim 100" />
	<node pkg="tf"
		type="static_transform_publisher"
		name="base_link_to_antenna_publisher1"
		args="0.12 0 -0.11 0 0 0 base_link_sim antenna_1 100" />
	<node pkg="tf"
		type="static_transform_publisher"
		name="base_link_to_antenna_publisher2"
		args="-0.12 0 -0.11 3.14 0 0 base_link_sim antenna_2 100" />
	<node pkg="tf"
		type="static_transform_publisher"
		name="base_link_to_antenna_publisher3"
		args="0 0.12 -0.11 1.57 0 0 base_link_sim antenna_3 100" />
	<node pkg="tf"
		type="static_transform_publisher"
		name="base_link_to_antenna_publisher4"
		args="0 -0.12 -0.11 -1.57 0 0 base_link_sim antenna_4 100" />
``` Shows that 4 antenna frames are connected to
the base_link_sim frame which represents the robot frame. An example
video of 4 antennas connected to an aerial robot is shown at the end of
this page.

```wiki
'''assign the relative position/pose of the antenna carefully with the robot, it should be set the same way the antenna model is positioned in the gazebo'''

Admonitions should be used with care. A page riddled with admonitions will look restless and will be harder to follow than a page where admonitions are used sparingly.
```

## RFID Tag Sensor Gazebo Plugin

### Overview

The second plugin (RFID_tag_plugin): Contains the plugin that simulates
RFID tags that are usually attached to a product/box called a
"fixture" This plugin/package is compiled using catkin_make or catkin
build. In real life, RFID Tags are small objects that contain a small
antenna. Similarly, in simulation, the plugin does two major tasks.
First, it reads a file called **map.txt** which exists in the plugin
folder that contains in each line information of the fixtures (boxes
that contain tags) in this order:

1.  fix_name id x y z, which are the fixture name, id, and coordinates
    according to the world map. Secondly, it will spawn a pre-set number
    of tags in each box in gazebo. The parameters that could be changed
    in this plugin are:

### Params

```wiki
'''NOTE:''' These parameters could be changed in the SDF/Xacro file while adding the plugin.
```

-   `<tag_name>`: A parameter that sets the name of the tag.
-   `<tags_per_fix>`: which sets the number of tags spawned in each
    box/fixture.
-   `<parent_frame>`: A parameter that sets the world/robot frame you
    desire the tag frames to be attached to.
-   `<fix_sdf_path>`: A parameter that sets the SDF model path of the
    box or fixtures to be spawned.
-   `<tag_sdf_path>`: A parameter that sets the SDF model path of the
    tags to be spawned.

### TF

Unlike the antenna plugin, no further adjustments are needed as the
plugin will generate a frame for each tag with a relative pose. The
below image shows the transform tree of 3 tags:
<attachment:rqt_3tags.png>

## HOW TO USE?

### First Step

Setting up your ROS source folder: Clone the packages **gazebo_to_ros_tf
gazebo** & **RFID_antenna_plugin** & **RFID_tag_plugin** to your source
folder **catkin_ws/src** ```highlight
git clone https://github.com/Abdu-lybot/RFID_Sensor_Plugin_gazebo.git
```

### Second Step

Compile your workspace: From the location of your workspace folder
**catkin_ws** ```highlight
catkin_make
```

### Third Step

Adding to your bashrc the path of your plugin: ```highlight
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:/home/<USER>/catkin_ws/src/RFID_tag_plugin/cmake-build-debug/devel/lib
export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:/home/<USER>/catkin_ws/src/RFID_antenna_plugin/cmake-build-debug/devel/lib
```

### Fourth Step

add the **RFID_antenna** & **RFID_tag** plugins to your robot model
Xacro/SDF file or any other: For adding the plugins: Adding the Plugin
to your model: ```highlight
!--for the RFID_tags plugin:-->
  <gazebo reference="base_link">
     <sensor type="rfid" name="rfid_tags">
       <plugin name="rfid_tags" filename="libRFID_tag_plugin.so">
	 <tag_name>rfid_tag</tag_name>
	 <parent_frame>odom_sim</parent_frame>
	 <tags_per_fix>5</tags_per_fix>
	 <fix_sdf_path>/home/<USER>/catkin_ws/src/RFID_antenna_plugin/Models/normal_size_fixture/model.sdf</fix_sdf_path>
	 <tag_sdf_path>/home/<USER>/catkin_ws/src/RFID_antenna_plugin/Models/RFID_1/model.sdf</tag_sdf_path>
       </plugin>
     </sensor>
  </gazebo>
``` For the RFID_antenna plugin:
Adding the Plugin and the Graphical Antenna Model to Gazebo:
```wiki
'''NOTE:''' These parameters could be changed in the SDF/Xacro file while adding the plugin.
```0

### Published topics-msgs

-   `</detected_tags >`: The detected tags information will be published
    in this topic with the message PoseStamped geometric messages. This
    message contains:
-   `<frame_id>`: this parameter contains the name and id of the
    detected tag.
-   `<stamp>`: Contains the time stamp of when it was detected.
-   `<position.x>`: Contains the position of the detected tag relative
    to x-axis of the world.
-   `<position.y>`: Contains the position of the detected tag relative
    to y-axis of the world.
-   `<position.z>`: Contains the position of the detected tag relative
    to z-axis of the world.

### Finnaly

Run your gazebo simulation, then run the tf tree node:
```wiki
'''NOTE:''' These parameters could be changed in the SDF/Xacro file while adding the plugin.
```1

### Video Example

A video of a UAV equipped with 4 RFID antennas in an environment
containing 1000 RFID tags, while only having the attached antenna facing
the right side of the UAV active.
[target="UAV equipped with 4 RFID antennas in an environment of 1000 RFID tags"](https://www.youtube.com/watch?v=xMaFSDsqnAc site)

------------------------------------------------------------------------

CategoryCategory
