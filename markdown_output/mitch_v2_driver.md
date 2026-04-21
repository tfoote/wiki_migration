## Introduction

This package provides the official ROS driver for the 221e Multisensor
InerTial CHamaleon (MITCH) V2 device.

Package available for:

-   ROS Noetic - Ubuntu 20.04
-   ROS Noetic - Windows 10

## Installation

### Install ROS and create a Catkin workspace

a\. Ubuntu 20.04:

-   Install [ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)
    on [Ubuntu 20.04](https://www.ubuntu-it.org/download)
-   Create your
    [ Catkin Workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) b.
    Windows 10:
-   Install [ROS Noetic](https://wiki.ros.org/Installation/Windows) on
    Windows 10
-   Open your ROS short cut terminal
-   Create your
    [ Catkin Workspace](https://github.com/Brabalawuka/RosOnWindows) (in
    this tutorial, we assume that your catkin workspace is located in
    your ```c:\\``` directory)

Tips for Windows:

-   Remember to start your installation routine from the ROS command
    short cut (created in the installation step)
-   Assuming you are exploiting
    [Microsoft Visual Studio 2019](https://docs.microsoft.com/en-us/visualstudio/releases/2019/release-notes),
    remember to include the "Desktop development with C++" workload.
    Moreover, in the Individual Components, select "Windows 10 SDK".
-   if you need the Ninja build tool, go to the
    [ releases page](https://github.com/ninja-build/ninja/releases ) and
    download a suitable binary for Windows. Place ```ninja.exe```
    in a suitable spot, e.g., ```C:\\Ninja```. Make sure that
    CMake can find ```ninja.exe``` by adding ```C:\\Ninja```
    to your ```%PATH%```.

To set up the ```catkin_make``` tools in Visual Studio 2019:

-   From the ROS shortcut, enter ```devenv``` to start your Visual
    Studio IDE;
-   Choose to open up your catkin workspace from your local folder;
-   As Visual Studio is using different settings for CMake projects, we
    need to configure the CMake file. Thus, click ```Project \-->
    CMake Settings for Project``` and edit the JSON version of your
    Cmake settings file as follows:



```
{
  "configurations": [
    {
      "name": "x64-Debug",
      "generator": "Ninja",
      "configurationType": "RelWithDebInfo",
      "inheritEnvironments": [ "msvc_x64_x64" ],
      "buildRoot": "C:\\catkin_ws\\build",
      "installRoot": "C:\\catkin_ws\\install",
      "cmakeCommandArgs": "DCATKIN_DEVEL_PREFIX=C:\\catkin_ws\\devel",
      "ctestCommandArgs": ""
    }
  ]
}
```



In this way, Cmaking and building your project from Visual Studio will
be equal to a catkin_make outside the Visual Studio environment. You can
also open the Command Line directly from the Visual Studio
```Tools``` button.

### Install lib221e

lib221e is the C++ library for the 221e Communication Protocol. Follow
the installation instructions available
[here](https://github.com/221eROS/lib221e.git).

### Clone mitch_v2_driver in your Catkin Workspace

a\) Ubuntu: 

```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/221eROS/mitch_v2_driver.git
$ catkin_make
```



b\) Windows: 

```
$ cd c:\catkin_ws\src
$ git clone https://github.com/221eROS/mitch_v2_driver.git
$ cd ..
$ catkin_make
```



## Usage

### Device connection

Switch on your MITCH V2 device. From your catkin workspace, launch the
following command to connect to your sensor and enable its ROS node:


```
$ roslaunch mitch_v2_driver mitch_v2.launch
```

 Among others, this launch file allows you to
set: - port name (Default: COM4); - baudrate (Default: 115200).

### Device shutdown

Assuming the ROS node of your MITCH V2 sensor is active \[step 3(a)\],
launch the following command to switch off your device:


```
$ roslaunch mitch_v2_driver shutdown.launch
```



### Battery charge and voltage

Assuming the ROS node of your MITCH V2 sensor is active \[step 3(a)\],
type the following command from your catkin workspace:


```
$ roslaunch mitch_v2_driver battery.launch
```

 The node will send back the battery charge, its
voltage, or both depending on whether the arguments \*charge\* and
\*voltage\* are set to \*true\*.

### Firmware version

Assuming the ROS node of your MITCH V2 sensor is active \[step 3(a)\],
type the following command from your catkin workspace:


```
$ roslaunch mitch_v2_driver get_firmware_version.launch
```


