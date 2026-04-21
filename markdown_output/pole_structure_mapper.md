## Overview

The goal of the software presented in this stack is to be able to use a
ground robot equipped with a depth sensor to generate a 3D map of a
structure composed of poles as it is climbed by a climbing robot. This
sections contains an overview of the two algorithms implemented in this
package, pole section extractor and 3D structure mapper.

### Pole Extractor

This algorithm is in charge of extracting pole sections from the
environment inside a region of interest centered at the gripper of the
climbing robot. Extraction is achieved using cylindrical segmentation.

![\|width=100%](attachment:extractor.jpg)

### 3D Structure Mapper

This algorithm uses the pole sections published by pole extractor to
construct a map of the structure being climbed.

![\|width=100%](attachment:mapper.jpg)

For more details on how the algorithms work check the publications
section down below.

## ROS API



```clearsilver
node.0 {
name=pole_extractor_node
desc=`pole_extractor_node` is a region of interest cylindrical segmentation algorithm.
pub{
0.name= pole_cloud
0.type= sensor_msgs/PointCloud2
0.desc= This allows to visually debug the segmented pole surface.

1.name= roi_cloud
1.type= sensor_msgs/PointCloud2
1.desc= This allows to visually debug the filtered roi point cloud.

2.name= pole_extractor_markers
2.type= visualization_msgs/Marker
2.desc= This allows to visually debug the output of the algorithm.

3.name= pole
3.type= pole_structure_mapper/PoleSectionStamped
3.desc= The output of the algorithm.
}
sub{
0.name= chewed_cloud
0.type= sensor_msgs/PointCloud2
0.desc= The point cloud from the depth sensor.

1.name= extract_poles
1.type= std_msgs/Bool
1.desc= Control topic for outputting data or not.
}
param {
0.name= ~gripper_tag_frame_id
0.default= ar_marker
0.type= string
0.desc= The frame id of the gripper ar tag.

1.name= ~filter_box_width
1.default= 2.0
1.type= double
1.desc= The width of the roi.

2.name= ~filter_box_height
2.default= 2.0
2.type= double
2.desc= The height of the roi.

3.name= ~min_diameter
3.default= 0.2
3.type= double
3.desc= The minimum diameter admissible for the cylindrical segmentation.

4.name= ~max_diameter
4.default= 0.35
4.type= double
4.desc= The maximum diameter admissible for the cylindrical segmentation.

5.name= ~normal_distance
5.default= 0.1
5.type= double
5.desc= Normal distance parameter of the cylindrical segmentation.

6.name= ~max_iterations
6.default= 10000
6.type= int
6.desc= Maximum number of iterations for the cylindrical segmentation.

7.name= ~distance_threshold
7.default= 0.05
7.type= double
7.desc= Distance threshold parameter of the cylindrical segmentation.
}
}

node.1 {
name=structure_mapper_node
desc=`structure_mapper_node` is a 3D structure mapper for climbing robots.
pub{
0.name= pole_structure
0.type= pole_structure_mapper/PoleStructure
0.desc= The output of the algorithm.

1.name= pole_structure_visualizer
1.type= visualization_msgs/Marker
1.desc= This allows to visually debug the output of the algorithm.
}
sub{
0.name= pole
0.type= pole_structure_mapper/PoleSectionStamped
0.desc= The output of the pole extractor algorithm.
}
param {
0.name= ~global_frame_id
0.default= map
0.type= string
0.desc= The global frame id.

1.name= ~diameter_threshold
1.default= 0.03
1.type= double
1.desc= The diameter threshold for matching two pole sections (in meters).

2.name= ~axis_threshold
2.default= 10.0
2.type= double
2.desc= The axis threshold for matching two pole sections (in degrees).

3.name= ~distance_threshold
3.default= 0.10
3.type= double
3.desc= The distance threshold for matching two pole sections (in meters).

4.name= ~length_threshold
4.default= 0.6
4.type= double
4.desc= The minimum length a pole section must have to be considered.

5.name= ~temporary_section_timeout
5.default= 30.0
5.type= double
5.desc= The lifespan of a temporary pole section.

6.name= ~num_of_temporary_sections
6.default= 10
6.type= int
6.desc= Number of pole sections required to turn a temporary section into a permanent one.
}
}
```



## Video

The following video shows the pole extractor and 3D stricture mapper
working in rviz.

[Youtube](https://www.youtube.com/watch?v=oBhnhtqXVkg)

## Tutorials

Coming soon\...

## Related Publications

Coming soon\...
