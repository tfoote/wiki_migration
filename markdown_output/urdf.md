  -- ------------------ -- -- -- ---------------------- --
     [English](urdf )            [简体中文](cn/urdf )   
  -- ------------------ -- -- -- ---------------------- --

## Overview

This package contains a number of [XML specifications](urdf/XML) for
robot models, sensors, scenes, etc. Each XML specification has a
corresponding parser in one or more languages.

  -- ---------------------------- -- ----------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------- -- --------------------------------------------- -- ------------------------------------------------------------------------------- --
     \<rowbgcolor=\"#FFFFE0\"\>      \'\'\'XML Description\'\'\'      \'\'\'C++\'\'\'                                                                                                                             \'\'\'Python\'\'\'                               \'\'\'XML Schema\'\'\'                                                          
     Model                           [model](urdf/XML/model)          [Parser API](http://www.ros.org/doc/api/urdf/html/) [Model API](https://github.com/ros/urdfdom_headers/tree/master/include/urdf_model)      [Model API](http://wiki.ros.org/urdfdom_py)      [urdf.xsd](https://raw.githubusercontent.com/ros/urdfdom/master/xsd/urdf.xsd)   
     Sensor                          [sensor](urdf/XML/sensor)                                                                                                                                                                                                                                                                                     
  -- ---------------------------- -- ----------------------------- -- ---------------------------------------------------------------------------------------------------------------------------------------- -- --------------------------------------------- -- ------------------------------------------------------------------------------- --

## Components == A number of different packages and components make up urdf. The following diagram attempts to explain the relationship between these components:

![\|width=\"780\"](attachment:urdf_diagram.png)

### Current Status of URDF Components in Hydro:

-   The core URDF parser and data structures (urdfdom, urdfdom_headers)
    have been pushed upstream into stand alone (no ROS-dependencies)
    software packages that will in the future be released into Ubuntu
    completely separate from ROS.

```{=html}
<!-- -->
```
-   There is now a distinction between a URDF file and a URDF data
    structure. A URDF file follows the XML format as described on the
    ros.org wiki. A URDF data structure is a set of generic classes that
    various formats (currently URDF and Collada) can be parsed into.

```{=html}
<!-- -->
```
-   A new plugin abstraction layer (urdf_parser_plugin) allows the URDF
    data structures to be populated with various file formats (currently
    URDF and Collada)

```{=html}
<!-- -->
```
-   The ROS packages urdf_parser and urdf_interface have been deprecated
    in Groovy and removed in Hydro.

## Getting Started

There is large set of \'\'\'tutorials\'\'\' on how to build up your own
robot models using the URDF specification. Check out the
[urdf/Tutorials](urdf/Tutorials) page.

We also developed a macro language called [xacro](xacro) to make it
easier to maintain the robot description files, increase their
readability, and to avoid duplication in the robot description files.

## Examples

See [this page](urdf/Examples) for a list of robots described by a URDF
model.

## Tools

### Verification

A command line tool \`\`check_urdf\`\` attempts to parse a file as a
URDF description, and either prints a description of the resulting
kinematic chain, or an error message.

For example, to run this tool on the pr2 urdf, first create the urdf
file by running: ```
rosrun xacro xacro.py `rospack find pr2_description`/robots/pr2.urdf.xacro -o /tmp/pr2.urdf
```

Then run the check by running:

Note: You may need to run \`sudo apt-get install liburdfdom-tools\`.

```
check_urdf pr2.urdf
```

Then run the check by running: ```
rosrun urdfdom check_urdf /tmp/pr2.urdf
```

and you should see something resembling:

```
robot name is: pr2
---------- Successfully Parsed XML ---------------
root Link: base_footprint has 1 child(ren)
    child(1):  base_link
        child(1):  base_laser_link
        child(2):  bl_caster_rotation_link
            child(1):  bl_caster_l_wheel_link
            child(2):  bl_caster_r_wheel_link
        child(3):  br_caster_rotation_link
            child(1):  br_caster_l_wheel_link
            child(2):  br_caster_r_wheel_link
        child(4):  fl_caster_rotation_link
            child(1):  fl_caster_l_wheel_link
            child(2):  fl_caster_r_wheel_link
        child(5):  fr_caster_rotation_link
            child(1):  fr_caster_l_wheel_link
            child(2):  fr_caster_r_wheel_link
        child(6):  torso_lift_link
            child(1):  head_pan_link
                child(1):  head_tilt_link
                    child(1):  head_plate_frame
                        child(1):  sensor_mount_link
                            child(1):  double_stereo_link
                                child(1):  narrow_stereo_link
 ...
```

### Visualization

Visual Studio Code has a
[ROS extension](https://hiro-group.ronc.one/vscode_urdf_previewer.html)
that supports URDF visualization.

To get a graphviz diagram of your urdf file, do the following: In
Indigo, the \`urdf_to_graphiz\` tool has moved to the
\`liburdfdom-tools\` package. You may need to run \`sudo apt-get install
liburdfdom-tools\` if you can\'t use \`urdf_to_graphiz\`
```
urdf_to_graphiz pr2.urdf
``` ```
urdf_to_graphiz pr2.urdf
```

The result is a file called pr2.pdf that looks something like this:

![\|width=\"700\"](attachment:graphiz.png)

### Creating URDF

URDF is XML, which is a text format. So you can create the files in any
text editor. An IDE with good XML support is recommended.

If there already exists a CAD model of the robot, there are some tools
that can be used to convert the CAD model to URDF. Here is a
non-exhaustive list:

-   [PTC Creo to URDF (iCub)](https://github.com/icub-tech-iit/cad-libraries/wiki/Prepare-PTC-Creo-Mechanism-for-URDF)
-   [SolidWorks URDF exporter](http://wiki.ros.org/sw_urdf_exporter)
-   [fusion2urdf](https://github.com/syuntoku14/fusion2urdf)
-   [OnShape to Robot](https://onshape-to-robot.readthedocs.io/en/latest/)
-   [Phobos Blender plugin](https://github.com/dfki-ric/phobos)

## Known Issues

-   Sensor model information is not included (except in gazebo
    extensions for simulated sensors).
