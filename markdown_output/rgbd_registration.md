![](attachment:img.jpg)

## Method

This algorithm consists of two main parts;

-   Extracting and matching 2D RGB features from the images
-   Performing a variant of ICP, or "Joint Optimization" incorporating
    both dense pointcloud information and 2D feature matches

The first step uses standard computer vision approaches to extract and
match features. Various extraction and matching methods may be
configured in the launch file. The feature points are then projected
into 3D space using the associated point clouds. RANSAC is used to find
a transformation that best fits the movement of 3D points between
frames. The outliers are discarded and the 3D locations' of the inliers
are used in the next step.

The next step is the variant of ICP. It combines both 3D visual features
(sparse points) and pointcloud data (dense points) by using the visual
features as distinct point correspondences. These correspondences are
assumed to be correct and not recalculated on each iteration. The
distance error function to minimize is a weighted combination of point
to point distance of the sparse distinct points and point to plane
distance of the dense points. The weighting can be changed by the
variable alpha which is a parameter of this implementation.

A more detailed description of this approach was in the 3D mapping paper
from Intel labs
[link](http://www.cs.washington.edu/robotics/projects/postscripts/3d-mapping-iser-10-final.pdf).
An evaluation of this approach can be found
[here](http://ias.cs.tum.edu/_media/spezial/bib/kidson12registration.pdf).

### Implementation

The feature extraction and matching has been implemented using opencv.
The RANSAC step uses some functions from PCL but is mostly implemented
in this package. The Joint Optimization was done by extending PCL's
registration module.

## Installation Instructions

```
git clone http://code.in.tum.de/git/mapping.git
cd mapping/rgbd_registration
make
```

The makefile will download some sample test data (130MB download) from
the internet. This can be disabled in the CMakeLists.txt

The test data is a sample from the
[RGB-D SLAM Dataset and Benchmark](http://vision.in.tum.de/data/datasets/rgbd-dataset).
There are 4 scenes with the presence or absences of texture and
structure.

## Usage

```
roslaunch rgbd_registration rgbd_registration.launch
```

The package has just one executable and is best started with the launch
file rgbd_registration.launch. The launch file handles file input and
output, debugging and algorithm parameters. This launch file contains
all the available parameters, their defaults and descriptions of what
they do.

The results can be found in the results directory. The transformed
pointcloud will be written here, along with other files as selected in
the launch file. The "source" pointcloud is transformed to the
"target". So to see the alignment one should view both the target and
transformed pointclouds together:

```
cd results
pcd_viewer target_cloud.pcd transformed_cloud.pcd
```

## ROS Parameters

Please consult rgbd_registration.launch for a full list of parameters
and descriptions
