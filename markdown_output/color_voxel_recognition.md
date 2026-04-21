## Description

This package provides sliding-box object detection application using
linear subspace method and Circular Color Cubic Higher-order Local
Auto-Correlation (C3-HLAC), which was proposed in
[A. Kanezaki, T. Suzuki, T. Harada & Y. Kuniyoshi. Fast Object Detection for Robots in a Cluttered Indoor Environment Using Integral 3D Feature Table, Proceedings of the 2011 IEEE International Conference on Robotics and Automation (ICRA2011), 2011](http://www.isi.imi.i.u-tokyo.ac.jp/~kanezaki/publications/icra2011_kanezaki.pdf).

Please also see our project page
[here](http://www.isi.imi.i.u-tokyo.ac.jp/en/project/3d_world_recognition.htm).

## Demo

[Youtube](https://www.youtube.com/watch?v=ySNAxUvZgYM)

### Get color point cloud

This application works with Kinect. Please install
[openni_kinect](http://www.ros.org/wiki/openni_kinect) package, first.
Connect Kinect and start to get color point could:
```
$ roslaunch openni_camera openni_node.launch
```

### Three steps for object detection application

**1. learn the environment** ```
$ bash `rospack find color_voxel_recognition`/demos/SH/learn_env.sh
``` Press \"Enter\"
key for saving data, and \"Ctrl+C\" ONLY ONCE for quit. (This step is
necessary for only once.)

**2. learn objects** ```
$ bash `rospack find color_voxel_recognition`/demos/SH/learn_obj.sh <object_name>
``` Put the target object
closest from Kinect and confirm the green box contains only the object.
Press \"Enter\" key for saving data, and \"Ctrl+C\" ONLY ONCE for quit.
(This step is necessary once for each object.)

**3. detect one object** ```
$ bash `rospack find color_voxel_recognition`/demos/SH/detect_test.sh <object_name> <similarity_threshold> <bounding_box_size>
``` *similarity_threshold*
should be between 0 and 1. *bounding_box_size* should be given in metric
unit.
