## camera_self_filter

-   camera_self_filter: The camera_self_filter node renders the mesh
    model of its current configuration into a camera view. It publishes
    a binary mask image stream and optionally the original camera image
    with the binary mask in the alpha channel as shown below. *Note: The
    node requires an X-server to render the mask. It is recommended to
    run it on an external Ubuntu desktop machine with OpenGL enabled
    graphics. If the node is to be run on the PR2 check out
    pr2_camera_self_filter package.*

```{=html}
<!-- -->
```
-   camera_self_filter_server: Does the same as the camera_self_filter
    node but does not stream constantly, but rather creates a service
    that returns the binary mask of the robot configuration for the
    requested time_stamp.

```{=html}
<!-- -->
```
-   image_view: A modified version of image_view to display the
    overlayed image. 

```
rosrun camera_self_filter image_view image:=/wide_stereo/left/image_rect_color_alpha_masked
```



[![\|width=640px](attachment:overlayed_image.jpg)](attachment:overlayed_image.jpg)

-   The mask can be displayed running 

```
rosrun image_view image_view image:=/wide_stereo/left/self_mask
```



[![\|width=640px](attachment:mask.jpg)](attachment:mask.jpg)

### launch

Example launch file:



```
<node pkg="camera_self_filter" type="camera_self_filter"  
 name="camera_self_filter_wide_stereo_left" output="screen">
   <param name="camera_frame" type="string" value="wide_stereo_optical_frame" />
   <param name="camera_topic" type="string" value="/wide_stereo/left" />
   <param name="publish_mask" type="bool" value="true" />
   <param name="publish_alpha" type="bool" value="true" />
   <param name="inverted" type="bool" value="false" />
   <param name="robot_description_package_path" type="string" 
     value="$(find pr2_description)" />
		
</node>
```



Note that the camera_self_filter node expects the robot urdf on the
parameter server. If has not been loaded automatically (for instance
when replaying a .bag file), set the "robot_description" parameter
manually (e.g. run "cat robot.urdf \| xargs rosparam set
robot_description").
