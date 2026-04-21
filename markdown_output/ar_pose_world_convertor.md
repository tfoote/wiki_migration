## Description

This package adds a given TF transformation to a AR marker message. This
allows the user to add the camera to world TF to the marker to camera
transformation. An example of the use of this package can be found in
the ar_pose_demo package.

## Use in launch file



```
<!-- Static TF from each of the camera's to the world -->
   	<node pkg="tf" type="static_transform_publisher" name="world_to_cam_322" args="0.46 0 0 0 0 0 world gc655c_322 10" />

	<node pkg="ar_pose_world_convertor" type="ar_pose_world_convertor" respawn="false" name="ar_pose_world_convertor_322" >
    		<param name="first_frame" type="string" value="world" />
    		<param name="second_frame" type="string" value="ar_pose_marker_322" />
    		<param name="marker_topic" type="string" value="ar_pose_marker_322" />
  	</node>
```


