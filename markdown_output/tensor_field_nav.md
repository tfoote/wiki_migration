## Introduction

Tensor_field_nav package is developed for autonomous mapping of unknown
indoor scenes by a mobile robot holding an RGBD camera. The key idea is
to utilize 2D directional fields to guide robot movement. We compute and
update a geometry-aware tensor field constrained by the currently
reconstructed scene. The 3D scene geometry (i.e., the known surfaces) is
projected to the floor plane. A set of 2D tangential constraints along
the projected boundaries is extracted and used to compute/update the
tensor field. The robot path is formed by particle advection over the
tensor field, which is inherently obstacle avoiding.

During online scanning, the tensor field is updated in real-time,
conforming to the incrementally reconstructed scene. To ensure a smooth
robot path when advecting over the time-varying field, we propose a
space-time optimization of tensor fields via imposing both spatial
smoothness and temporal coherence. There are several important
advantages of tensor field guided navigation. First, tensor fields are
orientation-free and thus contain much less singularities (degenerate
points), as compared to vector fields which are predominantly used in
the literature. Fewer singularities lead not only to smoother path
advection, which is critical for quality reconstruction, but also to
more efficient navigation due to less ambiguity. In addition, tensor
fields are sink-free, avoiding the issue of local trapping. Most
importantly, the topological skeleton of a tensor field, comprised of
all degenerate points and the separatrices connecting them, can be
viewed as a routing graph. With this global structure, one can achieve
global path planning for efficient scene scanning.

## Overview

Our tensor_field_nav package is composed of five sub-packages:

1\) **octomap_tensor_field** for mapping based on
[Octomap](https://octomap.github.io/%Octomap)

2\) **odom_tf_publish** for monitoring robot position

3\) **pure_pursuit_controller** for controlling robot movement

4\) **rviz_textured_quads** for visualizing tensor field in rviz

5\) **tensor_field_nav_core** is the core sub-package of our method used
for computing and updating tensor field and achieving field-guided robot
exploration and scanning.

## Contributors and Publication

The contributors to this package are Lintao
Zheng(lintaozheng1991@gmai.com) and Kai Xu(kevin.kai.xu@gmail.com). This
method has been published at SIGGRAPH Asia 2017. Please refer to
[the project page](http://kevinkaixu.net/projects/tfnav.html). If you
find the package useful, please consider citing the following paper:

```
@article {xu_siga16,
    title = {Autonomous Reconstruction of Unknown Indoor Scenes Guided by Time-varying Tensor Fields},
    author = {Kai Xu and Lintao Zheng and Zihao Yan and Guohang Yan and Eugene Zhang and Matthias Niessner and Oliver Deussen and Daniel Cohen-Or and Hui Huang},
    journal = {ACM Transactions on Graphics (Proc. of SIGGRAPH Asia 2017)},
    volume = {36},
    number = {6},
    pages = {Article No. ??},
    year = {2016}
}
```

## Download and Install

### Dependencies

This package depends on CUDA and OpenCV. Please install these two
libraries first. CUDA version 7.5 and OpenCV 2.4.8 version were tested
and thus recommended.

### From source

Please download the source code from: ```
git clone https://github.com/zlt1991/tensor_field_nav.git
``` then
```
catkin_make
```

## Run

```
$ roslaunch tensor_field_nav_core complete_run.launch
$ roslaunch octomap_tensor_field octomap_mapping.launch
```

## Acknowledgements

The implementation of our tensor field navigation is based on the code
of tensor field design provided by Eugene Zhang. If you use this code,
please also cite the following paper:

```
@article{zhang2007interactive,
  title={Interactive tensor field design and visualization on surfaces},
  author={Zhang, Eugene and Hays, James and Turk, Greg},
  journal={IEEE Transactions on Visualization and Computer Graphics},
  volume={13},
  number={1},
  year={2007},
  publisher={IEEE}
}
```
