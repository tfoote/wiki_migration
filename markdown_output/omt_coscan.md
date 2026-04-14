## Introduction

The omt_coscan package is designed for the collaborative scanning of
unknown environments driven by Optimal Mass Transport(OMT) using
multiple RGBD cameras. The key idea is to formulate the collaborative
scanning task as a resource distribution problem. We solve the problem
by a tailored OMT algorithm to achieve high scanning coverage while
keeping low scanning effort.

## Overview

The package consists of three sub-packages:

1\) \'\'\'co_scan\'\'\' for the core algorithm

2\) \'\'\'srbot_description\'\'\' for robot(RGBD sensor) params

3\) \'\'\'virtual_scan\'\'\' for the simulator of virtual scanning using
Gazebo.

## Contributors and Publication

The contributors to this package are Siyan Dong(siyandong.3@gmail.com),
Kai Xu(kevin.kai.xu@gmail.com) and Qiang Zhou(bamboosdu@gmail.com). This
method has been published at SIGGRAPH 2019. Please refer to
<https://kevinkaixu.net/projects/multirobot.html>. If you find the
package helpful for your research, please consider citing the following
paper: ```
@article{dong2019multi,
  title={Multi-robot collaborative dense scene reconstruction},
  author={Dong, Siyan and Xu, Kai and Zhou, Qiang and Tagliasacchi, Andrea and Xin, Shiqing and Nie{\ss}ner, Matthias and Chen, Baoquan},
  journal={ACM Transactions on Graphics (TOG)},
  volume={38},
  number={4},
  pages={84},
  year={2019},
  publisher={ACM}
}
```

## Download and Install

### Dependencies

This package depends on OpenCV, CGAL and OctoMap. Please install these
libraries first.

### From Source

Please download the source code: ```
catkin_ws/src$ git clone https://github.com/siyandong/CoScan.git
``` Modify the
direcrotries of OpenCV, CGAL and OctoMap in CMakeLists.txt. Then
```
catkin_ws$ catkin_make_isolated
```

## Run

```
catkin_ws$ roslaunch virtual_scan simulator.launch
catkin_ws$ roslaunch virtual_scan data_sever.launch
catkin_ws$ rosrun co_scan co_scan
```
