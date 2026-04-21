ROS packages for SICK line guidance sensors. This driver provides the
measurement data as
[PointCloud2](http://docs.ros.org/api/sensor_msgs/html/msg/PointCloud2.html).
The software is hosted under
<https://github.com/SICKAG/sick_line_guidance>

The package supports ROS distributions
[kinetic](http://wiki.ros.org/kinetic) and
[melodic](http://wiki.ros.org/melodic)

## Devices Supported

The driver supports at least the devices listed below and has also been
tested with these devices:

  -- ----------------- -- ------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------- -- -------------- --
     **device name**      **part no.**                                                                                                                 **description**                                            **tested?**    
     OLS10                [1092169](https://www.sick.com/de/en/line-guidance-sensors/optical-line-guidance-sensors/ols/ols10-bp112311/p/p553247)       Optical line guidance sensor with CANopen-Interface        ✔ \[stable\]   
     OLS20                [1095594](https://www.sick.com/de/en/line-guidance-sensors/optical-line-guidance-sensors/ols/ols20-bb1114142/p/p614644)      Optical line guidance sensor with CANopen-Interface        ✔ \[stable\]   
     MLS                  [1092496](https://www.sick.com/de/en/mls/mlse-0200a2tp0/p/p585645)                                                           Magnetic line guidance sensors with CANopen-Interface      ✔ \[stable\]   
  -- ----------------- -- ------------------------------------------------------------------------------------------------------------------------- -- ------------------------------------------------------- -- -------------- --

## Installation from sources

The driver is constantly being further developed, so we recommend that
you check out and compile the software from the devel branch of the
repository. The following actions are necessary for this:

```bash
source /opt/ros/<rosdistro>/setup.bash
mkdir -p ~/ros_catkin_ws/src/
cd ~/ros_catkin_ws/src/
git clone -b devel --single-branch git://github.com/SICKAG/sick_line_guidance.git
cd ..
catkin_make
source ~/ros_catkin_ws/install/setup.bash
```

## First steps

Following the steps described in section "starting" under
<https://github.com/SICKAG/sick_line_guidance>

## Troubleshooting

Following the steps described in section "Troubleshooting and
diagnostics" under <https://github.com/SICKAG/sick_line_guidance>

## Support

-   In case of technical support please open a new issue. Under
    <https://github.com/SICKAG/sick_line_guidance/issues>. For optimal
    support, add the following information to your request: 1. Line
    guidance model name, 1. Ros node startup log, 1. Sopas file of your
    device configuration. The instructions at
    <http://sickusablog.com/create-and-download-a-sopas-file/> show how
    to create the Sopas file.
-   In case of application support please use
    <https://supportportal.sick.com>.
