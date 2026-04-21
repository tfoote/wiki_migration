## datamatrix: tf frames from vision the easy way

![](attachment:crt_camera.jpg) ![](attachment:crt_rviz.jpg)

datamatrix subscribes to a stereo camera, looks for coded markers, and
publishes the pose of any markers it finds as [tf](tf) frames.

To use it, you:

-   print out some markers with 3-letter names of your choice
-   run the datamatrix node for the camera
-   put the markers in a visible place
-   start using the new [tf](tf) frames

### printing markers

Use the makeps.py script in datamatrix:

`$ rosrun datamatrix makeps.py CRT | lpr`

Usage:



```
Usage: makeps.py [options] code

Options:
  -h, --help            show this help message and exit
  -s SIZE, --size=SIZE  size of marker in m, default is .1
  -o OUT, --out=OUT     output filename, default is standard output
```



### running the node

Takes a single parameter stereo as the base camera topic:

`$ rosrun datamatrix datamatrix.py stereo:=/wide_stereo`

Or in monocular mode:

`$ rosrun datamatrix datamatrix.py image_stream:=/wide_stereo/left/image_rect camera_info:=/wide_stereo/left/camera_info `
