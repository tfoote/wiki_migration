## Overview

A plugin module for the Gazebo simulation that enables control of a set
of actuators. A simulated robot can be generated from the existing robot
description URDF by simply adding a Gazebo Actuator Array Controller.

![](attachment:actuator_array_gazebo.png)

## Example Usage

The following XML block inside of robot description [urdf](urdf) creates
an Actuator Array Driver interface with four joints. The `<joint>`
block may be repeated as often as needed. Inside each `<joint>`
block, the `<name>` tag must reference the name of a joint specified
in the urdf. The `<home>` tag is used to specify the home position
of each joint. Internally, each joint is controlled by a PID loop. The
tuning parameters for the PID are specified for each joint. This allows
the simulated performance to be tuned to match the real system.



```xml
<!-- Add a Gazebo plugin controller -->
<gazebo>
  <controller:gazebo_ros_actuator_array 
              name="actuator_array_controller" 
              plugin="libgazebo_ros_actuator_array.so">
    <alwaysOn>true</alwaysOn>
    <updateRate>50.0</updateRate>
    <robotParam>robot_description</robotParam>
    <joint>
      <name>joint1</name>
      <home>0.0</home>
      <p>10.0</p>
      <i>0.0</i>
      <d>0.0</d>
      <iClamp>0.0</iClamp>
    </joint>
    <joint>
      <name>joint2</name>
      <home>2.094395102</home>
      <p>10.0</p>
      <i>0.0</i>
      <d>0.0</d>
      <iClamp>0.0</iClamp>
    </joint>
    <joint>
      <name>joint3</name>
      <home>1.483529864</home>
      <p>10.0</p>
      <i>0.0</i>
      <d>0.0</d>
      <iClamp>0.0</iClamp>
    </joint>
    <joint>
      <name>joint4</name>
      <home>0.0</home>
      <p>10.0</p>
      <i>0.0</i>
      <d>0.0</d>
      <iClamp>0.0</iClamp>
    </joint>
  </controller:gazebo_ros_actuator_array>
</gazebo>
```


