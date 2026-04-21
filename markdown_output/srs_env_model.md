## Overview

This package provides a new Dynamic Environment Model server partially
based on OctomapServer from the octomap_mapping stack. The model manages
information about all detected, permanent, temporary and moving objects
in the environment. It publishes own topics, subscribes to some of input
data stream topics and it\'s internal state can be controlled by
services. We have created some simple
[tutorials](srs_env_model/Tutorials) that walk you through basic using
it.

## System architecture

The Dynamic Environment Model (DEM) serves as a node containing octomap
of the scene viewed by sensors and additional data types storing
detected objects.

Environment model server is based on core-plugin architecture model.
Whole this structure can be virtually divided into two parts - plugins
connected to the octomap and independent data structures. The first part
serves as a \"raw data\" processor. It tranforms input octomap to the
different data structure. The second part of the environment server
contains some \"higher level\" data structures, added by some detectors
in general.

-   Raw data structures
-   Octo map
-   Collision map
-   Collision grid
-   Collision objects
-   2D map
-   Marker array
-   Point cloud

```{=html}
<!-- -->
```
-   Other data structures
-   Object tree

```{=html}
<!-- -->
```
-   Other plugins
-   Compressed point cloud plugin
-   Example plugin
-   Limited point cloud plugin

### Octo map plugin

Contains octomap data - octomap tree with own node type
(`octomap::EModelTreeNode`). Can be subscribed to the point cloud
publishing topic to fill the map. This plugin is used by some other
plugins as a data source.

The octomap plugin also supports RGB colouring of the point cloud based
on the data from RGB camera. Other provided functionality is octree
filtering used to remove speckles and faster noise removal in the view
cone.

![\|width=90%](attachment:colored_voxel_map.png)

### Collision map plugin

This plugin converts occupied octomap nodes to the collision map
(`arm_navigation_msgs::CollisionMap`). Diameter can be set to limit
robot collision distance (this leads to smaller data flow).

### Collision grid plugin

This plugin also converts occupied octomap nodes to the other form -
occupancy grid (`nav_msgs::OccupancyGrid`). Used tree depth, map x and y
direction sizes can be set.

![\|width=90%](attachment:collision_grid.png)

### Collision objects plugin

It converts and publishes occupied octomap nodes to the collision
objects (`rm_navigation_msgs::CollisionObject`).

### Compressed point cloud plugin

