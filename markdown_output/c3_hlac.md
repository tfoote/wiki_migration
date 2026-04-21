## Description

Circular Color Cubic Higher-order Local Auto-Correlation (C3-HLAC) is an
efficient descriptor extracted from color voxel data, as presented in
[A. Kanezaki, T. Suzuki, T. Harada & Y. Kuniyoshi. Fast Object Detection for Robots in a Cluttered Indoor Environment Using Integral 3D Feature Table, Proceedings of the 2011 IEEE International Conference on Robotics and Automation (ICRA2011), 2011](http://www.isi.imi.i.u-tokyo.ac.jp/~kanezaki/publications/icra2011_kanezaki.pdf).
It is obtained as a 981-dimensional histogram, where each bin is
differentiated by the RGB color space and the relative position of the
two neighboring voxels.

Please also see our project page
[here](http://www.isi.imi.i.u-tokyo.ac.jp/en/project/3d_world_recognition.htm).

## Usage



```
$ rosrun c3_hlac example_c3_hlac `rospack find c3_hlac`/data/sample.pcd
```



This executable reads color point cloud "sample.pcd" and writes its
C3-HLAC descriptor into "c3_hlac.pcd" in the current directory.

If you have pcl_visualization, you can see the histogram by:


```
$ rosrun pcl_visualization pcd_viewer c3hlac.pcd
```


