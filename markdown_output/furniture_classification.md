## Description

This package provides tools to recognize and classify furniture in
Kinect captured scenes using user provided CAD models. The process
consists of generating pointclouds from mesh models, training classifier
using generated data and classifying furniture in a scene. The approach
is described in the paper by Mozos and Marton,
[Furniture Models Learned from the WWW \-- Using Web Catalogs to Locate and Categorize Unknown Furniture Pieces in 3D Laser Scans](http://ias.in.tum.de/_media/spezial/bib/mozos11furniture.pdf).

![](attachment:chairAndTable.png)

## Install

### Electric

You need perception_pcl_electric_unstable stack to run this code. First
check out perception_pcl_electric_unstable in some directory on your
computer. 

```
$ svn co http://svn.pointclouds.org/ros/branches/electric/perception_pcl_unstable/
```



Add the directory where you downloaded perception_pcl_electric_unstable
to the beginning of ROS_PACKAGE_PATH. You can do it by adding this line
to /.bashrc



```
ROS_PACKAGE_PATH=/your_install_dir:$ROS_PACKAGE_PATH
```



Then build pcl by running rosmake in perception_pcl_electric_unstable
directory.

You also need to download mapping stack into a directory, which is in
your ROS_PACKAGE_PATH and build furniture_classification package.


```
$ git clone -b electric http://code.in.tum.de/git/mapping.git
$ rosmake furniture_classification
```



### Fuerte

You need pcl17 package to run this code. First check out
perception_pcl_unstable in some directory on your computer.


```
$ svn co http://svn.pointclouds.org/ros/branches/fuerte/perception_pcl_unstable/
```



Add the directory where you downloaded perception_pcl_unstable to the
beginning of ROS_PACKAGE_PATH. You can do it by adding this line to
/.bashrc



```
ROS_PACKAGE_PATH=/your_install_dir:$ROS_PACKAGE_PATH
```



Then build pcl17 by running 

```
$ rosmake pcl17
```



You also need to download mapping stack into a directory, which is in
your ROS_PACKAGE_PATH and build furniture_classification package.


```
$ git clone http://code.in.tum.de/git/mapping.git
$ rosmake furniture_classification
```



## Usage

First create a directory where you want to save results and cd to it.
After that run following commands:



```
$ rosrun furniture_classification scan -input_dir `rospack find furniture_classification`/data/models/ -output_dir scans/ -height 3 -noise_std 0.07 -distance 4 -tilt -30 -shift 0 -num_views 12
```

 This executable generates partial view
pointclouds for CAD models stored in data/models/ and saves them into
scan folder. Expected directory stucture is Class_Name/Model_Name.vtk
(Example: Chairs/Big_Chair.vtk)



```
$ rosrun furniture_classification train -input_dir scans/ -output_dir database/ -num_clusters 40 -features sgf
```

 This executable generates classifier database
from partial view scans found in scans/ folder and saves it to
database.yaml



```
$ rosrun furniture_classification classify -database_dir database/ -scene_file_name `rospack find furniture_classification`/data/test/scenes/chairAndDesk1.pcd -features sgf
```



This executable finds and classifies furniture in a scene specified
using classifier from database.yaml. Result is stored in
scene_name/result/ (in this case chairAndDesk1/result/)

You can view result by executing 

```
ROS_PACKAGE_PATH=/your_install_dir:$ROS_PACKAGE_PATH
```

0

![](attachment:result.png)

You can also try live version if you have Kinect.

First start Kinect 

```
ROS_PACKAGE_PATH=/your_install_dir:$ROS_PACKAGE_PATH
```

1

Then run classify_live executable. Point your Kinect to a scene. In the
scene the floor should be visible, because it is used for alignment.
Press 'c' to start classification process. 

```
ROS_PACKAGE_PATH=/your_install_dir:$ROS_PACKAGE_PATH
```

2
