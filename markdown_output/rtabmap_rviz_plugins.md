\<\<Include(rtabmap_ros/menu)\>\>

## RVIZ plugins

### Map Cloud Display

![MapCloudType.png](attachment:MapCloudType.png)

This rviz plugin subscribes to /mapData
(\<\<MsgLink(rtabmap_msgs/MapData)\>\>) topic. A 3D map cloud will be
created incrementally in RVIZ. When the graph is changed, all point
clouds added in RVIZ will be transformed to new poses. It has the same
properties as [PointCloud](rviz/DisplayTypes/PointCloud) display but
with these new ones:

  -- -------------------------------- -- ------------------------------------------------------------------------------------------------------------------ -- -------------------------- -- --------------------- --
                                         \'\'\'Properties\'\'\'                                                                                                                                                    
     \'\'\'Name\'\'\'                    \'\'\'Description\'\'\'                                                                                               \'\'\'Valid Values\'\'\'      \'\'\'Default\'\'\'   
     Cloud decimation                    How the input depth and RGB images are decimated before creating the point cloud                                      \[1-16\]                      4                     
     Cloud max depth (m)                 Maximum depth of each point cloud added to map (0 means no maximum)                                                   \[0-9999\]                    4                     
     Cloud voxel size (m)                Voxel size of the generated point clouds (0 means no voxel)                                                           \[0-1\]                       0.01                  
     Filter floor (m)                    Maximum height of the floor filtered (disabled=0).                                                                    \[0-9999\]                    0                     
     Node filtering radius (m)           Only keep one node in the specified radius (disabled=0).                                                              \[0-1\]                       0.2                   
     Node filtering angle (degrees)      Only keep one node in the specified angle in the filtering radius (disabled=0).                                       \[0-180\]                     30                    
     Download Map                        Download the map from [rtabmap](rtabmap_slam#rtabmap) node. This may take a while if the map is big, be patient!      .                             .                     
     Download Graph                      Download the graph from [rtabmap](rtabmap_slam#rtabmap) node.                                                         .                             .                     
  -- -------------------------------- -- ------------------------------------------------------------------------------------------------------------------ -- -------------------------- -- --------------------- --

### Map Graph Display

This rviz plugin subscribes to /mapGraph
(\<\<MsgLink(rtabmap_msgs/MapGraph)\>\>) topic. It will show the
RTAB-Map\'s graph with different colors depending on the links\' type.
It has the same properties as [Path](rviz/DisplayTypes/Path) display.

### Info Display

This rviz plugin subscribes to /info
(\<\<MsgLink(rtabmap_msgs/Info)\>\>) topic. Information about loop
closures detected are shown in the \"Status\".
