## PR2 Plugins

This package contains dynamic plugins for [Gazebo](gazebo) and
[ROS](ROS) integration with simulated hardware.

- Plugin-Supported Hardware:
- [pr2_etherCAT](pr2_etherCAT)/[PR2 Controller Manager](https://index.ros.org/p/pr2_controller_manager):
  provided by `GazeboRosControllerManager`.
- [Prosilica Camera](https://index.ros.org/p/prosilica_camera): provided
  by `GazeboRosProsilica`.
- [Battery Power Monitor](https://index.ros.org/p/power_monitor):
  provided by `GazeboRosPowerMonitor`.
- Unsupported Features:
- [Power Board Driver](https://index.ros.org/p/pr2_power_drivers)

Please see [gazebo_plugins](https://index.ros.org/p/gazebo_plugins) for
additional supported hardware components in simulation.

## Gazebo XML Plugin Configuration

### gazebo_ros_controller_manager

#### Parameters

`<robotParam>` (string, default: "robot_description") Name of ROS
parameter where robot description is stored. `<robotNamespace>`
(string, default: "/") Robot namespace.

#### Example



```
<!-- GazeboMechanismControl -->
    <controller:gazebo_ros_controller_manager name="gazebo_ros_controller_manager" plugin="libgazebo_ros_controller_manager.so">
      <alwaysOn>true</alwaysOn>
      <updateRate>1000.0</updateRate>
      <robotParam>robot_description</robotParam>
      <robotNamespace>/</robotNamespace>
    </controller:gazebo_ros_controller_manager>
```



### gazebo_ros_prosilica

`GazeboRosProsilica` plugin provides ROS topic and service interfaces
similar to those provided by the
[Prosilica Camera hardware](https://index.ros.org/p/prosilica_camera) on
PR2.

#### Parameters

`<robotNamespace>` (string, default: "/") Robot namespace.
`<imageTopicName>` (string, default: "image_raw") ROS topic name
for publishing image. `<cameraInfoTopicName>` (string, default:
"camera_info") ROS topic name for publishing camera info.
`<pollServiceName>` (string, default: "request_image") ROS service
name for polling. `<frameName>` (string, default: "") Frame name
of camera. `<CxPrime>` (integer, default: 320) !CxPrime `<Cx>`
(integer, default: 320) Cx `<Cy>` (integer, default: 240) Cy
`<focal_length>` (double, default: 554.256) image_width(px) /
(2\*tan( hfov(radian) /2)) `<distortion_k1>` (double, default: 0)
Distortion k1 value. `<distortion_k2>` (double, default: 0)
Distortion k2 value. `<distortion_k3>` (double, default: 0)
Distortion k3 value. `<distortion_t1>` (double, default: 0)
Distortion t1 value. `<distortion_t2>` (double, default: 0)
Distortion t2 value. `<hackBaseline>` (double, default: 0) Hack for
right stereo camera

#### Example



```
<body:empty name="camera_body_name">
    <sensor:camera name="high_def_sensor">
      <imageFormat>R8G8B8</imageFormat>
      <imageSize>2448 2050</imageSize>
      <hfov>45</hfov>
      <nearClip>0.1</nearClip>
      <farClip>100</farClip>
      <updateRate>20.0</updateRate>
      <controller:gazebo_ros_prosilica name="high_def_controller" plugin="libgazebo_ros_prosilica.so">
        <alwaysOn>true</alwaysOn>
        <updateRate>20.0</updateRate>
        <imageTopicName>/prosilica/image_raw</imageTopicName>
        <cameraInfoTopicName>/prosilica/camera_info</cameraInfoTopicName>
        <pollServiceName>/prosilica/request_image</pollServiceName>
        <frameName>high_def_frame</frameName>
        <CxPrime>1224.5</CxPrime>
        <Cx>1224.5</Cx>
        <Cy>1025.5</Cy>
        <focal_length>2955</focal_length> <!-- image_width / (2*tan(hfov_radian /2)) -->
        <distortion_k1>0.00000001</distortion_k1>
        <distortion_k2>0.00000001</distortion_k2>
        <distortion_k3>0.00000001</distortion_k3>
        <distortion_t1>0.00000001</distortion_t1>
        <distortion_t2>0.00000001</distortion_t2>
        <interface:camera name="high_def_iface"/>
      </controller:gazebo_ros_prosilica>
    </sensor:camera>
  </body:empty>
```



### gazebo_ros_power_node

`GazeboRosPowerNode` plugin provides ROS topics and services similar
to those provided by
[PR2 power monitor node](https://index.ros.org/p/power_monitor) on
physical PR2.

#### Parameters

`<robotNamespace>` (string, default: "/") Robot namespace
`<powerStateTopic>` (string, default: "power_state") Topic to
subscribe to power state on `<powerStateRate>` (double, default:
1.0) Power state rate. `<fullChargeCapacity>` (double, default:
80.0) Full charge capacity `<chargeRate>` (double, default: 500.0)
Charge rate `<dischargeVoltage>` (double, default: 16.0) Discharge
voltate `<dischargeRate>` (double, default: -500.0) Discharge rate
`<chargeVoltage>` (double, default: 16.0) Charge voltage.

#### Example



```
<controller:gazebo_ros_power_monitor name="gazebo_ros_power_monitor_controller" plugin="libgazebo_ros_power_monitor.so">
        <alwaysOn>true</alwaysOn>
        <updateRate>1.0</updateRate>
        <timeout>5</timeout>
        <interface:audio name="power_monitor_dummy_interface" />
        <powerStateTopic>power_state</powerStateTopic>
        <powerStateRate>10.0</powerStateRate>
        <fullChargeCapacity>87.78</fullChargeCapacity>
        <dischargeRate>-474</dischargeRate>
        <chargeRate>525</chargeRate>
        <dischargeVoltage>15.52</dischargeVoltage>
        <chargeVoltage>16.41</chargeVoltage>
    </controller:gazebo_ros_power_monitor>
```



## ROS API

### gazebo_ros_power_node

Gazebo plugin for simulating the PR2 power monitor.

#### Subscribed Topics

- `plugged_in`
  ([pr2_gazebo_plugins/msg/PlugCommand](https://docs.ros.org/en/rolling/p/pr2_gazebo_plugins/msg/PlugCommand.html)):
  plugged in state

#### Published Topics

- `<powerStateTopic>`
  ([pr2_msgs/msg/PowerState](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/PowerState.html)):
  simulated power state

### gazebo_ros_prosilica_node

Gazebo plugin for simulating the prosilica camera. This follows the
standard ROS API for camera drivers.

#### Published Topics

- `<imageTopicName>`
  ([sensor_msgs/msg/Image](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/Image.html)):
  Camera image
- `<cameraInfoTopicName>`
  ([sensor_msgs/msg/CameraInfo](https://docs.ros.org/en/rolling/p/sensor_msgs/msg/CameraInfo.html)):
  Camera info

#### Services

- `request_image`
  ([polled_camera/srv/GetPolledImage](https://docs.ros.org/en/rolling/p/polled_camera/srv/GetPolledImage.html)):
  **(Polled Mode Only)** Captures an image and publishes it in the
  namespace specified by the request message. Returns the timestamp.

### gazebo_ros_controller_manager

`GazeboRosControllerManager` plugin provides similar ROS interface as
[pr2_etherCAT](pr2_etherCAT) on the physical PR2 robot. This plugin is
written in a way that
[PR2 controller manager](https://index.ros.org/p/pr2_controller_manager)
works transparently with either this simulated plugin or the
[pr2_etherCAT](pr2_etherCAT) hardware. For more information on using
[generic controllers](https://index.ros.org/p/robot_mechanism_controllers)
or
[PR2 specific controllers](http://ros.org/wiki/pr2_mechanism_controllers)
with this plugin, please see
[pr2_controller_manager](https://index.ros.org/p/pr2_controller_manager).

## Tutorials

- [Adding a GazeboRosForce gazebo ros plugin to a simulated object](#adding-a-gazeborosforce-gazebo-ros-plugin-to-a-simulated-object):
  \## the next tutorial description (optional)
- [Attaching a ROS Ground Truth Pose Broadcaster to Objects in Simulation](#attaching-a-ros-ground-truth-pose-broadcaster-to-objects-in-simulation):
  Attaching a ROS ground truth pose broadcaster to objects in simulation

## Roadmap

This stack will be updated with new features as the PR2 hardware itself
is updated. Future versions will also incorporate
[dynamic_reconfigure](https://index.ros.org/p/dynamic_reconfigure)
options to match ORS driver functionality.

## Adding a GazeboRosForce gazebo ros plugin to a simulated object

- **Note:** Adding a GazeboRosForce gazebo ros plugin to a simulated
  object.
- **Keywords:** gazebo plugins GazeboRosForce

### GazeboRosForce Example

#### Create a Simple Box URDF using the GazeboRosForce plugin

Create an URDF for an object and save it as object.urdf:


```
<?xml version="1.0" ?>
<robot name="single_joint">
  <gazebo reference="base">
    <material>Gazebo/GrassFloor</material>
  </gazebo>
  <link name="world"/>
  <joint name="link_joint" type="continuous">
    <axis xyz="0 0 1"/>
    <parent link="world"/>
    <origin rpy="0 0 0" xyz="0 0 1"/>
    <child link="link"/>
    <limit effort="100" velocity="100" k_velocity="0" />
    <joint_properties damping="0.1" friction="1.0" />
  </joint>
  <link name="link">
    <inertial>
      <mass value="10"/>
      <origin xyz="0 0 0"/>
      <inertia ixx="1.0" ixy="0.0" ixz="0.0" iyy="0.1" iyz="0.0" izz="0.1"/>
    </inertial>
    <visual>
      <origin rpy="0 0 1" xyz="0 0 0"/>
      <geometry>
        <box size="0.2 1.0 0.2"/>
      </geometry>
    </visual>
    <collision>
      <origin rpy="0 0 1" xyz="0 0 0"/>
      <geometry>
        <box size="0.2 1.0 0.2"/>
      </geometry>
    </collision>
  </link>
  <gazebo reference="link">
    <material>Gazebo/GrassFloor</material>
    <turnGravityOff>true</turnGravityOff>
  </gazebo>
  
   <gazebo>
    <controller:gazebo_ros_force name="gazebo_ros_force" plugin="libgazebo_ros_force.so">
      <alwaysOn>true</alwaysOn>
      <update>100</update>
      <updateRate>100.0</updateRate>
      <bodyName>link</bodyName>
      <topicName>force</topicName>
    </controller:gazebo_ros_force>
  </gazebo>
</robot>
```



#### Spawn Model in Simulation

Start an empty world simulation 

```
rosmake gazebo_worlds
roslaunch gazebo_worlds empty_world.launch
```

 To spawn above
URDF 

```
rosrun gazebo spawn_model -file object.urdf -urdf -z 1 -model my_object
```

 You will see the /force topic listed with


```
rostopic list
```

 You can applaiy a torque


```
rostopic pub /force geometry_msgs/Wrench  '{force:  {x: 0.0, y: 0.0, z: 0.0}, torque: {x: 0.0,y: 0.0,z: 0.6}}'
```

 You should see the box rotating

## Attaching a ROS Ground Truth Pose Broadcaster to Objects in Simulation

- **Note:** This tutorial assumes that you have completed the previous
  tutorials:
  [Spawn simple URDF object in simulation](simulator_gazebo/Tutorials/SpawningObjectInSimulation).
- **Description:** Attaching a ROS ground truth pose broadcaster to
  objects in simulation



```wiki
Users are highly discouraged from using the documentation and tutorials for Gazebo on this page. Gazebo is now a stand alone project at [[http://gazebosim.org|gazebosim.org]]. See documentation there, thanks!
```



### Attaching a Ground Truth Plugin

1\. Update the URDF from
[this tutorial](simulator_gazebo/Tutorials/SpawningObjectInSimulation)
by adding a Gazebo extension for **ros_p3d** plugin:


```text
<?xml version="1.0"?>
<robot xmlns:controller="http://playerstage.sourceforge.net/gazebo/xmlschema/#controller" name="simple_box">
  <gazebo>
    <controller:ros_p3d name="my_box_controller" plugin="libros_p3d.so">
      <alwaysOn>true</alwaysOn>
      <updateRate>100.0</updateRate>
      <bodyName>my_box</bodyName>
      <topicName>my_box_pose_ground_truth</topicName>
      <gaussianNoise>0.0</gaussianNoise>
      <frameName>my_box</frameName>
      <interface:position name="my_box_p3d_position_iface" />
    </controller:ros_p3d>
  </gazebo>

  <joint name="my_box_joint" type="revolute" >
    <!-- axis is in the parent link frame coordintates -->
    <axis xyz="0 1 0" />
    <parent link="world" />
    <child link="my_box" />
    <!-- initial pose of my_box joint/link in the parent frame coordiantes -->
    <origin xyz="0 0 2" rpy="0 0 0" />
  </joint>
  <link name="my_box">
    <inertial>
      <mass value="1.0" />
      <!-- center of mass (com) is defined w.r.t. link local coordinate system -->
      <origin xyz="1 0 0" /> 
      <inertia  ixx="1.0" ixy="0.0"  ixz="0.0"  iyy="100.0"  iyz="0.0"  izz="1.0" />
    </inertial>
    <visual>
      <!-- visual origin is defined w.r.t. link local coordinate system -->
      <origin xyz="1 0 0" rpy="0 0 0" />
      <geometry name="my_box_visual_geom">
        <box size="0.05 0.05 0.10" />
      </geometry>
    </visual>
    <collision>
      <!-- collision origin is defined w.r.t. link local coordinate system -->
      <origin xyz="1 0 0" rpy="0 0 0 " />
      <geometry name="my_box_collision_geom">
        <box size="0.05 0.05 0.10" />
      </geometry>
    </collision>
  </link>
  <gazebo reference="my_box">
    <material>Gazebo/Blue</material>
    <turnGravityOff>false</turnGravityOff>
  </gazebo>
</robot>
```



The additional Gazebo extension block below: instantiates a `ros_p3d`
plugin that broadcasts a `geometry_msgs/Pose` message over ROS topic
**my_box_pose_ground_truth**. To see pose information, run


```
rostopic echo my_box_pose_ground_truth
```

 after simulation has started.

## Tutorials

*Also see
[pr2_simulator tutorials](https://index.ros.org/p/pr2_simulator).*

- [Adding a GazeboRosForce gazebo ros plugin to a simulated object](#adding-a-gazeborosforce-gazebo-ros-plugin-to-a-simulated-object):
  \## the next tutorial description (optional)
- [Attaching a ROS Ground Truth Pose Broadcaster to Objects in Simulation](#attaching-a-ros-ground-truth-pose-broadcaster-to-objects-in-simulation):
  Attaching a ROS ground truth pose broadcaster to objects in simulation

## Troubleshooting

### Errors when using package

#### Error: ERROR NAME

**Example:** 

```
the error output the user will see on the console
```



**Solution:**

- Is something not connected? No device is connected.
