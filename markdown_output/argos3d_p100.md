```
argos3d_p100_ros_pkg
```

------------------------------------------------------------------------

------------------------------------------------------------------------

This ROS package uses an old API for the Bluetechnix Argos3D P100 ToF
sensor.

There is a new package
(<https://github.com/voxel-dot-at/bta_tof_driver>) that uses the new
[BltToFApi](https://support.bluetechnix.at/wiki/Bluetechnix_'Time_of_Flight'_API)
developed by Bluetechnix for interacting with their sensors.

We recommend to use the new bta_tof_driver package.

------------------------------------------------------------------------

# Description

This package explains how to configure your system and ROS to use the
Argos3D P100 ToF camera. The package includes an example allowing you to
visualize images using the rviz viewer included in ROS. It demonstrates
how to use the camera within ROS and the different parameter
configurations of the Argos3D P100 as well as its capabilities.

To get more information about the Time of Flight camera Argos3D P100
please visit Bluetechnix website:
<http://ww2.bluetechnix.com/en/products/depthsensing/product/argos3d-p100/>

# First step: Get ROS

The **\'argos3d_p100_ros_pkg**\' works with ROS versions groovy and
hydro. You can use catkin workspaces or the previous rosbuild to
configure, compile and get ready ROS.

The following are links to tutorials on setup and basic use of ROS to
get you get started:

In Ubuntu follow the ROS installation tutorial:

<http://wiki.ros.org/hydro/Installation/Ubuntu>.

Why to use catkin workspaces:

<http://wiki.ros.org/catkin>

<http://wiki.ros.org/catkin_or_rosbuild>

<http://wiki.ros.org/catkin/Tutorials/create_a_workspace>

To configure a catkin workspace in your ROS installation, follow this:

ROS tutorial:
<http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment>

# Known Problems

Be sure your libboost library version is \>= 1.49. Previous versions as
1.46 generate errors while compiling argos3d_p100-ros-pkg.

# Configuration

## Setup P100 USB rules and native libraries

The first step is to add the PMDSDK to our system. (The PMDSDK is
copyrighted software and it is distributed with your Argos3D P100)

### Usb Device rules

After unziping the software distributed with your Argos3D P100 camera,
browse to the directory of your operating system version.

Install the driver for using the ToF camera:

In Ubuntu/linux copy the file from the driver folder to
**/etc/udev/rules.d/**

```
cd driver 
sudo cp 10-pmd-ubuntu.rules /etc/udev/rules.d/
``` This will set the right permissions to allow
not sudo users to use the camera.

### Libraries setup

Add PMDSDK to your system (use the right version for your system 32 or
64 bits).

-   1\. Add the dynamically linked shared object library libpmdaccess2.
    Use one of the following options:

1\. You have different ways to add it to the **LD_LIBRARY_PATH**. 1. You
can simply copy the libpmdaccess2.so file to **/usr/local/lib** as root
(or the defauld search library path of your system) 1. Add a .conf file
(like pmd_camera_L64.conf) with the path of your library in
**/etc/ld.so.conf.d**. The file must contaning the following lines:

```
#PMD camera support
/.../PMDSDK/bin
/.../PMDSDK/include
```

-   **replace the dots with the absolute path to the PMDSDK directory**

```{=html}
<!-- -->
```
-   2\. Add includes and dynamic plugin libraries

```{=html}
<!-- -->
```
-   Move the PMDSDK folder to a directory where the operating system can
    find it (/usr/include)
-   or set an environment variable called \$PMDDIR to the path where
    there is the PMDSDK.

After adding libraries, update the links and cache of the share
libraries with:

```
ldconfig
```

# Installation

## Install dependencies

Make sure you have the following dependencies already installed:

```
apt-get install ros-hydro-pcl-ros ros-hydro-pcl-conversions ros-hydro-perception-pcl
```

## Install the package

Clone from repository:
<https://github.com/voxel-dot-at/argos3d_p100_ros_pkg.git> to your src/
folder in your catkin workspace and compile it with:

```
cd catkin_ws
source devel/setup.bash ## initialize search path to include local workspace
cd src/
git clone https://github.com/voxel-dot-at/argos3d_p100_ros_pkg.git
cd ..
catkin_make
```

# Usage

## Watch our demo video:

[Youtube](https://www.youtube.com/watch?v=1yVNbUQoMrU)

## Start the ROS core

```
roscore &
```

## Start capturing

```
cd catkin_ws
source devel/setup.bash
rosrun argos3d_p100 argos3d_p100_node
```

-   You can change the camera parameters through command option when
    initializing the node.

```{=html}
<!-- -->
```
-   Use \--help parameter to display parameter initialization usage.

```
Using help for argos3d_p100_ros_pkg
 You can set default configuration values for the camera with the following options:

 Usage:
 rosrun argos3d_p100 argos3d_p100_node
        -it *Integration_Time*
          Integration time(in msec) for the sensor
          (min: 100 | max: 2700 | default: 1500)
        -mf  *Modulation_Frequency*
          Set the modulation frequency(Hz) of the sensor
          (min: 5000000 | max: 30000000 | default: 30000000)
         -fr *Frame_Rate* 
          Set the frame rate of the camera by setting the Phase Time (Please be careful when setting values higher than 40 FPS without using an extra cooling system. The camera can stress by overheating and be damaged). 
          (min: 1 | max: 160 | default: 40)
         -flip_x *flip_x* 
          Flip images in the x coordinate. 
          (ON: if set | OFF: default)
         -flip_y *flip_y* 
          Flip images in the y coordinate. 
          (ON: if set | OFF: default)
        -bf *Bilateral_Filter*
          Turns bilateral filtering on or off
          (ON: if set | OFF: default)
        -af *Amplitude_Filter_On*
          Whether to apply amplitude filter or not. Image pixels with amplitude values less than the threshold will be filtered out
          (ON: if set | OFF: odefault)
        -at *Amplitude_Threshold*
          What should be the amplitude filter threshold. Image pixels with lesser aplitude values will be filtered out. Amplitude Filter Status should be true to use this filter
          (min: 0 | max: 2500 | default: 0)

 Example:
```

## \* Use calibration file

In the software distibuted with your camera there is a calibration file
that provides precise 3D position calculation. The file is load when the
connection with you Argos3D is established.

In order to use it, just copy this file to the folder where you will
execute the node:

```
cp argos3d.cal catkin_ws
cd catkin_ws
rosrun argos3d_p100 argos3d_p100_node
```

The argos3d_p100_node will show a message that confirmes you if the
calibration file was loaded successfully.

## Visualization in rviz

```
cd driver 
sudo cp 10-pmd-ubuntu.rules /etc/udev/rules.d/
```0 After the rviz window comes up, set the
following options.

Add a Pointcloud2 topic to visualize the depth clouds. Two different
point sets are published with following topic names:

-   **/depth_non_filtered :** raw data from the pmd camera.
-   **/depth_filtered : ** after applying amplitude threshold, if
    selected.

To do this please perform the following steps:

1\. In the \"Display\" panel on the left, open the first group of
settings called \"Global Options\", set the option \"Fixed frame\" to
**/tf_argos3d** 1. At the bottom in \"Display\" click on the button
**add** to open a dialog titled \"Create visualization\" 1. In the
dialog opened after, choose the tab \"By topic\" and select the
**/depth_non_filtered** topic.

## Using filters and parameters configuration

To apply point filters and change camera parameters, use
dynamic_reconfigure from ros. To use, it run the configuration interface
(after launching argos3d_p100_ros_pkg)

```
cd driver 
sudo cp 10-pmd-ubuntu.rules /etc/udev/rules.d/
```1

-   Select /argos3d_p100 to view the options available for
    modifications.

Following camera parameters and filtering methods can be accessed using
the dynamic reconfigure

. **Integration_Time :** Modifies the integration time of the sensor.

. **Modulation_Frequency :** Modifies the modulation frequency of the
sensor.

. **Frame_Rate :** Sets the frame rate by changing the Phase Time.
**NOTE** Please be careful when setting values higher than 40 FPS
without using an extra cooling system. The camera can stress by
overheating and be damaged.

. **Flip_X :** Flip 3d data in the x coordinate.

. **Flip_Y :** Flip 3d data in the y coordinate.

. **Bilateral_Filter :** Turns bilateral filtering on or off.

. **Amplitude_Filter_On :** Use the amplitude filter or not.

. **Amplitude_Threshold :** Image pixels with smaller amplitude values
will be filtered out. Amplitude_Filter_On status needs to be true to
apply this filter value.
