  -- ------------------------- -- -- -- ----------------------------- --
     [English](roch_bringup)            [简体中文](cn/roch_bringup)   
  -- ------------------------- -- -- -- ----------------------------- --

## Roch Bringup

Follow the [Roch tutorial](roch/Tutorials/Using package of roch_bringup)
to start your Ro\`\`ch.

## Launch Files

-   \'\'\'minimal.launch\'\'\' - The base launch file for Ro\`\`ch.
    Starts the basic nodes ([roch_base](roch_base)),
    [robot_state_publisher](robot_state_publisher),
    [diagnostic_aggregator](diagnostic_aggregator), and
    [robot_localization](robot_localization).

```{=html}
<!-- -->
```
-   \'\'\'sensor.launch\'\'\' - The sensor launch file. contains 3D
    sensors and 2D lasers. Starts all the nodes/nodelets required to use
    the 3D sensor contain Microsoft Kinect, ASUS Xtion, Intel Realsense
    200 or 2D laser include LS01C or Rplidar A1/A2 as a laser scanner
    and camera: [openni_camera](openni_camera) or
    [realsense_camera](realsense_camera) with [rgbd_launch](rgbd_launch)
    and
    [depthimage_to_laserscan](http://www.ros.org/wiki/depthimage_to_laserscan).

```{=html}
<!-- -->
```
-   \'\'\'concert_minimal.launch\'\'\' - The base launch file for rocon
    with Roch. This launch file will turn on
    [rocon_master_info](rocon_master_info),
    [rocon_app_manager](rocon_app_manager),
    [zeroconf_avahi](zeroconf_avahi), minimal.launch and etc. Note:
    rocon version with 0.9.0 and above, please checkout
    [tutorials](https://github.com/SawYer-Robotics/roch/blob/indigo/roch_rapps/README.md)
    for more details.
