## PR2 Plugins

This package contains dynamic plugins for [ Gazebo](gazebo) and
[ROS](ROS) integration with simulated hardware.

-   Plugin-Supported Hardware:
-   [pr2_etherCAT](pr2_etherCAT)/[ PR2 Controller Manager](pr2_controller_manager):
    provided by `GazeboRosControllerManager`.
-   [ Prosilica Camera](prosilica_camera): provided by
    `GazeboRosProsilica`.
-   [Battery Power Monitor](power_monitor): provided by
    `GazeboRosPowerMonitor`.
-   Unsupported Features:
-   [ Power Board Driver](pr2_power_drivers)

Please see [gazebo_plugins](gazebo_plugins) for additional supported
hardware components in simulation.

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
[ Prosilica Camera hardware](prosilica_camera) on PR2.

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
to those provided by [PR2 power monitor node](power_monitor) on physical
PR2.

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



```clearsilver
name = gazebo_ros_power_node
desc = Gazebo plugin for simulating the PR2 power monitor.
sub {
  0.name = plugged_in
  0.type = pr2_gazebo_plugins/PlugCommand
  0.desc = plugged in state
}
pub {
  0.name = <powerStateTopic>
  0.type = pr2_msgs/PowerState
  0.desc = simulated power state
}
```





```clearsilver
name = gazebo_ros_prosilica_node
desc = Gazebo plugin for simulating the prosilica camera. This follows the standard ROS API for camera drivers.
pub {
  0.name = <imageTopicName>
  0.type = sensor_msgs/Image
  0.desc = Camera image
  1.name = <cameraInfoTopicName>
  1.type = sensor_msgs/CameraInfo
  1.desc = Camera info
}

srv {
    0.name = request_image
    0.type = polled_camera/GetPolledImage
    0.desc = '''(Polled Mode Only)''' Captures an image and publishes it in the namespace specified by the request message. Returns the timestamp.
}
```



### gazebo_ros_controller_manager

`GazeboRosControllerManager` plugin provides similar ROS interface as
[pr2_etherCAT](pr2_etherCAT) on the physical PR2 robot. This plugin is
written in a way that [PR2 controller manager](pr2_controller_manager)
works transparently with either this simulated plugin or the
[pr2_etherCAT](pr2_etherCAT) hardware. For more information on using
[generic controllers](robot_mechanism_controllers) or
[PR2 specific controllers](http://ros.org/wiki/pr2_mechanism_controllers)
with this plugin, please see
[pr2_controller_manager](pr2_controller_manager).

## Tutorials

## Roadmap

This stack will be updated with new features as the PR2 hardware itself
is updated. Future versions will also incorporate
[dynamic_reconfigure](dynamic_reconfigure) options to match ORS driver
functionality.
