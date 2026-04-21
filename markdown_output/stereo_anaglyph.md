## Samples

  -- -- -- --------------------------------------------------------------------------- -- -- --
           <style="text-align: center;"> ![](attachment:table_top.png)                   
           <style="text-align: center;"> A table top scene during teleoperation.         
  -- -- -- --------------------------------------------------------------------------- -- -- --

  -- -- -- ----------------------------------------------------------------------------- -- -- --
           <style="text-align: center;"> ![](attachment:room_narrow.png)                   
           <style="text-align: center;"> A view through the narrow stereo cameras.         
  -- -- -- ----------------------------------------------------------------------------- -- -- --

## Requirements

-   A functioning ROS install, and checked out copy of gt-ros-pkg.
-   Images captured by a stereo pair published on topics:
    /CAMERA_NAME/left/image_rect_color and
    /CAMERA_NAME/right/image_rect_color
-   [Red-cyan stereo glasses](http://www.berezin.com/3d/3dglasses.htm).

## Running

If you are on a machine configured to communicate with a PR2, run this
node by executing: 

```
rosrun stereo_anaglyph red-cyan-anaglyph.py -d /wide_stereo -d 20
```

 If you are not on a PR2,
replace `/wide_stereo` with a topic of your choice. The -d option here
controls the separation distance. To get a feel for what this should be,
launch the node then press the left and right arrow key while the
`stereo-anaglyph` window has focus. The goal here is to control the
image separation such that the disparity presented to you eye is not too
large. A large disparity typically results in seeing double instead of
true depth.

  -- -- -- -------------------------------------------------------------------------- -- -- --
           <style="text-align: center;"> ![](attachment:room_wide.png)                  
           <style="text-align: center;"> Typical images from from /wide_stereo.         
  -- -- -- -------------------------------------------------------------------------- -- -- --

One thing to note on the `/wide_stereo` images is that it'll be
difficult to adjust the disparity such that subjects far away and
subjects close up has appropriate disparity for stereo integration. This
is a known limitation of the system.

### Tweak for Higher Frame Rates

To view video at higher frame rates interleave two
[republish](http://www.ros.org/wiki/image_transport#republish) nodes,
one for each image stream. The two launch files provided
`pr2_narrow_stereo_view.launch` and `pr2_wide_stereo_view.launch`
does this by default. Run them with the command:



```
roslaunch stereo_anaglyph pr2_wide_stereo_view.launch
```

 For reference, this launch file contains:



```
<launch>
    <node pkg="image_transport" name="left_cam_republish_wide"  type="republish" args="theora in:=/wide_stereo/left/image_rect_color raw out:=/wide_stereo_raw/left/image_rect_color" respawn="true"/>
    <node pkg="image_transport" name="right_cam_republish_wide" type="republish" args="theora in:=/wide_stereo/right/image_rect_color raw out:=/wide_stereo_raw/right/image_rect_color" respawn="true"/>
    <node pkg="stereo_anaglyph" name="anaglyph_view_wide" type="red-cyan-anaglyph.py" args="-c /wide_stereo_raw -d 56"/>
</launch>
```



## Command Line Interface



```
./red-cyan-anaglyph.py --help
Usage: red-cyan-anaglyph.py [options]

Options:
  -h, --help  show this help message and exit
  -c CAM      which camera to listen to
  -d DIST     separation distance
```



## ROS API



```clearsilver
name=red_cyan_anaglyph.py
desc=Displays images in red-cyan anaglyph mode
sub {
 0.name = /CAMERA_NAME/left/image_color_rect
 0.type = sensor_msgs/Image
 0.desc = left image

 1.name = /CAMERA_NAME/right/image_color_rect
 1.type = sensor_msgs/Image
 1.desc = right image
 }
```


