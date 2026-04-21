**DEPRECATED: Use
<http://www.pointclouds.org/documentation/tutorials/vfh_recognition.php>
instead.**

## Description

This package implements a variant of the global VFH (Viewpoint Feature
Histogram) descriptor, as presented in
[R.B. Rusu, G. Bradski, R. Thibaux, J. Hsu. Fast 3D Recognition and Pose Using the Viewpoint Feature Histogram, Proceedings of the 23rd IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Taipei, Taiwan, October 18-22, 2010](http://www.willowgarage.com/papers/fast-3d-recognition-and-pose-using-viewpoint-feature-histogram).

The computational steps usually are along the lines of:

-   point cloud cluster extraction (e.g., through segmentation)
-   estimation of surface normals at each point
-   estimation of VFH global descriptors (one per cluster)
-   build a kd-tree of VFH signatures in some metric space (e.g.,
    Chi-Square)
-   use the kd-tree for nearest neighbor searches to identify new
    (unseen) clusters.

## Demo

Assuming that the package is built, the **demos** subdirectory contains
a number of scripts that illustrate how to use VFH signatures for point
cloud cluster classification. A number of example datasets are already
bundled with the package and should be available in **demos/data**.

The following explains what every script in **demos** does:

-   *0.estimate_vfh_and_normals.sh* needs
    *estimate_normals_and_vfh.launch* launched first, e.g.:
    ```
$ roslaunch vfh_cluster_classifier estimate_normals_and_vfh.launch
``` and for a given directory containing point
    cloud clusters, it will estimate the surface normals and VFH global
    descriptors;
-   *0.estimate_vfh.sh* needs *estimate_vfh.launch* launched first,
    e.g.: ```
$ roslaunch vfh_cluster_classifier estimate_vfh.launch
``` and for a given directory containing
    point cloud clusters with surface normals at each point, it will
    estimate the VFH global descriptors;
-   *1.build_tree.sh* uses the estimated VFH global descriptors to build
    a kd-tree representation in some given metric space;
-   *2.nearest_neighbors.sh* uses the previously created kd-tree and
    displays the nearest neighbors in the chosen VFH metric space for
    one cluster per directory (from **demos/data**);
-   *3.view_histograms.sh* draws the VFH signatures for one cluster per
    directory (from **demos/data**).

For a quick test, just run: ```
$ bash 1.build_tree.sh
$ bash 2.nearest_neighbors.sh
``` in **demos**. You
should see something along the lines of:

![](attachment:ex1.jpg) ![](attachment:ex2.jpg)

Here, the inlier distance threshold was set to 100. All shapes with
distances larger than that are considered outliers.
