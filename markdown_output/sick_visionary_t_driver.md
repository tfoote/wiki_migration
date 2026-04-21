## Description

This is an open source driver for the
[SICK visionary-T](https://www.sick.com/us/en/downloads/literature?q=%3ADef_Type%3ADownload%3Apartnumber%3A8018964).
The visionary-T is a 3D camera based on the time-of- flight (TOF)
principle. It provides real-time 3D data at up to 30 frame per second
(fps).

The 3D camera is configured and its images visualized via the
[SOPAS ET](https://www.mysick.com/partnerPortal/ProductCatalog/DataSheet.aspx?ProductID=92094)
software.

Once configured it runs in stand-alone operation mode and continuously
streams 3D data via TCP/IP.

Please see the operation manual for further information and/or technical
details.

Driver repository:

-   License: Apache 2.0
-   Source: <https://github.com/SICKAG/sick_visionary_t>
    \[\[<https://travis-ci.org/SICKAG/sick_visionary_t>\|![build status\|align="left"](https://travis-ci.org/SICKAG/sick_visionary_t.svg?branch=indigo-devel)\|target="_blank"\]\]

## Supported Hardware

This driver works with the following products

  -- ------------------------------------- -- ------------------------------------------------------------------------------------------------------- -- -------------- --
     **device name**                          **type**                                                                                                   **part no.**   
     visionary-T CX                           [V3S100-1AAAAAA](https://www.mysick.com/partnerPortal/ProductCatalog/DataSheet.aspx?ProductID=106219)      1067189        
     visionary-T CX without cooling fins      [V3S100-1AABAAB](https://www.mysick.com/partnerPortal/ProductCatalog/DataSheet.aspx?ProductID=106220)      1075027        
     visionary-T AG                           V3S110-1AAAAAA                                                                                             1075613        
     visionary-T AG without cooling fins      V3S110-1AABAAB                                                                                             1075614        
  -- ------------------------------------- -- ------------------------------------------------------------------------------------------------------- -- -------------- --

## API Stability

The 3D data streaming part of the ROS API is stable.

The digital i/o channel interface of this driver is considered
*unstable* and *not implemented* yet.

## Installation

In order to receive data, the IP address of the device has to be known.
Using SOPAS ET the default IP address (192.168.1.10) can be verified,
changed and stored permanently into the device.

In order to determine the IP address: 1. first connect the camera device
to a power source and the network interface to your computer, then 1.
start the SOPAS ET executable (Windows (r) based system required).

The device should be found, its IP address shown and automatically be
added to the SOPAS project.

Make sure that the device is pingable to verify the correct network
configuration.

The `remote_device_ip` parameter in the launch file needs to be set to
the verified device IP address. This easiest way is to provide the
parameter is in the launch file
(`launch/sick_visionary_t_driver.launch`).

## Operation

When the ROS driver is started, it sends a command that starts the data
streaming of the visionary-T. When the driver is terminated, the data
streaming is stopped at the device.

Attention:: This means the device has to be power-cycled before it can
be used with Sopas ET to view the 3D data.

## ROS API

```clearsilver
node.0 {
  name = sick_visionary_t_driver_node
  desc = Open source driver for the SICK visionary-T 3d TOF camera.
  pub {
    group.0 {
      name = Depth camera
      desc = Publishes depth, confidence and itensity data.
      0.name = camera/camera_info
      0.type = sensor_msgs/CameraInfo
      0.desc = Camera calibration and metadata.
      1.name = camera/depth
      1.type = sensor_msgs/Image
      1.desc = Raw image from device. Contains `uint16` depths in mm.
      2.name = camera/confidence
      2.type = sensor_msgs/Image
      2.desc = Raw image from device. Contains `uint16` confidence values.
      3.name = camera/intensity
      3.type = sensor_msgs/Image
      3.desc = Raw image from device. Contains `uint16` intensity values.
    }
    group.1 {
      name = Status and inputs/outputs
      desc = Publishes the status information and IO state of the sensor.
      0.name = camera/ios
      0.type = std_msgs/ByteMultiArray
      0.desc = IO state of the camera.
      1.name = /diagnostics
      1.type = diagnostic_msgs/DiagnosticStatus
      1.desc = Current state of the device including device variables.
    }
    group.2 {
      name = Polar Scan
      desc = Publishes the response of the polar scan (uses 3D camera as laser scan, configuration by Sick software).
      0.name = camera/scan
      0.type = sensor_msgs/LaserScan
      0.desc = Measurements reduced to a laser scan.
    }
    group.3 {
      name = Height Map
      desc = Publishes the response of the height map (uses 3D camera to detect obstacles on the floor in front of the camera, configuration by Sick software).
      0.name = camera/cartesian
      0.type = sensor_msgs/PointCloud2
      0.desc = Measurements reduced to a 2D grid.
    }
  }
  srv{
      0.name = enable_depth_map
      0.type = std_srvs/Trigger
      0.desc = Stops height map and polar scan stream and starts stream of pointclouds.

      1.name = enable_height_map
      1.type = std_srvs/Trigger
      1.desc = Stops depth map and polar scan stream and starts stream of the Cartesian warning zones.

      2.name = enable_polar_scan
      2.type = std_srvs/Trigger
      2.desc = Stops height map and depth map stream and starts stream of polar scan which simulates a laser scan.
  }
  param {
    group.0 {
      0.name = ~remote_device_ip
      0.type = string
      0.default = 192.168.1.10
      0.desc = Specifies the address of the device to open (e. g. an ip address). The settings of the sensor (regarding calibration, resolution and so) are read from the device and used.

      1.name = ~frame_id
      1.type = string
      1.default = camera
      1.desc = Specifies the frame id of the published messages.

      2.name = ~prevent_frame_skipping
      2.type = bool
      2.default = false
      2.desc = Specifies whether the publishing and generation of ROS messages are skipped if the computer is too slow to handle all the data. Therefore only the most recent data from the sensor is published (if parameter is false).

      3.name = ~io_polling_interval
      3.type = double
      3.default = 0.1
      3.desc = Specifies the time interval in seconds to poll the IOs of the device.

      4.name = ~channel
      4.type = string
      4.default = NO_CHANGE
      4.desc = Specifies the initial selected streaming/channel (NO_CHANGE, DEPTHMAP, POLAR2D, CARTESIAN).

      5.name = ~user
      5.type = string
      5.default = SERVICE
      5.desc = Specifies the default user level used to write parameters (RUN, AUTHORIZEDCLIENT, MAINTENANCE, SERVICE).

    }
}
```
