## Description

A ROS driver to interact with the Ibeo LUX sensor and the Ibeo LUX
Fusion ECU. This driver does not work with the Ibeo LUX 8L or the
[ibeo_scala](ibeo_scala). Please see the list of supported hardware
below for more information. This driver was developed using the Ethernet
interface documentation version 1.38. An updated driver using Ethernet
interface documentation 1.47 is coming soon.

## Supported Hardware

-   Ibeo LUX 4L
-   Ibeo LUX 4L HD
-   Ibeo LUX Fusion ECU

## Subscribed Topics:

-   None

## Published Topics (Single LUX and LUX Fusion ECU)

  -- ---------------------------------------------------------------------------------------------------------------- -- ----------------------------- -- -------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>**Message Type **                                       **Topic **                       **Description **                                                                                   
     [network_interface/TCPFrame](http://docs.ros.org/api/network_interface/html/msg/TCPFrame.html)                      tcp_tx                           A copy of all raw TCP (Ethernet) data sent from the sensor/ECU.                                    
     [sensor_msgs/PointCloud2](http://docs.ros.org/melodic/api/sensor_msgs/html/msg/PointCloud2.html)                    as_tx/point_cloud                The scan data represented as a PCL::PointCloud\<pcl::PointXYZL\>.                                  
     [visualization_msgs/MarkerArray](http://docs.ros.org/melodic/api/visualization_msgs/html/msg/MarkerArray.html)      as_tx/objects                    Visualization of the detected objects as an array of wireframe boxes (intended for use in RViz).   
     [visualization_msgs/Marker](http://docs.ros.org/melodic/api/visualization_msgs/html/msg/Marker.html)                as_tx/object_contour_points      Visualization of the contour points which define detected objects (intended for use in RViz).      
  -- ---------------------------------------------------------------------------------------------------------------- -- ----------------------------- -- -------------------------------------------------------------------------------------------------- --

## Published Topics (Single LUX Only)

  -- -------------------------------------------------------------------------------------------------------- -- ----------------------------------- -- ------------------------------------------------------------------------------------------------------------------------ --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>**Message Type **                               **Topic **                             **Description **                                                                                                         
     [ibeo_msgs/ScanData2202](http://docs.ros.org/api/ibeo_msgs/html/msg/ScanData2202.html)                      parsed_tx/scan_data_2202               All data produced by a single LUX sensor about each scan including all points and their layers.                          
     [ibeo_msgs/ObjectData2221](http://docs.ros.org/api/ibeo_msgs/html/msg/ObjectData2221.html)                  parsed_tx/object_data_2221             All object data produced by a single LUX sensor and information about the detected objects                               
     [ibeo_msgs/HostVehicleState2805](http://docs.ros.org/api/ibeo_msgs/html/msg/HostVehicleState2805.html)      parsed_tx/host_vehicle_state_2805      Information about the estimated and provided vehicle state (x and y position, wheel angles, velocity, yaw rate, etc.).   
     [ibeo_msgs/ErrorWarninig](http://docs.ros.org/api/ibeo_msgs/html/msg/ErrorWarning.html)                     parsed_tx/error_warning                Error and warning data from the sensor.                                                                                  
  -- -------------------------------------------------------------------------------------------------------- -- ----------------------------------- -- ------------------------------------------------------------------------------------------------------------------------ --

## Published Topics (LUX Fusion ECU Only)

  -- -------------------------------------------------------------------------------------------------------- -- ----------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------- --
     \<tablewidth=\"100%\"rowbgcolor=\"#cccccc\"width=\"260px\"\>**Message Type **                               **Topic **                             **Description **                                                                                                                                        
     [ibeo_msgs/ScanData2204](http://docs.ros.org/api/ibeo_msgs/html/msg/ScanPoint2204.html)                     parsed_tx/scan_data_2204               All data produced by the Fusion ECU about each scan including all points and their layers (Fusion System v2.1 and older).                               
     [ibeo_msgs/ScanData2205](http://docs.ros.org/api/ibeo_msgs/html/msg/ScanData2205.html)                      parsed_tx/scan_data_2205               All data produced by the Fusion ECU about each scan including all points and their layers (Fusion System v2.2 and newer).                               
     [ibeo_msgs/ObjectData2225](http://docs.ros.org/api/ibeo_msgs/html/msg/ObjectData2225.html)                  parsed_tx/object_data_2225             All object data produced by the Fusion ECU and information about those objects (Fusion System v2.1 and older).                                          
     [ibeo_msgs/ObjectData2280](http://docs.ros.org/api/ibeo_msgs/html/msg/Object2280.html)                      parsed_tx/fusion_object_data_2280      All object data produced by the Fusion ECU and information about those objects (Fusion System v2.2 and newer).                                          
     [ibeo_msgs/CameraImage](http://docs.ros.org/api/ibeo_msgs/html/msg/CameraImage.html)                        parsed_tx/camera_image                 Image data provided by the Fusion ECU if a camera is attached and configured.                                                                           
     [ibeo_msgs/HostVehicleState2806](http://docs.ros.org/api/ibeo_msgs/html/msg/HostVehicleState2806.html)      parsed_tx/host_vehicle_state_2806      Information about the estimated and provided vehicle state (x and y position, wheel angles, velocity, yaw rate, etc.) (Fusion System v2.1 and older).   
     [ibeo_msgs/HostVehicleState2807](http://docs.ros.org/api/ibeo_msgs/html/msg/HostVehicleState2807.html)      parsed_tx/host_vehicle_state_2807      Information about the estimated and provided vehicle state (x and y position, wheel angles, velocity, yaw rate, etc.) (Fusion System v2.2 and newer).   
  -- -------------------------------------------------------------------------------------------------------- -- ----------------------------------- -- ------------------------------------------------------------------------------------------------------------------------------------------------------- --

## Parameters

\`ip_address\`\
The IP address of the sensor or ECU.

\`port\`\
The TCP port on which to listen for the data from the sensor or ECU.

\`is_fusion\`\
Whether the IP address above points to a fusion ECU (\`true\`) or a
single sensor (\`false\`).

\`sensor_frame_id\`\
The frame_id to be used for all published data from the sensor.
