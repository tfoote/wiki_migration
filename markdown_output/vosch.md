## Description

Voxelized Shape and Color Histograms (VOSCH) is an efficient
rotation-invariant descriptor extracted from color voxel data. It is
obtained as a 137-dimensional histogram, where each bin is represented
by local correlations of surface normal types or RGB color values.

Thus the descriptor enables object classification and identification
considering both shape and color characteristics. It can be used with
any type of classifier, e.g., Support Vector Machine (SVM) or Linear
Subspace Method (LSM).

![](attachment:vosch.png)

## Install



```
git clone git://github.com/kanezaki/isi-ros-pkg.git
git clone http://code.in.tum.de/git/mapping.git
```



## Usage



```
$ rosrun vosch example_vosch `rospack find vosch`/data/sample_cone_green.pcd
```

 This executable reads color point cloud
"sample_cone_green.pcd" and writes its VOSCH descriptor into
"vosch.pcd" in the current directory.

If you have pcl_visualization, you can see the histogram by:



```
$ rosrun pcl_visualization pcd_viewer vosch.pcd
```

 ![](attachment:vosch_cone.png)
![](attachment:vosch_torus.png)

## The Code

The following code (test/example_vosch.cpp) snippet will estimate a set
of VOSCH features for all the points in the input dataset.

<<GetCode(<http://code.in.tum.de/indefero/index.php//p/mapping/source/file/master/vosch/test/example_vosch.cpp,cplusplus>)>>

If you use the following two lines instead of the corresponding lines in
above example code, you can get a set of VOSCH feature vectors extracted
from the subdivisions of 10x10x10 voxel grid with 5x5x5 overlapping
respectively:



```
std::vector< std::vector<float> > vosch;
extractVOSCH( grid, cloud, cloud_downsampled, vosch, 127, 127, 127, voxel_size, 10, 5, 5, 5 );
```


