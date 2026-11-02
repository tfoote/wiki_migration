## Overview

As thermal camera simulation isn't supported natively by gazebo, this
plugin takes the following approach: Objects of interest (OOIs) that
have to appear hot in thermal vision are modelled using COLLADA and have
their emissive and ambient material properties set to maximum red like
this: 

```
<emission>
              <color sid="emission">1 0 0 1</color>
            </emission>
            <ambient>
              <color sid="ambient">1 0 0 1</color>
            </ambient>
```

 The relevant OOI will then always have
exactly red color, regardless of lighting conditions in gazebo. The
gazebo_ros_thermal_camera plugin then colors only the portions of the
MONO8 thermal image as white (for white hot) that have exactly this
maximum red color. The rest of the visual image is written to the
thermal image with much reduced intensity. The result looks like this:
![width=720](doc/Thermal_Cam_example.png)

Using this approach, methods for detection of objects by their heat
signature can be tested in simulation. However, this might not be
possible for methods fusing information from visual and thermal images,
as the visuals of OOIs are limited to red color. Note that
reconfiguration options for the color of interest and other convenience
options are not currently implemented.

## Example Use

The plugin is based on the gazebo_ros_camera plugin and thus has the
same parameters and signature for use in a URDF model:


```
<gazebo reference="thermal_frame">
      <sensor:camera name="thermal_camera_sensor">
        <imageSize>160 120</imageSize>
        <imageFormat>R8G8B8</imageFormat>
        <hfov>90</hfov>
        <nearClip>0.01</nearClip>
        <farClip>100</farClip>
        <updateRate>10</updateRate>
        <controller:gazebo_ros_thermal_camera name="thermal_camera_controller" plugin="libgazebo_ros_thermal_depth_camera.so">
          <alwaysOn>true</alwaysOn>
          <updateRate>10</updateRate>
          <imageTopicName>/thermal_camera/image_raw</imageTopicName>
          <cameraInfoTopicName>/thermal_camera/camera_info</cameraInfoTopicName>
          <frameName>thermal_optical_frame</frameName>
          <interface:camera name="thermal_camera_iface" />
        </controller:gazebo_ros_thermal_camera>
      </sensor:camera>
    </gazebo>
```
