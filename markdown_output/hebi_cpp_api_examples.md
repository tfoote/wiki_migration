# Overview

This package is a set of examples as well as useful standalone nodes for
controlling [HEBI Robots](http://hebi.us).

**Note: this should be used in preference to the older/deprecated HEBI
ROS API**

# Dependencies/Installation

These examples depend on:

-   The [HEBI C++ API](http://wiki.ros.org/hebi_cpp_api) package:
    contains the library necessary for connecting to HEBI physical
    hardware.

Some of these examples depend on:

-   The [hebi_description](http://wiki.ros.org/hebi_description)
    package: contains XACRO macros and URDF files to assist in
    visualizing HEBI robots.
-   The
    [hebi_moveit_configs](https://github.com/HebiRobotics/hebi_moveit_configs)
    package: contains MoveIt configs for several standard HEBI kits.

To install all dependencies in a new catkin workspace, run the following
steps (replace `<ros-distro>` with kinetic` or `melodic`):


```
sudo apt-get install ros-<ros-distro>-hebi-cpp-api

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/HebiRobotics/hebi_moveit_configs.git
git clone https://github.com/HebiRobotics/hebi_description.git
git clone https://github.com/HebiRobotics/hebi_cpp_api_ros_examples.git hebi_cpp_api_examples
cd ..
catkin_make
```



# Getting Started

To launch an example, run `roslaunch hebi_cpp_api_examples <example
name>`.

(if you haven't yet, you will need to run `source devel/setup.sh`
first)

For more detail about the available examples and parameter, select the
system you wish to work with.

  -- ---------------------------------------------------------------------------------------------------------------- ---------------------------------------------------- ------------------------------------------------------------------ ------------------------------------------- ---------------------------------------------------------------------------------------------------------------- -- --
     <:>**Robot Type**                                                                                                                                                   <:48%> **Relevant Examples**                                                                                 <:48%> **Examples in Other Packages **                                                                            
     <#000000>                                                                                                                                                           <#000000>                                                                                                    <#000000>                                                                                                         
     <:                                                                                                              3>![\|width="120"](attachment:arm.png) **Arms**                                                                      [Arm Node](hebi_cpp_api_examples/ArmNode)                                                                                                                       
     [MoveIt Node](hebi_cpp_api_examples/MoveItArmNode)                                                                                                                                                                                                                                                                                                                                                       
     [Teach-repeat Arm Node](hebi_cpp_api_examples/TeachRepeatArmNode)                                                                                                                                                                                                                                                                                                                                        
     <#000000>                                                                                                                                                           <#000000>                                                                                                    <#000000>                                                                                                         
     <:>![\|width="120"](attachment:daisy.png) **Hexapod (Daisy)**                                                                                                                                                                                                                    [Hexapod Control](https://github.com/HebiRobotics/hebi-ros-daisy)                                                   
     <#000000>                                                                                                                                                           <#000000>                                                                                                    <#000000>                                                                                                         
     <:>![\|width="120"](attachment:rosie.png) **Omnibase Mobile Manipulator (Rosie)**                                                                                 [Rosie teach-repeat](hebi_cpp_api_examples/RosieTeachRepeat)                                                   [Beanbag Picking Vision Demo (requires Intel RealSense)](https://github.com/HebiRobotics/hebi_rosie_ros_demo/)      
     <#000000>                                                                                                                                                           <#000000>                                                                                                    <#000000>                                                                                                         
     <:>![\|width="120"](attachment:diffdrive.png) ![\|width="120"](attachment:omnibase.png) **Mobile Bases**                                                        [Mobile Base Nodes](hebi_cpp_api_examples/MobileBases)                                                                                                                                                                             
     <#000000>                                                                                                                                                           <#000000>                                                                                                    <#000000>                                                                                                         
     <:>![\|width="120"](attachment:jackal.png) **Clearpath Jackal Integration**                                                                                       [Clearpath Jackal Teleop](hebi_cpp_api_examples/ClearpathJackal)                                                                                                                                                                   
  -- ---------------------------------------------------------------------------------------------------------------- ---------------------------------------------------- ------------------------------------------------------------------ ------------------------------------------- ---------------------------------------------------------------------------------------------------------------- -- --