This plugin takes robot camera position and uses it to filter currently
visible part of octomap. This is converted to the point cloud form and
it is sent as differential frame. The
[compressed_pc_publisher node](#CPC_NODE) can be used to combine
differential frames and to publish complete octomap again (in the usuall
point cloud form). This indirectness can be used to lower data flow.

### 2D map plugin

It converts and publishes octomap nodes to the 2D map
(`nav_msgs::OccupancyGrid`).

### Marker array plugin

It converts and publishes octomap nodes to the marker array
(`visualization_msgs::MarkerArray`).

### Point cloud plugin

It can convert incomming point cloud (`sensor_msgs::PointCloud2`) frame
id to some other and re-publishes it.

### Object tree plugin

This plugin is used to store objects detected by various perceptors.
These objects are stored in octree structure and they are represented by
their position and other needed parameters instead of point cloud.
Objects can be visualized with srs_interaction_primitives package.

Currently plugin supports bounding boxes and planes detected by tools in
the srs_env_model_percp package. All plugin functionality is provided by
services.

### Compressed point cloud plugin

This plugin publishes only visible part of the environment model. This
cloud can be used as live sight on octomap data or can be used together
with compressed point cloud publisher to transfer octomap to the other
device.

## Compressed point cloud publisher node

This node can be used to assembly and publish complete octomap from
differential frames published by
[ compressed point cloud plugin](#CPC_PLUGIN).

## ROS API

### Nodes

  -- ------------------------- -- ---------------------- -- ----------------------------------------------------------------- --
     **Node Name**                **Published Topics**      **Description**                                                   
     but_server_node                                        Main server node.                                                 
     compressed_pc_publisher      /input                    Differrential frames completion and complete octomap publishing   
  -- ------------------------- -- ---------------------- -- ----------------------------------------------------------------- --

### Services

All services are published in the /but_env_model/ namespace.

  -- ----------------------------------- -- ---------------------------------------------------------------------- -- --------------------------------------------------------------- -- --------------------------------------------------------------------------------------------------------- --
     **Service Name**                       **Input**                                                                 **Output**                                                         **Description**                                                                                           
     server_reset                                                                                                                                                                        Reset server                                                                                              
     server_pause                                                                                                                                                                        Pause server                                                                                              
     server_use_input_color                 bool                                                                                                                                         Set true (default) if input color information should be stored and used.                                  
     get_collision_map                      int32 - local version stamp id                                            arm_navigation_msgs/CollisionMap                                   Get current collision map.                                                                                
     insert_planes                          srs_env_model_msgs/PlaneArray plane_array                                                                                                    Add array of planes                                                                                       
     reset_octomap                                                                                                                                                                       Reset only octomap data.                                                                                  
     load_octomap                           string - input file name                                                  bool - true if all ok                                              Tries to load octomap file (without header) as a new env. model                                           
     load_octomap_full                      string - input file name                                                  bool - true if all ok                                              Tries to load octomap file (with header) as a new env. model                                              
     save_octomap                           string - output file name                                                 bool - true if all ok                                              Tries to store current env. model as octomap file (without header)                                        
     save_octomap_full                      string - output file name                                                 bool - true if all ok                                              Tries to store current env. model as octomap file (with header)                                           
     add_cube_to_octomap                    geometry_msgs::Pose - cube position, geometry_msgs::Pose - cube size                                                                         Set all cells inside given box as occupied                                                                
     remove_cube_from\\n_octomap            geometry_msgs::Pose - cube position, geometry_msgs::Pose - cube size                                                                         Set all cells inside given box as free                                                                    
     lock_collision_map                     bool - true if lock                                                                                                                          Lock collision map - map will not be updated from octree. Should be called before manual modifications.   
     is_new_collision_map                   time - time stamp of local data                                           bool - true if new data present, time - timestamp of new data      Service can be used to test if new collision map data is present                                          
     add_cube_to_collision_map              geometry_msgs::Pose - cube position, geometry_msgs::Pose - cube size                                                                         Set all collision maps cells inside given box as occupied                                                 
     remove_cube_from\\n_collision_map      geometry_msgs::Pose - cube position, geometry_msgs::Pose - cube size                                                                         Set all collision map cells inside given box as free                                                      
     set_crawl_depth                        uint8 - tree depth                                                        Set tree depth used for publishing                                                                                                                                           
     get_tree_depth                                                                                                   uint16 - tree depth                                                Get octomap tree depth                                                                                    
  -- ----------------------------------- -- ---------------------------------------------------------------------- -- --------------------------------------------------------------- -- --------------------------------------------------------------------------------------------------------- --

### Object tree plugin services

Services provided by Object tree plugin can be divided into two parts.
The first one is common for all saved objects. Services in the other one
have variants for all supported objects. All services are published in
the /but_env_model/ namespace.

  -- -------------------------- -- ------------------ -- ----------------------- -- ------------------------------------------------------------- --
     **Service Name**              **Input**             **Output**                 **Description**                                               
     get_objects_in_box                                  uint32\[\] object_ids      Returns ids of objects inside a box.                          
     get_objects_in_halfspace                            uint32\[\] object_ids      Returns ids of objects inside a halfspace defined by plane.   
     get_objects_in_sphere                               uint32\[\] object_ids      Returns ids of objects inside a sphere.                       
     remove_object                 uint32 object_id                                 Removes object from object tree.                              
     show_object                   uint32 object_id                                 Shows object using a srs_interaction_primitives server.       
     show_objtree                                                                   Show octree structure using a Marker.                         
  -- -------------------------- -- ------------------ -- ----------------------- -- ------------------------------------------------------------- --

The following services are available for these object types: plane,
aligned_box and bounding_box. All services are published in the
/but_env_model/ namespace.

  -- ------------------------------------ -- -------------------- -- -------------------- -- --------------------------------------------------------------------------------------------------- --
     **Service Name**                        **Input**               **Output**              **Description**                                                                                     
     get\_{object_type}                      uint32 object_id        object_description      Gets object from object tree.                                                                       
     get_similar\_{object_type}              object_description      uint32 object_id        Checks object tree for object similar to object in input parameter. Returns -1 if no such exists.   
     insert\_{object_type}                   object_description      uint32 object_id        Inserts object into object tree. Replaces object with same id if exists.                            
     insert\_{object_type}\_by_position      object_description      uint32 object_id        Inserts object into object tree. Replaces similar object if exists.                                 
  -- ------------------------------------ -- -------------------- -- -------------------- -- --------------------------------------------------------------------------------------------------- --

### Messages

  -- ------------------------------ -- ------------- -- ------------------------------------------------------------- --
     **Msg Name**                      **Content**      **Description**                                               
     srs_env_model/OctomapUpdates                       Partial frame message used in compressed pointcloud plugin.   
  -- ------------------------------ -- ------------- -- ------------------------------------------------------------- --

### Published topics

List of all published topics. All topics are published in the
/but_env_model/ namespace.

  -- ---------------------------- -- ------------------------------------- -- ------------------------------------------------------------------------------- --
     **Topic Name**                  **Message**                              **Description**                                                                 
     visualization_marker            visualization_msgs/Marker                Visualization markers                                                           
     collision_object                arm_navigation_msgs/CollisionObject      Octomap data - occupied nodes - as a collision objects                          
     pointcloud_centers              sensor_msgs/PointCloud2                  Octomap data - occupied nodes - as a point cloud                                
     collision_map                   arm_navigation_msgs/CollisionMap         Diameter limited octomap converted to the collision map                         
     marker_array_object             visualization_msgs/MarkerArray           Octomap data as a marker array                                                  
     map2d_object                    nav_msgs/OccupancyGrid                   Whole octomap converted to the 2D map                                           
     binary_octomap                  octomap_ros/OctomapBinary                Binary octomap data - whole tree                                                
     visible_pointcloud_centers      sensor_msgs/PointCloud2                  Octomap data - occupied nodes visible from the rviz camera - as a point cloud   
  -- ---------------------------- -- ------------------------------------- -- ------------------------------------------------------------------------------- --

## Installation

All components are in srs git in srs_env_model package and can be
compiled with ROS standard tool rosmake ```
rosmake srs_env_model
```

## Configuration

### Octo map plugin

For further information about octomap library and meaning of its
parameters see: <http://octomap.sourceforge.net>

Octomap and sensor parameters:

  -- ---------------------------- -- --------------------------------------------- -- ----------------------- --
     ** Parameter name **            ** Description **                                **Default value**       
     *resolution*                    Octomap resolution                               0.1                     
     *sensor_model/hit*              Probability value set to the occupied node.      0.7                     
     *sensor_model/miss*             Probability value set to the free node           0.4                     
     *sensor_model/min*              Clamping minimum threshold                       0.12                    
     *sensor_model/max*              Clamping maximum threshold                       0.97                    
     *max_range*                     Maximal sensor scope                             -1.0 - no range check   
     *octomap_publishing_topic*      Binary octomap publishing topic name             butsrv_binary_octomap   
  -- ---------------------------- -- --------------------------------------------- -- ----------------------- --

Outdated node filtering parameters:

  -- ------------------------------ -- ----------------------------------------------------- -- ---------------------- --
     ** Parameter name **              ** Description **                                        **Default value**      
     *camera_info_topic*               Camera info topic name                                   /cam3d/camera_info     
     *visualize_markers*               Should markers displayng camera cone be visualized?      true                   
     *markers_topic*                   Markers topic name                                       visualization_marker   
     *camera_stereo_offset_left*       Stereo camera left eye offset                            128                    
     *camera_stereo_offset_right*      Stereo camera right eye offset                           0                      
  -- ------------------------------ -- ----------------------------------------------------- -- ---------------------- --

Ground plane filtering parameters:

  -- -------------------------------- -- ------------------------------------------------------------------------------------ -- ------------------- --
     ** Parameter name **                ** Description **                                                                       **Default value**   
     *filter_ground*                     Should ground plane be filtered?                                                        false               
     *ground_filter/distance*            Distance of points from plane for RANSAC                                                0.04                
     *ground_filter/angle*               Angular derivation of ground plane                                                      0.15                
     *ground_filter/plane_distance*      Distance of found plane from z=0 to be detected as ground (e.g. to exclude tables)      0.07                
  -- -------------------------------- -- ------------------------------------------------------------------------------------ -- ------------------- --

### Collision map plugin

  -- ------------------------------ -- ----------------------------------------------------------------------- -- ---------------------- --
     ** Parameter name **              ** Description **                                                          **Default value**      
     *collision_map_octree_depth*      Used octree depth for map generation.                                      0 - whole tree         
     *collision_map_radius*            Collision map maximal radius in meters                                     2.0                    
     *collision_map_publisher*         Collision map publishing topic name                                        butsrv_collision_map   
     *collisionmap_frame_id*           FID to which will be points transformed when publishing collision map      /base_footprint        
  -- ------------------------------ -- ----------------------------------------------------------------------- -- ---------------------- --

### Collision grid plugin

  -- ------------------------------- -- ---------------------------------------- -- ---------------------- --
     ** Parameter name **               ** Description **                           **Default value**      
     *collision_grid_octree_depth*      Used octree depth for grid generation.      0 - whole tree         
     *grid_min_x_size*                  Collision grid minimal x                    0.0                    
     *grid_min_y_size*                  Collision grid minimal y                    0.0                    
     *collision_grid_publisher*         Collision grid publishing topic name        butsrv_collision_map   
  -- ------------------------------- -- ---------------------------------------- -- ---------------------- --

### Collision objects plugin

  -- --------------------------------- -- ------------------------------------------- -- ------------------------- --
     ** Parameter name **                 ** Description **                              **Default value**         
     *collision_object_publisher*         Collision object publishing topic name         butsrv_collision_object   
     *collision_object_frame_id*          Output frame id                                /map                      
     *collision_object_octree_depth*      Used octree depth for objects generation.      0 - whole tree            
  -- --------------------------------- -- ------------------------------------------- -- ------------------------- --

### 2D map plugin

  -- --------------------------------- -- ------------------------------------------- -- --------------------- --
     ** Parameter name **                 ** Description **                              **Default value**     
     *collision_object_publisher*         Collision map publishing topic name            butsrv_map2d_object   
     *collision_object_frame_id*          Output map frame id                            /map                  
     *min_x_size*                         Minimal map size - used for padding            0.0                   
     *min_y_size*                         Minimal map size - used for padding            0.0                   
     *collision_object_octree_depth*      Used octree depth for objects generation.      0 - whole tree        
  -- --------------------------------- -- ------------------------------------------- -- --------------------- --

### Marker array plugin

  -- ----------------------------- -- ------------------------------------------- -- --------------------------- --
     ** Parameter name **             ** Description **                              **Default value**           
     *marker_array_publisher*         Marker array publishing topic name             butsrv_markerarray_object   
     *marker_array_frame_id*          Marker array output frame id                   /map                        
     *marker_array_octree_depth*      Used octree depth for objects generation.      0 - whole tree              
  -- ----------------------------- -- ------------------------------------------- -- --------------------------- --

### Point cloud plugin

  -- -------------------------------- -- ------------------------------------------- -- --------------------------------------- --
     ** Parameter name **                ** Description **                              **Default value**                       
     *pointcloud_centers_publisher*      Pointcloud publishing topic name               butsrv_pointcloud_centers               
     *pointcloud_subscriber*             Input pointcloud subscriber topic name         /cam3d/depth/points                     
     *pointcloud_min_z*                  Point cloud minimal z value                    -std::numeric_limits\<double\>::max()   
     *pointcloud_max_z*                  Point cloud maximal z value                    std::numeric_limits\<double\>::max()    
     *pointcloud_octree_depth*           Used octree depth for objects generation.      0 - whole tree                          
  -- -------------------------------- -- ------------------------------------------- -- --------------------------------------- --

### Dynamic Environment Model

\...component specific parameters\...

command
